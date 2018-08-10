================================
Galera Load Balancer Parameters
================================
.. _`glb-parameters`:

Galera Load Balancer provides simple TCP connection balancing developed with scalability and performance in mind.  It draws on Pen for inspiration, but its functionality is limited to only balancing TCP connections.

It can be run either through the ``service`` command or the command-line interface of ``glbd``.  Configuration for Galera Load Balancer depends on which you use to run it.


----------------------------
Configuration Parameters
----------------------------
.. _`glb-config-parameters`:

When Galera Load Balancer starts as a system service, it reads the ``glbd.cfg`` configuration file for default parameters you want to use.  Only the :ref:`LISTEN_ADDR <glb-listen_addr>` parameter is mandatory.

+------------------------+------------------------+
| Parameter              | Default Configuration  |
+========================+========================+
| :ref:`CONTROL_ADDR     | ``127.0.0.1:8011``     |
| <glb-control_addr>`    |                        |
+------------------------+------------------------+
| :ref:`CONTROL_FIFO     | ``/var/run/glbd.fifo`` |
| <glb-control_fifo>`    |                        |
+------------------------+------------------------+
| :ref:`DEFAULT_TARGETS  | ``127.0.0.1:80         |
| <glb-default_targets>` | 10.0.1:80              |
|                        | 10.0.0.2:80``          |
+------------------------+------------------------+
| :ref:`LISTEN_ADDR      | ``8010``               |
| <glb-listen_addr>`     |                        |
+------------------------+------------------------+
| :ref:`MAX_CONN         |                        |
| <glb-max_conn-par>`    |                        |
+------------------------+------------------------+
| :ref:`OTHER_OPTIONS    |                        |
| <glb-other_options>`   |                        |
+------------------------+------------------------+
| :ref:`THREADS          | ``2``                  |
| <glb-threads-par>`     |                        |
+------------------------+------------------------+



.. rubric:: ``CONTROL_ADDR``
.. _`glb-control_addr`:

Defines the IP address and port for controlling connections.

+----------------------------+--------------------------------+
| **Command-line Argument**  | :ref:`--control <glb-control>` |
+----------------------------+--------------------------------+
| **Default Configuration**  | ``127.0.0.1:8011``             |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This is an optional parameter.  Use it to define the server used in controlling client connections.  When using this parameter you must define the port.  In the event that you do not define this parameter, Galera Load Balancer does not open the relevant socket.

.. code-block:: ini

   CONTROL_ADDR="127.0.0.1:8011"




.. rubric:: ``CONTROL_FIFO``
.. _`glb-control_fifo`:

Defines the path to the FIFO control file.

+----------------------------+--------------------------------+
| **Command-line Argument**  | :ref:`--fifo <glb-fifo>`       |
+----------------------------+--------------------------------+
| **Default Configuration**  | ``/var/run/glbd.fifo``         |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This is an optional parameter.  It defines the path to the FIFO control file as is always opened.  In the event that there is already a file at this path, Galera Load Balancer fails to start.

.. code-block:: ini

   CONTROL_FIFO="/var/run/glbd.fifo"


.. rubric:: ``DEFAULT_TARGETS``
.. _`glb-default_targets`:

Defines the IP addresses and ports of the destination servers.

+----------------------------+--------------------------------+
| **Default Configuration**  | ``127.0.0.1:80 10.0.0.1:80     |
|                            | 10.0.0.2:80:2``                |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This parameter defines that IP addresses that Galera Load Balancer uses as destination servers.  Specifically, in this case the Galera Cluster nodes that it routes application traffic onto.

.. code-block:: ini

   DEFAULT_TARGETS="192.168.1.1 192.168.1.2 192.168.1.3"


.. rubric:: ``LISTEN_ADDR``
.. _`glb-listen_addr`:

Defines the IP address and port used for client connections.

+----------------------------+--------------------------------+
| **Default Configuration**  | ``8010``                       |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | Yes                            |
+----------------------------+--------------------------------+

This parameter defines the IP address and port that Galera Load Balancer listens on for incoming client connections.  The IP address is optional, the port mandatory.  In the event that you define a port without an IP address, Galera Load Balancer listens on that port for all available network interfaces.

.. code-block:: ini

   LISTEN_ADDR="8010"



.. rubric:: ``MAX_CONN``
.. _`glb-max_conn-par`:

Defines the maximum allowed client connections.

+----------------------------+--------------------------------+
| **Command-line Argument**  | :ref:`--max_conn               |
|                            | <glb-max_conn-arg>`            |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This parameter defines the maximum number of client connections that you want to allow to Galera Load Balancer.  It modifies the system open files limit to accommodate at least this many connections, provided sufficient privileges.  It is recommend that you define this parameter if you expect the number of client connections to exceed five hundred.

.. code-block:: ini

   MAX_CONN="135"


This option defines the maximum number of client connections that you want allow to Galera Load Balancer. Bear in mind, that it can be operating system dependent.

.. rubric:: ``OTHER_OPTIONS``
.. _`glb-other_options`:

Defines additional options that you want to pass to Galera Load Balancer.

+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This parameter defines various additional options that you would like to pass to Galera Load Balancer, such as a destination selection policy or Watchdog configurations.  Use the same syntax as you would for the command-line arguments.  For more information on the available options, see :ref:`Configuration Options <glb-config-options>`.

.. code-block:: ini

   OTHER_OPTIONS="--random --watchdog exec:'mysql -utest -ptestpass' --discover"


.. rubric:: ``THREADS``
.. _`glb-threads-par`:

Defines the number of threads you want to use.

+----------------------------+--------------------------------+
| **Command-line Argument**  | :ref:`--threads                |
|                            | <glb-threads-arg>`             |
+----------------------------+--------------------------------+
| **Mandatory Parameter**    | No                             |
+----------------------------+--------------------------------+

This parameter allows you to define the number of threads (that is, connection pools), which you want to allow Galera Load Balancer to use.  It is advisable that you have at least a few per CPU core.

.. code-block:: ini

   THREADS="6"


----------------------------
Configuration Options
----------------------------
.. _`glb-config-options`:

When Galera Load Balancer starts as a daemon process, through the ``/sbin/glbd`` command, it allows you to pass a number of command-line arguments to configure how it operates.  It uses the following syntax:

.. code-block:: text

   /usr/local/sbin/glbd [OPTIONS] LISTEN_ADDRESS [DESTINATION_LIST]

In the event that you would like to set any of these options when you run Galera Load Balancer as a service, you can define them through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

+----------------------+--------+------------+-------------------------+
| Long Argument        | Short  | Type       | Parameter               |
+======================+========+============+=========================+
| :ref:`--control      | ``-c`` | IP address | :ref:`CONTROL_ADDR      |
| <glb-control>`       |        |            | <glb-control_addr>`     |
+----------------------+--------+------------+-------------------------+
| :ref:`--daemon       | ``-d`` | Boolean    |                         |
| <glb-daemon>`        |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--defer-accept | ``-a`` | Boolean    |                         |
| <glb-defer-accept>`  |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--discover     | ``-D`` | Boolean    |                         |
| <glb-discover>`      |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--extra        | ``-x`` | Decimal    |                         |
| <glb-extra>`         |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--fifo         | ``-f`` | File Path  | :ref:`CONTROL_FIFO      |
| <glb-fifo>`          |        |            | <glb-control_fifo>`     |
+----------------------+--------+------------+-------------------------+
| :ref:`--interval     | ``-i`` | Decimal    |                         |
| <glb-interval>`      |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--keepalive    | ``-K`` | Boolean    |                         |
| <glb-keepalive>`     |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--latency      | ``-L`` | Integer    |                         |
| <glb-latency>`       |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--linger       | ``-l`` | Boolean    |                         |
| <glb-linger>`        |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--max_conn     | ``-m`` | Integer    | :ref:`MAX_CONN          |
| <glb-max_conn-arg>`  |        |            | <glb-max_conn-par>`     |
+----------------------+--------+------------+-------------------------+
| :ref:`--nodelay      | ``-n`` | Boolean    |                         |
| <glb-nodelay>`       |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--random       | ``-r`` | Boolean    |                         |
| <glb-random>`        |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--round        | ``-b`` | Boolean    |                         |
| <glb-round>`         |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--single       | ``-S`` | Boolean    |                         |
| <glb-single>`        |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--source       | ``-s`` | Boolean    |                         |
| <glb-source>`        |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--threads      | ``-t`` | Integer    | :ref:`THREADS           |
| <glb-threads-arg>`   |        |            | <glb-threads-par>`      |
+----------------------+--------+------------+-------------------------+
| :ref:`--top          | ``-T`` | Boolean    |                         |
| <glb-top>`           |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--verbose      | ``-v`` | Boolean    |                         |
| <glb-verbose>`       |        |            |                         |
+----------------------+--------+------------+-------------------------+
| :ref:`--watchdog     | ``-w`` | String     |                         |
| <glb-watchdog>`      |        |            |                         |
+----------------------+--------+------------+-------------------------+


.. rubric:: ``--control``
.. _`glb-control`:

Defines the IP address and port for control connections.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-c``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--control [IP|Hostname:]port`` |
+-----------------------------+----------------------------------+
| **Type**                    | IP Address                       |
+-----------------------------+----------------------------------+
| **Configuration Parameter** | :ref:`CONTROL_ADDR               |
|                             | <glb-control_addr>`              |
+-----------------------------+----------------------------------+

For more information on defining the controlling connections, see the :ref:`CONTROL_ADDR <glb-control_addr>` parameter.

.. code-block:: console

   # glbd --control 192.168.1.1:80 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--daemon``
.. _`glb-daemon`:

Defines whether you want Galera Load Balancer to run as a daemon process.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-d``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--daemon``                     |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

This option defines whether you want to start ``glbd`` as a daemon process.  That is, if you want it to run in the background, instead of claiming the current terminal session.

.. code-block:: console

   # glbd --daemon 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--defer-accept``
.. _`glb-defer-accept`:

Enables TCP deferred acceptance on the listening socket.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-a``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--defer-accept``               |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

Enabling ``TCP_DEFER_ACCEPT`` allows Galera Load Balancer to awaken only when data arrives on the listening socket.  It is disabled by default.

.. code-block:: console

   # glbd --defer-accept 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--discover``
.. _`glb-discover`:

Defines whether you want to use watchdog results to discover and set new destinations.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-D``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--discover``                   |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

When you define the :ref:`--watchdog <glb-watchdog>` option, this option defines whether Galera Load Balancer uses the return value in discovering and setting new addresses for destination servers.  For instance, after querying for the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter.


.. code-block:: console

   # glbd --discover -w exec:"mysql.sh -utest -ptestpass" 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3



.. rubric:: ``--extra``
.. _`glb-extra`:

Defines whether you want to perform an extra destination poll on connection attempts.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-x``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--extra D.DDD``                |
+-----------------------------+----------------------------------+
| **Type**                    | Decimal                          |
+-----------------------------+----------------------------------+

This option defines whether and when you want Galera Load Balancer to perform an additional destination poll on connection attempts.  The given value indicates how many seconds after the previous poll that you want it to run the extra poll.  By default, the extra polling feature is disabled.

.. code-block:: console

   # glbd --extra 1.35 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--fifo``
.. _`glb-fifo`:

Defines the path to the FIFO control file.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-f``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--fifo /path/to/glbd.fifo``    |
+-----------------------------+----------------------------------+
| **Type**                    | File Path                        |
+-----------------------------+----------------------------------+
| **Configuration Parameter** | :ref:`CONTROL_FIFO               |
|                             | <glb-control_fifo>`              |
+-----------------------------+----------------------------------+


For more information on using FIFO control files, see the :ref:`CONTROL_FIFO <glb-control_fifo>` parameter.

.. code-block:: console

   # glbd --fifo /var/run/glbd.fifo 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--interval``
.. _`glb-interval`:

Defines how often to probe destinations for liveliness.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-i``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--interval D.DDD``             |
+-----------------------------+----------------------------------+
| **Type**                    | Decimal                          |
+-----------------------------+----------------------------------+

This option defines how often Galera Load Balancer checks destination servers for liveliness.  It uses values given in seconds.  By default, it checks every second.

.. code-block:: console

   # glbd --interval 2.013 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--keepalive``
.. _`glb-keepalive`:

Defines whether you want to disable the ``SO_KEEPALIVE`` socket option on server-side sockets.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-K``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--keepalive``                  |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

Linux systems feature the socket option ``SO_KEEPALIVE``, which causes the server to send packets to a remote system in order to main the client connection with the destination server.  This option allows you to disable ``SO_KEEPALIVE`` on server-side sockets.  It allows ``SO_KEEPALIVE`` by default.

.. code-block:: console

   # glbd --keepalive 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--latency``
.. _`glb-latency`:

Defines the number of samples to take in calculating latency for watchdog.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-L``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--latency N``                  |
+-----------------------------+----------------------------------+
| **Type**                    | Integer                          |
+-----------------------------+----------------------------------+

When the Watchdog module tests a destination server to calculate latency, it sends a number of packets through to measure its responsiveness.  This option configures how many packets it sends in sampling latency.

.. code-block:: console

   # glbd --latency 25 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--linger``
.. _`glb-linger`:

Defines whether Galera Load Balancer disables sockets lingering after they are closed.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-l``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--linger``                     |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

When Galera Load Balancer sends the ``close()`` command, occasionally sockets linger in a ``TIME_WAIT`` state.  This options defines whether or not you want Galera Load Balancer to disable lingering sockets.

.. code-block:: console

   # glbd --linger 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--max_conn``
.. _`glb-max_conn-arg`:

Defines the maximum allowed client connections.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-m``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--max_conn N``                 |
+-----------------------------+----------------------------------+
| **Type**                    | Integer                          |
+-----------------------------+----------------------------------+

For more information on defining the maximum client connections, see the :ref:`MAX_CONN <glb-max_conn-par>` parameter.

.. code-block:: console

   # glbd --max_conn 125 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--nodelay``
.. _`glb-nodelay`:

Defines whether it disables the TCP no-delay socket option.


+-----------------------------+----------------------------------+
| **Short Argument**          | ``-n``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--nodelay``                    |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

Under normal operation, TCP connections automatically concatenate small packets into larger frames through the Nagle algorithm.  In the event that you want Galera Load Balancer to disable this feature, this option causes it to open TCP connections with the ``TCP_NODELAY`` feature.

.. code-block:: console

   # glbd --nodelay 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--random``
.. _`glb-random`:

Defines the destination selection policy as Random.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-r``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--random``                     |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Random, it randomly chooses a destination from the pool of available servers.  You can enable this feature by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.


For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.

.. code-block:: console

   # glbd --random 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--round``
.. _`glb-round`:

Defines the destination selection policy as Round Robin.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-b``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--round``                      |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Round Robin, it directs new connections to the next server in a circular order list.  You can enable this feature by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.


.. code-block:: console

   # glbd --round 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--single``
.. _`glb-single`:

Defines the destination selection policy as Single.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-S``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--single``                     |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.

When you set the policy to Single, all connections route to the server with the highest weight value.  You can enable this by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

.. code-block:: console

   # glbd --single 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3



.. rubric:: ``--source``
.. _`glb-source`:

Defines the destination selection policy as Source Tracking.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-s``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--source``                     |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

The destination selection policy determines how Galera Load Balancer determines which servers to route traffic to.  When you set the policy to Source Tracking, connections that originate from one address are routed to the same destination.  That is, you can ensure that certain IP addresses always route to the same destination server.  You can enable this by default through the :ref:`OTHER_OPTIONS <glb-other_options>` parameter.

Bear in mind, there are some limitations to this selection policy.  When the destination list changes, the destination choice for new connections changes as well, while established connections remain in place.  Additionally, when a destination is marked as unavailable, all connections that would route to it fail over to another, randomly chosen destination.  When the original target becomes available again, routing to it for new connections resumes.  In other words, Source Tracking works best with short-lived connections.

For more information on other policies, see :ref:`Destination Selection Policies <glb-dest-select>`.

.. code-block:: console

   # glbd --source 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--threads``
.. _`glb-threads-arg`:

Defines the number of threads that you want to use.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-t``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--threads N``                  |
+-----------------------------+----------------------------------+
| **Type**                    | Integer                          |
+-----------------------------+----------------------------------+

For more information on threading in Galera Load Balancer, see :ref:`THREADS <glb-threads-par>`.

.. code-block:: console

   # glbd --threads 6 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

.. rubric:: ``--top``
.. _`glb-top`:

Enables balancing to top weights only.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-T``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--top``                        |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

This option restricts all balancing policies to a subset of destination servers with the top weight.  For instance, if you have servers with weights ``1``, ``2`` and ``3``, balancing occurs only on servers with weight ``3``, while they remain available.

.. code-block:: console

   # glbd --top 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3




.. rubric:: ``--verbose``
.. _`glb-verbose`:

Defines whether you want Galera Load Balancer to run as verbose.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-v``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--verbose``                    |
+-----------------------------+----------------------------------+
| **Type**                    | Boolean                          |
+-----------------------------+----------------------------------+

This option enables verbose output for Galera Load Balancer, which you may find useful for debugging purposes.

.. code-block:: console

   # glbd --verbose 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3


.. rubric:: ``--watchdog``
.. _`glb-watchdog`:

Defines specifications for watchdog operations.

+-----------------------------+----------------------------------+
| **Short Argument**          | ``-w``                           |
+-----------------------------+----------------------------------+
| **Syntax**                  | ``--watchdog SPEC_STR``          |
+-----------------------------+----------------------------------+
| **Type**                    | String                           |
+-----------------------------+----------------------------------+

Under normal operation, Galera Load Balancer checks destination availability by attempting to establish a TCP connection to the server.  For most use cases, this is insufficient.  If you want to establish a connection with web server, you need to know if it is able to serve web pages.  If you want to establish a connection with a database server, you need to know if it is able to execute queries.  TCP connections don't provide that kind of information.

The Watchdog module implements asynchronous monitoring of destination servers through back-ends designed to service availability.  This option allows you to enable it by defining the back-end ID string, optionally followed by a colon and the configuration options.

.. code-block:: console

   # glbd -w exec:"mysql.sh -utest -ptestpass" 3306 \
         192.168.1.1 192.168.1.2 192.168.1.3

This initializes the ``exec`` back-end to execute external programs.  It runs the ``mysql.sh`` script on each destination server in order to determine it's availability.  You can find the ``mysql.sh`` in the Galera Load Balancer build directory, under ``files/``.

.. note:: The Watchdog module remains a work in progress.  Neither its functionality nor terminology is final.


