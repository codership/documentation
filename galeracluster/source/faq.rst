============================
 Frequently Asked Questions
============================
.. _`Frequently Asked Questions`:

This page lists a number of frequently asked questions on Galera Cluster and other related matters.

.. rubric:: What is Galera Cluster?
.. _`what-is-galera-cluster`:

Galera Cluster is a write-set replication service provider in the form of the *dlopenable* library.  It provides synchronous replication and supports multi-master replication.  Galera Cluster is capable of unconstrained parallel applying (i.e., "parallel replication"), multicast replication and automatic node provisioning.

The primary focus of Galera Cluster is data consistency.  Transactions are either applied to every node or not at all.  Galera Cluster is not a cluster manager, a load balancer or a cluster monitor.  What it does is keep databases synchronized, provided they were properly configured and synchronized in the beginning.

.. rubric:: What is Galera?
.. _`what-is-galera`:

The word *galera* is the Italian word for *galley*.  The galley is a class of naval vessel used in the Mediterranean Sea from the second millennium :sub:`B.C.E.` until the Renaissance.  Although it used sails when the winds were favorable, its principal method of propulsion came from banks of oars.

In order to manage the vessel effectively, rowers had to act synchronously, lest the oars become intertwined and became blocked.  Captains could scale the crew up to hundreds of rowers, making the galleys faster and more maneuverable in combat.

.. note:: **See Also**: For more information on galleys, see `Wikipedia <http://en.wikipedia.org/wiki/Galley>`_.



.. rubric:: How are Failovers Managed?
.. _`failover`:

Galera Cluster is a true synchronous multi-master replication system, which allows the use of any or all of the nodes as master at any time without any extra provisioning.  What this means is that there is no failover in the traditional MySQL master-slave sense.

The primary focus of Galera Cluster is data consistency across the nodes.  This doesn't allow for any modifications to the database that may compromise consistency.  For instance, the node rejects write requests until the joining node synchronizes with the cluster and is ready to process requests.

The results of this is that you can safely use your favorite approach to distribute or migrate connections between the nodes without the risk of causing inconsistency.

.. note:: **See Also**: For more information on connection distribution, see :doc:`deploymentvariants`.



.. rubric:: How do I Upgrade the Cluster?
.. _`faq-upgrade`:

Periodically, updates will become available for Galera Cluster--for the database server itself or the :term:`Galera Replication Plugin`.  To update the software for a node, you would redirect client connections away from it and then stop the node. Then upgrade the node's software.  When finished, just restart the node.

.. note:: **See Also**: For more information on upgrade process, see :doc:`upgrading`.

.. rubric:: What InnoDB Isolation Levels does Galera Cluster Support?
.. _`faq-isolation-levels`:

You can use all isolation levels.  Locally, in a given node, transaction isolation works as it does natively with InnoDB.

Globally, with transactions processing in separate nodes, Galera Cluster implements a transaction-level called ``SNAPSHOT ISOLATION``.  The ``SNAPSHOT ISOLATION`` level is between the ``REPEATABLE READ`` and ``SERIALIZABLE`` levels.

The ``SERIALIZABLE`` level cannot be guaranteed in the multi-master use case because Galera Cluster replication does not carry a transaction read set.  Also, ``SERIALIZABLE`` transaction is vulnerable to multi-master conflicts.  It holds read locks and any replicated write to read locked row will cause the transaction to abort.  Hence, it is recommended not to use it in Galera Cluster.

.. note:: **See Also**: For more information, see :doc:`isolationlevels`.

	     
.. rubric:: How are DDL's Handled by Galera Cluster?
.. _`ddl-galera`:

For :abbr:`DDL (Data Definition Language)` statements and similar queries, Galera Cluster has two modes of execution:

- :term:`Total Order Isolation`: A query is replicated in a statement before executing on the master.  The node waits for all preceding transactions to commit and then all nodes simultaneously execute the transaction in isolation.

- :term:`Rolling Schema Upgrade`: Schema upgrades run locally, blocking only the node on which they are run.  The changes do not replicate to the rest of the cluster.

.. note:: **See Also**: For more information, see :doc:`schemaupgrades`.
  
	     


.. rubric:: What if Connections return an ``Unknown Command`` Error?
.. _`connection-unknown-command`:

This may happen when a cluster experiences a temporary split, during which a portion of the nodes loses connectivity to the :term:`Primary Component`.  When they reconnect, nodes from the former non-operational component drop their client connections.  New connections to the database client will return ``Unknown command`` errors.

Basically, the node does not yet consider itself a part of the Primary Component.  While it has restored network connectivity, it still has to resynchronize itself with the cluster.  MySQL doesn't have an error code for the node lacking Primary status. So it defaults to an ``Unknown command`` message.

Nodes in a non-operational component must regain network connectivity with the Primary Component, process a state transfer, and catch up with the cluster before they can resume normal operation.



.. rubric:: Is GCache a Binlog?

The :term:`Write-set Cache`, which is also called GCache, is a memory allocator for write-sets.  Its primary purpose is to minimize the write-set footprint in RAM.  It is not a log of events, but rather a cache.

- GCache is not persistent.
- Not every entry in GCache is a write-set.
- Not every write-set in GCache will be committed.
- Write-sets in GCache are not allocated in commit order.
- Write-sets are not an optimal entry for the binlog, since they contain extra information.

Nevertheless, it is possible to construct a binlog out of the write-set cache.
	    


.. rubric:: What if a Node Crashes during ``rsync`` SST

You can configure :ref:`wsrep_sst_method <wsrep_sst_method>` to use ``rsync`` for :term:`State Snapshot Transfer`.  If the node crashes before the state transfer is complete, it may cause the ``rsync`` process to hang forever, occupying the port and not allowing you to restart the node.  If this occurs, the error logs for the database server will show that the port is in use.

To correct the problem, kill the orphaned ``rsync`` process.  For example, if the process had a pid of ``501``, you might enter the following from the command-line:

.. code-block:: console

   # kill 501

Once you kill the orphaned process, it will free the relevant ports and allow you to restart the node.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
