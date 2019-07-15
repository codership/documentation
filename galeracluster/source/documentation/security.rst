.. meta::
   :title: Security Settings related to Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :ref:`Configure Firewall <firewall-config>`
      - :ref:`Disable SELinux <disable-selinux>`
      - :doc:`firewall-settings`
      - :doc:`selinux`
      - :doc:`ssl`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`security`:

==========
Security
==========

On occasion, you may want or need to enable degrees of security that go beyond the basics of Unix file permissions and secure database management.  For situations such as these,  you can secure both node communications and client connections between the application servers and the cluster.

- :doc:`firewall-settings`

  In order to use Galera Cluster, nodes must have access to a number of ports to maintain network connectivity with the cluster.  While it was touched upon briefly in the :ref:`Installation <firewall-config>` section, this section provides more detailed guides on configuring a system firewall using ``iptables``, FirewallD and PF.

- :doc:`ssl`

  To secure communications between nodes and from the application severs, you can enable encryption through the SSL protocol for client connections, replication traffic and State Snapshot Transfers.  This section provides guidance to configuring SSL on Galera Cluster.

- :doc:`selinux`

  Without proper configuration, SELinux can either block nodes from communicating or it can block the database server from starting at all.  When it does so, it causes the given process to fail silently, without any notification sent to standard output or error as to why.  While you can configure SELinux to permit all activity from the database server, (as was explained in the :ref:`Installation <disable-selinux>` section, this is not a good long-term solution.

  This section provides a guide to creating an SELinux security policy for Galera Cluster.

.. toctree::
   :hidden:

   firewall-settings
   ssl
   selinux
