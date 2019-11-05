.. meta::
   :title: Using Synchronization Functions in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: sub-links

         - :doc:`Troubleshooting <../trouble/index>`

         .. cssclass:: here

         - :doc:`Best Practices <./index>`

      - :doc:`Training <../../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      Related Documents

      - :ref:`wsrep_sync_wait <wsrep_sync_wait>`
      - :ref:`WSREP_LAST_WRITTEN_GTID() <WSREP_LAST_WRITTEN_GTID>`
      - :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`
      - :ref:`wsrep_provider_version <wsrep_provider_version>`

      Related Articles


.. cssclass:: library-article
.. _`kb-best-using-sync-functions`:

=================================
Using Synchronization Functions
=================================

Occasionally, an application may need to perform a critical read. Critical reads are queries that require that the local database reaches the most up-to-date state possible before the query is executed.

In Galera Cluster prior to 4.x, you could manage critical reads using the :ref:`wsrep_sync_wait <wsrep_sync_wait>` session variable.  This would cause the node to enable causality checks, holding new queries until the database server catches up with all updates that were made prior to the start of the current transaction.  While this method does ensure that the node reaches the most up-to-date state before executing the query, it also means that the node may wait to receive updates that might have nothing to do with the query at hand.

Beginning with Galera Cluster 4.0, though, you can use synchronization functions.  This allows you to tie the synchronization process to specific transactions so that the node waits only until a specific transaction is applied before executing the query.  Here is an example of how this might work:


.. rst-class:: kb
.. rubric:: Scenario

Suppose on ``node1``, you begin a transaction, make changes to a table and then commit the transaction like so:

.. code-block:: console

   START TRANSACTION;

   UPDATE table1 SET col4 = col4 * 1.2;

   COMMIT;

After that, using the :ref:`WSREP_LAST_WRITTEN_GTID() <WSREP_LAST_WRITTEN_GTID>` function, say you obtain the :term:`Global Transaction ID` of the transaction and save it to the ``$transaction_1_gtid`` variable like this:

.. code-block:: console

   $transaction_1_gtid = SELECT WSREP_LAST_WRITTEN_GTID();

Now, on ``node2``, suppose you set it to wait until it replicates and applies the transaction from ``node1`` before starting a new transaction:

.. code-block:: console

   SELECT WSREP_SYNC_WAIT_UPTO_GTID($transaction_1_gtid);

   START TRANSACTION;

Next, you execute your critical reads.


.. rst-class:: kb
.. rubric:: Recommendations

Using the :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>` function, the node waits until it has replicated and applied the given Global Transaction ID before starting a new transaction.

Synchronization Functions were introduced in Galera Cluster 4.  If you have an older version, you won't be able to use these features.  To determine which version is installed on a server, use the ``SHOW STATUS`` statement and look for the :ref:`wsrep_provider_version <wsrep_provider_version>` status variable.

.. code-block:: console

    SHOW STATUS LIKE 'wsrep_provider_version';

    +------------------------+----------------------+
    | Variable_name          | Value                |
    +------------------------+----------------------+
    | wsrep_provider_version | 25.3.5-wheezy(rXXXX) |
    +------------------------+----------------------+

The digits after the second and third decimal places are the version. The results here indicate that Galera Cluster version 3.5 is installed on the server.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
