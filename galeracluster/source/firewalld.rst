======================================
Firewall Configuration with FirewallD
======================================
.. _`firewalld`:

The firewall daemon, or FirewallD, is an interface for dynamically managing firewalls on Linux operating systems, allowing you to set up, maintain and inspect IPv4 and IPv6 firewall rules.

FirewallD includes support for defining zones, allowing you to set the trust level of a given network connection or interface.  For example, when deploying nodes that connect to each other over the internet, rather than a private network, you might configure your firewall around the ``public`` zone.  This assumes that other computers on the network are untrusted and only accepts designated connections.

.. note:: For more information on FirewallD, see the `Documentation <https://fedoraproject.org/wiki/FirewallD>`_.

--------------------------------------
Opening Ports for Galera Cluster
--------------------------------------
.. _`firewalld-ports`:

Galera Cluster requires four ports open for replication over TCP, and, in the event that you want to use multicast replication, one for UDP transport.  In order for this to work over FirewallD, you also need to add the database service to your firewall rules.

#. Enable the database service for FirewallD:

   .. code-block:: console

      # firewall-cmd --zone=public --add-service=mysql

#. Open the TCP ports for Galera Cluster:

   .. code-block:: console

      # firewall-cmd --zone=public --add-port=3306/tcp
      # firewall-cmd --zone=public --add-port=4567/tcp
      # firewall-cmd --zone=public --add-port=4568/tcp
      # firewall-cmd --zone=public --add-port=4444/tcp

#. Optionally, in the event that you would like to use multicast replication, run this command as well to open UDP transport on ``4567``:

   .. code-block:: console

      # firewall-cmd --zone=public --add-port=4567/udp

These commands dynamically configure FirewallD.  Your firewall now permits the rest of the cluster to connect to the node hosted on this server.  Repeat the above commands on each server.  Bear in mind, these changes are not persistent.  When the server reboots, FirewallD returns to its default state.



--------------------------------------
Making Firewall Changes Persistent
--------------------------------------
.. _`firewalld-persistent`:

The commands given in the above section allow you to configure FirewallD on a running server and update the firewall rules without restarting.  However, these changes are not persistent.  When the server restarts, FirewallD reverts to its default configuration.  To update the default configuration yourself, a somewhat different approach is required:


#. Enable the database service for FirewallD:

   .. code-block:: console

      # firewall-cmd --zone=public --add-service=mysql \
            --permanent

#. Open the TCP ports for Galera Cluster:

   .. code-block:: console

      # firewall-cmd --zone=public --add-port=3306/tcp \
            --permanent
      # firewall-cmd --zone=public --add-port=4567/tcp \
            --permanent
      # firewall-cmd --zone=public --add-port=4568/tcp \
            --permanent
      # firewall-cmd --zone=public --add-port=4444/tcp \
            --permanent

#. Optionally, in the event that you would like to use multicast replication, run this command as well to open UDP transport on ``4567``:

   .. code-block:: console

      # firewall-cmd --zone=public --add-port=4567/udp \
            --permanent

#. Reload the firewall rules, maintaining the current state information:

   .. code-block:: console

      # firewall-cmd --reload

These commands modify the default FirewallD settings and then cause the new settings take effect immediately.  FirewallD is now configured to allow the rest of the cluster to access this node.  The configuration remains in effect across reboots.
