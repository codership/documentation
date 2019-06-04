====================================
Firewall Configuration with PF
====================================
.. _`firewall-pf`:

FreeBSD provides packet filtering support at the kernel level.  Using PF you can set up, maintain and inspect the packet filtering rule sets.

.. warning:: Different versions of FreeBSD use different versions of PF.  Examples here are from FreeBSD 10.1, which uses the same version of PF as OpenBSD 4.5.


-------------------
Enabling PF
-------------------
.. _`using-pf`:

In order to use PF on FreeBSD, you must first set the system up to load its kernel module.  Additionally, you need to set the path to the configuration file for PF.

Using your preferred text editor, add the following lines to ``/etc/rc.conf``:

.. code-block:: ini

   pf_enable="YES"
   pf_rules="/etc/pf.conf"

You may also want to enable logging support for PF and set the path for the log file.  This can be done by adding the following lines to ``/etc/rc.conf``:

.. code-block:: ini

   pflog_enable="YES"
   pflog_logfile="/var/log/pflog"

FreeBSD now loads the PF kernel module with logging features at boot.

---------------------
Configuring PF Rules
---------------------
.. _`pf-config`:

In the above section, the configuration file for PF was set to ``/etc/pf.conf``.  This file allows you to set up the default firewall configuration that you want to use on your server.  The settings you add to this file are the same for each cluster node.

There are two variables that you need to define for Galera Cluster in the PF configuration file:  a list for the ports it needs open for :abbr:`TCP (Transmission Control Protocol)` and a table for the IP addresses of nodes in the cluster.

.. code-block:: ini

   # Galera Cluster Macros
   wsrep_ports="{ 3306, 4567, 4568,4444}"
   table <wsrep_cluster_address> persist {192.168.1.1 192.168.1.2 192.168.1.3}"

Once you have these defined, you can add the rule to allow cluster packets to pass through the firewall.

.. code-block:: ini

   # Galera Cluster TCP Filter Rule
   pass in proto tcp from <wsrep_cluster_address> to any port $wsrep_ports keep state

In the event that you deployed your cluster in a :abbr:`LAN (Local Area Network)` environment, you need to also create on additional rule to open port ``4568`` to :abbr:`UDP (User Datagram Protocol)` transport for mutlicast replication.

.. code-block:: ini

   # Galera Cluster UDP Filter Rule
   pass in proto udp from <wsrep_cluster_address> to any port 4568 keep state

This defines the packet filtering rules that Galera Cluster requires.  You can test the new rules for syntax errors using ``pfctl``, with the ``-n`` options to prevent it from trying to load the changes.

.. code-block:: console

   # pfctl -v -nf /etc/pf.conf

   wsrep_ports = "{ 3306, 4567, 4568, 4444 }"
   table <wsrep_cluster_address> persist { 192.168.1.1 192.168.1.2 192.168.1.3 }
   pass in proto tcp from <wsrep_cluster_address> to any port = mysql flags S/A/ keep state
   pass in proto tcp from <wsrep_cluster_address> to any port = 4567 flags S/SA keep state
   pass in proto tcp from <wsrep_cluster_address> to any port = 4568 flags S/SA keep state
   pass in proto tcp from <wsrep_cluster_address> to any port = krb524 falgs S/SA keep state
   pass in proto udp from <wsrep_cluster_address> to any port = 4568 keep state

If there are no syntax errors, ``pfctl`` prints each of the rules it adds to the firewall, (expanded, as in the example above).  If there are syntax errors, it notes the line near where the errors occur.

.. warning:: The IP addresses in the example are for demonstration purposes only.  Use the real values from your nodes and netmask in your PF configuration.


-------------------
Starting PF
-------------------
.. _`pf-start`:

When you finish configuring packet filtering for Galera Cluster and for any other service you may require on your FreeBSD server, you can start the service.  This is done with two commands: one to start the service itself and one to start the logging service.

.. code-block:: console

   # service pf start
   # service pflog start

In the event that you have PF running already and want to update the rule set to use the settings in the configuration file for PF, (for example, the rules you added for Galera Cluster), you can load the new rules through the ``pfctl`` command.

.. code-block:: console

   # pfctl -f /etc/pf.conf
