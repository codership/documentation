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

In the event that the expense of adding resources, such as a third datacenter, is too costly, you can use :term:`Galera Arbitrator`.  Galera Arbitrator is a member of the cluster that participates in voting, but not in the actual replication.

.. note:: **Warning** While Galera Arbitrator does not participate in replication, it does receive the same data as all other nodes.  You must secure its network connection.

Galera Arbitrator serves two purposes:

- When you have an even number of nodes, it functions as an odd node, to avoid split-brain situations.

- It can request a consistent application state snapshot, for use in making backups.

.. figure:: images/arbitrator.png

   *Galera Arbitrator*

If one datacenter fails or loses :abbr:`WAN (Wide Area Network)` connection, the node that sees the arbitrator, and by extension sees clients, continues operation.

.. note:: Even though Galera Arbitrator does not store data, it must see all replication traffic.  Placing Galera Arbitrator in a location with poor network connectivity to the rest of the cluster may lead to poor cluster performance.

In the event that Galera Arbitrator fails, it does not affect cluster operation.  You can attach a new instance to the cluster at any time and there can be several instances running in the cluster.

.. note:: **See Also**: For more information on using Galera Arbitrator in making backups, see :doc:`backingupthecluster`.


-----------------------------
Starting Galera Arbitrator
-----------------------------
.. _`starting-arbitrator`:

Galera Arbitrator is a separate daemon from Galera Cluster, called ``garbd``.  This means that you must start it separate from the cluster.  It also means that you cannot configure Galera Arbitrator through the ``my.cnf`` configuration file.

How you configure Galera Arbitrator depends on how you start it.  That is, whether it runs from the shell or as a service.

.. note::  When Galera Arbitrator starts, the script executes a ``sudo`` statement as the user ``nobody`` during its process.  There is a particular issue in Fedora and some other distributions of Linux, where the default ``sudo`` configuration blocks users that operate without ``tty`` access.  To correct this, using your preferred text editor, edit the ``/etc/sudoers`` file and comment out the line 

	   .. code-block:: bash

	      Defaults requiretty

	   This prevents the operating system from blocking Galera Arbitrator.

			      



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting Galera Arbitrator from the Shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`arbitrator-shell-start`:

When starting Galera Arbitrator from the shell, you have two options in how you configure it.  Firstly, you can set the parameters through the command line arguments.  For example,

.. code-block:: console

   $ garbd --group=example_cluster \
        --address="gcomm://192.168.1.1,192.168.1.2,192.168.1.3" \
        --option="socket.ssl_key=/etc/ssl/galera/server-key.pem;socket.ssl_cert=/etc/ssl/galera/server-cert.pem;socket.ssl_ca=/etc/ssl/galera/ca-cert.pem;socket.ssl_cipher=AES128-SHA""

If you use SSL it is necessary to also specify the cipher, otherwise there will be "terminate called after throwing an instance of 'gu::NotSet'" after initializing the ssl context.

If you do not want to type out the options every time you start Galera Arbitrator from the shell, you can set the options you want to use in a configuration file:

.. code-block:: linux-config

   # arbtirator.config
   group = example_cluster
   address = gcomm://192.168.1.1,192.168.1.2,192.168.1.3

Then, when you start Galera Arbitrator, use the ``--cfg`` option.

.. code-block:: console

   $ garbd --cfg /path/to/arbitrator.config

For more information on the options available to Galera Arbitrator through the shell, run it with the ``--help`` argument.

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


In addition to the standard configurations, any parameter available to Galera Cluster also works with Galera Arbitrator, excepting those prefixed by ``repl``.  When you start it from the shell, you can set these using the ``--option`` argument.

.. note:: **See Also**: For more information on the options available to Galera Arbitrator, see :doc:`galeraparameters`.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting Galera Arbitrator as a Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`arbitrator-service-start`:

When starting Galera Aribtrator as a service, whether using ``init`` or ``systemd``, you use a different format for the configuration file than you would use when starting it from the shell.

.. code-block:: linux-config

   # Copyright (C) 2013-2015 Codership Oy
   # This config file is to be sourced by garbd service script.
   
   # A space-separated list of node addresses (address[:port]) in the cluster:
   GALERA_NODES="192.168.1.1:4567 192.168.1.2:4567"

   # Galera cluster name, should be the same as on the rest of the node.
   GALERA_GROUP="example_wsrep_cluster"

   # Optional Galera internal options string (e.g. SSL settings)
   # see http://galeracluster.com/documentation-webpages/galeraparameters.html
   GALERA_OPTIONS="socket.ssl_cert=/etc/galera/cert/cert.pem;socket.ssl_key=/$"
    
   # Log file for garbd. Optional, by default logs to syslog
   LOG_FILE="/var/log/garbd.log"

In order for Galera Arbitrator to use the configuration file, you must place it in a directory that your system looks to for service configurations.  There is no standard location for this directory, it varies from distribution to distribution, though it usually somewhere in ``/etc``.

Common locations include:

- ``/etc/defaults/``

- ``/etc/init.d/``

- ``/etc/systemd/``

- ``/etc/sysconfig/``
  
Check the documentation for your distribution to determine where to place service configuration files.

Once you have the service configuration file in the right location, you can start the ``garb`` service.  For systems that use ``init``, run the following command:

.. code-block:: console

   # service garb start

For systems that run ``systemd``, instead use this command:

.. code-block:: console

   # systemctl start garb

This starts Galera Arbitrator as a service.  It uses the parameters set in the configuration file.

In addition to the standard configurations, any parameter available to Galera Cluster also works with Galera Arbitrator, excepting those prefixed by ``repl``.  When you start it as a service, you can set these using the ``GALERA_OPTIONS`` parameter.

.. note:: **See Also**: For more information on the options available to Galera Arbitrator, see :doc:`galeraparameters`.



