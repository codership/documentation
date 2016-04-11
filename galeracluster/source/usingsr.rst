###########################
Using Streaming Replication
###########################
.. _`using-sr`:

When a node replicates a transaction under :term:`Streaming Replication`, instead of waiting for the commit, it breaks the transaction down into fragments, then certifies and applies the fragments to slave nodes while the transaction is still in progress.

This allows you to work with larger data-sets, manage hot records, and help avoid conflicts and blocks in the case of long-running transactions.

.. note:: Streaming Replication is a new feature introduced in version 4.0 of Galera Cluster.  Older versions do not support these operations.

==============================
Enabling Streaming Replication
==============================
.. _`enable-sr`:

The best practice when working with :term:`Streaming Replication` is to enable it at a session-level for specific transactions.  The reason is that Streaming Replication increases the load on all nodes when applying and rolling back transactions.  Meaning, you'll get better performance if you only enable Streaming Replication on those transactions that won't run correctly without it.

.. note:: For more information, see :ref:`When to Use Streaming Replication <when-use-sr>`.

Enabling Streaming Replication requires that you define the replication unit and number of units that to use in forming the transaction fragments.  Two parameters control these variables: :ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>` and :ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`.

.. code-block:: mysql

   SET SESSION wsrep_trx_fragment_unit='statement';
   SET SESSION wsrep_trx_fragment_size=3;

In the example, the fragment is set to three statements.  For every three statements the node receives in the transaction, it certifies and applies a fragment.

You can choose between several replication units in forming fragments:

- **Bytes** Defines the fragment size as the transaction size in bytes.
- **Events** Defines the fragment size as the number of binary log events the transaction generates.
- **Rows** Defines the fragment size as the number of rows the transaction updates.
- **Statement** Defines the fragment size as the number of states in the transaction.

Choose the replication unit and fragment size that best suits the specific operation you want to run.

======================================
Streaming Replication with Hot Records
======================================
.. _`usr-hot-records`:

When your application needs to frequently update the same records from the same table, (such as when implementing a locking schema, counter, or job queues), Streaming Replication allows you to force critical changes to replicate to the entire cluster.

For instance, consider the use case of a web application that creates work orders for a company.  When the transaction starts it updates the table ``word_orders`` setting the queue position for the order.  Under normal replication, two transactions can come into conflict if they attempt to set the same queue position.

You can avoid this with Streaming Replication:

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

When the client starts the work order transaction, it initiates Streaming Replication for a single statement, which it uses to set the queue position.  The queue position then replicates through the cluster, which prevents other nodes from coming into conflict with the new work order.
      
   

