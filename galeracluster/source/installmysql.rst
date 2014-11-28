============================
Binary Installation
============================
.. _`galera-mysql-binary-install`:

Galera Cluster for MySQL is the reference implementation from Codership.  Debian and RPM binary packages are available for download from Launchpad.net.  

------------------------------
Installing Dependencies
------------------------------
.. _`galera-mysql-dependencies`:

At this time, there is no repository available for installing and updating Galera Cluster for MySQL through your package manager.  As such, you will need to download and install the required dependencies separately.  There are three that you will need: the PSmsic utilities package, the MySQL client and from Oracle the MySQL Shared Compatibility libraries.

If you have an existing installation of MySQL, you will need to remove it.  For Debian-based distributions, in the terminal run the following command:

.. code-block:: console

   # apt-get remove mysql-server \
         mysql-server-core

For RPM-based distributions, instead run this command:

.. code-block:: console

   # rpm --nodeps --allmatches -e \
         MySQL-server \
         MySQL-test \
         MySQL-bench

To install the Galera Cluster dependencies, complete the following steps:

#. Install the PSmsic and MySQL client packages.  For Debian-based distributions, in the terminal run the following command:

   .. code-block:: console

      # apt-get install psmisc \
            mysql-client

   For RPM-based distributions, instead use this command:

   .. code-block:: console

      # yum install psmisc \
            MySQL

#. Go to the `Oracle MySQL Community <http://dev.mysql.com/downloads/mysql>`_ download page, and download the relevant binary package for the MySQL Shared Compatibility libraries.

#. Install the MySQL Shared Compatibility libraries.  For Debian-based distributions, run the following command:

   .. code-block:: console

      # dpkg --install mysql-shared-compat-*.deb

   For RPM-based distributions, instead use this command:

   .. code-block:: console

      # rpm -i MySQL-shared-compat-*.rpm

Once this process is complete, you are ready to begin installing Galera Cluster.


------------------------------------
Installing Galera Cluster
------------------------------------
.. _`mysql-install`:

There are two binary packages that make up Galera Cluster.  The first is the MySQL database server, which has been built to include the needed wsrep API patch.  The second is the Galera Replication plugin.

To install Galera Cluster for MySQL, complete the following steps:

#. In your browser, go to `MySQL Patches by Codership <https://launchpad.net/codership-mysql/+download>`_, and download the relevant database server package for your system and architecture.

#. Install the MySQL database server package.  For Debian-based distributions, in the terminal run the following command:

   .. code-block:: console

      # dpkg --install mysql-server-wsrep-*.deb

   For RPM-based distributions, instead use this command:

   .. code-block:: console

      # rpm -i MySQL-server-wsrep-*.rpm

#. In your browser, go to `Galera Replicator <https://launchpad.net/galera>`_ and download the Galera Replication plugin package for your system and architecture.

#. Install the Galera Replication plugin.  For Debian-based distributions, in the terminal run the following command:

   .. code-block:: console
		   
      # dpkg --install galera-*.deb

   For RPM-based distributions, instead use this command:

   .. code-block:: console

      # rpm -i galera-*.rpm

#. Using a text editor, add to your configuration file the path to the Galera Replicator plugin.  For instance:

   .. code-block:: ini

      # vim /etc/my.cnf
      
      wsrep_provider = /usr/lib/galera/libgalera_smm.so

Galera Cluster for MySQL is now installed on your system.


^^^^^^^^^^^^^^^^^^^^^^^^^
Upgrading System Tables
^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-system-tables`:

If you installed Galera Cluster over an existing installation of MySQL, you will need to also upgrade the system tables from standalone MySQL to Galera Cluster.  To do so, in the terminal run the following command:

.. code-block:: console

   $ mysql_upgrade

If this command generates any errors, check the MySQL Reference Manual for more information related to the error messages.  The errors it generates are typically not critical and you can usually ignore them, unless they relate to specific functionality that your system requires.



