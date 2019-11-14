.. meta::
   :title: Galera Cluster Arbitrator
   :description: Galera Arbitrator serves can function as an odd node to avoid split-brain and can be useful in making back-ups.
   :language: en-US
   :keywords: galera cluster, mysql, mariadb, arbitrator, garbd
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

      - :doc:`backup-cluster`
      - :doc:`galera-parameters`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`arbitrator`:

===================
 Galera Arbitrator
===================

.. index::
   pair: Descriptions; Galera Arbitrator
.. index::
   single: Split-brain; Prevention
.. index::
   pair: Logs; Galera Arbitrator

When deploying a Galera Cluster, it's recommended that you use a minimum of three instances: Three nodes, three data centers and so on.

If the cost of adding resources (e.g., a third data center) is too much, you can use :term:`Galera Arbitrator`.  Galera Arbitrator is a member of a cluster that participates in voting, but not in the actual replication.

.. warning:: While Galera Arbitrator does not participate in replication, it does receive the same data as all other nodes.  You must secure its network connection.

Galera Arbitrator serves two purposes: When you have an even number of nodes, it functions as an odd node, to avoid split-brain situations. It can also request a consistent application state snapshot, which is useful in making backups.

.. figure:: ../images/arbitrator.png

*Galera Arbitrator*

If one datacenter fails or loses its :abbr:`WAN (Wide Area Network)` connection, the node that sees the arbitrator---and by extension sees clients---continues operation.

.. note:: Even though Galera Arbitrator doesn't store data, it must see all replication traffic.  Placing Galera Arbitrator in a location with poor network connectivity to the rest of the cluster may lead to poor cluster performance.

In the event that Galera Arbitrator fails, it won't affect cluster operation.  You can attach a new instance to the cluster at any time and there can be several instances running in the cluster.

For more information on using Galera Arbitrator for making backups, see :doc:`backup-cluster`.


.. _`starting-arbitrator`:
.. rst-class:: section-heading
.. rubric:: Starting Galera Arbitrator

Galera Arbitrator is a separate daemon from Galera Cluster, called ``garbd``.  This means that you must start it separately from the cluster.  It also means that you cannot configure Galera Arbitrator through the ``my.cnf`` configuration file.

How you configure Galera Arbitrator depends on how you start it.  That is to say, whether it runs from the shell or as a service. These two methods are described in the next two sections.

.. note::  When Galera Arbitrator starts, the script executes a ``sudo`` statement as the user ``nobody`` during its process.  There is a particular issue in Fedora and some other distributions of Linux, in which the default ``sudo`` configuration will block users that operate without ``tty`` access.  To correct this, edit with a text editor the ``/etc/sudoers`` file and comment out this line:

	   .. code-block:: bash

	      Defaults requiretty

	   This will prevent the operating system from blocking Galera Arbitrator.



.. _`arbitrator-shell-start`:
.. rst-class:: section-heading
.. rubric:: Starting Galera Arbitrator from the Shell

When starting Galera Arbitrator from the shell, you have two options as to how you may configure it.  You can set the parameters through the command line arguments, as in the example here:

.. code-block:: console

   $ garbd --group=example_cluster \
        --address="gcomm://192.168.1.1,192.168.1.2,192.168.1.3" \
        --option="socket.ssl_key=/etc/ssl/galera/server-key.pem;socket.ssl_cert=/etc/ssl/galera/server-cert.pem;socket.ssl_ca=/etc/ssl/galera/ca-cert.pem;socket.ssl_cipher=AES128-SHA256""

If you use SSL, it's necessary to specify the cipher. Otherwise, after initializing the ssl context an error will occur with a message saying, "Terminate called after throwing an instance of 'gu::NotSet'".

If you don't want to enter the options every time you start Galera Arbitrator from the shell, you can set the options in the ``arbtirator.config`` configuration file:

.. code-block:: linux-config

   # arbtirator.config
   group = example_cluster
   address = gcomm://192.168.1.1,192.168.1.2,192.168.1.3

Then, to enable those options when you start Galera Arbitrator, use the ``--cfg`` option like so:

.. code-block:: console

   $ garbd --cfg /path/to/arbitrator.config

For more information on the options available to Galera Arbitrator through the shell, run ``garbd`` with the ``--help`` argument.

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


In addition to the standard configuration, any parameter available to Galera Cluster also works with Galera Arbitrator, except for those prefixed by ``repl``.  When you start it from the shell, you can set those using the ``--option`` argument.

For more information on the options available to Galera Arbitrator, see :doc:`galera-parameters`.


.. _`arbitrator-service-start`:
.. rst-class:: section-heading
.. rubric:: Starting Galera Arbitrator as a Service

When starting Galera Aribtrator as a service, whether using ``init`` or ``systemd``, you would use a different format for the configuration file than you would use when starting it from the shell. Below is an example of the configuration file:

.. code-block:: linux-config

   # Copyright (C) 2013-2015 Codership Oy
   # This config file is to be sourced by garbd service script.

   # A space-separated list of node addresses (address[:port]) in the cluster:
   GALERA_NODES="192.168.1.1:4567 192.168.1.2:4567"

   # Galera cluster name, should be the same as on the rest of the node.
   GALERA_GROUP="example_wsrep_cluster"

   # Optional Galera internal options string (e.g. SSL settings)
   # see https://galeracluster.com/documentation-webpages/galeraparameters.html
   GALERA_OPTIONS="socket.ssl_cert=/etc/galera/cert/cert.pem;socket.ssl_key=/$"

   # Log file for garbd. Optional, by default logs to syslog
   LOG_FILE="/var/log/garbd.log"

In order for Galera Arbitrator to use the configuration file, you must place it in a file directory where your system looks for service configuration files.  There is no standard location for this directory; it varies from distribution to distribution, though it usually in ``/etc`` and at least one sub-directory down. Some common locations include:

- ``/etc/defaults/``

- ``/etc/init.d/``

- ``/etc/systemd/``

- ``/etc/sysconfig/``

Check the documentation for the operating system distribution your server uses to determine where to place service configuration files.

Once you have the service configuration file in the right location, you can start the ``garb`` service.  For systems that use ``init``, run the following command:

.. code-block:: console

   # service garb start

For systems that run ``systemd``, use instead this command:

.. code-block:: console

   # systemctl start garb

This starts Galera Arbitrator as a service.  It uses the parameters set in the configuration file.

In addition to the standard configuration, any parameter available to Galera Cluster also works with Galera Arbitrator, excepting those prefixed by ``repl``.  When you start it as a service, you can set those using the ``GALERA_OPTIONS`` parameter.

For more information on the options available to Galera Arbitrator, see :doc:`galera-parameters`.

.. container:: bottom-links

   Related Documents

   - :doc:`backup-cluster`
   - :doc:`galera-parameters`
