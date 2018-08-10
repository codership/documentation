============================================
MariaDB Galera Cluster - Binary Installation
============================================
.. _`galera-mariadb-binarys-install`:

MariaDB Galera Cluster is the MariaDB implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions of Linux through the MariaDB repository.

---------------------------------
Enabling the MariaDB Repository
---------------------------------
.. _`mariadb-repo`:

In order to install MariaDB Galera Cluster through your package manager, you need to first enable the MariaDB repository on your system.  There are two different ways to accomplish this, depending on which Linux distribution you use.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``apt`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mariadb-deb`:

For Debian and Debian-based Linux distributions, the procedure for adding a repository requires that you first install the Software Properties.  The package names vary depending on your distribution.  For Debian, in the terminal run the following command:

.. code-block:: console

   # apt-get install python-software-properties

For Ubuntu or a distribution that derives from Ubuntu, instead run this command:

.. code-block:: console

   $ sudo apt-get install software-properties-common

In the event that you use a different Debian-based distribution and neither of these commands work, consult your distribution's package listings for the appropriate package name.

Once you have the Software Properties installed, you can enable the MariaDB repository for your system.

#. Add the GnuPG key for the MariaDB repository.

   .. code-block:: console

      # apt-key adv --recv-keys --keyserver \
            keyserver.ubuntu.com 0xcbcb082a1bb943db

#. Add the MariaDB repository to your sources list.


   .. code-block:: console

      # add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/version/distro release main'

   For the repository address, make the following changes:

   - ``version`` Indicates the version number of MariaDB that you want to use.  For example, ``5.6``.

   - ``distro`` Indicates the name of your Linux distribution.  For example, ``ubuntu``.

   - ``release`` Indicates your distribution release.  For example, ``wheezy``.

     In the event that you do not know which release you have installed on your server, you can find out using the following command:

     .. code-block:: console

	$ lsb_release -a

#. Update the local cache.

   .. code-block:: console

      # apt-get update


For more information on the repository, package names or available mirrors, see the `MariaDB Repository Generator <https://downloads.mariadb.org/mariadb/repositories/>`_.

Packages in the MariaDB repository are now available for installation through ``apt-get``.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``yum`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mariadb-rpm`:

For RPM-based distributions, such as CentOS, Red Hat and Fedora, you can enable the MariaDB repository by adding a ``.repo`` file to the ``/etc/yum/repos.d/`` directory.

Using your preferred text editor, create the ``.repo`` file.

.. code-block:: ini

   # vim /etc/yum/repos.d/MariaDB.repo

   [mariadb]
   name = MariaDB
   baseurl = http://yum.mariadb.org/version/package
   gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
   gpgcheck = 1

In the ``baseurl`` field, make the following changes to web address:

- ``version`` Indicates the version of MariaDB you want to use.  For example, ``5.6``.

- ``package`` indicates the package name for your distribution, release and architecture.  For example, ``rhel6-amd64`` would reference packages for a Red Hat Enterprise Linux 6 server running on 64-bit hardware.

For more information on the repository, package names or available mirrors, see the `MariaDB Repository Generator <https://downloads.mariadb.org/mariadb/repositories/>`_.

---------------------------------
Installing MariaDB Galera Cluster
---------------------------------
.. _`mariadb-install`:

There are three packages involved in the installation of MariaDB Galera Cluster: the MariaDB database client, a command line tool for accessing the database; the MariaDB database server, built to include the :term:`wsrep API` patch; and the :term:`Galera Replication Plugin`.

For Debian-based distributions, in the terminal run the following command:

.. code-block:: console

   # apt-get install mariadb-client \
         mariadb-galera-server \
	 galera

For RPM-based distributions, instead run this command:

.. code-block:: console

   # yum install MariaDB-client \
         MariaDB-Galera-server \
	 galera

MariaDB Galera Cluster is now installed on your server.  You will need to repeat this process for each node in your cluster.

.. note:: **See Also**: In the event that you installed MariaDB Galera Cluster over an existing standalone instance of MariaDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.
