.. meta::
   :title: Upgrading Galera Cluster Software
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :ref:`Rolling Upgrade <rolling-upgrade>`
      - :ref:`Bulk Upgrade <bulk-upgrade>`
      - :ref:`Provider Upgrade <provider-upgrade>`
      - :ref:`gcache.size <gcache.size>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`upgrading`:

==========================
Upgrading Galera Cluster
==========================

Since high-availability is a priority for many Galera Cluster administrators, how to go about upgrading the nodes is important. Doing so with the least amount of downtime is tricky.  There are three methods for upgrading Galera Cluster, the Galera software on the individual nodes:

.. rst-class:: soft-list

   - :ref:`Rolling Upgrade <rolling-upgrade>` permits you to upgrade one node  at a time, without taking down the cluster |---| and newly upgraded nodes can join the cluster without problems.

   - :ref:`Bulk Upgrade <bulk-upgrade>` is the method by which you take down the cluster and upgrade all of the nodes together.

   - :ref:`Provider Upgrade <provider-upgrade>` is a method in which you only upgrade the Galera Replication Plugin on each node.

There are advantages and disadvantages to each of these methods.  For instance, while a rolling upgrade may prove time consuming, the cluster continues to run during the upgrades.  Similarly, while a bulk upgrade is faster, depending on on your situation, problems can result from taking down the cluster for a longer period of time.  You will have to choose the best method for your situation, needs and concerns.


.. _`rolling-upgrade`:
.. rst-class:: rubric-1
.. rubric:: Rolling Upgrade

When you need the cluster to remain live and do not mind the time it takes to upgrade each node, use rolling upgrades.

In rolling upgrades, you take each node down individually, upgrade its software and then restart the node.  When the node reconnects, it brings itself back into sync with the cluster, as it would in the event of any other outage.  Once the individual finishes syncing with the cluster, you can move to the next in the cluster.

The main advantage of a rolling upgrade is that in the even that something goes wrong with the upgrade, the other nodes remain operational, giving you time to troubleshoot the problem.

Some of the disadvantages to consider in rolling upgrades are:

.. rst-class:: verbose-list

   **Time Consumption** Performing a rolling upgrade can take some time, longer depending on the size of the databases and the number of nodes in the cluster, during which the cluster operates at a diminished capacity.

   Unless you use :term:`Incremental State Transfer`, as you bring each node back online after an upgrade, it initiates a full :term:`State Snapshot Transfer`, which can take a long time to process on larger databases and slower state transfer methods.

   During the State Snapshot Transfer, the node continues to accumulate catch-up in the replication event queue, which it will then have to replay to synchronize with the cluster.  At the same time, the cluster is operational and continues to add further replication events to the queue.

   **Blocking Nodes** When the node comes back online, if you use ``mysqldump`` for State Snapshot Transfers, the donor node remains blocked for the duration of the transfer.  In practice, this means that the cluster is short two nodes for the duration of the state transfer, one for the donor node and one for the node in catch-up.

   Using ``xtrabackup`` or ``rsync`` with the LVM state transfer methods, you can avoid blocking the donor, but doing so may slow the donor node down.

   Depending on the load balancing mechanism, you may have to configure the load balancer not to direct requests at joining and donating nodes.

   **Cluster Availability** Taking down nodes for a rolling upgrade can greatly diminish cluster performance or availability, such as if there are too few nodes in the cluster to begin with or where the cluster is operating at its maximum capacity.

   In such cases, losing access to two nodes during a rolling upgrade can create situations where the cluster can no longer serve all requests made of it or where the execution times of each request increase to the point where services become less available.

   **Cluster Performance** Each node you bring up after an upgrade, diminishes cluster performance until the node buffer pool warms back up.  Parallel applying can help with this.

.. _`rolling-upgrade-steps`:
.. rst-class:: rubric-3
.. rubric:: Rolling Upgrade Procedure

Assuming you've read and considered the above, below are the steps for upgrading each node in a cluster |---| one at a time. This procedure, though, is for minor upgrades, not major upgrades.  For those, see the next section.

.. rst-class:: slight-list

   - First, transfer all client connections from the node you're about to upgrade to the other nodes.

   - When there are no more client connections trying to access the node, shut down the database software (i.e., ``mysqld``). This will remove the node from the cluster.

   - Now use the method you prefer to upgrade the software.  A package management utility such as ``yum``, or whatever is appropriate for the your operating system distribution.

   - When you've finished updating the database and Galera software, start the node. Check that it has successfully joined the cluster and finished synchronizing before beginning the process to upgrade another node in the cluster.

.. tip:: If you upgrade a node that will be part of a weighted quorum, set the initial node weight to zero.  This guarantees that if the joining node should fail before it finishes synchronizing, it won't affect any quorum computations that follow.


.. _`rolling-upgrade-major-versions`:
.. rst-class:: rubric-2
.. rubric:: Rolling Upgrades of Major Versions of Galera Cluster

Performing a rolling upgrade between major versions of Galera Cluster (e.g., from 5.6 to 5.7) has certain additional limitations.  Below is a list of them; you should consider these factors.

.. rst-class:: verbose-list

   SST is not supported between nodes of different major versions. Therefore, nodes of different major versions should not coexist in the same cluster for longer than necessary to perform the upgrade;

   Prior to performing the upgrade, ensure that the :ref:`gcache.size <gcache.size>` provider option on all nodes is sized so that it can provide IST for the expected duration of the upgrade;

   While the cluster contains nodes of multiple versions, avoid running any statements that are only supported in a particular version or statements that have different effect in different versions. For example, do not run DDL statements that are only available in the newer version.


.. _`rolling-major-upgrade-steps`:
.. rst-class:: rubric-3
.. rubric:: Rolling Major Upgrade Procedure

Below are the steps of the following procedure for performing rolling upgrades between major versions of Galera Cluster.

.. rst-class:: slight-list

   - Choose one node to upgrade and make sure that all client connections are directed elsewhere.  Once it's free of its cluster obligations, shut down the database daemon (e.g., ``mysqld``).

   - Edit the database configuration file (i.e., ``my.cnf``) and temporarily comment out the ``wsrep_provider`` line. This will prevent the node from attempting to rejoin the cluster during the package upgrade process.

   - Uninstall all existing ``mysql-wsrep`` packages and install the new packages using a package manager (e.g., ``yum``)

   - Start the ``mysqld`` daemon |---| without connecting to the cluster |---| and then run the ``mysql_upgrade`` script, if it wasn't run automatically as part of package installation.

   - Last, restore the ``wsrep_provider`` line in the database configuration and restart the ``mysqld`` daemon.


.. _`bulk-upgrade`:
.. rst-class:: rubric-1
.. rubric:: Bulk Upgrade

When you want to avoid time-consuming state transfers and the slow process of upgrading each node, one at a time, use a bulk upgrade.

In bulk upgrades, you take all of the nodes down in an idle cluster, perform the upgrades, then bring the cluster back online.  This allows you to upgrade your cluster quickly, but does mean a complete service outage for your cluster.

.. warning:: Always use bulk upgrades when using a two-node cluster, as the rolling upgrade would result in a much longer service outage.

The main advantage of bulk upgrade is that when you are working with huge databases, it is much faster and results in better availability than rolling upgrades.

The main disadvantage is that it relies on the upgrade and restart being quick.  Shutting down InnoDB may take a few minutes as it flushes dirty pages.  If something goes wrong during the upgrade, there is little time to troubleshoot and fix the problem.

.. note:: To minimize any issues that might arise from an upgrade, do not upgrade all of the nodes at once.  Rather, run the upgrade on a single node first.  If it runs without issue, upgrade the rest of the cluster.

To perform a bulk upgrade on Galera Cluster, complete the following steps:

#. Stop all load on the cluster

#. Shut down all the nodes

#. Upgrade software

#. Restart the nodes. The nodes will merge to the cluster without state transfers, in a matter of seconds.

#. Resume the load on the cluster

.. note:: You can carry out steps 2-3-4 on all nodes in parallel, therefore reducing the service outage time to virtually the time needed for a single server restart.


.. _`provider-upgrade`:
.. rst-class:: rubric-1
.. rubric:: Provider-Only Upgrade

.. index::
   pair: Parameters; wsrep_cluster_address

When you only need to upgrade the Galera provider, you can further optimize the bulk upgrade to only take a few seconds.

.. important:: In provider-only upgrade, the warmed up InnoDB buffer pool is fully preserved and the cluster continues to operate at full speed as soon as you resume the load.


.. _`upgrade-plugin`:
.. rst-class:: rubric-2
.. rubric:: Upgrading Galera Replication Plugin

If you installed Galera Cluster for MySQL using the binary package from the Codership repository, you can upgrade the Galera Replication Plugin through your package manager..

To upgrade the Galera Replicator Plugin on an RPM-based Linux distribution, run the following command for each node in the cluster:

   .. code-block:: console

      $ yum update galera

To upgrade the Galera Replicator Plugin on a Debian-based Linux distribution, run the following commands for each node in the cluster:

   .. code-block:: console

      $ apt-get update
      $ apt-get upgrade galera

When ``apt-get`` or ``yum`` finish, you will have the latest version of the Galera Replicator Plugin available on the node.  Once this process is complete, you can move on to updating the cluster to use the newer version of the plugin.


.. _`updating-galera-cluster`:
.. rst-class:: rubric-2
.. rubric:: Updating Galera Cluster

After you upgrade the Galera Replicator Plugin package on each node in the cluster, you need to run a bulk upgrade to switch the cluster over to the newer version of the plugin.

#. Stop all load on the cluster.

#. For each node in the cluster, issue the following queries:

   .. code-block:: mysql

      SET GLOBAL wsrep_provider='none';
      SET GLOBAL wsrep_provider='/usr/lib64/galera/libgalera_smm.so';

#. One any one node in the cluster, issue the following query:

   .. code-block:: mysql

      SET GLOBAL wsrep_cluster_address='gcomm://';

#. For every other node in the cluster, issue the following query:

   .. code-block:: mysql

      SET GLOBAL wsrep_cluster_address='gcomm://node1addr';

   For ``node1addr``, use the address of the node in step 3.

#. Resume the load on the cluster.

Reloading the provider and connecting it to the cluster typically takes less than ten seconds, so there is virtually no service outage.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
