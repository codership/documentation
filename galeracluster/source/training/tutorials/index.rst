.. meta::
   :title: Tutorials on Galera Cluster
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

         - :doc:`Tutorial Articles <./index>`
         - :doc:`Training Videos <../videos/index>`


.. cssclass:: training-list
.. _`training-tutorials`:

======================================
Codership Tutorials on Galera Cluster
======================================

These are tutorial articles of the training section of the Codership Library. Here you'll find tutorial articles on how to get started with Galera and other basic tasks related to initially starting a Galera Cluster. There are also some intermediate articles on a few other aspects of Galera and related software.


.. _`training-tutorials-entry`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Basic & Entry Level

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`getting-started`

   .. rst-class:: list-stats

      Length: 840 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      This article explains Galera Cluster, how it works. It provides an overview for installing Galera Cluster and initializing nodes in a cluster. It's a jumping off point to several other tutorial articles here.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-installation`

   .. rst-class:: list-stats

      Length: 946 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      This tutorial provides instruction to prepare your servers and installing Galera Cluster on each.  When you install Galera Cluster, you must choose between three implementations available.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`configuration`

   .. rst-class:: list-stats

      Length:  964 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      After installing Galera Cluster on your servers, you'll need to configure the database itself to serve as a node in a cluster.  This straightforward article provides you a list of parameters to set in each node's database configuration file, as well as setting swap space.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`wsrep-configuration`

   .. rst-class:: list-stats

      Length:  964 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      With the system-level configurations complete, this article provides a guide to configuring the database server to connect and communicate with the cluster and explains the syntax format used in cluster addresses.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`starting-cluster`

   .. rst-class:: list-stats

      Length:  1,097 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      A cluster requires at least two nodes, but you have to start the first node somehow. To do this, you'll need to bootstrap the Primary Component. This article explains how to initialize the cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`testing-cluster`

   .. rst-class:: list-stats

      Length:  499 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      Once you have a cluster running, you should test some of the features to ensure it’s working properly. This will also help you understand how a cluster works so you can decide on your deployment. This tutorial provides a rough guide to testing replication and similar cluster operations.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`restarting-cluster`

   .. rst-class:: list-stats

      Length:  791 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      You may need occasionally to restart a cluster, perhaps becauser of a major power failure. Whatever the reason, restarting a cluster so that data saved only on one node isn't overwritten by another node which just happened to have rejoined the cluster first can be tricky. This article explains how to determine the most up-to'-date node and then to restart the Primary Component on that one.



.. _`training-tutorials-intermediate`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Intermediate Level


.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`galera-monitoring`

   .. rst-class:: list-stats

      Length: 2535 words; Writer: Russell J.T. Dyer; Pub: Jul 2019

   .. rst-class:: list-abstract

      This tutorial explains how to monitor a Galera Cluster, utilizing the Galera specific status variables, as well as employing scripts for logging status information.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`debug-problems-with-sst`

   .. rst-class:: list-stats

      Length:  985 words; Writer: Philip Stoev; Pub: Jul 2015

   .. rst-class:: list-abstract

      When new nodes join a cluster, Galera will transfer internally the entire dataset to the joiner. The same procedure, called State Snapshot Transfer (SST), applies to nodes that are rejoining the cluster after being down for a long period of time. This article offers some insights and troubleshooting advice for when there are problems with SST.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`primary-component`

   .. rst-class:: list-stats

      Length:  782 words; Writer: Philip Stoev; Pub: Aug 2015

   .. rst-class:: list-abstract

      This article describes the Primary Component. This is a central concept in how Galera ensures database consistency and no divergence between nodes in case of a network split.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`supporting-transaction-isolation-levels`

   .. rst-class:: list-stats

      Length:  1009 words; Writer: Seppo Jaakola; Pub: Sep 2015

   .. rst-class:: list-abstract

      Many DBAs and database developers don't understand what MySQL transaction isolation levels Galera CLuster supports and how it does so. This articles tries to answer those uncertainties.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`safe-to-bootstrap-feature`

   .. rst-class:: list-stats

      Length:  745 words; Writer: Philip Stoev; Pub: Nov 2016

   .. rst-class:: list-abstract

      It's usually not necessary to shut down an entire cluster for normal operation. However, sometimes it's necessary. Often times it's in the midst of a stressful situaiton. So it's important to shut down a cluster safely and as quickly as possible to avoid extended downtime and potential data loss. This article addresses this situation, in particular “Safe-to-Bootstrap” protection.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`sst-or-not`

   .. rst-class:: list-stats

      Length:  1001 words; Writer: Philip Stoev; Pub: Dec 2016

   .. rst-class:: list-abstract

      If a node leaves the cluster and subsequently rejoins, Galera will use one of two primary methods of getting the node rejoined and synchronized quickly with the rest of the cluster. This article describes the entire process of doing this and confusing messages one might see in the logs.



.. _`training-tutorials-advanced`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Advanced Level

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`achieving-read-after-write-semantics`

   .. rst-class:: list-stats

      Length:  599 words; Writer: Philip Stoev; Pub: Jun 2015

   .. rst-class:: list-abstract

      Some applications attempt to read immediately a value just inserted into the database, without making those operations part of a single transaction. A read/write splitting proxy or a connection pool combined with a load-balancer can direct each operation to a different database node.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`geo-distributed-clusters`

   .. rst-class:: list-stats

      Length:  1043 words; Writer: Philip Stoev; Pub: Oct 2014

   .. rst-class:: list-abstract

      With Galera, nodes may be located in a different physical or even geographical location. This article presents some of the benefits from having a geo-distributed cluster and the specific Galera features that enable practical replication across a WAN.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`debugging-transaction-conflicts`

   .. rst-class:: list-stats

      Length:  1,086 words; Writer: Philip Stoev; Pub: Jun 2015

   .. rst-class:: list-abstract

      When using Galera Cluster in multi-master mode, transaction conflicts may occur if two clients attempt to modify the same row at the same time. Such conflicts are reported a deadlock errors to the application. This article explains how to use the logs to troubleshoot such a problem.



.. _`training-tutorials-special`:
.. container:: banner

   .. rst-class:: rubric-1
   .. rubric:: Special Topics

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`aws-galera-cluster`

   .. rst-class:: list-stats

      Length: 2494 words; Writer: Russell J.T. Dyer; Pub: Jun 2019

   .. rst-class:: list-abstract

      This tutorial explains how to use Amazon Web Services (AWS) to create virtual servers to be used as a Galera Cluster. It will explain how to create and configure AWS, as well as how to install and configure the database and Galera software on each node. It'll end by showing you how to start the cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`migrate`

   .. rst-class:: list-stats

      Length:  2087 words; Writer: Staff; Pub: Oct 2014

   .. rst-class:: list-abstract

      If you have an existing database, but aren't yet using Galera Cluster, you'll have to migrate your data. This has to be done a particular way. This tutorial article will help you to understand the concepts involved and take you through the steps to migrate a database.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`getting-started-docker`

   .. rst-class:: list-stats

      Length: 1416 words; Writer: Erkan Yanar; Pub: May 2015

   .. rst-class:: list-abstract

      Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications. This first of two articles on using Galera with Docker explains how to build a basic Docker Image and locally deploy it on a test cluster. It also describes how to deploy Galera Cluster over multiple Docker hosts.



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
   aws-galera-cluster
   galera-monitoring
   migrate
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
