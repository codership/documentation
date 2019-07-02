.. cssclass:: tutorial-article
.. _`getting-started-docker-pt2`:

===========================================
Getting Started Galera with Docker, Part 2
===========================================

.. rst-class:: list-stats

   Length:  654 words; Writer: Erkan Yanar; Published: May 12, 2015; Topic: Container; Level: Intermediate


In the previous article of this series, we described how to run a multi-node Galera Cluster on a single Docker host.

In this article, we will describe how to deploy Galera Cluster over multiple Docker hosts.

By design, Docker containers are reachable using port-forwarded TCP ports only, even if the containers have IP addresses. So we will set up port forwarding for all TCP ports that are required for Galera to operate.

The following TCP port are used by Galera:

.. code-block:: console

   3306-MySQL port
   4567-Galera Cluster
   4568-IST port
   4444-SST port

Before we start, we need to stop enforcing AppArmor for Docker:

.. code-block:: console

   $ aa-complain /etc/apparmor.d/docker


------------------------------------------------------
Building a Multi-Node Cluster using the Default Ports
------------------------------------------------------

Building a multi-node cluster using the default ports is not complicated. Besides mapping the ports 1:1, we also need to set `–wsrep-node-address` to the IP address of the host.

We assume following 3 nodes

.. code-block:: console

   nodea 10.10.10.10
   nodeb 10.10.10.11
   nodec 10.10.10.12

A simple cluster setup would look like this:

.. code-block:: console

   nodea$ docker run -d -p 3306:3306 -p 4567:4567 -p 4444:4444 -p 4568:4568
   --name nodea erkules/galera:basic
   --wsrep-cluster-address=gcomm:// --wsrep-node-address=10.10.10.10
   nodeb$ docker run -d -p 3306:3306 -p 4567:4567 -p 4444:4444 -p 4568:4568
   --name nodeb erkules/galera:basic
   --wsrep-cluster-address=gcomm://10.10.10.10 --wsrep-node-address=10.10.10.11
   nodec$ docker run -d -p 3306:3306 -p 4567:4567 -p 4444:4444 -p 4568:4568
   --name nodec erkules/galera:basic
   --wsrep-cluster-address=gcomm://10.10.10.10 --wsrep-node-address=10.10.10.12
   nodea$ docker exec -t nodea mysql -e 'show status like "wsrep_cluster_size"'

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size |     3 |
   +--------------------+-------+

In this example, we used the image from the previous blog post. Docker is going to download the image if it is not already present on the node.


------------------------------------------------------
Building a Multi-Node Cluster using Non-Default Ports
------------------------------------------------------

In the long run, we may want to start more than one instance of Galera on a host in order to run more than one Galera cluster using the same set of hosts.

For the purpose, we set Galera Cluster to use non-default ports and then map MySQL’s default port to 4306:

.. code-block:: console

   MySQL port 3306 is mapped to 4306
   Galera Cluster port 4567 is changed to 5567
   Galera IST port 4568 is changed to 5678
   Galera SST port 4444 is changed to 5444

The docker command line part is straightforward. Please note the additional command-line options used to configure Galera

.. code-block:: console

   nodea$ docker run -d -p 4306:3306 -p 5567:5567 -p 5444:5444 -p 5568:5568
   --name nodea erkules/galera:basic --wsrep-cluster-address=gcomm://
   --wsrep-node-address=10.10.10.10:5567 --wsrep-sst-receive-address=10.10.10.10:5444
   --wsrep-provider-options="ist.recv_addr=10.10.10.10:5568"
   nodeb$ docker run -d -p 4306:3306 -p 5567:5567 -p 5444:5444 -p 5568:5568
   --name nodeb erkules/galera:basic --wsrep-cluster-address=gcomm://10.10.10.10:5567
   --wsrep-node-address=10.10.10.11:5567 --wsrep-sst-receive-address=10.10.10.11:5444
   --wsrep-provider-options="ist.recv_addr=10.10.10.11:5568"
   nodec$ docker run -d -p 4306:3306 -p 5567:5567 -p 5444:5444 -p 5568:5568
   --name nodec erkules/galera:basic --wsrep-cluster-address=gcomm://10.10.10.10:5567
   --wsrep-node-address=10.10.10.12:5567 --wsrep-sst-receive-address=10.10.10.12:5444
   --wsrep-provider-options="ist.recv_addr=10.10.10.12:5568"
   nodea$ docker exec -t nodea mysql -e 'show status like "wsrep_cluster_size"'

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size |     3 |
   +--------------------+-------+

The following Galera Cluster configuration options are used to specify each port:

.. code-block:: console

   4567 Galera Cluster is configured using `–wsrep-node-address`
   4568 IST port is configured using `–wsrep-provider-options=”ist.recv_addr=”`
   4444 SST port is configured using `–wsrep-sst-receive-address`

---------
Summary
---------

In this blog post, we described how to run Galera Cluster inside Docker on multiple hosts, even with non-standard ports. It is also possible to use solutions such as weave, socketplane.io and flannel that provide a multi-host network for the containers.
