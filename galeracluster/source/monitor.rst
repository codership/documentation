------------------------------
Cluster Monitoring
------------------------------
.. _`monitor`:

Occasionally, you may want or need to check on the status of the cluster.  For instance, to check the health of nodes or monitor for network connectivity issues between the nodes.  There are three methods available in monitoring cluster activity and replication health: querying status variables through the database client, using the notification script, or through a third-party monitoring application, such as Nagios.

- :doc:`monitoringthecluster`

  In addition to those that are standard in MySQL, Galera Cluster provides a series of status variables, which allow you to check node and cluster state as well as replication health through the database client.

- :doc:`log`

  Queries sent through the database client provide information on the current state of the cluster, but to check its history for more systemic issues, you need to use the logs.  This chapter provides a guide to Galera Cluster parameter used to configure database logging to ensure that you get the information you need.

  
- :doc:`notificationcmd`

  While checking logs and status variables may give you the information you need while on the node, getting information from them remains a manual process.  Using the notification command, you can set the node to call a script in response to changes in cluster membership or node status.  You can use this to raise alerts, adjust load balances or script for any other situation where you need your infrastructure to respond to changes in the cluster.
  
.. note:: You can also use Nagios for monitoring Galera Cluster.  For more information, see `Galera Cluster Nagios Plugin <http://www.fromdual.com/galera-cluster-nagios-plugin-en>`_

.. toctree::
   :maxdepth: 2
   :hidden:

   monitoringthecluster
   log
   notificationcmd
