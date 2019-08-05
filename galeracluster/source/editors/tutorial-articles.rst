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
.. _`tutorial-article-plans`:

=============================
Tutorial Articles
=============================

Below is a list of tutorial articles planned for the next few months. They cover essential topics and are grouped by skill level, as well as an extra set of articles cover some special topics.

.. rst-class:: rubric-1 rubric-separated
.. rubric:: Beginner Tutorials

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Introduction to Galera Cluster** :raw-html:`<small>scheduled 12 aug. 2019</small>` Overview of Galera and minimal components. Although conceptual, not practical, it doesn't delve deep.", "**Installing Galera Cluster** :raw-html:`<small>scheduled 5 aug. 2019</small>` Shows the basics of how to install the Galera Cluster with three nodes."
   "**Plain Replication vs. Galera Cluster** :raw-html:`<small>scheduled 19 aug. 2019</small>` Explains standard replication compared to Galera.", "**The Essentials** :raw-html:`<small>scheduled 19 aug. 2019</small>` Which configuration settings are need and recommended."


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Intermediate Tutorials

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Back-Ups with Galera** :raw-html:`<small>not yet scheduled</small>` How to remove a node from the cluster to make a proper back-up with GTIDs.", "**Scheming within a Cluster** :raw-html:`<small>not yet scheduled</small>` Article on methods to change a table schema."
   "**Recovering from a Cluster Crash** :raw-html:`<small>not yet scheduled</small>` Explains the steps to restart a cluster, to ensure data isn't lost or overwritten.", "**Software Upgrades** :raw-html:`<small>not yet scheduled</small>` Planning and conducting upgrades of Galera software on an active cluster."
   "**The Lines of Communications** :raw-html:`<small>not yet scheduled</small>` Understanding the point of each port and how nodes communicate with each other.", ""


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Advanced Tutorials

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Multi-Mastering Conflicts** :raw-html:`<small>not yet scheduled</small>` Explain how Multi-Master conflicts can occur and how to resolve them and methods to prevent them.", "**Testing a Schema Change** :raw-html:`<small>not yet scheduled</small>` Explain how to install and use ``sysbench`` to test a schema change, to determine how long it will take."
   "**Managing Users** :raw-html:`<small>not yet scheduled</small>` some text", "**Recovering from Split Brain** :raw-html:`<small>not yet scheduled</small>` some text"


.. rst-class:: rubric-1 rubric-separated
.. rubric:: Special Topics

.. csv-table::
   :class: doc-options library-small
   :widths: 50, 50

   "**Load Balancing a Galera Cluster** :raw-html:`<small>scheduled 15 sept. 2019</small>` How to install and configure a load balancer (e.g., MaxScale) to balance traffic among nodes.", ":doc:`Monitoring a Cluster <../training/tutorials/galera-monitoring>` :raw-html:`<small>published 17 july 2019</small>` Present status variables used to monitor, including ``wsrep_provider_options`` and a bash simple script."


.. |br| raw:: html

   <br />
