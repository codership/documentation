==========================
 Schema Upgrades
==========================
.. _`schema-upgrades`:

Schema changes are of particular interest related to Galara Cluster. Schema changes are  :abbr:`DDL (Data Definition Language)` statement executed on a database (e.g., ``CREATE TABLE``, ``GRANT``).  These :abbr:`DDL (Data Definition Language)` statements change the database itself and are non-transactional.

Galera Cluster processes schema changes by two different methods:

- :ref:`Total Order Isolation <toi>`: Abbreviated as TOI, these are schema changes made on all cluster nodes in the same total order sequence, preventing other transations from committing for the duration of the operation.

- :ref:`Rolling Schema Upgrade <rsu>` Known also as RSU, these are schema changes run locally, affecting only the node on which they are run.  The changes do not replicate to the rest of the cluster.

You can set the method for online schema changes by using the ``wsrep_OSU_method`` parameter in the configuration file, (``my.ini`` or ``my.cnf`, depending on your build) or through the ``mysql`` client.  Galera Cluster defaults to the Total Order Isolation method.

.. note:: **See Also**: If you're using Galera Cluster for Percona XtraDB Cluster, see the the `pt-online-schema-change <http://www.percona.com/doc/percona-toolkit/2.2/pt-online-schema-change.html>`_ in the Percona Toolkit.




---------------------------------
 Total Order Isolation
---------------------------------
.. _`toi`:
.. index::
   pair: Descriptions; Total Order Isolation

When you want an online schema change to replicate through the cluster and don't care that other transactions will be blocked while the cluster processes the :abbr:`DDL (Data Definition Language)` statements, use the :term:`Total Order Isolation` method. You would do this with the ``SET`` statement like so:

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='TOI';

In Total Order Isolation, queries that change the schema replicate as statements to all nodes in the cluster.  The nodes wait for all preceding transactions to commit simultaneously, then they execute the schema change in isolation.  For the duration of the :abbr:`DDL (Data Definition Language)` processing, no other transactions can commit.

The main advantage of Total Order Isolation is its simplicity and predictability, which guarantees data consistency. Additionally, when using Total Order Isolation, you should take the following particularities into consideration:

- From the perspective of certification, schema upgrades in Total Order Isolation never conflict with preceding transactions, given that they only execute after the cluster commits all preceding transactions.  What this means is that the certification interval for schema changes using this method has a zero length. Therefore, schema changes will never fail certification and their execution is guaranteed.

- Transactions that were in progress while the DDL was running and that involved the same database resource will get a deadlock error at commit time and will be rolled back.

- The cluster replicates the schema change query as a statement before its execution.  There is no way to know whether or not individual nodes succeed in processing the query.  This prevents error checking on schema changes in Total Order Isolation.

---------------------------------
 Rolling Schema Upgrade
---------------------------------
.. _`rsu`:
.. index::
   pair: Descriptions; Rolling Schema Upgrade
.. index::
   pair: Parameters; wsrep_OSU_method

When you want to maintain high-availability during schema upgrades and can avoid conflicts between new and old schema definitions, use the :term:`Rolling Schema Upgrade` method.  You would do this with the ``SET`` statement like so:

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='RSU';

In Rolling Schema Upgrade, queries that change the schema are only processed on the local node.  While the node processes the schema change, it desynchronizes with the cluster.  When it finishes processing the schema change, it applies delayed replication events and synchronizes itself with the cluster.

To change a schema cluster-wide, you must manually execute the query on each node in turn.  Bear in mind that during a rolling schema change the cluster continues to operate, with some nodes using the old schema structure while others use the new schema structure.

The main advantage of the Rolling Schema Upgrade is that it only blocks one node at a time. The main disadvantage of the Rolling Schema Upgrade is that it is potentially unsafe, and may fail if the new and old schema definitions are incompatible at the replication event level.

.. warning:: To avoid conflicts between new and old schema definitions, execute SQL statements such as ``CREATE TABLE`` and ``DROP TABLE`` using the :ref:`Total Order Isolation <toi>` method.
