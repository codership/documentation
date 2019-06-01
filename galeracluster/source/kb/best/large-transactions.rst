================================
Dealing with Large Transactions
================================
.. _`kb-best-large-transactions`:

Large transactions, especially ones deleting removes millions of rows from a table at once, can lead to diminished performance. One reason is that the table may reindexed and rescanned after each row is deleted.


.. rubric:: Scenario
   :class: kb

Suppose you have a node called ``dbhost`` with a database called ``keystone``.  Suppose further that you execute a large transaction, which includes a ``DELETE`` statement that deletes expired tokens from their table in that database and on that host. If this transaction involves millions of rows, it could affect the overall performance of the cluster.


.. rubric:: Recommendations
   :class: kb

This problem might be easily resolved by changing the size of the InnoDB buffer pool. The pool is bytes of the memory area where InnoDB caches table and index data. The larger the pool (i.e., the more RAM is used), the less the disk is  accessed, which is especially important when dealing with the same data in tables multiple times as you might in a large transaction on the same table.

To change the buffer pool size, check the value of the :ref:`innodb_buffer_pool_size <innodb_buffer_pool_size>` variable. If your servers are dedicated only to database service, try setting it to 80% of the server's physical memory size. You can use the ``free`` command to see how much memory you have.  Once you determine how much memory you can spare for the InnoDB pool, add or change a line in the server's configuration file like the following:

.. code-block:: ini

   innodb_buffer_pool_size=128M


If you must frequently perform extremely large transactions including ``DELETE`` statements, you might consider using ``pt-archiver`` from the Percona Toolkit.  It's very efficient at deleting millions of rows without reading them or reindexing after each row is deleted.

To use ``pt-archiver``, you'll have to install the Percona Toolkit. Once that's done, you would enter something like the following from the command-line to delete rows from tables (i.e., ``keystone.token``) based on a ``WHERE`` clause (i.e., datetime column ``expires`` with values before now):

.. code-block:: console

   $ pt-archiver --source h=dbhost,D=keystone,t=token \
      --purge --where "expires < NOW()" --primary-key-only \
      --sleep-coef 1.0 --txn-size 500

This allows you to delete rows efficiently from the cluster.

The ``--source`` parameter provides the host, database, and table. Since there is no  ``--destination`` parameter given, it won't move the data to another table for archiving, per the primary function of ``pt-archiver``. The ``--purge`` parameter instructs ``pt-archiver`` to remove the rows from the database. The ``--where`` parameter provides the ``WHERE`` clause of the ``DELETE`` statement.

The ``--primary-key-only`` parameter is efficient when purging rows. It prevents fetching each row in its entirety, when only the primary key column is used in the ``WHERE`` clause for ``DELETE`` statements.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :ref:`innodb_buffer_pool_size <innodb_buffer_pool_size>` variable
- `pt-archiver <http://www.percona.com/doc/percona-toolkit/2.1/pt-archiver.html>`

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
