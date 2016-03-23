===========================================
MariaDB Galera Cluster- Source Installation
===========================================
.. _'MariaDB-Source Installation':

MariaDB Galera Cluster is the MariaDB implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  In the event that your Linux distribution is based on a different package management system, or if it runs on a different unix-like operating system where binary installation packages are not available, such as Solaris or FreeBSD, you will need to build MariaDB Galera Cluster from source.


.. note:: **See Also**: In the event that you built MariaDB Galera Cluster over an existing standalone instance of MariaDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.




---------------------------------
Preparing the Server
---------------------------------
.. _`installmariadb-prep-server`:

When building from source code, ``make`` cannot manage or install dependencies for either Galera Cluster or the build process itself.  You need to install these packages first.

- For Debian-based distributions of Linux, if MariaDB is available in your repositories, you can run the following command:

  .. code-block:: console

     # apt-get build-dep mariadb-server

- For RPM-based distributions, instead run this command:

  .. code-block:: console

     # yum-builddep MariaDB-server

In the event that neither command works for your system or that you use a different Linux distribution or FreeBSD, the following packages are required:

- **MariaDB Database Server with wsrep API**: Git, CMake, GCC and GCC-C++, Automake, Autoconf, and Bison, as well as development releases of libaio and ncurses.

- **Galera Replication Plugin**: SCons, as well as development releases of Boost, Check and OpenSSL.

Check with the repositories for your distribution or system for the appropriate package names to use during installation.  Bear in mind that different systems may use different names and that some may require additional packages to run.  For instance, to run CMake on Fedora you need both ``cmake`` and ``cmake-fedora``.  

     
-----------------------------------------
Building MariaDB Galera Cluster
-----------------------------------------
.. _`build-galera-mariadb`:

The source code for MariaDB Galera Cluster is available through GitHub_. Using Git you can download the source code to build MariaDB and the Galera Replicator Plugin locally on your system.

#. Clone the MariaDB database server repository.

   .. code-block:: console

      # git clone https://github.com/mariadb/server


#. Checkout the branch for the version that you want to use.

   .. code-block:: console

      # git checkout 10.0-galera

   The main branches available for MariaDB Galera Cluster are:

   - ``10.1``
   - ``10.0-galera``
   - ``5.5-galera``

   Starting with version 10.1, MariaDB includes the wsrep API for Galera Cluster by default.

   .. note:: **Warning**: MariaDB version 10.1 is still in beta.

     
You now have the source files for the MariaDB database server with the wsrep API needed to function as a Galera Cluster node.

In addition to the database server, you also need the wsrep Provider, also known as the Galera Replicator Plugin.  In a separate directory run the following command:
     
.. code-block:: console
		
   # cd ..
   # git clone https://github.com/codership/galera.git

Once Git finishes downloading the source files, you can start building the database server and the Galera Replicator Plugin.  You now have the source files for the database server in a ``server/`` directory and the Galera source files in ``galera/``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Building the Database Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`build-mariadb`:

The database server for Galera Cluster is the same as that of the standard database servers for  standalone instances of MariaDB, with the addition of a patch for the wsrep API, which is packaged in the version downloaded from GitHub_.  You can enable the patch through the ``WITH_WSREP`` and ``WITH_INNODB_DISALLOW_WRITES`` CMake configuration options.

To build the database server, ``cd`` into the ``server/`` directory and run the following commands:

.. code-block:: console

   # cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON ./
   # make
   # make install


.. note:: In addition to compiling through ``cmake`` and ``make``, there are also a number of build scripts in the ``BUILD/`` directory, which you may find more convenient to use.  For example, 

	  .. code-block:: console

	     # ./BUILD/compile-pentium64-wsrep

	  This has the same effect as running the above commands with various build options pre-configured.  There are several build scripts available in the directory, select the one that best suits your needs.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Building the wsrep Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`build-mariadb-galera`:

The :term:`Galera Replication Plugin` implements the :term:`wsrep API` and operates as the wsrep Provider for the database server.  What it provides is a certification layer to prepare write-sets and perform certification checks, a replication layer and a group communication framework.  

To build the Galera Replication Plugin, ``cd`` into the ``galera/`` directory and run SCons.

.. code-block:: console

   # scons

This process creates the Galera Replication Pluigin, (that is, the ``libgalera_smm.so`` file).  In your ``my.cnf`` configuration file, you need to define the path to this file for the :ref:`wsrep_provider <wsrep_provider>` parameter.

.. note:: For FreeBSD users, building the Galera Replication Plugin from source raises certain issues due to Linux dependencies.  You can mitgate these by using the ports build available at ``/usr/ports/databases/galera`` or by installing the binary package:

	  .. code-block:: console

	     # pkg install galera
	  
--------------------------------
Post-installation Configuration
--------------------------------
.. _`installmariadb-postinstall`:

After the build completes, there are some additional steps that you must take in order to finish installing the database server on your system.  This is over and beyond the standard configuration process listed in :doc:`configuration` and :doc:`dbconfiguration`.

.. note:: Unless you defined the ``CMAKE_INSTALL_PREFIX`` configuration variable when you ran ``cmake`` above, by default the database is installed to the path ``/usr/local/mysql/``.  If you chose a custom path, adjust the commands below to accommodate the change.

#. Create the user and group for the database server.

   .. code-block:: console

      # groupadd mysql
      # useradd -g mysql mysql

#. Install the database.

   .. code-block:: console

      # cd /usr/local/mysql
      # ./scripts/mysql_install_db --user=mysql

   This installs the database in the working directory, (that is, at ``/usr/local/mysql/data``).  If you would like to install it elsewhere or run the script from a different directory, specify the desired paths with the ``--basedir`` and ``--datadir`` options.

#. Change the user and group permissions for the base directory.

   .. code-block:: console

      # chown -R mysql /usr/local/mysql
      # chgrp -R mysql /usr/local/mysql
      
#. Create a system unit for the database server.

   .. code-block:: console

      # cp /usr/local/mysql/supported-files/mysql.server \
            /etc/init.d/mysql
      # chmod +x /etc/init.d/mysql
      # chkconfig --add mysql

   This allows you to start Galera Cluster using the ``service`` command.  It also sets the database server to start during boot.


In addition to this procedure, bear in mind that any further customization variables you enabled during the build process, such as a nonstandard base or data directory, may require you to define additional parameters in the configuration file, (that is, ``my.cnf``).


.. note:: This tutorial omits MariaDB authentication options for brevity.

.. _GitHub: https://github.com
