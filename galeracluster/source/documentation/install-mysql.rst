.. meta::
   :title: Install MySQL Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, mysql, binaries, apt, yum
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

      - :doc:`Install Galera <./install>`
      - :doc:`Galera MySQL Source <./install-mysql-src>`
      - :ref:`MySQL Shared Compatibility Libraries <centos-mysql-shared-compt>`
      - :doc:`Galera MariaDB Binaries <./install-mariadb>`

      Related Articles

      - :doc:`../training/tutorials/migration`

      Other Resources

      - :doc:`Galera AWS (video)  <../../training/videos/galera-aws-installing>`
      - :doc:`Galera MySQL (video)  <../../training/videos/galera-mysql-installing>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`install-mysql-binary`:

===================================================
Galera Cluster for MySQL |---| Binary Installation
===================================================

Galera Cluster for MySQL may be installed on Linux servers using binary packages. These files can be downloaded directly from the Codership repository, or by way of a package manager: ``apt-get`` or ``yum``.

   .. only:: html

          .. image:: ../images/training.jpg
             :target: https://galeracluster.com/training-courses/
             :width: 740

   .. only:: latex

          .. image:: ../images/training.jpg
		  :target: https://galeracluster.com/training-courses/

.. _`mysql-repo`:
.. rst-class:: section-heading
.. rubric:: Enabling the Codership Repository

To install Galera Cluster for MySQL with a package manager, you first will have to enable the Codership repository on the server. There are a few ways to do this, depending on which Linux distribution and package manager you use. The sections below provide details on how to use each of the three main supported package managers to install Galera Cluster for MySQL.


.. _`mysql-deb`:
.. rst-class:: sub-heading
.. rubric:: Enabling the ``apt`` Repository

For Debian and Debian-based Linux distributions, the procedure for adding a repository requires that you first install the *Software Properties*. The package names vary depending on the distribution. For Debian, at the command-line, execute the following command:

.. code-block:: console

   apt-get install python-software-properties

For Ubuntu or a distribution derived from Ubuntu, you would execute instead the following:

.. code-block:: console

   apt-get install software-properties-common

If your server uses a different Debian-based distribution, and neither of these commands work on your system, try consulting your distribution's package listings for the appropriate package name.

Once you have the *Software Properties* installed, you can then enable the Codership repository for your system. Start by adding the GnuPG key for the repository. This is done by executing the following from the command-line:

.. code-block:: console

   apt-key adv --keyserver keyserver.ubuntu.com --recv 8DA84635

.. note::

   For packages before MySQL 5.7.44 and 8.0.35, the signing key is BC19DDBA. Next, add the Codership repository to your sources list. Using a simple text editor, create file called, `galera.list` in the ``/etc/apt/sources.list.d/`` directory. Add these lines to that file, with the necessary adjustments for the version used:

.. code-block:: linux-config

   # Codership Repository (Galera Cluster for MySQL)
   deb https://releases.galeracluster.com/mysql-wsrep-VERSION/DIST RELEASE main
   deb https://releases.galeracluster.com/galera-3/DIST RELEASE main

In the example above, you would change the repository addresses. The ``VERSION`` should be set to MySQL-wsrep version you want to install. For example, it might be something like, ``8.4``. The ``DIST`` should be replaced with the name of the Linux distribution on the server. This could be ``ubuntu``. Last, replace ``RELEASE`` with the distribution release (for example, ``wheezy``).

If you do not know which release you have installed on your server, you can generally find this using the following command:

.. code-block:: console

	 lsb_release -a

Version 4 of Galera was recently released. If you'd like to install it, the configuration lines in `galera.list` should read similar to the following:

.. code-block:: linux-config

   # Codership Repository (Galera Cluster for MySQL)
   deb https://releases.galeracluster.com/galera-4/ubuntu focal main
   deb https://releases.galeracluster.com/mysql-wsrep-8.0/ubuntu focal main

Again, you may have to adust the version and release numbers, depending on which you want to install. Please note that this will require at least version 18.04 of Ubuntu.

To be assured the proper version is installed and updated, set which repository you prefer to the Codership repository (this is not only recommended, it is required). To do this, using a text editor, create a file called, `galera.pref` in the ``/etc/apt/preferences.d/`` directory. The contents should look like the following:

.. code-block:: linux-config

   # Prefer Codership repository
   Package: *
   Pin: origin releases.galeracluster.com
   Pin-Priority: 1001

This is needed to make sure the patched versions are preferred. This might be important, for instance, if a third-party program requires ``libmysqlclient20`` and the OS-version for the library is newer.

Finally, you should update the local cache of the repository. Do this by entering the following from the command-line:

.. code-block:: console

   apt-get update

Once you've done all of these tasks, the packages in the Codership repository will be available for installation. For information on installing them using ``apt-get``, skip ahead on this page to the section entitled, :ref:`Installing Galera Cluster for MySQL <mysql-install>`.



.. _`mysql-yum-repo`:
.. rst-class:: sub-heading
.. rubric:: Enabling the ``yum`` Repository

For rpm-based distributions of Linux (for example, CentOS and Red Hat Enterprise Linux), you will need to enable the Codership repository. Using a simple text editor, create a file called, ``galera.repo`` in the ``/etc/yum.repos.d/`` directory. The contents of that file should look something like the following:

.. code-block:: ini

   [galera]
   name = Galera
   baseurl = https://releases.galeracluster.com/galera-3/DIST/RELEASE/ARCH
   gpgkey = https://releases.galeracluster.com/GPG-KEY-galeracluster.com
   gpgcheck = 1

   [mysql-wsrep]
   name = MySQL-wsrep
   baseurl =  https://releases.galeracluster.com/mysql-wsrep-VERSION/DIST/RELEASE/ARCH
   gpgkey = https://releases.galeracluster.com/GPG-KEY-galeracluster.com
   gpgcheck = 1


In this sample repository configuration file, you would change the repository addresses for the ``baseurl``. The ``VERSION`` should be set to the whichever MySQL-wsrep version you want (for example, it might be ``8.0``). The ``DIST`` should be changed to the name of the Linux distribution you are using on your server (for example, ``redhat``). The ``RELEASE`` should be replaced with the distribution's release number. It might be ``8`` or ``9`` for CentOS and Red Hat Enterprise Linux. Last, the ``ARCH`` indicates the architecture of your hardware. This could be changed to ``x86_64`` for 64-bit systems.

Here is a sample repository configuration file for Red Hat 9 and Galera Cluster with MySQL 8.

.. code-block:: ini

	[galera4]
	name = Galera
	baseurl = https://releases.galeracluster.com/galera-4/redhat/9/x86_64
	gpgkey = https://releases.galeracluster.com/GPG-KEY-galeracluster.com
	gpgcheck = 1

	[mysql-wsrep8]
	name = MySQL-wsrep
	baseurl = https://releases.galeracluster.com/mysql-wsrep-8.0/redhat/9/x86_64
	gpgkey = https://releases.galeracluster.com/GPG-KEY-galeracluster.com
	gpgcheck = 1


After you've created, modified, and saved this repository file, you will be able to install the packages from the Codership repository using ``yum``. For an explanation on installing, skip ahead on this page to the section entitled, :ref:`Installing Galera Cluster for MySQL <mysql-install>`.


.. _`mysql-install`:
.. rst-class:: section-heading
.. rubric:: Installing Galera Cluster for MySQL

There are two packages involved in the installation of Galera Cluster for MySQL: the MySQL database server, but one that has been built to include the :term:`wsrep API`; and the :term:`Galera Replication Plugin`. The ``yum`` repositories include Galera Arbitrator with the Galera Replication Plugin, but for Debian-based distributions using ``apt-get`` you will need to include add it to your installation instruction.

.. note:: If SELinux (Security-Enhanced Linux) is enabled on the servers, disable it. See :ref:`Disabling SELinux for mysqld <disable-selinux>`. Also, if AppArmor is enabled on the servers, disable it. See :ref:`Disabling AppArmor <disable-apparmor>`. However, this is optional, and there are methods to enable the context files.

So, for Debian-based distributions using the ``apt-get`` package manager, execute the following from the command-line:

For Galera Cluster 8.0:

.. code-block:: console

   apt-get install galera-4 galera-arbitrator-4 mysql-wsrep-8.0

For Galera Cluster 8.4:

.. code-block:: console

   apt-get install galera-4 galera-arbitrator-4 mysql-wsrep-8.4

On servers using the ``yum`` package manager (that is, Red Hat Enterprise Linux and CentOS distributions), you would instead execute this command:

.. code-block:: console

   yum install galera-4 mysql-wsrep-8.4

For ``mysql-wsrep-8.0``:

.. code-block:: console

   yum install galera-4 mysql-wsrep-8.0

.. note:: On Red Hat 9, this command may generate a transaction check error. For more information on that error and how to resolve it, see the section below on :ref:`MySQL Shared Compatibility Libraries <centos-mysql-shared-compt>`.

Please note that on Red Hat 8, you need to disable MySQL and
MariaDB modules before installing Galera Cluster from a repository under
https://releases.galeracluster.com/. In order to do this, execute the
following from the command-line:

.. code-block:: console

   dnf module disable mysql mariadb

Once you've executed the line appropriate to your distribution and package manager, Galera Cluster for MySQL should be installed on your server. You will then have to repeat this process for each node in your cluster, including enabling the repository files mentioned earlier.

Incidentally, when deciding which packages from the Codership repository to install, the package manager may elect to install a newer major verion of Galera Cluster, newer than the one you intended to install. Before confirming the installation of packages, make sure that the package manager is planning to install the Galera Cluster version you want.

If you installed Galera Cluster for MySQL over an existing stand-alone instance of MySQL, there are some additional steps that you will need to take to update your system to the new database server. For more information, see :doc:`../training/tutorials/migration`.


.. _`centos-mysql-shared-compt`:
.. rst-class:: section-heading
.. rubric:: MySQL Shared Compatibility Libraries

When installing Galera Cluster for MySQL on CentOS 8 or 9, you may encounter a transaction check-error that blocks the installation. The error message may look something like this:

.. code-block:: text

   Transaction Check Error:
   file /usr/share/mysql/czech/errmsg.sys from install
   mysql-wsrep-server-5.6-5.6.23-25.10.e16.x86_64 conflicts
   with file from package mysql-libs-5.1.73-.3.e16_5.x86_64

This relates to a dependency problem between the version of the MySQL shared compatibility libraries that CentOS uses, and the one that Galera Cluster requires. To resolve this, you will have to upgrade, which can be done with the Codership repository using ``yum``.

There are two versions available for this package. Which version you will need will depend on which version of the MySQL wsrep database server you want to install.

For CentOS, you would enter something like the following from the command-line:

.. code-block:: console

   yum upgrade -y mysql-wsrep-libs-compat-VERSION

You would, of course, replace ``VERSION`` here with ``8.0`` or ``8.1``, depending on the version of MySQL you want to use. For CentOS 8 or 9, to install MySQL version 8.0, you would execute the following from the command-line:

.. code-block:: console

   yum upgrade mysql-wsrep-shared-8.0

For CentOS 8 or 9, to install MySQL version 8.0, you will also need to disable the 8.0 upgrade. To do this, enter the following from the command-line:

.. code-block:: console

   yum upgrade -y mysql-wsrep-shared-8.0 -x mysql-wsrep-shared-8.0

When ``yum`` finishes the upgrade, you can then install the MySQL wsrep database server and the Galera Replication Plugin as described above.

.. container:: bottom-links

   Related Documents

   - :doc:`Install Galera <./install>`
   - :doc:`Galera MySQL Source <./install-mysql-src>`
   - :ref:`MySQL Shared Compatibility Libraries <centos-mysql-shared-compt>`
   - :doc:`Galera MariaDB Binaries <./install-mariadb>`

   Related Articles

   - :doc:`../training/tutorials/migration`

   Other Resources

   - :doc:`Galera AWS (video)  <../../training/videos/galera-aws-installing>`
   - :doc:`Galera MySQL (video)  <../../training/videos/galera-mysql-installing>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
