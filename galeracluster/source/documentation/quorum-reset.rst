.. meta::
   :title: Resetting a Galera Cluster Quorum
   :description: "Provides an explanation of how determine if a cluster needs to be restarted and how to do it."
   :language: en-US
   :keywords: galera cluster, quorum, split-brain, recovery, primary component, restarting cluster
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
      - :ref:`wsrep_last_committed <wsrep_last_committed>`
      - :ref:`pc.bootstrap <pc.bootstrap>`
      - :ref:`wsrep_provider_options <wsrep_provider_options>`

      Related Articles


.. cssclass:: library-document
.. _`quorum-reset`:

======================
Resetting the Quorum
======================

.. index::
   pair: Parameters; wsrep_last_committed
.. index::
   pair: Parameters; wsrep_provider_options
.. index::
   pair: Parameters; pc.bootstrap
.. index::
   single: Split-brain; Recovery
.. index::
   single: Primary Component; Nominating

Although it's unlikely, you may find your nodes no longer consider themselves part of the :term:`Primary Component`.  There might have been a network failure; perhaps more than half of the cluster failed; or there is a split-brain situation.  In these cases, the node come to suspect that there is another Primary Component, to which they are no longer connected.

This loss of integrity can be a problem. When it occurs, the nodes will start to return an ``Unknown command`` error to all of queries they're given to execute: they simply stop performing their duties for fear of making the situation worse by becoming too out-of-sync with their true cluster.

You can see if this is happening by executing the ``SHOW STATUS`` statement and checking the :ref:`wsrep_cluster_status <wsrep_cluster_status>` status variable.  Specifically, this is done by executing the following SQL statement on each node:

.. code-block:: mysql

   SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_cluster_status | Primary |
   +----------------------+---------+

The return value ``Primary`` indicates that the node on which it was executed is part of the Primary Component.  When the query returns any other value it indicates that the node is part of a non-operational component.  If none of the nodes return the value ``Primary``, you need to reset the quorum.

Situations in which none of the nodes show they are part of the Primary Component are very rare.  If you discover one or more nodes wtih a value ``Primary``, it may indicate a problem with network connectivity, rather than a need to reset the quorum.  Investigate the connection possibility.  Once the nodes regain network connectivity they automatically resynchronize with the Primary Component.


.. _`finding-most-advanced-node`:
.. rst-class:: section-heading
.. rubric:: Finding the Most Advanced Node

Before you can reset the quorum, you need to identify the most advanced node in the cluster.  That is, you must find the node whose local database committed the last transaction.  Regardless of the method you use in resetting the quorum, this node should serve as the starting point for the new :term:`Primary Component`.

Identifying the most advanced node requires that you find the node with the highest sequence number (i.e., seqno).  You can determine this by checking the :ref:`wsrep_last_committed <wsrep_last_committed>` status variable. From the database client on each node, run the following query:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

The return value is the sequence number for the last transaction the node committed.  If the ``mysqld`` daemon is down, you can restart ``mysqld`` without starting Galera.  If you don't want to restart the databases, you may be able to ascertain the sequence number from the ``grastate.dat`` file, located in the data directory.

Once you've found the sequence numbers of each node, the one with the highest value is the most advanced one in the cluster.  Use that node as the starting point when bootstrapping the new Primary Component. This is explained in the next section here.


.. _`resetting-quorum`:
.. rst-class:: section-heading
.. rubric:: Resetting the Quorum

When you reset the quorum, what you're doing is bootstrapping the :term:`Primary Component` on the most advanced node you have available.  This node then functions as the new Primary Component, bringing the rest of the cluster into line with its state.

There are two methods available to you in this process: automatic and manual. The recommended one for a quorum reset is the automatic method.  Unlike the manual method, automatic bootstrapping preserve the write-set cache, or GCache, on each node.  What this means is that when the new Primary Component starts, some or all of the joining nodes can be provisioned quickly using the :term:`Incremental State Transfer` (IST) method, rather than the slower :term:`State Snapshot Transfer` (SST) method.


.. _`automatic-bootstrap`:
.. rst-class:: sub-heading
.. rubric:: Automatic Bootstrap

Resetting the quorum will bootstrap the :term:`Primary Component` onto the most advanced node.  With the automatic method, this is done by dynamically enabling :ref:`pc.bootstrap <pc.bootstrap>` through the :ref:`wsrep_provider_options <wsrep_provider_options>` through the database client |---| it's not done through the configuration file.  Once you set this option, it will make the node a new Primary Component.

To perform an automatic bootstrap, run the following command using the ``mysql`` client of the most advanced node:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

The node now operates as the starting node in a new Primary Component.  Nodes in nonoperational components that have network connectivity attempt to initiate incremental state transfers if possible, state snapshot transfers if not, with this node, bringing their own databases up-to-date.


.. _`manual-bootstrap`:
.. rst-class:: sub-heading
.. rubric:: Manual Bootstrap

Resetting the quorum bootstraps the :term:`Primary Component` onto the most advanced node.  With the manual method, this is done by shutting down the cluster |---| shutting down ``mysqld`` on all of the nodes |---| and then starting ``mysqld`` with Galera on each node, beginning with the most advanced one.

To bootstrap manually a cluster, first determine the most advanced node by executing the following from the command-line on each node:

.. code-block:: mysql

   mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_last_committed'"

Once you've determined which node has the highest sequence number, you can begin shutting down the cluster.  Just shut down ``mysqld`` on all of the nodes in the cluster |---| leaving the most advanced node until last.  For servers that use ``init``, enter the following from the command-line:

.. code-block:: console

   service mysql stop

For servers that use ``systemd``, execute instead this from the command-line:

.. code-block:: console

   systemctl stop mysql

You're now ready to start the cluster again.  Start the most advanced node with the ``--wsrep-new-cluster`` option |---| not the other nodes.  For servers that use ``init``, run the following command:

.. code-block:: console

   service mysql start --wsrep-new-cluster

For servers that use ``systemd`` and Galera Cluster 5.5 or 5.6, enter instead the following from the command-line:

.. code-block:: console

   systemctl start mysqld --wsrep-new-cluster

For MySQL servers that use ``systemd`` and at least version 5.7 of Galera Cluster, you can execute the following script from the command-line only on the first node:

.. code-block:: console

   mysqld_bootstrap


For MariaDB servers that use ``systemd``, you might try to execute the following script from the command-line |---| again, only on the first node:

.. code-block:: console

   galera_new_cluster


With that first node running and acting as Primary Component, you're not ready to start all of the other nodes in the cluster.  For servers that use ``init``, run the following command:

.. code-block:: console

   service mysql start

For servers that use ``systemd``, instead run this command:

.. code-block:: console

   systemctl start mysqld

Written into all of these scripts is the ``--wsrep-new-cluster`` option, but it's done with a certain finesse.  Whichever method or script you use, when the first node starts with the ``--wsrep-new-cluster`` option, it initializes a new cluster using the data from the most advanced state available from the previous cluster.  As the other nodes start, they connect to this node and request state snapshot transfers, to bring their own databases up-to-date.  In a short amount of time, they all should become synchronized and running smoothly.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
