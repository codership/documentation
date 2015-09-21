====================== 
 Isolation Levels
======================
.. _`isolation-levels`:

Galera Cluster handles transactions in "isolation". This isolation guarantees that the cluster processes transactions in a reliable manner.

Before going into details about possible isolation levels which can be set for a client session in Galera Cluster it is important to make a distinction between single node and global cluster transaction isolation. Individual cluster nodes can provide any isolation level *to the extent* it is supported by MySQL/InnoDB. However isolation level *between* the nodes in the cluster is determined by certification protocol and is always ``SNAPSHOT`` isolation level, which is *not supported* by MySQL/InnoDB. That means that transactions issued on different nodes may not be isolated *identically* to transactions issued on the same node.

The highest MySQL-supported isolation level that may be provided cluster-wide is ``REPEATABLE READ``, which is also the default isolation level in MySQL/InnoDB. However for transactions issued on different nodes it is also strengthened by the "first committer wins" rule, whereas for transactions issued on the same node this rule does not hold (as per original MySQL/InnoDB behavior). This makes for different outcomes depending on transaction origin, but in either case it is no weaker than the ``REPEATABLE READ`` on a standalone MySQL/InnoDB.

Data consistency between the nodes is always guaranteed regardless of the isolation level chosen by client.

-------------------------------
Understanding Isolation Levels
-------------------------------

Isolation ensures that concurrently running transactions do not interfere with each other.  Because of this, it also ensures data consistency.  If the transactions were not isolated, one transaction could modify data that other transactions are reading, which would lead to data inconsistency.

Galera Cluster employs four isolation levels, which are in ascending order:

- :ref:`READ-UNCOMMITTED <read-uncommitted>`
- :ref:`READ-COMMITTED <read-committed>`
- :ref:`REPEATABLE-READ <repeatable-read>`
- :ref:`SERIALIZABLE <serializable>`

^^^^^^^^^^^^^^^^^^^^^^^^
READ-UNCOMMITTED
^^^^^^^^^^^^^^^^^^^^^^^^
.. _`read-uncommitted`:

Here transactions can see changes to data made by other transactions that are not yet committed.  

In other words, transactions can read data that eventually may not exist, given that other transactions can always rollback the changes without commit.  This is known as a dirty read.  Effectively, ``READ-UNCOMMITTED`` has no real isolation at all.

^^^^^^^^^^^^^^^^^^^^^^^^
READ-COMMITTED
^^^^^^^^^^^^^^^^^^^^^^^^
.. _`read-committed`:

Here dirty reads are not possible.  Uncommitted changes remain invisible to other transactions until the transaction commits.  

However, at this isolation level ``SELECT`` queries use their own snapshots of committed data, that is data committed before the ``SELECT`` query executed.  As a result, ``SELECT`` queries, when run multiple times within the same transaction, can return different result sets.  This is called a non-repeatable read.



^^^^^^^^^^^^^^^^^^^^^^^^
REPEATABLE-READ
^^^^^^^^^^^^^^^^^^^^^^^^
.. _`repeatable-read`:

Here non-repeatable reads are not possible.  Snapshots taken for the ``SELECT`` query are taken the first time the ``SELECT`` query runs during the transaction.  

The snapshot remains in use throughout the entire transaction for the ``SELECT`` query.  It always returns the same result set.  This level does not take into account changes to data made by other transactions, regardless of whether or not they have been committed.  IN this way, reads remain repeatable.


^^^^^^^^^^^^^^^^^^^^^^^^
SERIALIZABLE
^^^^^^^^^^^^^^^^^^^^^^^^
.. _`serializable`:

Here all records accessed within a transaction are locked.  The resource locks in a way that also prevents you from appending records to the table the transaction operates upon.

``SERIALIZABLE`` prevents a phenomenon known as a phantom read.  Phantom reads occur when, within a transaction, two identical queries execute, and the rows the second query returns differ from the first.


------------------------------------
Where Isolation Levels Occur
------------------------------------

Galera Cluster uses transaction isolation at both the local and the cluster level.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Local Transaction Isolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`local-isolation`:

Transaction isolation occurs on each node at the local level of the database server.  It functions the same as with the native InnoDB storage engine.  All four levels are available.

The default setting for local transaction isolation is ``REPEATABLE-READ``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cluster Transaction Isolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`cluster-isolation`:

Transaction isolation also occurs at the cluster level.  Between transactions processing on separate nodes, Galera Cluster implements a transaction level called ``SNAPSHOT-ISOLATION``.  The ``SNAPSHOT-ISOLATION`` level occurs between ``REPEATABLE-READ`` and ``SERIALIZABLE``.

The reason for this is that there is no support in the ``SERIALIZABLE`` transaction isolation level for the multi-master use case, neither in the ``STATEMENT`` nor the ``ROW`` formats.  This is due to the fact that the Galera Replication Plugin does not carry a transaction read-set.  Also, because the ``SERIALIZABLE`` transaction isolation level is vulnerable to multi-master conflicts.  It holds read locks and any replicated writes to a read locked row cause the transaction to abort.  

It is recommended that you avoid using ``SERIALIZABLE`` in Galera Cluster.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
