.. meta::
   :title: Galera Cluster - High Availability Proxy
   :description:
   :language: en-US
   :keywords: galera cluster, high availability, ha proxy, destination selection
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`ha-proxy`:

===========
 HAProxy
===========

High Availability Proxy, or HAProxy is a single-threaded event-driven non-blocking engine that combines a fast I/O layer with a priority-based scheduler. You can use it to balance  TCP connections between application servers and Galera Cluster.

.. only:: html

          .. image:: ../images/support.jpg
             :target: https://galeracluster.com/support/#galera-cluster-support-subscription
             :width: 740

   .. only:: latex

          .. image:: ../images/support.jpg
		  :target: https://galeracluster.com/support/#galera-cluster-support-subscription


.. _`install-haproxy`:
.. rst-class:: section-heading
.. rubric:: Installation

HAProxy is available in the software repositories of most Linux distributions and it is the ports tree of FreeBSD. You can install it using the appropriate package manager.

- For DEB-based Linux distributions (for example, Debian and Ubuntu), run the following from the command-line:

  .. code-block:: console

     # apt-get install haproxy

- For RPM-based Linux distributions (for example, Red Hat Enterprise Linux and CentOS), execute the following from the command-line:

  .. code-block:: console

     # yum install haproxy

- For FreeBSD and similar operating systems, HAProxy is available in the ports tree at `/usr/ports/net/haproxy`. Alternatively, you can install it using the package manager like so:

  .. code-block:: console

     # pkg install net/haproxy

Whichever method you use, it installs HAProxy on your server. In the event that the command for your Linux distribution or operating system does not work as expected, check  your system's documentation or software repository for the correct procedure to install HAProxy.


.. _`haproxy-config`:
.. rst-class:: section-heading
.. rubric:: Configuration

Configuration options for HAProxy are managed through an ``haproxy.cfg`` configuration file. The above package installations generally put this file in the ``/etc/haproxy/`` directory. However, it may have a different path depending on your operating system distribution.

To configure HAProxy to work with Galera Cluster, add the lines to the ``haproxy.cfg`` configuration file similar to the following:

.. code-block:: squid

   # Load Balancing for Galera Cluster
   listen galera 192.168.1.10:3306
        balance source
	mode tcp
	option tcpka
	option mysql-check user haproxy
	server node1 192.168.1.1:3306 check weight 1
	server node2 192.168.1.2:3306 check weight 1
	server node3 192.168.1.3:3306 check weight 1

You will create the proxy for Galera Cluster using the ``listen`` parameter. This gives HAProxy an arbitrary name for the proxy and defines the IP address and port you want it to listen on for incoming connections. Under this parameter, indent and define a series of options to tell HAProxy what you want it to do with these connections.

- ``balance`` defines the destination selection policy HAProxy should use in choosing which server it routes incoming connections.

- ``mode tcp`` defines the type of connections it should route. Galera Cluster uses TCP connections.

- ``option tcpka`` enables the keepalive function to maintain TCP connections.

- ``option mysql-check user <username>`` enables a database server check to determine whether the node is currently operational.

- ``server <server-name> <IP_address> check weight 1`` defines the nodes HAProxy should use in routing connections.


.. _`haproxy-destination-selection`:
.. rst-class:: sub-heading
.. rubric:: Destination Selection Policies

When HAProxy receives a new connection, there are a number of options available to define which algorithm it uses to choose where to route the connection. This algorithm is its destination selection policy. It is defined by the ``balance`` parameter.

- **Round Robin** directs new connections to the next destination in a circular order list, modified by the server's weight. Enable it with ``balance roundrobin``.

- **Static Round Robin** directs new connections to the next destination in a circular order list, modified by the server's weight. Unlike the standard implementation of round robin, in static round robin you can't modify the server weight on the fly. Changing the server weight requires you to restart HAProxy. Enable it with ``balance static-rr``.

- **Least Connected** directs new connections to the server with the smallest number of connections available, which is adjuted for the server's weight. Enable it with ``balance leastconn``.

- **First** directs new connections to the first server with a connection slot available. They are chosen from the lowest numeric identifier to the highest. Once the server reaches its maximum connections value, HAProxy moves to the next in the list. Enable it with ``balance first``.

- **Source Tracking** divides the source IP address by the total weight of running servers. Ensures that client connections from the same source IP always reach the same server. Enable it with ``balance source``.

In the above configuration example, HAProxy is configured to use the source selection policy. For your implementation, choose the policy that works best with your infrastructure and load.


.. _`haproxy-mysql-check`:
.. rst-class:: sub-heading
.. rubric:: Enabling Database Server Checks

In addition to routing TCP connections to Galera Cluster, HAProxy can also perform basic health checks on the database server. When enabled, HAProxy attempts to establish a connection with the node and parses its response, or any errors, to determine if the node is operational.

For HAProxy, you can enable this through the ``mysql-check`` option. However, it requires that you also create a user in the cluster for HAProxy to use when connecting.

.. code-block:: mysql

   CREATE USER 'haproxy'@'192.168.1.10';

Make the user name the same as given in the ``haproxy.cfg`` configuration file for the ``mysql-check`` option. Replace the IP address with that of the server that runs HAProxy.


.. _`haproxy-use`:
.. rst-class:: section-heading
.. rubric:: Using HAProxy

When you finish configuring HAProxy and the nodes to work with HAProxy, you can start it on the server. For servers that use ``init``, run the following command:

.. code-block:: console

   # service haproxy start

For servers that use ``systemd``, run instead this command:

.. code-block:: console

   # systemctl start haproxy

After doing this, the server will be running HAProxy. When new connections are made to this server, it routes them through to nodes in the cluster.
