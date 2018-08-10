==========================
System Configuration
==========================
.. _`configuration`:

When you have finished installing Galera Cluster on your server hardware, you are ready to configure the database itself to serve as a node in your cluster.  To do this, you will need to edit the MySQL configuration file.

Using your preferred text editor, edit the ``/etc/my.cnf`` file.

.. code-block:: ini

   [mysqld]
   datadir=/var/lib/mysql
   socket=/var/lib/mysql/mysql.sock
   user=mysql
   binlog_format=ROW
   bind-address=0.0.0.0
   default_storage_engine=innodb
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0
   innodb_buffer_pool_size=122M
   wsrep_provider=/usr/lib/libgalera_smm.so
   wsrep_provider_options="gcache.size=300M; gcache.page_size=300M"
   wsrep_cluster_name="example_cluster"
   wsrep_cluster_address="gcomm://IP.node1,IP.node2,IP.node3"
   wsrep_sst_method=rsync

   [mysql_safe]
   log-error=/var/log/mysqld.log
   pid-file=/var/run/mysqld/mysqld.pid




--------------------------------
Configuring Database Server
--------------------------------
.. _`db-config`:

There are certain basic configurations that you will need to set up in the ``/etc/my.cnf`` file.  Before starting the database server, edit the configuration file for the following:

- Ensure that ``mysqld`` is not bound to 127.0.0.1.  This is IP address for localhost.  If the configuration variable appears in the file, comment it out:

  .. code-block:: ini

     # bind-address = 127.0.0.1

- Ensure that the configuration file includes the ``conf.d/``.

  .. code-block:: ini

     !includedir /etc/mysql/conf.d/

- Ensure that the binary log format is set to use row-level replication, as opposed to statement-level replication.

  .. code-block:: ini

     binlog_format=ROW

  Do not change this value, as it affects performance and consistency.  The binary log can only use row-level replication.

- Ensure that the default storage engine is InnoDB

  .. code-block:: ini

     default_storage_engine=InnoDB

  Galera Cluster will not work with MyISAM or similar nontransactional storage engines.

- Ensure that the InnoDB locking mode for generating auto-increment values is set to interleaved lock mode, which is designated by a ``2`` value.

  .. code-block:: ini

     innodb_autoinc_lock_mode=2

  Do not change this value.  Other modes may cause ``INSERT`` statements on tables with ``AUTO_INCREMENT`` columns to fail.

  .. note:: **Warning**: When `innodb_autoinc_lock_mode <http://dev.mysql.com/doc/refman/5.5/en/innodb-parameters.html#sysvar_innodb_autoinc_lock_mode>`_ is set to traditional lock mode, indicated by ``0``, or to consecutive lock mode, indicated by ``1``, in Galera Cluster it can cause unresolved deadlocks and make the system unresponsive.

- Ensure that the InnoDB log buffer is written to file once per second, rather than on each commit, to improve performance.

  .. code-block:: ini

     innodb_flush_log_at_trx_commit=0

  .. note:: **Warning**: While setting `innodb_flush_log_at_trx_commit <http://dev.mysql.com/doc/refman/5.1/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit>`_ to a value of ``0`` or ``2`` improves performance, it also introduces certain dangers.  Operating system crashes or power outages can erase the last second of transaction.  Although normally you can recover this data from another node, it can still be lost entirely in the event that the cluster goes down at the same time, (for instance, in the event of a data center power outage).


After you save the configuration file, you are ready to configure the database privileges.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring the InnoDB Buffer Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`config_innodb_buffer_pool_size`:

The InnoDB storage engine uses a memory buffer to cache data and indexes of its tables, which you can configure through the
`innodb_buffer_pool_size <http://dev.mysql.com/doc/refman/5.1/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size>`_ parameter.  The default value is 128MB.  To compensate for the increased memory usage of Galera Cluster over the standalone MySQL database server, you should scale your usual value back by 5%.

.. code-block:: ini

   innodb_buffer_pool_size=122M


-----------------------------------------
Configuring Swap Space
-----------------------------------------
.. _`swap-config`:

Memory requirements for Galera Cluster are difficult to predict with any precision.  The particular amount of memory it uses can vary significantly, depending upon the load the given node receives.  In the event that Galera Cluster attempts to use more memory than the node has available, the ``mysqld`` instance crashes.


The way to protect your node from such crashing is to ensure that you have sufficient swap space available on the server, either in the form of a swap partition or swap files.  To check the available swap space, run the following command:

.. code-block:: console

   $ swapon --summary
   Filename        Type        Size     Used    Priority
   /dev/sda2       partition   3369980  0       -1
   /swap/swap1     file        524284   0       -2
   /swap/swap2     file        524284   0       -3

If your system does not have swap space available or if the allotted space is insufficient for your needs, you can fix this by creating swap files.

#. Create an empty file on your disk, set the file size to whatever size you require.

   .. code-block:: console

      # fallocate -l 512M /swapfile

   Alternatively, you can manage the same using ``dd``.

   .. code-block:: console

      # dd if=/dev/zero of=/swapfile bs=1M count=512

#. Secure the swap file.

   .. code-block:: console

      # chmod 600 /swapfile

   This sets the file permissions so that only the root user can read and write to the file.  No other user or group member can access it.  You can view the results with ``ls``:

   .. code-block:: console

      $ ls -a / | grep swapfile
      -rw------- 1 root root 536870912 Feb 12 23:55 swapfile

#. Format the swap file.

   .. code-block:: console

      # mkswap /swapfile

#. Activate the swap file.

   .. code-block:: console

      # swapon /swapfile

#. Using your preferred text editor, update the ``/etc/fstab`` file to include the swap file by adding the following line to the bottom:

   .. code-block:: ini

      /swapfile none swap defaults 0 0

After you save the ``/etc/fstab`` file, you can see the results with ``swapon``.

.. code-block:: console

   $ swapon --summary
   Filename        Type        Size     Used    Priority
   /swapfile       file        524284   0       -1


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:




