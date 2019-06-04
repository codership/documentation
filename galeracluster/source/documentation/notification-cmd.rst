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

----------------------------------------
Example Notification Script
----------------------------------------
.. _`example-notification-script`:

Nodes can call a notification script when changes happen in the membership of the cluster, that is when nodes join or leave the cluster.  You can specify the name of the script the node calls using the :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`.  While you can use whatever script meets the particular needs of your deployment, you may find it helpful to consider the example below as a starting point.

.. code-block:: sh

   #!/bin/sh -eu

   # This is a simple example of wsrep notification script (wsrep_notify_cmd).
   # It will create 'wsrep' schema and two tables in it: 'membeship' and 'status'
   # and fill them on every membership or node status change.
   #
   # Edit parameters below to specify the address and login to server.

   USER=root
   PSWD=rootpass
   HOST=<host_IP_address>
   PORT=3306

   SCHEMA="wsrep"
   MEMB_TABLE="$SCHEMA.membership"
   STATUS_TABLE="$SCHEMA.status"

   BEGIN="
      SET wsrep_on=0;
      DROP SCHEMA IF EXISTS $SCHEMA; CREATE SCHEMA $SCHEMA;
      CREATE TABLE $MEMB_TABLE (
         idx  INT UNIQUE PRIMARY KEY,
	 uuid CHAR(40) UNIQUE, /* node UUID */
	 name VARCHAR(32),     /* node name */
	 addr VARCHAR(256)     /* node address */
      ) ENGINE=MEMORY;
      CREATE TABLE $STATUS_TABLE (
         size   INT,      /* component size   */
	 idx    INT,      /* this node index  */
	 status CHAR(16), /* this node status */
	 uuid   CHAR(40), /* cluster UUID */
	 prim   BOOLEAN   /* if component is primary */
      ) ENGINE=MEMORY;
      BEGIN;
      DELETE FROM $MEMB_TABLE;
      DELETE FROM $STATUS_TABLE;
   "
   END="COMMIT;"

   configuration_change()
   {
      echo "$BEGIN;"

      local idx=0

      for NODE in $(echo $MEMBERS | sed s/,/\ /g)
      do
         echo "INSERT INTO $MEMB_TABLE VALUES ( $idx, "
	 # Don't forget to properly quote string values
	 echo "'$NODE'" | sed  s/\\//\',\'/g
	 echo ");"
	 idx=$(( $idx + 1 ))
      done

      echo "
         INSERT INTO $STATUS_TABLE
	 VALUES($idx, $INDEX,'$STATUS', '$CLUSTER_UUID', $PRIMARY);
      "

      echo "$END"
   }

   status_update()
   {
      echo "
         SET wsrep_on=0;
	 BEGIN;
	 UPDATE $STATUS_TABLE SET status='$STATUS';
	 COMMIT;
      "
   }

   COM=status_update # not a configuration change by default

   while [ $# -gt 0 ]
   do
      case $1 in
         --status)
	    STATUS=$2
	    shift
	    ;;
	 --uuid)
	    CLUSTER_UUID=$2
	    shift
	    ;;
	 --primary)
	    [ "$2" = "yes" ] && PRIMARY="1" || PRIMARY="0"
	    COM=configuration_change
	    shift
	    ;;
	 --index)
	    INDEX=$2
	    shift
	    ;;
	 --members)
	    MEMBERS=$2
	    shift
	    ;;
	    esac
	    shift
      done

   # Undefined means node is shutting down
   if [ "$STATUS" != "Undefined" ]
   then
      $COM | mysql -B -u$USER -p$PSWD -h$HOST -P$PORT
   fi

   exit 0

When you finish editing the script to fit your needs, you need to move it into a directory in the ``$PATH`` environment variable or the binaries directory for your system.  On Linux, the binaries directory is typically at ``/usr/bin``, while on FreeBSD it is at ``/usr/local/bin``.

.. code-block:: console

   # mv my-wsrep-notify.sh /usr/bin

In addition to this, given that the notification command contains your root password, change the ownership to the ``mysql`` user and make the script executable only to that user.

.. code-block:: console

   # chown mysql:mysql /usr/bin/my-wsrep-notify.sh
   # chmod 700 /usr/bin/my-wsrep-notify.sh.

This ensures that only the ``mysql`` user executes and can read the notification script, preventing all other users from seeing your root password.



----------------------------------
Enabling the Notification Command
----------------------------------
.. _`enable-notification-command`:

You can enable the  notification command through the :ref:`wsrep_notify_cmd <wsrep_notify_cmd>` parameter in the configuration file.

.. code-block:: ini

   wsrep_notify_cmd=/path/to/wsrep_notify.sh

The node then calls the script for each change in cluster membership and node status.  You can use these status changes in configuring load balancers, raising alerts or scripting for any other situation where you need your infrastructure to respond to changes to the cluster.

Galera Cluster provides a default script, ``wsrep_notify.sh``, for you to use in handling notifications or as a starting point in writing your own custom notification script.


