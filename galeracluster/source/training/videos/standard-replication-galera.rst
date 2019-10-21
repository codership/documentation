.. meta::
   :title: Standard Replication & Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../../kb/trouble/index>`
         - :doc:`Best Practices <../../kb/best/index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../tutorials/index>`
         - :doc:`Training Videos <./index>`

      .. cssclass:: bull-head

         Related Documents

         - `Binary Log <https://dev.mysql.com/doc/refman/en/binary-log.html>`_
         - `CHANGE MASTER <https://dev.mysql.com/doc/refman/5.5/en/change-master-to.html>`_
         - :doc:`Firewall Settings <../../documentation/firewall-settings>`
         - :doc:`firewalld <../../documentation/firewalld>`
         - :doc:`Load Balancer <../../documentation/glb>`
         - `Master Configuration <https://dev.mysql.com/doc/refman/en/replication-howto-masterbaseconfig.html>`_
         - :doc:`Node Provisioning <../../documentation/node-provisioning>`
         - `Replication Threads <https://dev.mysql.com/doc/refman/en/replication-implementation-details.html>`_
         - :doc:`SELinux <../../documentation/selinux>`
         - `SHOW MASTER STATUS <https://dev.mysql.com/doc/refman/8.0/en/show-master-status.html>`_
         - `SHOW SLAVE STATUS <https://dev.mysql.com/doc/refman/8.0/en/show-slave-status.html>`_
         - `Slave Options <https://dev.mysql.com/doc/refman/en/replication-options-slave.html>`_
         - :doc:`State Transfer <../../documentation/state-transfer>`
         - :doc:`wsrep Options <../tutorials/wsrep-configuration>`
         - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

      .. cssclass:: bull-head

         Related Articles

         - :doc:`Starting Galera <../tutorials/starting-cluster>`

      .. cssclass:: bull-head

         Other Resources

         - `MariaDB Replication <https://mariadb.com/kb/en/library/high-availability-performance-tuning-mariadb-replication/>`_
         - `MySQL Replication <https://dev.mysql.com/doc/refman/en/replication.html>`_



.. role:: raw-html(raw)
   :format: html

.. cssclass:: tutorial-article video-article
.. _`video-standard-replication-galera-cluster`:

=======================================
Standard Replication & Galera Cluster
=======================================

.. rst-class:: video-stats

   Speaker: Russell J.T. Dyer; Date: October 15, 2019; Length of Video: 54 minutes

This training video introduces standard MySQL and MariaDB replication.  It explains and demonstrates how to configure two services |---| one master and one slave |---| for replication.  It also contrasts replication against Galera Cluster; it talks about the advantages of Galera over standard replication.  Then explains and demonstrates how to configure three servers for Galera cluster.


.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Outline of Training Video

.. container:: list-col1

   .. rubric:: Standard Replication

   **1. Purpose & Advantages** :raw-html:`<small>(time index: 3:10)</small>` |br| The values, the point of using replication and clusters of servers.

   **2. Standard Replication Layout** :raw-html:`<small>(time index: 8:39)</small>` |br| An introduction to standard MySQL or MariaDB replication.

   **3. Configuring Replication** :raw-html:`<small>(time index: 17:12)</small>` |br| The steps for configuring MySQL and MariaDB software for use in standard replication.


.. container:: list-col2

   .. rubric:: Galera Cluster

   **4. Galera Basics** :raw-html:`<small>(time index: 34:49)</small>` |br| The basics — concepts and some important terms.

   **5. Configuring Galera** :raw-html:`<small>(time index: 39:29)</small>` |br| Explanation and demonstration on configuring servers for Galera.

   **6. Deploying a Cluster** :raw-html:`<small>(time index: 43:47)</small>` |br| Starting and testing a minimum three-node cluster.


.. raw:: html

    <video width="820" height="547" preload="metadata" controls>
    <source src="https://galeracluster.com/library-media/videos/galera-vs-standard-replication.mp4#t=0.1" type="video/mp4">
    </video>



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
