=====================================
Starting the Cluster
=====================================
.. _`Starting a Cluster`:

When you finish installing and configuring Galera Cluster you have the databases ready for use, but they are not yet connected to each other to form a cluster.  To do this, you will need to start ``mysqld`` on one node, using the ``--wsrep-new-cluster`` option.  This initializes the new :term:`Primary Component` for the cluster.  Each node you start after this will connect to the component and begin replication.

Before you attempt to initialize the cluster, check that you have the following ready:

- Database hosts with Galera Cluster installed, you will need a minimum of three hosts;

- No firewalls between the hosts;

- SELinux and AppArmor set to permit access to ``mysqld``; and,

- Correct path to ``libgalera_smm.so`` given to the :ref:`wsrep_provider <wsrep_provider>` option.  For example,

  .. code-block:: ini

     wsrep_provider=/usr/lib64/libgalera_smm.so

With the hosts prepared, you are ready to initialize the cluster.

.. note:: **See Also**: When migrating from an existing, standalone instance of MySQL or MariaDB Galera Cluster, there are some additional steps that you must take.  For more information on what you need to do, see :doc:`migration`.


-------------------------------------
Starting the First Cluster Node
-------------------------------------
.. _`Starting First Cluster Node`:

By default, nodes do not start as part of the :term:`Primary Component`.  Instead, they assume that the Primary Component exists already somewhere in the cluster.

When nodes start, they attempt to establish network connectivity with the other nodes in the cluster.  For each node they find, they check whether or not it is a part of the Primary Component.  When they find the Primary Component, they request a state transfer to bring the local database into sync with the cluster.  If they cannot find the Primary Component, they remain in a nonoperational state.

There is no Primary Component when the cluster starts.  In order to initialize it, you need to explicitly tell one node to do so with the ``--wsrep-new-cluster`` argument.  By convention, the node you use to initialize the Primary Component is called the first node, given that it is the first that becomes operational.

.. note:: **See Also**: When you start a new cluster, any node can serve as the first node, since all the databases are empty.  When you migrate from MySQL to Galera Cluster, use the original master node as the first node.  When restarting the cluster, use the most advanced node.  For more information, see :doc:`migration` and :doc:`quorumreset`.

Bear in mind, the first node is only "first" in that it initializes the Primary Component. This node can fall behind and leave the cluster without necessarily affecting the Primary Component.

To start the first node, launch the database server on your first node. The command to use depends on your OS and the Galera Cluster version.

For all systems that use SysV ``init`` scripts, run the following command:

.. code-block:: console

   $ service mysql start --wsrep-new-cluster

For systems that use ``systemd`` and Galera Cluster 5.5 or 5.6, use this command:

.. code-block:: console

   $ systemctl start mysql --wsrep-new-cluster

For systems that use ``systemd`` and Galera Cluser 5.7, use the dedicated ``mysqld_bootstrap`` script:

.. code-block:: console

   $ /usr/bin/mysqld_bootstrap

This starts ``mysqld`` on the node.

.. note:: **Warning**: Only use the ``--wsrep-new-cluster`` argument or an equivalent command when initializing the Primary Component.  Do not use it when you want the node to connect to an existing cluster.


Once the node starts the database server, check that startup was successful by checking :ref:`wsrep_cluster_size <wsrep_cluster_size>`.  In the database client, run the following query:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 1     |
   +--------------------+-------+

This status variable tells you the number of nodes that are connected to the cluster.  Since you have just started your first node, the value is ``1``.


.. note:: Do not restart ``mysqld`` at this point.


--------------------------------------
Adding Additional Nodes to the Cluster
--------------------------------------
.. _`Add Nodes to Cluster`:

When you start the first node you initialize a new cluster.  Once this is done, the procedure for adding all the other nodes is the same.

To add a node to an existing cluster, launch ``mysqld`` as you would normally.  If your system uses ``init``, run the following command:

.. code-block:: console

   # service mysql start

For systems that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl start mysql

When the database server initializes as a new node, it connects to the cluster members as defined by the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter.  Using this parameter, it automatically retrieves the cluster map and connects to all other available nodes.

You can test that the node connection was successful using the :ref:`wsrep_cluster_size <wsrep_cluster_size>` status variable.  In the database client, run the following query:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 2     |
   +--------------------+-------+

This indicates that the second node is now connected to the cluster.  Repeat this procedure to add the remaining nodes to your cluster.

When all nodes in the cluster agree on the membership state, they initiate state exchange.  In state exchange, the new node checks the cluster state.  If the node state differs from the cluster state, (which is normally the case), the new node requests a state snapshot transfer from the cluster and it installs it on the local database.  After this is done, the new node is ready for use.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
