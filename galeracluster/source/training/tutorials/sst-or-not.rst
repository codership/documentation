.. cssclass:: tutorial-article
.. _`sst-or-not`:

==========================
To SST or Not To SST?
==========================

.. rst-class:: list-stats

   Length:  1001 words; Writer: Philip Stoev; Published: December 6, 2016; Topic: General; Level: Intermediate

If a node leaves the cluster and subsequently rejoins, Galera will internally make sure that the node is brought up to speed with the rest of the cluster. It is important for DBAs that this process completes quickly, so ideally SST is avoided altogether and IST is used. However, when looking at the log, SST is still mentioned even if IST is ultimately chosen, which may cause confusion.
In this article, we will describe the entire process of getting a restarted node back to speed with the rest of the cluster and explain the logic behind the various log messages.

--------------------------------
Basic Principles
--------------------------------

State transfers in Galera are governed by the following basic principles:
The cluster will pick a donor node using an algorithm that favors IST and attempts to avoid any transfers over a wide-area network. A specific donor can be explicitly chosen using the wsrep_sst_donor variable.
The joiner will declare if IST, SST or both are possible:

If the ``mysqld`` process was shut down and is now being restarted, SST or IST are both possible;
If a node is starting from an unknown state (such as empty database or a missing grastate.dat file), only SST can be performed;
If the node was temporarily disconnected from the cluster while the mysqld process remains running, only IST can happen if the SST method is set to xtrabackup, xtrabackup-v2 or rsync. This is because the entire data directory can not be copied over to a running server.
If both methods are possible, as is the case during a vanilla server restart, it is up to the donor node to decide if it can deliver IST. If needed, the donor has the ability to fall back to SST instead.

--------------------------------
Step-by-Step Walkthrough
--------------------------------

This section describes the entire state transfer process during a normal server restart and shows the typical log messages that happen at each phase.
First, the joining node establishes its current replication position and compares it to the position the rest of the cluster has moved to while the node was disconnected:

.. code-block:: console

   WSREP: State transfer required:
        Group state: cdecf830-bad9-11e6-850b-d6cd097d8360:17
        Local state: cdecf830-bad9-11e6-850b-d6cd097d8360:3
   ...
   WSREP: Gap in state sequence. Need state transfer.

Then, it prepares its own side for receiving a state transfer. Since the data can come as either IST and SST, the joiner prepares for both and runs the SST script just in case:

.. code-block:: console

   WSREP: Running: 'wsrep_sst_rsync --role 'joiner' --address '127.0.0.2:13011' --datadir '/home/philips/git/mysql-wsrep-bugs-5.6/mysql-test/var/mysqld.3/data/' --defaults-file '/home/philips/git/mysql-wsrep-bugs-5.6/mysql-test/var/my.cnf' --defaults-group-suffix '.3' --parent '10676'  '' '
   WSREP: Prepared SST request: rsync|127.0.0.2:13011/rsync_sst
   ...
   IST receiver addr using tcp://127.0.0.1:13010
   Prepared IST receiver, listening at: tcp://127.0.0.1:13010

Now, it is time to select the actual donor node. This decision is made by the cluster as a whole, so this message is printed on all nodes:

Member 0.0 (fedora20) requested state transfer from '*any*'. Selected 2.0 (fedora20)(SYNCED) as donor.

The donor node now joins the action. If it determines that it can serve IST after all, it calls the SST script on its side using the ``--bypass`` parameter. This instructs the script that no actual transfer of the entire database needs to happen, so the script exits quickly.

.. code-block:: console

   WSREP: Running: 'wsrep_sst_rsync --role 'donor' --address '127.0.0.2:13011/rsync_sst' --socket '/home/philips/git/mysql-wsrep-bugs-5.6/mysql-test/var/tmp/mysqld.1.sock' --datadir '/home/philips/git/mysql-wsrep-bugs-5.6/mysql-test/var/mysqld.1/data/' --defaults-file '/home/philips/git/mysql-wsrep-bugs-5.6/mysql-test/var/my.cnf' --defaults-group-suffix '.1'   '' --gtid 'cdecf830-bad9-11e6-850b-d6cd097d8360:0' --bypass'
   WSREP_SST: [INFO] Bypassing state dump. (20161205 14:02:54.673)

on the joiner side, the empty SST is also wrapped up and the rsync process that was spawned and remained unused is cleaned up. The InnoDB storage engine can now be initialized:

.. code-block:: console

   WSREP: 2.0 (fedora20): State transfer to 0.0 (fedora20) complete.
   Joiner cleanup. rsync PID: 10706 (20161205 03:03:38.482)
   Joiner cleanup done. (20161205 03:03:39.003)
   ...
   InnoDB: 5.6.34 started; log sequence number 1636039

With InnoDB up and running, the actual IST can follow, as seen in the donor log:

.. code-block:: console

   async IST sender starting to serve tcp://127.0.0.1:13010 sending 4-17
   ...
   WSREP: async IST sender served

and in the joiner log:

.. code-block:: console

   WSREP: Receiving IST: 14 writesets, seqnos 3-17
   ...
   WSREP: IST received: cdecf830-bad9-11e6-850b-d6cd097d8360:17
   WSREP: 0.0 (fedora20): State transfer from 2.0 (fedora20) complete.

The entire procedure ends when the replication events from the IST have been applied and the node has fully caught up with the cluster:

.. code-block:: console

   WSREP: Shifting JOINED -> SYNCED (TO: 17)
   WSREP: Synchronized with group, ready for connections

------------
Catch-Up
------------

After the joiner has received a State Transfer, it must also catch up with any transactions that were issued on the rest of the cluster while the State Transfer was in progress. Those transactions are continuously received by the joiner and stored in the gcache. As soon as the state transfer completes, the donor needs to apply them all.

An attentive reader may ask "What happens if the joining node is never able to catch up because there are too many new transactions? Will flow-control kick in?". The answer is yes, however rather than applying flow control immediately and stopping the entire cluster in its tracks until the catch-up phase is complete, Galera uses a heuristics to determine when throttling is required.
If the node is able to make progress towards catching up, as evidenced by a decreasing length of its receive queue, no flow control will kick in. However, if the node begins to fall further behind and the queue continues to grow, the cluster will be throttled so that the node is given some breathing room. This way the entire procedure for joining a new node is guaranteed to complete even in the presence of continuing load on the database.
