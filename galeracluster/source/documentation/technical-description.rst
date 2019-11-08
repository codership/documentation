.. meta::
   :title: Technical Description of Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, overview, introduction, replication
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`Certification Replication <certification-based-replication>`
      - :doc:`tech-desc-introduction`
      - :doc:`node-states`
      - :doc:`isolation-levels`
      - :doc:`Node Recovery <recovery>`
      - :doc:`weighted-quorum`
      - :doc:`Replication Architecture <architecture>`
      - :doc:`state-transfer`
      - :doc:`streaming-replication`

      Related Articles


.. cssclass:: library-document
.. _`tech-description`:

======================
Technical Description
======================

Galera Cluster is a synchronous certification-based replication solution for MySQL, MariaDB and Percona XtraDB.  Cluster nodes are identical and fully representative of the cluster state. They allow for unconstrained transparent client access, acting as a single-distributed database server.  In order to better understand Galera Cluster, this section provides detailed information on how it works and how you can benefit from it.


.. _`understanding-repl`:
.. rst-class:: section-heading
.. rubric:: Understanding Replication

Replication in the context of databases refers to the frequent copying of data from one database server to another.  These sections provide a high-level explanation of replication both in the general sense of how it works, as well as the particulars of how Galera Cluster implements these core concepts.

- :doc:`tech-desc-introduction`

  This section explains how database replication works in general.  It provides an overview of the problems inherent in the various replication implementations, including master-slave, asynchronous and synchronous replication.

- :doc:`certification-based-replication`

  Using group communications and transaction ordering techniques, certification-based replication allows for synchronous replication.


.. _`understanding-galera`:
.. rst-class:: section-heading
.. rubric:: Understanding Galera Cluster

With a better grasp on how replication works, these pages provide a more detailed explanation of how Galera Cluster implements certification-based replication, including the specific architecture of the nodes, how they communicate with each other, as well as replicate data and manage the replication process.


- :doc:`architecture`

  While the above sections explain the abstract concepts surrounding certification-based replication, this section covers the specific architecture used by Galera Cluster in implementing write-set replication, including the wsrep API and the Galera Replication and Group Communication plug-ins.


- :doc:`isolation-levels`

  In a database system, the server will process concurrent transactions in isolation from each other. The level of isolation determines whether and how these transactions affect one another.  This section provides an overview of the isolation levels supported by Galera Cluster.

- :doc:`state-transfer`

  The actual process that nodes use to replicate data into each other is called provisioning.  Galera Cluster supports two provisioning methods: State Snapshot Transfers and Incremental State Transfers.  This section presents an overview of each.

- :doc:`node-states`

  Galera Cluster manages the replication process using a feedback mechanism called Flow Control.  This allows the node to pause and resume replication according to its performance needs and to prevent any node from lagging too far behind the others in applying transaction.  This section provides an overview of Flow Control and the different states nodes can hold.

- :doc:`recovery`

  Nodes fail to operate when they lose their connection with the cluster.  This can occur for various reasons, such as hardware failures, software crashes, or the loss of network connectivity.  This section provides an overview of how nodes and the cluster cope with failure and how they may recover.

- :doc:`weighted-quorum`

  When nodes connect to each other, they form components.  The Primary Component is a component that has quorum: it carries the majority of nodes in the cluster.  By default, each node represents one vote in quorum calculations. However, you can modify this feature in order to ensure certain stable nodes with strong connections carry a greater value.  This section provides an overview of how Galera Cluster handles weighted values in quorum calculations.

- :doc:`streaming-replication`

  Normally, nodes transfer all replication and certification events on the transaction commit.  With Streaming Replication, the nodes break the transaction into fragments.  Then they certify, replicate and apply these replication fragments onto the slave nodes.  This section describes Streaming Replication, how it works and the limitations of its use.

.. toctree::
   :maxdepth: 2
   :hidden:

   tech-desc-introduction
   certification-based-replication
   architecture
   isolation-levels
   state-transfer
   node-states
   recovery
   weighted-quorum
   streaming-replication
