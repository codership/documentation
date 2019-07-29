.. meta::
   :title: Using Docker with Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, containers, docker, container image, firewall
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :doc:`Firewall Settings <firewall-settings>`
      - :ref:`wsrep_node_address <wsrep_node_address>`
      - :ref:`wsrep_node_name <wsrep_node_name>`

      .. cssclass:: bull-head

         Related Articles

      - :doc:`Starting a Cluster <../training/tutorials/starting-cluster>`


.. cssclass:: library-document
.. _`docker`:

==============
Using Docker
==============

Docker provides an open source platform for automatically deploying applications within software containers.

Galera Cluster can run from within a such a container, within Docker.  You may find containers useful in portable deployment across numerous machines, testing applications that depend on Galera Cluster, or scripting the installation and configuration process.

.. note:: This guide assumes that you are only running one container node per server.  For more information on running multiple nodes per server, see *Getting Started Galera with Docker, `Part I <https://galeracluster.com/2015/05/getting-started-galera-with-docker-part-1/>`_ and `Part II <https://galeracluster.com/2015/05/getting-started-galera-with-docker-part-2-2/>`_.*


.. _`configure-container`:
.. rst-class:: rubric-1
.. rubric:: Configuring a Container

Images are the containers that Docker has available to run.  There are a number of base images available through `Docker Hub <https://registry.hub.docker.com>`_.  You can pull these to your system through the ``docker`` command-line tool.  You can also build new images.

When Docker builds a new image, it sources a ``Dockerfile`` to determine the steps that it needs to take in order to generate the image you want to use. This means you can script the installation and configuration process.  Basically, such a script would need to load the needed configuration files, run updates, and install packages when the image is built---all through a single command.  Below is an example of how you might write such a script:

.. code-block:: Dockerfile

   # Galera Cluster Dockerfile
   FROM ubuntu:14.04
   MAINTAINER your name <your.user@example.org>

   ENV DEBIAN_FRONTEND noninteractive

   RUN apt-get update
   RUN apt-get install -y  software-properties-common
   RUN apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA
   RUN add-apt-repository 'deb https://releases.galeracluster.com/galera-3/ubuntu trusty main'
   RUN add-apt-repository 'deb https://releases.galeracluster.com/mysql-wsrep-5.6/ubuntu trusty main'


   RUN apt-get update
   RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync

   COPY my.cnf /etc/mysql/my.cnf
   ENTRYPOINT ["mysqld"]

This example follows the installation process for running Galera Cluster from within a Docker container running on Ubuntu.  When you run the build command, Docker pulls down the Ubuntu 14.04 image from Docker Hub, if it's needed. It then runs each command in the ``Dockerfile`` to initialize the image for your use.


.. _`docker-my-cnf`:
.. rst-class:: rubric-2
.. rubric:: Configuration File

Before you build the container, you need to create the configuration file for the node.  The ``COPY`` command in the ``Dockerfile`` example above copies ``my.cnf``, the MySQL configuration file, from the build directory into the container.

For the most part, the configuration file for a node running within Docker is the same as when the node is running on a standard Linux server.  However, there are some parameters that may not be included in the MySQL configuration file and instead use the default values from the underlying database system---or they may have been set manually, on-the-fly using the ``SET`` statement.  For these parameters, since Docker can't access the host system, you may need to set them, manually.

- :ref:`wsrep_node_address <wsrep_node_address>`: A node will determine the default address from the IP address on the first network interface.  Containers cannot see the network interfaces on the host system.  Therefore, you will need to set this parameter to ensure the cluster is given the correct IP address for the node.

- :ref:`wsrep_node_name <wsrep_node_name>`:  A node will determine the default host name from the system hostname.  Containers have their own hostnames distinct from the host system.

Changes to the ``my.cnf`` file will not propagate into an existing container.  Therefore, whenever you make changes to the configuration file, run the build again to create a new image with the updated configuration file.  Docker caches each step of the build and only runs those steps that have changed when rebuilding.  For example, using the ``Dockerfile`` example above, if you rebuild an image after changing ``my.cnf``, Docker will run only  the last two steps.

.. note:: If you need Docker to rerun the entire build, use the ``--force-rm=true`` option.



.. _`building-the-container`:
.. rst-class:: rubric-1
.. rubric:: Building a Container Image

Building an image simplifies everyting---the node installation, the configuration and the deployment process---by reducing it to a single command.  It will create a server instance where Galera Cluster is already installed, configured and ready to start.

You can build a container node using the ``docker`` command-line tool like so:

.. code-block:: console

   # docker build -t ubuntu:galera-node1 ./

When this command runs, Docker looks in the current working directory, (i.e., ``./``), for the ``Dockerfile``.  It then follows each command in the ``Dockerfile`` to build the image.  When the build is complete, you can view the addition among the available images by executing the following:

.. code-block:: console

   # docker images

   REPOSITORY  TAG           IMAGE ID      CREATED        SIZE
   ubuntu      galera-node-1 53b97c3d7740  2 minutes ago  362.7 MB
   ubuntu      14.04         ded7cd95e059  5 weeks ago    185.5 MB

You can see in the results here that there is a working node image available for use as a container.  You would launch it executing ``docker run`` at the command-line.  You would repeat the build process on each server to create a node container image for Galera Cluster.

You would then update the container tag to help differentiate between each node by executing something like this:

.. code-block:: console

   [root@node2]# docker build -t ubuntu:galera-node2 ./
   [root@node3]# docker build -t ubuntu:galera-node3 ./


.. _`deploy-container`:
.. rst-class:: rubric-1
.. rubric:: Deploying a Container

When you finish building an image, you're ready to launch the node container.  For each node, start the container using the Docker command-line tool with the ``run`` argument like so:

.. code-block:: console

   # docker run -i -d --name Node1 --host node1 \
         -p 3306:3306 -p 4567:4567 -p 4568:4568 -p 4444:4444 \
	 -v /var/container_data/mysql:/var/lib/mysql \
	 ubuntu:galera-node1

In this example, Docker launches a pre-built Ubuntu container tagged as ``galera-node1``, which was built using the example ``Dockerfile`` from above.  The ``ENTRYPOINT`` parameter is set to ``/bin/mysqld`` so that the container launches the database server when starting.  You would modify the ``--name`` option in the example here for each node container you start.

You'll notice in the example here there are several ``-p`` options included. Those are described in the next section on Firewall Settings.  The ``-v`` option is described in the section after it on Persistent Data.

.. note:: The above command starts a container node meant to be attached to an existing cluster.  If you're starting the first node in a cluster, append the argument ``--wsrep-new-cluster`` to the end of the command.  For more information, see :doc:`Starting a Cluster <../training/tutorials/starting-cluster>`.


.. _`docker-firewall`:
.. rst-class:: rubric-2
.. rubric:: Firewall Settings

When you launch the Docker container (i.e., ``docker run`` as shown above), the series of ``-p`` options connect the ports on the host system to those in the container.  When the container is launched this way, nodes in the container have the same level of access to the network as the node would if it were running on the host system.

Use these settings, though, when you run only one container on the server.  If you are running multiple containers on the server, you'll need a load balancer to handle and direct incoming connections to individual nodes.

For more information on configuring the firewall for Galera Cluster, see :doc:`Firewall Settings <firewall-settings>`.


.. _`docker-data`:
.. rst-class:: rubric-2
.. rubric:: Persistent Data

Docker containers are not meant to carry persistent data.  When you close a container, the data it carries is lost.  To avoid this problem, you can link volumes in the container to directories on the host file system. This is done with the ``-v`` option when you launch the container.

In the launch example above (i.e., the ``docker run`` lines), the ``-v`` argument connects the ``/var/container_data/mysql/`` directory to ``/var/lib/mysql/`` in the container.  This replaces the local datadir inside the container with a symbolic link to a directory on the host system. This ensures that you won't lose data when the container restarts.

.. rst-class:: rubric-2
.. rubric:: Database Client

Once you have a container node running, you can execute additional commands on the container using the ``docker exec`` command with the container name given with the ``--name`` parameter.

Using the example above, if you want access to the database client, you would run the following command:

.. code-block:: console

   # docker exec -ti Node1 /bin/mysql -u root -p

Notice here that ``Node1`` is the name given with the ``--name`` parameter in the example earlier.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
