.. meta::
   :title: Installing a Galera Cluster on AWS
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

      - :doc:`Install Galera on AWS <../tutorials/galera-on-aws>`

      Other Resources

      - `Galera Repository <http://releases.galeracluster.com/>`_
      - `MariaDB Repository <https://downloads.mariadb.org/mariadb/repositories/>`_

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
.. _`video-aws-galera-cluster`:

====================================
Installing a Galera Cluster on AWS
====================================

.. container:: video-abstract list-col2-3

   This training video explains how to use Amazon Web Services (AWS) to create virtual servers to be used as a Galera Cluster. It explains how to create and configure AWS, as well as how to install and configure the database and Galera software on each node. The video ends by showing you how to start a Galera Cluster.

   As part of the training process, in the right margin here, you can find a link to a page containing exercises related to the training video.  You should look at it before starting the video so that you can be prepared.  There's also a link to a PDF copy of the slide presentation. It's been set so that you make notes on it.  In the left margin are links to related documentation, articles, and other materials.

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Russell J.T. Dyer
      - Date: July 12, 2019
      - Length of Video: 52 minutes

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Training Exercises <galera-aws-installing-exercises>`
      - `Slide Presentation </library-media/pdf/galera-aws-installing.pdf>`_
      - :doc:`Example Configuration <galera-mariadb-installing-examples>`
      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_


.. container:: banner

   .. rst-class:: section-heading
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

.. container:: bottom-links

   Related Documents

   - :doc:`Firewall Settings <../../documentation/firewall-settings>`
   - :doc:`firewalld <../../documentation/firewalld>`
   - :doc:`Installing Galera <../../documentation/install>`
   - :doc:`Node Provisioning <../../documentation/node-provisioning>`
   - :doc:`SELinux <../../documentation/selinux>`
   - :doc:`State Transfer <../../documentation/state-transfer>`
   - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

   Related Articles

   - :doc:`Install Galera on AWS <../tutorials/galera-on-aws>`

   Other Resources

   - `Galera Repository <http://releases.galeracluster.com/>`_
   - `MariaDB Repository <https://downloads.mariadb.org/mariadb/repositories/>`_


.. toctree::
   :maxdepth: 2
   :hidden:

   galera-aws-installing-exercises

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
