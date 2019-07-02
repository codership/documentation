.. cssclass:: library-document
.. _`ip-tables`:

=========================================
Firewall Configuration with ``iptables``
=========================================

Linux provides packet filtering support at the kernel level.  Using ``iptables`` and ``ip6tables`` you can set up, maintain and inspect tables of IPv4 and IPv6 packet filtering rules.

There are several tables that the kernel uses for packet filtering and within these tables are chains that it match specific kinds of traffic.  In order to open the relevant ports for Galera Cluster, you need to append new rules to the ``INPUT`` chain on the filter table.

.. _`iptables-ports`:

----------------------------------
Opening Ports for Galera Cluster
----------------------------------

Galera Cluster requires four ports for replication.  There are two approaches to configuring the firewall to open these ``iptables``.  The method you use depends on whether you deploy the cluster in a :abbr:`LAN (Local Area Network)` environment, such as an office network, or if you deploy the cluster in a :abbr:`WAN (Wide Area Network)` environment, such as on several cloud servers over the internet.

.. _`iptables-lan-config`:

^^^^^^^^^^^^^^^^^^
LAN Configuration
^^^^^^^^^^^^^^^^^^

When configuring packet filtering rules for a :abbr:`LAN (Local Area Network)` environment, such as on an office network, there are four ports that you need to open to :abbr:`TCP (Transmission Control Protocol)` for Galera Cluster and one to :abbr:`UDP (User Datagram Protocol)` transport to enable multicast replication.  This means five commands that you must run on each cluster node:

.. code-block:: console

   # iptables --append INPUT --in-interface eth0 \
      --protocol tcp --match tcp --dport 3306 \
      --source 192.168.0.1/24 --jump ACCEPT
   # iptables --append INPUT --in-interface eth0 \
      --protocol tcp --match tcp --dport 4567 \
      --source 192.168.0.1/24 --jump ACCEPT
   # iptables --append INPUT --in-interface eth0 \
      --protocol tcp --match tcp --dport 4568 \
      --source 192.168.0.1/24 --jump ACCEPT
   # iptables --append INPUT --in-interface eth0 \
      --protocol tcp --match tcp --dport 4444 \
      --source 192.168.0.1/24 --jump ACCEPT
   # iptables --append INPUT --in-interface eth0 \
      --protocol udp --match udp --dport 4567 \
      --source 192.168.0.1/24 --jump ACCEPT

These commands open the relevant ports to :abbr:`TCP (Transmission Control Protocol)` and :abbr:`UDP (User Datagram Protocol)` transport.  It assumes that the IP addresses in your network begin with 192.168.0.

.. warning:: The IP addresses in the example are for demonstration purposes only.  Use the real values from your nodes and netmask in your ``iptables`` configuration.

Galera Cluster can now pass packets through the firewall to the node, but the configuration reverts to default on reboot.  In order to update the default firewall configuration, see :ref:`Making Firewall Changes Persistent <persistent-config>`.

.. _`iptables-wan-config`:

^^^^^^^^^^^^^^^^^^^
WAN Configuration
^^^^^^^^^^^^^^^^^^^

While the configuration shown above for :abbr:`LAN (Local Area Network)` deployments offers the better security, only opening those ports necessary for cluster operation, it does not scale well into :abbr:`WAN (Wide Area Network)` deployments.  The reason is that in a :abbr:`WAN (Wide Area Network)` environment the IP addresses are not in sequence.  The four commands to open the relevant ports to :abbr:`TCP (Transmission Control Protocol)` would grow to four commands per node on each node.  That is, for ten nodes you would need to run four hundred ``iptables`` commands across the cluster in order to set up the firewall on each node.

Without much loss in security, you can instead open a range of ports between trusted hosts.  This reduces the number of commands to one per node on each node.  For example, firewall configuration in a three node cluster would look something like:

.. code-block:: console

    # iptables --append INPUT --protocol tcp \
    	--source 64.57.102.34 --jump ACCEPT
    # iptables --append INPUT --protocol tcp \
    	--source 193.166.3.20  --jump ACCEPT
    # iptables --append INPUT --protocol tcp \
    	--source 193.125.4.10  --jump ACCEPT

When these commands are run on each node, they set the node to accept :abbr:`TCP (Transmission Control Protocol)` connections from the IP addresses of the other cluster nodes.


.. warning:: The IP addresses in the example are for demonstration purposes only.  Use the real values from your nodes and netmask in your ``iptables`` configuration.

Galera Cluster can now pass packets through the firewall to the node, but the configuration reverts to default on reboot.  In order to update the default firewall configuration, see :ref:`Making Firewall Changes Persistent <persistent-config>`.


.. _`persistent-config`:

------------------------------------
Making Firewall Changes Persistent
------------------------------------

Whether you decide to open ports individually for :abbr:`LAN (Local Area Network)` deployment or in a range between trusted hosts for a :abbr:`WAN (Wide Area Network)` deployment, the tables you configure in the above sections are not persistent.  When the server reboots, the firewall reverts to its default state.

For systems that use ``init``, you can save the packet filtering state with one command:

.. code-block:: console

   # service save iptables

For systems that use ``systemd``, you need to save the current packet filtering rules to the path the ``iptables`` unit reads from when it starts.  This path can vary by distribution, but you can normally find it in the ``/etc`` directory.  For example:

- ``/etc/sysconfig/iptables``
- ``/etc/iptables/iptables.rules``

Once you find where your system stores the rules file, use ``iptables-save`` to update the file:

.. code-block:: console

   # iptables-save > /etc/sysconfig/iptables

When your system reboots, it now reads this file as the default packet filtering rules.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
