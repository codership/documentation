.. cssclass:: library-document

========================
Physical State Snapshot
========================
.. _`sst-physical`:


There are two back-end methods available for Physical State Snapshots: ``rsync`` and ``xtrabackup``.

The :term:`Physical State Transfer Method` has the following advantages:

- These transfers physically copy the data from one node to the disk of the other, and as such do not need to interact with the database server at either end.

- These transfers do not require the database to be in working condition, as the donor node overwrites what was previously on the joining node disk.

- These transfers are faster.

The Physical State Transfer Method has the following disadvantages:

- These transfers require the joining node to have the same data directory layout and the same storage engine configuration as the donor node.  For example, you must use the same file-per-table, compression, log file size and similar settings for InnoDB.

- These transfers are not accepted by servers with initialized storage engines.

  What this means is that when your node requires a state snapshot transfer, the database server must restart to apply the changes.  The database server remains inaccessible to the client until the state snapshot transfer is complete, since it cannot perform authentication without the storage engines.


.. _`sst-physical-rsync`:

----------------------------
``rsync``
----------------------------

The fastest back-end method for State Snapshot Transfers is ``rsync``.  It carries all the advantages and disadvantages of of the Physical Snapshot Transfer.  While it does block the donor node during transfer, ``rsync`` does not require database configuration or root access, which makes it easier to configure.

When using terabyte-scale databases, ``rsync`` is considerably faster, (1.5 to 2 times faster), than ``xtrabackup``.  This translates to a reduction in transfer times by several hours.

``rsync`` also features the rsync-wan modification, which engages the ``rsync`` delta transfer algorithm.  However, given that this makes it more I/O intensive, you should only use it when the network throughput is the bottleneck, which is usually the case in :abbr:`WAN (Wide Area Network)` deployments.

.. note:: The most common issue encountered with this method is due to incompatibilities between the various versions of ``rsync`` on the donor and joining nodes.

The ``rsync`` script runs on both donor and joining nodes.  On the joiner, it starts ``rsync`` in server-mode and waits for a connection from the donor.  On the donor, it starts ``rsync`` in client-mode and sends the contents of the data directory to the joining node.

.. code-block:: ini

   wsrep_sst_method = rsync

For more information about ``rsync``, see the `rsync Documentation <http://rsync.samba.org/>`_.


.. _`sst-physical-xtrabackup`:

----------------------------
``xtrabackup``
----------------------------

The most popular back-end method for State Snapshot Transfers is ``xtrabackup``.  It carries all the advantages and disadvantages of a Physical State Snapshot, but is virtually non-blocking on the donor node.

``xtrabackup`` only blocks the donor for the short period of time it takes to copy the MyISAM tables, (for instance, the system tables).  If these tables are small, the blocking time remains very short.  However, this comes at the cost of speed: a state snapshot transfer that uses ``xtrabackup`` can be considerably slower than one that uses ``rsync``.

Given that ``xtrabackup`` copies a large amount of data in the shortest possible time, it may also noticeably degrade donor performance.

.. note:: The most common issue encountered with this method is due to its configuration.  ``xtrabackup`` requires that you set certain options in the configuration file, which means having local root access to the donor server.


.. code-block:: ini

   [mysqld]
   wsrep_sst_auth = <wsrep_sst_user>:<password>
   wsrep_sst_method = xtrabackup
   datadir = /path/to/datadir

   [client]
   socket = /path/to/socket

For more information on ``xtrabackup``, see the `Percona XtraBackup User Manual <https://www.percona.com/doc/percona-xtrabackup/2.1/manual.html?id=percona-xtrabackup:xtrabackup_manual>`_ and `XtraBackup SST Configuration <http://www.percona.com/doc/percona-xtradb-cluster/5.6/manual/xtrabackup_sst.html>`_.
