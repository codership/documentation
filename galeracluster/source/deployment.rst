---------------
Deployment
---------------
.. _`deployment`:

When you start Galera Cluster, you do so by initializing a series of nodes that are configured to communicate with and replicate into each other.  Each node in the cluster is a particular instance of a MySQL, MariaDB, or Percona XtraDB database server.  How your application servers interact with the cluster and how you manage the load and the individual nodes represents your deployment.

- :doc:`deploymentvariants`

  Galera Cluster provides synchronous multi-master replication.  This means that the nodes collectively operate as a single database server that listens across many interfaces.  This chapter provides various examples of how you might deploy the cluster in relation to your application servers.

- :doc:`loadbalancing`

  In high availability environments, you may sometimes encounter situations where certain nodes are put under a much greater load than others.  If you find yourself in this situation, you may find some benefit in configuring and deploying load balancers between your application servers and Galera Cluster.  Doing so allows you to distribute client connections more evenly between the nodes, ensuring better performance.

  This chapter provides guides to installing, configuring and deploying HAProxy, Pen and Galera Load Balancer, allowing you to better manage traffic between clients and the cluster.
  
  
- :doc:`containers`

  When using the standard deployment methods of Galera Cluster, the nodes run directly on the Linux or FreeBSD server hardware.  By contrast, with container deployments the nodes run in containerized virtual environments on the server.  You may find this useful in building portable deployments across numerous machines, when testing applications or scripting installations, or when isolating processes for security.

  This chapter provides guides to installing, configuring and deploying Galera Cluster nodes in container instances using FreeBSD Jails and Docker.


  
.. toctree::
   :maxdepth: 2
   :hidden:
   
   deploymentvariants
   loadbalancing
   containers
      
