=====================
Binary Installation
=====================
.. _`galera-mysql-binary-install`:

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
      deb http://releases.galeracluster.com/DIST RELEASE main

   For the repository address, make the following changes:

   - ``DIST`` Indicates the name of your Linux distribution.  For example, ``ubuntu``.

   - ``RELEASE`` Indicates your distribution release.  For example, ``wheezy``.

     In the event that you do not know which release you have installed on your server, you can find out using the following command:

     .. code-block:: console

	$ lsb_release -a

#. Update the local cache.

   .. code-block:: console

      # apt-get update

Packages in the Codership repository are now available for installation through ``apt-get``.



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``yum`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-yum-repo`:


For RPM-based distributions, such as CentOS, Red Hat and Fedora, you can enable the Codership repository by adding a ``.repo`` file to the ``/etc/yum.repos.d/`` directory.

Using your preferred text editor, create the ``.repo`` file.

.. code-block:: ini

   [galera]
   name = Galera
   baseurl = http://releases.galeracluster.com/DIST/RELEASE/ARCH
   gpgkey = http://releases.galeracluster.com/GPG-KEY-galeracluster.com
   gpgcheck = 1

In the ``baseurl`` field, make the following changes to web address:

- ``DIST`` Indicates the distribution name.  For example, ``centos`` or ``fedora``.

- ``RELEASE`` indicates the distribution release number.  For example, ``6`` for CentOS, ``20`` or ``21`` for Fedora.

- ``ARCH`` indicates the architecture of your hardware.  For example, ``x86_64`` for 64-bit systems.

Packages in the Codership repository are now available for installation through ``yum``.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling the ``zypper`` Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`mysql-zypper-repo`:

For distributions that use ``zypper`` for package management, such as openSUSE and SUSE Linux Enterprise Server, you can enable the Codership repository by importing the GPG key and then creating a ``.repo`` file in the local directory.

#. Import the GPG key.

   .. code-block:: console

      $ sudo rpm --import "http://releases.galeracluster.com/GPG-KEY-galeracluster.com"

#. Create a ``galera.repo`` file in the local directory.

   .. code-block:: ini

      [galera]
      name = Galera
      baseurl = http://releases.galeracluster.com/DIST/RELEASE

   For the ``baseurl`` repository address, make the following changes:

   - ``DIST`` indicates the distribution name.  For example, ``opensuse`` or ``sles``.

   - ``RELEASE`` indicates the distribution version number.
 
#. Add the Codership repository.

   .. code-block:: console

      $ sudo zypper addrepo galera.repo

#. Refresh ``zypper``.

   .. code-block:: console

      $ sudo zypper refresh
      
Packages in the Codership repository are now available for installation through ``zypper``.



--------------------------------
Installing Galera Cluster
--------------------------------
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

For openSUSE and SUSE Linux Enterprise Server, run this command:

.. code-block:: console

   # zypper install galera-3 \
		mysql-wsrep-5.6
		
Galera Cluster for MySQL is now installed on your server.  You need to repeat this process for each node in your cluster.

.. seealso:: In the event that you installed Galera Cluster for MySQL over an existing standalone instance of MySQL, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.


