======================
 Technical Description
======================
.. _`tech-description`:

Galera Cluster is a synchronous certification-based replication solution for MySQL, MariaDB and Percona XtraDB.  Cluster nodes are identical and fully representative of the cluster state.  They allow for unconstrained transparent client access, acting as a single-distributed database server.  In order to better understand Galera Cluster, this part provides detailed information on how it works and how it can work for you.

.. rubric:: Understanding Replication
.. _`understanding-repl`:

Replication in the context of databases refers to the frequent copying of data from one database server into another.  These chapters provide a high-level explanation of replication both in the general sense of how it works as well as the particulars of how Galera Cluster implements these core concepts.

- :doc:`introduction`

  How does database replication generally work?  This chapter provides a high-level overview of the problems inherent in the various replication implementations, include master-slave, asynchronous and synchronous replication.
	    
- :doc:`certificationbasedreplication`

  Using group communications and transaction ordering techniques, certification-based replication allows for synchronous replication.  

  
.. rubric:: Understanding Galera Cluster
.. _`understanding-galera`:

With a better grasp on how replication works, these chapters provide a more detailed explanation of how Galera Cluster implements certification-based replication, including the specific architecture of the nodes, how they communicate with each other, replicate data and manage the replication process.


- :doc:`architecture`

  Where the above chapters explain the abstract concepts surrounding certification-based replication, this chapter covers the specific architecture used by Galera Cluster in implementing write-set replication, including the wsrep API and the Galera Replication and Group Communication plugins.


- :doc:`isolationlevels`

  In a database system, the server processes concurrent transactions in isolation from each other, where the level of isolation determines whether and how these transactions affect one another.  This chapter provides an overview of the isolation levels supported by Galera Cluster.
  
- :doc:`statetransfer`

  The actual process nodes uses to replicate data into each other is called provisioning.  Galera Cluster supports two provisioning methods: State Snapshot Transfers and Incremental State Transfers.  This chapter provides an overview of each.

- :doc:`nodestates`

  Galera Cluster manages the replication process using a feedback mechanism called Flow Control.  This allows the node to pause and resume replication according to its performance needs and to prevent any node from lagging too far behind the others in applying transaction.  This chapter provides an overview of Flow Control and the different states it nodes can hold.

- :doc:`recovery`

  Nodes fail to operate when they lose their connection with the cluster.  It can occur for various reasons, such as hardware failures, software crashes, or the loss of network connectivity.  This chapter provides an overview of how nodes and the cluster cope with failure and recover.

- :doc:`weightedquorum`

  When nodes connect to each other they form components.  The Primary Component is a component that has quorum, that is it carries the majority of nodes in the cluster.  By default, each node represents one vote in quorum calculations, however, you can modify this feature in order to ensure certain stable nodes with strong connections carry a greater value.  This chapter provides an overview of how Galera Cluster handles weighted values in quorum calculations.

- :doc:`streamingreplication`

  Normally, nodes transfer all replication and certification events on the transaction commit.  With Streaming Replication, the nodes break the transaction down into fragments.  Then, they certify, replicate and apply these replication fragments onto the slave nodes.  This chapter provides an overview to Streaming Replication, how it works and the limitations to its use.

.. toctree::
   :maxdepth: 2
   :hidden:
      
   introduction
   certificationbasedreplication
   architecture
   isolationlevels
   statetransfer
   nodestates
   recovery
   weightedquorum
   streamingreplication

