.. meta::
   :title: Synchronizing a Transaction Before Executing Another
   :description:
   :language: en-US
   :keywords:
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

      - :doc:`Galera Functions <../documentation/wsrep-functions>`
      - :ref:`wsrep_provider_version <wsrep_provider_version>`
      - :ref:`wsrep_last_written_gtid() <WSREP_LAST_WRITTEN_GTID>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-sync-transaction-first`:

======================================================
Synchronizing a Transaction Before Executing Another
======================================================

.. rst-class:: article-stats

   Length: 391 words; Published: May 30, 2019; Updated: October 22, 2019; Category: Schema & SQL; Type: Best Practices

There are times in which a user |---| or an application |---| will perform complex tasks, to add and change data dynamically and contingent upon whatever factors might be important to the user. Along these lines, someone or an application may enter a transaction, but may not want it commited until a previous transaction has been committed.  This can be a bit tricky, especially when a cluster is using a load balancer:  The second transaction may have be sent to a different node than the first.  If that happens, the user will have difficulty being sure that the second node has already replicated the first transaction. Fortunately, there are now some Galera functions that can help.

Prior to version 4.0 of Galera Cluster, you could use the :ref:`wsrep_sync_wait <wsrep_sync_wait>` session variable to wait for the node to be synchronized before executing a transaction.  It would cause the node to enable causality checks, holding any new queries until the database server is synchronized with all updates that were made prior to the start of the current transaction. While this method does ensure that the node reaches the most up-to-date state before executing a query, it also means that the node may be waiting to receive updates that might have nothing to do with a query it's waiting to execute. If those unrealted queries are large and time consuming, the pending transaction will be significantly delayed and the apparent performce will be reduced.

Beginning with version 4.0 of Galera Cluster, you can use Galera functions to make transactions contingent upon a specific transaction.  The node will waits only until that transaction, based on its GTID, is applied before executing the query.

.. rst-class:: section-heading
.. rubric:: Scenario

With the preamble above in mind, consider this scenario:  Suppose we start a transaction on one node, then we make some schema and data changes to a huge table during that transaction, and then we execute ``COMMIT`` to finish and commit the transaction.  As an example, imagine we have a database for a ``bookstore``, with a table for ``books`` we sell.  That table is huge, containing millions of rows of data with many columns, including a some ``BLOB`` columns, and it has a few indexes. The processing will take quite a while.

Let's be more specific, for this example: The ``books`` table contains a column for the ISBN code for each book, but it's the older 10-digit code.  We want to convert to the new 13-digit code.  Some time ago, as a temporary work-around, we created a user function called, ``CONVERT_ISBN()`` that uses a `complex formula <https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation>`_ to convert from the old ISBN to the new one. That worked fine for a while, but one of our main vendors has stopped using the old ISM and will only use the new 13-digit ISBN codes. They've just given us a file that we want to import into our books table. So we decide to alter our ``books`` table to the new system and stop relying on our user function after this transaction.

The first transaction, to convert the ``books`` table, might look something like this:

.. code-block:: mysql

   START TRANSACTION;

   ALTER TABLE books DISABLE KEYS;

   ALTER TABLE books
   ADD COLUMN isbn_10 CHAR(10),
   CHANGE COLUMN isbn CHAR(14);

   UPDATE books SET isbn_10 = isbn;
   UPDATE books SET isbn = CONVERT_ISBN(isbn);

   ALTER TABLE books ENABLE KEYS;

   COMMIT;

Let's go through each SQL statement here. After this transaction is started, we disable the indexes so the schema changes and data updates will execute faster.  Then we execute an ``ALTER TABLE`` statement to add a column that will store the old 10-digit code (e.g., ``0578041065``) as a reference, and change the current ``isbn`` column to allow for thirteen digits plus the one hyphen in the book code (e.g., ``978-0578041063``). Once that's done, we execute an ``UPDATE`` statement to copy the old ISBN to ``isbn_10``, and another to convert the values in ``isbn`` to the new format.  We end by enabling the indexes, which will run for quite a while, and then ending the transaction with ``COMMIT``.

Once the transaction above has been executed and committed on all nodes, we want to execute a transaction to execute the ``LOAD DATA`` statement to import the list of new books from our vendor. But we want to be sure that all of the nodes have committed the previous transaction.  We don't want to risk that load balancer sends this transaction to a different node that has not yet changed the ``isbn`` column. It won't be wide enough for the 13-digit codes, so the import will fail.  To do this, we'll need to use one of the new Galera functions available starting in version 4.0 of Galera Cluster.

.. rst-class:: section-heading
.. rubric:: Solution

To make a transaction contingent upon the completing of a previous transaction, we will need to get the GTID for the transaction.  Much like the MySQL function, ``LAST_INSERT_ID()`` will return the number inserted the ``AUTO_INCREMENT`` column of the table, the :ref:`WSREP_LAST_WRITTEN_GTID() <WSREP_LAST_WRITTEN_GTID>` function will return the :term:`Global Transaction ID` (GTID) of the transaction. So after the first transaction is committed, we would execute the following SQL statement to get the GTID:

.. code-block:: mysql

   SET @books_change_gtid = (SELECT WSREP_LAST_WRITTEN_GTID());

To make it easier to use, we've saved the results of the ``SELECT`` with the ``WSREP_LAST_WRITTEN_GTID( )`` function in a user variable we created here. We can use that variable in the next transaction, which also will import the data file from our vendor:

.. code-block:: mysql

   START TRANSACTION;

   SELECT WSREP_SYNC_WAIT_UPTO_GTID(@books_change_gtid);

   ALTER TABLE books DISABLE KEYS;

   LOAD DATA LOCAL INFILE 'oup_books.csv'
   INTO TABLE books
   FIELDS TERMINATED BY '|'
   ENCLOSED BY '"'
   LINES TERMINATED BY '\r\n'
   IGNORE 1 LINES
   (isbn, title, author, description, publisher, pub_year, price);

   ALTER TABLE books ENABLE KEYS;

   COMMIT;

With this function, :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>` tells the node to wait until the transaction identified by the GTID given within the parentheses (the value of our user variable) is committed before processing this transaction.

.. container:: bottom-links

   Related Documents

   - :doc:`Galera Functions <../documentation/wsrep-functions>`
   - :ref:`wsrep_provider_version <wsrep_provider_version>`
   - :ref:`wsrep_last_written_gtid() <WSREP_LAST_WRITTEN_GTID>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
