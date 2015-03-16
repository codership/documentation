=========================================
Source Installation
=========================================
.. _'MariaDB-Source Installation':

MariaDB Galera Cluster is the MariaDB implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  In the event that your Linux distribution is based on a different package management system, or if it runs on a different unix-like operating system where binary installation packages are not available, such as Solaris or FreeBSD, you will need to build MariaDB Galera Cluster from source.

.. note:: This tutorial omits MariaDB authentication options for brevity.

-----------------------------------------
Build Dependencies
-----------------------------------------
.. _`Build Dependencies`:

Before you begin building MariaDB Galera Cluster from source, you must first install the build dependencies on your server.  If your system uses a Debian-based distribution of Linux, run the following command:

.. code-block:: console

   # apt-get build-dep mysql-server

For system uses an RPM-based distribution, instead run this command:

.. code-block:: console

   # yum-builddep MariaDB-server

For other distributions and unix-like operating systems, consult the documentation for the appropriate package manager and syntax.


--------------------------------------------
Building the Galera Cluster for MariaDB
--------------------------------------------
.. _`Build Galera MariaDB`:

The source code for MariaDB Galera Cluster is available through Launchpad.net.  Using Bazaar with the ``branch`` argument, you can download the source code for your specific system:

.. code-block:: console

   $ bzr branch lp:maria trunk

Once Bazaar finishes running, you can start building the database server.  You have two options for how to build MariaDB Galera Cluster.  You can use a build script or you can build it using ``cmake``.  If you choose to use a build script, the command will vary depending upon your system architecture.

- To run the build script on a 64-bit system, use the following command:

  .. code-block:: console

     # BUILD/compile-pentium64-max

- To run the build script on a 32-bit system, instead use this command:

  .. code-block:: console

     # BUILD/compile-pentium-max

- To build MariaDB Galera Cluster using ``cmake``, run the following commands from the source code directory:

  .. code-block:: console

     # cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=1
     # make
     # make install

MariaDB Galera Cluster is now installed on your server.

.. seealso:: In the event that you built MariaDB Galera Cluster over an existing standalone instance of MariaDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.
