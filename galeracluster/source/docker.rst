==========================
Using Docker
==========================
.. _`docker`:

Docker provides an open source platform for automatically deploying applications within software containers.

Galera Cluster can run from within a Docker container.  You may find it useful in portable deployment across numerous machines, testing applications that depend on Galera Cluster, or scripting the installation and configuration process.

.. note:: This guide assumes that you are only running one container node per server.  For more information on running multiple nodes per server, see Getting Started Galera with Docker, `Part I <http://galeracluster.com/2015/05/getting-started-galera-with-docker-part-1/>`_ and `Part II <http://galeracluster.com/2015/05/getting-started-galera-with-docker-part-2-2/>`_.


---------------------------
Configuring the Container
---------------------------
.. _`configure-container`:

Images are the containers that Docker has available to run.  There are a number of base images available through `Docker Hub <https://registry.hub.docker.com>`_.  You can pull these down to your system through the ``docker`` command-line tool.  You can also build new images.

When Docker builds a new image, it sources a ``Dockerfile`` to determine the steps that it needs to take in order to generate the image that you want to use. What this means that you can script the installation and configuration process: loading the needed configuration files, running updates and installing packages when the image is built through a single command.

.. code-block:: Dockerfile

   # Galera Cluster Dockerfile
   FROM ubuntu:14.04
   MAINTAINER your name <your.user@example.org>

   ENV DEBIAN_FRONTEND noninteractive

   RUN apt-get update
   RUN apt-get install -y  software-properties-common
   RUN apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA
   RUN add-apt-repository 'deb http://releases.galeracluster.com/galera-3/ubuntu trusty main'
   RUN add-apt-repository 'deb http://releases.galeracluster.com/mysql-wsrep-5.6/ubuntu trusty main'


   RUN apt-get update
   RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync

   COPY my.cnf /etc/mysql/my.cnf
   ENTRYPOINT ["mysqld"]

The example follows the installation process for running Galera Cluster from within a Docker container based on Ubuntu.  When you run the build command, Docker pulls down the Ubuntu 14.04 image from Docker Hub, if it's needed, then it runs each command in the ``Dockerfile`` to initialize the image for your use.

^^^^^^^^^^^^^^^^^^^^
Configuration File
^^^^^^^^^^^^^^^^^^^^
.. _`docker-my-cnf`:

Before you build the container, you need to write the configuration file for the node.  The ``COPY`` command in the ``Dockerfile`` above copies ``my.cnf`` from the build directory into the container.

For the most part, the configuration file for a node running within Docker is the same as when the node is running on a standard Linux server.  But, there are some parameters that draw their defaults from the base system.  These you need to set manually, as Docker cannot access the host system.

- :ref:`wsrep_node_address <wsrep_node_address>` The node determines the default address from the IP address on the first network interface.  Containers cannot see the network interfaces on the host system.  You need to set this parameter to ensure that the cluster is given the correct IP address for the node.

- :ref:`wsrep_node_name <wsrep_node_name>`  The node determines the default name from the system hostname.  Containers have their own hostnames distinct from the host system.

Changing the ``my.cnf`` file does not propagate into the container.  Whenever you need to make changes to the configuration file, run the build again to create a new image with the updated file.  Docker caches each step of the build and on rebuild only runs those steps that have changed since the last run.  For example, using the above ``Dockerfile``, if you rebuild an image after changing ``my.cnf``, Docker only runs the last two steps.

.. note:: If you need Docker to rerun the entire build, use the ``--force-rm=true`` option.



-----------------------------
Building the Container Image
-----------------------------
.. _`building-the-container`:

Building the image reduces the node installation, configuration and deployment process to a single command.  This creates a server instance where Galera Cluster is already installed, configured and ready to start.

You can build a container node using the ``docker`` command-line tool.

.. code-block:: console

   # docker build -t ubuntu:galera-node1 ./

When this command runs, Docker looks in the working directory, (here ``./``), for the ``Dockerfile``.  It then follows each command in the ``Dockerfile`` to build the image you want.  When the build is complete, you can view the addition among the available images:

.. code-block:: console

   # docker images

   REPOSITORY  TAG           IMAGE ID      CREATED        SIZE
   ubuntu      galera-node-1 53b97c3d7740  2 minutes ago  362.7 MB
   ubuntu      14.04         ded7cd95e059  5 weeks ago    185.5 MB

You now have a working node image available for use as a container.  You can launch it using the ``docker run`` command.  Repeat the build process on each server to create a node container image for Galera Cluster.

Update the container tag to help differentiate between them.  That is,

.. code-block:: console

   [root@node2]# docker build -t ubuntu:galera-node2 ./
   [root@node3]# docker build -t ubuntu:galera-node3 ./

-------------------------
Deploying the Container
-------------------------
.. _`deploy-container`:

When you finish building the image, you're ready to launch the node container.  For each node start the container using the Docker command-line tool with the ``run`` argument.

.. code-block:: console

   # docker run -i -d --name Node1 --host node1 \
         -p 3306:3306 -p 4567:4567 -p 4568:4568 -p 4444:4444 \
	 -v /var/container_data/mysql:/var/lib/mysql \
	 ubuntu:galera-node1

In the example, Docker launches a pre-built Ubuntu container tagged as ``galera-node1``, which was built using the above ``Dockerfile``.  The ``ENTRYPOINT`` parameter is set to ``/bin/mysqld``, so the container launches the database server on start.

Update the ``--name`` option for each node container you start.

.. note:: The above command starts a container node meant to be attached to an existing cluster.  If you are starting the first node in a cluster, append the argument ``--wsrep-new-cluster`` to the end of the command.  For more information, see :doc:`startingcluster`.


^^^^^^^^^^^^^^^^^^^
Firewall Settings
^^^^^^^^^^^^^^^^^^^
.. _`docker-firewall`:

When you launch the Docker container, (with ``docker run`` above), the series of ``-p`` options connect the ports on the host system to those in the container.  When the container is launched this way, nodes in the container have the same level of access to the network as the node would when running on the host system.

Use these settings when you only run one container to the server.  If you are running multiple containers to the server, you will need a load balancer to dole the incoming connections out to the individual nodes.

For more information on configuring the firewall for Galera Cluster, see :doc:`firewallsettings`.

^^^^^^^^^^^^^^^^^^
Persistent Data
^^^^^^^^^^^^^^^^^^
.. _`docker-data`:

Docker containers are not meant to carry persistent data.  When you close the container, the data it carries is lost.  To avoid this, you can link volumes in the container with directories on the host file system, using the ``-v`` option when you launch the container.

In the example, (that is, ``docker run`` above), the ``-v`` argument connects the ``/var/container_data/mysql/`` directory to ``/var/lib/mysql/`` in the container.  This replaces the local datadir inside the container with a symbolic link to a directory on the host system, ensuring that you don't lose data when the container restarts.

^^^^^^^^^^^^^^^^^^^^
Database Client
^^^^^^^^^^^^^^^^^^^^

Once you have the container node running, you can execute additional commands on the container using the ``docker exec`` command with the container name given above for the ``--name`` parameter.

For example, if you want access to the database client, run the following command:

.. code-block:: console

   # docker exec -ti Node1 /bin/mysql -u root -p
