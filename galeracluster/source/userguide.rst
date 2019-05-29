==============
Administration
==============
.. _`admin-guide`:

With the basics of how the cluster works and how to install and initialize it covered, this part begins a five part series on the administration and management of Galera Cluster.

The chapters in this part relate to the administration of nodes and the cluster.  :doc:`deployment`, covers how to use Galera Cluster in relation to your wider infrastructure, how to configure load balancers to work with the cluster and edge case deployments, such as running nodes in containers.  The chapters in :doc:`monitor` show how to keep tabs on the status of the cluster and automate reporting.  :doc:`security` covers configuring Galera Cluster to work with firewalls, SELinux and SSL encryption.  :doc:`migrate` how to transition from a standalone instance of MySQL, MariaDB or Percona XtraDB to Galera Cluster.


.. rubric:: Node Administration
.. _`node-admin`:

Managing and administering nodes in Galera Cluster is similar to the administration and management of the standard standalone MySQL, MariaDB and Percona XtraDB database servers, with some additional features used to manage its interaction with the cluster.  These chapters cover the administration of individual nodes, how they handle write-set replication and schema updates, and the procedure for upgrading Galera Cluster software.

- :doc:`nodeprovisioning`

  The complete process of replicating data into a node so that it can operate as part of the Primary Component is called 'provisioning' the node.  It ensures that the nodes update the local data, keeping it consistent with the state of the cluster.  This chapter provides an overview to how nodes join the cluster and maintain their state through state transfers.

- :doc:`sst`

  When a node falls too far behind the cluster, they request State Snapshot Transfers from another node in order to bring its local database up to date with the cluster.  This chapter provides a guide to each state transfer method Galera Cluster supports.

- :doc:`scriptablesst`

  When nodes send and receive State Snapshot Transfers, they manage the process through external scripts that call the standard state transfer methods.  In event that you require additional functionality than what is available by default, you can use scripts to implement your own custom state snapshot transfer methods.

- :doc:`system-tables`

  When you install Galera Cluster, it creates a set of system tables in the ``mysql`` database, which it uses to store configuration information.  Similar to how the underlying database server uses the ``performance_schema`` and ``information_schema``, Galera Cluster uses these tables to record information relevant to replication.  This section provides a guide to what you'll find in these tables and how you might query them for useful information about the status of the node and the cluster.


- :doc:`schemaupgrades`

  Statements that update the database schema, (that is, DDL statements), are non-transactional and as such won't replicate to the cluster through write-sets.  This chapter covers different methods for online schema upgrades and how to implement them in your deployment.

- :doc:`upgrading`

  In order to upgrade Galera Cluster to a new version or increment of the software, there are a few additional steps you need to take in order to maintain the cluster during the upgrade.  This chapter provides guides to different methods in handling this process.





.. rubric:: Cluster Administration
.. _`cluster-admin`:

In addition to node administration, Galera Cluster also provides interfaces for managing and administering the cluster.  These chapters cover Primary Component recovery, managing Flow Control and Auto Eviction, as well as Galera Arbitrator and how to handle backups.


- :doc:`pcrecovery`

  When nodes establish connections with each other, they form components.  The operational component in the cluster is called the Primary Component.  This chapter covers a new feature in version 3.6 of Galera Cluster, which sets the nodes to save the Primary Component state to disk.  In the event of an outage, once all the nodes that previously formed the Primary Component reestablish network connectivity, they automatically restore themselves as the new Primary Component.

- :doc:`quorumreset`

  The Primary Component maintains quorum when most of the nodes in the cluster are connected to it.  This chapter provides a guide to resetting the quroum in the event that the cluster becomes non-operational due to a major network outage, the failure of more than half the nodes, or a split-brain situation.

- :doc:`managingfc`

  When nodes fall too far behind, Galera Cluster uses a feedback mechanism called Flow Control, pausing replication to give the node to process transactions and catch up with the cluster.  This chapter covers the monitoring and configuration of Flow Control, in order to improve node performance.

- :doc:`autoeviction`

  When Galera Cluster notices erratic behavior from a node, such as in the case of unusually delayed response times, it can initiate a process to remove the node permanently from the cluster.  This chapter covers the configuration and management of how the cluster handles these Auto Evictions.

- :doc:`usingsr`

  When the node uses Streaming Replication, instead of waiting for the commit to replicate and apply transactions to the cluster, it breaks the transaction down into replication units, transferring and applying these on the slave nodes while the transaction is still open.  This chapter provides a guide to how to enable, configure and utilize Streaming Replication.


- :doc:`arbitrator`

  Galera Arbitrator is a separate application from Galera Cluster.  It functions as an additional node in quorum calculations, receives the same data as other node, but does not participate in replications.  You can use it to provide an odd node to help avoid split-brain situations, or use it in generating consistent application state snapshots, in generating backups.

- :doc:`backingupthecluster`

  Standard backup methods available to MySQL database servers fail to preserve Global Transaction ID's used by Galera Cluster.  You can recover data from these backups, but they're insufficient in restoring nodes to a well-defined state.  This chapter shows how to use state transfers to properly perform backups in Galera Cluster.


.. toctree::
   :maxdepth: 2
   :hidden:

   nodeprovisioning
   sst
   scriptablesst
   system-tables
   schemaupgrades
   upgrading
   pcrecovery
   quorumreset
   managingfc
   autoeviction
   usingsr
   arbitrator
   backingupthecluster
