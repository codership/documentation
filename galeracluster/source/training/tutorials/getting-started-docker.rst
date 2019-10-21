.. meta::
   :title: Getting Started Galera with Docker, Part 1
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../../kb/trouble/index>`
         - :doc:`Best Practices <../../kb/best/index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <./index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: bull-head

         Related Documents

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: tutorial-article
.. _`getting-started-docker`:

===================================
Getting Started Galera with Docker
===================================

.. rst-class:: list-stats

   Length: 1416 words; Writer: Erkan Yanar; Published: May 6, 2015; Topic: Container; Level: Intermediate

Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications. Consisting of Docker Engine, a portable, lightweight runtime and packaging tool, and Docker Hub, a cloud service for sharing applications and automating workflows, Docker enables apps to be quickly assembled from components and eliminates the friction between development, QA, and production environments. As a result, it can ship faster and run the same app, unchanged, on laptops, data center VMs, and any cloud.

let's first look at how to build a basic Docker Image, which we will extend later. Then we'll deploy on a test cluster on a local machine. The examples here have been tested on Ubuntu 14.04 with Docker 1.5.


.. rst-class:: rubric-1
.. rubric:: Build a Basic Docker Image

In Docker, Dockerfiles are used to describe the Docker images we are going to use to start our Galera Cluster. We are using the following Dockerfile:

.. code-block:: console

   FROM ubuntu:14.04
   MAINTAINER Erkan Yanar <erkan.yanar@linsenraum.de>
   ENV DEBIAN_FRONTEND noninteractive

   RUN apt-get update
   RUN apt-get install -y software-properties-common
   RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 BC19DDBA
   RUN add-apt-repository 'deb https://releases.galeracluster.com/ubuntu trusty main'
   RUN apt-get update
   RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync lsof
   COPY my.cnf /etc/mysql/my.cnf
   ENTRYPOINT ["mysqld"]

This image builds on top of the Ubuntu 14.04 image. It simply installs Galera using the Codership repository and copies the my.cnf over.

The `my.cnf` is quite simple.

.. code-block:: console

   [mysqld]
   user = mysql
   bind-address = 0.0.0.0
   wsrep_provider = /usr/lib/galera/libgalera_smm.so
   wsrep_sst_method = rsync
   default_storage_engine = innodb
   binlog_format = row
   innodb_autoinc_lock_mode = 2
   innodb_flush_log_at_trx_commit = 0
   query_cache_size = 0
   query_cache_type = 0

A pre-built image is available from Docker Hub. You can pull it by running:

.. code-block:: console

   sudo docker pull erkules/galera:basic

(All commands in this article need to run as root.)


.. rst-class:: rubric-1
.. rubric:: Deploy on a Test Cluster on a Local Machine

Next, we are going to start a Galera Cluster on the local host. The instructions below are for demonstration purposes only and will not work when deploying on multiple hosts, as networking between containers needs to be set up. Configuring Docker networking across multiple hosts will be described in a following post.


.. rst-class:: rubric-1
.. rubric:: Starting a Cluster

There have been a number of blog posts showing how to start Galera Cluster on a single host. This post is going to show the simplest way to do that in Docker by using simple commands, which will not work for a multi-host installation. First, if working on Ubuntu, we need to put AppArmor’s Docker profile in complain mode in advance.

.. code-block:: console

   $ sudo aa-complain /etc/apparmor.d/docker

Then we can start the first Galera node by instructing Docker to create a container and run mysqld in it.

.. code-block:: console

   $ sudo docker run --detach=true --name node1 -h node1 erkules/galera:basic --wsrep-cluster-name=local-test --wsrep-cluster-address=gcomm://

In addition to defining the internal name and hostname, we also define the name of the cluster.

MySQLs error log is not configured explicitly, and Docker records STDOUT and STDERR of every container. So, using `sudo docker logs node1`, the log output from the first node can be displayed without having to enter the container.
For the next two containers, we use a simple Docker trick. The `–link` option writes the name and the IP of host1 into the `/etc/hosts` file of the container. This way, we can connect the remaining nodes to node1 without having to obtain its IP from its container.

.. code-block:: console

   $ sudo docker run --detach=true --name node2 -h node2 --link node1:node1 erkules/galera:basic --wsrep-cluster-name=local-test --wsrep-cluster-address=gcomm://node1
   $ sudo docker run --detach=true --name node3 -h node3 --link node1:node1 erkules/galera:basic --wsrep-cluster-name=local-test --wsrep-cluster-address=gcomm://node1

Now we have a running Galera cluster. We can check the number of nodes in the Cluster by running the mysql client from inside one of the containers:

.. code-block:: console

   $ sudo docker exec -ti node1 mysql -e 'show status like "wsrep_cluster_size"'

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size |     3 |
   +--------------------+-------+

We built a simple Galera Cluster on one host, without using SSH and without the need to configure any IP addresses. This setup does not support restarting the container |---| you should remove the container and recreate it instead.


.. rst-class:: rubric-1
.. rubric:: Deploying Galera on Mutiple Docker Hosts

Now let's discuss how to deploy Galera on multiple Docker hosts. By design, Docker containers are reachable using port-forwarded TCP ports only, even if the containers have IP addresses. So we will set up port forwarding for all TCP ports that are required for Galera to operate.

The following TCP port are used by Galera:

.. code-block:: console

   3306-MySQL port
   4567-Galera Cluster
   4568-IST port
   4444-SST port

Before we start, we need to stop enforcing AppArmor for Docker:

.. code-block:: console

   $ aa-complain /etc/apparmor.d/docker


.. rst-class:: rubric-1
.. rubric:: Building a Multi-Node Cluster using the Default Ports

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


.. rst-class:: rubric-1
.. rubric:: Building a Multi-Node Cluster using Non-Default Ports

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


.. rst-class:: rubric-1
.. rubric:: Summary

That concludes this tutorial. As you can see, it's easy to run Galera on Docker and inside Docker on multiple hosts, even with non-standard ports. It is also possible to use solutions such as weave, socketplane.io and flannel that provide a multi-host network for the containers.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
