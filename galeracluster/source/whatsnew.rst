################################
What's New in Galera Cluster 4.x
################################
.. _`whats-new`:
.. index::
   pair: Galera Cluster 4.x; Streaming Replication
.. index::
   pair: Galera Cluster 4.x; Non-Blocking Operation
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

With the latest release of Galera Cluster in the 4.x branch, a number of new features are now available to you, including,

- **Non-Blocking Operations** When performing DDL statements that update, analyze or optimize tables, you can now use the Non-Blocking Operation online schema upgrade method.  Unlike other methods, this allows you to update the cluster schema without blocking reads on the nodes.

  For more information, see :ref:`Non-Blocking Operations <nbo>`.

- **Streaming Replication** Under normal operation, the node initiates all replication and certification operations when the transaction commits.  In large transactions, this can result in conflicts, as smaller transactions can get in first and cause the large transactions to abort.  With Streaming Replication, the node breaks the transaction down into fragments, then certifies and replicates them on all slaves nodes while the transaction is still in progress.  Once certified, conflicting transactions can no longer abort the fragment.

  This provides an alternative replication method for handling large or long-running write transactions, or when working with hot records.

  For more information, see :doc:`streamingreplication` and :doc:`usingsr`.
  
- **Synchronization Functions**  This version introduces a series of SQL functions for use in wsrep synchronization operations.  You can use them to obtain the :term:`Global Transaction ID`, based on either the last write or last seen transaction, as well as setting the node to wait for a specific GTID to replicate and apply, before initiating the next transaction.

  For more information, see :ref:`Using Synchronization Functions <using-sync-functions>` and :doc:`mysqlwsrepfunctions`.
  


  
