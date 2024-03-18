.. meta::
   :title: Install XtraDB Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, xtradb, binaries, apt, yum
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


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

For more information on the repository, available packages and mirrors, see `Percona Software Repositories Documentation <https://docs.percona.com/percona-software-repositories/index.html>`_.

Packages in the Percona repository are now available for installation on your server through ``apt-get``.


.. _`xtradb-yum`:
.. rst-class:: sub-heading
.. rubric:: Enabling the ``yum`` Repository

For RPM-based distributions, you can enable the Percona repository through ``yum`` using the following command:

.. code-block:: console

   # yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm

For more information on the repository, package names or available mirrors, see `Percona Software Repositories Documentation <https://docs.percona.com/percona-software-repositories/index.html>`_.

Packages in the Percona repository are now available for installation on your server through ``yum``.


.. _`xtradb-galera-install`:
.. rst-class:: section-heading
.. rubric:: Installing Percona XtraDB Cluster

There are three packages involved in the installation of Percona XtraDB Cluster: the Percona XtraDB client, a command line tool for accessing the database; the percona XtraDB database server, built to include the :term:`wsrep API` patch and the :term:`Galera Replication Plugin`.

For Debian and Ubuntu-based distributions, run the following commands in the terminal:

.. code-block:: console

   # apt-get update
   # apt-get install -y wget gnupg2 lsb-release curl
   # wget https://repo.percona.com/apt/percona-release_latest.generic_all.deb
   # dpkg -i percona-release_latest.generic_all.deb
   # apt-get update
   # percona-release setup pxc80
   # apt-get install -y percona-xtradb-cluster


For RPM-based distributions, instead run this command:

.. code-block:: console

   # yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
   # percona-release setup pxc-80
   # yum install percona-xtradb-cluster

Percona XtraDB Cluster is now installed on your server.

.. note::  If you installed Percona XtraDB Cluster over an existing standalone instance of Percona XtraDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`../training/tutorials/migration`.

.. container:: bottom-links

   Related Articles

   - :doc:`../training/tutorials/migration`
