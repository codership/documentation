.. meta::
   :title: Support for Transaction Isolation Levels
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`supporting-transaction-isolation-levels`:

=========================================
Support for Transaction Isolation Levels
=========================================

.. rst-class:: article-stats

   Length:  1009 words; Writer: Seppo Jaakola; Published: September 21, 2015; Topic: General; Level: Intermediate


There appears to be great misunderstanding as to what MySQL transaction isolation levels Galera CLuster actually supports and how. This blog post tries to give answer to those uncertainties.

Galera Cluster provides ``SNAPSHOT ISOLATION`` between transactions running on separate cluster nodes. Transactions running on the same node are isolated by whatever was configured as the transaction isolation level in the MySQL configuration. So, if you have configured the default ``REPEATABLE READ`` isolation, transactions issued on the same node will behave under ``REPEATABLE READ`` semantics. However, for transactions issued on separate cluster nodes, the ‘first committer wins’ rule of ``SNAPSHOT ISOLATION`` is provided, and this will fix the lost update problem that generally hurts REPEATABLE READ isolation.

Therefore, it is not safe for the application to rely on ``SNAPSHOT ISOLATION`` semantics. But in general, transaction isolation in Galera CLuster is no less than what was configured for transaction isolation level in MySQL.

Note that this transaction isolation behavior has changed somewhat over time. Earlier Galera releases have also supported ``SNAPSHOT ISOLATION`` among transactions on the same node.

Here is an example showing how the lost update anomaly hurts transactions using plain ``REPEATABLE READ`` isolation. Two transactions read a value from a row in table t and then update the value and commit. The transactions are issued on the same node, and will behave under MySQL’s ``REPEATABLE READ`` isolation.

.. code-block:: console

   Transaction #1                  Transaction #2

   node1> begin;
   Query OK, 0 rows affected

                                node1> begin;
                                Query OK, 0 rows affected

   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    0 |
   +---+------+
   1 row in set

                                node1> select * from t;
                                +---+------+
                                | i | j    |
                                +---+------+
                                | 1 |    0 |
                                +---+------+
                                1 row in set

   node1> update t set j=1 where i=1;
   Query OK, 1 row affected

                                node1> update t set j=2
                                node1> where i=1;
                                # Waits for InnoDB lock ...

   node1> commit;
   Query OK, 0 rows affected

                                Query OK, 1 row affected
                                # Lock waiting ends

   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    1 |
   +---+------+
   1 row in set
   # Transaction #1's update is now visible

                                node1> commit;

   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    2 |
   +---+------+
   1 row in set

                                node1> select * from t;
                                +---+------+
                                | i | j    |
                                +---+------+
                                | 1 |    2 |
                                +---+------+
                                1 row in set

   # Transaction #2 has written over transaction #1's result

Both transactions have read the same value in the row (0), and made their decision on how to change the value based on the application logic.
But, as the outcome of running these transactions in parallel, transaction #1’s write was visible in the database for a short while, but it went unnoticed by transaction #2 who blindly wrote over its value (2) in the table. Had it noticed that the value had changed to 1, the application logic may have dictated another value to be written in the table.

Here is the same exercise, but now transactions #1 and #2 connect to separate cluster nodes (node1 and node2).

.. code-block:: console

   Transaction #1                  Transaction #2

   node1> begin;
   Query OK, 0 rows affected

                                node2> begin;
                                Query OK, 0 rows affected

   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    0 |
   +---+------+
   1 row in set
                                node2> select * from t;
                                +---+------+
                                | i | j    |
                                +---+------+
                                | 1 |    0 |
                                +---+------+
                                1 row in set

   node1> update t set j=1 where i=1;
   Query OK, 1 row affected

                                node2> update t set j=2
                                node2> where i=1;
                                Query OK, 1 row affected
                                # There is no lock wait here,
                                # as we are operating
                                # on another node

   node1> commit;
   Query OK, 0 rows affected
                                node2> commit;
                                ERROR 1213 (40001): Deadlock
                                found when trying to get lock;
                                try restarting transaction

   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    1 |
   +---+------+
   1 row in set
                                node2> select * from t;
                                +---+------+
                                | i | j    |
                                +---+------+
                                | 1 |    1 |
                                +---+------+
                                1 row in set

   # Transaction #1, the first committer, has won

Here the ‘first committer wins’ rule is applied, and only transaction #1 is let to commit. Transaction #2 will notice that it is working on the same database snapshot as transaction #1 and has a conflicting write, therefore it aborts and returns a deadlock error back to the client.

Therefore, transactions on multiple nodes are protected from the ‘lost update’ problem. The lost update phenomenon can hurt only transactions that are using ``REPEATABLE READ`` isolation and are running on the same node. However, MySQL/InnoDB has a workaround even for this situation by using ``SELECT FOR UPDATE``, which will lock the rows read, and prevent other transactions from operating on this ‘read view’ until the transaction finally commits. Here is an example showing how transactions #1 and #2 can tackle the lost update problem by using the read locks granted by ``SELECT FOR UPDATE``:

.. code-block:: console

   Transaction #1                  transaction #2

   node1> begin;
   Query OK, 0 rows affected
                                node1> begin;
                                Query OK, 0 rows affected

   node1> select * from t for update;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    0 |
   +---+------+
   1 row in set
                                node1> select * from t
                                node1> for update;
                                # Blocks waiting
                                # for InnoDB lock

   node1> update t set j=1 where i=1;
   Query OK, 1 row affected

   node1> commit;
   Query OK, 0 rows affected

                                +---+------+
                                | i | j    |
                                +---+------+
                                | 1 |    1 |
                                +---+------+
                                1 row in set
                                # Lock wait ends
                                # We see transaction #1's
                                # result and work on
                                # a different snapshot now

                                node1> update t set j=3
                                node1> where i=1;
                                Query OK, 1 row affected

                                node1>  commit;
                                Query OK, 0 rows affected
   node1> select * from t;
   +---+------+
   | i | j    |
   +---+------+
   | 1 |    3 |
   +---+------+
   1 row in set
                                 node1> select * from t;
                                 +---+------+
                                 | i | j    |
                                 +---+------+
                                 | 1 |    3 |
                                 +---+------+
                                 1 row in set

Galera Cluster can support transaction isolation levels up to ``REPEATABLE READ`` and also protect against lost update problem if the application can be tuned to use proper locking strategy like the one shown above.

However, Galera does not support ``SERIALIZABLE`` isolation in multi-master topology, because there is currently no means to protect read locks from being overwritten by the replication. ``SERIALIZABLE`` isolation should work in controlled master-slave topologies, but in practice its use is not recommended at all. And, ``SERIALIZABLE`` isolation may be disabled in future releases, unless we can figure out a way to support it in a safe way.
