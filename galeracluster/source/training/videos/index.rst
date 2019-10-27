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


.. cssclass:: training-list
.. _`training-videos`:

===========================
Codership Training Videos
===========================

To help you to learn how to install, configure and use Galera Cluster and related software, we have created a series of traiing videos, screencasts and demonstrations.  They're grouped on three main catagories:  Introduction & Installation; Administration & Resolution; and Performance & High Availability.

.. _`training-videos-intro-install`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Introduction & Installation

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-intro`

   .. rst-class:: list-stats

      published: march 2016; length: 4 mins

   .. rst-class:: list-abstract

      This fairly non-technical video presents Galera Cluster:  How it works and the benefits to organizations using it.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-mysql-installing`

   .. rst-class:: list-stats

      published: sep 2019; length: 32 mins

   .. rst-class:: list-abstract

      Shows the basics of how to install Galera Cluster and MySQL software, and configure them on three nodes.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-mariadb-installing`

   .. rst-class:: list-stats

      published: sep 2019; length: 30 mins

   .. rst-class:: list-abstract

      Shows the basics of how to install Galera Cluster and MariaDB software on three nodes |---| and configure the ports for security and other basic items.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`aws-galera-cluster`

   .. rst-class:: list-stats

      published: jul 2019; length: 52 mins

   .. rst-class:: list-abstract

      Shows the basics of how to set up server instances on Amazon's AWS for a Galera Cluster with either MySQL or MariaDB.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`standard-replication-galera`

   .. rst-class:: list-stats

      published: oct 2019; length: 54 mins

   .. rst-class:: list-abstract

      Demonstrates how to configure and use standard MySQL and MariaDB replication and Galera Cluster |---| and compares the two.



.. _`training-videos-admin-trouble`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Administration & Resolution

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-monitoring`

   .. rst-class:: list-stats

      published: sep 2019; length: 47 mins

   .. rst-class:: list-abstract

      This training video explains how to monitor a Galera Cluster, utilizing the Galera specific status variables, as well as employing scripts for logging status information.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: **Software Upgrades**

   .. rst-class:: list-stats

      scheduled: undecided; length: unknown

   .. rst-class:: list-abstract

      Planning and conducting upgrades of Galera software on an active cluster.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-backup`

   .. rst-class:: list-stats

      published: oct 2019; length: 1 hr, 5 mins

   .. rst-class:: list-abstract

      Explains the basics of back-ups and demonstrates a few methods for making back-ups of databases on a node in a Galera Cluster. Additionally, it covers briefly how to restore back-ups and a cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: **Recovering from a Cluster Crash**

   .. rst-class:: list-stats

      scheduled: undecided; length: unknown

   .. rst-class:: list-abstract

      Goes through the steps to restart a cluster, and to ensure data isn't lost or overwritten.



.. _`training-videos-performance-availability`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Performance & High Availability

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: **Load Balancing a Galera Cluster**

   .. rst-class:: list-stats

      scheduled: nov 2019; length: unknown

   .. rst-class:: list-abstract

      How to install and configure a load balancer (e.g., HA Proxy) to balance traffic among nodes in a Galera Cluster.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`high-availability-with-galera-cluster`

   .. rst-class:: list-stats

      published: april 2019; length: 60 mins

   .. rst-class:: list-abstract

      This video is of Colin Charles speaking about the MySQL Server High Availability landscape and how Galera Cluster fits into it.


.. toctree::
   :maxdepth: 2
   :hidden:

   aws-galera-cluster
   galera-intro
   galera-backup
   high-availability-with-galera-cluster
   galera-mariadb-installing
   galera-mysql-installing
   galera-monitoring
   standard-replication-galera

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
