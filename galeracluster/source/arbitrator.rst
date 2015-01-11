===================
 Galera Arbitrator
===================
.. _`arbitrator`:

.. index::
   pair: Descriptions; Galera Arbitrator
.. index::
   single: Split-brain; Prevention
.. index::
   pair: Logs; Galera Arbitrator

The recommended deployment of Galera Cluster is that you use a minimum of three instances.  Three nodes, three datacenters and so on.

In the event that the expense of adding resources, such as a third datacenter, is too costly, you can use Galera Arbitrator.  ``garbd`` is a member of the cluster that participates in voting, but not in the actual replication.

.. warning:: While Galera Arbitrator does not participate in replication, it does receive the same data as all other nodes.  You must secure its network connection.

Galera Arbitrator serves two purposes:

- In the event that the cluster spreads only over two nodes, it functions as an odd node.

- It can request a consistent application state snapshot.

.. figure:: images/arbitrator.png

   *Galera Arbitrator*

If one datacenter fails or loses :abbr:`WAN (Wide Area Network)` connection, the node that sees the arbitrator, and by extension sees clients, continues operation.

.. note:: Even though Galera Arbitrator does not store data, it must see all replication traffic.  Placing ``garbd`` in a location with poor network connectivity to the rest of the cluster may lead to poor cluster performance.

In the event that ``garbd`` fails, it does not affect cluster operation.  You can attach a new instance to the cluster at any time and there can be several instances running in the cluster.



--------------------------------
 Configuring Galera Arbitrator
--------------------------------
.. _`arbitrator-configuration`:
.. index::
   pair: Configuration; Galera Arbitrator

Galera Arbitrator functions as a member of the cluster.  Any configuration parameters that you can use with a given node you can also apply to the Arbitrator, except those parameters

with the exception of those parameters prefixed by ``repl``.


.. code-block:: linux-config

   # Copyright (C) 2013 Codership Oy
   # This config file is to be sourced by garbd service script.
   
   # A space-separated list of node addresses (address[:port]) in the cluster:
   GALERA_NODES="192.168.1.1:4567 192.168.1.2:4567"

   # Galera cluster name, should be the same as on the rest of the node.
   GALERA_GROUP="example_wsrep_cluster"

   # Optional Galera internal options string (e.g. SSL settings)
   # see http://www.codership.com/wiki/doku.php?id=galera_parameters
   GALERA_OPTIONS="socket.ssl_cert = /etc/galera/cert/cert.pem; socket.ssl_key = /$"
    
   # Log file for garbd. Optional, by default logs to syslog
   LOG_FILE="/var/log/garbd.log"



.. seealso:: For more information of the configuration parameters available to Galera Arbitrator, see :doc:`Galera Parameters <galeraparameters>`.



----------------------------
 Starting Galera Arbitrator
----------------------------
.. _`starting-arbitrator`:

Galera Arbitrator is a separate daemon from Galera Cluster, called ``garbd``.  You need to start it separate from the cluster.

.. code-block:: console

   $ garbd --help
   
   Usage: garbd [options] [group address]

   Configuration:
     -d [ --daemon ]       Become daemon
     -n [ --name ] arg     Node name
     -a [ --address ] arg  Group address
     -g [ --group ] arg    Group name
     --sst arg             SST request string
     --donor arg           SST donor name
     -o [ --options ] arg  GCS/GCOMM option list
     -l [ --log ] arg      Log file
     -c [ --cfg ] arg      Configuration file

   Other options:
     -v [ --version ]      Print version
     -h [ --help ]         Show help message


For systems that use ``init``, you can start the ``garb`` service using the following command:

.. code-block:: console

   # service garb start

For systems that run ``systemd``, instead use this command:

.. code-block:: console

   # systemctl start garb

When you start ``garbd`` you can pass options through the command, or you can set these options through the configuration file.

   
You can set Galera Arbitrator options manually when starting ``garbd``.  Alternatively, you can set the configurations to load every time ``garbd`` starts using the configuration file described above.

