=========================
Using Jails on FreeBSD
=========================
.. _`galera-jails`:

In FreeBSD, jails provides a platform for securely deploying applications within virtual instances.  You may find it useful in portable deployments across numerous machines for testing and security.

Galera Cluster can run from within a jail instance.

--------------------------
Preparing the Server
--------------------------
.. _`jails-prep-serve`:

Jails exist as isolated file systems within, but unaware of the host server.  In order to grant the node running within the jail network connectivity with the cluster, you need to configure the network interfaces and firewall to redirect from the host into the jail.

^^^^^^^^^^^^^^^^^^^^^
Network Configuration
^^^^^^^^^^^^^^^^^^^^^
.. _`jail-net-config`:

To begin, create a second loopback interface for the jail.  this allows you to isolate jail traffic from ``lo0``, the host loopback interface.

.. note:: For the purposes of this guide, the jail loopback is called ``lo1``, if ``lo1`` already exists on your system, increment the digit to create one that does not already exist, (for instance, ``lo2``).

To create a loopback interface, complete the following steps:

#. Add the loopback interface to ``/etc/rc.conf``:

   .. code-block:: ini
   
      # Network Interface
      cloned_interfaces="${cloned_interfaces} lo1"

#. Create the loopback interface:   

   .. code-block:: console

      # service netif cloneup

This creates ``lo1``, a new loopback network interface for your jails.  You can view the new interface in the listing using the following command:

.. code-block:: console

   $ ifconfig

		

^^^^^^^^^^^^^^^^^^^^^^^
Firewall Configuration
^^^^^^^^^^^^^^^^^^^^^^^
.. _`jails-pf`:

FreeBSD provides packet filtering support at the kernel level.  Using PF you can set up, maintain and inspect the packet filtering rule sets.  For jails, you can route traffic from external ports on the host system to internal ports within the jail's file system.  This allows the node running within the jail to function as though it were running on the host system.

#. Using your preferred text editor, make the following additions to ``/etc/rc.conf``:

   .. code-block:: ini

      # Firewall Configuration
      pf_enable="YES"
      pf_rules="/etc/pf.conf"
      pflog_enable="YES"
      pflog_logfile="/var/log/pf.log"

#. Create the rules files for PF at ``/etc/pf.conf``
      
   .. code-block:: ini

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
		
.. seealso:: For more information on firewall configurations for FreeBSD, see :doc:`pf`.
   
----------------------
Creating the Node Jail
----------------------
.. _`jail-creation`:

While FreeBSD does provide a manual interface in ``jail(8)`` for creating and managing jails on your servers, it can prove cumbersome in managing multiple instances per server.  The application ``ezjail`` handles this process, automating common tasks and using templates and symbolic links to reduce the need for disk space.

It is available for installation through ``pkg``.  Alternative, you can build it through ports at ``sysutils/ezjail``.

#. Using your preferred text editor, add the following line to ``/etc/rc.conf``:

   .. code-block:: ini
		   
      ezjail_enable="YES"

   This enables ``ezjail`` on startup and allows you to start and stop jails through the ``service`` command.

#. Initialize the ``ezjail`` environment:

   .. code-block:: console

      # ezjail-admin install -sp

   This install the base jail system at ``/usr/jails/``.  It also installs a local build of the ports tree for your jails to use.

#. Create the node jail.

   .. code-block:: console
   
      # ezjail-admin create galera-node 'lo1|jail_IP_address'

   This creates the particular jail for your node and links it to the ``lo1`` loopback interface and IP address.

   Replace ``jail_IP_address`` with a local IP address for internal use.  Use the same address as you assigned in the firewall redirects for ``/etc/pf.conf`` above.

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

While on the host system, you can access and manipulate files and directories in the jail file system from ``/usr/jails/galera-node/``.  Additionally, you can enter the jail directly and manipulate processes running within.
 
.. code-block:: console

   root@FreeBSDHost:/usr/jails # ezjail-admin console galera-node1
   root@galera-node:~ #

When you enter the jail file system, note that the hostname changes to indicate the transition.
   

--------------------------
Installing Galera Cluster
--------------------------
.. _`jails-galera-install`:

Regardless of whether you are on the host system or working from within a jail, currently there is no binary package or port available for installing Galera Cluster on FreeBSD.

The specific build process that you need to follow depends on the database server that you want to use:

- Galera Cluster for MySQL :doc:`installmysqlsrc`.
- Percona XtraDB Cluster :doc:`installxtradbsrc`.
- MariaDB Galera Cluster :doc:`installmariadbsrc`.




---------------------------
Starting the Cluster
---------------------------
.. _`jails-galera-start`:



===========
Old Jails
===========

While FreeBSD does provide a manual interface for creating and managing jails on your servers, ``jail(8)``, it can prove cumbersome in managing multiple instances per server.  The application ``ezjail`` manages this process, automating common tasks and using templates and symbolic links to reduce the need for disk space.  It is available in ports at ``sysutils/ezjail``.

When you have ``ezjail`` installed on your system, you need to initialize the environment.  To do so, run the following command:

.. code-block:: console

   # ezjail-admin install -sp

This creates the base file system for jails to use.  You can view it on the host system at ``/usr/jails``.  This creates a ``basejail``, which is the base operating system all jails use, as well as flavors, which contain additional configuration settings that you may want to use in particular instances.

Since jails managed through ``ezjail`` rely on a base system to which they are tied through symbolic links, you can update all jails together using the following command:

.. code-block:: console

   # ezjail-admin update



