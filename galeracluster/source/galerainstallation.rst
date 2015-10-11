The IP addresses in the example are for demonstration purposes only.  Use the real values from your nodes and netmask in the ``iptables`` configuration for your cluster.

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

.. seealso:: For more information on setting up the firewall for Galera Cluster and other programs for configuring packet filtering in Linux and FreeBSD, see :doc:`firewallsettings`.


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

^^^^^^^^^^^^^^^^^^^^^^^^^^
Removing Postfix
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`removing-postfix`:
	  
For RPM-based distributions, such as Red Hat Enterprise Linux and Fedora, if you have an existing MySQL or related database server and Postfix installed on your system, you need to remove Postfix before you can install Galera Cluster.

When you install Galera Cluster over an existing MySQL installation, ``yum`` removes the existing database server package and replaces it with a new one that was built using the wsrep API patch.  However, Postfix registers the database server package as a dependency.  Meaning that, if you try to install the ``mysql-wsrep-server`` package from Codership without removing Postfix, ``yum`` fails since Postfix's dependency on ``MySQL-server`` blocks the installation.

To remove Postfix, run the following command:

.. code-block:: console

   # yum remove postfix

This removes Postfix from your system.  If you still want to use Postfix, you can reinstall it after you finish installing Galera Cluster.  

.. code-block:: console

   # yum install postfix

Postfix now uses Galera Cluster as its database server backend.

.. note:: Remember that this is a problem specific to RPM-based distributions, like Red Hat Enterprise Linux and Fedora.  For Debian- and SUSE-based distributions this is not an issue.  ``apt-get`` and ``zypper`` can update the database server without interfering with Postfix.


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
  

.. seealso:: In the event that you build or install Galera Cluster over an existing standalone instance of MySQL, MariaDB or Percona XtraDB there are some additional steps that you need to take in order to update your system to the new database server.  For more information, see :doc:`migration`.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

