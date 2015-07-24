==========================
Using Docker on Linux
==========================
.. _`docker`:

Docker provides an open source platform for automatically deploying applications within software containers on Linux.  You may find it useful in portable deployment across numerous machines, testing applications that depend on Galera Cluster, or scripting the installation and configuration process.

Galera Cluster can run from within a Docker container.

---------------------------
Configuring the Container
---------------------------
.. _`configure-container`:

Images are the containers that Docker has available to run.  There are a number of base images available through `Docker Hub <https://registry.hub.docker.com>`_.  You can pull these down to your system through the ``docker`` command-line tool.

When Docker builds a new mage, it sources the ``Dockerfile`` to determine the steps that it needs to take in order to generate the image that you want to use.

This means that you can script the installation and configuration process: loading the needed configuration files, running updates and installing packages when the image is built through a single command.

.. code-block:: docker
		
   FROM ubuntu:14.04
   MAINTAINER your name <your.user@company.org>

   ENV DEBIAN_FRONTEND noninteractive
   
   RUN apt-get update 
   RUN apt-get install -y  software-properties-common
   RUN apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA 
   RUN add-apt-repository 'deb http://releases.galeracluster.com/ubuntu trusty main'

   RUN apt-get update 
   RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync

   COPY my.cnf /etc/mysql/my.cnf
   ENTRYPOINT ["mysqld"]

The example follows the installation process for running Galera Cluster from within a Docker container based on Ubuntu.  When you run the build command, ``docker`` pulls down the Ubuntu 14.04 image from Docker HUb, if it's needed, then runs each command in the ``Dockerfile`` to initialize the image for your use.

^^^^^^^^^^^^^^^^^^^^
Configuration File
^^^^^^^^^^^^^^^^^^^^
.. _`docker-my-cnf`:

Before you build the container, you will need to write the configuration file for the node.  The ``COPY`` command in the ``Dockerfile`` above copies ``my.cnf`` from the build directory into the container.  It must be ready at the time of the build. 

For the most part, the configuration file for a node running within a Docker container is the same as when the node is running on a standard Linux server.  However, you need to manually set any parameter that draws its default from the base system.

- :ref:`wsrep_node_address <wsrep_node_address>` Galera Cluster determines the default address from the IP address on the first network interface.  This interface is inaccessible from within the container, so you need to set it explicitly to ensure that the cluster can find node containers.

- :ref:`wsrep_node_name <wsrep_node_name>` Galera Cluster determines the default node name from the system hostname.  Docker containers have their own hostnames, distinct from that of the host system.

Changing the ``my.cnf`` file does not propagate into the container.  Whenever you need to make changes to the configuration file, run the build again to propagate the update into the container.

.. note:: Docker caches each step of the build and on rebuild only runs those steps that have changed since the last run.  For example, using the above ``Dockerfile``, if you rebuild an image after changing ``my.cnf``, Docker only runs the last two steps.  If you need Docker to rerun the entire build, use the ``--force-rm=true`` option.

  

-------------------------
Building the Container
-------------------------
.. _`building-the-container`:

The purpose of building a Docker container is to reduce the installation, configuration and deployment process for container nodes to a single command.  To manage this, you need to first create an image of the container in which you have Galera Cluster installed, configured and ready for use.

You can build a container node using the Docker command-line tool.

.. code-block:: console

   # docker build -t ubuntu:galera-node1 ./ 

When this command runs, Docker looks in the working direction, (here ``./``), for the ``Dockerfile``.  It then follows each command in the ``Dockerfile`` to build the image you want.  When the build is complete, you can view the addition among the available images:
   
.. code-block:: console

   # docker images
   
   REPOSITORY  TAG           IMAGE ID      CREATED        SIZE
   ubuntu      galera-node-1 53b97c3d7740  2 minutes ago  362.7 MB
   ubuntu      14.04         ded7cd95e059  5 weeks ago    185.5 MB

You now have a working node image available for use as a container.  You can launch it using the ``docker run`` command.  Repeat the build process on each server to create a node container image for Galera Cluster.  Update the container tag to help differentiate between them.

-------------------------
Deploying the Container
-------------------------
.. _`deploy-container`:

When you finish building the image, you're ready to launch the container for your Galera node.  You can start a container using the Docker command-line tool with the ``run`` argument.

.. code-block:: console

   # docker run -i -d --name Node1 --host node1 \
         -p 3306:3306 -p 4567:4567 -p 4568:4568 -p 4444:4444 \
	 -v /var/container_data/mysql:/var/lib/mysql \
	 ubuntu:galera-node1

In the example, Docker launches a pre-built Ubuntu container tagged as ``galera-node1``, which was built using the above ``Dockerfile``.  The ``ENTRYPOINT`` parameter is set to ``/bin/mysqld``, so the container launches the database server on start.

.. note:: The above command starts a container node meant to be attached to an existing cluster.  If you are starting the first node in a cluster, append the argument ``--wsrep-new-cluster`` to the end of the command.
	  
^^^^^^^^^^^^^^^^^^^
Firewall Settings
^^^^^^^^^^^^^^^^^^^
.. _`docker-firewall`:

When you launch the Docker container, (``docker run`` above), the series of ``-p`` options connect the ports on the host system to those in the container.  When the container is launched this way, nodes in the container have the same level of access to the network as the node would when running on the host system.

Use these settings when you only run one container to the server.  If you are running multiple containers to the server, you will need a load balancer to dole the incoming connections out to the individual nodes.

For more information on configuring the firewall for Galera Cluster, see :doc:`firewallsettings`.

^^^^^^^^^^^^^^^^^^
Persistent Data
^^^^^^^^^^^^^^^^^^
.. _`docker-data`:

Docker containers are not meant to carry persistent data.  When you close the container, the data it carries is lost.  When you first launch the container with the ``docker run`` command, you can link volumes in the container with directories on the host file system, using the ``-v`` option.

In the above example, the ``-v`` argument connections the ``/var/container_data/mysql`` directory to ``/var/lib/mysql`` in the container.  This replaces the local datadir within the container with a symbolic link to the host system, ensuring that you don't lose data when the container restarts.

^^^^^^^^^^^^^^^^^^^^
Database Client
^^^^^^^^^^^^^^^^^^^^

Once you have the container node running, you can execute additional commands on the container using the ``docker exec`` command with the container name given above for the ``--name`` parameter.

For example, if you want access to the database client, run the following command:

.. code-block:: console

   # docker exec -ti Node1 /bin/mysql -u root -p
