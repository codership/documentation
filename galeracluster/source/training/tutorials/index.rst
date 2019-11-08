.. meta::
   :title: Tutorials on Galera Cluster
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

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      .. cssclass:: sub-links

         - :doc:`Training Videos <../videos/index>`

      - :doc:`FAQ <../../faq>`

.. cssclass:: library-index
.. _`training-tutorials`:

======================================
Codership Tutorials on Galera Cluster
======================================

.. rst-class:: page-abstract

   These are tutorial articles of the training section of the Codership Library. Here you'll find tutorial articles on how to get started with Galera and other basic tasks related to initially starting a Galera Cluster. There are also some intermediate articles on a few other aspects of Galera and related software.


.. _`training-tutorials-entry-install`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Introduction & Installation

.. container:: list-col1

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`getting-started`

   .. rst-class:: list-stats

      Length: 840 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      This article explains Galera Cluster, how it works. It provides an overview for installing Galera and initializing nodes in a cluster. It's a jumping off point to several other tutorials here.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`galera-installation`

   .. rst-class:: list-stats

      Length: 946 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      This tutorial provides instructions to prepare your servers and instal Galera Cluster on each.  When you install Galera, you have to choose between three implementations available.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`galera-on-aws`

   .. rst-class:: list-stats

      Length: 2494 words; Writer: Russell J.T. Dyer; Pub: Jun 2019

   .. rst-class:: list-abstract

      This tutorial explains how to use Amazon Web Services (AWS) to create virtual servers for a Galera Cluster: how to install and configure the database and Galera software on each node.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`configuration`

   .. rst-class:: list-stats

      Length:  964 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      After installing Galera, you'll need to configure each node. This straightforward article provides a list of parameters to set in each node's database configuration file.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`wsrep-configuration`

   .. rst-class:: list-stats

      Length:  964 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      This article provides a guide to configure the database server to connect and communicate with the cluster. It explains the syntax format used in cluster addresses.


.. container:: list-col2

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`starting-cluster`

   .. rst-class:: list-stats

      Length:  1,097 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      A cluster requires at least two nodes, but you have to start the first one somehow. You'll need to bootstrap the Primary Component. This article explains how to initialize the cluster.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`getting-started-docker`

   .. rst-class:: list-stats

      Length: 1416 words; Writer: Erkan Yanar; Pub: May 2015

   .. rst-class:: list-abstract

      This article explains how to build a basic Docker Image and deploy it on a test cluster. It also describes how to deploy Galera Cluster over multiple Docker hosts.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`testing-cluster`

   .. rst-class:: list-stats

      Length:  499 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      Once you have a cluster running, test its features to ensure it’s working well, to decide on a deployment plan. This tutorial provides a guide to testing replication and cluster operations.



.. _`training-tutorials-admin`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Administration

.. container:: list-col1

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`galera-monitoring`

   .. rst-class:: list-stats

      Length: 2535 words; Writer: Russell J.T. Dyer; Pub: Jul 2019

   .. rst-class:: list-abstract

      This tutorial explains how to monitor a Galera Cluster, utilizing the Galera specific status variables, as well as employing scripts for logging status information.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`galera-backup`

   .. rst-class:: list-stats

      Length: 2693 words; Writer: Russell J.T. Dyer; Pub: Nov 2019

   .. rst-class:: list-abstract

      Using Galera, there are a few ways to make a back-up. This article looks at back-up basics, methods involving replication, and how to automate back-ups using the Galera functionality.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`debug-problems-with-sst`

   .. rst-class:: list-stats

      Length:  985 words; Writer: Philip Stoev; Pub: Jul 2015

   .. rst-class:: list-abstract

      The entire dataset is transfered (i.e., SST) to a new node and when a node rejoin after being down for a long time. This article offers insights and advice if there are problems with SST.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`primary-component`

   .. rst-class:: list-stats

      Length:  782 words; Writer: Philip Stoev; Pub: Aug 2015

   .. rst-class:: list-abstract

      This article describes the Primary Component. This is a central concept in how Galera ensures database consistency and no divergence between nodes in case of a network split.


.. container:: list-col2

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`migrate`

   .. rst-class:: list-stats

      Length:  2087 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      Migrating data with Galera Cluster should be done carefully. This tutorial article will help you to understand the concepts involved and take you through the steps to migrate a database.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`supporting-transaction-isolation-levels`

   .. rst-class:: list-stats

      Length:  1009 words; Writer: Seppo Jaakola; Pub: Sep 2015

   .. rst-class:: list-abstract

      Many DBAs and database developers don't understand what MySQL transaction isolation levels Galera CLuster supports and how it does so. This articles tries to answer those uncertainties.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`sst-or-not`

   .. rst-class:: list-stats

      Length:  1001 words; Writer: Philip Stoev; Pub: Dec 2016

   .. rst-class:: list-abstract

      When a node rejoins a cluster, there are two methods of synchronizing it quickly. This article describes the process of doing this and confusing messages one might see in the logs.



.. _`training-tutorials-restart-recover`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Restarting & Recovery


.. container:: list-col1

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`restarting-cluster`

   .. rst-class:: list-stats

      Length:  791 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      Restarting a cluster so that data isn't overwritten can be tricky. This article explains how to determine the most up-to-date node, so that it's the first node of the new cluster.


.. container:: list-col2

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`safe-to-bootstrap-feature`

   .. rst-class:: list-stats

      Length:  745 words; Writer: Philip Stoev; Pub: Nov 2016

   .. rst-class:: list-abstract

      When it's necessary to shut down a cluster, it's important to do so safely and as quickly as possible to avoid extended downtime and data loss. This article gives advice in this area.


.. _`training-tutorials-performance-availability`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Performance & High Availability

.. container:: list-col1

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`achieving-read-after-write-semantics`

   .. rst-class:: list-stats

      Length:  599 words; Writer: Philip Stoev; Pub: Jun 2015

   .. rst-class:: list-abstract

      Clients may try to read rows just inserted, excluding it from a transaction. Read/write splitting proxy, or a connection pool and a load balancer, can send queries to other nodes.


   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`geo-distributed-clusters`

   .. rst-class:: list-stats

      Length:  1043 words; Writer: Philip Stoev; Pub: Oct 2014

   .. rst-class:: list-abstract

      Nodes may be located in multiple physical locations. This article presents the benefits of a geo-distributed cluster, and Galera specific features to enable replication across a WAN.


.. container:: list-col2

   .. rst-class:: sub-heading list-sub-header
   .. rubric:: :doc:`debugging-transaction-conflicts`

   .. rst-class:: list-stats

      Length:  1,086 words; Writer: Philip Stoev; Pub: Jun 2015

   .. rst-class:: list-abstract

      When using Galera in multi-master mode, transaction conflicts may occur if clients try to modify the same row at the same time. This discusses troubleshooting these deadlock errors.




.. toctree::
   :maxdepth: 3
   :hidden:

   getting-started
   galera-installation
   configuration
   wsrep-configuration
   starting-cluster
   testing-cluster
   restarting-cluster
   galera-on-aws
   galera-monitoring
   migrate
   galera-backup
   getting-started-docker
   achieving-read-after-write-semantics
   debugging-transaction-conflicts
   debug-problems-with-sst
   geo-distributed-clusters
   primary-component
   supporting-transaction-isolation-levels
   safe-to-bootstrap-feature
   sst-or-not

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
