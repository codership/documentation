.. meta::
   :title: Error 1213: Deadlock Found
   :description: Describes Why a Transaction Can't Lock Rows
   :language: en-US
   :keywords: galera cluster, deadlock found, transaction incomplete
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`wsrep_debug <wsrep_debug>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-deadlock-found`:

====================================
Deadlock Found during a Transaction
====================================

.. rst-class:: article-stats

   Length: 887 words; Published: November 15, 2019; Category: Schema & SQL; Type: Troubleshooting

Galera Cluster uses optimistic row locking, as opposed to pestimistic locking used by MySQL and MariaDB. Galera's attitude about locking rows can sometimes cause, especially in a cluster with many nodes, transactions to be partially rolled back and generate an error message about a deadlock. Understanding and awareness of the possibility of this situation can be reduce or eliminate problems.

.. rst-class:: section-heading
.. rubric:: Explanation

When a transaction involves an ``UPDATE``, ``REPLACE``, or any SQL statement that affects existing data, MySQL and MariaDB will lock the rows so that no other client can change the same rows during the transaction. This is known as pessimistic locking: the assumption that something might go wrong, so it's better to lock the rows.

When such a transaction is started with Galera Cluster running, it will do the same locally.  However, it won't make sure the other nodes have also locked the rows in the table. As a result, there may be a node that is in the midst of a transaction that is changing the same rows and has locked them. Galera is optomistic that there is very little likelihood of this occurring and a conflict arising.  Otherwise, each transaction would take much longer as it waits for each node to report it has locked the rows before proceeding.

This is a performance choice: assume the worst and lock rows on all nodes for all data changing transactions and thereby reduce overall performance; or assume everything will be fine and lock rows locally only and resolve the rare problems if they ever occur. Galera chooses improving overall performance, over draining performance to protect against the rare exception.


.. rst-class:: section-heading
.. rubric:: Scenario

To understand this situation better, let's look at a possible scenario in which this problem may occur.  Suppose we're trying to change the data in a table using the ``UPDATE`` statement.  For instance, suppose we have a database for a ``store`` and we sell ``toys``, with the tables named accordingly.  To do this, we start a transaction like so:

.. code-block:: mysql

   START TRANSACTION;

   UPDATE toys
   SET price = price * 1.05
   WHERE toy_category = 'baseball_equip';

   SELECT toy_id, toy, price
   FROM toys
   WHERE toy_category = 'baseball_equip'
   AND age_category = 'pre-teen';

   ERROR 1213 (40001):
   Deadlock found when trying to get lock;
   try restarting transaction

   UPDATE toys
   SET price = price * .90
   WHERE toy_category = 'baseball_equip'
   AND age_category = 'pre-teen'
   AND price > 10;

   COMMIT;

Before discussing the problems, let's review these SQL statements. The first one starts the transaction. The first  ``UPDATE`` increases the price of baseball equipment by five percent. We've omitted the results for each of these statements, except for the error message we'll look at in a moment. Then we execute a ``SELECT`` to check the price of baseball equipment for pre-teen children.  To this, we get an error message saying it can't get a table or a row lock, but it doesn't say which table |---| although we can assume it's ``toys`` |---| or why it would need a lock just to read the table and rows.

After this, there is a second ``UPDATE`` that reduces the price of baseball equipment for pre-teen children that cost more than ten dollars by ten percent |---| this is based on the new, increased price. We end the transaction with a ``COMMIT`` statement.

When we check the tables, we find that the first ``UPDATE`` failed, but the second ``UPDATE`` was executed on all of the nodes. As a result, some rows weren't updated when they would have been given the five percent increase that didn't execute, and all rows that were decreased too much since the five percent increase didn't happen before the ten percent decrease.

Normally, since all of these SQL statements are valid, both ``UPDATE`` statements would have executed without any problems, and there wouldn't have been an error message.  The problem was caused because another node had started a transaction before this one started, giving it a lower GTID sequence number, and was executing an SQL statement to change data for the same rows, but maybe not even the ``price`` column. It committed the transaction after the first ``UPDATE`` statement in the example above, and before the ``SELECT`` statement. Even though the error message is actually for the first ``UPDATE``, which was blocked from executing, it was returned for the ``SELECT`` since it was the first change Galera had to report the error. What may be particularly disturbing is that the next ``UPDATE`` was allowed to be executed, even though it was part of a transaction that included a statement that had failed.

.. rst-class:: section-heading
.. rubric:: Work-Around

Once you understand how Galera works, you can prevent problems that may occur as a result of its optimistic locking policy.  To work-around this situation is to ``ROLLBACK`` a transaction that receives an error message saying there is a deadlock, like the one above.

Don't add to the optimism by hoping the error and locking problem doesn't matter since it was strangely returned for a ``SELECT`` or an unimportant and unrelated SQL statement.  Cancel the transaction and start again.  Probably, the other transaction on the other node will have finished and been committed by the time you start the transaction again.  Then you can decide if you want to adjust your SQL statements or to re-enter them the same way.


.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_debug <wsrep_debug>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
