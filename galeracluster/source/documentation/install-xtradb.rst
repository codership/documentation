.. meta::
   :title: Install XtraDB Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, xtradb, binaries, apt, yum
   :copyright: Codership Oy, 2014 - 2022. All Rights Reserved.


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

      Related Articles

      - :doc:`../training/tutorials/migration`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`install-xtradb-binary`:

============================================
Percona XtraDB Cluster - Binary Installation
============================================

Percona XtraDB Cluster is the Percona implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions through the Percona repository.


.. _`xtradb-repo`:
.. rst-class:: section-heading
.. rubric:: Enabling the Percona Repository

In order to install Percona XtraDB Cluster through your package manager, you need to first enable the Percona repository on your system.  There are two different ways to accomplish this, depending upon which Linux distribution you use.

.. _`xtradb-apt`:
.. rst-class:: sub-heading
.. rubric:: Enabling the ``apt`` Repository

For Debian and Debian-based Linux distributions, the procedure for adding the Percona repository requires that you first install Software Properties on your system.  The package names vary depending upon which distribution you use.  For Debian, in the terminal run the following command:

.. code-block:: console

   # apt-get install python-software-properties

For Ubuntu, instead run this command:

.. code-block:: console

   $ sudo apt-get install software-properties-common

In the event that you use a different Debian-based distribution and neither of these commands work, consult your distribution's package listings for the appropriate package name.

Once you have Software Properties installed, you can enable the Percona repository for your system.

#. Add the GnuPG key for the Percona repository:

   .. code-block:: console

      # add-key adv --recv-keys --keyserver \
            keyserver.ubuntu.com 1C4CBDCDCD2EFD2A

#. Add the Percona repository to your sources list:

   .. code-block:: console

      # add-apt-repository 'deb https://repo.percona.com/apt release main'

   For the repository address, make the following changes:

   - ``release`` Indicates the release name for the distribution you are using.  For example, ``wheezy``.

     In the event that you do not know which release you have installed on your server, you can find out using the following command:

     .. code-block:: console

	$ lsb_release -a

#. Update the local cache.

   .. code-block:: console

      # apt-get update

For more information on the repository, available packages and mirrors, see the `Percona apt Repository <https://www.percona.com/doc/percona-server/5.5/installation/apt_repo.html>`_

Packages in the Percona repository are now available for installation on your server through ``apt-get``.


.. _`xtradb-yum`:
.. rst-class:: sub-heading
.. rubric:: Enabling the ``yum`` Repository

For RPM-based distributions, you can enable the Percona repository through ``yum`` using the following command:

.. code-block:: console

   # yum install https://www.percona.com/downloads/percona-release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm

For more information on the repository, package names or available mirrors, see the `Percona yum Repository <https://www.percona.com/doc/percona-server/5.5/installation/yum_repo.html>`_.

Packages in the Percona repository are now available for installation on your server through ``yum``.


.. _`xtradb-galera-install`:
.. rst-class:: section-heading
.. rubric:: Installing Percona XtraDB Cluster

.. note::  Telemetry is enabled by default. To disable it, see `https://docs.percona.com/percona-xtradb-cluster/8.0/telemetry.html <https://docs.percona.com/percona-xtradb-cluster/8.0/telemetry.html>`_.

Percona provides generic tarballs with all required files and binaries for manual installation.

You can download the appropriate tarball package from `https://www.percona.com/downloads <https://www.percona.com/downloads>`_.

Starting with Percona XtraDB Cluster 8.0.20-11, the ``Linux - Generic`` section lists only full or minimal tar files. Each tarball file replaces the multiple tar file listing used in earlier versions and supports all distributions.

The version number in the tarball name must be substituted with the appropriate version number for your system. To indicate that such a substitution is needed in statements, we use ``<version-number>``.

.. csv-table::
   :class: doc-options tight-header
   :widths: 40, 20, 40

   Percona-XtraDB-Cluster_-Linux.x86_64.glibc2.17.tar.gz, Full, Contains binary files, libraries, test files, and debug symbols
   Percona-XtraDB-Cluster_-Linux.x86_64.glibc2.17.minimal.tar.gz, Minumum, Contains binary files and libraries but does not include test files, or debug symbols

For installations before Percona XtraDB Cluster 8.0.20-11, the ``Linux - Generic`` section contains multiple tarballs based on the operating system names:

   .. code-block:: console

      Percona-XtraDB-Cluster_8.0.18-9.3_Linux.x86_64.bionic.tar.gz
      Percona-XtraDB-Cluster_8.0.18-9.3_Linux.x86_64.buster.tar.gz
      ...

For example, you can use ``curl`` as follows:

   .. code-block:: console

      curl -O https://downloads.percona.com/downloads/Percona-XtraDB-Cluster-LATEST/Percona-XtraDB-Cluster-8.0.27/binary/tarball/Percona-XtraDB-Cluster_8.0.27-18.1_Linux.x86_64.glibc2.17-minimal.tar.gz


Check your system to make sure the packages that the PXC version requires are installed.

For most Debian-based distributions, you can install all of these through a single package.  In the terminal run the following command:

.. code-block:: console

   # sudo apt-get install -y \
         socat libdbd-mysql-perl \
         libaio1 libc6 libcurl3 libev4 libgcc1 libgcrypt20 \
         libgpg-error0 libssl1.1 libstdc++6 zlib1g libatomic1

For Ubuntu and distributions that derive from Ubuntu, however, you will need to specify the meta package.  In the terminal, run this command instead:

.. code-block:: console

   $ sudo apt-get install -y \
         socat libdbd-mysql-perl \
         libaio1 libc6 libcurl3 libev4 libgcc1 libgcrypt20 \
         libgpg-error0 libssl1.1 libstdc++6 zlib1g libatomic1
         percona-xtradb-cluster-galera


For RPM-based distributions, instead run this command:

.. code-block:: console

   # sudo yum install -y openssl socat  \
         procps-ng chkconfig procps-ng coreutils shadow-utils \

Percona XtraDB Cluster is now installed on your server.

.. note::  If you installed Percona XtraDB Cluster over an existing standalone instance of Percona XtraDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`../training/tutorials/migration`.

.. container:: bottom-links

   Related Articles

   - :doc:`../training/tutorials/migration`
