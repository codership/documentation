=================================
Galera Load Balancer
=================================
.. _`glb-doc`:

Galera Load Balancer provides simple TCP connection balancing developed with scalability and performance in mind.  It draws on Pen for inspiration, but its functionality is limited to only balancing TCP connections.

- Support for configuring back-end servers at runtime.
- Support for draning servers.
- Support for the epoll API for routing performance.
- Support for multithreaded operations.
- Optional watchdog module to monitor destinations and adjust the routing table.

------------------------
Installation
------------------------
.. _`glb-install`:

Unlike Galera Cluster, there is no binary installation available for Galera Load Balancer.  Installing it on your system requires that you build it from source.  It is available on GitHub at `glb <https://github.com/codership/glb>`_.

To build Galera Load Balancer, complete the following steps:

#. From a directory convenient to you for source builds, such as ``/opt``, use Git to clone the GitHub repo for Galera Load Balancer.

   .. code-block:: console

      $ git clone https://github.com/codership/glb

#. Change into the new ``glb/`` directory created by Git, then run the bootstrap script.

   .. code-block:: console

      $ cd glb/
      $ ./bootstrap.sh

#. Configure Make to build on your system.

   .. code-block:: console

      $ ./configure

#. Build the application with Make.

   .. code-block:: console

      $ make

#. Install the application on your system.

   .. code-block:: console

      # make install

   .. note:: Galera Load Balancer installs in ``/usr/sbin``.  You need to run the above command as root.

Galera Load Balancer is now installed on your system.  You can launch it from the command-line, using the ``glbd`` command.

In addition to the system daemon, you have also installed ``libglb``, a shared library for connection balancing with any Linux applications that use the ``connect()`` call from the C Standard Library.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Service Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`glb-service`:

The above installation procedure only installs Galera Load Balancer to be run manually from the command-line.  However, you may find it more useful to run this application as a system service.

In the source directory you cloned from GitHub, navigate into the ``files/`` directory.  Within this directory there is a configuration file and a service script that you need to copy to their relevant locations.

- Place ``glbd.sh`` into ``/etc/init.d`` directory under a service name.

  .. code-block:: console

     # cp glbd.sh /etc/init.d/glb

- Place ``glbd.cfg`` into either configuration directory.  For Red Hat and its derivatives, this is ``/etc/sysconfig/glbd.cfg``.  For Debian and its derivatives, use ``/etc/default/glbd.cfg``.

  .. code-block:: console

     # cp glbd.cfg /etc/sysconfig/glbd.cfg

  .. note:: The ``glbd.cfg`` configuration file used below refer to the one you have copied into ``/etc``.

When you finish this, you can manage Galera Load Balancer through the ``service`` command.  For more information on available commands, see :ref:`Using Galera Load Balancer <glb-use>`.

---------------------
Configuration
---------------------
.. _`glb-config`:

When you run Galera Load Balancer, you can configure its use through the command-line options, which you can reference through the ``--help`` command.  For users that run Galera Load Balancer as a service, you can manage it through the ``glbd.cfg`` configuration file.

- :ref:`LISTEN_ADDR <glb-listen_addr>` Defines the address that Galera Load Balancer monitors for incoming client connections.

- :ref:`DEFAULT_TARGETS <glb-default_targets>` Defines the default servers that Galera Load Balancer routes incoming client connections to.  For this parameter, use the IP addresses for the nodes in your cluster.

- :ref:`OTHER_OPTIONS <glb-other_options>` Defines additional Galera Load Balancer options, such as the balancing policy you want to use.  Use the same format as they would appear on the command-line.

For instance,

.. code-block:: ini

   # Galera Load Balancer COnfigurations
   LISTEN_ADDR="8010"
   DEFAULT_TARGETS="192.168.1.1 192.168.1.2 192.168.1.3"
   OTHER_OPTIONS="--random --top 3"

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Destination Selection Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`glb-dest-select`:

Galera Load Balancer, both the system daemon and the shared library, support five destination selection policies.  When you run it from the command-line, you can define these using the command-line arguments, otherwise add the arguments to the :ref:`OTHER_OPTIONS <glb-other_options>` parameter in the ``glbd.cfg`` configuration file.

- **Least Connected** Directs new connections to the server using the smallest number of connections possible, which is adjusted for the server weight.  This is the default policy.

- **Round Robin** Directs new connections to the next destination in the circular order list.  You can enable it through the :ref:`--round <glb-round>` option.

- **Single** Directs all connections to the single server with the highest weight of those available.  Routing continues to that server until it fails or a server with a higher weight becomes available.  You can enable it through the :ref:`--single <glb-single>` option.

- **Random** Directs connections randomly to available servers.  You can enable it through the :ref:`--random <glb-random>` option

- **Source Tracking** Directs connections originating from the same address to the same server.  You can enable it through the :ref:`--source <glb-source>` option.



---------------------------
Using Galera Load Balancer
---------------------------
.. _`glb-use`:

In the above section :ref:`Service Installation <glb-service>`, you configured your system to run Galera Load Balancer as a service.  This allows you to manage common operations through the ``service`` command, for instance:

.. code-block:: console

   # service glb getinfo

   Router:
   -------------------------------------------
        Address       : weight   usage  cons
     192.168.1.1:4444 : 1.000    0.000    0
     192.168.1.2:4444 : 1.000    0.000    0
     192.168.1.3:4444 : 1.000    0.000    0
   -------------------------------------------
   Destinations: 3, total connections: 0

The ``service`` script supports the following operations:

- ``start``/``stop``/``restart`` Commands to start, stop and restart Galera Load Balancer.
- ``getinfo`` Command provides the current routing information: the servers available, their weight and usage, the number of connections made to them.
- ``add``/``remove <IP Address>`` Add or remove the designated IP address from the routing table.
- ``getstats`` Command provides performance statistics.
- ``drain <IP Address>`` Sets the designated server to drain.  That is, Galera Load Balancer does not allocate new connections to the server, but also does not kill existing connections.  Instead, it waits for the connections to this server to end gracefully.

When adding an IP address to Galera Load Balancer at runtime, bear in mind that it must follow the convention: ``IP Address:port:weight``.  When adding through a hostname, the convention is ``Hostname:port:weight``.

