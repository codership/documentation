========================
Server Error Log
========================
.. _`server-error-log`:



.. rubric:: ``Node 0 (XXX) requested state transfer from '*any*'. Selected 1 (XXX) as donor.``
.. _`node-requested-sst-from-any`:

The node is attempting to initiate a :term:`State Snapshot Transfer`.

In the event that you do not explicitly set the donor node through :ref:`wsrep_sst_donor <wsrep_sst_donor>`, the *Group Communication* module will select a donor based on the information available about the node states.

Group Communication monitors node states for the purposes of flow control, state transfers and quorum calculations.  It ensures that a node that shows as ``JOINING`` doesn't count towards flow control and quorum.

A node can serve as a donor when it is in the ``SYNCED`` state.  The joiner node selects a donor from the available synced nodes.  It shows preference to synced nodes that have the same :ref:`gmcast.segment <gmcast.segment>` wsrep Provider option, or it selects the first in the index.  When a donor node is chosen, its state changes immediately to ``DONOR``. It's no longer available for requests.

If a node can find no free nodes that show as ``SYNCED``, the joining node reports the following:

.. code-block:: text

   Requesting state transfer failed: -11(Resource temporarily
   unavailable).  Will keep retrying every 1 second(s).

The joining node will continue to retry the state transfer request.



.. rubric:: ``SQL SYNTAX`` Errors
.. _`sql-syntax`:

When a :term:`State Snapshot Transfer` fails using ``mysqldump`` for any reason, the node will write a ``SQL SYNTAX`` message into the server error logs.

This is a pseudo-statement, though.  You can find the actual error message the state transfer returned within the ``SQL SYNTAX`` entry.  It will provide the information you need to correct the problem.


.. rubric:: ``Commit failed for reason: 3``
.. _`commit-failed-reason-3`:

When you have :ref:`wsrep_debug <wsrep_debug>` turned ``ON``, you may occasionally see a message noting that a commit has failed due to reason ``3``.  Below is an example of this:

.. code-block:: text
  
      110906 17:45:01 [Note] WSREP: BF kill (1, seqno: 16962377), victim:  (140588996478720 4) trx: 35525064
      110906 17:45:01 [Note] WSREP: Aborting query: commit
      110906 17:45:01 [Note] WSREP: kill trx QUERY_COMMITTING for 35525064
      110906 17:45:01 [Note] WSREP: commit failed for reason: 3, seqno: -1

When attempting to apply a replicated write-set, slave threads occasionally encounter lock conflicts with local transactions, which may already be in the commit phase.  In such cases, the node aborts the local transaction, allowing the slave thread to proceed.

This is a consequence of optimistic transaction execution.  The database server executes transaction under the expectation that there will be no row conflicts.  It is an expected issue in a multi-master configuration.

To mitigate such conflicts, there are a couple of things you can do:

- Use the cluster in a master-slave configuration.  Direct all writes to a single node.

- Use the same approach as master-slave read/write splitting.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
  
