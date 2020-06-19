.. meta::
   :title: Methods for Monitoring a Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, monitoring, monitor, high availability
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`log`
      - :doc:`notification-cmd`
      - :doc:`monitoring-cluster`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`monitor`:

====================
Cluster Monitoring
====================

Occasionally, you may want or need to check on the status of the cluster. For instance, you may want to check the state of nodes. You may want to check for network connectivity problems amongst nodes.

There are four methods available in monitoring cluster activity and replication health: query status variables through a database client; check regularly related log files; use a monitoring application; or write a notification script.

- :doc:`monitoring-cluster`

  In addition to the standard status variables in MySQL, Galera Cluster provides a series of its own status variables. These will allow you to check node and cluster states, as well as replication health through the database client.

- :doc:`log`

  Queries entered through the database client will provide information on the current state of the cluster. However, to check its history for more systemic issues, you need to check the logs.  This section provides a guide to the Galera Cluster parameter used to configure database logging to ensure it records the information you need.

- :doc:`galera-manager`

  If you have an account with Amazon Web Services (AWS) for server hosting, you can use Galera Manager to create and configure easily Galera Clusters.  Additionally, Galera Manager provides a graphical user interface with charts for monitoring over one thousand cluster metrics: just configure it to track metrics you find most useful.

- :doc:`notification-cmd`

  Although checking logs and status variables may give you the information you need while logged into a node, getting information from them is a manual process.  Using the notification command, you can set the node to call a script in response to changes in cluster membership or node status.  You can use this to raise alerts and adjust load balances. You can use it in a script for any situation in which you need the infrastructure to respond to changes in the cluster.

You can also use Nagios for monitoring Galera Cluster.  For more information, see `Galera Cluster Nagios Plugin <https://www.fromdual.com/galera-cluster-nagios-plugin-en>`_

.. container:: bottom-links

   Related Documents

   - :doc:`log`
   - :doc:`notification-cmd`
   - :doc:`monitoring-cluster`


.. toctree::
   :maxdepth: 2
   :hidden:

   monitoring-cluster
   log
   galera-manager
   notification-cmd
   notification-cmd-example
