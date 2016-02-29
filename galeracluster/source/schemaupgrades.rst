==========================
 Schema Upgrades
==========================
.. _`Schema Upgrades`:

Any :abbr:`DDL (Data Definition Language)` statement that runs for the database, such as ``CREATE TABLE`` or ``GRANT``, upgrades the schema.  These :abbr:`DDL (Data Definition Language)` statements change the database itself and are non-transactional.

Galera Cluster processes schema upgrades in two different methods:

- :ref:`Total Order Isolation <toi>` (TOI) Where the schema upgrades run on all cluster nodes in the same total order sequence, locking affected tables for the duration of the operation.

- :ref:`Rolling Schema Upgrade <rsu>` (RSU) Where the schema upgrades run locally, blocking only the node on which they are run.  The changes do *not* replicate to the rest of the cluster.

- :ref:`Non-Blocking Operation <nbo>` (NBO)

You can set the method for online schema upgrades by using the ``wsrep_OSU_method`` parameter in the configuration file, (**my.ini** or **my.cnf**, depending on your build) or through the MySQL client.  Galera Cluster defaults to the Total Order Isolation method.

.. note:: **See Also**: If you are using Galera Cluster for Percona XtraDB Cluster, see the the `pt-online-schema-change <http://www.percona.com/doc/percona-toolkit/2.2/pt-online-schema-change.html>`_ in the Percona Toolkit.




---------------------------------
 Total Order Isolation
---------------------------------
.. _`toi`:
.. index::
   pair: Descriptions; Total Order Isolation

When you want your online schema upgrades to replicate through the cluster and don't mind the loss of high availability while the cluster processes the :abbr:`DDL (Data Definition Language)` statements, use the :term:`Total Order Isolation` method.

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='TOI';

In Total Order Isolation, queries that update the schema replicate as statements to all nodes in the cluster before they execute on the master.  The nodes wait for all preceding transactions to commit then, simultaneously, they execute the schema upgrade in isolation.  For the duration of the :abbr:`DDL (Data Definition Language)` processing, part of the database remains locked, causing the cluster to function as single server.

The cluster can maintain isolation at the following levels:

- **Server Level** For ``CREATE SCHEMA``, ``GRANT`` and similar queries, where the cluster cannot apply concurrently any other transactions.

- **Schema Level** For ``CREATE TABLE`` and similar queries, where the cluster cannot apply concurrently any transactions that access the schema.

- **Table Level** For ``ALTER TABLE`` and similar queries, where the cluster cannot apply concurrently any other transactions that access the table.

The main advantage of Total Order Isolation is its simplicity and predictability, which guarantees data consistency.

In addition, when using Total Order Isolation you should take the following particularities into consideration:

- From the perspective of certification, schema upgrades in Total Order Isolation never conflict with preceding transactions, given that they only execute after the cluster commits all preceding transactions.  What this means is that the certification interval for schema upgrades in this method is of zero length.  The schema upgrades never fail certification and their execution is a guarantee.

- The certification process takes place at a resource level.  Under server-level isolation transactions that come in during the certification interval that include schema upgrades in Total Order Isolation, will fail certification.

- The cluster replicates the schema upgrade query as a statement before its execution.  There is no way to know whether or not the nodes succeed in processing the query.  This prevents error checking on schema upgrades in Total Order Isolation.

The main disadvantage of Total Order Isolation is that while the nodes process the :abbr:`DDL (Data Definition Language)` statements, the cluster functions as a single server, which can potentially prevent high-availability for the duration of the process.


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

Brief intro of the value of NBO.

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='NBO';

When DDL statements replicate under the :term:`Total Order Isolation` method, the nodes block almost all updates made to them.  With some statements this can go on for a particularly long time.  In the Non-Blocking Operation method, the node applies special table locks called metadata locks on all nodes, in order to ensure consistency.  The nodes all execute the DDL statements, using a separate applier thread.  Then, once the statement is applied, all nodes simultaneously release the locks.

DDL statements that support Non-Blocking Operation:

- ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE}, alter_specification``
- ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE} PARTITION``
- ``ANALYZE TABLE``
- ``OPTIMIZE TABLE`` 

.. note:: For partition management, the comma that occurs after ``LOCK = {SHARED|EXCLUSIVE}`` does not get used.


DDL statements that do not support Non-Blocking Operation:

- ``ALTER TABLE LOCK = {DEFAULT|NONE}``, including ``ALTER`` statements without the ``LOCK`` clause, as these locks default to the ``DEFAULT`` lock.
- ``CREATE``, ``RENAME``, ``DROP``, and ``REPAIR``.

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

  When you set the lock to ``EXCLUSIVE``, the node also blocks reads.  When you set the lock to ``SHARED``, the node allows read operations on the table.

- The table locks acquired at the beginning of the operation remains a blocking operation.  Long transactions running against the table already may lead the cluster to block the locks.  To avoid this, ensure that no clients have open transactions that include the table prior to running the ``ALTER`` statement.

- During DDL operations, nodes cannot serve as donors for a :term:`State Snapshot Transfer`.  

  What this means is that nodes are unable to join the cluster while DDL statements are in progress under this method.  Nodes that attempt to rejoin the cluster, must have sufficient data in their write-set caches to perform a :term:`Incremental State Transfer`.  Those that do not are unable to rejoin.  

  .. note:: If you expect a DDL statement to take an hour to run, adjust the :ref:`gcache.size <gcache.size>` wsrep option according so that the nodes cache enough data to continue performing incremental state transfers during the process.

- Under this method, nodes that leave the cluster during DDL operations have inconsistent data with the cluster, meaning that they can only rejoin the cluster through a State Snapshot Transfer, rather than the much faster Incremental State Transfer.

- Do not use DDL statements with this method that operate on more than one table at a time.

- Do not execute other DDL statements, such as part of the :term:`Rolling Schema Upgrade` method while upgrades using the Non-Blocking Operation method are in progress.


