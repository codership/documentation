==============
Installation
==============
.. _`galera-install-configure`:

Galera Cluster requires server hardware for a minimum of three nodes.

If your cluster runs on a single switch, use three nodes.  If your cluster spans switches, use three switches.  If your cluster spans networks, use three networks.  If your cluster spans data centers, use three data centers.  This ensures that the cluster can maintain a Primary Component in the event of network outages.

Each node in the cluster requires:

- 100 Mbps or better network connectivity;
- Linux or FreeBSD;
- Database server for MySQL, MariaDB or Percona XtraDB;
- wsrep API patch for the database server;
- Galera Replication Plugin.

There are binary installation packages available that bundle the wsrep API with the database server.  Once you have these prerequisites ready, you can begin installing Galera Cluster.

------------------------------
Preparing the Server
------------------------------
.. _`system-requirements`:

Before you begin the installation process, there are a few tasks that you need to undertake to prepare the servers for Galera Cluster.  You must perform the following steps for each node in your cluster.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disabling SELinux for mysqld
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`disable-selinux`:



If you have SELinux enabled, it may block ``mysqld`` from carrying out required operations.  You must either disable SELinux for mysqld or configure it to allow ``mysqld`` to run external programs and open listen sockets on unprivileged ports |---| that is, things that an unprivileged user can do.

To disable SELinux for mysql run the following command:

.. code-block:: console

   # setmanage permissive -a mysqld_t

.. seealso:: For more information on writing SELinux policies, see `SELinux and MySQL <https://blogs.oracle.com/jsmyth/selinux_and_mysql>`.  For additional information, see the SELinux.

.. Revision Note: Add a label for port 4567 as mysqld_port_t, check if other ports on the firewall need something similar.  Check if AppArmor requires a similar label as well.

	     
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Firewall Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`firewall-config`:

Next, you will need to change the firewall settings, so that the nodes cna communicate with each other and to ensure that you can interact with them.  For instance, if you use ``iptables`` on CentOS, complete the following steps:

.. code-block:: console

   # iptables --insert RH-Firewall-1-INPUT 1 --proto tcp \
      --source my_IP/24 --destination my_IP/32 \
      --dport 3306 -j ACCEPT
   # iptables --insert RH-Firewall-1-INPUT 1 --proto tcp \
      --source my_IP/24 --destination my_IP/32 \
      --dport 4567 -j ACCEPT
   # iptables --insert RH-Firewall-1-INPUT 1 --proto tcp \
      --source my_IP/24 --destination my_IP/32 \
      --dport 4568 -j ACCEPT

Once this is done, you need to save ``iptables``.  If your system uses init scripts, run the following command:

.. code-block:: console

   # service iptables save

If instead, your system uses ``systemd``, run this command instead:

.. code-block:: console

   # systemctl save iptables

You will need to set the above firewall configurations for each node in your cluster.

.. note:: If there is a NAT firewall between the nodes, you must configure it to allow for direct connections between the nodes, such as through port forwarding.
      
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
  



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

