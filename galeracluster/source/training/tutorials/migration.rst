.. meta::
   :title: Migrating to Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`
      - :ref:`search`

      Related Documents

      - :ref:`wsrep_on <wsrep_on>`
      - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
      - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
      - :ref:`Upgrading System Tables <upgrade-system-tables>`

      Related Articles

      - :doc:`Galera Installation <galera-installation>`
      - :doc:`Starting the Cluster <starting-cluster>`
      - :doc:`System Configuration <configuration>`
      - :doc:`Replication Configuration <wsrep-configuration>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`migration`:

============================
Migrating to Galera Cluster
============================

.. rst-class:: article-stats

   Length: xxx words; Published: October 20, 2014; Topic: General; Level: Beginner

For systems that already have instances of the standalone versions of MySQL or MariaDB, the Galera Cluster installation replaces the existing database server with a new one that includes the :term:`wsrep API` patch. This only affects the database server, not the data.

When upgrading from a standalone database server, you must take some additional steps in order to subsequently preserve and use your data with Galera Cluster.

For more information on installing Galera Cluster, see :doc:`Galera Installation <galera-installation>`.


.. _`upgrade-system-tables`:
.. rst-class:: section-heading
.. rubric:: Upgrading System Tables

When you finish upgrading a standalone database server to Galera Cluster, but before you initialize your own cluster, you need to update the system tables to take advantage of the new privileges and capabilities. You can do this with ``mysql_upgrade``.

In order to use ``mysql_upgrade``, you need to first start the database server, but start it without initializing replication. For systems that use ``init``, run the following command:

.. code-block:: console

   # service mysql start --wsrep_on=OFF

For servers that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl start mysql --wsrep_on=OFF

The command starts ``mysqld`` with the :ref:`wsrep_on <wsrep_on>` parameter set to ``OFF``, which disables replication. With the database server running, you can update the system tables:

.. code-block:: console

   # mysql_upgrade

If this command generates any errors, check the MySQL Reference Manual for more information related to the particular error message. Typically, these errors are not critical and you can usually ignore them, unless they relate to specific functionality that your system requires.

When you finish upgrading the system tables, you need to stop the ``mysqld`` process until you are ready to initialize the cluster. For servers that use ``init``, run the following command:

.. code-block:: console

   # service mysql stop

For servers that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl stop mysql

Running this command stops database server. When you are ready to initialize your cluster, choose this server as your starting node.

For more information on initializing and adding nodes to a cluster, see :doc:`Starting the Cluster <starting-cluster>`.


.. _`migrating-mysql-galera`:
.. rst-class:: section-heading
.. rubric:: Migrating from MySQL to Galera Cluster

In the event that you have an existing database server that uses the MyISAM storage engine or the stock MySQL primary-replica replication, there are some additional steps that you need to take. The :term:`Galera Replication Plugin` requires a transactional storage engine in order to function. As MyISAM is non-transactional, you need to migrate your data to InnoDB, in addition to installing the new software packages.

There are three types of database servers referred to in this guide:

- **Primary Server** Refers to the MySQL primary (formerly referred to as master) server.
- **Replica Server**  Refers to a MySQL replica (formerly referred to as slave) server.
- **Cluster Node** Refers to a node in Galera Cluster.

For the sake of simplicity, replica servers and cluster nodes are referenced collectively, rather than individually. In production, you may have several replica servers and must have at least three cluster nodes.


.. _`migrate-infrastructure`:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Infrastructure Preparation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For your existing infrastructure, you have a MySQL primary server as well as several replica servers that form a primary-replica cluster. Before you can begin migration, you first need to prepare your infrastructure for the change.

#. Launch at least three new servers, outside of and unconnected to your existing database infrastructure.

#. On each new server, install Galera Cluster. For information on how to do this, see :doc:`Galera Installation <galera-installation>`.

#. Configure the database server. In addition to the IP addresses of each node, on the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter, include the IP addresses of the MySQL primary server and each instance of the replica servers.

For more information on configuring Galera Cluster, see :doc:`System Configuration <configuration>` and :doc:`Replication Configuration <wsrep-configuration>`.

#. When you finish the installation and configuration, start the cluster. For more information on how to start the cluster, see :doc:`Starting the Cluster <starting-cluster>`.

To check that it is running properly, log into one of the database clients and run the :ref:`wsrep_cluster_size <wsrep_cluster_size>` status variable:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Varialbe_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 3     |
   +--------------------+-------+

Galera Cluster is now running in parallel to your MySQL primary-replica cluster. It contains no data and remains unused by your application servers. You can now begin migrating your data.


.. _`migrate-data`:

^^^^^^^^^^^^^^^^^^^
Data Migration
^^^^^^^^^^^^^^^^^^^

In order to migrate data from a MySQL primary-replica cluster to Galera Cluster, you need to manually transfer it from your existing infrastructure to the new one.

#. Stop the load of the primary server.

#. On the primary server, run ``mysqldump``:

   .. code-block:: console

      $ mysqldump -u root -p --skip-create-options --all-databases > migration.sql

   The ``--skip-create-options`` ensures that the database server uses the default storage engine when loading the data, instead of MyISAM.
   
   .. note:: If the migration does not correctly import all data, you can try to export the data and manually change the database engine.

#. Transfer the ``migration.sql`` output file to one of your new cluster nodes.

   .. code-block:: console

      $ scp migration.sql user@galera-node-IP

#. On the cluster node, load the data from the primary server.

   .. code-block:: console

      mysql -u root -p < migration.sql

#. Restart the load from the application servers, this time directing it towards your cluster nodes instead of the primary server.

Your application now uses Galera Cluster, instead of your previous MySQL primary-replica cluster.

.. note:: Bear in mind that your application will experience downtime at this stage of the process. The length of the downtime varies depending on the amount of data you have to migrate, specifically how long it takes ``mysqldump`` to create a snapshot of the primary server, then transfer and upload it onto a cluster node.


.. _`migrate-db`:

^^^^^^^^^^^^^^^^^^^^
Database Migration
^^^^^^^^^^^^^^^^^^^^

With your application server now using the new cluster nodes, you now need to migrate your primary and replica servers from stock MySQL to Galera Cluster.

#. Using the same process described in :doc:`Galera Installation <galera-installation>`, install and configure Galera Cluster on the server.

#. Start the node with replication disabled. For servers that use ``init``, run the following command:

   .. code-block:: console

      # service mysql start --wsrep-on=OFF

   For servers that use ``systemd``, instead run this command:

   .. code-block:: console

      # systemctl start mysql --wsrep-on=OFF

#. From the database client, manually switch the storage engine on each table from MyISAM to InnoDB:

   .. code-block:: mysql

      ALTER TABLE table_name ENGINE = InnoDB;

#. Update the system tables:

   .. code-block:: console

      # mysql_upgrade

    For more information, see :ref:`Upgrading System Tables <upgrade-system-tables>`.

#. From one of the running Galera Cluster nodes, copy the ``grastate.dat`` file into the data directory of the former MySQL primary server.

   .. code-block:: console

      $ scp grastate.dat user@server-primary-ip:/path/to/datadir

#. Using your preferred text editor, on the former MySQL primary server update the sequence number (that is, the seqno) in the ``grastate.dat`` file from ``-1`` to ``0``.

#. Restart the primary and replica servers. For servers that use ``init``, run the following command:

   .. code-block:: console

      # service mysql restart

   For servers that use ``systemd``, instead run this command:

   .. code-block:: console

      # systemctl restart mysql

#. Resume load on these servers.

When the former MySQL primary and replica servers come back after restarting, they establish network connectivity with the cluster and begin catching up with recent changes. All of the servers now function as nodes in Galera Cluster.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_on <wsrep_on>`
   - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
   - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
   - :ref:`Upgrading System Tables <upgrade-system-tables>`

   Related Articles

   - :doc:`Galera Installation <galera-installation>`
   - :doc:`Starting the Cluster <starting-cluster>`
   - :doc:`System Configuration <configuration>`
   - :doc:`Replication Configuration <wsrep-configuration>`
