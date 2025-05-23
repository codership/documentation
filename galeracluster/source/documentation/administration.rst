.. meta::
   :title: Galera Cluster Administration
   :description: A menu of pages on the administration and management of Galera Cluster.
   :language: en-US
   :keywords: galera cluster, mysql, mariadb, dba, admin, node provisioning
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


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

      - :doc:`Arbitrator <arbitrator>`
      - :doc:`auto-eviction`
      - :doc:`Backups <backup-cluster>`
      - :doc:`monitor`
      - :doc:`deployment`
      - :doc:`Flow Control <managing-fc>`
      - :doc:`system-tables`
      - :doc:`node-provisioning`
      - :doc:`Recover Primary <pc-recovery>`
      - :doc:`Reset Quorum <quorum-reset>`
      - :doc:`schema-upgrades`
      - :doc:`Scriptable SST <scriptable-sst>`
      - :doc:`security`
      - :doc:`sst`
      - :doc:`Streaming Replication <using-sr>`
      - :doc:`Upgrading Galera <upgrading>`

      Related Articles

      - :doc:`../training/tutorials/migrate`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`administration`:

===============================
Galera Cluster Administration
===============================

With the basics of how the cluster works and how to install and initialize it covered, this part begins a five part series on the administration and management of Galera Cluster.

The sections in this part relate to the administration of nodes and the cluster. :doc:`deployment`, covers how to use Galera Cluster in relation to your wider infrastructure, how to configure load balancers to work with the cluster and edge case deployments, such as running nodes in containers. The pages in :doc:`monitor` show how to keep tabs on the status of the cluster and automate reporting. :doc:`security` covers configuring Galera Cluster to work with firewalls, SELinux and SSL encryption. :doc:`../training/tutorials/migrate` how to transition from a standalone instance of MySQL, MariaDB or Percona XtraDB to Galera Cluster.

.. only:: html

          .. image:: ../../images/support.jpg
             :target: https://galeracluster.com/support/#galera-cluster-support-subscription
             :width: 740

   .. only:: latex

          .. image:: ../../images/support.jpg
		  :target: https://galeracluster.com/support/#galera-cluster-support-subscription

.. _`node-admin`:
.. rst-class:: section-heading
.. rubric:: Node Administration

Managing and administering nodes in Galera Cluster is similar to the administration and management of the standard standalone MySQL, MariaDB and Percona XtraDB database servers, with some additional features used to manage its interaction with the cluster. These pages cover the administration of individual nodes, how they handle write-set replication and schema updates, and the procedure for upgrading Galera Cluster software.

- :doc:`node-provisioning`

  The complete process of replicating data into a node so that it can operate as part of the Primary Component is called 'provisioning' the node. It ensures that the nodes update the local data, keeping it consistent with the state of the cluster. This section provides an overview to how nodes join the cluster and maintain their state through state transfers.

- :doc:`sst`

  When a node falls too far behind the cluster, they request State Snapshot Transfers from another node in order to bring its local database up to date with the cluster. This section provides a guide to each state transfer method Galera Cluster supports.

- :doc:`scriptable-sst`

  When nodes send and receive State Snapshot Transfers, they manage the process through external scripts that call the standard state transfer methods. If you require additional functionality than what is available by default, you can create a script to implement your own custom state snapshot transfer methods.

- :doc:`system-tables`

  When you install Galera Cluster, it creates a set of system tables in the ``mysql`` database, which it uses to store configuration information. Similar to how the underlying database server uses the ``performance_schema`` and ``information_schema``, Galera Cluster uses these tables to record information relevant to replication. This section provides a guide to what you will find in these tables and how you might query them for useful information about the status of the node and the cluster.

- :doc:`schema-upgrades`

  Statements that update the database schema, (that is, DDL statements), are non-transactional and as such won't replicate to the cluster through write-sets. This section covers different methods for online schema upgrades and how to implement them in your deployment.

- :doc:`upgrading`

  In order to upgrade Galera Cluster to a new version or increment of the software, there are a few additional steps you need to take in order to maintain the cluster during the upgrade. This section provides guides to different methods in handling this process.


.. _`cluster-admin`:
.. rst-class:: section-heading
.. rubric:: Cluster Administration

In addition to node administration, Galera Cluster also provides interfaces for managing and administering the cluster. These sections cover Primary Component recovery, managing Flow Control and Auto Eviction, as well as Galera Arbitrator and how to handle backups.


- :doc:`pc-recovery`

  When nodes establish connections with each other, they form components. The operational component in the cluster is called the Primary Component. This section covers a new feature in version 3.6 of Galera Cluster, which sets the nodes to save the Primary Component state to disk. In the event of an outage, once all the nodes that previously formed the Primary Component reestablish network connectivity, they automatically restore themselves as the new Primary Component.

- :doc:`quorum-reset`

  The Primary Component maintains :term:`Quorum` when most of the nodes in the cluster are connected to it. This section provides a guide to resetting the quroum in the event that the cluster becomes non-operational due to a major network outage, the failure of more than half the nodes, or a split-brain situation.

- :doc:`managing-fc`

  When nodes fall too far behind, Galera Cluster uses a feedback mechanism called Flow Control, pausing replication to give the node to process transactions and catch up with the cluster. This section covers the monitoring and configuration of Flow Control, in order to improve node performance.

- :doc:`auto-eviction`

  When Galera Cluster notices erratic behavior from a node, such as in the case of unusually delayed response times, it can initiate a process to remove the node permanently from the cluster. This section covers the configuration and management of how the cluster handles these Auto Evictions.

- :doc:`using-sr`

  When the node uses Streaming Replication, instead of waiting for the commit to replicate and apply transactions to the cluster, it breaks the transaction down into replication units, transferring and applying these on the replica nodes while the transaction is still open. This section provides a guide to how to enable, configure and utilize Streaming Replication.

- :doc:`arbitrator`

  Galera Arbitrator is a separate application from Galera Cluster. It functions as an additional node in quorum calculations, receives the same data as other node, but does not participate in replications. You can use it to provide an odd node to help avoid split-brain situations, or use it in generating consistent application state snapshots, in generating backups.

- :doc:`backup-cluster`

  Standard backup methods available to MySQL database servers fail to preserve Global Transaction ID's used by Galera Cluster. You can recover data from these backups, but they're insufficient in restoring nodes to a well-defined state. This section shows how to use state transfers to properly perform backups in Galera Cluster.

.. container:: bottom-links

   Related Documents

   - :doc:`Arbitrator <arbitrator>`
   - :doc:`auto-eviction`
   - :doc:`Backups <backup-cluster>`
   - :doc:`monitor`
   - :doc:`deployment`
   - :doc:`Flow Control <managing-fc>`
   - :doc:`system-tables`
   - :doc:`node-provisioning`
   - :doc:`Recover Primary <pc-recovery>`
   - :doc:`Reset Quorum <quorum-reset>`
   - :doc:`schema-upgrades`
   - :doc:`Scriptable SST <scriptable-sst>`
   - :doc:`security`
   - :doc:`sst`
   - :doc:`Streaming Replication <using-sr>`
   - :doc:`Upgrading Galera <upgrading>`

   Related Articles

   - :doc:`../training/tutorials/migrate`


.. toctree::
   :maxdepth: 2
   :hidden:

   node-provisioning
   sst
   scriptable-sst
   system-tables
   schema-upgrades
   upgrading
   pc-recovery
   quorum-reset
   managing-fc
   auto-eviction
   using-sr
   arbitrator
   backup-cluster
