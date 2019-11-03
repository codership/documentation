.. meta::
   :title: Installing Galera Cluster with MySQL
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

         - :doc:`Firewall Settings <../../documentation/firewall-settings>`
         - :doc:`firewalld <../../documentation/firewalld>`
         - :doc:`Installing Galera <../../documentation/install>`
         - :doc:`Node Provisioning <../../documentation/node-provisioning>`
         - :doc:`SELinux <../../documentation/selinux>`
         - :doc:`State Transfer <../../documentation/state-transfer>`
         - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

      .. cssclass:: bull-head

         Related Articles

      .. cssclass:: bull-head

         Other Resources

         - `Galera Repository <http://releases.galeracluster.com/>`_

.. role:: raw-html(raw)
   :format: html

.. cssclass:: tutorial-article video-article
.. _`video-galera-mysql-installing`:

=====================================
Installing Galera Cluster with MySQL
=====================================

.. container:: video-abstract list-col2-3

   This training video explains how to use install MySQL and Galera Cluster software on a server, on three servers, and to use those servers as nodes of a Galera Cluster. It shows how to download and install the software, as well as how to configure MySQL and Galera on each node. The video ends by showing the steps to start a cluster, and some tips on resolving problems when first starting a cluster.

   As part of the training process, in the right margin here, you can find a link to a page containing exercises related to the training video.  You should look at it before starting the video so that you can be prepared.  There's also a link to a PDF copy of the slide presentation. It's been set so that you make notes on it.  In the left margin are links to related documentation, articles, and other materials.

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Russell J.T. Dyer
      - Date: September 24, 2019
      - Length of Video: 32 minutes

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Training Exercises <galera-mysql-installing-exercises>`
      - `Slide Presentation </library-media/pdf/galera-mysql-installing.pdf>`_
      - :doc:`Example Configuration <galera-mysql-installing-examples>`
      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_


.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Outline of Training Video

.. container:: list-col1

   **1. Galera Cluster Overview** :raw-html:`<small>(time index: 2:17)</small>` |br| Briefly discusses Galera Cluster in general.

   **2. Installing Software on Nodes** :raw-html:`<small>(time index: 8:51)</small>` |br| Explains and demonstrates how to install the needed software on three servers.

   **3. Configuring Nodes** :raw-html:`<small>(time index: 18:03)</small>` |br| Covers the minimum required for configuring the nodes.


.. container:: list-col2

   **4. Opening Ports** :raw-html:`<small>(time index: 22:16)</small>` |br| Setting security to allow Galera traffic through specific ports.

   **5. Starting Galera** :raw-html:`<small>(time index: 24:57)</small>` |br| Starting and testing a Galera cluster |---| and some resolving common beginner problems.

.. raw:: html

    <video width="820" height="547" preload="metadata" controls>
    <source src="https://galeracluster.com/library-media/videos/galera-mysql-installing.mp4#t=0.5" type="video/mp4">
    </video>


.. toctree::
   :maxdepth: 2
   :hidden:

   galera-mysql-installing-exercises
   galera-mysql-installing-examples

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
