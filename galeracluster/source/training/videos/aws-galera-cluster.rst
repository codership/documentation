.. meta::
   :title: Installing a Galera Cluster on AWS
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
         - `MariaDB Repository <https://downloads.mariadb.org/mariadb/repositories/>`_



.. role:: raw-html(raw)
   :format: html

.. cssclass:: tutorial-article video-article
.. _`video-aws-galera-cluster`:

====================================
Installing a Galera Cluster on AWS
====================================

.. rst-class:: video-stats

   Speaker: Russell J.T. Dyer; Date: July 12, 2019; Length of Video: 52 minutes

This training video explains how to use Amazon Web Services (AWS) to create virtual servers to be used as a Galera Cluster. It will explain how to create and configure AWS, as well as how to install and configure the database and Galera software on each node. It'll end by showing you how to start the cluster.


.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Outline of Training Video

.. container:: list-col1

   **1. Galera Cluster Overviews** :raw-html:`<small>(time index: 2:47)</small>` |br| Briefly discusses Galera Cluster basics.

   **2. Encryption Key** :raw-html:`<small>(time index: 9:37)</small>` |br| In preparation for AWS, shows how to create an encryption key.

   **3. Creating AWS Instances** :raw-html:`<small>(time index: 13:27)</small>` |br| Demonstrates how to create AWS instances |---| virtual servers to be nodes for cluster.

   **4. Installing Software on Nodes** :raw-html:`<small>(time index: 22:21)</small>` |br| Installing the needed software on each node.


.. container:: list-col2

   **5. Configuring Nodes** :raw-html:`<small>(time index: 36:59)</small>` |br| Shows how to configure nodes for use in cluster.

   **6. Opening Ports** :raw-html:`<small>(time index: 41:55)</small>` |br| Setting security to allow Galera traffic through specific ports.

   **7. Starting Galera** :raw-html:`<small>(time index: 44:41)</small>` |br| Starting and testing a Galera cluster.


.. raw:: html

    <video width="820" height="547" preload="metadata" controls>
    <source src="https://galeracluster.com/library-media/videos/galera-on-aws.mp4#t=0.5" type="video/mp4">
    </video>

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
