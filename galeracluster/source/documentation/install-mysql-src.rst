.. meta::
   :title: Install MySQL Galera Cluster Source
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, mysql, source
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`Install Galera <./install>`
      - :doc:`Galera MySQL Binaries <./install-mysql>`
      - :doc:`Galera MariaDB Source <./install-mariadb-src>`
      - :ref:`wsrep_provider <wsrep_provider>`

      Related Articles

      - :doc:`../training/tutorials/migration`
      - :doc:`System Configuration <../training/tutorials/configuration>`
      - :doc:`Replication Configuration <../training/tutorials/wsrep-configuration>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`install-mysql-src`:

==============================================
Galera Cluster for MySQL - Source Installation
==============================================

Galera Cluster for MySQL is the reference implementation from Codership Oy.  Binary installation packages are available for Debian- and RPM-based distributions of Linux.  If your Linux distribution is based upon a different package management system, if your server uses a different unix-like operating system, such as Solaris or FreeBSD, you will need to build Galera Cluster for MySQL from source.


.. note:: If you built Galera Cluster for MySQL over an existing standalone instance of MySQL, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`../training/tutorials/migration`.


.. _`mysql-build-dep`:
.. rst-class:: section-heading
.. rubric:: Installing Build Dependencies

When building from source code, ``make`` cannot manage or install dependencies for either Galera Cluster or the build process itself.  You need to install these first.  For Debian-based systems, run the following command:

.. code-block:: console

   # apt-get build-dep mysql-server

For RPM-based distributions, instead run this command:

.. code-block:: console

   # yum-builddep MySQL-server


If neither command works on your system or that you use a different Linux distribution or FreeBSD, the following packages are required:

- **MySQL Database Server with wsrep API**: Git, CMake, GCC and GCC-C++, Automake, Autoconf, and Bison, as well as development releases of libaio and ncurses.

- **Galera Replication Plugin**: SCons, as well as development releases of Boost, Check and OpenSSL.

Check with the repositories for your distribution or system for the appropriate package names to use during installation.  Bear in mind that different systems may use different names and that some may require additional packages to run.  For instance, to run CMake on Fedora you need both ``cmake`` and ``cmake-fedora``.


.. _`build-galera-mysql`:
.. rst-class:: section-heading
.. rubric:: Building Galera Cluster for MySQL

The source code for Galera Cluster for MySQL is available through GitHub_.  You can download the source code from the website or directly using ``git``.  In order to build Galera Cluster, you need to download both the database server with the wsrep API patch and the :term:`Galera Replication Plugin`.

To download the database server, complete the following steps:

#. Clone the Galera Cluster for MySQL database server source code.

   .. code-block:: console

      # git clone https://github.com/codership/mysql-wsrep

#. Checkout the branch for the version that you want to use.

   .. code-block:: console

      # git checkout 5.6

   The main branches available for Galera Cluster for MySQL are:

   - ``5.6``
   - ``5.5``


You now have the source files for the MySQL database server, including the wsrep API patch needed for it to function as a Galera Cluster node.

In addition to the database server, you need the wsrep Provider, also known as the Galera Replication Plugin.  In a separator directory, run the following command:

.. code-block:: console

   # cd ..
   # git clone https://github.com/codership/galera.git

Once Git finishes downloading the source files, you can start building the database server and the Galera Replication Plugin.  The above procedures created two directories: ``mysql-wsrep/`` for the database server source and for the Galera source ``galera/``


.. _`build-mysql`:
.. rst-class:: sub-heading
.. rubric:: Building the Database Server

The database server for Galera Cluster is the same as that of the standard database servers for  standalone instances of MySQL, with the addition of a patch for the wsrep API, which is packaged in the version downloaded from GitHub_.  You can enable the patch through  the wsrep API, requires that you enable it through the ``WITH_WSREP`` and ``WITH_INNODB_DISALLOW_WRITES`` CMake configuration options.

To build the database server, ``cd`` into the ``mysql-wsrep/`` directory and run the following commands:

.. code-block:: console

   # cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON ./
   # make
   # make install


.. _`build-mysql-galera`:
.. rst-class:: sub-heading
.. rubric:: Building the wsrep Provider

The :term:`Galera Replication Plugin` implements the :term:`wsrep API` and operates as the wsrep Provider for the database server.  What it provides is a certification layer to prepare write-sets and perform certification checks, a replication layer and a group communication framework.

To build the Galera Replicator plugin, ``cd`` into the ``galera/`` directory and run SCons:

.. code-block:: console

   # scons

This process creates the Galera Replication Plugin, (that is, the ``libgalera_smm.so`` file).  In your ``my.cnf`` configuration file, you need to define the path to this file for the :ref:`wsrep_provider <wsrep_provider>` parameter.

.. note:: For FreeBSD users, building the Galera Replicator Plugin from source raises certain Linux compatibility issues.  You can mitigate these by using the ports build at ``/usr/ports/databases/galera``.


.. _`installmysql-postinstall`:
.. rst-class:: section-heading
.. rubric:: Post-installation Configuration

After the build completes, there are some additional steps that you must take in order to finish installing the database server on your system.  This is over and beyond the standard configurations listed in :doc:`System Configuration <../training/tutorials/configuration>` and :doc:`Replication Configuration <../training/tutorials/wsrep-configuration>`.

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
.. _GitHub: https://github.com


.. container:: bottom-links

   Related Documents

   - :doc:`Install Galera <./install>`
   - :doc:`Galera MySQL Binaries <./install-mysql>`
   - :doc:`Galera MariaDB Source <./install-mariadb-src>`
   - :ref:`wsrep_provider <wsrep_provider>`

   Related Articles

   - :doc:`../training/tutorials/migration`
   - :doc:`System Configuration <../training/tutorials/configuration>`
   - :doc:`Replication Configuration <../training/tutorials/wsrep-configuration>`
