=====================
 HAProxy
=====================
.. _`haproxy`:

High Availability Proxy, or HAProxy is a single-threaded event-driven non-blocking engine that combines a fast I/O layer with a priority-based scheduler.  You can use it to balance the TCP connections between application servers and Galera Cluster.

---------------------
 Installation
---------------------
.. _`install-haproxy`:

HAProxy is available in the software repositories of most Linux distributions and it is the ports tree of FreeBSD.  You can install it using the package manager.

- For DEB-based Linux distributions, such as Debian and Ubuntu, run the following command:

  .. code-block:: console

     # apt-get install haproxy

- For RPM-based Linux distributions, such as Red Hat, Fedora and CentOS, run the following command:

  .. code-block:: console

     # yum install haproxy

- For SUSE-based Linux distributions, such as SUSE Enterprise Linux and openSUSE, instead run this command:

  .. code-block:: console

     # zypper install haproxy

- For FreeBSD and similar operating systems, HAProxy is available in the ports tree at `/usr/ports/net/haproxy`.  Alternatively, you can install it using the package manager:

  .. code-block:: console

     # pkg install net/haproxy

This installs HAProxy on your system.  In the event that the command for your distribution or operating system does not work as expected, check the your system's documentation or software repository for the correct procedure to install HAProxy.

----------------------
Configuration
----------------------
.. _`haproxy-config`:

Configuration options for HAProxy are managed through an ``haproxy.cfg`` configuration file.  The above package installations generally places this file in the ``/etc/haproxy/`` directory, though it may have a different path depending on your distribution or operating system.

To configure HAProxy to work with Galera Cluster, add the following lines to the ``haproxy.cfg`` configuration file:

.. code-block:: squid

   # Load Balancing for Galera Cluster
   listen galera 192.168.1.10:3306
        balance source
	mode tcp
	option tcpka
	option mysql-check user haproxy
	server node1 192.168.1.1:3306 check weight 1
	server node2 192.168.1.2:3306 check weight 1
	server node2 192.168.1.3:3306 check weight 1

Create the proxy for Galera Cluster using the ``listen`` parameter.  This gives HAProxy an arbitrary name for the proxy and defines the IP address and port you want it to listen on for incoming connections.  Under this parameter, indent and define a series of options to tell HAProxy what you want it to do with these connections.

- ``balance`` Defines the destination selection policy you want HAProxy to use in choosing which server it routes the incoming connections to.

- ``mode tcp`` Defines the type of connections it should route. Galera Cluster uses TCP connections.

- ``option tcpka`` Enables the keepalive function to maintain TCP connections.

- ``option mysql-check user <username>`` Enables a database server check, to determine whether the node is currently operational.

- ``server <server-name> <IP_address> check weight 1`` Defines the nodes you want HAProxy to use in routing connections.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Destination Selection Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`haproxy-destination-selection`:

When HAProxy receives a new connection, there are a number of options available to define which algorithm it uses to choose where to route that connection.  This algorithm is its destination selection policy.  It is defined by the ``balance`` parameter.

- **Round Robin** Directs new connections to the next destination in a circular order list, modified by the server's weight.  Enable it with ``balance roundrobin``.
- **Static Round Robin** Directs new connections to the next destination in a circular order list, modified by the server's weight.  Unlike the standard implementation of round robin, in static round robin you cannot modify the server weight on the fly.  Changing the server weight requires you to restart HAProxy. Enable it with ``balance static-rr``.
- **Least Connected** Directs new connections to the server with the smallest number of connections available, which is adjuted for the server's weight.  Enable it with ``balance leastconn``
- **First** Directs new connections to the first server with a connection slot available.  They are chosen from the lowest numeric identifier to the highest.  Once the server reaches its maximum connections value, HAProxy moves to the next in the list.  Enable it with ``balance first``.
- **Source Tracking** Divides the source IP address by the total weight of running servers.  Ensures that client connections from the same source IP always reach the same server.  Enable it with ``balance source``

In the above configuration example, HAProxy is configured to use the source selection policy.  For your own implementations, choose the policy that works best with your infrastructure and load.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling Database Server Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`haproxy-mysql-check`:

In addition to routing TCP connections to Galera Cluster, HAProxy can also perform basic health checks on the database server.  When enabled, HAProxy attempts to establish a connection with the node and parses its response or any errors to determine if the node is operational.

For HAProxy you can enable this through the ``mysql-check`` option.  However, it requires that you also create a user in the cluster for HAProxy to use when connecting.

.. code-block:: mysql

   CREATE USER 'haproxy'@'192.168.1.10';

Define the user name as the same as given in the ``haproxy.cfg`` configuration file for the ``mysql-check`` option.  Replace the IP address with that of the server that runs HAProxy.


----------------------
Using HAProxy
----------------------
.. _`haproxy-use`:

When you finish configuring HAProxy and the nodes to work with HAProxy, you can start it on the server.  For servers that use ``init``, run the following command:

.. code-block:: console

   # service haproxy start

For servers that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl start haproxy

The server is now running HAProxy.  When new connections are made to this server, it routes them through to nodes in the cluster.


