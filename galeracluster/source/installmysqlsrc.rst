=========================================
Source Installation
=========================================
.. _`MySQL Source Installation`:

Galera Cluster for MySQL is the reference implementation from Codership Oy.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  In the event that your Linux distribution is based upon a different package management system, if your server uses a different unix-like operating system, such as Solaris or FreeBSD, you will need to build Galera Cluster for MySQL from source.


.. note:: This tutorial omits MySQL authentication options for brevity.

-----------------------------------------
Build Dependencies
-----------------------------------------
.. _`Build Dependencies`:

Before you begin building Galera Cluster for MySQL from source, you must first install the build dependencies on your server.  If your system uses a Debian-based distribution of Linux, run the following command:

.. code-block:: console

   # apt-get build-dep mysql-server

For systems that use an RPM-based distribution, instead run this command:

.. code-block:: console

   # yum-builddep MySQL-server

For other distributions and unix-like operating systems, consult the documentation for the appropriate package manager and syntax.


--------------------------------------------
Building Galera Cluster for MySQL
--------------------------------------------
.. `Build Galera MySQL`:

The source code for Galera Cluster for MySQL is available through `Github <http://github.com>`_.  You can download the source code using ``git``.

.. code-block:: console

   $ git clone http://github.com/codership/mysql-wsrep.git

Once ``git`` finishes running, you can start building the database server.  You have two options for how to build Galera CLuster for MySQL.  You can use the build script, or you can build it using ``cmake``.  If you choose the build script, the command will vary depending upon your system architecture.  From the ``mysql-wsrep/`` directory, use one of the following commands:

- To run the build script on a 64-bit system, use this command:

  .. code-block:: console

     # BUILD/compile-pentium64

- To run the build script on a 32-bit system, instead use this command:

  .. code-block:: console

     # BUILD/compile-penitum

- To build Galera Cluster for MySQL using ``cmake``, run the following commands:

  .. code-block:: console

     # cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=1
     # make
     # make install

Galera Cluster for MySQL  is now installed on your server.

.. seealso:: In the event that you built Galera Cluster for MySQL over an existing standalone instance of MySQL, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.




