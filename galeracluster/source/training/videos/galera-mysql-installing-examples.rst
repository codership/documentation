.. meta::
   :title: Training Video Examples |---| Installing Galera Cluster with MySQL
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

        .. cssclass:: sub-links

           - :doc:`Troubleshooting <../../kb/trouble/index>`
           - :doc:`Best Practices <../../kb/best/index>`

        - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

        Related Documents

        - :doc:`Firewall Settings <../../documentation/firewall-settings>`
        - :doc:`firewalld <../../documentation/firewalld>`
        - :doc:`Installing Galera <../../documentation/install>`
        - :doc:`Node Provisioning <../../documentation/node-provisioning>`
        - :doc:`SELinux <../../documentation/selinux>`
        - :doc:`State Transfer <../../documentation/state-transfer>`
        - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

        Related Articles

        Other Resources

        - `Galera Repository <http://releases.galeracluster.com/>`_
        - `MariaDB Repo. Generator <https://downloads.mariadb.org/mariadb/repositories/>`_


.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article training-exercises
.. _`examples-galera-mysql-installing`:

==========================
Training Video Examples
==========================

---------------------------------------
Installing Galera Cluster with MySQL
---------------------------------------

.. container:: video-abstract list-col2-3

   These examples are part of the training video, *Installing Galera Cluster with MySQL*.  They correspond to what was taught, and should be done after each viewing section, unless otherwise noted.

   Before starting these exercises, make sure you have all of the requirements and preparations in place.

.. container:: list-col1-3

   .. rst-class:: training-video-resources
   .. rubric:: Requirements & Preparation

   .. rst-class:: training-video-resources

      - Test Servers:  3
      - Operating System:  Linux
      - Software:  Don’t install MariaDB or Galera Cluster in preparation.


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Exercises

Before starting an exercise, read it fully and carefully. The headings for each set of exercises corresponds to the section with the same name in training video.  Make notes for yourself as you go along, for when you have to do these tasks for your job or for yourself.


.. rst-class:: sub-heading
.. rubric:: Database Configuration (``/etc/my.cnf``)

Do these exercises after viewing the first two sections of the training video:  *Galera Cluster Overview*, and *Installing Software on Nodes*. Don’t configure the nodes until the next section.

.. code:: text

   # MySQL Options

   [mysqld]
   datadir=/var/lib/mysql
   socket=/var/lib/mysql/mysql.sock
   bind-address=0.0.0.0
   user=mysql

   default_storage_engine=InnoDB
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0
   innodb_buffer_pool_size=128M

   binlog_format=ROW
   symbolic-links=0

   log-error=/var/log/mysqld.log
   pid-file=/var/run/mysqld/mysqld.pid

   # Galera Optons

   wsrep_on=ON
   wsrep_provider=/usr/lib64/galera-3/libgalera_smm.so

   wsrep_node_name='galera-2'
   wsrep_node_address="172.31.23.129"

   wsrep_cluster_name='galera-training'
   wsrep_cluster_address="gcomm://172.31.18.216,172.31.23.129,172.31.25.198"
   wsrep_provider_options="gcache.size=300M; gcache.page_size=300M"
   wsrep_slave_threads=4
   wsrep_sst_method=rsync


.. rst-class:: sub-heading
.. rubric:: Configuring Nodes & Opening Ports

Do these exercises after viewing the section with the two titles. MariaDB should be down on each node; don’t start ``mysqld`` again until the next section.





.. note::

  If you struggled at any point in doing these exercises, especially in getting the Galera nodes started, you might want to do them again.  Start with fresh installations of the servers, without MariaDB or Galera Cluster.  If you use the same servers, before doing the exercises again, uninstall MariaDB and Galera, and delete MariaDB’s data directory.  Do the exercises multiple times, until you’re able to install, configure, and start a Galera cluster without any problems.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
