.. meta::
   :title: Debugging Transaction Conflicts in Galera Cluster
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
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           .. cssclass:: here

           - :doc:`Tutorial Articles <./index>`

        .. cssclass:: sub-links

           - :doc:`Training Videos <../videos/index>`

      - :doc:`FAQ <../../faq>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`debugging-transaction-conflicts`:

================================
Debugging Transaction Conflicts
================================

.. rst-class:: article-stats

   Length:  1,086 words; Writer: Philip Stoev; Published: June 29, 2015; Topic: General; Level: Beginner

If you are using Galera Cluster in multi-master mode, you will most likely run into transaction conflicts if two clients attempt to modify the same row at the same time. Such conflicts are reported a deadlock errors to the application.
Legacy applications are frequently unable to handle transaction conflicts properly and may not provide sufficient information to debug the source of the problem.

If the ``wsrep_log_conflicts`` option is set, Galera can output all the information about transaction conflicts that is available to it to the error log. As it is a dynamic option, you can enable it while the server is running, collect some entries for examination, and disable it to avoid filling up the log.

.. rst-class:: section-heading
.. rubric:: Decoding the Output

The output from ``wsrep_log_conflicts`` may look a bit intimidating at first, but in fact contains a lot of information that can be used to pin-point the offending application, module or SQL operation. The relevant pieces of information have been underlined:

.. code-block:: console

   *** Priority TRANSACTION:
   TRANSACTION 1375, ACTIVE 0 sec starting index read
   mysql tables in use 1, locked 1
   1 lock struct(s), heap size 360, 0 row lock(s)
   MySQL thread id 2, OS thread handle 0x7fbbbc1f4700, query id 52 System lock

   *** Victim TRANSACTION:
   TRANSACTION 1374, ACTIVE 23 sec starting index read
   mysql tables in use 1, locked 1
   4833 lock struct(s), heap size 554536, 1004832 row lock(s), undo log entries 934296
   MySQL thread id 5, OS thread handle 0x7fbbb4601700, query id 50
   localhost ::1 root updating
   update t1 set f2 = 'problematic_key_value21'
   *** WAITING FOR THIS LOCK TO BE GRANTED:
   RECORD LOCKS space id 8 page no 4 n bits 280 index `PRIMARY`
   of table `test`.`t1` trx id 1374 lock_mode X
   Record lock, heap no 1 PHYSICAL RECORD: n_fields 1; compact format; info bits 0
   0: len 8; hex 73757072656d756d; asc supremum;;

   Record lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info bits 0
   0: len 4; hex 80000001; asc     ;;
   1: len 6; hex 00000000055e; asc      ^;;
   2: len 7; hex 39000021fd0110; asc 9  !   ;;
   3: len 30; hex 70726f626c656d617469635f6b65795f76616c7565323120202020202020; asc problematic_key_value21       ; (total 50 bytes);

   ...

   2015-06-29 09:41:02 7900 [Note] WSREP: cluster conflict due to high priority abort for threads:
   2015-06-29 09:41:02 7900 [Note] WSREP: Winning thread:
   THD: 2, mode: applier, state: executing, conflict: no conflict, seqno: 24
   SQL: (null)
   2015-06-29 09:41:02 7900 [Note] WSREP: Victim thread:
   THD: 5, mode: local, state: executing, conflict: no conflict, seqno: -1
   SQL: update t1 set f2 = 'problematic_key_value21'

Galera provides the following information:

ACTIVE 23 sec - how long the victim transaction has been running before it was aborted. Long-running transactions are more prone to being unable to complete due to other transactions committing in the meantime.

Consider breaking down such transactions into smaller parts or changing them to modify a smaller number of rows. Transactions that perform housekeeping can be modified to do less work, but run more frequently, or be moved to a dedicated maintenance window or a period of lower server activity.

MySQL thread id 5 - the ID of the thread that was aborted due to the conflict.
This ID is the same that is used in ``SHOW PROCESSLIST``, the query log and the slow query log, so can be used to cross-reference with those sources of information

.. code-block:: console

   localhost ::1 root - the username of the client for the aborted transaction and the host the client connected from.
   update t1 set ... The SQL string of the query that was aborted.

For multi-statement transactions, the SQL string may not be available, or show simply COMMIT, if the conflict was detected at commit time.

index `PRIMARY` - the name of the index that was used by the aborted query.
PHYSICAL RECORD - a dump of the record or records where the conflict occurred.
This section comes directly from the InnoDB storage engine and follows the format used in ``SHOW ENGINE INNODB STATUS``.

The record with heap no 1 can be disregarded, while the following entries contain the actual conflicting records from the table.

hex 80000001 - in our example, this is the hex dump of the primary key.
As the key is declared as ``UNSIGNED INTEGER``, the value has a leading sign bit that should be taken into account when converting to decimal.

problematic_key_value21 - any string fields will be decoded and visible in the output.

seqno: 24 - the binary log ID of the winning transaction.


.. rst-class:: section-heading
.. rubric:: Determining the Winning Transaction

All the information from the output above, except for the seqno, pertains to the victim transaction of a conflict. Sometimes it is useful to determine the transaction that won the conflict and was not aborted, and the seqno can be used to obtain that information from the binary log.

In order to be able to fetch this information, the server needs to be running with binary logging enabled. If ``log-slave-updates`` is enabled, then the binlog on each server will contain all updates, so only one server needs to be searched in order to find the transaction. Otherwise the binlogs of all servers need to be searched separately.

MariaDB Cluster provides the actual SQL update statements from the transaction if the ``--binlog-annotate-row-events`` option is enabled. Galera Cluster and Percona XtraDB Cluster will only provide a list of the updates made by the transaction.

Unfortunately one needs to search through the entire binlog for the seqno in question, which is called Xid in the binlog:

.. code-block:: console

   $ mysqlbinlog var/mysqld.2/data/0.000001 | grep 'Xid = 3'
   #150629  0:46:45 server id 2  end_log_pos 644 CRC32 0x39cbbd68  Xid = 3

This provides the server id that executed the winning transaction, plus the position in the binlog when the transaction ended. We can use mysqlbinlog again to display the binlog up to and including the winning transaction:

.. code-block:: console

   $ mysqlbinlog var/mysqld.2/data/0.000001 --server-id=2 --stop-position=644 --base64-output=DECODE-ROWS --verbose

   ...

   BEGIN
   /*!*/;
   # at 513
   #150629  0:46:45 server id 2  end_log_pos 559 CRC32 0xae3feaec  Table_map: `test`.`t1` mapped to number 70
   # at 559
   #150629  0:46:45 server id 2  end_log_pos 613 CRC32 0x77b280b0  Update_rows: table id 70 flags: STMT_END_F
   ### UPDATE `test`.`t1`
   ### WHERE
   ###   @1=1
   ###   @2=1
   ### SET
   ###   @1=1
   ###   @2=50
   # at 613
   #150629  0:46:45 server id 2  end_log_pos 644 CRC32 0x39cbbd68  Xid = 3
   COMMIT/*!*/;
   DELIMITER ;

From this output, we can see what updates the winning transaction made, as artificially-generated SQL statements. MariaDB Cluster with ``--binlog-annotate-row-events`` would provide the original SQL that was issued.
