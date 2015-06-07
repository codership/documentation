============================
 Frequently Asked Questions
============================
.. _`Frequently Asked Questions`:

This chapter lists a number of frequently asked questions on Galera Cluster and other related matters.

.. rubric:: What does "``Commit failed for reason: 3``" mean?
.. _`commit-failed-reason-3`:

In the event that you have :ref:`wsrep_debug <wsrep_debug>` turned ``ON``, you may occasionally see a message noting that a commit has failed due to reason ``3``.  For example:


.. code-block:: text
  
      110906 17:45:01 [Note] WSREP: BF kill (1, seqno: 16962377), victim:  (140588996478720 4) trx: 35525064
      110906 17:45:01 [Note] WSREP: Aborting query: commit
      110906 17:45:01 [Note] WSREP: kill trx QUERY_COMMITTING for 35525064
      110906 17:45:01 [Note] WSREP: commit failed for reason: 3, seqno: -1

When attempting to apply a replicated write-set, slave threads occasionally encounter lock conflicts with local transactions, which may already be in the commit phase.  In such cases, the node aborts the local transaction, allowing the slave thread to proceed.

This is a consequence of optimistic transaction execution.  The database server executes transaction under the expectation that there will be no row conflicts.  It is an expected issue in a multi-master configuration.

To mitigate such conflicts:

- Use the cluster in a master-slave configuration.  Direct all writes to a single node.

- Use the same approaches as for master-slave read/write splitting.



.. rubric:: What if connections give an ``Unknown command`` error?
.. _`connection-unknown-command`:

Your cluster experiences a temporary split, during which a portion of the nodes lose connectivity to the :term:`Primary Component`.  When it reconnects, nodes from the former nonoperational component drop database client connections.  New connections to the database client returns ``Unknown command`` errors.

What's happening is that the node does not consider yet itself a part of the Primary Component.  While it has restored network connectivity, it still to resynchronize itself with the cluster.  MySQL does not have an error code for the node lacking Primary status and defaults to an ``Unknown command`` message.

Nodes in a nonoperational component must regain network connectivity with the Primary Component, process a state transfer and catch up with the cluster before they can resume normal operation.





.. rubric:: What if ``mysqldump`` SST returns SQL Syntax Errors?

You configure :ref:`wsrep_sst_method <wsrep_sst_method>` to use ``mysqldump`` for :term:`State Snapshot Transfer`.  If the process fails for any reason, the node writes a ``SQL SYNTAX`` entry to the error log.  The pseudo-statement within the SQL Syntax entry contains the actual error message.

Read the pseudo-statement within the SQL syntax entry.  It provides the information you need to correct the problem.


.. rubric:: What if the node crashes during ``rsync`` SST

You configure :ref:`wsrep_sst_method <wsrep_sst_method>` to use ``rsync`` for :term:`State Snapshot Transfer`.  If the node crashes before the state transfer is complete, it may cause the ``rsync`` process to hang forever, occupying the port and not allowing you to restart the node.  In the event that this occurs, the error logs for the database server show that the port is in use.

To correct the issue, kill the orphaned ``rsync`` process .  For instance, if you find the process had a pid of ``501``, you might run the following command:

.. code-block:: console

   # kill 501

Once you kill the orphaned process, it frees up the relevant ports and allows you to restart the node.


