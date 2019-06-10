.. cssclass:: tutorial-article

=================
 Getting Started
=================
.. _`getting-started`:

.. rst-class:: list-stats

   Length: 840 words; Published: October 20, 2014; Topic: General; Level: Beginner


Galera Cluster is a synchronous replication solution to improve availability and performance of the MySQL database service.  All nodes in Galera Cluster are identical and fully representative of the cluster.  They allow for unconstrained transparent client access, operating as a single, distributed MySQL server.  It provides,

- Transparent client connections, so it's highly compatible with existing applications;

- Synchronous data safety semantics |---| if a client received confirmation, transactions will be committed on every node; and

- Automatic write conflict detection and resolution, so that nodes are always consistent.

Galera Cluster is well suited for LAN, WAN, container and cloud environments.  The following tutorial articles provide you with the basics to setting up and deploying Galera Cluster.  Bear in mind before you get started that you need root access to at least three Linux or FreeBSD hosts and their IP addresses.

.. note:: With the latest release Galerea Cluster begins the 4.x branch, introducing a number of new features.  For more information on these features, see :doc:`What's New <../../whats-new>`.


.. rubric:: How Galera Cluster Works
.. _`how-galera-works`:

The primary focus is data consistency.  The transactions are either applied on every node or not all.  So, the databases stay synchronized, provided that they were properly configured and synchronized at the beginning.

The :term:`Galera Replication Plugin` differs from the standard MySQL Replication by addressing several issues, including multi-master write conflicts, replication lag and slaves being out of sync with the master.

.. figure:: ../../images/galerausecases1.png

In a typical instance of a Galera Cluster, applications can write to any node in the cluster and transaction commits, (RBR events), are then applied to all the servers, through certification-based replication.

Certification-based replication is an alternative approach to synchronous database replication, using group communication and transaction ordering techniques.

.. note:: For security and performance reasons, it's recommended that you run Galera Cluster on its own subnet.


.. rubric:: Node Initialization
.. _`node-init`:

Individual nodes in Galera Cluster are MySQL, MariaDB or Percona XtraDB.  But, deploying a node is not exactly the same as the standard standalone instance of the database server.  You need to take a few additional steps in order to properly install and configure the software.  The software runs on any unix-like operating system.  These articles provide guides to installing and configuring nodes for Galera Cluster.

- :doc:`Installation <galera-installation>`

  Once you have your server hardware ready, including at least three hosts running either Linux or FreeBSD and their respective IP addresses.  This article provides guides to preparing the server and installing Galera Cluster.  When you install Galera Cluster, you must choose between three implementations available.  For each implementations, you can install the software using Debian- and RPM-based binary packages or by building the node from source.

  - **Galera Cluster for MySQL**: The reference implementation from Codership, Oy. You can use either the :doc:`Install MySQL Binary Installation <../../documentation/install-mysql>` or the :doc:`Source Build <../../documentation/install-mysql-src>` methods.

  - **Percona XtraDB Cluster**: The Percona alternative implementation of Galera Cluster, which uses XtraDB in place of MySQL.  You can use either the :doc:`Install XtraDB Binary Installation <../../documentation/install-xtradb>` or the :doc:`Source Build <../../documentation/install-xtradb-src>` methods.

  - **MariaDB Galera Cluster**: The MariaDB Ab alternative implementation of Galera Cluster, which uses MariaDB in place of MySQL.  You can use either the :doc:`Install MariaDB Binary Installation <../../documentation/install-mariadb>` or the :doc:`Source Build <../../documentation/install-mariadb-src>`.


- :doc:`System Configuration <configuration>`

  Before you can start the cluster, you need to configure the individual nodes.  This article covers general parameters that you must set in the ``my.cnf`` configuration file in order to use Galera Cluster.  It also provides a guide to configuring swap space in order to protect the node from crashing due to large write-sets requiring more memory than the server has available.


- :doc:`Replication Configuration <wsrep-configuration>`

  With the system-level configurations complete, this article provides a guide to configuring the database server to connect and communicate with the cluster and explains the syntax format used in cluster addresses.



.. rubric:: Cluster Initialization
.. _`cluster-init`:

With the software installed on the relevant servers in your your infrastructure, you can now initialize Galera Cluster, by bootstrapping the Primary Component then starting all the other nodes as you would any other database server instance.  These tutorial articles provide guides to starting the cluster, ways of testing that it's operational and, when you need to, how to restart the entire cluster.

- :doc:`Starting the Cluster <starting-cluster>`

  In order to start Galera Cluster, you need to bootstrap the Primary Component.  Afterwards, you can start nodes using the same command as you would the standard standalone MySQL, MariaDB or Percona XtraDB database server.  This article provides a guide to initializing the cluster.

- :doc:`Testing a Cluster <testing-cluster>`

  With your cluster online, you may want to test out some of the features in order to ensure it's working properly and to better see how it works in planning out your own deployment.  This tutorial provides a rough guide to testing replication and similar cluster operations.

- :doc:`Restarting the Cluster <restarting-cluster>`

  On occasion, you may need to restart the entire cluster, such as in the case of a power failure where every node is shut down and there is no database server process left running.  This article provides guides to finding your most advanced node and restarting the Primary Component on that node.


.. toctree::
   :maxdepth: 3
   :hidden:

   galera-installation
   configuration
   wsrep-configuration
   starting-cluster
   testing-cluster
   restarting-cluster



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
