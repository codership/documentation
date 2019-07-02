.. cssclass:: library-document
.. _`glossary`:

==========
 Glossary
==========

.. glossary::
   :sorted:


   Galera Arbitrator
      An external process that functions as an additional node in certain cluster operations, such as quorum calculations and generating consistent application state snapshots.

      For example, consider a situation where your cluster becomes partitioned due to a loss of network connectivity that results in two components of equal size.  Each component initiates quorum calculations to determine which should remain the :term:`Primary Component` and which should become a non-operational component.  If the components are of equal size, it risks a split-brain condition.  Galera Arbitrator provides an addition vote in the quorum calculation, so that one component registers as larger than the other.  The larger component then remains the Primary Component.

      Unlike the main ``mysqld`` process, ``garbd`` doesn't generate replication events of its own and doesn't store replication data. It does, however, acknowledge all replication events.  Furthermore, you can route replication through Galera Arbitrator, such as when generating a consistent application state snapshot for backups.

      For more information, see :doc:`arbitrator` and :doc:`backup-cluster`.


   Galera Replication Plugin
      Galera Replication Plugin is a general purpose replication plugin for any transactional system. It can be used to create a synchronous multi-master replication solution to achieve high availability and scale-out.

      See :ref:`Galera Replication Plugin <galera-replication-plugin>` for more details.

   Global Transaction ID
      To keep the state identical on all nodes, the :term:`wsrep API` uses global transaction IDs (GTID), which are used to identify the state change and to identify the state itself by the ID of the last state change

      The GTID consists of a state UUID, which uniquely identifies the state and the sequence of changes it undergoes, and an ordinal sequence number (seqno, a 64-bit signed integer) to denote the position of the change in the sequence.

      For more information on Global Transaction ID's, see :ref:`wsrep API <wsrep-api>`.


   Incremental State Transfer
      In an Incremental State Transfer (IST) a node only receives the missing write-sets and catches up with the group by replaying them. See also the definition for State Snapshot Transfer (SST).

      For more information on IST's, see :ref:`Incremental State Transfer (IST) <state-transfer-ist>`.

   IST
      See :term:`Incremental State Transfer`.

   Logical State Transfer Method
      This is a type of back-end state transfer method that operates through the database server (e.g., ``mysqldump``).

      For more information, see :ref:`Logical State Snapshot <sst-logical>`.


   Physical State Transfer Method
      This is another type of back-end state transfer method, but it operates on the physical media in the datadir (e.g., ``rsync`` and ``xtrabackup``).

      For more information, see :ref:`Physical State Snapshot <sst-physical>`.

   Primary Component
      In addition to single-node failures, the cluster may be split into several components due to network failure. In such a situation, only one of the components can continue to modify the database state to avoid history divergence. This component is called the Primary Component (PC).

      For more information on the Primary Component, see :doc:`weighted-quorum`.

   Rolling Schema Upgrade
      The rolling schema upgrade is a :abbr:`DDL (Data Definition Language)` processing method in which the :abbr:`DDL (Data Definition Language)` will only be processed locally on the node. The node is desynchronized from the cluster for the duration of the :abbr:`DDL (Data Definition Language)` processing in a way that it doesn't block the other nodes.  When the :abbr:`DDL (Data Definition Language)` processing is complete, the node applies the delayed replication events and synchronizes with the cluster.

      For more information, see :ref:`Rolling Schema Upgrade <rsu>`.

   RSU
      See :term:`Rolling Schema Upgrade`.

   seqno
      See :term:`Sequence Number`.

   Sequence Number
      This is a 64-bit signed integer that the node uses to denote the position of a given transaction in the sequence.  The seqno is second component to the :term:`Global Transaction ID`.

   State Snapshot Transfer
      State Snapshot Transfer refers to a full data copy from one cluster node (i.e., a donor) to the joining node (i.e., a joiner). See also the definition for Incremental State Transfer (IST).

      For more information, see :ref:`State Snapshot Transfer (SST) <sst>`.

   State UUID
      Unique identifier for the state of a node and the sequence of changes it undergoes.  It's the first component of the :term:`Global Transaction ID`.

   SST
      See :term:`State Snapshot Transfer`.


   Streaming Replication
      This provides an alternative replication method for handling large or long-running write transactions.  It's a new feature in version 4.0 of Galera Cluster.  In older versions, the feature is unsupported.

      Under normal operation, the node performs all replication and certification operations when the transaction commits. With large transactions this can result in conflicts if smaller transactions are committed first.  With Streaming Replication, the node breaks the transaction into fragments, then certifies and replicates them to all nodes while the transaction is still in progress.  Once certified, a fragment can no longer be aborted by a conflicting transaction.

      For more information see :doc:`streaming-replication` and :doc:`using-sr`.


   Total Order Isolation
      By default, :abbr:`DDL (Data Definition Language)` statements are processed by using the Total Order Isolation (TOI) method. In TOI, the query is replicated to the nodes in a statement form before executing on the master. The query waits for all preceding transactions to commit and then gets executed in isolation on all nodes, simultaneously.

      For more information, see :ref:`Total Order Isolation <toi>`.

   TOI
      See :term:`Total Order Isolation`.

   write-set
      Transaction commits the node sends to and receives from the cluster.

   Write-set Cache
      Galera stores write-sets in a special cache called, Write-set Cache (GCache). GCache is a memory allocator for write-sets. Its primary purpose is to minimize the write set footprint on the RAM.

      For more information, see :ref:`Write-Set Cache (GCache) <state-transfer-gcache>`.

   GCache
      See :term:`Write-set Cache`.

   wsrep API
      The wsrep API is a generic replication plugin interface for databases.  The API defines a set of application callbacks and replication plugin calls.

      For more information, see :ref:`wsrep API <wsrep-api>`.
