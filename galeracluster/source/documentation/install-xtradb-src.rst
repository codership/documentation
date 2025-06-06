.. meta::
   :title: Install XtraDB Cluster Source
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, xtradb, source
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

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
.. _`install-xtradb-src`:

============================================
Percona XtraDB Cluster - Source Installation
============================================

Percona XtraDB Cluster is the Percona implementation of Galera Cluster for MySQL. Binary installation packages are available for Debian- and RPM-based distributions of Linux. If your Linux distribution is based on a different package management system or if it runs on a different unix-like operating system where binary installation packages are unavailable, such as Solaris or FreeBSD, you will need to build Percona XtraDB Cluster from source.


.. note:: In the event that you built Percona XtraDB Cluster over an existing standalone instance of Percona XtraDB, there are some additional steps that you need to take in order to update your system to the new database server. For more information, see :doc:`../training/tutorials/migration`.


.. _`installxtradb-prep-server`:
.. rst-class:: section-heading
.. rubric:: Preparing the Server

When building from source code, ``make`` cannot manage or install dependencies necessary for either Galera Cluster itself or the build process. You need to install these packages first.

- For Debian-based distributions of Linux, if Percona is available in your repositories, you can run the following command:

  .. code-block:: console

     # apt-get build-dep percona-xtradb-cluster

- For RPM-based distributions, instead run this command:

  .. code-block:: console

     # yum-builddep percona-xtradb-cluster

In the event that neither command works for your system or that you use a different Linux distribution or FreeBSD (FreeBSD is available up to Galera Cluster for MySQL 5.7), the following packages are required:

- **Percona XtraDB Database Server with wsrep API**: Git, CMake, GCC and GCC-C++, Automake, Autoconf, and Bison, as well as development releases of libaio and ncurses.

- **Galera Replication Plugin**: SCons, as well as development releases of Boost, Check and OpenSSL.

Check with the repositories for your distribution or system for the appropriate package names to use during installation. Bear in mind that different systems may use different names and that some may require additional packages to run. For instance, to run CMake on Fedora you need both ``cmake`` and ``cmake-fedora``.


.. _`build-percona-xtradb`:
.. rst-class:: section-heading
.. rubric:: Building Percona XtraDB Cluster

The source code for Percona XtraDB Cluster is available through GitHub_. Using Git you can download the source to build both Percona XtraDB Cluster and the Galera Replication Plugin locally on your system.

#. Clone the Percona XtraDB Cluster database server.

   .. code-block:: console

      # git clone https://github.com/percona/percona-xtradb-cluster.git

#. Checkout the 8.0 branch and initialize submodules:

   .. code-block:: console

      # cd percona-xtradb-cluster
      # git checkout 8.0
      # git submodule update --init --recursive


You now have the source files for the Percona XtraDB Cluster database server, set to the branch of development that you want to build.

Download the matching Percona XtraBackup 8.0 tarball (*.tar.gz) for your operating system from `Percona Downloads <https://www.percona.com/downloads>`_. The following example extracts the Percona XtraBackup 8.0.32-25 tar.gz file to the target directory ``./pxc-build``:

   .. code-block:: console

      ```{.bash data-prompt="$"}
      # tar -xvf percona-xtrabackup-8.0.32-25-Linux-x86_64.glibc2.17.tar.gz -C ./pxc-build
      ```

Run the build script ``./build-ps/build-binary.sh``. By default, it attempts building into the current directory. Specify the target output directory, such as ``./pxc-build``:

   .. code-block:: console

      # mkdir ./pxc-build
      # ./build-ps/build-binary.sh ./pxc-build

When the compilation completes, pxc-build contains a tarball, such as ``Percona-XtraDB-Cluster-8.0.x86_64.tar.gz``, that you can deploy on your system.

In addition to the database server, you also need the wsrep Provider, also known as the Galera Replication Plugin. In a separate directory, run the following command:

.. code-block:: console

   # cd ..
   # git clone https://github.com/codership/galera.git

Once Git finishes downloading the source file,s you can start building the database server and the Galera Replication Plugin. You now have the source file for the database server in a ``percona-xtradb-cluster/`` and the Galera source files in ``galera/``.

.. _`build-percona`:
.. rst-class:: sub-heading
.. rubric:: Building the Database Server

The database server for Galera Cluster is the same as that of the standard database servers for  standalone instances of Percona XtraDB, with the addition of a patch for the wsrep API, which is packaged in the version downloaded from GitHub_. You can enable the patch through  the wsrep API, requires that you enable it through the ``WITH_WSREP`` and ``WITH_INNODB_DISALLOW_WRITES`` CMake configuration options.

To build the database server, ``cd`` into the ``percona-xtradb-cluster`` directory and run the following commands:

.. code-block:: console

   # cmake -DWITH_WSREP=ON -DWITH_INNDOB_DISALLOW_WRITES=ON ./
   # make
   # make install

.. note:: In addition to compiling through ``cmake`` and ``make``, there are also a number of build scripts available in the ``BUILD/`` directory, which you may find more convenient to use. For example:

	  .. code-block:: console

	     # ./BUILD/compile-pentium64

	  This has the same effect as running the above commands with various build options pre-configured. There are several build scripts available in the ``BUILD/`` directory. Select the one that best suits your nees.


.. _`build-percona-galera`:
.. rst-class:: sub-heading
.. rubric:: Building the wsrep Provider

The :term:`Galera Replication Plugin` implements the :term:`wsrep API` and operates as the wsrep Provider for the database server. What it provides is a certification layer to prepare write-sets and perform certification checks, a replication layer and a group communication framework.

To build the Galera Replication Plugin, ``cd`` into the ``galera/`` directory and run SCons.

.. code-block:: console

   # scons

This process creates the Galera Replication Plugin, (that is, the ``libgalera_smm.so`` file). In your ``my.cnf`` configuration file, you need to define the path to this file for the :ref:`wsrep_provider <wsrep_provider>` parameter.

.. note:: For FreeBSD users, building the Galera Replication Plugin from sources raises certain Linux compatibility issues. You can mitigate these by using the ports build available at ``/usr/ports/databases/galera`` or by install the binary package:

	  .. code-block:: console

	     # pkg install galera


.. _`installxtradb-postinstall`:
.. rst-class:: section-heading
.. rubric:: Post-installation Configuration

After the build completes, there are some additional steps that you must take in order to finish installing the database server on your system. This is over and beyond the standard configuration process listed in :doc:`System Configuration <../training/tutorials/configuration>` and :doc:`Replication Configuration <../training/tutorials/wsrep-configuration>`.

.. note:: Unless you defined the ``CMAKE_INSTALL_PREFIX`` configuration varaible when you ran ``cmake`` above, by default the database is installed to the path ``/usr/local/mysql/``. If you chose a custom path, adjust the commands below to accommodate this change.


#. Create the user and group for the database server.

   .. code-block:: console

      # groupadd mysql
      # useradd -g mysql mysql

#. Install the database.

   .. code-block:: console

      # cd /usr/local/mysql
      # ./scripts/mysql_install_db --user=mysql

   This installs the database in the working directory, (that is, at ``/usr/local/mysql/data``). If you would like to install it elsewhere or run the script from a different directory, specify the desired paths with the ``--basedir`` and ``--datadir`` options.

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

   This allows you to start Galera Cluster using the ``service`` command. It also sets the database server to start during boot.


In addition to this procedure, bear in mind that any further customization variables that you enabled during the build process through ``cmake``, (such as nonstandard base or data directories), may require you to define addition parameters in the configuration file, (that is, the ``my.cnf``).

.. _GitHub: https://github.com


.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_provider <wsrep_provider>`

   Related Articles

   - :doc:`../training/tutorials/migration`
   - :doc:`System Configuration <../training/tutorials/configuration>`
   - :doc:`Replication Configuration <../training/tutorials/wsrep-configuration>`
