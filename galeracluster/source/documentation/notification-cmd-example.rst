.. meta::
   :title: Example of a Galera Notification Script
   :description:
   :language: en-US
   :keywords: galera cluster, notification, notify command, trigger, script
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`example-notification-script`:

===========================
Notification Script Example
===========================

Nodes can call a notification script when changes happen in the membership of the cluster, that is when nodes join or leave the cluster.  You can specify the name of the script the node calls using the :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`.  While you can use whatever script meets the particular needs of a deployment, you may find it helpful to consider the example below as a starting point.

.. code-block:: sh

   #!/bin/sh -eu

   # This is a simple example of wsrep notification script (wsrep_notify_cmd).
   # It will create 'wsrep' schema and two tables in it: 'membership' and 'status'
   # and insert data into them on every membership or node status change.
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


.. _`notification-cmd-path-permissions`:
.. rst-class:: section-heading
.. rubric:: Path and Permissions

After you modify this script to fit your requirements, you need to move it into a directory in the ``$PATH`` or the binaries directory for your system.  On Linux, the binaries directory is typically at ``/usr/bin``, while on FreeBSD it is at ``/usr/local/bin``.

.. code-block:: console

   # mv my-wsrep-notify.sh /usr/bin

In addition to this, given that the notification command contains your root password, change the ownership to the ``mysql`` user and make sure the script is executable only by that user.

.. code-block:: console

   # chown mysql:mysql /usr/bin/my-wsrep-notify.sh
   # chmod 700 /usr/bin/my-wsrep-notify.sh.

This ensures that only the ``mysql`` user can execute and read the notification script, preventing all other users from seeing the root password.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`
   
