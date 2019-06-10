.. cssclass:: training-list

==============
Tutorials
==============
.. _`training-tutorials`:

These are tutorial articles of the training section of the Codership Library. Here you'll find tutorial articles on how to get started with Galera and other basic tasks related to initially starting a Galera Cluster. There are also some intermediate articles on a few other aspects of Galera and related software.

---------------
Beginner Level
---------------

.. rubric:: :doc:`getting-started`
   :class: list-sub-header

.. rst-class:: list-stats

   Length: 840 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   This article explains Galera Cluster, how it works. It provides an overview for installing Galera Cluster and initializing nodes in a cluster. It's a jumping off point to several other tutorial articles here.


.. rubric:: :doc:`galera-installation`
   :class: list-sub-header

.. rst-class:: list-stats

   Length: 946 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   This tutorial provides instruction to prepare your servers and installing Galera Cluster on each.  When you install Galera Cluster, you must choose between three implementations available.


.. rubric:: :doc:`configuration`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  964 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   After installing Galera Cluster on your servers, you'll need to configure the database itself to serve as a node in a cluster.  This straightforward article provides you a list of parameters to set in each node's database configuration file, as well as setting swap space.


.. rubric:: :doc:`wsrep-configuration`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  964 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   With the system-level configurations complete, this article provides a guide to configuring the database server to connect and communicate with the cluster and explains the syntax format used in cluster addresses.


.. rubric:: :doc:`starting-cluster`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  1,097 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   A cluster requires at least two nodes, but you have to start the first node somehow. To do this, you'll need to bootstrap the Primary Component. This article explains how to initialize the cluster.


.. rubric:: :doc:`testing-cluster`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  499 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   Once you have a cluster running, you should test some of the features to ensure it’s working properly. This will also help you understand how a cluster works so you can decide on your deployment. This tutorial provides a rough guide to testing replication and similar cluster operations.


.. rubric:: :doc:`restarting-cluster`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  791 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

.. rst-class:: list-abstract

   You may need occasionally to restart a cluster, perhaps becauser of a major power failure. Whatever the reason, restarting a cluster so that data saved only on one node isn't overwritten by another node which just happened to have rejoined the cluster first can be tricky. This article explains how to determine the most up-to'-date node and then to restart the Primary Component on that one.


-------------------
Intermediate Level
-------------------

.. rubric:: :doc:`getting-started-docker-pt1`
   :class: list-sub-header

.. rst-class:: list-stats

   Length: 762 words; Writer: Erkan Yanar; Published: May 6, 2015; Topic: Container; Level: Intermediate

.. rst-class:: list-abstract

   Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications. This first of two articles on using Galera with Docker explains how to build a basic Docker Image and locally deploy it on a test cluster.


.. rubric:: :doc:`getting-started-docker-pt2`
   :class: list-sub-header

.. rst-class:: list-stats

   Length: 654 words; Writer: Erkan Yanar; Published: May 12, 2015; Topic: Container; Level: Intermediate

.. rst-class:: list-abstract

   This second article of two on using Galera with Docker describes how to deploy Galera Cluster over multiple Docker hosts.


.. rubric:: :doc:`achieving-read-after-write-semantics`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  599 words; Writer: Philip Stoev; Published: June 17, 2015; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   Some applications attempt to read immediately a value just inserted into the database, without making those operations part of a single transaction. A read/write splitting proxy or a connection pool combined with a load-balancer can direct each operation to a different database node.


.. rubric:: :doc:`debugging-transaction-conflicts`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  1,086 words; Writer: Philip Stoev; Published: June 29, 2015; Topic: Troubleshooting; Level: Intermediate

.. rst-class:: list-abstract

   When using Galera Cluster in multi-master mode, transaction conflicts may occur if two clients attempt to modify the same row at the same time. Such conflicts are reported a deadlock errors to the application. This article explains how to use the logs to troubleshoot such a problem.


.. rubric:: :doc:`debug-problems-with-sst`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  985 words; Writer: Philip Stoev; Published: July 6, 2015; Topic: Troubleshooting; Level: Intermediate

.. rst-class:: list-abstract

   When new nodes join a cluster, Galera will transfer internally the entire dataset to the joiner. The same procedure, called State Snapshot Transfer (SST), applies to nodes that are rejoining the cluster after being down for a long period of time. This article offers some insights and troubleshooting advice for when there are problems with SST.


.. rubric:: :doc:`geo-distributed-clusters`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  1043 words; Writer: Philip Stoev; Published: October 20, 2014; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   With Galera, nodes may be located in a different physical or even geographical location. This article presents some of the benefits from having a geo-distributed cluster and the specific Galera features that enable practical replication across a WAN.


.. rubric:: :doc:`primary-component`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  782 words; Writer: Philip Stoev; Published: August 25, 2015; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   This article describes the Primary Component. This is a central concept in how Galera ensures database consistency and no divergence between nodes in case of a network split.


.. rubric:: :doc:`supporting-transaction-isolation-levels`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  1009 words; Writer: Seppo Jaakola; Published: September 21, 2015; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   Many DBAs and database developers don't understand what MySQL transaction isolation levels Galera CLuster supports and how it does so. This articles tries to give answer to those uncertainties.


.. rubric:: :doc:`safe-to-bootstrap-feature`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  745 words; Writer: Philip Stoev; Published: November 18, 2016; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   It's usually not necessary to shut down an entire cluster for normal operation. However, sometimes it's necessary. Often times it's in the midst of a stressful situaiton. So it's important to shut down a cluster safely and as quickly as possible to avoid extended downtime and potential data loss. This article addresses this situation, in particular “Safe-to-Bootstrap” protection.


.. rubric:: :doc:`sst-or-not`
   :class: list-sub-header

.. rst-class:: list-stats

   Length:  1001 words; Writer: Philip Stoev; Published: December 6, 2016; Topic: General; Level: Intermediate

.. rst-class:: list-abstract

   If a node leaves the cluster and subsequently rejoins, Galera will use one of two primary methods of getting the node rejoined and synchronized quickly with the rest of the cluster. This article describes the entire process of doing this and confusing messages one might see in the logs.


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
   getting-started-docker-pt1
   getting-started-docker-pt2
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
