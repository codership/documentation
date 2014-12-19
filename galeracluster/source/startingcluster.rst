=====================================
Starting the Cluster
=====================================
.. _`Starting a Cluster`:

When you finish installing and configuring Galera Cluster you have the databases ready for use, but they are not yet connected to each other to form a cluster.  To do this, you will need to start ``mysqld`` on one node, using the ``--wsrep-new-cluster`` option.  This initializes the new Primary Component for the cluster.  Each node you start after this will connect to the component and begin replication.

Before you attempt to initialize the cluster, check that you have the following ready:

- Database hosts with Galera Cluster installed, you will need a minimum of three hosts;

- No firewalls between the hosts;

- SELinux and AppArmor set to permit access to ``mysqld``; and,

- Correct path to ``libgalera_smm.so`` given to the :ref:`wsrep_provider <wsrep_provider>` option.  For example,

  .. code-block:: ini

     wsrep_provider=/usr/lib64/libgalera_smm.so

With the hosts prepared, you are ready to initialize the cluster.



-------------------------------------
Creating Client Connections between the Nodes
-------------------------------------
.. _`Creating Client Connections between Nodes`:

Connecting the database servers to each other as a cluster requires that you create client connections between the nodes.  This allows the nodes to carry out state snapshot transfers with each other.

To connect the clients, on each node run the following queries:

.. code-block:: mysql

	GRANT ALL ON *.* TO 'root'@'node1-address';
	GRANT ALL ON *.* TO 'root'@'node2-address';
	GRANT ALL ON *.* TO 'root'@'node3-address';

This grants the root user of each node root privileges on the other nodes in the cluster.


-------------------------------------
Starting the First Cluster Node
-------------------------------------
.. _`Starting First Cluster Node`:

The process for starting the first node in your cluster is different from all the others.  This is because the first requires that you use the ``--wsrep-new-cluster`` option when you launch ``mysqld``.  This starts the Primary Component for the cluster as a single node.  Each node you start afterwards connects to this component.

.. note:: It does not matter which node you choose to use as your first.

To start the first node, launch the database server on your first node.  For systems that use ``init``, run the following command:

.. code-block:: console

   # service mysql start --wsrep-new-cluster

For systems that use ``systemd``, instead use this command:

.. code-block:: console

   # systemctl mysql start --wsrep-new-cluster

This starts ``mysqld`` on the node.

.. warning:: Don't use the ``--wsrep-new-cluster`` option to start a database when you want to connect or reconnect to an existing cluster. 

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


-------------------------------------
Adding Additional Nodes to the Cluster
-------------------------------------
.. _`Add Nodes to Cluster`:

When you start the first node you initialize a new cluster.  Once this is done, the procedure for adding all the other nodes is the same.

To add a node to an existing cluster, launch ``mysqld`` as you would normally.  If your system uses ``init``, run the following command:

.. code-block:: console

   # service mysql start

For systems that use ``systemd``, instead run this command:

.. code-block:: console

   # systemctl mysql start

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


-------------------------------------
Understanding Cluster Addresses
-------------------------------------
.. _`Understand Cluster Address`:

For each node in the cluster, you must enter an address in the ``wsrep_cluster_address`` parameter of your configuration file.

The syntax for cluster addresses is explained below:

.. code-block:: ini

	<backend schema>://<cluster address>[?option1=value1[&option2=value2]]

- ``<backend schema>``: Indicates the Galera Cluster schema.

  - ``dummy``: This schema is a pass-through backend for testing and profiling purposes.  It does not connect to anywhere.  The node ignores any values given to it.

  - ``gcomm``: This schema is the group communication backend for use in production.  It takes an address and has several settings that you can enable through the option list or through the configuration file, using the ``wsrep_provider_options`` parameter.

- ``<cluster address>``: The address for each node in the cluster.

  - An address of any current member, if you want to connect to an existing cluster, or

  - A comma-separated list of possible cluster members, assuming that the list members can belong to no more than one :term:`Primary Component`.  Or,

  - An empty string, if you want this node to the first in a new cluster, (that is, there are no pre-existing node that you want it to connect to).

- ``options``: The option list sets backend parameters, such as the listen address and timeout values.

  .. note:: The option list is not durable and must be resubmitted on every connection to the cluster.  To make the options durable, set them in the configuration file using the ``wsrep_provider_options`` parameter.

  The parameters set in the URL take precedence over parameters set elsewhere, (for example, the configuration file).  Parameters that you can set through the options list are:

  - ``evs.*``

  - ``pc.*``

  - ``gmcast.*``

  You can follow the option list with a list of ``key=value`` queries according to the URL standard.

  .. note:: If the listen address and port are not set in the parameter list, ``gcomm`` will listen on all interfaces.  The listen port will be taken from the cluster address.  If it is not specified in the cluster address, the default port is ``4567``.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
