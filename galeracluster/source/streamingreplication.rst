#####################
Streaming Replication
#####################
.. _`streaming-replication`:


Under normal operation, the node performs all replication and certification events when the transaction commits.  When working with small transactions this is fine, but it poses an issue with long-running writes and changes to large data-sets.

In :term:`Streaming Replication`, the node breaks the transaction down into fragments, then certifies and applies them on the slaves while the transaction is still in progress.  Once certified, conflicting transactions can no longer abort the fragment.

Additionally, Streaming Replication allows the node to process transaction write-sets greater than 2Gb.

.. note:: Streaming Replication is a new feature introduced in Galera Cluster version 4.  Older versions do not support these operations.

	  
===========================
Using Streaming Replication
===========================
.. _`using-sr`:


In order to enable Streaming Replication, you need to configure two parameters on the node: :ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>` and :ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`.  For instance,

.. code-block:: mysql

   SET SESSION wsrep_trx_fragment_unit='statement';
   SET SESSION wsrep_trx_fragment_size=3;

This configures the current transaction to use Streaming Replication, breaking it down into fragments three statements in size.


.. Bear in mind that there are some :ref:`disadvantages <disadvantages>` to using Streaming Replication.  It is recommended that you only enable it at a session-level on those transactions that would benefit from this feature. 


-------------------------------
Long-running Write Transactions
-------------------------------
.. _`longrun-write-trx`:


When using normal replication, you may often encounter issues when attempting long-running write transactions.  The longer it takes for the node to write in the transaction, the greater the likelihood that a smaller, conflicting transaction will get through ahead of it and cause a rollback. Moreover, while slave nodes apply long-running write transactions, they cannot commit other transactions, which may result in Flow Control throttling the entire cluster.

With Streaming Replication, you can set the node to replicate fragments of long-running write transactions.  Once the node replicates and certifies the fragment, it is no longer possible for other transactions to abort it.

Additionally, after the slave applies the fragment, it is free to apply and commit other, concurrent transactions without blocking.  This allows the slave nodes to process the entire long-running write transaction with a minimal impact on other transactions.



-----------
Hot Records
-----------
.. _`hot-records`:

In cases where an application frequently updates one and the same records from the same tables, such as when implementing a locking schema, counters, job queues, you can use Streaming Replication to force the changes to replicate to the entire cluster.  This effectively causes the hot records to become locked on all nodes, preventing other transactions from modifying them.  It also increases the chances that the transaction successfully commits and that the client receives the desired outcome.

For instance, use streaming replication to set the user's position in the queue:

#. Begin the transaction:

   .. code-block:: mysql

      START TRANSACTION;

#. After reading the data that you need for the application, enable Streaming Replication:

   .. code-block:: mysql

      SET SESSION wsrep_trx_fragment_unit='statement';
      SET SESSION wsrep_trx_fragment_size=1;

#. Set the user's position in the queue:

   .. code-block:: mysql

      UPDATE work_orders SET queue_position = queue_position + 1;

#. Disable Streaming Replication:

   .. code-block:: mysql

      SET SESSION wsrep_trx_fragment_size=0;

#. Perform whatever additional tasks you need to ready the work order, then commit the transaction:

   .. code-block:: mysql

      COMMIT;

In the example hot record transaction, the node uses Streaming Replication to update the `work_orders` table to set the position in the queue for the user, before replicating the actual work order through the cluster.  This ensures that if two users connect to different nodes, they won't cause one of the transactions to abort due to conflict.
      
   

-----------------------------
Large Data Write Transactions
-----------------------------
.. _`large-write-trx`:


When using the normal replication method, there is a limit to the size of the transactions that the node can replicate: 2Gb.  There is also a practical limit on network connections




