.. meta::
   :title: Maintaining a Two-Node Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`pc.boostrap <pc.bootstrap>`
      - :ref:`pc.ignore_sb <pc.ignore_sb>`
      - :ref:`Arbitrator <arbitrator>`


.. cssclass:: library-article
.. _`kb-best-two-node-clusters`:

=======================
Two-Node Clusters
=======================

.. rst-class:: article-stats

   Length: 880 words; Published: October 22, 2019; Category: Topology; Type: Best Practices

When using Galera Cluster, it's recommended that the cluster have at least three nodes.  However, some DBAs would prefer to use only two nodes.  This could be because their budget doesn't allow for the cost of a third production node.  Or it could be that they are putting together a cluster for testing updates and want to minimize the effort and expense of testing.

Whatever the reason for having only two nodes, there are some factors to consider, some preventive measures to take.  In a two-node cluster, when there is a conflicting pair of transactions, it could lead to a split-brain situation. Also, when one node fails, the remaining node will become non-operational. This KB article will explain how to address these possibilities.


.. rst-class:: section-heading
.. rubric:: Two Scenarios

For this KB article, we'll consider two scenarios.  The first scenario involves dealing with conflicting transactions in a two-node cluster.  Suppose each node executes a transaction which changes the same row in the same table at the same time.  Each node will vote for its transaction as being the superior one.  Normally, a third node would be called upon to cast the deciding vote. Without that tie-breaking vote, each node will commit their respective conflicting transaction. This is known as a split-brain. As more transactions occur, the data could continue to deviate, more conflicts can occur.

For the second scenario, suppose that one of the nodes in a two-node cluster, leaves the cluster, ungracefully.  For instance, it crashes or loses network connectivity.  When this happens, the other node becomes non-operational.  It will remain so until additional information is provided by a third entity, such as another node joining or an administrator intervening.

There's a reason for nodes becoming non-operational. If a node is separated from the cluster due to losing network connection, both nodes will think itself as being the :term:`Primary Component`.  Each will be unaware that the other is still running. This could cause problems once network connectivity is restored. To prevent this, the nodes become non-operational.


.. rst-class:: section-heading
.. rubric:: Recommendation |---| Scenario One

Let's look at how to resolve the potential problem with the first scenario above, one in which there are conflicting transactions and no tie-breaking vote.  The simplest solution is to use Galera Arbitrator.  It will be a member of the cluster and thereby participate in voting, but not in the actual replication.  It has its own daemon, ``garbd``, separate from the ``mysqld`` daemon.

To use Galera Arbitrator, you can either start it at the command-line with a set of options, or use the easier method of a configuration file. You can name this configuration file whatever you want and locate it wherever you want.  One possibility is to name it ``garbd.cnf`` and put it in the ``/etc`` directory, where the database configuration file is located. Below is an example of how the Arbitrator configuration file might look:

.. code-block:: text

   group="galera-testing"
   address="gcomm://172.31.30.39,172.31.18.53,172.31.26.106"

   options="gmcast.listen_addr=tcp://0.0.0.0:4444"
   log="/var/log/garbd.log"

You would set the ``name`` option to match the value given in the ``wsrep_cluster_name`` option in the database configuration file.  The ``address`` option would match the value given in the ``wsrep_cluster_address`` option.  The ``log`` option is to set the path and name of the log file.

You'll have to create an identical configuration file on each node, since you won't know which node is the one that will fail. Using the configuration file, to start the Galera Arbitrator daemon, you would execute something like the following at the command-line:

.. code-block:: text

   garbd --cfg /etc/garbd.cnf

This will start the ``garbd`` daemon,  using the options in the configuration file given.  You can add more options to the command-line here.  You'll have to execute this on each node. The ``garbd`` daemons will work together as one across the network.  If a node in a two-node cluster fails, the surviving node with the ``garbd`` daemon will remain operational since the node has the Arbitrator.


.. rst-class:: section-heading
.. rubric:: Recommendation |---| Scenario Two

To resolve the potential problem in the second scenario above, instead of using Galera Arbitrator, you can bootstrap the surviving node to form a new :term:`Primary Component`. You would do this by using the :ref:`pc.boostrap <pc.bootstrap>` wsrep Provider option.  To do so, log into the node using the ``mysql`` client and excute the following SQL statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

This will bootstrap the surviving node as a new Primary Component.  When the other node comes back online or regains network connectivity with this node, it will recognize that it's behind and initiate a state transfer to be synchronized.

Another solution, but a bad choice, is to configure the ``wsrep_provider_options`` parameter.  You would set it to use  :ref:`pc.ignore_sb <pc.ignore_sb>`.  This would allow it to continue to operate independently. To do so, you would log into the node with the ``mysql`` client and execute the following SQL statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.ignore_sb=TRUE';

The node will resume processing updates, even if it suspects a split-brain situation. Enabling :ref:`pc.ignore_sb <pc.ignore_sb>` is dangerous, though, in a multi-master setup due to the risk for split-brain situations.  However, it does simplify things in master-slave clusters |---| especially in situations with only two nodes.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
