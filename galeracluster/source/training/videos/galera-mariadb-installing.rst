.. meta::
   :title: Installing Galera Cluster with MariaDB
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
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

      - :doc:`FAQ <../../faq>`

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

      - `MariaDB Repo. Generator <https://downloads.mariadb.org/mariadb/repositories/>`_
      - `Galera Repository <http://releases.galeracluster.com/>`_

.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article library-video
.. _`video-galera-mariadb-installing`:

=======================================
Installing Galera Cluster with MariaDB
=======================================

.. container:: video-abstract list-col2-3

   This training video explains how to use install MariaDB and Galera Cluster software on a server, on three servers, and to use those servers as nodes of a Galera Cluster. It shows how to download and install the software, as well as how to configure MariaDB and Galera on each node. The video ends by showing the steps to start a cluster, and some tips on resolving problems when first starting a cluster.

   As part of the training process, in the right margin here, you can find a link to a page containing exercises related to the training video.  You should look at it before starting the video so that you can be prepared.  There's also a link to a PDF copy of the slide presentation. It's been set so that you make notes on it.  In the left margin are links to related documentation, articles, and other materials.

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Russell J.T. Dyer
      - Date: September 27, 2019
      - Length of Video: 30 minutes

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Training Exercises <galera-mariadb-installing-exercises>`
      - `Slide Presentation </library-media/pdf/galera-mariadb-installing.pdf>`_
      - :doc:`Example Configuration <galera-mariadb-installing-examples>`
      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Outline of Training Video

.. container:: list-col1

   **1. Galera Cluster Overview** :raw-html:`<small>(time index: 2:24)</small>` |br| Briefly discusses Galera Cluster in general.

   **2. Installing Software** :raw-html:`<small>(time index: 9:02)</small>` |br| Explains and demonstrates how to install the needed software on three servers.

   **3. Configuring Nodes** :raw-html:`<small>(time index: 16:34)</small>` |br| Covers the minimum required for configuring the nodes.


.. container:: list-col2

   **4. Opening Ports** :raw-html:`<small>(time index: 20:54)</small>` |br| Setting security to allow Galera traffic through specific ports.

   **5. Starting Galera** :raw-html:`<small>(time index: 23:20)</small>` |br| Starting and testing a Galera cluster |---| and some resolving common beginner problems.


.. raw:: html

    <video width="820" height="547" preload="metadata" controls>
    <source src="https://galeracluster.com/library-media/videos/galera-mariadb-installing.mp4#t=0.5" type="video/mp4">
    </video>

.. toctree::
   :maxdepth: 2
   :hidden:

   galera-mariadb-installing-exercises
   galera-mariadb-installing-examples

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
