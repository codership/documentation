==========================
 Schema Upgrades
==========================
.. _`Schema Upgrades`:

Any :abbr:`DDL (Data Definition Language)` statement that runs for the database, such as ``CREATE TABLE`` or ``GRANT``, upgrades the schema.  These :abbr:`DDL (Data Definition Language)` statements change the database itself and are non-transactional.

Galera Cluster processes schema upgrades in two different methods:

- :ref:`Total Order Isolation <toi>` (TOI) Where the schema upgrades run on all cluster nodes in the same total order sequence, preventing other transations from committing for the duration of the operation.

- :ref:`Rolling Schema Upgrade <rsu>` (RSU) Where the schema upgrades run locally, affecting only the node on which they are run.  The changes do *not* replicate to the rest of the cluster.

- :ref:`Non-Blocking Operation <nbo>` (NBO)

You can set the method for online schema upgrades by using the ``wsrep_OSU_method`` parameter in the configuration file, (**my.ini** or **my.cnf**, depending on your build) or through the MySQL client.  Galera Cluster defaults to the Total Order Isolation method.

.. note:: **See Also**: If you are using Galera Cluster for Percona XtraDB Cluster, see the the `pt-online-schema-change <http://www.percona.com/doc/percona-toolkit/2.2/pt-online-schema-change.html>`_ in the Percona Toolkit.




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


----------------------------
Non-Blocking Operation
----------------------------
.. _`nbo`:
.. index::
   pair: Galera Cluster 4.x; Non-Blocking Operation
.. index::
   pair: Online Schema Upgrades; Non-Blocking Operation

When you want to maintain high-availability while altering, analyzing or optimizing tables and don't mind the particular limitations, use the :term:`Non-Blocking Operation` method.

Under the :term:`Total Order Isolation` method, when DDL statements replicate, the nodes block almost all updates and with some statements this can go on for a particularly long time.  In the Non-Blocking Operation method, the node applies special table locks called metadata locks on all nodes, in order to ensure consistency.  The nodes all execute the DDL statements, using a separate applier thread.  Then, once the statement is applied, all nodes simultaneously release the locks.

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='NBO';

Given its :ref:`limitations <nbo-limitations>`, the recommended method in updating the schema with a Non-Blocking Operation is to enable it at a session level, run the command, and then reset the Online Schema Upgrade method back to ``TOI`` or ``RSU``.
   
DDL statements that support Non-Blocking Operation:

- ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE}, alter_specification``
- ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE} PARTITION``
- ``CREATE INDEX ... LOCK = {SHARED|EXCLUSIVE}``
- ``DROP INDEX``
- ``ANALYZE TABLE``
- ``OPTIMIZE TABLE`` 

.. note:: For partition-management operations, no comma is used after ``LOCK = {SHARED|EXCLUSIVE}``.

DDL statements that do not support Non-Blocking Operation:

- ``ALTER TABLE LOCK = {DEFAULT|NONE}``, including ``ALTER`` statements without the ``LOCK`` clause, as such statements default to the ``DEFAULT`` lock.
- ``CREATE TABLE``, ``RENAME``, ``DROP``, and ``REPAIR``.

Issuing unsupported operations while using the Non-Blocking Operation method results in an error code.  For example,

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='NBO';
   CREATE TABLE table_name (
        id INT,
	title VARCHAR(255)) ENGINE=InnoDB;

   Error 42000: wsrep_OSU_method NBO not supported for query


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`nbo-limitations`:

In addition to unsupported DDL statements, there are a number of limitations in using the :term:`Non-Blocking Operation` method to consider:

- Given that DDL statements such as ``CREATE`` or using ``ALTER`` without the ``LOCK`` clause results in an error under the Non-Blocking Operation method, it is not recommended that you set :ref:`wsrep_OSU_method <wsrep_OSU_method>` to ``NBO`` server-wide.

  Instead, only use the Non-Blocking Operation method for specific sessions that run supported DDL statements.

- While the node processes a DDL statement under the Non-Blocking Operation method, it is not possible to write to the table being altered.  The node blocks write attempts until it finishes applying the ``ALTER``.

  When you set the lock to ``EXCLUSIVE``, the node also blocks reads to the table.  When you set the lock to ``SHARED``, the node allows read operations on the table.

- The acquisition of the table metadata lock at the beginning of the operation remains a blocking operation.  Long transactions already running against the table may lead the cluster to block while the lock is granted.  To avoid this, ensure that no clients have open transactions that include the table prior to running the ``ALTER`` statement.

- During NBO DDL operations, nodes cannot serve as donors for a :term:`State Snapshot Transfer`.  

  What this means is that nodes are unable to join the cluster while DDL statements are in progress under this method.  Nodes that attempt to rejoin the cluster, must have sufficient data in their write-set caches to perform a :term:`Incremental State Transfer`.  Those that do not are unable to rejoin.  

  .. note:: If you expect a DDL statement to take an hour to run, adjust the :ref:`gcache.size <gcache.size>` wsrep option accordingly so that the nodes cache enough data to perform incremental state transfers, in the event that they need to during the process.

- Under this method, nodes that leave the cluster during DDL operations will have an inconsistent snapshot of the data, meaning that they can only rejoin the cluster through a State Snapshot Transfer, rather than the much faster Incremental State Transfer.

- Do not use DDL statements with this method that operate on more than one table at a time.

- Do not execute other DDL statements, such as ones using the :term:`Rolling Schema Upgrade` method while upgrades using the Non-Blocking Operation method are in progress.


