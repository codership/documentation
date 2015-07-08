==========================
Using Docker on Linux
==========================
.. _`docker`:

Docker provides an open source platform for automatically deploying applications within software containers on Linux.  You may find it useful in portable deployment across numerous machines, development testing or automatic builds.

Galera Cluster can run from within a Docker container.

---------------------------
Configuring the Container
---------------------------
.. _`configure-container`:

There are two configuration files that you need to create to run Galera Cluster on Docker: ``my.cnf`` and ``Dockerfile``.  Place both of these in the build directory for your container.


^^^^^^^^^^^^
``my.cnf``
^^^^^^^^^^^^
.. _`my-cnf`:

Galera Cluster sources the ``my.cnf`` configuration file when the database server starts, regardless of whether or not the server is running from within a container.  When you write the configuration file for a container, you follow the same conventions as you would use in the standard deployment for a host operating system.  For example:

.. code-block:: ini

   [mysqld]
   user=mysql
   bind-address=0.0.0.0

   # Cluster Options
   wsrep_provider=/usr/lib/galera/libgalera_smm.so
   wsrep_cluster_address="gcomm://192.168.1.1, 192.168.1.2, 192.16.1.3"
   wsrep_node_address="192.168.1.1"
   wsrep_node_name="node1"
   wsrep_cluster_name="example_cluster"

   # InnoDB Options
   default_storage_engine=innodb
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0

   # SST
   wsrep_sst_method=rsync


^^^^^^^^^^^^^^^^^^^^^^^^^^
``Dockerfile``
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`dockerfile`:

Docker images are the containers it has available for launch.  There are a number of base images available through `Docker Hub <https://registry.hub.docker.com>`_.  You can pull these down to your system through the ``docker`` command-line tool.

When Docker builds a new image, it sources the ``Dockerfile`` to determine the steps that it needs to take in order to generate the image that you want to use.  To complete automate deployment, this means everything that your system needs to start ready for use from the base operating system, to loading configuration files, to running updates and installations through the package manager.

.. code-block:: docker
		
   FROM ubuntu:14.04
   MAINTAINER your name <your.user@company.org>

   ENV DEBIAN_FRONTEND noninteractive
   
   RUN apt-get update \
   apt-get install -y  software-properties-common \
   apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 BC19DDBA \
   add-apt-repository 'deb http://releases.galeracluster.com/ubuntu trusty main'

   RUN apt-get update \
   apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync

   COPY my.cnf /etc/mysql/my.cnf
   ENTRYPOINT ["mysqld"]

The example follows the installation process for running Galera Cluster from within a Docker container based on Ubuntu.  When you run the build command, ``docker`` pulls down the Ubuntu 14.04 image from Docker HUb, if it's needed, then runs each command in the ``Dockerfile`` to initialize the image for your use.

.. note:: As an alternative to the ``Dockerfile`` above, you can also pull down a pre-built image from Docker Hub.  To do so, run the following command:

	  .. code-block:: console

	     # docker pull erkules/galera:basic

-------------------------
Building the Container
-------------------------
.. _`building-the-container`:

The purpose of building a Docker container is to reduce the installation, configuration and deployment process for container nodes to a single command.  To manage this, you need to first create an image of the container in which you have Galera Cluster installed, configured and ready for use.

.. note:: For Debian- and Ubuntu-based distributions, there is another package that uses the name ``docker``.  Substitute ``docker.io`` for the package name and command-line tool on these distributions.

You can build a container node using the Docker command-line tool.

.. code-block:: console

   # docker build -t centos:galera ./ 

When this command runs, Docker looks in the working direction, (here ``./``), for the ``Dockerfile``.  It then follows each command in the ``Dockerfile`` to build the image you want.  When the build is complete, you can view the addition among the available images:
   
.. code-block:: console

   # docker images
   
   REPOSITORY  TAG      IMAGE ID      CREATED        SIZE
   centos      galera   53b97c3d7740  2 minutes ago  362.7 MB
   centos      centos7  ded7cd95e059  5 weeks ago    185.5 MB

You now have a working node image available for use as a container.  You can launch it using the ``docker run`` command.
   
      

-------------------------
Deploying the Container
-------------------------
.. _`deploy-container`:

When you finish building images, (or pulling them down from Docker Hub), you're ready to launch containers for your Galera nodes.  You can start a container using the Docker command-line tool with the ``run`` parameter.

.. code-block:: console

   # docker run -i -d --name Node1 --host node1 \
         -p 3306:3306 -p 4567:4567 -p 4568:4568 -p 4444:4444 \
	 erkules/galera:basic

This Docker image uses the database server as an ``ENTRYPOINT`` parameter.  This means that it runs ``/bin/mysqld`` on start.  Meaning that the command launches a container then starts Galera Cluster.

.. note:: The above command starts a container node meant to attach to an existing cluster.  If you are starting the first node in a cluster, append the argument ``--wsrep-new-cluster`` to the end of the command.

Once you have the container node running, you can execute additional commands on the container using the ``docker exec`` command with the container name given above for the ``--name`` parameter.  For example, if you want access to the database client, run the following command:

.. code-block:: console

   # docker exec -ti Node1 /bin/mysql -u root -p
