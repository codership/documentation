=======================
SELinux Configuration
=======================
.. _`selinux`:

Security-Enhanced Linux, or SELinux, is a kernel module for improving security on Linux operating system.  It integrates support for access control security policies, including mandatory access control (MAC), that limit user applications and system daemons access to files and network resources.  Some Linux distributions, such as Fedora, ship with SELinux enabled by default.

In the context of Galera Cluster, systems with SELinux may block the database server, keeping it from starting or preventing the node from establishing connectivity with the cluster.  To avoid this, you need to configure SELinux policies to allow the node to operate.


-----------------------------
Generating an SELinux Policy
-----------------------------
.. _`gen-selinux-policy`:

In order to create an SELinux policy for Galera Cluster, you need to first open ports and set SELinux into permissive mode.  Then, generate after generating various replication event, state transfers and notifications, create a policy from this activity, then restore SELinux.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disabling SELinux for Galera Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`disable-selinux`:

Building a policy for SELinux requires that you first disable it.  More specifically, set SELinux to open the necessary ports and to permit activities originating from the database server.  While in permissive mode, SELinux continues to create log entries for system events, but takes no action to restrict this activity. 

To disable SELinux, complete the following steps:

#. Using ``semanage``, open the relevant ports:

   .. code-block:: console

      # semanage port -a -t mysqld_port_t -p tcp 4567
      # semanage port -a -t mysqld_port_t -p tcp 4568
      # semanage port -a -t mysqld_port_t -p tcp 4444

   SELinux already opens the standard MySQL port ``3306``.  In the event that you use UDP in your cluster, you also need to open ``4567`` to those connections.

   .. code-block:: console

      # semanage port -a -t mysqld_port_t -p udp 4567

#. Set SELinux to permissive mode for the database server.

   .. code-block:: console

      # semanage permissive -a mysqld_t

SELinux now permits the database server to function on the server and no longer blocks the node from network connectivity with the cluster.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Defining the SELinux Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`define-selinux-policy`:

While SELinux remains in permissive mode, it continues to log activity from the database server.  In order for it to understand normal operation for the database, you need to start the database and generate routine events for SELinux to see.

For servers that use ``init``, start the database with the following command:

.. code-block:: console
		
   # service mysql start

For servers that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl mysql start

You can now begin to create events for SELinux to log.  There are many ways to go about this, including:

- Deleting the write-set cache forces the node to restore itself using a :term:`State Snapshot Transfer`.  The write-set cache is typically in the datadir and is named ``galera.cache`.

- Stop the node, then make changes on another node before starting it again.  Not being that far behind, the node updates itself using an :term:`Incremental State Transfer`.

- Using :ref:`wsrep_desync <wsrep_desync>`, you can change the node state, triggering the notification command defined by :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`. 

- Using :term:`Galera Arbitrator` to run a backup.

When you feel you have generated sufficient events for the log, you can begin work creating the policy and turning SELinux back on.


^^^^^^^^^^^^^^^^^^^^^^^^^^^
Enabling an SELinux Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`enable-selinux`:

Generating an SELinux policy requires that you search log events for the relevant information and pipe it to the ``audit2allow`` utility, creating a ``galera.te`` file to load into SELinux.

To generate and load an SELinux policy for Galera Cluster, complete the following steps:

#. Using ``fgrep`` and ``audit2allow``, create a textease file with the policy information.

   .. code-block:: console

      # fgrep "mysqld" /var/log/audit/audit.log | audit2allow -m MySQL_galera -o galera.te

   This creates a ``galera.te`` file in your working directory.

#. Compile the audit logs into an SELinux policy module.

   .. code-block:: console

      # checkmodule -M -m galera.te -o galera.mod

   This creates a ``galera.mod`` file in your working directory.

#. Package the compiled policy module.

   .. code-block:: console

      # semodule_package -m galera.mod -o galera.pp.

   This creates a ``galera.pp`` file in your working directory.

#. Load the package into SELinux.

   .. code-block:: console

      semodule -i galera.pp

#. Disable permissive mode for the database server.

   .. code-block:: console

      # semanage permissive -d mysql_t


SELinux returns to enforcement mode, now using new policies that work with Galera Cluster.

