=================
 Getting Started 
=================
.. _`getting-started`:

Galera Cluster for MySQL is a synchronous replication solutation that can improve availability and performance of MySQL service.  All Galera Cluster nodes are identical and fully representative of the cluster and allow unconstrained transparent ``mysql`` client access, acting as a single-distributed MySQL server.  It provides:

- Transparent client connections, so it's highly compatible with existing applications;

- Synchronous data safety semantics |---| if a client received confirmation, transactions will be committed on every node; and

- Automatic write conflict detection and resolution, so that nodes are always consistent.

Galera Cluster is well suited for :abbr:`LAN (Local Area Network)`, :abbr:`WAN (Wide Area Network)`, and cloud environments.  This Getting Started chapter will help you to get started with a basic Galera Cluster.  You will need root access to three Linux hosts and their IP Addresses.



--------------------------------------
How Galera Cluster Works
--------------------------------------
.. `how-galera-works`:

The primary focus is data consistency.  The transactions are either applied on every node or not all.  So, the databases stay synchronized, provided that they were properly configured and synchronized at the beginning.

The Galera Replication Plugin differs from the regular MySQL Replication by addressing several issues, including multi-master write conflicts, replication lag and slaves being out of sync with the master.

.. figure:: images/galerausecases1.png

In a typical instance of a Galera Cluster, applications can write to any node in the cluster and transaction commits, (RBR events), are then applied to all the servers, through certification-based replication.

Certification-based replication is an alternative approach to synchronous database replication, using group communication and transaction ordering techniques.

.. note:: For security and performance reasons, it's recommended that you run Galera Cluster on its own subnet.


--------------------
How To Get Started
--------------------

.. toctree::
   :maxdepth: 2
	      
   galerainstallation
   sysconfiguration
   dbconfiguration


------------------------------
Cluster Management
------------------------------
.. _`cluster-management`:

When you finish installation and configuration on your server, you're ready to launch the first node and bring the cluster online.  Once all the nodes are started, you can test that they're working and restart if necessary.

.. toctree::
   :maxdepth: 2

   startingcluster
   testingcluster
   restartingcluster

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
