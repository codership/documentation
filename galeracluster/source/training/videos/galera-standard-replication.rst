.. meta::
   :title: Standard Replication & Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Training Courses <../courses/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

      - :doc:`FAQ <../../faq>`

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

      Related Articles

      - :doc:`Starting Galera <../tutorials/starting-cluster>`

      Other Resources

      - `MariaDB Replication <https://mariadb.com/kb/en/library/high-availability-performance-tuning-mariadb-replication/>`_
      - `MySQL Replication <https://dev.mysql.com/doc/refman/en/replication.html>`_

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article library-video
.. _`video-galera-standard-replication`:

=======================================
Standard Replication & Galera Cluster
=======================================

.. container:: video-abstract list-col2-3

   This training video introduces standard MySQL and MariaDB replication.  It explains and demonstrates how to configure two services |---| one master and one slave |---| for replication.  It also contrasts replication against Galera Cluster; it talks about the advantages of Galera over standard replication. The video also explains and demonstrates how to configure three servers for Galera cluster.

   As part of the training process, in the right margin here, you can find a link to a page containing exercises related to the training video.  You should look at it before starting the video so that you can be prepared.  There's also a link to a PDF copy of the slide presentation. It's been set so that you make notes on it.  In the left margin are links to related documentation, articles, and other materials.

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Russell J.T. Dyer
      - Date: October 15, 2019
      - Length of Video: 54 minutes

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Training Exercises <galera-standard-replication-exercises>`
      - `Slide Presentation </library-media/pdf/galera-standard-replication.pdf>`_


.. container:: banner

   .. rst-class:: section-heading
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
    <source src="https://galeracluster.com/library-media/videos/galera-standard-replication.mp4#t=0.1" type="video/mp4">
    </video>

.. container:: bottom-links

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

   Related Articles

   - :doc:`Starting Galera <../tutorials/starting-cluster>`

   Other Resources

   - `MariaDB Replication <https://mariadb.com/kb/en/library/high-availability-performance-tuning-mariadb-replication/>`_
   - `MySQL Replication <https://dev.mysql.com/doc/refman/en/replication.html>`_


.. toctree::
   :maxdepth: 2
   :hidden:

   galera-standard-replication-exercises

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
