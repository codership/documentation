==========
 Glossary
==========
.. _`Glossary`:

.. glossary::
   :sorted:


   Galera Arbitrator
      External process that functions as an additional node in certain cluster operations, such as quorum calculations and generating consistent application state snapshots.

      Consider a situation where you cluster becomes partitioned due to a loss of network connectivity that results in two components of equal size.  Each component initiates quorum calculations to determine which should remain the :term:`Primary Component` and which should become a nonoperational component.  If the components are of equal size, it risks a split-brain condition.  Galera Arbitrator provides an addition vote in the quorum calculation, so that one component registers as larger than the other.  The larger component then remains the Primary Component.

      Unlike the main ``mysqld`` process, ``garbd`` does not generate replication events of its own and does not store replication data, but it does acknowledge all replication events.  Furthermore, you can route replication through Galera Arbitrator, such as when generating a consistent application state snapshot for backups.

      .. note:: **See Also**: For more information, see :doc:`arbitrator` and :doc:`backingupthecluster`.


   Galera Replication Plugin
      Galera Replication Plugin is a general purpose replication plugin for any transactional system. It can be used to create a synchronous multi-master replication solution to achieve high availability and scale-out.

      .. note:: **See Also**: For more information, see :ref:`Galera Replication Plugin <galera-replication-plugin>` for more details.

   Global Transaction ID
      To keep the state identical on all nodes, the :term:`wsrep API` uses global transaction IDs (GTID), which are used to both:

        - Identify the state change
        - Identify the state itself by the ID of the last state change

      The GTID consists of:

        - A state UUID, which uniquely identifies the state and the sequence of changes it undergoes
        - An ordinal sequence number (seqno, a 64-bit signed integer) to denote the position of the change in the sequence

      .. note:: **See Also**: For more information on Global Transaction ID's, see :ref:`wsrep API <wsrep-api>`.


   Incremental State Transfer
      In an Incremental State Transfer (IST) a node only receives the missing write-sets and catch up with the group by replaying them. See also the definition for State Snapshot Transfer (SST).

      .. note:: **See Also**: For more information on IST's, see :ref:`Incremental State Transfer (IST) <ist>`.

   IST
      See :term:`Incremental State Transfer`.

   Logical State Transfer Method
      Type of back-end state transfer method that operates through the database server.  For example: ``mysqldump``.

      .. note:: **See Also**: For more information see, :ref:`Logical State Snapshot <sst-logical>`.

   Physical State Transfer Method
      Type of back-end state transfer method that operates on the physical media in the datadir.  For example: ``rsync`` and ``xtrabackup``.

      .. note:: **See Also**: For more information see, :ref:`Physical State Snapshot <sst-physical>`.

   Primary Component
      In addition to single node failures, the cluster may be split into several components due to network failure. In such a situation, only one of the components can continue to modify the database state to avoid history divergence. This component is called the Primary Component (PC).

      .. note:: **See Also**: For more information on the Primary Component, see :doc:`weightedquorum` for more details.

   Rolling Schema Upgrade
      The rolling schema upgrade is a :abbr:`DDL (Data Definition Language)` processing method, where the :abbr:`DDL (Data Definition Language)` will only be processed locally at the node. The node is desynchronized from the cluster for the duration of the :abbr:`DDL (Data Definition Language)` processing in a way that it does not block the rest of the nodes.  When the :abbr:`DDL (Data Definition Language)` processing is complete, the node applies the delayed replication events and synchronizes back with the cluster.

      .. note:: **See Also**: For more information, see :ref:`Rolling Schema Upgrade <rsu>`.

   RSU
      See :term:`Rolling Schema Upgrade`.

   seqno
      See :term:`Sequence Number`.

   sequence number
      64-bit signed integer that the node uses to denote the position of a given transaction in the sequence.  The seqno is second component to the :term:`Global Transaction ID`.

   State Snapshot Transfer
      State Snapshot Transfer refers to a full data copy from one cluster node (donor) to the joining node (joiner). See also the definition for Incremental State Transfer (IST).

      .. note:: **See Also**: For more information, see :ref:`State Snapshot Transfer (SST) <sst>`.

   State UUID
      Unique identifier for the state of a node and the sequence of changes it undergoes.  It is the first component of the :term:`Global Transaction ID`.

   SST
      See :term:`State Snapshot Transfer`.


   Total Order Isolation
      By default, :abbr:`DDL (Data Definition Language)` statements are processed by using the Total Order Isolation (TOI) method. In TOI, the query is replicated to the nodes in a statement form before executing on master. The query waits for all preceding transactions to commit and then gets executed in isolation on all nodes simultaneously.

      .. note:: **See Also**: For more information, see :ref:`Total Order Isolation <toi>`.

   TOI
      See :term:`Total Order Isolation`.

   write-set
      Transaction commits the node sends to and receives from the cluster.

   Write-set Cache
      Galera stores write-sets in a special cache called Write-set Cache (GCache).  In short, GCache is a memory allocator for write-sets and its primary purpose is to minimize the write set footprint on the RAM.

      .. note:: **See Also**: For more information, see :ref:`Write-set Cache (GCache) <gcache>`.

   GCache
      See :term:`Write-set Cache`.

   wsrep API
      The wsrep API is a generic replication plugin interface for databases.  The API defines a set of application callbacks and replication plugin calls.

      .. note:: **See Also**: For more information, see :ref:`wsrep API <wsrep-api>`.



