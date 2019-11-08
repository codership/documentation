.. meta::
   :title: Galera Cluster Deployment
   :description:
   :language: en-US
   :keywords: galera cluster, deployment, containers, load balancing
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


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

      - :doc:`containers`
      - :doc:`Deployment Variants <deployment-variants>`
      - :doc:`load-balancing`

      Related Articles


.. cssclass:: library-document
.. _`deployment`:

=============
Deployment
=============

When you start Galera Cluster, you have to do so by initializing a series of nodes that are configured to communicate with each other and to replicate each other.  Each node in the cluster is a particular instance of a MySQL, MariaDB, or Percona XtraDB database server.  How your application servers interact with the cluster and how you manage the load and the individual nodes represents your deployment.

:doc:`deployment-variants`

Galera Cluster provides synchronous multi-master replication.  This means that the nodes collectively operate as a single database server that listens across many interfaces.  This section provides various examples of how you might deploy a cluster in relation to your application servers.

:doc:`load-balancing`

In high availability environments, you may sometimes encounter situations in which some nodes have a much greater load of traffic than others.  If you discover such a situation, there may be some benefit in configuring and deploying load balancers between your application servers and Galera Cluster.  Doing so will allow you to distribute client connections more evenly between the nodes, ensuring better performance.

This section provides guides to installing, configuring and deploying HAProxy, Pen and Galera Load Balancer, helping you to manage traffic between clients and the cluster.


:doc:`containers`

When using the standard deployment methods of Galera Cluster, nodes run directly on the  server hardware -- interacting directly with the operating system (i.e., Linux, FreeBSD).  By contrast, with container deployments nodes run in containerized virtual environments on the server.  You may find containers useful in building portable deployments across numerous machines, when testing applications or scripting installations, or when isolating processes for security.

This section provides guides to installing, configuring and deploying Galera Cluster nodes in container instances using FreeBSD Jails and Docker.



.. toctree::
   :maxdepth: 2
   :hidden:

   deployment-variants
   load-balancing
   containers



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
