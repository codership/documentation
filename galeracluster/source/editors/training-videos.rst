.. meta::
   :title: Codership Editors' Page
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../documentation/index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

.. role:: raw-html(raw)
   :format: html


.. cssclass:: library-list
.. _`training-video-plans`:

=============================
Codership Training Videos
=============================

Below is a list of training vides planned for the next few months. They cover essential topics and are grouped by skill level, as well as an extra set of articles cover some special topics.

.. rst-class:: rubric-1 rubric-separated
.. rubric:: Beginner Tutorials

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   ":doc:`Introduction to Galera Cluster <../training/videos/galera-intro>` :raw-html:`<small>published 2 march 2016</small>` Overview of Galera and minimal components. Although conceptual, not practical, it doesn't delve deep.", "**Installing Galera Cluster with MySQL** :raw-html:`<small>scheduled 25 sept. 2019</small>` Shows the basics of how to install the Galera Cluster with MySQL on three nodes."
   "**MySQL Replication vs. Galera Cluster** :raw-html:`<small>scheduled 15 oct. 2019</small>` Demonstrates how to configure and use standard replication and compares that to a Galera Cluster.", "**Installing Galera Cluster with MariaDB** :raw-html:`<small>scheduled 25 sept. 2019</small>` Shows the basics of how to install the Galera Cluster with MariaDB on three nodes."


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Intermediate Tutorials

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Back-Ups with Galera** :raw-html:`<small>not yet scheduled</small>` Shows how to remove a node from a cluster to make a proper back-up with GTIDs.", "**Software Upgrades** :raw-html:`<small>not yet scheduled</small>` Planning and conducting upgrades of Galera software on an active cluster."
   "**Recovering from a Cluster Crash** :raw-html:`<small>not yet scheduled</small>` Goes through the steps to restart a cluster, and to ensure data isn't lost or overwritten.", ""


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Special Topics

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   ":doc:`Galera Cluster on AWS <../training/videos/galera-aws-installing>` :raw-html:`<small>scheduled 15 july 2019</small>` Shows the basics of how to set up server instances on Amazon's AWS for a Galera Cluster with MySQL or MariaDB.", ":doc:`Monitoring a Cluster <../training/videos/galera-monitoring>` :raw-html:`<small>published 15 sept. 2019</small>` Present status variables used for monitoring, including ``wsrep_provider_options`` and a bash simple script."
   "**Load Balancing a Galera Cluster** :raw-html:`<small>scheduled 15 nov. 2019</small>` How to install and configure a load balancer (e.g., HA Proxy) to balance traffic among nodes.", ""


.. |br| raw:: html

   <br />
