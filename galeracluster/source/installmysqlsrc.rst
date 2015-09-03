=========================================
Source Installation
=========================================
.. _`MySQL Source Installation`:

Galera Cluster for MySQL is the reference implementation from Codership Oy.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  In the event that your Linux distribution is based upon a different package management system, if your server uses a different unix-like operating system, such as Solaris or FreeBSD, you will need to build Galera Cluster for MySQL from source.


.. seealso:: In the event that you built Galera Cluster for MySQL over an existing standalone instance of MySQL, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.



------------------------------
Installing Build Dependencies
------------------------------
.. _`mysql-build-dep`:

When building from source code, ``make`` cannot manage or install dependencies for either Galera Cluster or the build process itself.  You need to install these first.  For Debian-based systems, run the following command:

.. code-block:: console

   # apt-get build-dep mysql-server

For RPM-based distributions, instead run this command:

.. code-block:: console

   # yum-builddep MySQL-server

In the event that neither command works on your system or that you use a different Linux distribution or FreeBSD, the following packages are required:

- **MySQL Database Server with wsrep API**: Git, CMake, GCC and GCC-C++, Automake, Autoconf, and Bison, as well as development releases of libaio and ncurses.

- **Galera Replication Plugin**: SCons, as well as development releases of Boost, Check and OpenSSL.

.. note:: Different systems may use different names for these packages or additional build dependencies.  Check with the package repositories for your system.


	  
--------------------------------------------
Building Galera Cluster for MySQL
--------------------------------------------
.. `build-galera-mysql`:

The source code for Galera Cluster for MySQL is available through `GitHub <https://github.com/codership/>`_.  You can download the source code using Git.  You need the MySQL database server with the wsrep API patch and the Galera Replicator Plugin.

.. code-block:: console

   $ git clone https://github.com/codership/mysql-wsrep.git
   $ git clone https://github.com/codership/galera.git

Once Git finishes downloading the source files, you can start building the database server and Galera Replicator plugin.  The ``git`` commands create directories for each at ``mysql-wsrep/`` and ``galera/``.

To build the database server, run the following commands from the ``mysql-wsrep/`` directory:

.. code-block:: console

   # cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON ./
   # make
   # make install

.. note:: In addition to compiling through ``cmake`` and ``make``, there are also a number of build scripts in the ``BUILD/`` directory, which you may find more convenient to use.  For example, 

	  .. code-block:: console

	     # ./BUILD/compile-pentium64-max

	  This has the same effect as running the above commands with various build options pre-configured.  There are several build scripts available in the directory, select the one that best suits your needs.

To build the Galera Replicator plugin, run the following command from the ``galera/`` directory:

.. code-block:: console

   # scons

This process creates the wsrep Provider, (that is, the ``libgalera_smm.so`` file).  In your configuration file, you need to define the path to this file for the :ref:`wsrep_provider <wsrep_provider>` parameter.

.. note:: For FreeBSD users, building the Galera Replicator Plugin from source raises certain issues due to Linux dependencies.  You can mitigate these by using the ports build at ``/usr/ports/databases/galera``.



----------------------------------
Post-installation Configuration
----------------------------------
.. _`installmysql-postinstall`:

After the build completes, there are some additional steps that you must take in order to finish installing the database server on your system.  This is over and beyond the standard configurations listed in :doc:`configuration` and :doc:`dbconfiguration`.

.. note:: Unless you defined the ``CMAKE_INSTALL_PREFIX`` configuration variable when you ran ``cmake`` above, by default the database server installed to the path ``/usr/local/mysql/``.  If you chose a custom path, adjust the commands below to accommodate the change.

#. Create the user and group for the database server.

   .. code-block:: console

      # groupadd mysql
      # useradd -g mysql mysql

	  
#. Install the database.

   .. code-block:: console

      # cd /usr/local/mysql
      # ./scripts/mysql_install_db --user=mysql

   This installs the database in the working directory.  That is, at ``/usr/local/mysql/data/``.  If you would like to install it elsewhere or run it from a different directory, specify the desired path with the ``--basedir`` and ``--datadir`` options.

#. Change the user and group for the directory.

   .. code-block:: console

      # chown -R mysql /usr/local/mysql
      # chgrp -R mysql /usr/local/mysql

#. Create a system unit.

   .. code-block:: console

      # cp /usr/local/mysql/supported-files/mysql.server \
            /etc/init.d/mysql
      # chmod +x /etc/init.d/mysql
      # chkconfig --add mysql

   This allows you to start Galera Cluster using the ``service`` command.  It also sets the database server to start during boot.

In addition to this procedure, bear in mind that any custom variables you enabled during the build process, such as a nonstandard base or data directory, requires that you add parameters to cover this in the configuration file, (that is, ``my.cnf``).

      
.. note:: This tutorial omits MySQL authentication options for brevity.



