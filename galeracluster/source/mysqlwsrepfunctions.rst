===========================================
MySQL wsrep Functions
===========================================
.. _`mysqlwsrepfunctions`:


+-------------------------------------+-------------------------+---------+
| Function                            | Arguments               | Support |
+=====================================+=========================+=========+
| :ref:`WSREP_LAST_SEEN_GTID()        |                         | 4+      |
| <WSREP_LAST_SEEN_GTID>`             |                         |         | 
+-------------------------------------+-------------------------+---------+
| :ref:`WSREP_LAST_WRITTEN_GTID()     |                         | 4+      |
| <WSREP_LAST_WRITTEN_GTID>`          |                         |         |
+-------------------------------------+-------------------------+---------+
| :ref:`WSREP_SYNC_WAIT_UPTO_GTID()   | ``gtid`` ``[timeout]``  | 4+      |
| <WSREP_SYNC_WAIT_UPTO_GTID>`        |                         |         |
+-------------------------------------+-------------------------+---------+


.. rubric:: ``WSREP_LAST_SEEN_GTID()``
.. _`WSREP_LAST_SEEN_GTID`:
.. index::
   pair: Functions; WSREP_LAST_SEE_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions
   
Returns the :term:`Global Transaction ID` of the last write transaction observed by the client.

+---------------+----------------------------+
| **Function**  | ``WSREP_LAST_SEEN_GTID()`` |
+---------------+----------------------------+
| **Arguments** | None                       |
+---------------+----------------------------+
| **Support**   | 4+                         |
+---------------+----------------------------+

This function returns the Global Transaction ID of the last write transaction observed by the client.  You may find it useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`, using this parameter to identify the transaction it should wait on before unblocking the client.


.. code-block:: mysql

   SELECT WSREP_LAST_SEEN_GTID();


   
.. rubric:: ``WSREP_LAST_WRITTEN_GTID()``
.. _`WSREP_LAST_WRITTEN_GTID`:
.. index::
   pair: Functions; WSREP_LAST_WRITTEN_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions
   
Returns the :term:`Global Transaction ID` of the last write transaction made by the client.


+---------------+-------------------------------+
| **Function**  | ``WSREP_LAST_WRITTEN_GTID()`` |
+---------------+-------------------------------+
| **Arguments** | None                          |
+---------------+-------------------------------+
| **Support**   | 4+                            |
+---------------+-------------------------------+

This function returns the Global Transaction ID of the last write transaction made by the client.  You may find it useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`, using this parameter to identify the transaction it should wait on before unblocking the client.

.. code-block:: mysql

   BEGIN;
   UPDATE table_name SET id = 0 WHERE field = 'example';
   COMMIT;
   SELECT WSREP_LAST_WRITTEN_GTID();



   
.. rubric:: ``WSREP_SYNC_WAIT_UPTO_GTID()``
.. _`WSREP_SYNC_WAIT_UPTO_GTID`:
.. index::
   pair: Functions; WSREP_SYNC_WAIT_UPTO_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions
   
Blocks the client until the node applies and commits the given transaction.

+---------------+----------------------------------------------+
| **Function**  | ``WSREP_LAST_WRITTEN_GTID()``                |
+---------------+----------------------+-----------------------+
| **Arguments** | *Required Arguments* | Global Transaction ID |
|               +----------------------+-----------------------+
|               | *Optional Arguments* | timeout               |
+---------------+----------------------+-----------------------+
| **Support**   | 4+                                           |
+---------------+----------------------------------------------+

This function blocks the client until the node applies and commits the given :term:`Global Transaction ID`.  If you don't provide a timeout, it defaults to the value of :ref:`repl.causal_read_timeout <repl.causal_read_timeout>`.

The function uses the following return values:

- When the node applies and commits the given Global Transaction ID, it returns the value ``1``.

- When the function times out before the node can apply the transaction, it returns an ``ER_LOCAL_WAIT_TIMEOUT`` error.

- When the function is given an incorrect Global Transaction ID, it returns an ``ER_WRONG_ARGUMENTS`` error.

.. code-block:: mysql

   $transaction_gtid = SELECT WSREP_LAST_SEEN_GTID();
   ...
   SELECT WSREP_SYNC_WAIT_UPTO_GTID($transaction_gtid);

