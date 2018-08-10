==========================
 Schema Upgrades
==========================
.. _`Schema Upgrades`:

Any :abbr:`DDL (Data Definition Language)` statement that runs for the database, such as ``CREATE TABLE`` or ``GRANT``, upgrades the schema.  These :abbr:`DDL (Data Definition Language)` statements change the database itself and are non-transactional.

Galera Cluster processes schema upgrades in two different methods:

- :ref:`Total Order Isolation <toi>` (TOI) Where the schema upgrades run on all cluster nodes in the same total order sequence, preventing other transations from committing for the duration of the operation.

- :ref:`Rolling Schema Upgrade <rsu>` (RSU) Where the schema upgrades run locally, affecting only the node on which they are run.  The changes do *not* replicate to the rest of the cluster.

You can set the method for online schema upgrades by using the ``wsrep_OSU_method`` parameter in the configuration file, (**my.ini** or **my.cnf**, depending on your build) or through the MySQL client.  Galera Cluster defaults to the Total Order Isolation method.

.. note:: **See Also**: See also the `pt-online-schema-change <http://www.percona.com/doc/percona-toolkit/2.2/pt-online-schema-change.html>`_ in the Percona Toolkit for an alternative approach to schema changes.

---------------------------------
 Total Order Isolation
---------------------------------
.. _`toi`:
.. index::
   pair: Descriptions; Total Order Isolation

When you want your online schema upgrades to replicate through the cluster and don't mind that other transactions will be blocked while the cluster processes the :abbr:`DDL (Data Definition Language)` statements, use the :term:`Total Order Isolation` method.

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='TOI';

In Total Order Isolation, queries that update the schema replicate as statements to all nodes in the cluster.  The nodes wait for all preceding transactions to commit then, simultaneously, they execute the schema upgrade in isolation.  For the duration of the :abbr:`DDL (Data Definition Language)` processing, no other transactions can commit.

The main advantage of Total Order Isolation is its simplicity and predictability, which guarantees data consistency.

In addition, when using Total Order Isolation, you should take the following particularities into consideration:

- From the perspective of certification, schema upgrades in Total Order Isolation never conflict with preceding transactions, given that they only execute after the cluster commits all preceding transactions.  What this means is that the certification interval for schema upgrades using this method has a zero length. Therefore, schema upgrades will never fail certification and their execution is guaranteed.

- Transactions that were in progress while the DDL was running and that involved the same database resource will get a deadlock error at commit time and will be rolled back.

- The cluster replicates the schema upgrade query as a statement before its execution.  There is no way to know whether or not individual nodes succeed in processing the query.  This prevents error checking on schema upgrades in Total Order Isolation.

---------------------------------
 Rolling Schema Upgrade
---------------------------------
.. _`rsu`:
.. index::
   pair: Descriptions; Rolling Schema Upgrade
.. index::
   pair: Parameters; wsrep_OSU_method

When you want to maintain high-availability during schema upgrades and can avoid conflicts between new and old schema definitions, use the :term:`Rolling Schema Upgrade` method.

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='RSU';

In Rolling Schema Upgrade, queries that update the schema are only processed on the local node.  While the node processes the schema upgrade, it desynchronizes with the cluster.  When it finishes processing the schema upgrade it applies delayed replication events and synchronizes itself with the cluster.

To upgrade the schema cluster-wide, you must manually execute the query on each node in turn.  Bear in mind that during a rolling schema upgrade the cluster continues to operate, with some nodes using the old schema structure while others use the new schema structure.

The main advantage of the Rolling Schema Upgrade is that it only blocks one node at a time.

The main disadvantage of the Rolling Schema Upgrade is that it is potentially unsafe, and may fail if the new and old schema definitions are incompatible at the replication event level.

.. note:: **Warning**: To avoid conflicts between new and old schema definitions, execute operations such as ``CREATE TABLE`` and ``DROP TABLE`` using the :ref:`Total Order Isolation <toi>` method.


