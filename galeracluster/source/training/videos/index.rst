.. meta::
   :title: Training Videos on Galera Cluster
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

      .. cssclass:: bull-head

         Related Articles

.. role:: raw-html(raw)
   :format: html

.. cssclass:: training-list
.. _`training-videos`:

===========================
Codership Training Videos
===========================

This section is for training videos on Galera Cluster and related software. At this point, they're primarily screencasts from presentations given at various conferences. We intend to add more screencasts, but made in a controlled enviroment, focusing on one aspect of Galera Cluster or related software.


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Basic & Entry Level


.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   ":doc:`galera-intro` :raw-html:`<small>published 2 march 2016; length:  4 minutes</small>` This faily non-technical video presents Galera Cluster:  How it works and the benefits to organizations using it.", ":doc:`galera-mysql-installing` :raw-html:`<small>scheduled 25 sept. 2019; length: 32 minutes</small>` Shows the basics of how to install Galera Cluster and MySQL software, and configure them on three nodes."
   "**MySQL Replication vs. Galera Cluster** :raw-html:`<small>scheduled 15 oct. 2019; length: 30 minutes</small>` Demonstrates how to configure and use standard replication and compares that to a Galera Cluster.", ":doc:`galera-mariadb-installing` :raw-html:`<small>scheduled 27 sept. 2019; length: not yet published</small>` Shows the basics of how to install Galera Cluster and MariaDB software on three nodes |---| and configure the ports for security and other basic items."


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Intermediate Level

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Back-Ups with Galera** :raw-html:`<small>not yet scheduled</small>` Shows how to remove a node from a cluster to make a proper back-up with GTIDs.", "**Software Upgrades** :raw-html:`<small>not yet scheduled</small>` Planning and conducting upgrades of Galera software on an active cluster."
   "**Recovering from a Cluster Crash** :raw-html:`<small>not yet scheduled</small>` Goes through the steps to restart a cluster, and to ensure data isn't lost or overwritten.",""


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Special Topics

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   ":doc:`aws-galera-cluster` :raw-html:`<small>published 12 july 2019; length: 52 minutes</small>` Shows the basics of how to set up server instances on Amazon's AWS for a Galera Cluster with either MySQL or MariaDB.", ":doc:`galera-monitoring` :raw-html:`<small>published 15 sept. 2019; length: 47 minutes</small>` This training video explains how to monitor a Galera Cluster, utilizing the Galera specific status variables, as well as employing scripts for logging status information."
   "**Load Balancing a Galera Cluster** :raw-html:`<small>scheduled 15 nov. 2019; length: not yet published</small>` How to install and configure a load balancer (e.g., HA Proxy) to balance traffic among nodes in a Galera Cluster.", ":doc:`high-availability-with-galera-cluster` :raw-html:`<small>scheduled 10 april 2019; length: 60 minutes</small>` This video is of Colin Charles speaking about the MySQL Server High Availability landscape and how Galera Cluster fits into it."




.. toctree::
   :maxdepth: 2
   :hidden:

   aws-galera-cluster
   ddl-schema-upgrades
   galera-intro
   galera-installation-quick-start
   high-availability-with-galera-cluster
   migrating-master-slave-to-multi-master
   geo-distributed-galera-cluster
   galera-dba-devops
   galera-mariadb-installing
   galera-mysql-installing
   galera-monitoring
   multi-master-galera-advantages

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
