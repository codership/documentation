.. meta::
   :title: Making Back-Ups with Galera Cluster
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

        - :doc:`Galera Arbitrator <../../documentation/arbitrator>`
        - :doc:`Node Recovery <../../documentation/recovery>`
        - :doc:`Scriptable SST  <../../documentation/scriptable-sst>`
        - :doc:`State Transfer <../../documentation/state-transfer>`
        - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

        Related Articles

        - :doc:`Galera Back-Ups <../tutorials/galera-backup>`

        Other Resources

        - `mysqldump <https://mariadb.com/kb/en/mariadb/mysqldump/>`_
        - `Slave Options <https://dev.mysql.com/doc/refman/en/replication-options-slave.html>`_
        - `Std Replication with Galera <https://mariadb.com/kb/en/library/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica/>`_
        - `Types of Back-Ups <https://dev.mysql.com/doc/mysql-backup-excerpt/en/backup-types.html>`_
        - `CHANGE MASTER <https://dev.mysql.com/doc/refman/en/change-master-to.html>`_
        - `SHOW MASTER STATUS <https://dev.mysql.com/doc/refman/en/show-master-status.html>`_
        - `SHOW SLAVE STATUS <https://dev.mysql.com/doc/refman/en/show-slave-status.html>`_

.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article library-video
.. _`video-galera-backup`:

=====================================
Making Back-Ups with Galera Cluster
=====================================

.. container:: video-abstract list-col2-3

   A primary responsibility of a database administrator, a DBA, is to make back-ups |---| or to ensure they are made properly and regularly.  It's a key part of ensuring high availability of data. While the average DBA may know well how to perform this essentential administrative task on stand-alone database servers, most aren't so sure how best to do so when the database server is part of a Galera Cluster.

   This training video explains in detail how to make back-ups of MySQL and MariaDB databases within a Galera Cluster.  It presents in stages, different methods for removing or pausing a node to make a proper back-up.  Additionally, it presents methods for restoring back-ups |---| recovering single nodes and an entire cluster.

   As part of the training process, in the right margin here, you can find a link to a page containing exercises related to the training video.  You should look at it before starting the video so that you can be prepared.  There's also a link to a PDF copy of the slide presentation. It's been set so that you make notes on it.  In the left margin are links to related documentation, articles, and other materials.

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Russell J.T. Dyer
      - Date: October 25, 2019
      - Length of Video: 1 hour, 5 minutes

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Training Exercises <galera-backup-exercises>`
      - `Slide Presentation </library-media/pdf/galera-backup.pdf>`_


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Outline of Training Video

.. container:: list-col1

   **1. Back-Up Basics** :raw-html:`<small>(time index: 3:30)</small>` |br| Covers the basic concepts, reasons and goals in making back-ups of databases.

   **2. Using Standard Replication** :raw-html:`<small>(time index: 16:23)</small>` |br| Presents how to use standard MySQL or MariaDB replication to attach a slave to a Galera node, with it acting as master. With this arrangement, it's easy to stop the slave and regularly make back-ups.

   **3. Using Galera Arbitrator** :raw-html:`<small>(time index: 27:31)</small>` |br| Galera Arbitrator may be used to desynchronize a node and then initiate a back-up script on that node.  When it's finished, it will resynchronize the node.

.. container:: list-col2

   **4. Restoring Nodes** :raw-html:`<small>(time index: 42:31)</small>` |br| Explains how to recover nodes and a cluster by various methods, including using back-up files to restore the data and start an entire cluster.

   **5. Back-Up & Restoration Plan** :raw-html:`<small>(time index: 59:14)</small>` |br| Provides some sound advice on developing a back-up and restoration plan for Galera nodes.

.. raw:: html

   <video width="820" height="547" preload="metadata" controls>
   <source src="https://galeracluster.com/library-media/videos/galera-backup.mp4#t=0.5" type="video/mp4">
   </video>

.. toctree::
   :maxdepth: 2
   :hidden:

   galera-backup-exercises

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
