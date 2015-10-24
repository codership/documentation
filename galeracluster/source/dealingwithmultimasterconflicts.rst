======================================
 Dealing with Multi-Master Conflicts
======================================
.. _`Dealing with Multi-Master Conflicts`:

The type of conflicts that you need to address in multi-master database environments are typically row conflicts on different nodes.

Consider a situation in a multi-master replication system.  Users can submit updates to any database node.  In turn two nodes can attempt to change the same database row with different data.  Galera Cluster copes with situations such as this by using certification-based replication.

.. note:: **See Also**: For more information, see :doc:`certificationbasedreplication`.

-----------------------------------
 Diagnosing Multi-Master Conflicts
-----------------------------------

.. index::
   pair: Parameters; wsrep_debug
.. index::
   pair: Parameters; wsrep_local_bf_aborts
.. index::
   pair: Parameters; wsrep_local_cert_failures
.. index::
   pair: Parameters; cert.log_conflicts
.. index::
   pair: Logs; Debug log

There are a few techniques available to you in logging and monitoring for problems that may indicate multi-master conflicts.

- :ref:`wsrep_debug <wsrep_debug>` tells the node to include additional debugging information in the server output log.  You can enable it through the configuration file:

  .. code-block:: ini

     # Enable Debugging Output to Server Error Log
     wsrep_debug=ON

  Once you turn debugging on, you can use your preferred monitoring software to watch for row conflicts.
     
  .. code-block:: text

     110906 17:45:01 [Note] WSREP: BF kill (1, seqno: 16962377), victim:  (140588996478720 4) trx: 35525064
     110906 17:45:01 [Note] WSREP: Aborting query: commit
     110906 17:45:01 [Note] WSREP: kill trx QUERY_COMMITTING for 35525064
     110906 17:45:01 [Note] WSREP: commit failed for reason: 3, seqno: -1


  .. note:: **Warning**: In addition to useful debugging information, this parameter also causes the database server to print authentication information, (that is, passwords), to the error logs.  Do not enable it in production environments.
     
- In the event that you are developing your own notification system, you can use status variables to watch for conflicts:

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_local_bf_aborts';

     +-----------------------+-------+
     | Variable_name         | Value |
     +-----------------------+-------+
     | wsrep_local_bf_aborts | 333   |
     +-----------------------+-------+
          
     SHOW STATUS LIKE 'wsrep_local_cert_failures';

     +---------------------------+-------+
     | Variable_name             | Value |
     +---------------------------+-------+
     | wsrep_local_cert_failures | 333   |
     +---------------------------+-------+
     
  :ref:`wsrep_local_bf_aborts <wsrep_local_bf_aborts>` gives the total number of local transactions aborted by slave transactions while in execution.  :ref:`wsrep_local_cert_failures <wsrep_local_cert_failures>` gives the total number of transactions that have failed certification tests.

- Lastly, you can enable conflict logging features through :ref:`wsrep_log_conflicts <wsrep_log_conflicts>` and :ref:`cert.log_conflicts <cert.log_conflicts>`.

  .. code-block:: ini

     # Enable Conflict Logging
     wsrep_log_conflicts=ON
     wsrep_provider_options="cert.log_conflicts=YES"

  These parameters enable different forms of conflict logging on the database server.  When turned on, the node logs additional information about the conflicts it encounters, such as the name of the table and schema where the conflict occurred and the actual values for the keys that produced the conflict.
  
  .. code-block:: text
		  
     7:51:13 [Note] WSREP: trx conflict for key (1,FLAT8)056eac38 0989cb96:
     source: cdeae866-d4a8-11e3-bd84-479ea1a1e941 version: 3 local: 1 state:
     MUST_ABORT flags: 1 conn_id: 160285 trx_id: 29755710 seqnos (l: 643424,
     g: 8749173, s: 8749171, d: 8749171, ts: 12637975935482109) <--X-->
     source: 5af493da-d4ab-11e3-bfe0-16ba14bdca37 version: 3 local: 0 state:
     APPLYING flags: 1 conn_id: 157852 trx_id: 26224969 seqnos (l: 643423,
     g: 8749172, s: 8749171, d: 8749170, ts: 12637839897662340)

------------------------------
 Auto-committing Transactions
------------------------------

.. index::
   pair: Parameters; wsrep_retry_autocommit

When two transactions come into conflict, the later of the two is rolled back by the cluster.  The client application registers this rollback as a deadlock error.  Ideally, the client application *should* retry the deadlocked transaction, but not all client applications have this logic built in.
   
In the event that you encounter this problem, you can set the node to attempt to auto-commit the deadlocked transactions on behalf of the client application, using the :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>` parameter.

.. code-block:: ini

   wsrep_retry_autocommit=4

When a transaction fails the certification test due to a cluster-wide conflict, this tells the node how many times you want it to retry the transaction before returning a deadlock error.
   
.. note:: Retrying only applies to auto-commit transactions, as retrying is not safe for multi-statement transactions.

---------------------------------------
 Working Around Multi-Master Conflicts
---------------------------------------

.. index::
   pair: Parameters; wsrep_retry_autocommit

While Galera Cluster resolves multi-master conflicts automatically, there are steps you can take to minimize the frequency of their occurrence.

- Analyze the hot-spot and see if you can change the application logic to catch deadlock exceptions.

- Enable retrying logic at the node level using, :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>`.

- Limit the number of master nodes or switch to a master-slave model.
  
.. note:: If you can filter out the access to the hot-spot table, it is enough to treat writes only to the hot-spot table as master-slave.
