.. meta::
   :title: Install Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, installation, install, mysql, mariadb, xtradb
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

      Related Articles

      - :doc:`Install Galera <../../training/tutorials/galera-installation>`
      - :doc:`Install Galera on AWS <../../training/tutorials/galera-on-aws>`

      Other Resources

      - :doc:`Galera AWS (video)  <../../training/videos/galera-aws-installing>`
      - :doc:`Galera MariaDB (video)  <../../training/videos/galera-mariadb-installing>`
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
.. _`install-galera`:

=============================
Installing Galera Cluster
=============================

Galera Cluster is essentially used to form a cluster among multiple database servers.  It's widely used in conjunction with MySQL, MariaDB, and XtraDB database software systems.  Galera Cluster is integral to these database systems.  As a result, it may be installed together with one of them.

There are several methods available for installing the paired systems: you may use binary installation packages or install with the source files. Below is a list of the various pairs and links to how to use whichever method your prefer:

.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Installing MySQL Galera Cluster

MySQL the company and the database software was purchased quite a while ago by Oracle.  They continue to support MySQL software and cooperate with Codership to deliver an excellent database cluster system.

.. rst-class:: sub-heading
.. rubric:: :doc:`MySQL Binary Installation <./install-mysql>`

Click on the heading here to read this article on how to install MySQL using a binary installation package. Binary installation packages are available for Linux distributions using ``apt-get``, ``yum`` and ``zypper`` package managers through the Codership repository.

.. rst-class:: sub-heading
.. rubric:: :doc:`MySQL Source Installation <./install-mysql-src>`

If you're using a Linux distribution for which we don't have binary files that work with its package management system, or if your server uses a different unix-like operating system (e.g., Solaris or FreeBSD), you will need to build Galera Cluster for MySQL from source files.


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Installing MariaDB Galera Cluster

MariaDB the company and the database software is somewhat of a spinoff or fork of MySQL.  The software is basically the same as MySQL; Some people who worked formerly at MySQL, founded MariaDB several years ago.  Because of all of this, MariaDB software works well with Galera.  In fact, starting with version 10.4 of MariaDB, Galera is included.  Before that version, you'll have to use one our binary installation packages or install from the source files.

.. rst-class:: sub-heading
.. rubric:: :doc:`MariaDB Binary Installation <./install-mariadb>`

This article provides information on how to install MariaDB using a binary installation package. They're available for Debian-based and RPM-based distributions of Linux, from the `MariaDB Repository Generator <https://downloads.mariadb.org/mariadb/repositories/>`_.

.. rst-class:: sub-heading
.. rubric:: :doc:`MariaDB Source Installation <./install-mariadb-src>`

If there aren't a binary installation packages that are suited to the distribution of Linux your servers are using, or you're using a different unix-like operating system (e.g., Solaris or FreeBSD), you'll have to build MariaDB Galera Cluster from the source files.

.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Installing XtraDB Galera Cluster

Many years before MariaDB was formed and several years before MySQL was bought by Oracle, some key personnel at MySQL, who specialized in performance tuning MySQL software, left to form Percona |---| the name is an amalgamation of the words, *Performance* and *Consulting*.  In their efforts to get the most out of MySQL software, they developed their own fork with some extra performance enhancements, called XtraDB.  It also works well with Galera Cluster.

.. rst-class:: sub-heading
.. rubric:: :doc:`XtraDB Binary Installation <./install-xtradb>`

Binary packages for installing XtraDB with Galera Cluster are available for Debian-based and RPM-based distributions, but through the Percona repository.  This article explains how to install and configure this pairing of software, as well as provides links to the repository.

.. rst-class:: sub-heading
.. rubric:: :doc:`XtraDB Source Installation <./install-xtradb-src>`

You may not be able to use one of the binary installation packages available because of your operating system. If so, you'll have to use our source files. Actually, you may want to use the source files to make minor changes that will become part of the files you'll build.


.. container:: bottom-links

   Related Articles

   - :doc:`Install Galera <../../training/tutorials/galera-installation>`
   - :doc:`Install Galera on AWS <../../training/tutorials/galera-on-aws>`

   Other Resources

   - :doc:`Galera AWS (video)  <../../training/videos/galera-aws-installing>`
   - :doc:`Galera MariaDB (video)  <../../training/videos/galera-mariadb-installing>`
   - :doc:`Galera MySQL (video)  <../../training/videos/galera-mysql-installing>`


.. toctree::
   :hidden:
   :maxdepth: 3

   install-mysql
   install-mysql-src
   install-mariadb
   install-mariadb-src
   install-xtradb
   install-xtradb-src


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
