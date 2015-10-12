============================
Migrating to Galera Cluster
============================
.. _`migration`:

For systems that already have instances of the standalone versions of MySQL, MariaDB or Percona XtraDB, the Galera Cluster installation replaces the existing database server with a new one that includes the :term:`wsrep API` patch.  This only affects the database server, not the data.

When upgrading from a standalone database server, you must take some additional steps in order to subsequently preserve and use your data with Galera Cluster.

.. note:: **See Also**: For more information on installing Galera Cluster, see :doc:`galerainstallation`.

-----------------------------------
Upgrading System Tables
-----------------------------------
.. _`upgrade-system-tables`:

When you finish upgrading a standalone database server to Galera Cluster, but before you initialize your own cluster, you need to update the system tables to take advantage of the new privileges and capabilities.  You can do this with ``mysql_upgrade``.

In order to use ``mysql_upgrade``, you need to first start the database server, but start it without initializing replication.  For systems that use ``init``, run the following command:

.. code-block:: console

   # service mysql start --wsrep_on=OFF

For servers that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl start mysql --wsrep_on=OFF

The command starts ``mysqld`` with the :ref:`wsrep_on <wsrep_on>` parameter set to ``OFF``, which disables replication.  With the database server running, you can update the system tables:

.. code-block:: console

   # mysql_upgrade

If this command generates any errors, check the MySQL Reference Manual for more information related to the particular error message.  Typically, these errors are not critical and you can usually ignore them, unless they relate to specific functionality that your system requires. 

When you finish upgrading the system tables, you need to stop the ``mysqld`` process until you are ready to initialize the cluster.  For servers that use ``init``, run the following command:

.. code-block:: console

   # service mysql stop

For servers that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl stop mysql

Running this command stops database server.  When you are ready to initialize your cluster, choose this server as your starting node.  

.. note:: **See Also**: For more information on initializing and adding nodes to a cluster, see :doc:`startingcluster`.

---------------------------------------
Migrating from MySQL to Galera Cluster
---------------------------------------
.. _`migrating-mysql-galera`:

In the event that you have an existing database server using the MyISAM storage engine or the stock MySQL master-slave cluster, there are some additional steps that you must take in order to migrate your data to Galera Cluster.

There are two stages to this migration: migrating the database state from the previous installation to Galera Cluster and migrating the MySQL installation on the former master node to Galera Cluster.

^^^^^^^^^^^^^^^^^^^^^^^^^^^
Data Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`data-migration`:

The first stage of migration is to transfer the database state from the existing system to Galera Cluster.  Begin by creating a cluster.  For more information on how to do so, see :doc:`gettingstarted`.

- For migration from a standalone MySQL server, create the cluster using only new nodes.

- For migration from a stock MySQL master-slave cluster, create the cluster using only slave nodes.

You now have Galera Cluster and a single MySQL server running together.  The MySQL server is hereafter referred to as the MyISAM master.  To migrate your data from the MyISAM master to Galera Cluster, complete the following steps:

#. Stop all load on the MyISAM master.

#. Run ``mysqldump`` to create a state snapshot.

   .. code-block:: console

      $ mysqldump --skip-create-options --all-databases > sst.sql

   The ``--skip-create-options`` ensures that the newly created tables default to InnoDB.

#. Transfer the ``sst.sql`` file to one of the Galera Cluster nodes, then load the data through the database client.

   .. code-block:: console

      $ mysql -u root -p < sst.sql 
		   
#. When the node finishes loading the data, resume the load on Galera Cluster.  Leave the MyISAM master offline.

When the load resumes, it runs on Galera Cluster alone, excluding the MyISAM master.  The other nodes in your cluster replicate the data out from the first on their own.

Downtime for migration depends on the size of your database and how long it takes ``mysqldump`` to download from one and upload to the other.  

^^^^^^^^^^^^^^^^^^^^^^^^^
Database Migration
^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`database-migration`:

After the above procedure, you now have Galera Cluster running independent of the MyISAM master.  In order to continue using this node, you need to migrate it from MySQL to Galera Cluster and from MyISAM to InnoDB.

#. Install Galera Cluster on the former MyISAM master node.

#. Start the node without replication.  For servers that use ``init``, run the following command:

   .. code-block:: console

      # service mysql start --wsrep_on=OFF

   For servers that use ``systemd``, instead run this command:

   .. code-block:: console

      # systemctl start mysql --wsrep_on=OFF

#. From the database client, convert each table from MyISAM to InnoDB.

   .. code-block:: mysql

      ALTER TABLE table ENGINE=InnoDB;

#. From one of the nodes already running Galera Cluster, copy the ``grastate.dat`` file to the former MyISAM master node.

#. Using your preferred text editor, in the ``grastate.dat`` file on the former MyISAM master, change the sequence number (seqno) value from ``-1`` to ``0``.

#. Restart the node.  For servers that use ``init``, run the following command:

   .. code-block:: console

      # service mysql restart

   For servers that use ``systemd``, instead run this command:

   .. code-block:: console

      # systemctl restart mysql

When the database server starts on the former MyISAM master, it launches as a node rejoining the cluster and will request a state transfer to catch up with any changes that occurred while it was offline.




