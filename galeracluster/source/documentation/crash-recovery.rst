.. meta::
   :title: Crash Recovery
   :description:
   :language: en-US
   :keywords: galera cluster, streaming replication
   :copyright: Codership Oy, 2014 - 2021. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :ref:`Recovering Primary Component <pc-recovery>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`crash-recovery`:

============================
Crash Recovery
============================

A Galera Cluster works as one logical entity, controlling the status and consistency of its nodes as well as the status of the whole cluster. This allows maintaining the data integrity more efficiently than with asynchronous replication, without losing safe writes on multiple nodes at the same time.

.. only:: html

          .. image:: ../images/support.jpg
             :target: https://galeracluster.com/support/#galera-cluster-support-subscription

   .. only:: latex

          .. image:: ../images/support.jpg
		  :target: https://galeracluster.com/support/#galera-cluster-support-subscription


Nevertheless, scenarios may occur where the database service can stop with no node being able to serve requests. These scenarios are described in the sections that follow.


.. _`node-a-is-gracefully-stopped`:
.. rst-class:: section-heading
.. rubric:: Node 1 Is Gracefully Stopped

In a three-node cluster (nodes 1, 2 and 3), node 1 is gracefully stopped, for the purpose of maintenance, configuration change and so on.

In this case, the other nodes receive a “good bye” message from the stopped node and the cluster size is reduced; some properties like :term:`Quorum` calculation or auto increment are automatically changed. As soon as node 1 is started again, it joins the cluster based on its ``wsrep_cluster_address`` variable in ``my.cnf``.

If the writeset cache (``gcache.size``) on nodes 2 and/or 3 still has all the transactions executed while node 1 was down, joining is possible through :term:`IST`. If IST is impossible due to missing transactions in donor’s gcache, the fallback decision is made by the donor, and :term:`SST` is started automatically.


.. _`two-nodes-are-gracefully-stopped`:
.. rst-class:: section-heading
.. rubric:: Two Nodes Are Gracefully Stopped

As in :ref:`Node 1 Is Gracefully Stopped <node-a-is-gracefully-stopped>`, the cluster size is reduced to 1, even the single remaining node 3 forms the primary component and can serve client requests. To get the nodes back into the cluster, you just have to start them.

However, when a new node joins the cluster, node 3 will be switched to the “Donor/Desynced” state, as it has to provide the state transfer at least to the first joining node. It is still possible to read/write to it during that process, but it may be much slower, which depends on how large amount of data should be sent during the state transfer. Also, some load balancers may consider the donor node as not operational and remove it from the pool. So, it is best to avoid the situation when only one node is up.

If you restart node 1 and then node 2, ensure that node 2 does not use node 1 as the state transfer donor: node 1 may not have all the needed writesets in its gcache. Specify node 3 node as the donor in your configuration file and start the ``mysql`` service:

.. code-block:: console

   $ systemctl start mysql


.. _`all-three-nodes-are-gracefully-stopped`:
.. rst-class:: section-heading
.. rubric:: All Three Nodes Are Gracefully Stopped

The cluster is completely stopped and the problem is how to initialize it again. It is important that a node writes its last executed position to the ``grastate.dat`` file.

By comparing the seqno number in this file, you can see which is the most advanced node (most likely the last stopped). The cluster must be bootstrapped using this node, otherwise nodes that had a more advanced position will have to perform the full SST to join the cluster initialized from the less advanced one. As a result, some transactions will be lost). To bootstrap the first node, invoke the startup script like this:

For MySQL:

.. code-block:: console

   $ mysqld_bootstrap --wsrep-new-cluster

For PXC:

.. code-block:: console

   $ systemctl start mysql@bootstrap.service

For MariaDB:

.. code-block:: console

   $ galera_new_cluster


.. note:: Even though you bootstrap from the most advanced node, the other nodes have a lower sequence number. They will still have to join through the full SST, as the Galera Cache is not retained on restart.
          For this reason, it is recommended to stop writes to the cluster before its full shutdown, so that all nodes can stop at the same position. See also :ref:`pc.recovery <pc.recovery>`.


.. _`one-node-disappears-from-the-cluster`:
.. rst-class:: section-heading
.. rubric:: One Node Disappears from the Cluster

This is the case when one node becomes unavailable due to, for example, power outage, hardware failure, kernel panic, mysqld crash or ``kill -9`` on mysqld pid.

The two remaining nodes notice the connection to node 1 is down and start trying to re-connect to it. After several timeouts, node 1 is removed from the cluster. The quorum is saved (two out of three nodes are up), so no service disruption happens. After it is restarted, node 1 joins automatically, as described in :ref:`Node 1 Is Gracefully Stopped <node-a-is-gracefully-stopped>`.


.. _`two-nodes-disappear-from-the-cluster`:
.. rst-class:: section-heading
.. rubric:: Two Nodes Disappear from the Cluster

Two nodes are not available and the remaining node (node 3) is not able to form the quorum alone. The cluster has to switch to a non-primary mode, where MySQL refuses to serve any SQL queries. In this state, the "mysqld" process on node 3 is still running and can be connected to, but any statement related to data fails with an error.

.. code-block:: mysql

   mysql> select * from test.sbtest1;
   ERROR 1047 (08S01): WSREP has not yet prepared node for application use

Reads are possible until node 3 decides that it cannot access node 1 and node 2. New writes are forbidden.

As soon as the other nodes become available, the cluster is formed again automatically. If node 2 and node 3 were just network-severed from node 1, but they can still reach each other, they will keep functioning as they still form the quorum.

If node 1 and node 2 crashed, you need to enable the primary component on node 3 manually, before you can bring up node 1 and node 2. The command to do this is:

.. code-block:: mysql

   mysql> SET GLOBAL wsrep_provider_options='pc.bootstrap=true';

This approach only works, if the other nodes are down before doing that! Otherwise, you end up with two clusters having different data.



.. _`all-nodes-go-down-without-a-proper-shutdown-procedure`:
.. rst-class:: section-heading
.. rubric:: All Nodes Go Down Without a Proper Shutdown Procedure

This scenario is possible in the case of a datacenter power failure or when hitting a MySQL or Galera bug. Also, it may happen as a result of data consistency being compromised where the cluster detects that each node has different data. The ``grastate.dat`` file is not updated and does not contain a valid sequence number (seqno). It may look like this:.

.. code-block:: console

   $ cat /var/lib/mysql/grastate.dat
   # GALERA saved state
   version: 2.1
   uuid: 220dcdcb-1629-11e4-add3-aec059ad3734
   seqno: -1
   safe_to_bootstrap: 0

In this case, you cannot be sure that all nodes are consistent with each other. We cannot use ``safe_to_bootstrap`` variable to determine the node that has the last transaction committed as it is set to 0 for each node. An attempt to bootstrap from such a node will fail unless you start ``mysqld`` with the ``--wsrep-recover`` parameter:

.. code-block:: console

   $ mysqld --wsrep-recover

Search the output for the line that reports the recovered position after the node UUID (1122 in this case):

.. code-block:: mysql

   ...
   ... [Note] WSREP: Recovered position: 220dcdcb-1629-11e4-add3-aec059ad3734:1122
   ...

The node where the recovered position is marked by the greatest number is the best bootstrap candidate. In its ``grastate.dat`` file, set the ``safe_to_bootstrap`` variable to 1. Then, bootstrap from this node.

.. note:: After a shutdown, you can boostrap from the node which is marked as safe in the grastate.dat file.

          .. code-block:: mysql

             ...
             safe_to_bootstrap: 1
             ...

The ``pc.recovery`` option (enabled by default) saves the cluster state into a file named ``gvwstate.dat`` on each member node. As the name of this option suggests (pc – primary component), it saves only a cluster being in the PRIMARY state. An example content of a ``gvwstate.dat`` file may look like this:

.. code-block:: mysql

   cat /var/lib/mysql/gvwstate.dat
   my_uuid: 76de8ad9-2aac-11e4-8089-d27fd06893b9
   #vwbeg
   view_id: 3 6c821ecc-2aac-11e4-85a5-56fe513c651f 3
   bootstrap: 0
   member: 6c821ecc-2aac-11e4-85a5-56fe513c651f 0
   member: 6d80ec1b-2aac-11e4-8d1e-b2b2f6caf018 0
   member: 76de8ad9-2aac-11e4-8089-d27fd06893b9 0
   #vwend

We can see a three node cluster with all members being up. Thanks to this feature, the nodes will try to restore the primary component once all the members start to see each other. This makes the cluster automatically recover from being powered down without any manual intervention!


.. _`the-cluster-loses-its-primary-state-due-to-split-brain`:
.. rst-class:: section-heading
.. rubric:: The Cluster Loses its Primary State Due to Split Brain

Let’s assume that we have a cluster that consists of an even number of nodes: six, for example. Three of them are in one location while the other three are in another location and they lose network connectivity. It is best practice to avoid such topology: if you cannot have an odd number of real nodes, you can use an additional arbitrator (garbd) node or set a higher ``pc.weight`` to some nodes. But when the :term:`Split Brain` happens any way, none of the separated groups can maintain the quorum: all nodes must stop serving requests and both parts of the cluster will be continuously trying to re-connect.

If you want to restore the service even before the network link is restored, you can make one of the groups primary again using the same command as described in :ref:`Two Nodes Disappear from the Cluster <two-nodes-disappear-from-the-cluster>`.

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=true';

After this, you are able to work on the manually restored part of the cluster, and the other half should be able to automatically re-join using IST, as soon as the network link is restored.

.. warning:: If you set the bootstrap option on both the separated parts, you will end up with two living cluster instances, with data likely diverging away from each other. Restoring a network link in this case will not make them re-join until the nodes are restarted and members specified in configuration file are connected again.
             Then, as the Galera replication model truly cares about data consistency: once the inconsistency is detected, nodes that cannot execute row change statement due to a data difference – an emergency shutdown will be performed and the only way to bring the nodes back to the cluster is through the full SST.


This article is based on the blog post Galera replication - how to recover a PXC cluster by Przemysław Malkowski: `Galera replication – how to recover a PXC cluster <https://www.percona.com/blog/2014/09/01/galera-replication-how-to-recover-a-pxc-cluster/>`_

.. container:: bottom-links
