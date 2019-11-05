.. meta::
   :title: High Availability with Galera Cluster
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

        Related Articles

.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article library-video
.. _`video-galera-high-availability`:

======================================
High Availability with Galera Cluster
======================================


.. container:: video-abstract list-col2-3

   The MySQL Server High Availability landscape provides with a slew of tools to help you ensure that your databases keep humming. Such tools are Galera Cluster, however, it is worth looking at semi-synchronous replication with failover tools, and also the usual leader-follower asynchronous replication. Today more workloads are moving to the cloud, and what failover options do you get with Amazon RDS for MySQL or even Aurora? What about the newfangled group replication and InnoDB Cluster? And let us not forget that Galera Cluster has spawned branches too!

.. container:: list-col1-3

   .. rst-class:: video-stats
   .. rubric:: Video Specifications

   .. rst-class:: video-stats

      - Speaker: Colin Charles
      - Date: April 10, 2019
      - Length of Video: 60 minutes


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Outline of Training Video

.. container:: list-col1

   **1. Codership** :raw-html:`<small>(time index: 1:04)</small>` |br| Brief introduction to Codership, the creators and developers of Galera Cluster.

   **2. What is High Availability** :raw-html:`<small>(time index: 2:50)</small>` |br| Discussion of the fundamentals of High Availability |---| the value and goals |---| as well as how it's achieved generally.

   **3. Redundancy Through MySQL Replication** :raw-html:`<small>(time index: 19:22)</small>` |br| Covers briefly how standard replication may be used for maintaining high availability.

   **4. Failover Frameworks** :raw-html:`<small>(time index: 21:55)</small>` |br| Discusses methods by which failed servers, in particular a master, may be replaced |---| including common difficulties one may encounter.

.. container:: list-col2

   **5. Proxies** :raw-html:`<small>(time index: 25:05)</small>` |br| Explains how proxies may be used for directing traffic among multiple servers, and redirecting away from a down server.

   **6. Galera Cluster** :raw-html:`<small>(time index: 27:13)</small>` |br| Introduction to Galera Cluster and how high availability can be achieved so easily with it, as well as an explanation of how Galera works.

   **7.**Cloud-Based Solutions** :raw-html:`<small>(time index: 45:37)</small>` |br| Explains how Galera Cluster may be used on a cloud situation, how a cloud-based cluster can solved problems, as well as how to make use of them.

.. raw:: html

    <video width="820" height="547" preload="metadata" controls>
    <source src="https://galeracluster.com/library-media/videos/galera-high-availability.mp4#t=0.1" type="video/mp4">
    </video>

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
