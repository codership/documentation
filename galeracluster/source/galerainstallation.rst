
==============
Installation
==============
.. _`galera-install-configure`:

Galera Cluster requires server hardware for a minimum of three nodes.

If your cluster runs on a single switch, use three nodes.  If your cluster spans switches, use three switches.  If your cluster spans networks, use three networks.  If your cluster spans data centers, use three data centers.  This ensures that the cluster can maintain a Primary Component in the event of network outages.

For server hardware, each node requires at a minimum:

- 1GHz single core CPU
- 512MB RAM
- 100 Mbps network connectivity

.. note:: **See Also**: Galera Cluster may occasionally crash when run on limited hardware due to insufficient memory.  To prevent this, ensure that you have sufficient swap space available.  For more information on how to create swap space, see :ref:`Configuring Swap Space <swap-config>`.

For software, each node in the cluster requires:

- Linux or FreeBSD;
- MySQL, MariaDB or Percona XtraDB server with wsrep API patch;
- Galera Replication Plugin.

.. note:: Binary installation packages for Galera Cluster include the database server with the wsrep API patch.  When building from source, you must apply this patch yourself.

	  
-------------------------------
Preparing the Server
-------------------------------
.. _`system-requirements`:

Before you begin the installation process, there are a few tasks that you need to undertake to prepare the servers for Galera Cluster.  You must perform the following steps for each node in your cluster.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disabling SELinux for mysqld
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`disable-selinux`:

If you have SELinux enabled, it may block ``mysqld`` from carrying out required operations.  You must either disable SELinux for mysqld or configure it to allow ``mysqld`` to run external programs and open listen sockets on unprivileged ports |---| that is, things that an unprivileged user can do.

To disable SELinux for mysql run the following command:

.. code-block:: console

   # semanage permissive -a mysqld_t

This command switches SELinux into permissive mode when it registers activity from the database server.  While this is fine during the installation and configuration process, it is not in general a good policy to disable applications that improve security.  

In order to use SELinux with Galera Cluster, you need to create an access policy, so that SELinux can understand and allow normal operations from the database server.  For information on how to create an access policy, see :doc:`selinux`.

.. note:: **See Also**: For more information on writing SELinux policies, see `SELinux and MySQL <https://blogs.oracle.com/jsmyth/entry/selinux_and_mysql>`_.
.. Revision Note: Add a label for port 4567 as mysqld_port_t, check if other ports on the firewall need something similar.  Check if AppArmor requires a similar label as well.
	     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Firewall Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`firewall-config`:

Next, you need to update the firewall settings on each node so that they can communicate with the cluster.  How you do this varies depending upon your distribution and the particular firewall software that you use.

.. note:: If there is a :abbr:`NAT (Network Address Translation)` firewall between the nodes, you must configure it to allow for direct connections between the nodes, such as through port forwarding.

As an example, to open ports between trusted hosts using ``iptables`` the commands you run on each  would look something like this:

.. code-block:: console
		
   # iptables --append INPUT --protocol tcp \
         --source 64.57.102.34 --jump ACCEPT
   # iptables --apend INPUT --protocol tcp \
         --source 193.166.33.20 --jump ACCEPT
   # iptables --append INPUT --protocol tcp \
         --source 193.125.4.10 --jump ACCEPT

This causes packet filtering on the kernel to accept :abbr:`TCP (Transmission Control Protocol)` connections between the given IP addresses.

.. note:: **Warning**: The IP addresses in the example are for demonstration purposes only.  Use the real values from your nodes and netmask in the ``iptables`` configuration for your cluster.

The updated packet filtering rules take effect immediately, but are not persistent.  When the server reboots, it reverts to default packet filtering rules, which do not include your updates.  To use these rules after rebooting, you need to save them as defaults.

For systems that use ``init``, run the following command:

.. code-block:: console

   # service save iptables

For systems that use ``systemd``, you need to save the current packet filtering rules to the path that the ``iptables`` unit reads when it starts.  This path can vary by distribution, but you can normally find it in the ``/etc`` directory.

- ``/etc/sysconfig/iptables``
- ``/etc/iptables/iptables.rules``

When you find the relevant file, you can save the rules using the ``iptables-save`` command, then redirecting the output to overwrite this file.

.. code-block:: console

   # iptables-save > /etc/sysconfig/iptables

When ``iptables`` starts it now reads the new defaults, with your updates to the firewall.

.. note:: **See Also**: For more information on setting up the firewall for Galera Cluster and other programs for configuring packet filtering in Linux and FreeBSD, see :doc:`firewallsettings`.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disabling AppArmor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`disable-apparmor`:

By default, some servers |---| for instance, Ubuntu |---| include AppArmor, which may prevent ``mysqld`` from opening additional ports or running scripts.  You must disable AppArmor or configure it to allow ``mysqld`` to run external programs and open listen sockets on unprivileged ports.

To disable AppArmor, run the following commands:

.. code-block:: console

   $ sudo ln -s /etc/apparmor.d/usr /etc/apparmor.d/disable/.sbin.mysqld

You will then need to restart AppArmor.  If your system uses init scripts, run the following command:

.. code-block:: console

   $ sudo service apparmor restart

If instead, your system uses ``systemd``, run the following command instead:

.. code-block:: console

  $ sudo systemctl restart apparmor

 
---------------------------
Installing Galera Cluster
---------------------------
.. _`galera-install`:

There are three versions of Galera Cluster for MySQL: the original Codership reference implementation; Percona XtraDB Cluster; and MariaDB Galera Cluster.  For each database server, binary packages are available for Debian- and RPM-based Linux distributions, or you can build them from source.

^^^^^^^^^^^^^^^^^^^^^^^^^
Galera Cluster for MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   installmysql
   installmysqlsrc

^^^^^^^^^^^^^^^^^^^^^^^^^^
Percona XtraDB Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
   :maxdepth: 1
	      
   installxtradb
   installxtradbsrc

^^^^^^^^^^^^^^^^^^^^^^^^^^
MariaDB Galera Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   installmariadb
   installmariadbsrc
  

.. note:: **See Also**: In the event that you build or install Galera Cluster over an existing standalone instance of MySQL, MariaDB or Percona XtraDB there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

