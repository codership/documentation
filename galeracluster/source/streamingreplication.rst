#####################
Streaming Replication
#####################
.. _`sr`:
.. index::
   pair: Galera Cluster 4.x; Streaming Replication

Under normal operation, the node performs all replication and certification events when the transaction commits.  When working with small transactions this is fine, but it poses an issue with long-running writes and changes to large data-sets.

In :term:`Streaming Replication`, the node breaks the transaction down into fragments, then certifies and replicates them on the slaves while the transaction is still in progress.  Once certified, the fragment can no longer be aborted by conflicting transactions.

Additionally, Streaming Replication allows the node to process transaction write-sets greater than 2Gb.

.. note:: Streaming Replication is a new feature introduced in version 4.0 of Galera Cluster.  Older versions do not support these operations.

	  
=================================
When to Use Streaming Replication
=================================
.. _`when-use-sr`:

In most cases, the normal method Galera Cluster uses in replication is sufficient in transferring data from the node to the cluster.  :term:`Streaming Replication` provides you with an alternative for situations where this is not the case.  Bear in mind that there are some limitations to its use.  It is recommended that you only enable it at a session-level, and then only on specific transactions that require the feature.

.. note:: For more information on the limitations to Streaming Replication, see :ref:`Limitations <sr-limit>`.


-------------------------------
Long-running Write Transactions
-------------------------------
.. _`longrun-write-trx`:

When using normal replication, you may occasionally encounter issues with long-running write transactions.

The longer it takes for the node to commit the transaction, the greater the likelihood that the cluster will apply a smaller, conflicting transaction before the longer one can replicate to the cluster.  When this happens, the cluster aborts the long-running transaction.

Using :term:`Streaming Replication` on long-running transactions mitigates this situation.  Once the node replicates and certifies a fragment, it is no longer possible for other transactions to abort it.


-----------------------------
Large Data Write Transactions
-----------------------------
.. _`large-write-trx`:

When using normal replication, the node processes the transaction locally and doesn't replicate the data until you commit.  This can create problems when updating a large volume of data, especially on nodes with slower network connections.

Additionally, while slave nodes apply a large transaction, they cannot commit other transactions that they receive, which may result in Flow Control throttling of the entire cluster.

With :term:`Streaming Replication`, the node begins to replicate the data with each transaction fragment, rather than waiting for the commit.  This allows you to spread the replication out over the lifetime of the transaction.

In the case of the slave nodes, after the slave applies a fragment, it is free to apply and commit other, concurrent transactions without blocking.  This allows the slave node to incrementally process the entire large transaction with a minimal impact on the cluster.


-----------
Hot Records
-----------
.. _`hot-records`:

In cases where an application frequently updates one and the same records from the same table, (such as when implementing a locking scheme, a counter, or a job queue), you can use :term:`Streaming Replication` to force critical updates to replicate to the entire cluster.

Running the transaction in this way effectively locks the hot record on all nodes, preventing other transactions from modifying the row.  It also increases the chances that the transaction will commit successfully and that the client in turn will receive the desired outcome. 

.. note:: For more information and an example of how to implement Streaming Replication in situations such as this, see :ref:`Using Streaming Replication with Hot Records <usr-hot-records>`.

===========
Limitations
===========
.. _`sr-limit`:

In deciding whether you want to use :term:`Streaming Replication` with your application, consider the following limitations.

-------------------------
Replication Fragment Size
-------------------------
.. _`limit-sr-fragement-size`:

While a transaction is in progress, Streaming Replication fragments are temporarily stored as blobs in a dedicated InnoDB table. In MySQL 5.6, InnoDB limits the maximum blob size to 10% of the total redo log size. If the redo log size is insufficient to store a particular fragment, an error will be returned to the client:

.. code-block:: mysql

   ERROR 1534 (HY000): Writing one row to the row-based binary log failed

and an error will be reported in the error log:

.. code-block:: console

   2016-06-23 10:41:36 49989 [ERROR] InnoDB: The total blob data length (10485855) is greater than 10% of the total redo log size (10485760). Please increase total redo log size.
   2016-06-23 10:41:36 49989 [ERROR] WSREP: Error writing into wsrep_schema.SR: 139
   2016-06-23 10:41:36 49989 [ERROR] WSREP: Failed to write to frag table: 1
   2016-06-23 10:41:36 49989 [ERROR] WSREP: Failed to append frag to persistent storage

To accomodate larger fragments, increase the InnoDB redo log size using the ``innodb_log_file_size`` variable.

----------------------------------
Performance during the Transaction
----------------------------------
.. _`limit-in-trx`:

When you enable :term:`Streaming Replication`, each node in the cluster begins recording their write-sets to the ``SR`` table in the ``wsrep_schema`` database.  The nodes do this to ensure the persistence of Streaming Replication updates in the event that they crash.  However, this operation increases the load on the node, which may adversely affect its performance.

As such, it is recommend that you only enable Streaming Replication at a session-level and then only for transactions that would not run correctly without it.


----------------------------
Performance during Rollbacks
----------------------------
.. _`limit-rollback`:

Occasionally, you may encounter situations where the cluster needs to roll back a transaction while :term:`Streaming Replication` is in use.  In these cases, the rollback operation consumes system resources on all nodes.

When long-running write transactions frequently need to be rolled back, this can become a performance issue.  Therefore, it is a good application design policy to use shorter transactions wherever possible.  In the event that your application performs batch processing or scheduled housekeeping tasks, consider splitting these into smaller transactions in addition to using Streaming Replication.

------------------------------------
Interaction with LOAD DATA Splitting
------------------------------------
.. _`limit-load-data-splitting`:

The :ref:`wsrep_load_data_splitting <wsrep_load_data_splitting>` variable, which controls the ``LOAD DATA`` splitting functionality, has no effect for statements where :term:`Streaming Replication` is in effect.
