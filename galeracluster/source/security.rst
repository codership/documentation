--------
Security
--------
.. _`security`:

On occasion, you may want or need to enable degrees of security that go beyond the basics of Unix file permissions and secure database management.  For situations such as these,  you can secure both node communications and client connections between the application servers and the cluster.

- :doc:`firewallsettings`

  In order to use Galera Cluster, nodes must have access to a number of ports to maintain network connectivity with the cluster.  While it was touched upon briefly in the :ref:`Installation <firewall-config>` chapter, this chapter provides more detailed guides on configuring a system firewall using ``iptables``, FirewallD and PF.
  
- :doc:`ssl`

  To secure communications between nodes and from the application severs, you can enable encryption through the SSL protocol for client connections, replication traffic and State Snapshot Transfers.  This chapter provides guidance to configuring SSL on Galera Cluster.
  
- :doc:`selinux`

  Without proper configuration, SELinux can either block nodes from communicating or it can block the database server from starting at all.  When it does so, it causes the given process to fail silently, without any notification sent to standard output or error as to why.  While you can configure SELinux to permit all activity from the database server, (as was explained in the :ref:`Installation <disable-selinux>` chapter, this is not a good long-term solution.

  This chapter provides a guide to creating an SELinux security policy for Galera Cluster.
  
.. toctree::
   :hidden:

   firewallsettings
   ssl
   selinux

