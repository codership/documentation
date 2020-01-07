.. meta::
   :title: Setting an SELinux Policy
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`SELinux with Galera <../../documentation/selinux>`
      - :doc:`Firewall Settings <../../documentation/firewall-settings>`
      - :doc:`Firewall Settings <../../documentation/firewalld>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-setting-selinux`:

===================================
Setting an SELinux Policy
===================================

.. index::
   pair: Configuration; SELinux

.. rst-class:: article-stats

   Length: 345 words; Published: June 24, 2015; Updated: October 20, 2019; Category: Security; Type: Best Practices

Security-Enhanced Linux (SELinux) is a security module of the Linux kernel for all distributions.  It supports access control security policies.  When you first install Galera Cluster, unless you disable or configure SELinux properly, it will prevent communications between Galera nodes. In order to enable replication on the node, unless you disable SELinux, you will need a policy for Galera so that SELinux wil recognize cluster activities as legitimate.

.. rst-class:: section-heading
.. rubric:: Recommendations

To create a policy for Galera Cluster, you can first set SELinux to run in permissive mode.  Permissive mode does not block cluster activity, but it does log the actions as warnings.  You can make this change generally by editing the SELinux configuration file (e.g., ``/etc/selinux/config``) to include an uncommented line like so:

.. code-block:: console

   SELINUX=permissive

As mentioned above, it will collect warnings about cluster activities. With this, you can iteratively create a policy for Galera Cluster.  Once SELinux no longer registers warnings from Galera Cluster, you can switch it back into enforcing mode.  SELinux will then use the new policy to allow the cluster access to the various ports and files it needs.

A more straightforward method would be to open the ports that Galera needs. TCP port 3306 is used by MySQL and MariaDB by default. TCP and UDP port 4567 is used for general Galera Cluster communications. TCP port 4444 is used for Incremental State Transfers, while TCP port 4568 is used for State Snapshot Transfers. You'll have to enable all of these ports in SELinux |---| and in your firewall if you're using one. You can manage ports with the ``semanage`` tool by entering something like the following from the command-line:

.. code-block:: console

   semanage port -a -t mysqld_port_t -p tcp 3306

   semanage port -a -t mysqld_port_t -p tcp 4444
   semanage port -a -t mysqld_port_t -p tcp 4567
   semanage port -a -t mysqld_port_t -p udp 4567
   semanage port -a -t mysqld_port_t -p tcp 4568

   semanage permissive -a mysqld_t

Almost all Linux distributions ship with a MySQL or MariaDB policy for SELinux. The last line here enables that policy.

.. container:: bottom-links

   Related Documents

   - :doc:`SELinux with Galera <../../documentation/selinux>`
   - :doc:`Firewall Settings <../../documentation/firewall-settings>`
   - :doc:`Firewall Settings <../../documentation/firewalld>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
