.. cssclass:: library-document
.. _`jails`:

==============
Using Jails
==============

In FreeBSD, jails provides a platform for securely deploying applications within virtual instances.  You may find it useful in portable deployments across numerous machines for testing and security.

Galera Cluster can run from within a jail instance.

.. _`jails-prep-serve`:

--------------------------
Preparing the Server
--------------------------

Jails exist as isolated file systems within, but unaware of, the host server.  In order to grant the node running within the jail network connectivity with the cluster, you need to configure the network interfaces and firewall to redirect from the host into the jail.

.. _`jail-net-config`:

^^^^^^^^^^^^^^^^^^^^^
Network Configuration
^^^^^^^^^^^^^^^^^^^^^

To begin, create a second loopback interface for the jail.  this allows you to isolate jail traffic from ``lo0``, the host loopback interface.

.. note:: For the purposes of this guide, the jail loopback is called ``lo1``, if ``lo1`` already exists on your system, increment the digit to create one that does not already exist, (for instance, ``lo2``).

To create a loopback interface, complete the following steps:

#. Using your preferred text editor, add the loopback interface to ``/etc/rc.conf``:

   .. code-block:: console

      # Network Interface
      cloned_interfaces="${cloned_interfaces} lo1"

#. Create the loopback interface:

   .. code-block:: console

      # service netif cloneup

This creates ``lo1``, a new loopback network interface for your jails.  You can view the new interface in the listing using the following command:

.. code-block:: console

   $ ifconfig


.. _`jails-pf`:

^^^^^^^^^^^^^^^^^^^^^^^
Firewall Configuration
^^^^^^^^^^^^^^^^^^^^^^^

FreeBSD provides packet filtering support at the kernel level.  Using PF you can set up, maintain and inspect the packet filtering rule sets.  For jails, you can route traffic from external ports on the host system to internal ports within the jail's file system.  This allows the node running within the jail to have network access as though it were running on the host system.

To enable PF and create rules for the node, complete the following steps:

#. Using your preferred text editor, make the following additions to ``/etc/rc.conf``:

   .. code-block:: console

      # Firewall Configuration
      pf_enable="YES"
      pf_rules="/etc/pf.conf"
      pflog_enable="YES"
      pflog_logfile="/var/log/pf.log"

#. Create the rules files for PF at ``/etc/pf.conf``

   .. code-block:: console

      # External Network Interface
      ext_if="vtnet0"

      # Internal Network Interface
      int_if="lo1"

      # IP Addresses
      external_addr="host_IP_address"
      internal_addr="jail_IP_address_range"

      # Variables for Galera Cluster
      wsrep_ports="{3306,4567,4568,4444}"
      table <wsrep_cluster_address> persist {192.168.1.1,192.168.1.2,192.168.1.3}

      # Translation
      nat on $ext_if from $internal_addr to any -> ($ext_if)

      # Redirects
      rdr on $ext_if proto tcp from any to $external_addr/32 port 3306 -> jail_IP_address port 3306
      rdr on $ext_if proto tcp from any to $external_addr/32 port 4567 -> jail_IP_address port 4567
      rdr on $ext_if proto tcp from any to $external_addr/32 port 4568 -> jail_IP_address port 4568
      rdr on $ext_if proto tcp from any to $external_addr/32 port 4444 -> jail_IP_address port 4444

      pass in proto tcp from <wsrep_cluster_address> to any port $wsrep_ports keep state

   Replace ``host_IP_address`` with the IP address of the host server and ``jail_IP_address`` with the IP address you want to use for the jail.

#. Using ``pfctl``, check for any typos in your PF configurations:

   .. code-block:: console

      # pfctl -v -nf /etc/pf.conf

#. If ``pfctl`` runs without throwing any errors, start PF and PF logging services:

   .. code-block:: console

      # service pf start
      # service pflog start

The server now uses PF to manage its firewall.  Network traffic directed at the four ports Galera Cluster uses is routed to the comparable ports within the jail.

For more information on firewall configurations for FreeBSD, see :doc:`firewall-pf`.


.. _`jail-creation`:

----------------------
Creating the Node Jail
----------------------

While FreeBSD does provide a manual interface for creating and managing jails on your server, (``jail(8)``), it can prove cumbersome in the event that you have multiple jails running on a server.

The application ``ezjail`` facilitates this process by automating common tasks and using templates and symbolic links to reduce the disk space usage per jail.  It is available for installation through ``pkg``.  Alternative, you can build it through ports at ``sysutils/ezjail``.

To create a node jail with ``ezjail``, complete the following steps:

#. Using your preferred text editor, add the following line to ``/etc/rc.conf``:

   .. code-block:: console

      ezjail_enable="YES"

   This allows you to start and stop jails through the ``service`` command.

#. Initialize the ``ezjail`` environment:

   .. code-block:: console

      # ezjail-admin install -sp

   This install the base jail system at ``/usr/jails/``.  It also installs a local build of the ports tree within the jail.

   .. note:: While the database server is not available for FreeBSD in ports or as a package binary, a port of the :term:`Galera Replication Plugin` is available at ``databases/galera``.

#. Create the node jail.

   .. code-block:: console

      # ezjail-admin create galera-node 'lo1|192.168.68.1'

   This creates the particular jail for your node and links it to the ``lo1`` loopback interface and IP address.  Replace the IP address with the local IP for internal use on your server.  It is the same address as you assigned in the firewall redirects above for ``/etc/pf.conf``.

   .. note:: Bear in mind that in the above command ``galera-node`` provides the hostname for the jail file system.  As Galera Cluster draws on the hostname for the default node name, you need to either use a unique jail name for each node, or manually set :ref:`wsrep_node_name <wsrep_node_name>` in the configuration file to avoid confusion.

#. Copy the ``resolve.conf`` file from the host file system into the node jail.

   .. code-block:: console

      # cp /etc/resolv.conf /usr/jails/galera-node/etc/

   This allows the network interface within the jail to resolve domain names in connecting to the internet.

#. Start the node jail.

   .. code-block:: console

      # ezjail-admin start galera-node

The node jail is now running on your server.  You can view running jails using the ``ezjail-admin`` command:

.. code-block:: console

   # ezjail-admin list
   STA JID  IP            Hostname     Root Directory
   --- ---- ------------- ------------ ----------------------
   DR  2    192.168.68.1  galera-node  /usr/jails/galera-node

While on the host system, you can access and manipulate files and directories in the jail file system from ``/usr/jails/galera-node/``.  Additionally, you can enter the jail directly and manipulate processes running within using the following command:

.. code-block:: console

   root@FreeBSDHost:/usr/jails # ezjail-admin console galera-node
   root@galera-node:~ #

When you enter the jail file system, note that the hostname changes to indicate the transition.


.. _`jails-galera-install`:

--------------------------
Installing Galera Cluster
--------------------------

Regardless of whether you are on the host system or working from within a jail, currently, there is no binary package or port available to fully install Galera Cluster on FreeBSD.  You must build the database server from source code.

The specific build process that you need to follow depends on the database server that you want to use:

- :doc:`Galera Cluster for MySQL <install-mysql-src>`
- :doc:`MariaDB Galera Cluster <install-mariadb-src>`

Due to certain Linux dependencies, the :term:`Galera Replication Plugin` cannot be built from source on FreeBSD.  Instead you can use the port at ``/usr/ports/databases/galera`` or install it from a binary package within the jail:

.. code-block:: console

   # pkg install galera

This install the wsrep Provider file in ``/usr/local/lib``.  Use this path in the configuration file for the :ref:`wsrep_provider <wsrep_provider>` parameter.


.. _`jails-node-config`:

^^^^^^^^^^^^^^^^^^^^^^^
Configuration File
^^^^^^^^^^^^^^^^^^^^^^^

For the most part, the configuration file for a node running in a jail is the same as when the node runs on a standard FreeBSD server.  But, there are some parameters that draw their defaults from the base system.  These you need to set manually, as the jail is unable to access the host file system.

- :ref:`wsrep_node_address <wsrep_node_address>` The node determines the default address from the IP address on the first network interface.  Jails cannot see the network interfaces on the host system.  You need to set this parameter to ensure that the cluster is given the correct IP address for the node.

- :ref:`wsrep_node_name <wsrep_node_name>` The node determines the default name from the system hostname.  Jails have their own hostnames, distinct from that of the host system.

.. code-block:: console

   [mysqld]
   user=mysql
   #bind-address=0.0.0.0

   # Cluster Options
   wsrep_provider=/usr/lib/libgalera_smm.so
   wsrep_cluster_address="gcomm://192.168.1.1, 192.168.1.2, 192.16.1.3"
   wsrep_node_address="192.168.1.1"
   wsrep_node_name="node1"
   wsrep_cluster_name="example_cluster"

   # InnoDB Options
   default_storage_engine=innodb
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0

   # SST
   wsrep_sst_method=rsync

If you are logged into the jail console, place the configuration file at ``/etc/my.cnf``.  If you are on the host system console, place it at ``/usr/jails/galera-node/etc/my.cnf``.  Replace ``galera-node`` in the latter with the name of the node jail.


.. _`jails-galera-start`:

---------------------------
Starting the Cluster
---------------------------

When running the cluster from within jails, you create and manage the cluster in the same manner as you would in the standard deployment of Galera Cluster on FreeBSD.  The exception being that you must obtain console access to the node jail first.

To start the initial cluster node, run the following commands:

.. code-block:: console

   # ezjail-admin console galera-node
   # service mysql start --wsrep-new-cluster

To start each additional node, run the following commands:

.. code-block:: console

   # ezjail-admin console galera-node
   # service mysql start

Each node you start after the initial will attempt to establish network connectivity with the :term:`Primary Component` and begin syncing their database states into one another.
