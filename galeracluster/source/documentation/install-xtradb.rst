.. meta::
   :title: Install XtraDB Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, xtradb, binaries, apt, yum
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      .. cssclass:: bull-head

         Related Articles

      - :doc:`../training/tutorials/migration`


.. cssclass:: library-document
.. _`install-xtradb-binary`:

============================================
Percona XtraDB Cluster - Binary Installation
============================================

Percona XtraDB Cluster is the Percona implementation of Galera Cluster for MySQL.  Binary installation packages are available for Debian- and RPM-based distributions through the Percona repository.


.. _`xtradb-repo`:
.. rst-class:: rubric-1
.. rubric:: Enabling the Percona Repository

In order to install Percona XtraDB Cluster through your package manager, you need to first enable the Percona repository on your system.  There are two different ways to accomplish this, depending upon which Linux distribution you use.

.. _`xtradb-apt`:
.. rst-class:: rubric-2
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
.. rst-class:: rubric-2
.. rubric:: Enabling the ``yum`` Repository

For RPM-based distributions, you can enable the Percona repository through ``yum`` using the following command:

.. code-block:: console

   # yum install https://www.percona.com/downloads/percona-release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm

For more information on the repository, package names or available mirrors, see the `Percona yum Repository <https://www.percona.com/doc/percona-server/5.5/installation/yum_repo.html>`_.

Packages in the Percona repository are now available for installation on your server through ``yum``.


.. _`xtradb-galera-install`:
.. rst-class:: rubric-1
.. rubric:: Installing Percona XtraDB Cluster

There are three packages involved in the installation of Percona XtraDB Cluster: the Percona XtraDB client, a command line tool for accessing the database; the percona XtraDB database server, built to include the :term:`wsrep API` patch and the :term:`Galera Replication Plugin`.

For most Debian-based distributions, you can install all of these through a single package.  In the terminal run the following command:

.. code-block:: console

   # apt-get install percona-xtradb-cluster

For Ubuntu and distributions that derive from Ubuntu, however, you will need to specify the meta package.  In the terminal, run this command instead:

.. code-block:: console

   $ sudo apt-get install percona-xtradb-cluster
         percona-xtradb-cluster-galera


For RPM-based distributions, instead run this command:

.. code-block:: console

   # yum install Percona-XtraDB-Cluster

Percona XtraDB Cluster is now installed on your server.

.. note::  If you installed Percona XtraDB Cluster over an existing standalone instance of Percona XtraDB, there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`../training/tutorials/migration`.
