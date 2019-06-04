=====================================
Starting the Cluster
=====================================
.. _`starting-cluster`:

After you finish installing MySQL (or MariaDB or Percona XtraDB to Galera Cluster) and Galera and have added the necessary settings for the configuration file needed for Galera Cluster, the next steps are to start the nodes that will form the cluster.  To do this, you will need to start the ``mysqld`` daemon on one node, using the ``--wsrep-new-cluster`` option.  This initializes the new :term:`Primary Component` for the cluster.  Each node you start after that will connect to the component and begin replication.

Before you attempt to initialize the cluster, there are a few things you should verify are in place on each node and related services:

- At least three servers with the same version of MySQL, MariaDB, or Percona XtraDB installed on each;

- If you're using firewalls, make sure the ports 4444, 4567, and 4568 for TCP traffic, and 4567 for UPD traffic are open between the hosts;

- SELinux and AppArmor, whichever your system uses or both, has to be set to allow access to ``mysqld``; and,

- Set the parameter for :ref:`wsrep_provider <wsrep_provider>` to the location of ``libgalera_smm.so``. That line in the configuration file might look like this:

  .. code-block:: ini

     wsrep_provider=/usr/lib64/libgalera_smm.so

Once you have at least three hosts ready, you can initialize the cluster.

.. note:: When migrating from an existing, stand-alone instance of MySQL, MariaDB or Percona XtraDB to Galera Cluster, there will be some additional steps that you must take.  For more information on what you need to do, see :doc:`Migration <../../../documentation/migration>`.


-------------------------------------
Starting the First Node
-------------------------------------
.. _`Starting First Cluster Node`:

By default, a node don't start as part of the :term:`Primary Component`.  Instead, it assumes that the Primary Component is already running and it is merely joining an existing cluster.  For each node it encounters in the cluster, it checks whether or not it's a part of the Primary Component.  When it finds the Primary Component, it requests a state transfer to bring its database into sync with the cluster.  If it can't find the Primary Component, it will remains in a non-operational state.

The problem is that there is no Primary Component when a cluster starts, when the first node is initiated.  Therefore, you need explicitly to tell that first node to do so with the ``--wsrep-new-cluster`` argument.  Althought this initiate node is said to be the first node, it can fall behind and leave the cluster without necessarily affecting the Primary Component.

.. note:: When you start a new cluster, any node can serve as the first node, since all the databases are empty.  When you migrate from MySQL to Galera Cluster, use the original master node as the first node.  When restarting the cluster, use the most advanced node.  For more information, see :doc:`Migration <../../../documentation/migration>` and :doc:`Quorum Reset <../../../documentation/quorum-reset>`.

To start the first node--which should have MySQL, MariaDB or Percona XtraDB, and Galera installed--you'll have to launch the database server on it with the ``--wsrep-new-cluster`` option.  There are a few ways you might do this, depending on the operating system. For systems that use ``init``, execute the following from the command-line:

.. code-block:: console

   $ systemctl start mysql --wsrep-new-cluster

For operating systems that use ``systemd``, you would instead enter the following from the command-line:

.. code-block:: console

   $ /usr/bin/mysqld_bootstrap

Both of these start the ``mysqld`` daemon on the node. Starting in MariaDB version 10.4, which includes Galera version 4, you can enter instead the following from the command-line to start MariaDB, Galera, and to establish the Primary Component:

.. code-block:: console

   # galera_new_cluster

.. warning:: Use the ``--wsrep-new-cluster`` argument only when initializing the Primary Component.  Don't use it to connect a new node to an existing cluster.

Once the first node starts the database server, verify that the cluster has started, albeit a one-node cluster, by checking :ref:`wsrep_cluster_size <wsrep_cluster_size>`.  With the database client, execute the following SQL statement:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 1     |
   +--------------------+-------+

This status variable indicates the number of nodes that are connected to the cluster.  Since only the first node has been started, the value is ``1`` here.  After you start other nodes that will be part of this same cluster, execute this SQL statement again--on thee first node or any node you've verified are in the cluster.  The value should reflect the number of nodes in the cluster.

Once you get the first node started and the Primary Component initialized, don't restart ``mysqld``. Instead, wait until you've added more nodes to the cluster so that it can stay viable without the first node. If you must restart the first node before adding other nodes, shutdown ``mysqld`` and then bootstrap start it again (e.g., execute ``galera_new_cluster``). If it won't start as easily as it did the first time, you may have to edit the file containing the Galera Saved State (i.e., /var/lib/mysql/grastate.dat).  The contents of that file will look something like this:

.. code-block:: mysql

   # GALERA saved state
   version: 2.1
   uuid:    bd5fe1c3-7d80-11e9-8913-4f209d688a15
   seqno:   -1
   safe_to_bootstrap: 0

The variable ``safe_to_bootstrap`` is set to 0 on the first node after it's been bootstrapped to protect against you inadvertently bootstrapping again while the cluster is runnning.  You'll have to change the value to 1 to be able to bootstrap anew.


--------------------------------------
Adding Nodes to the Cluster
--------------------------------------
.. _`Add Nodes to Cluster`:

Once you have successfully started the first node and thereby initialized a new cluster, the procedure for adding all the other nodes is even simpler. You just launch ``mysqld`` as you would normally--without the ``--wsrep-new-cluster`` option.  You would enter something like the following from the command-line, depending on your operating system and database system (see above for other methods):

.. code-block:: console

   # systemctl start mariadb

When the database server initializes as a new node, it will try to connect to the cluster members. It knows where to find these other nodes based on the IP addresses listed in the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter in the configuration file.

You can verify that the node connection was successful checking the :ref:`wsrep_cluster_size <wsrep_cluster_size>` status variable.  In the database client of any node in the cluster, run the following SQL statement:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 2     |
   +--------------------+-------+

This indicates that the two nodes are now connected to the cluster.  When the nodes in the cluster agree on the membership state, they initiate state exchange.  In state exchange, a new node will check the cluster state.  If the state of a new node differs from the cluster state--which is normally the case--the new node requests a state snapshot transfer (SST) from the cluster and it installs it on its local database.  After this is done, the new node is ready for use.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
