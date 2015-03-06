============================
Migrating to Galera Cluster
============================
.. _`migration`:

For systems that already have instances of the standalone versions of MySQL, MariaDB or Percona XtraDB, the Galera Cluster installation replaces the existing database server with a new one that includes the wsrep API patch.  This only affects the database server, not the data.

When upgrading from a standalone database server, you must take some additional steps in order to subsequently preserve and use your data with Galera Cluster.

.. seealso:: For more information on installing Galera Cluster, see :doc:`galerainstallation`.

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

.. seealso:: For more information on initializing and adding nodes to a cluster, see :doc:`startingcluster`.
