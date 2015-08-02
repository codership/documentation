=====================
 Using Galera Cluster
=====================
.. _`admin-guide`:

Once you become familiar with the basics of how Galera Cluster works, consider how it can work for you.

----------------------------------------
Working with the Cluster
----------------------------------------
.. _`working-cluster`:

How do you recover failed nodes or a :term:`Primary Component`?  How to secure communications between the cluster nodes?  How do you back up cluster data?  With your cluster up and running, you can begin to manage its particular operations, monitor for and recover from issues, and maintain security.

.. toctree::
   :maxdepth: 2

   nodeprovisioning
   sst
   pcrecovery
   quorumreset
   managingfc
   autoeviction
   schemaupgrades
   upgrading
   scriptablesst
   loadbalancing
   arbitrator
   backingupthecluster

---------------
Deployment
---------------
.. _`deployment`:

.. toctree::
   :maxdepth: 2
   
   deploymentvariants
   docker
   jails
      
------------------------------
Monitor
------------------------------
.. _`monitor`:

There are three approaches to monitoring cluster activity and replication health: directly off the database client, using the notification script for Galera Cluster, or through a third-party monitoring application, such as Nagios.

.. toctree::
   :maxdepth: 2

   monitoringthecluster
   notificationcmd

.. note:: You can also use Nagios for monitoring Galera Cluster.  For more information, see `Galera Cluster Nagios Plugin <http://www.fromdual.com/galera-cluster-nagios-plugin-en>`_.

------------------------
Security
------------------------
.. _`security`:


.. toctree::
   :maxdepth: 2

   firewallsettings
   ssl


---------------------------
Migration
---------------------------


Bear in mind that there are certain key differences between how a standalone instance of the MySQL server works and the Galera Cluster wsrep database server.  This is especially important if you plan to install Galera Cluster over an existing MySQL server, preserving its data for replication.

.. toctree::
   :maxdepth: 2

   limitations
   migration

.. seealso:: For more information on the installation and basic management of Galera Cluster, see the :doc:`Getting Started Guide <gettingstarted>`.

   
