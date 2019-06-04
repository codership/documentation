=============================
 Firewall Settings
=============================
.. _`firewall-settings`:
.. index::
   pair: iptables; Firewall settings
.. index::
   single: iptables; Ports
.. index::
   single: Firewall settings; Ports

Galera Cluster requires a number of ports to maintain network connectivity between the nodes.  Depending on your deployment, you may not require all of these ports, but a cluster might require all of them on each node.  Below is a list of these ports and their purpose:

- ``3306`` is the default port for MySQL client connections and :term:`State Snapshot Transfer` using ``mysqldump`` for backups.

- ``4567`` is reserved for Galera Cluster replication traffic. Multicast replication uses both TCP and UDP transport on this port.

- ``4568`` is the port for :term:`Incremental State Transfer`.

- ``4444`` is used for all other :term:`State Snapshot Transfer`.

How these ports are enabled for Galera Cluster can vary depending upon your operating system distribution and what you use to configure the firewall.

.. toctree::
   :maxdepth: 2

   ip-tables
   firewalld
   pf
