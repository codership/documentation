#####################
Streaming Replication
#####################
.. _`sr`:

Under normal operation, the node performs all replication and certification events when the transaction commits.  When working with small transactions this is fine, but it poses an issue with long-running writes and changes to large data-sets.

In :term:`Streaming Replication`, the node breaks the transaction down into fragments, then certifies and applies them on the slaves while the transaction is still in progress.  Once certified, conflicting transactions can no longer abort the fragment.

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

The longer it takes for the node to write the transaction, the greater the likelihood that the cluster will apply a smaller, conflicting transaction before longer one can replicate to the cluster.  When this happens, the cluster aborts the long-running transaction.

Additionally, while slave nodes attempt to apply long-running transaction, they cannot commit other transactions that they receive, which may result in Flow Control throttling of the entire cluster.

Using :term:`Streaming Replication` on long-running transactions mitigates each of these cases.  Once the node replicates and certifies the fragment, it is no longer possible for other transactions to abort it.

In the case of the slave nodes, after the slave applies the fragment, it is free to apply and commit other, concurrent transactions without blocking the long-running one.  This allows the slave node to process the entire long-running write transaction with a minimal impact on the cluster.

-----------
Hot Records
-----------
.. _`hot-records`:

In cases where an application frequently updates one and the same records from the same table, (such as when implementing a locking schema, counter, or job queues), you can use :term:`Streaming Replication` to force critical changes to replicate to the entire cluster.

Running the transaction in this way effectively locks the hot record on all nodes, preventing other transactions from modifying the row.  It also increases the chances that the transaction commits successfully and that the client in turn receives the desired outcome. 

.. note:: For more information and an example of how to implement Streaming Replication in situations such as this, see :ref:`Using Streaming Replication with Hot Records <usr-hot-records>`.

-----------------------------
Large Data Write Transactions
-----------------------------
.. _`large-write-trx`:

When using normal replication, the node processes the transaction locally and doesn't replicate the data until you commit.  This can create problems when updating a large volume of data on nodes with slower network connection.

With :term:`Streaming Replication`, the node begins to replicate the data with each transaction fragment, rather than waiting for the commit.  This allows you to spread the replication out over the lifetime of the transaction.


===========
Limitations
===========
.. _`sr-limit`:

In deciding whether you want to use :term:`Streaming Replication` with your application, consider the following limitations.

----------------------------------
Performance during the Transaction
----------------------------------
.. _`limit-in-trx`:

When you enable :term:`Streaming Replication`, each node in the cluster begins recording their write-sets to the ``wsrep_schema`` database on the ``SR`` table.  The nodes do this to ensure the persistence of Streaming Replication in the event that they crash.  However, this operation increases the load on the node, which may adversely affect its performance.

As such, it is recommend that you only enable Streaming Replication at a session-level and then only for transactions that would not run correctly without it.


----------------------------
Performance during Rollbacks
----------------------------
.. _`limit-rollback`:

Occasionally, you may encounter situations where the cluster needs to roll back a transaction while :term:`Streaming Replication` is in use.  In these cases, the rollback operation consumes system resources on all nodes.

When the transaction being rolled back is a long-running write transaction, this can become a serious performance issue.  As such, it is a good application design policy to use shorter transactions wherever possible.  In the event that your application performs batch processing or scheduled housekeeping tasks, consider splitting these into smaller transactions with Streaming Replication.

