------------------------------
Cluster Monitoring
------------------------------
.. _`monitor`:

Occasionally, you may want or need to check on the status of the cluster. For instance, you may want to check the state of nodes. You may want to check for network connectivity problems amongst nodes.  

There are three methods available in monitoring cluster activity and replication health: query status variables through the database client; use a notification script; or through a third-party monitoring application (e.g., Nagios).

- :doc:`monitoringthecluster`

  In addition to the standard status variables in MySQL, Galera Cluster provides a series of its own status variables. These will allow you to check node and cluster states, as well as replication health through the database client.

- :doc:`log`

  Queries entered through the database client will provide information on the current state of the cluster. However, to check its history for more systemic issues, you need to check the logs.  This section provides a guide to the Galera Cluster parameter used to configure database logging to ensure it records the information you need.

  
- :doc:`notificationcmd`

  Although checking logs and status variables may give you the information you need while logged into a node, getting information from them is a manual process.  Using the notification command, you can set the node to call a script in response to changes in cluster membership or node status.  You can use this to raise alerts and adjust load balances. You can use it in a script for any situation in which you need the infrastructure to respond to changes in the cluster.
  
.. note:: You can also use Nagios for monitoring Galera Cluster.  For more information, see `Galera Cluster Nagios Plugin <http://www.fromdual.com/galera-cluster-nagios-plugin-en>`_

.. toctree::
   :maxdepth: 2
   :hidden:

   monitoringthecluster
   log
   notificationcmd
