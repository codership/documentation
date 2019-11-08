.. meta::
   :title: Galera Load Balancer (glbd) Parameters
   :description:
   :language: en-US
   :keywords: galera cluster, load balancing, galera load balancer, glbd, parameters, options
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

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

      - :ref:`Configuration Options <glb-config-options>`
      - :ref:`Destination Policies <glb-dest-select>`
      - :ref:`LISTEN_ADDR <glb-listen_addr>`
      - :ref:`OTHER_OPTIONS <glb-other_options>`
      - :ref:`--watchdog <glb-watchdog>`

      Related Articles


.. cssclass:: library-document
.. _`glb-parameters`:

================================
Galera Load Balancer Parameters
================================

Galera Load Balancer provides simple TCP connection balancing developed with scalability and performance in mind.  It draws on Pen for inspiration, but its functionality is limited to only balancing TCP connections.

It can be run either through the ``service`` command or the command-line interface of ``glbd``.  Configuration for Galera Load Balancer depends on which you use to run it.


.. _`glb-config-parameters`:
.. rst-class:: section-heading
.. rubric:: Configuration Parameters

When Galera Load Balancer starts as a system service, it reads the ``glbd.cfg`` configuration file for default parameters you want to use.  Only the :ref:`LISTEN_ADDR <glb-listen_addr>` parameter is mandatory.

.. csv-table::
   :class: doc-options
   :header: "Parameter", "Default Configuration"

   ":ref:`CONTROL_ADDR <glb-control_addr>`", "``127.0.0.1:8011``"
   ":ref:`CONTROL_FIFO <glb-control_fifo>`", "``/var/run/glbd.fifo``"
   ":ref:`DEFAULT_TARGETS <glb-default_targets>`", "``127.0.0.1:80 10.0.1:80 10.0.0.2:80``"
   ":ref:`LISTEN_ADDR <glb-listen_addr>`", "``8010``"
   ":ref:`MAX_CONN <glb-max_conn-par>`", ""
   ":ref:`OTHER_OPTIONS <glb-other_options>`", ""
   ":ref:`THREADS <glb-threads-par>`", "``2``"

.. _`glb-control_addr`:
.. rst-class:: section-heading
.. rubric:: ``CONTROL_ADDR``

Defines the IP address and port for controlling connections.

.. csv-table::
   :class: doc-options

   "**Command-line Argument**", ":ref:`--control <glb-control>`"
   "**Default Configuration**", "``127.0.0.1:8011``"
   "**Mandatory Parameter**", "No"


This is an optional parameter.  Use it to define the server used in controlling client connections.  When using this parameter you must define the port.  In the event that you do not define this parameter, Galera Load Balancer does not open the relevant socket.

.. code-block:: ini

   CONTROL_ADDR="127.0.0.1:8011"


.. _`glb-control_fifo`:
.. rst-class:: section-heading
.. rubric:: ``CONTROL_FIFO``

Defines the path to the FIFO control file.

.. csv-table::
   :class: doc-options

   "**Command-line Argument**", ":ref:`--fifo <glb-fifo>`"
   "**Default Configuration**", "``/var/run/glbd.fifo``"
   "**Mandatory Parameter**", "No"

This is an optional parameter.  It defines the path to the FIFO control file as is always opened.  In the event that there is already a file at this path, Galera Load Balancer fails to start.

.. code-block:: ini

   CONTROL_FIFO="/var/run/glbd.fifo"


.. _`glb-default_targets`:
.. rst-class:: section-heading
.. rubric:: ``DEFAULT_TARGETS``

Defines the IP addresses and ports of the destination servers.

.. csv-table::
   :class: doc-options

   "**Default Configuration**", "``127.0.0.1:80 10.0.0.1:80 10.0.0.2:80:2``"
   "**Mandatory Parameter**", "No"

This parameter defines that IP addresses that Galera Load Balancer uses as destination servers.  Specifically, in this case the Galera Cluster nodes that it routes application traffic onto.

.. code-block:: ini

   DEFAULT_TARGETS="192.168.1.1 192.168.1.2 192.168.1.3"


.. _`glb-listen_addr`:
.. rst-class:: section-heading
.. rubric:: ``LISTEN_ADDR``

Defines the IP address and port used for client connections.

.. csv-table::
   :class: doc-options

   "**Default Configuration**", "``8010``"
   "**Mandatory Parameter**", "Yes"

This parameter defines the IP address and port that Galera Load Balancer listens on for incoming client connections.  The IP address is optional, the port mandatory.  In the event that you define a port without an IP address, Galera Load Balancer listens on that port for all available network interfaces.

.. code-block:: ini

   LISTEN_ADDR="8010"


.. _`glb-max_conn-par`:
.. rst-class:: section-heading
.. rubric:: ``MAX_CONN``

Defines the maximum allowed client connections.

.. csv-table::
   :class: doc-options

   "**Default Configuration**", ":ref:`--max_conn <glb-max_conn-arg>`"
   "**Mandatory Parameter**", "No"

This parameter defines the maximum number of client connections that you want to allow to Galera Load Balancer.  It modifies the system open files limit to accommodate at least this many connections, provided sufficient privileges.  It is recommend that you define this parameter if you expect the number of client connections to exceed five hundred.

.. code-block:: ini

   MAX_CONN="135"

This option defines the maximum number of client connections that you want allow to Galera Load Balancer. Bear in mind, that it can be operating system dependent.


.. _`glb-other_options`:
.. rst-class:: section-heading
.. rubric:: ``OTHER_OPTIONS``

Defines additional options that you want to pass to Galera Load Balancer.  There is no default configuration and this is not a mandatory parameter.

This parameter defines various additional options that you would like to pass to Galera Load Balancer, such as a destination selection policy or Watchdog configurations.  Use the same syntax as you would for the command-line arguments.  For more information on the available options, see :ref:`Configuration Options <glb-config-options>`.

.. code-block:: ini

   OTHER_OPTIONS="--random --watchdog exec:'mysql -utest -ptestpass' --discover"


.. _`glb-threads-par`:
.. rst-class:: section-heading
.. rubric:: ``THREADS``

Defines the number of threads you want to use.

.. csv-table::
   :class: doc-options

   "**Default Configuration**", ":ref:`--threads <glb-threads-arg>`"
   "**Mandatory Parameter**", "No"

This parameter allows you to define the number of threads (that is, connection pools), which you want to allow Galera Load Balancer to use.  It is advisable that you have at least a few per CPU core.

.. code-block:: ini

   THREADS="6"


.. _`glb-config-options`:
.. rst-class:: section-heading
.. rubric:: Configuration Options

When Galera Load Balancer starts as a daemon process, through the ``/sbin/glbd`` command, it allows you to pass a number of command-line arguments to configure how it operates.  It uses the following syntax:

.. code-block:: text

   /usr/local/sbin/glbd [OPTIONS] LISTEN_ADDRESS [DESTINATION_LIST]

In the event that you would like to set any of these options when you run Galera Load Balancer as a service, you can define them through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

.. csv-table::
   :class: doc-options
   :header: "Long Argument", "Short", "Type", "Parameter"

   ":ref:`--control <glb-control>`", "``-c``", "IP address", ":ref:`CONTROL_ADDR <glb-control_addr>`"
   ":ref:`--daemon <glb-daemon>`", "``-d``", "Boolean", ""
   ":ref:`--defer-accept <glb-defer-accept>`", "``-a``", "Boolean", ""
   ":ref:`--discover <glb-discover>`", "``-D``", "Boolean", ""
   ":ref:`--extra <glb-extra>`", "``-x``", "Decimal", ""
   ":ref:`--fifo <glb-fifo>`", "``-f``", "File Path", ":ref:`CONTROL_FIFO <glb-control_fifo>`"
   ":ref:`--interval <glb-interval>`", "``-i``", "Decimal", ""
   ":ref:`--keepalive <glb-keepalive>`", "``-K``", "Boolean", ""
   ":ref:`--latency <glb-latency>`", "``-L``", "Integer", ""
   ":ref:`--linger <glb-linger>`", "``-l``", "Boolean", ""
   ":ref:`--max_conn <glb-max_conn-arg>`", "``-m``", "Integer", ":ref:`MAX_CONN <glb-max_conn-par>`"
   ":ref:`--nodelay <glb-nodelay>`", "``-n``", "Boolean", ""
   ":ref:`--random <glb-random>`", "``-r``", "Boolean", ""
   ":ref:`--round <glb-round>`", "``-b``", "Boolean", ""
   ":ref:`--single <glb-single>`", "``-S``", "Boolean", ""
   ":ref:`--source <glb-source>`", "``-s``", "Boolean", ""
   ":ref:`--threads <glb-threads-arg>`", "``-t``", "Integer", ":ref:`THREADS <glb-threads-par>`"
   ":ref:`--top <glb-top>`", "``-T``", "Boolean", ""
   ":ref:`--verbose <glb-verbose>`", "``-v``", "Boolean", ""
   ":ref:`--watchdog <glb-watchdog>`", "``-w``", "String", ""



.. _`glb-control`:
.. rst-class:: section-heading
.. rubric:: ``--control``

Defines the IP address and port for control connections.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-c``"
   "**Syntax**", "``--control [IP|Hostname:]port``"
   "**Type**", "IP Address"
   "**Configuration Parameter**", ":ref:`CONTROL_ADDR <glb-control_addr>`"

For more information on defining the controlling connections, see the :ref:`CONTROL_ADDR <glb-control_addr>` parameter.

.. code-block:: console

   # glbd --control 192.168.1.1:80 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-daemon`:
.. rst-class:: section-heading
.. rubric:: ``--daemon``

Defines whether you want Galera Load Balancer to run as a daemon process.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-d``"
   "**Syntax**", "``--daemon``"
   "**Type**", "Boolean"

This option defines whether you want to start ``glbd`` as a daemon process.  That is, if you want it to run in the background, instead of claiming the current terminal session.

.. code-block:: console

   # glbd --daemon 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-defer-accept`:
.. rst-class:: section-heading
.. rubric:: ``--defer-accept``

Enables TCP deferred acceptance on the listening socket.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-a``"
   "**Syntax**", "``--defer-accept``"
   "**Type**", "Boolean"

Enabling ``TCP_DEFER_ACCEPT`` allows Galera Load Balancer to awaken only when data arrives on the listening socket.  It is disabled by default.

.. code-block:: console

   # glbd --defer-accept 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-discover`:
.. rst-class:: section-heading
.. rubric:: ``--discover``

Defines whether you want to use watchdog results to discover and set new destinations.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-D``"
   "**Syntax**", "``--discover``"
   "**Type**", "Boolean"

When you define the :ref:`--watchdog <glb-watchdog>` option, this option defines whether Galera Load Balancer uses the return value in discovering and setting new addresses for destination servers.  For instance, after querying for the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter.

.. code-block:: console

   # glbd --discover -w exec:"mysql.sh -utest -ptestpass" 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-extra`:
.. rst-class:: section-heading
.. rubric:: ``--extra``

Defines whether you want to perform an extra destination poll on connection attempts.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-x``"
   "**Syntax**", "``--extra D.DDD``"
   "**Type**", "Decimal"

This option defines whether and when you want Galera Load Balancer to perform an additional destination poll on connection attempts.  The given value indicates how many seconds after the previous poll that you want it to run the extra poll.  By default, the extra polling feature is disabled.

.. code-block:: console

   # glbd --extra 1.35 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-fifo`:
.. rst-class:: section-heading
.. rubric:: ``--fifo``

Defines the path to the FIFO control file.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-f``"
   "**Syntax**", "``--fifo /path/to/glbd.fifo``"
   "**Type**", "File Path"
   "**Configuration Parameter**", ":ref:`CONTROL_FIFO <glb-control_fifo>`"

For more information on using FIFO control files, see the :ref:`CONTROL_FIFO <glb-control_fifo>` parameter.

.. code-block:: console

   # glbd --fifo /var/run/glbd.fifo 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-interval`:
.. rst-class:: section-heading
.. rubric:: ``--interval``

Defines how often to probe destinations for liveliness.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-i``"
   "**Syntax**", "``--interval D.DDD``"
   "**Type**", "Decimal"

This option defines how often Galera Load Balancer checks destination servers for liveliness.  It uses values given in seconds.  By default, it checks every second.

.. code-block:: console

   # glbd --interval 2.013 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-keepalive`:
.. rst-class:: section-heading
.. rubric:: ``--keepalive``

Defines whether you want to disable the ``SO_KEEPALIVE`` socket option on server-side sockets.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-K``"
   "**Syntax**", "``--keepalive``"
   "**Type**", "Boolean"

Linux systems feature the socket option ``SO_KEEPALIVE``, which causes the server to send packets to a remote system in order to main the client connection with the destination server.  This option allows you to disable ``SO_KEEPALIVE`` on server-side sockets.  It allows ``SO_KEEPALIVE`` by default.

.. code-block:: console

   # glbd --keepalive 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-latency`:
.. rst-class:: section-heading
.. rubric:: ``--latency``

Defines the number of samples to take in calculating latency for watchdog.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-L``"
   "**Syntax**", "``--latency N``"
   "**Type**", "Integer"

When the Watchdog module tests a destination server to calculate latency, it sends a number of packets through to measure its responsiveness.  This option configures how many packets it sends in sampling latency.

.. code-block:: console

   # glbd --latency 25 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-linger`:
.. rst-class:: section-heading
.. rubric:: ``--linger``

Defines whether Galera Load Balancer disables sockets lingering after they are closed.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-l``"
   "**Syntax**", "``--linger``"
   "**Type**", "Boolean"

When Galera Load Balancer sends the ``close()`` command, occasionally sockets linger in a ``TIME_WAIT`` state.  This options defines whether or not you want Galera Load Balancer to disable lingering sockets.

.. code-block:: console

   # glbd --linger 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-max_conn-arg`:
.. rst-class:: section-heading
.. rubric:: ``--max_conn``

Defines the maximum allowed client connections.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-m``"
   "**Syntax**", "``--max_conn N``"
   "**Type**", "Integer"

For more information on defining the maximum client connections, see the :ref:`MAX_CONN <glb-max_conn-par>` parameter.

.. code-block:: console

   # glbd --max_conn 125 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-nodelay`:
.. rst-class:: section-heading
.. rubric:: ``--nodelay``

Defines whether it disables the TCP no-delay socket option.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-n``"
   "**Syntax**", "``--nodelay``"
   "**Type**", "Boolean"

Under normal operation, TCP connections automatically concatenate small packets into larger frames through the Nagle algorithm.  In the event that you want Galera Load Balancer to disable this feature, this option causes it to open TCP connections with the ``TCP_NODELAY`` feature.

.. code-block:: console

   # glbd --nodelay 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-random`:
.. rst-class:: section-heading
.. rubric:: ``--random``

Defines the destination selection policy as Random.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-r``"
   "**Syntax**", "``--random``"
   "**Type**", "Boolean"

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Random, it randomly chooses a destination from the pool of available servers.  You can enable this feature by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.


For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.

.. code-block:: console

   # glbd --random 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-round`:
.. rst-class:: section-heading
.. rubric:: ``--round``

Defines the destination selection policy as Round Robin.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-b``"
   "**Syntax**", "``--round``"
   "**Type**", "Boolean"

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Round Robin, it directs new connections to the next server in a circular order list.  You can enable this feature by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.


.. code-block:: console

   # glbd --round 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-single`:
.. rst-class:: section-heading
.. rubric:: ``--single``

Defines the destination selection policy as Single.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-S``"
   "**Syntax**", "``--single``"
   "**Type**", "Boolean"

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.

When you set the policy to Single, all connections route to the server with the highest weight value.  You can enable this by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

.. code-block:: console

   # glbd --single 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-source`:
.. rst-class:: section-heading
.. rubric:: ``--source``

Defines the destination selection policy as Source Tracking.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-s``"
   "**Syntax**", "``--source``"
   "**Type**", "Boolean"

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Source Tracking, connections that originate from one address are routed to the same destination.  That is, you can ensure that certain IP addresses always route to the same destination server.  You can enable this by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

Bear in mind, there are some limitations to this selection policy.  When the destination list changes, the destination choice for new connections changes as well, while established connections remain in place.  Additionally, when a destination is marked as unavailable, all connections that would route to it fail over to another, randomly chosen destination.  When the original target becomes available again, routing to it for new connections resumes.  In other words, Source Tracking works best with short-lived connections.

For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.

.. code-block:: console

   # glbd --source 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-threads-arg`:
.. rst-class:: section-heading
.. rubric:: ``--threads``

Defines the number of threads that you want to use.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-t``"
   "**Syntax**", "``--threads N``"
   "**Type**", "Integer"

For more information on threading in Galera Load Balancer, see :ref:`THREADS <glb-threads-par>`.

.. code-block:: console

   # glbd --threads 6 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-top`:
.. rst-class:: section-heading
.. rubric:: ``--top``

Enables balancing to top weights only.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-T``"
   "**Syntax**", "``--top``"
   "**Type**", "Boolean"

This option restricts all balancing policies to a subset of destination servers with the top weight.  For instance, if you have servers with weights ``1``, ``2`` and ``3``, balancing occurs only on servers with weight ``3``, while they remain available.

.. code-block:: console

   # glbd --top 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-verbose`:
.. rst-class:: section-heading
.. rubric:: ``--verbose``

Defines whether you want Galera Load Balancer to run as verbose.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-v``"
   "**Syntax**", "``--verbose``"
   "**Type**", "Boolean"

This option enables verbose output for Galera Load Balancer, which you may find useful for debugging purposes.

.. code-block:: console

   # glbd --verbose 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. _`glb-watchdog`:
.. rst-class:: section-heading
.. rubric:: ``--watchdog``

Defines specifications for watchdog operations.

.. csv-table::
   :class: doc-options

   "**Short Argument**", "``-w``"
   "**Syntax**", "``--watchdog SPEC_STR``"
   "**Type**", "String"

Under normal operation, Galera Load Balancer checks destination availability by attempting to establish a TCP connection to the server.  For most use cases, this is insufficient.  If you want to establish a connection with web server, you need to know if it is able to serve web pages.  If you want to establish a connection with a database server, you need to know if it is able to execute queries.  TCP connections don't provide that kind of information.

The Watchdog module implements asynchronous monitoring of destination servers through back-ends designed to service availability.  This option allows you to enable it by defining the back-end ID string, optionally followed by a colon and the configuration options.

.. code-block:: console

   # glbd -w exec:"mysql.sh -utest -ptestpass" 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

This initializes the ``exec`` back-end to execute external programs.  It runs the ``mysql.sh`` script on each destination server in order to determine it's availability.  You can find the ``mysql.sh`` in the Galera Load Balancer build directory, under ``files/``.

.. note:: The Watchdog module remains a work in progress.  Neither its functionality nor terminology is final.
