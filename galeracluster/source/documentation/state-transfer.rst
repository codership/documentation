.. meta::
   :title: State Transfers with Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :doc:`Galera Parameters <galera-parameters>`
      - :ref:`gcache.dir <gcache.dir>`
      - :ref:`gcache.recover <gcache.recover>`
      - :ref:`Incremental St. Transfr. <state-transfer-ist>`
      - :doc:`sst`
      - :ref:`State Snap. Transfr. <state-transfer-sst>`

      .. cssclass:: bull-head

         Related Articles


.. raw:: html

    <style> .red {color:red} </style>

.. raw:: html

    <style> .green {color:green} </style>

.. role:: red
.. role:: green

.. cssclass:: library-document
.. _`state-transfer`:

==========================
State Transfers
==========================

The process of replicating data from the cluster to the individual node, bringing the node into sync with the cluster, is known as provisioning.  There are two methods available in Galera Cluster to provision nodes:

- :ref:`State Snapshot Transfers (SST) <state-transfer-sst>` Where a snapshot of the entire node state transfers.
- :ref:`Incremental State Transfers (IST) <state-transfer-ist>` Where only the missing transactions transfer.


.. _`state-transfer-sst`:
.. rst-class:: rubric-1
.. rubric:: State Snapshot Transfer (SST)

.. index::
   pair: Parameters; wsrep_sst_method
.. index::
   pair: State Snapshot Transfer methods; State Snapshot Transfer

In a :term:`State Snapshot Transfer` (SST), the cluster provisions nodes by transferring a full data copy from one node to another.  When a new node joins the cluster, the new node initiates a State Snapshot Transfer to synchronize its data with a node that is already part of the cluster.

You can choose from two conceptually different approaches in Galera Cluster to transfer a state from one database to another:

- **Logical** This method uses ``mysqldump``.  It requires that you fully initialize the receiving server and ready it to accept connections *before* the transfer.

  This is a blocking method.  The donor node becomes ``READ-ONLY`` for the duration of the transfer.  The State Snapshot Transfer applies the ``FLUSH TABLES WITH READ LOCK`` command on the donor node.

  ``mysqldump`` is the slowest method for State Snapshot Transfers.  This can be an issue in a loaded cluster.

- **Physical** This method uses ``rsync``, ``rsync_wan``, ``xtrabackup`` and other methods and copies the data files directly from server to server.  It requires that you initialize the receiving server *after* the transfer.

  This method is faster than ``mysqldump``, but they have certain limitations.  You can only use them on server startup.  The receiving server requires very similar configurations to the donor, (for example, both servers must use the same `innodb_file_per_table <https://dev.mysql.com/doc/refman/5.6/en/innodb-parameters.html#sysvar_innodb_file_per_table>`_ value).

  Some of these methods, such as ``xtrabackup`` can be made non-blocking on the donor.  They are supported through a scriptable SST interface.


For more information on the particular methods available for State Snapshot Transfers, see the :doc:`sst`.

You can set which State Snapshot Transfer method a node uses from the confirmation file.  For example:

.. code-block:: ini

   wsrep_sst_method=rsync_wan



.. _`state-transfer-ist`:
.. rst-class:: rubric-1
.. rubric:: Incremental State Transfer (IST)

.. index::
   pair: Parameters; wsrep_sst_method
.. index::
   pair: State Snapshot Transfer methods; Incremental State Transfer

In an :term:`Incremental State Transfer` (IST), the cluster provisions a node by identifying the missing transactions on the joiner and sends them only, instead of the entire state.

This provisioning method is only available under certain conditions:

- Where the joiner node :term:`state UUID` is the same as that of the group.

- Where all missing write-sets are available in the donor's write-set cache.

When these conditions are met, the donor node transfers the missing transactions alone, replaying them in order until the joiner catches up with the cluster.

For example, say that you have a node in your cluster that falls behind the cluster.  This node carries a node state that reads:

.. code-block:: text

   5a76ef62-30ec-11e1-0800-dba504cf2aab:197222

Meanwhile, the current node state on the cluster reads:

.. code-block:: text

   5a76ef62-30ec-11e1-0800-dba504cf2aab:201913

The donor node on the cluster receives the state transfer request from the joiner node.  It checks its write-set cache for the :term:`sequence number` ``197223``.  If that seqno is not available in the :term:`write-set cache`, a State Snapshot Transfer initiates.  If that seqno is available in the write-set cache, the donor node sends the commits from ``197223`` through to ``201913`` to the joiner, instead of the full state.

The advantage of Incremental State Transfers is that they can dramatically speed up the reemerging of a node to the cluster.  Additionally, the process is non-blocking on the donor.

.. note:: The most important parameter for Incremental State Transfers is ``gcache.size`` on the donor node.  This controls how much space you allocate in system memory for caching write-sets.  The more space available the more write-sets you can store.  The more write-sets you can store the wider the seqno gaps you can close through Incremental State Transfers.

   On the other hand, if the write-set cache is much larger than the size of your database state, Incremental State Transfers begun less efficient than sending a state snapshot.


.. _`state-transfer-gcache`:
.. rst-class:: rubric-2
.. rubric:: Write-set Cache (GCache)

.. index::
   pair: GCache; Descriptions
.. index::
   pair: Writeset Cache; Descriptions

Galera Cluster stores write-sets in a special cache called the :term:`Write-set Cache`, or GCache.  GCache cache is a memory allocator for write-sets.  Its primary purpose is to minimize the :term:`write-set` footprint on the :abbr:`RAM (Random Access Memory)`.  Galera Cluster improves upon this through the offload write-set storage to disk.

GCache employs three types of storage:

- **Permanent In-Memory Store** Here write-sets allocate using the default memory allocator for the operating system.  This is useful in systems that have spare :abbr:`RAM (Random Access Memory)`.  The store has a hard size limit.

  By default it is disabled.

- **Permanent Ring-Buffer File** Here write-sets pre-allocate to disk during cache initialization.  This is intended as the main write-set store.

  By default, its size is 128Mb.

- **On-Demand Page Store** Here write-sets allocate to memory-mapped page files during runtime as necessary.

  By default, its size is 128Mb, but can be larger if it needs to store a larger write-set.  The size of the page store is limited by the free disk space.  By default, Galera Cluster deletes page files when not in use, but you can set a limit on the total size of the page files to keep.

  When all other stores are disabled, at least one page file remains present on disk.

For more information on parameters that control write-set caching, see the ``gcache.*`` parameters on :doc:`Galera Parameters <galera-parameters>`.

Galera Cluster uses an allocation algorithm that attempts to store write-sets in the above order.  That is, first it attempts to use permanent in-memory store.  If there is not enough space for the write-set, it attempts to store to the permanent ring-buffer file.  The page store always succeeds, unless the write-set is larger than the available disk space.

By default, the write-set cache allocates files in the working directory of the process.  You can specify a dedicated location for write-set caching, using the :ref:`gcache.dir <gcache.dir>` parameter.

.. note:: Given that all cache files are memory-mapped, the write-set caching process may appear to use more memory than it actually does.

.. note:: If the :ref:`gcache.recover <gcache.recover>` parameter is set to ``yes``, an attempt to recover the gcache will be performed on startup, so that the node may continue to serve IST to other nodes. If set to ``no``, gcache will be invalidated on startup and the node will only be able to serve SST.
