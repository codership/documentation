================================
Restarting the Cluster
================================
.. _`Restarting the Cluster`:

Occasionally, you may have to restart the entire Galera Cluster.  This may happen, for example, in the case of a power failure where every node is shut down and you have no ``mysqld`` process at all.

To restart an entire Galera Cluster, complete the following steps:

1. Identify the node with the most advanced node state ID.

2. Start the most advanced node as the first node of the cluster.

3. Start the rest of the node as usual.


----------------------------------
Identifying the Most Advanced Node
----------------------------------
.. _`Identify Most Advanced Node`:

Identifying the most advanced node state ID is managed by comparing the :term:`Global Transaction ID` values on different nodes in your cluster.  You can find this in the ``grastate.dat`` file, located in the datadir for your database.

If the ``grastate.dat`` file looks like the example below, you have found the most advanced node state ID:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   8204503945773
	cert_index:

To find the sequence number of the last committed transaction, run ``mysqld`` with the ``--wsrep-recover`` option.  This recovers the InnoDB table space to a consistent state, prints the corresponding Global Transaction ID value into the error log, and then exits.  For example:

.. code-block:: console

	130514 18:39:13 [Note] WSREP: Recovered position: 5ee99582-bb8d-11e2-b8e3-
	23de375c1d30:8204503945771

This value is the node state ID.  You can use it to manually update the ``grastate.dat`` file, by entering it for the ``seqno`` field, or let ``mysqld_safe`` recover automatically and pass the value to your database server the next time you start it.

------------------------------
'Safe to Bootstrap' Protection
------------------------------
.. _`'Safe to Bootstrap' Protection`:

Starting with provider version 3.19, Galera has an additional protection against attempting to boostrap the cluster using a node that may not have been the last node remaining in the cluster prior to cluster shutdown.

If Galera can conclusively determine which node was the last node standing, it will be marked as 'safe to bootstrap', as seen in this example ``grastate.dat``:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5981f182-a4cc-11e6-98cc-77fabedd360d
	seqno:   1234
	safe_to_bootstrap: 1

Such a node can be used to bootstrap the cluster. Attempting to boostrap using any other node will cause the following error message:

.. code-block:: console

	2016-11-07 01:49:19 5572 [ERROR] WSREP: It may not be safe to bootstrap the cluster from this node.
	It was not the last one to leave the cluster and may not contain all the updates.
	To force cluster bootstrap with this node, edit the grastate.dat file manually and set safe_to_bootstrap to 1 .

To override this protection, edit the ``safe_to_bootstrap`` line in the ``grastate.dat`` file of the node you intend to use as the first node.

In the case when all nodes crashed simultaneously, no node will be considered safe to bootstrap until the ``grastate.dat`` file is edited manually.

---------------
Gcache Recovery
---------------

Starting with provider version 3.19, Galera provides the :ref:`gcache.recover <gcache.recover>` parameter. If set to ``yes``, Galera will attempt to recover the gcache on node startup.

If gcache recovery is successful, the node will be in position to provide IST to other joining nodes, which can speed up the overall restart time for the entire cluster.

Gcache recovery requires that the entire gcache file is read twice. For large gcache files located on slow disks, this operation may take some time.

Gcache recovery is a "best effort" operation. If recovery was not successful, the node will continue to operate normally however other nodes will fall back to SST when attempting to join.

--------------------------------------
Identifying Crashed Nodes
--------------------------------------
.. _`Identify Crashed Node`:

If the ``grastate.dat`` file looks like the example below, the node has either crashed during execution of a non-transactional operation, (such as ``ALTER TABLE``), or aborted due to a database inconsistency:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   -1
	cert_index:

It is possible for you to recover the :term:`Global Transaction ID` of the last committed transaction from InnoDB, as described above, but the recovery is rather meaningless.  After the crash, the node state is probably corrupted and may not even prove functional.

In the event that there are no other nodes in the cluster with a well-defined state, then there is no need to preserve the node state ID.  You must perform a thorough database recovery procedure, similar to that used on standalone database servers.  Once you recover one node, use it as the first node in a new cluster.

