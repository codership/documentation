############################
What's New in Galera Cluster
############################
.. _`whats-new`:

With the latest release of Galera Cluster in the 4.x branch, a number of new features are now available to you, including,

- **Non-Blocking Operations** When performing DDL statements that update, analyze or optimize tables, you can now use the Non-Blocking Operation online schema upgrade method.  Unlike other methods, this allows you to update the cluster schema without blocking reads on the nodes.

  For more information, see :ref:`Non-Blocking Operations <nbo>`.

- **Synchronization Functions**  This version introduces a series of SQL functions for use in wsrep synchronization operations.  You can use them to obtain the :term:`Global Transaction ID`, based on either the last write or last seen transaction, as well as setting the node to wait for a specific GTID to replicate and apply, before initiating the next transaction.

  For more information, see :ref:`Using Synchronization Functions <using-sync-functions>` and :doc:`mysqlwsrepfunctions`.
  


  
