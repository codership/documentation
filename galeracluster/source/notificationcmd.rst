====================================
Notification Command
====================================
.. _`notification-cmd`:

While you can use the database client to check the status of your cluster, the individual nodes and the health of replication, you may find it counterproductive to log into the client on each node to run these checks.  Galera Cluster provides a notification script and interface for customization, allowing you to automate the monitoring process for your cluster.



-------------------------------------
Notification Command Parameters
-------------------------------------
.. _`notification-cmd-parameters`:

When the node registers a change in the cluster or itself that triggers the notification command, it passes a number of parameters in calling the script.

- ``--status`` The node passes a string indicating it's current state.  For a list of the strings it uses, see :ref:`Node Status Strings <node-status>` below.
- ``--uuid`` The node passes a string of either `yes` or `no`, indicating whether it considers itself part of the :term:`Primary Component`.
- ``--members`` The node passes a list of the current cluster members.  For more information on the format of these listings, see :ref:`Member List Format <member-list-format>` below.
- ``--index`` The node passes a string that indicates its index value in the membership list.



.. note:: Only those nodes that in the ``Synced`` state accept connections from the cluster.  For more information on node states, see :ref:`Node State Changes <node-state-changes>`.


^^^^^^^^^^^^^^^^^^^^^^^^^
Node Status Strings
^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`node-status`:

The notification command passes one of six values with the ``--status`` parameter to indicate the current status of the node:

- ``Undefined`` Indicates a starting node that is not part of the Primary Component.
- ``Joiner`` Indicates a node that is part of the Primary Component that is receiving a state  snapshot transfer.
- ``Donor`` Indicates a node that is part of the Primary Component that is sending a state snapshot transfer.
- ``Joined`` Indicates a node that is part of the Primary Component  that is in a complete state and is catching up with the cluster.
- ``Synced`` Indicates a node that is syncrhonized with the cluster.
- ``Error`` Indicates that an error has occurred.  This status string may provide an error code with more information on what occurred.

^^^^^^^^^^^^^^^^^^^^^^^^^
Members List Format
^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`member-list-format`:

The notification command passes with the ``--member`` parameter a list containing entries for each node that is connected to the cluster component to which the node belongs.  For each entry in the list the node uses this format:

.. code-block:: text

   <node UUID> / <node name> / <incoming address>
   
- **Node UUID**  Refers to the unique identifier the node receives from the wsrep Provider.
- **Node Name** Refers to the node name, as you define it for the :ref:`wsrep_node_name <wsrep_node_name>` parameter, in the configuration file.
- **Incoming Address** Refers to the IP address for client connections, as set for the :ref:`wsrep_node_incoming_address <wsrep_node_incoming_address>` parameter, in the configuration file.

----------------------------------
Enabling the Notification Command
----------------------------------
.. _`enable-notification-command`:

You can enable the  notification command through the :ref:`wsrep_notify_cmd <wsrep_notify_cmd>` parameter in the configuration file. 

.. code-block:: ini

   wsrep_notify_cmd=/path/to/wsrep_notify.sh

The node then calls the script for each change in cluster membership and node status.  You can use these status changes in configuring load balancers, raising alerts or scripting for any other situation where you need your infrastructure to respond to changes to the cluster.

Galera Cluster provides a default script, ``wsrep_notify.sh``, for you to use in handling notifications or as a starting point in writing your own custom notification script.


