====================================
Notification Command
====================================
.. _`notification-cmd`:

Through the **mysql** client, you can check the status of your cluster, the individual nodes and the health of replication.  But, it can prove counterproductive to log into each node and run these checks.  Galera Cluster provides a notification script that allows you to automate monitoring the cluster.

When you set ``wsrep_notify_cmd`` on a node, the server invokes the Notification Command each time cluster membership or the node's local status changes.  You can use this to configure load balancers, raise alarms and so on.


- ``--status [status]`` This argument indicates the status of the node.

  For a list of available options, see :ref:`Node Status String <node-status>`.


- ``--uuid [state UUID]`` This option indicates the cluster state UUID.


- ``--primary [yes|no]`` This option indicates whether or not the current cluster component that the node belongs to is the Primary Component.


- ``--members [list]`` This option provides a list of the member UUID's.

  For more information on the format of the member list, see :ref:`Member List Format <member-list>`.


- ``--index [n]`` This option indicates the index of the node in the member list, (base 0).


--------------------
Node Status Strings
--------------------
.. _`node-status`:

The notification command with the ``--status`` option uses the following strings to indicate node status.

- ``Undefined`` Indicates a starting node that is not part of the Primary Component.

- ``Joiner`` Indicates a node in the Primary Component that is receiving a state snapshot transfer.

- ``Donor`` Indicates a node in the Primary Component that is sending a state snapshot transfer.

- ``Joined`` Indicates a node in the Primary Component with a complete state that is catching up with the cluster.

- ``Synced`` Indicates a node that is synchronized with the cluster.

- ``Error([error code if available])``

.. note:: Only those nodes that in the ``Synced`` state accept connections from the cluster.  For more information on node states, see :ref:`Node State Changes <node-state-changes>`.




---------------------
Member List Element
---------------------
.. _`member-list`:

When the notification command runs on the ``--member`` option, it returns a list for each node that is connected to the cluster component.  The notification command uses the following format for each entry in the list::

	[node UUID] / [node name] / [incoming address]

- ``[node UUID]`` This refers to the unique node ID that it receives automatically from the wsrep Provider.

- ``[node name]`` This refers to the name of the node, as set by the ``wsrep_node_name`` parameter in the configuration file.

- ``[incoming address]`` This refers to the IP address for client connections, as set in the ``wsrep_node_incoming_address`` parameter.



