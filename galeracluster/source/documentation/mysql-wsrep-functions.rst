.. cssclass:: library-document

=======================
MySQL wsrep Functions
=======================
.. _`mysql-wsrep-functions`:


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


.. _`WSREP_LAST_SEEN_GTID`:
.. rubric:: ``WSREP_LAST_SEEN_GTID()``
.. index::
   pair: Functions; WSREP_LAST_SEE_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

Much like ``LAST_INSERT_ID()`` for getting the identification number of the last row inserted in MySQL, this function returns the :term:`Global Transaction ID` of the last write transaction observed by the client.

+---------------+----------------------------+
| **Function**  | ``WSREP_LAST_SEEN_GTID()`` |
+---------------+----------------------------+
| **Arguments** | None                       |
+---------------+----------------------------+
| **Support**   | 4+                         |
+---------------+----------------------------+

This function returns the :term:`Global Transaction ID` of the last write transaction observed by the client. It can be useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`. You can use this parameter to identify the transaction upon which it should wait before unblocking the client.

Below is an example of how you might use the ``WSREP_LAST_SEEN_GTID()`` function to get the Global Transaction ID of the last write transaction observed:

.. code-block:: console

   SELECT WSREP_LAST_SEEN_GTID();


.. _`WSREP_LAST_WRITTEN_GTID`:
.. rubric:: ``WSREP_LAST_WRITTEN_GTID()``
.. index::
   pair: Functions; WSREP_LAST_WRITTEN_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

This function returns the :term:`Global Transaction ID` of the last write transaction made by the client.


+---------------+-------------------------------+
| **Function**  | ``WSREP_LAST_WRITTEN_GTID()`` |
+---------------+-------------------------------+
| **Arguments** | None                          |
+---------------+-------------------------------+
| **Support**   | 4+                            |
+---------------+-------------------------------+

This function returns the Global Transaction ID of the last write transaction made by the client.  This can be useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`. You can use this parameter to identify the transaction upon which it should wait before unblocking the client.

Below is an example of how you might use the ``WSREP_LAST_SEEN_GTID()`` function to get the Global Transaction ID of the last write transaction observed:

.. code-block:: console

   BEGIN;

   UPDATE table_name SET id = 0
   WHERE field = 'example';

   COMMIT;

   SELECT WSREP_LAST_WRITTEN_GTID();

.. _`WSREP_SYNC_WAIT_UPTO_GTID`:
.. rubric:: ``WSREP_SYNC_WAIT_UPTO_GTID()``
.. index::
   pair: Functions; WSREP_SYNC_WAIT_UPTO_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

This function blocks the client until the node applies and commits the given transaction.

+---------------+----------------------------------------------+
| **Function**  | ``WSREP_LAST_WRITTEN_GTID()``                |
+---------------+----------------------+-----------------------+
| **Arguments** | *Required Arguments* | Global Transaction ID |
|               +----------------------+-----------------------+
|               | *Optional Arguments* | timeout               |
+---------------+----------------------+-----------------------+
| **Support**   | 4+                                           |
+---------------+----------------------------------------------+

This function blocks the client until the node applies and commits the given :term:`Global Transaction ID`.  If you don't provide a timeout, it defaults to the value of :ref:`repl.causal_read_timeout <repl.causal_read_timeout>`. It the following return values:

- ``1``: The node applied and committed the given Global Transaction ID.

- ``ER_LOCAL_WAIT_TIMEOUT`` Error: The function times out before the node can apply the transaction.

- ``ER_WRONG_ARGUMENTS`` Error: The function is given an incorrect Global Transaction ID.


Below is an example of how you might use the ``WSREP_SYNC_WAIT_UPTO_GTID()`` function:

.. code-block:: console

   $transaction_gtid = SELECT WSREP_LAST_SEEN_GTID();
   ...
   SELECT WSREP_SYNC_WAIT_UPTO_GTID($transaction_gtid);
