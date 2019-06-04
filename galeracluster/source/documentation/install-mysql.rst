==============================================
Galera Cluster for MySQL - Binary Installation
==============================================
.. _`install-mysql-binary`:

Galera Cluster for MySQL is the reference implementation from Codership Oy.  Binary installation packages are available for Linux distributions using ``apt-get``, ``yum`` and ``zypper`` package managers through the Codership repository.

----------------------------------
Enabling the Codership repository
----------------------------------
.. _`mysql-repo`:

In order to install Galera Cluster for MySQL through your package manager, you need to first enable the Codership repository on your system.  There are different ways to accomplish this, depending on which Linux distribution and package manager you use.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``apt`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-deb`:

For Debian and Debian-based Linux distributions, the procedure for adding a repository requires that you first install the Software Properties.  The package names vary depending on your distribution.  For Debian, in the terminal run the following command:

.. code-block:: console

   # apt-get install python-software-properties

For Ubuntu or a distribution that derives from Ubuntu, instead run this command:

.. code-block:: console

   $ sudo apt-get install software-properties-common

In the event that you use a different Debian-based distribution and neither of these commands work, consult your distribution's package listings for the appropriate package name.

Once you have the Software Properties installed, you can enable the Codership repository for your system.

#. Add the GnuPG key for the Codership repository.

   .. code-block:: console

      # apt-key adv --keyserver keyserver.ubuntu.com \
            --recv BC19DDBA

#. Add the Codership repository to your sources list.  Using your preferred text editor, create a `galera.list` file in the ``/etc/apt/sources.list.d/`` directory.

   .. code-block:: linux-config

      # Codership Repository (Galera Cluster for MySQL)
      deb http://releases.galeracluster.com/mysql-wsrep-VERSION/DIST RELEASE main
      deb http://releases.galeracluster.com/galera-3/DIST RELEASE main

   For the repository address, make the following changes:

   - ``VERSION`` Indicates the desired MySQL-wsrep version. For example, ``5.6``

   - ``DIST`` Indicates the name of your Linux distribution.  For example, ``ubuntu``.

   - ``RELEASE`` Indicates your distribution release.  For example, ``wheezy``.

     In the event that you do not know which release you have installed on your server, you can find out using the following command:

     .. code-block:: console

	$ lsb_release -a

#. Prefer the Codership repository over other sources. Using your preferred text editor, create a `galera.pref` file in the ``/etc/apt/preferences.d/`` directory.

   .. code-block:: linux-config

      # Prefer Codership repository
      Package: *
      Pin: origin releases.galeracluster.com
      Pin-Priority: 1001

   This is needed to make sure the patched versions are preferred, for example if a 3rd-party program requires ``libmysqlclient20`` and the OS-Version for the library is newer.

#. Update the local cache.

   .. code-block:: console

      # apt-get update

Packages in the Codership repository are now available for installation through ``apt-get``.



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``yum`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-yum-repo`:


For RPM-based distributions, such as CentOS, Red Hat and Fedora, you can enable the Codership repository by adding a ``galera.repo`` file to the ``/etc/yum.repos.d/`` directory.

Using your preferred text editor, create the ``galera.repo`` file.

.. code-block:: ini

   [galera]
   name = Galera
   baseurl = http://releases.galeracluster.com/galera-3/DIST/RELEASE/ARCH
   gpgkey = http://releases.galeracluster.com/GPG-KEY-galeracluster.com
   gpgcheck = 1

   [mysql-wsrep]
   name = MySQL-wsrep
   baseurl =  http://releases.galeracluster.com/mysql-wsrep-VERSION/DIST/RELEASE/ARCH
   gpgkey = http://releases.galeracluster.com/GPG-KEY-galeracluster.com
   gpgcheck = 1


In the ``baseurl`` field, make the following changes to web address:

- ``VERSION`` Indicates the desired MySQL-wsrep version. For example, ``5.6``

- ``DIST`` Indicates the distribution name.  For example, ``centos`` or ``fedora``.

- ``RELEASE`` indicates the distribution release number.  For example, ``6`` for CentOS, ``20`` or ``21`` for Fedora.

- ``ARCH`` indicates the architecture of your hardware.  For example, ``x86_64`` for 64-bit systems.

Packages in the Codership repository are now available for installation through ``yum``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``zypper`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-zypper-repo`:

For distributions that use ``zypper`` for package management, such as openSUSE and SUSE Linux Enterprise Server, you can enable the Codership repository by importing the GPG key and then creating a ``galera.repo`` file in the local directory.

#. Import the GPG key.

   .. code-block:: console

      $ sudo rpm --import "http://releases.galeracluster.com/GPG-KEY-galeracluster.com"

#. Create a ``galera.repo`` file in the local directory.

   .. code-block:: ini

      [galera]
      name = Galera
      baseurl = http://releases.galeracluster.com/galera-3/DIST/RELEASE/ARCH

      [MySQL-wsrep]
      name = MySQL-wsrep
      baseurl = http://releases.galeracluster.com/mysql-wsrep-VERSION/DIST/RELEASE/ARCH

   For the ``baseurl`` repository address, make the following changes:

   - ``VERSION`` Indicates the desired MySQL-wsrep version. For example, ``5.6``

   - ``DIST`` indicates the distribution name.  For example, ``opensuse`` or ``sles``.

   - ``RELEASE`` indicates the distribution version number.

   - ``ARCH`` indicates the architecture of your hardware.  For example, ``x86_64`` for 64-bit systems.


#. Add the Codership repository.

   .. code-block:: console

      $ sudo zypper addrepo galera.repo

#. Refresh ``zypper``.

   .. code-block:: console

      $ sudo zypper refresh

Packages in the Codership repository are now available for installation through ``zypper``.



-----------------------------------
Installing Galera Cluster for MySQL
-----------------------------------
.. _`mysql-install`:


There are two packages involved in the installation of Galera Cluster for MySQL: the MySQL database server, built to include the :term:`wsrep API`; and the :term:`Galera Replication Plugin`.

.. note:: For Debian-based distributions, you also need to include a third package, :term:`Galera Arbitrator`.  This is only necessary with ``apt-get``.  The ``yum`` and ``zypper`` repositories package Galera Arbitrator with the Galera Replication Plugin.

For Debian-based distributions, run the following command:

.. code-block:: console

   # apt-get install galera-3 \
		galera-arbitrator-3 \
		mysql-wsrep-5.6

For Red Hat, Fedora and CentOS distributions, instead run this command:

.. code-block:: console

   # yum install galera-3 \
		mysql-wsrep-5.6


.. note:: On CentOS 6 and 7, this command may generate a transaction check error. For more information on this error and how to fix it, see :ref:`MySQL Shared Compatibility Libraries <centos-mysql-shared-compt>`.

For openSUSE and SUSE Linux Enterprise Server, run this command:

.. code-block:: console

   # zypper install galera-3 \
		mysql-wsrep-5.6

Galera Cluster for MySQL is now installed on your server.  You need to repeat this process for each node in your cluster.

.. note:: When deciding which packages to install, the package manager may elect to install a newer major verion of Galera Cluster than the one you intended to install. Before confirming the installation of packages, please make sure that the package manager intends to install the desired Galera Cluster version.

.. note:: In the event that you installed Galera Cluster for MySQL over an existing standalone instance of MySQL, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
MySQL Shared Compatibility Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`centos-mysql-shared-compt`:

When installing Galera Cluster for MySQL on CentOS, versions 6 and 7, you may encounter a transaction check error that blocks the installation.

.. code-block:: text

   Transaction Check Error:
   file /usr/share/mysql/czech/errmsg.sys from install
   mysql-wsrep-server-5.6-5.6.23-25.10.e16.x86_64 conflicts
   with file from package mysql-libs-5.1.73-.3.e16_5.x86_64

This relates to a dependency issue between the version of the MySQL shared compatibility libraries that CentOS uses and the one that Galera Cluster requires.  Upgrades are available through the Codership repository and you can install them with ``yum``.

There are two versions available for this package.  The version that you need depends on which version of the MySQL wsrep database server that you want to install.  Additionally, the package names themselves vary depending on the version of CentOS.

For CentOS 6, run the following command:

.. code-block:: console

   # yum upgrade -y mysql-wsrep-libs-compat-VERSION

Replace ``VERSION`` with ``5.5`` or ``5.6``, depending upon the version of MySQL you want to use.  For CentOS 7, to install MySQL version 5.6, run the following command:

.. code-block:: console

   # yum upgrade mysql-wsrep-shared-5.6

For CentOS 7, to install MySQL version 5.5, you also need to disable the 5.6 upgrade:

.. code-block:: console

   # yum upgrade -y mysql-wsrep-shared-5.5 \
         -x mysql-wsrep-shared-5.6

When ``yum`` finishes the upgrade, install the MySQL wsrep database server and the Galera Replication Plugin as described above.
