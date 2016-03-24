=================
 Getting Started 
=================
.. _`getting-started`:

Galera Cluster for MySQL is a synchronous replication solution that can improve availability and performance of MySQL service.  All Galera Cluster nodes are identical and fully representative of the cluster and allow unconstrained transparent ``mysql`` client access, acting as a single-distributed MySQL server.  It provides:

- Transparent client connections, so it's highly compatible with existing applications;

- Synchronous data safety semantics |---| if a client received confirmation, transactions will be committed on every node; and

- Automatic write conflict detection and resolution, so that nodes are always consistent.

Galera Cluster is well suited for :abbr:`LAN (Local Area Network)`, :abbr:`WAN (Wide Area Network)`, and cloud environments.  This Getting Started chapter will help you to get started with a basic Galera Cluster.  You will need root access to three Linux hosts and their IP Addresses.


.. rubric:: How Galera Cluster Works
.. `how-galera-works`:

The primary focus is data consistency.  The transactions are either applied on every node or not all.  So, the databases stay synchronized, provided that they were properly configured and synchronized at the beginning.

The :term:`Galera Replication Plugin` differs from the standard MySQL Replication by addressing several issues, including multi-master write conflicts, replication lag and slaves being out of sync with the master.

.. figure:: images/galerausecases1.png

In a typical instance of a Galera Cluster, applications can write to any node in the cluster and transaction commits, (RBR events), are then applied to all the servers, through certification-based replication.

Certification-based replication is an alternative approach to synchronous database replication, using group communication and transaction ordering techniques.

.. note:: For security and performance reasons, it's recommended that you run Galera Cluster on its own subnet.

.. toctree::
   :maxdepth: 2

   whatsnew
	  

--------------------
Node Initialization
--------------------
.. _`node-initialization`:

Galera Cluster for MySQL is not the same as a standard standalone MySQL database server.  You will need to install and configure additional software.  

This software runs on any unix-like operating system.  You can choose to build from source or to install using Debian- or RPM-based binary packages.  Once you have the software installed on your individual server, you must also configure the server to function as a node in your cluster. 

.. toctree::
   :maxdepth: 3
	      
   galerainstallation
   configuration
   dbconfiguration

------------------------
Cluster Initialization
------------------------
.. _`cluster-initialization`:

Once you have Galera Cluster installed and configured on your servers, you are ready to initialize the cluster for operation.  You do this by starting the cluster on the first node, then adding the remaining nodes to it.


.. toctree::
   :maxdepth: 3

   startingcluster
   testingcluster
   restartingcluster

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
