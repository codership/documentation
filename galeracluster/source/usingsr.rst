###########################
Using Streaming Replication
###########################
.. _`using-sr`:
.. index::
   pair: Galera Cluster 4.x; Streaming Replication

When a node replicates a transaction under :term:`Streaming Replication`, it breaks the transaction into fragments, and then certifies and applies the fragments to slave nodes while the transaction is still in progress.

This allows you to work with larger data-sets, manage hot records, and help avoid conflicts and hangs in the case of long-running transactions.

.. note:: Streaming Replication is a new feature introduced in version 4.0 of Galera Cluster.  Older versions do not support these operations.


==============================
Enabling Streaming Replication
==============================
.. _`enable-sr`:

The best practice when working with :term:`Streaming Replication` is to enable it at a session-level for specific transactions, or parts thereof.  The reason is that Streaming Replication increases the load on all nodes when applying and rolling back transactions.  You'll get better performance if you only enable Streaming Replication on those transactions that won't run correctly without it.

.. note:: For more information, see :ref:`When to Use Streaming Replication <when-use-sr>`.

Enabling Streaming Replication requires you tp define the replication unit and number of units to use in forming the transaction fragments.  Two parameters control these variables: :ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>` and :ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`.

Below is an example of how to set these two parameters:

.. code-block:: mysql

   SET SESSION wsrep_trx_fragment_unit='statement';
   SET SESSION wsrep_trx_fragment_size=3;

In this example, the fragment is set to three statements.  For every three statements from a transaction, the node will generate, replicate and certify a fragment.

You can choose between several replication units when forming fragments:

- **bytes** This defines the fragment size in bytes.
- **events** This defines the fragment size as the number of binary log events generated.
- **rows** This defines the fragment size as the number of rows the fragment updates.
- **statements** This defines the fragment size as the number of statements in a fragment.

Choose the replication unit and fragment size that best suits the specific operation you want to run.

======================================
Streaming Replication with Hot Records
======================================
.. _`usr-hot-records`:

When your application needs to update frequently the same records from the same table (e.g., implementing a locking scheme, a counter, or a job queue), Streaming Replication allows you to force critical changes to replicate to the entire cluster.

For instance, consider the use case of a web application that creates work orders for a company.  When the transaction starts, it updates the table ``work_orders``, setting the queue position for the order.  Under normal replication, two transactions can come into conflict if they attempt to update the queue position at the same time.

You can avoid this with Streaming Replication.  As an example of how to do this, you would first execute the following SQL statement to begin the transaction:

 .. code-block:: mysql

    START TRANSACTION;

After reading the data that you need for the application, you would enable Streaming Replication by executing the following two ``SET`` statements:

 .. code-block:: mysql

    SET SESSION wsrep_trx_fragment_unit='statement';
    SET SESSION wsrep_trx_fragment_size=1;

Next, set the user's position in the queue like so:

 .. code-block:: mysql

    UPDATE work_orders 
    SET queue_position = queue_position + 1;

Witht that done, you can disable Streaming Replication by executing one of the previous ``SET`` statemetns, but with a different value like so:

 .. code-block:: mysql

    SET SESSION wsrep_trx_fragment_size=0;

You can now perform whatever additional tasks you need to prepare the work order, and then commit the transaction:

   .. code-block:: mysql

      COMMIT;

During the work order transaction, the client initiates Streaming Replication for a single statement, which it uses to set the queue position.  The queue position update then replicates throughout the cluster, which prevents other nodes from coming into conflict with the new work order.
      
   

