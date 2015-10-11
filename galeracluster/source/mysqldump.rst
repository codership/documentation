=============================
Enabling ``mysqldump``
=============================
.. _`enabling-mysqldump`:

The :term:`Logical State Transfer Method` ``mysqldump`` works by interfacing through the database server rather than the physical data.  As such, they require some additional configurations beyond setting the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter.


--------------------------------------
Configuring SST Privileges
--------------------------------------
.. _`sst-privileges`:

In order for ``mysqldump`` to interface with the database server, it requires root connections for both the donor and joiner nodes.  You can enable this through the :ref:`wsrep_sst_auth <wsrep_sst_auth>` parameter.

Using your preferred text editor, open ``wsrep.cnf`` file.  You can find it in ``/etc/mysql/conf.d/``), and enter the relevant authentication information.

.. code-block:: ini

   # wsrep SST Authentication
   wsrep_sst_auth = wsrep_sst_username:password

This provides authentication information that the node requires to establish connections. Use the same values for every node in your cluster.

.. note:: **Warning**: Use your own authentication parameters in place of ``wsrep_sst_user`` and ``password``.

--------------------------
Granting SST Privileges
--------------------------
.. _`sst_authorization`:

When the database server start, it reads from the above file the authentication information it needs to access another database server.  In order for the node to accept connections from the cluster, you must also create and configure the State Snapshot Transfer user through the database client.

In order to do this, you need to start the database server.  If you have not used this node on the cluster before, start it with replication disabled.  For servers that use ``init``, run the following command:

.. code-block:: console

   # service mysql start --wsrep-on=off

For servers that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl start mysql --wsrep-on=OFF

When the database server is running, log into the database client and run the ``GRANT ALL`` command for the IP address of each node in your cluster.

.. code-block:: mysql

   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node1_IP_address'
	IDENTIFIED BY 'password';
   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node2_IP_address'
	IDENTIFIED BY 'password';
   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node3_IP_address'
 	IDENTIFIED BY 'password';

These commands grant each node in your cluster access to the database server on this node.  You need to run these commands on every other cluster node to allow ``mysqldump`` in state transfers between them.

In the event that you have not yet created your cluster, you can stop the database server while you configure the other nodes.  For servers that use ``init``, run the following command:

.. code-block:: console

   # service mysql stop

For servers that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl stop mysql


