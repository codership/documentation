
.. raw:: html

    <style> .red {color:red} </style>

.. raw:: html

    <style> .green {color:green} </style>

.. role:: red
.. role:: green


===============================
State Snapshot Transfers
===============================
.. _`State Snapshot Transfers`:

When a node requires a state transfer from the cluster, by default it attempts the :term:`Incremental State Transfer` (IST) method.  In the event that there are no nodes available for this or if it finds a manual donor defined through the :ref:`wsrep_sst_donor <wsrep_sst_donor>` parameter, uses a :term:`State Snapshot Transfer` (SST) method.

Galera Cluster supports several back-end methods for use in state snapshot transfers.  There are two types of methods available: Logical State Snapshots, which interface through the database server and client; and Physical State Snapshots, which copy the data files directly from node to node.
 
+------------------+------------------+-------------------+--------------------+------------------+-----------------------+
| Method           | Speed            | Blocks Donor      | Available          | Type             | DB Root Access        |
|                  |                  |                   | on Live Node       |                  |                       |
+==================+==================+===================+====================+==================+=======================+
| :ref:`mysqldump  | :red:`Slow`      | :green:`Blocks`   | :green:`Available` | :ref:`Logical    | Donor and Joiner      |
| <mysqldump>`     |                  |                   |                    | <sst-logical>`   |                       |
+------------------+------------------+-------------------+--------------------+------------------+-----------------------+
| :ref:`rsync      | :green:`Fastest` | :green:`Blocks`   | :red:`Unavailable` | :ref:`Physical   | None                  |
| <rsync>`         |                  |                   |                    | <sst-physical>`  |                       |
+------------------+------------------+-------------------+--------------------+------------------+-----------------------+
| :ref:`xtrabackup | :green:`Fast`    | Briefly           | :red:`Unavailable` | :ref:`Physical   | Donor only            |
| <xtrabackup>`    |                  |                   |                    | <sst-physical>`  |                       |
+------------------+------------------+-------------------+--------------------+------------------+-----------------------+


To set the State Snapshot Transfer method, use the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter.  For example:

.. code-block:: ini

   wsrep_sst_method = rsync

There is no single best method for State Snapshot Transfers.  You must decide which best suits your particular needs and cluster deployment.  Fortunately, you need only set the method on the receiving node.  So long as the donor has support, it servers the transfer in whatever method the joiner requests.

-------------------------------
Logical State Snapshot
-------------------------------
.. _`sst-logical`:

There is one back-end method available for a Logical State Snapshots: ``mysqldump``.

The :term:`Logical State Transfer Method` has the following advantages:

- These transfers are available on live servers.  In fact, only a fully initialized server can receive a Logical State Snapshot.

- These transfers do not require the receptor node to have the same configuration as the donor node.  This allows you to upgrade storage engine options.

  For example, when using this transfer method you can migrate from the Antelope to the Barracuda file format, use compression resize, or move iblog* files from one partition into another.

The Logical State Transfer Method has the following disadvantages:

- These transfers are as slow as ``mysqldump``.

- These transfers require that you configure the receiving database server to accept root connections from potential donor nodes.

- The receiving server must have a non-corrupted database.

^^^^^^^^^^^^^^^
``mysqldump``
^^^^^^^^^^^^^^^
.. _`mysqldump`:

The main advantage of ``mysqldump`` is that you can transfer a state snapshot to a working server.  That is, you start the server standalone and then instruct it to join a cluster from within the database client command line.  You can also use it to migrate from an older database format to a newer one.

``mysqldump`` requires that the receiving node have a fully functional database, which can be empty.  It also requires the same root credentials as the donor and root access from the other nodes.

This transfer method is several times slower than the others on sizable databases, but it may prove faster in cases of very small databases.  For instance, on a database that is smaller than the log files.

.. note:: **Warning**: This transfer method is sensitive to the version of ``mysqldump`` each node uses.  It is not uncommon for a given cluster to have installed several versions.  A State Snapshot Transfer can fail if the version one node uses is older and incompatible with the newer server.

On occasion, ``mysqldump`` is the only option available.  For instance, if you upgrade from a cluster using MySQL 5.1 with the built-in InnoDB support to MySQL 5.5, which uses the InnoDB plugin.

The ``mysqldump`` script only runs on the sending node.  The output from the script gets piped to the MySQL client that connects to the joiner node.

Because ``mysqldump`` interfaces through the database client, configuring it requires several steps beyond setting the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter.  For more information on its configuration, see:

.. toctree::

   mysqldump

.. note:: **See Also**: For more information on ``mysqldump``, see `mysqldump Documentation <http://dev.mysql.com/doc/refman/5.6/en/mysqldump.html>`_.

----------------------------------------
Physical State Snapshot
----------------------------------------
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


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``rsync``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`rsync`:

The fastest back-end method for State Snapshot Transfers is ``rsync``.  It carries all the advantages and disadvantages of of the Physical Snapshot Transfer.  While it does block the donor node during transfer, ``rsync`` does not require database configuration or root access, which makes it easier to configure.

When using terabyte-scale databases, ``rsync`` is considerably faster, (1.5 to 2 times faster), than ``xtrabackup``.  This translates to a reduction in transfer times by several hours.

``rsync`` also features the rsync-wan modification, which engages the ``rsync`` delta transfer algorithm.  However, given that this makes it more I/O intensive, you should only use it when the network throughput is the bottleneck, which is usually the case in :abbr:`WAN (Wide Area Network)` deployments.

.. note:: The most common issue encountered with this method is due to incompatibilities between the various versions of ``rsync`` on the donor and joining nodes.

The ``rsync`` script runs on both donor and joining nodes.  On the joiner, it starts ``rsync`` in server-mode and waits for a connection from the donor.  On the donor, it starts ``rsync`` in client-mode and sends the contents of the data directory to the joining node.

.. code-block:: ini

   wsrep_sst_method = rsync

For more information about ``rsync``, see the `rsync Documentation <http://rsync.samba.org/>`_.
	

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``xtrabackup``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`xtrabackup`:

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
