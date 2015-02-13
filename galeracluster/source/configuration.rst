==========================
System Configuration
==========================
.. _`configuration`:

When you have finished installing Galera Cluster on your server hardware, you are ready to configure the database itself to serve as a node in your cluster.  To do this, you will need to edit the MySQL configuration file.

Using your preferred text editor, edit the ``/etc/my.cnf`` file.

.. code-block:: ini
		
   [mysql]
   datadir=/var/lib/mysql
   socket=/var/lib/mysql/mysql.sock
   user=mysql
   binlog_format=ROW
   bind-address=0.0.0.0
   default-storage-engine=innodb
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0
   wsrep_provider=/usr/lib/libgalera_smm.so
   wsrep_provider_options="gcache.size=300M; gcache.page_size=1G"
   wsrep_cluster_name="example_cluster"
   wsrep_cluster_address="gcomm://IP.node1,IP.node2,IP.node3"
   wsrep_sst_method=rsync

   [mysql_safe]
   log-error=/var/log/mysqld.log
   pid-file=/var/run/mysqld/mysqld.pid




--------------------------------
Database Configuration
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

  Galera Cluster will not work with MyISAM or similar nontransactional storage eninges.

- Ensure that the InnoDB locking mode for generating auto-increment values is set to interleaved lock mode, which is designated by a ``2`` value.

  .. code-block:: ini

     innodb_autoinc_lock_mode=2

  Do not change this value.  Other modes may cause ``INSERT`` statements on tables with ``AUTO_INCREMENT`` columns to fail.  

  .. warning:: When `innodb_autoinc_lock_mode <http://dev.mysql.com/doc/refman/5.5/en/innodb-parameters.html#sysvar_innodb_autoinc_lock_mode>`_ is set to traditional lock mode, indicated by ``0``, or to consecutive lock mode, indicated by ``1``, in Galera Cluster it can cause unresolved deadlocks and make the system unresponsive.

- Ensure that the InnoDB log buffer is written to file once per second, rather than on each commit, to improve performance.

  .. code-block:: ini

     innodb_flush_logs_at_trx_commit=0

  .. warning:: While setting `innodb_flush_logs_at_trx_commit <http://dev.mysql.com/doc/refman/5.1/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit>`_ to a value of ``0`` or ``2`` improves performance, it also introduces certain dangers.  Operating system crashes or power outages can erase the last second of transaction.  Although normally you can recover this data from another node, it can still be lost entirely in the event that the cluster goes down at the same time, (for instance, in the event of a data center power outage).


After you save the configuration file, you are ready to configure the database privileges.

--------------------------------------
Configuring State Transfer Privileges
--------------------------------------
.. _`sst-privileges`:

Galera Cluster uses state transfers to send data from one database node into another.  When this occurs through the database server, such as is the case with ``mysqldump``, the node requires a user with privileges on the receiving server.

Using your preferred text editor, open ``wsrep.cnf`` file, (you can find it in ``/etc/mysql/conf.d/``), and edit the authentication information:

.. code-block:: ini

   wsrep_sst_auth = wsrep_sst-user:password

This provides the authentication information that the node requires.  Use the same value on all nodes in the cluster, as the parameter is used to authenticate both the sender and the receiver.

.. seealso:: For more information on authentication for the state transfer user, see :ref:`wsrep_sst_auth <wsrep_sst_auth>`.

Once you finish editing the ``wsrep.cnf`` file, start the database server and configure the privileges on the ``mysql`` tables.  If your system uses ``init``, you can start ``mysqld`` with the following command:

.. code-block:: console

   # service mysql start

For systems that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl start mysql

Once the server is running, you can use the database client to configure user privileges for the node, to remove empty users and create the write-set replication user for state snapshot transfers.

In the case of empty users, they create problems for database authentication matching rules.  Remove them with the following query:

.. code-block:: mysql

   SET wsrep_on=OFF;
   DELETE FROM mysql.user WHERE user='';

Next grant privileges to the write-set replication user.  Use the same username and password you used for the ``wsrep.cnf`` file.

.. code-block:: mysql

   SET wsrep_on=OFF;
   GRANT ALL ON *.* TO 'wsrep_sst-user'@'%'
      IDENTIFIED BY 'password';

When the node now attempts state snap transfers, it will use this user and password to authenticate both its own access to the database and to access and manipulate data on the receiving node.  There are a few different methods used in state snapshot transfers.  This authentication only occurs in the event of ``mysqldump``.  ``rsync`` operates independent of the database and thus ignores this parameter.

.. note:: While you can configure which state transfer method you want the node to use, if you choose ``rsync`` you should still configure for ``mysqldump``.  In the event of Incremental State Transfers, the cluster itself chooses whichever method will run the fastest.

Once finished, shut the node down until you are ready to initialize the cluster.  For systems that use ``init``, run the following command:

.. code-block:: console

   # service mysql stop

For systems that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl stop mysql

.. seealso:: For more information on state snapshot and incremental state transfers, see :doc:`statetransfer`.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:




