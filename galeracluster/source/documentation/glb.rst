.. meta::
   :title: Galera Load Balancer (glbd)
   :description:
   :language: en-US
   :keywords: galera cluster, load balancing, galera load balancer, glbd
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`Using Galera Load Balancer <glb-use>`
      - :ref:`LISTEN_ADDR <glb-listen_addr>`
      - :ref:`DEFAULT_TARGETS <glb-default_targets>`
      - :ref:`OTHER_OPTIONS <glb-other_options>`
      - :ref:`--round <glb-round>`
      - :ref:`--single <glb-single>`
      - :ref:`--random <glb-random>`
      - :ref:`--source <glb-source>`
      - :ref:`Service Installation <glb-service>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`glb-doc`:

======================
Galera Load Balancer
======================

Galera Load Balancer provides simple TCP connection balancing. It was developed with scalability and performance in mind.  It draws on Pen for inspiration, but its functionality is limited to only balancing TCP connections.  It provides several features:

- Support for configuring back-end servers at runtime.
- Support for draining servers.
- Support for the epoll API for routing performance.
- Support for multithreaded operations.
- Optional watchdog module to monitor destinations and adjust the routing table.


.. _`glb-install`:
.. rst-class:: section-heading
.. rubric:: Installation

Unlike Galera Cluster, there is no binary installation available for Galera Load Balancer.  Installing it on your system will require you to build it from the source files.  They're available on GitHub at `glb <https://github.com/codership/glb>`_.

To build Galera Load Balancer, you will need to complete a few steps.  First, from a directory convenient for source builds (e.g., ``/opt``), use the ``git`` utility to clone the GitHub repository for Galera Load Balancer. You would do this like so:

 .. code-block:: console

    $ git clone https://github.com/codership/glb

Next, from within ``glb`` directory created by ``git``, run the bootstrap script--which will be found in that directory.

 .. code-block:: console

    $ cd glb/
    $ ./bootstrap.sh

Now you will need to configure ``make`` to build on your system, then run ``make`` to build the application. After that, you'll use ``make`` to install it. This may seem like a lot, but it's simple. Just execute the following lines, one at a time, from the command-line:

 .. code-block:: console

    $ ./configure

    $ make

    # make install

.. note:: Galera Load Balancer installs in the ``/usr/sbin`` directory.  So you will need to run the last line above as root.

Once you've successfully execute everything above, Galera Load Balancer will be installed on your system.  You can launch it from the command-line, using the ``glbd`` command.

In addition to the system daemon, you will also have installed ``libglb``, a shared library for connection balancing with any Linux applications that use the ``connect()`` call from the C Standard Library.


.. _`glb-service`:
.. rst-class:: section-heading
.. rubric:: Service Installation

The above installation procedure only installs Galera Load Balancer to be run manually from the command-line.  However, you may find it more useful to run this application as a system service. To do this, you'll need to copy a couple of files to the appropriate directories.

In the source directory you cloned from GitHub, navigate into the ``files`` directory.  Within that directory there is a configuration file and a service script that you need to copy to their relevant locations.

First, copy ``glbd.sh`` into ``/etc/init.d`` directory under a service name. You would execute the following from the command-line to do this:

.. code-block:: console

   # cp glbd.sh /etc/init.d/glb

Now, copy the default ``glbd.cfg`` file into the appropriate configuration directory.  For Red Hat and its derivatives, this is ``/etc/sysconfig/glbd.cfg``.  For Debian and its derivatives, use ``/etc/default/glbd.cfg``. For the former possibility, you would execute this from the command-line:

.. code-block:: console

   # cp glbd.cfg /etc/sysconfig/glbd.cfg

When you finish this, you will be able to manage Galera Load Balancer through the ``service`` command.  For more information on available commands, see :ref:`Using Galera Load Balancer <glb-use>`.


.. _`glb-config`:
.. rst-class:: section-heading
.. rubric:: Configuration

When you run Galera Load Balancer, you can configure its use through the command-line options. You can get a list of by exeduting ``glb`` with the ``--help`` option.  For servers running Galera Load Balancer as a service, you can manage it through the ``glbd.cfg`` configuration file.

- :ref:`LISTEN_ADDR <glb-listen_addr>`: This is the address that Galera Load Balancer monitors for incoming client connections.

- :ref:`DEFAULT_TARGETS <glb-default_targets>`: This specifies the default servers where Galera Load Balancer is to route incoming client connections. For this parameter, use the IP addresses for the nodes in your cluster.

- :ref:`OTHER_OPTIONS <glb-other_options>`: This is used to define additional Galera Load Balancer options. For example, you might want to set the balancing policy.  Use the same format as you would from the command-line.

Below is an example of a `glbd.cfg`` configuration file:

.. code-block:: ini

   # Galera Load Balancer Configuration
   LISTEN_ADDR="8010"
   DEFAULT_TARGETS="192.168.1.1 192.168.1.2 192.168.1.3"
   OTHER_OPTIONS="--random --top 3"

The ``glbd.cfg`` configuration file would be the one you copied into ``/etc`` as mentioned in the previous section.


.. _`glb-dest-select`:
.. rst-class:: section-heading
.. rubric:: Destination Selection Policies

Galera Load Balancer--both the system daemon and the shared library--supports five destination selection policies. When you run it from the command-line, you can define these using the command-line arguments. Otherwise, you'll have to add the arguments to the :ref:`OTHER_OPTIONS <glb-other_options>` parameter in the ``glbd.cfg`` configuration file.

- **Least Connected**: This directs new connections to the server using the smallest number of connections possible. It will be adjusted for the server weight.  This is the default policy.

- **Round Robin**: This sets new connections to the next destination in the circular order list. You can enable it with the :ref:`--round <glb-round>` option.

- **Single**: This directs all connections to the single server with the highest weight of those available.  Routing continues to that server until it fails, or until a server with a higher weight becomes available.  You can enable it with the :ref:`--single <glb-single>` option.

- **Random**: This will direct connections randomly to available servers.  You can enable it using the :ref:`--random <glb-random>` option.

- **Source Tracking**: This will direct connections originating from the same address to the same server.  You can enable it with the :ref:`--source <glb-source>` option.


.. _`glb-use`:
.. rst-class:: section-heading
.. rubric:: Using Galera Load Balancer

The section on :ref:`Service Installation <glb-service>` explained how to configure a system to run Galera Load Balancer as a service.  If you do that, you can then manage common operations with the ``service`` command. The format for doing this is to enter ``service``, followed by ``glb``, and then an option.

Below is an example of how you might use ``service`` to get information on the Galera Load Balancer:

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

In the results shown here, you can see a list of servers available, their weight and usage, as well as the number of connections made to them.

The ``service`` script supports several operations.  Below is a list of them and their uses:

- ``start`` is used to start ``glb``, the Galera Load Balancer.
- ``stop`` will stop Galera Load Balancer.
- ``restart`` tells ``glb`` to stop and restart the Galera Load Balancer.

- ``getinfo`` is used as shown in the example above to retrieve the current routing information.
- ``getstats`` will provide performance statistics related to the cluster.

- ``add <IP Address>`` can be used to add an IP address from the routing table.
- ``remove <IP Address>`` will remove the designated IP address from the routing table.
- ``drain <IP Address>`` will sets the designated server to drain. When doing this, Galera Load Balancer won't send new connections to the given server, but it also won't kill existing connections. Instead, it waits for the connections to the specified server to end gracefully.

When adding an IP address to Galera Load Balancer at runtime, keep in mind that it must follow the convention, ``IP Address:port:weight``.  A hostname may be used instead of an IP address.

.. container:: bottom-links

   Related Documents

   - :ref:`Using Galera Load Balancer <glb-use>`
   - :ref:`LISTEN_ADDR <glb-listen_addr>`
   - :ref:`DEFAULT_TARGETS <glb-default_targets>`
   - :ref:`OTHER_OPTIONS <glb-other_options>`
   - :ref:`--round <glb-round>`
   - :ref:`--single <glb-single>`
   - :ref:`--random <glb-random>`
   - :ref:`--source <glb-source>`
   - :ref:`Service Installation <glb-service>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
