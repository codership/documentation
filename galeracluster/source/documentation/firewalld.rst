.. meta::
   :title: Configuring FirewallD for Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, firewall, firewalld
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

      Related Articles


.. cssclass:: library-document
.. _`firewalld`:

======================================
Firewall Configuration with FirewallD
======================================

The firewall daemon, or FirewallD, is an interface for dynamically managing firewalls on Linux operating systems. It allows you to set up, maintain and inspect IPv4 and IPv6 firewall rules.

FirewallD includes support for defining zones. This allows you to set the trust level of a given network connection or interface.  For example, when deploying nodes that connect to each other over the internet--rather than a private network--you might configure your firewall around the ``public`` zone.  This assumes that other computers on the network are untrusted and only accept designated connections.

For more information on FirewallD, see the `Documentation <https://fedoraproject.org/wiki/FirewallD>`_.


.. _`firewalld-ports`:
.. rst-class:: section-heading
.. rubric:: Opening Ports for Galera Cluster

Galera Cluster requires four open ports for replication over TCP. To use multicast replication, it also requires one for UDP transport.  In order for this to work over FirewallD, you also need to add the database service to the firewall rules.

To enable the database service for FirewallD, you would enter something like the following at the command-line:

 .. code-block:: console

    # firewall-cmd --zone=public --add-service=mysql

Next, you will need to open the TCP ports for Galera Cluster. Do this by executing the following from the command-line:

 .. code-block:: console

    # firewall-cmd --zone=public --add-port=3306/tcp
    # firewall-cmd --zone=public --add-port=4567/tcp
    # firewall-cmd --zone=public --add-port=4568/tcp
    # firewall-cmd --zone=public --add-port=4444/tcp

Optionally, if you would like to use multicast replication, execute the following from the command-line to open UDP transport on ``4567``:

 .. code-block:: console

    # firewall-cmd --zone=public --add-port=4567/udp

These commands dynamically configure FirewallD. Your firewall will then permit the rest of the cluster to connect to the node hosted on the server.  Repeat the above commands on each server.  Keep in mind, changes to the firewall made by this method are not persistent.  When the server reboots, FirewallD will return to its default state.


.. _`firewalld-persistent`:
.. rst-class:: section-heading
.. rubric:: Making Firewall Changes Persistent

The commands given in the above section allow you to configure FirewallD on a running server and update the firewall rules without restarting.  However, these changes are not persistent.  When the server restarts, FirewallD reverts to its default configuration.  To change the default configuration, a somewhat different approach is required:


First, enable the database service for FirewallD by entering the following from the command-line:

 .. code-block:: console

    # firewall-cmd --zone=public --add-service=mysql \
          --permanent

Now, you'll need to open the TCP ports for Galera Cluster.  To do so, enter the following lines from the command-line:

 .. code-block:: console

    # firewall-cmd --zone=public --add-port=3306/tcp \
          --permanent
    # firewall-cmd --zone=public --add-port=4567/tcp \
          --permanent
    # firewall-cmd --zone=public --add-port=4568/tcp \
          --permanent
    # firewall-cmd --zone=public --add-port=4444/tcp \
          --permanent

If you would like to use multicast replication, execute the following command. It will open UDP transport on ``4567``.

 .. code-block:: console

    # firewall-cmd --zone=public --add-port=4567/udp \
          --permanent

Now you just need to reload the firewall rules, maintaining the current state information. To do this, executing the following:

 .. code-block:: console

    # firewall-cmd --reload

These commands modify the default FirewallD settings and then cause the new settings to take effect, immediately.  FirewallD will then be configured to allow the rest of the cluster to access the node.  The configuration remains in effect after reboots. You'll have to repeat these commands on each server.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
