================================
Restarting the Cluster
================================
.. _`Restarting the Cluster`:

Occasionally, you may have to restart an entire Galera Cluster.  This may happen, for example, when there is a power failure in which every node is shut down and you have no ``mysqld`` process.  Restarting a cluster, starting nodes in the wrong order, starting the wrong nodes first, can be devastating and lead to loss of data.

When restarting an entire Galera Cluster, you'll need to determine which node has the most advanced node state ID. This is covered in the next section.  Once you've identified the most advanced node, you'll need to start that node first.  Then you can start the rest of the nodes in any order.  They will each look to the first node as the most up-to-date node.  


----------------------------------
Identifying the Most Advanced Node
----------------------------------
.. _`Identify Most Advanced Node`:

Identifying the most advanced node state ID is done by comparing the :term:`Global Transaction ID` values on each node in your cluster.  You can find this in the ``grastate.dat`` file, located in the data directory for your database.

If the ``grastate.dat`` file looks like the example below, you have found the most advanced node state ID:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   8204503945773
	cert_index:

To find the sequence number of the last committed transaction, run ``mysqld`` with the ``--wsrep-recover`` option.  This recovers the InnoDB table space to a consistent state, prints the corresponding Global Transaction ID value into the error log, and then exits.  Here's an example of this:

.. code-block:: console

	130514 18:39:13 [Note] WSREP: Recovered position: 5ee99582-bb8d-11e2-b8e3-
	23de375c1d30:8204503945771

This value is the node state ID.  You can use it to update manually the ``grastate.dat`` file, by entering it in the value of the ``seqno`` field. As an alternative, you can just let ``mysqld_safe`` recover automatically and pass the value to your database server the next time you start it.


--------------------------------------
Identifying Crashed Nodes
--------------------------------------
.. _`Identify Crashed Node`:

You can easily determine if a node has crashed by looking at the contents of the ``grastate.dat`` file. If it looks like the example below, the node has either crashed during execution of a non-transactional operation (e.g., ``ALTER TABLE``), or the node aborted due to a database inconsistency.

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   -1
	cert_index:

It's possible for you to recover the :term:`Global Transaction ID` of the last committed transaction from InnoDB, as described above. However, the recovery is rather meaningless.  After the crash, the node state is probably corrupted and may not prove functional.  

If there are no other nodes in the cluster with a well-defined state, there is no need to preserve the node state ID.  You must perform a thorough database recovery procedure, similar to that used on stand-alone database servers.  Once you recover one node, use it as the first node in a new cluster.


