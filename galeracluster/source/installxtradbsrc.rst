=========================================
Source Installation
=========================================
.. _'XtraDB Source Installation':

Percona XtraDB Cluster is the Percona implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  In the event that your Linux distribution is based on a different package management system or if it runs on a different unix-like operating system where binary installation packages are unavailable, such as Solaris or FreeBSD, you will need to build Percona XtraDB Cluster from source.

.. note:: This tutorial omits Percona XtraDB authentication options for brevity.

-----------------------------------------
Build Dependencies
-----------------------------------------
.. _`Build Dependencies`:

Before you begin building Percona XtraDB Cluster from source, you must first install the build dependencies on your server.  If your server uses a Debian-based distribution of Linux, run the following command:

.. code-block:: console

   # apt-get install build-essential flex bison automake \ 
         autoconf bzr libtool cmake libaio-dev mysql-client \
	 libncurses-dev zliblg-dev libbost-dev

If your server runs on an RPM-based distribution of Linux, instead run this command:

.. code-block:: console

   # yum install cmake gcc gcc-c++ libaio libaio-devel \ 
         automake autoconf bzr bison libtool ncurses5-devel \
	 boost

For other distributions and unix-like operating systems, consult the documentation for the appropriate package manager and syntax.

------------------------------------------
Building Percona XtraDB Cluster
------------------------------------------
.. _`Build Galera XtraDB`:

The source code for Percona XtraDB Cluster is available through Launchpad.net.  Using Bazaar with the ``branch`` argument, you can download the source code for your specific system.

.. code-block:: console

   $ bzr branch lp:percona-xtradb-cluster

Once Bazaar finishes running, you can start building the database server.  You have the option of using either the build script or compiling with ``cmake``.  If you decide to use the build script, the command varies depending on your server architecture.

- To run the build script on a 64-bit system, use the following command:

  .. code-block:: console

     # BUILD/compile-pentium64-wsrep

- To run the build script on a 32-bit system, instead use this command:

  .. code-block:: console

     # BUILD/compile-pentium-wsrep

- To build using ``cmake``, instead run these commands:

  .. code-block:: console

     # cmake -DWITH_WSREP=1 -DWITH_INNODB_DISALLOW_WRITES=1
     # make

Galera Cluster for Percona XtraDB is now installed on your server.

.. seealso:: In the event that you built Percona XtraDB Cluster over an existing standalone instance of Percona XtraDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.
