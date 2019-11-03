
.. meta::
   :title: Monitoring a Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../../kb/trouble/index>`
         - :doc:`Best Practices <../../kb/best/index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <./index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :doc:`Install MySQL Galera <../../documentation/install-mysql>`

      .. cssclass:: bull-head

         Related Articles

         - :doc:`Galera Monitoring (video) <../videos/galera-monitoring>`


.. cssclass:: tutorial-article
.. _`galera-monitoring`:

===================================
Monitoring a Galera Cluster
===================================

.. rst-class:: list-stats

   Length: 3100 words; Writer: Russell J.T Dyer: July 17, 2019; Topic: Administration; Level: Intermediate

Galera Cluster is a reliable, stable database replication clustering system. Both MySQL and MariaDB, with the InnoDB storage, utilize Galera for communications between nodes running Linux. Every aspect of such an arrangement is equally dependable for maintenance and availability of data.  It's truly a high-end professional package.

Nevertheless, you should monitor your cluster as an added level of assurance, to maintain a high availability standard -- to resolve problems quickly and without loss of data.  You should occasionally manually, and continuously by automated means, check the status of your cluster. Additionally, you should check and monitor the state of each node to ensure against problems (i.e., replication lag, network connectivity, etc.).

There are three methods available to monitor cluster activity and replication health: you can regularly query MySQL's status variables; use customized scripts, which would basically react to changes in status variables; or use a third-party monitoring application, which would also relies on status variables. In essence, you can either check the status variables yourself, or you can automate and record the process by employing a script or some sort of monitoring software to check the status variables and alert you when there's a problem.

In this article, we'll look closely at the essential status variables for you to consider and ways to log cluster and node status.


.. rst-class:: rubric-1
.. rubric:: Using Status Variables

In addition to the standard status variables in MySQL you may already monitor, Galera Cluster also provides a set of status variables. They will allow you to check node and cluster states, as well as replication health.

Galera Cluster variables are related to write-set replication and thereby prefixed with ``wsrep_``. To retrieve a list of all of these status variables, you would enter the following SQL statement on each node, using a simple database client, such as ``mysql``:

.. code-block:: mysql

   SHOW GLOBAL STATUS LIKE 'wsrep_%';

   +------------------------+--------------------------------------+
   | Variable_name          | Value                                |
   +------------------------+--------------------------------------+
   | wsrep_local_state_uuid | bd5fe1c3-7d80-11e9-8913-4f209d688a15 |
   | wsrep_protocol_version | 10                                   |
   | ...                    | ...                                  |
   | wsrep_thread_count     | 6                                    |
   +------------------------+--------------------------------------+

If you'd execute this SQL statement on one of your nodes, you'd see that there are over sixty status variables. Some of them may be of no interest to you -- perhaps most -- but there are some you should check regularly.  You could group these into three basic categories:  cluster integrity; node status; and replication health.


.. rst-class:: rubric-2
.. rubric:: A Cluster's Integrity

A cluster is said to have integrity when each node -- all of the nodes in the cluster -- receive and replicate write-sets from all of the other nodes. The cluster begins to lose integrity when this situation falters. This can be caused by the cluster going down, becoming partitioned, or if there is a split-brain situation.

The status variables that will reveal whether there is a loss of cluster integrity are the ``wsrep_cluster_state_uuid``, ``wsrep_cluster_conf_id``, ``wsrep_cluster_size``, and the ``wsrep_cluster_status``.  Let's consider each and how it may indicate a problem.


.. rst-class:: rubric-3
.. rubric:: Compare UUIDs

When all nodes are synchronized with each other, they will have executed all of the same transactions.  Each transaction includes a UUID to identify it.  Therefore, the last UUID on each node should be the same.

To confirm this, execute the following SQL statement on each node to see if the results are the same:

.. code-block:: console

   SHOW GLOBAL STATUS LIKE 'wsrep_cluster_state_uuid' \G

   *************************** 1. row ***************************
   Variable_name: wsrep_cluster_state_uuid
           Value: bd5fe1c3-7d80-11e9-8913-4f209d688a15

If the last node has a different result from the others, it may be that a transaction came through while you were in the process of executing the SQL statement. So, check again, maybe in a different order. But if one or more nodes clearly have different UUIDs than the others, the cluster has no integrity. This means more than one cluster has been formed, and the nodes are not all communicating with each other.


.. rst-class:: rubric-3
.. rubric:: Take Attendance

If there may be a problem with network connectivity or if you think the cluster may have split into separate clusters, check the ``wsrep_cluster_size`` on each to see that they agree.  If you have five nodes and some of the nodes say the cluster size contains three, while others say two, you have a problem. Any value that doesn't match the number of nodes you have running suggests there's a network connectivity problem, or maybe MySQL is down on one node.

However, if only one node is out of sync, you might solve the problem by taking it down, fixing whatever network problem it's having, and then starting it again. When it properly joins the cluster, it will undergo a  State Snapshot Transfer (SST), a full replacement of the databases.


.. rst-class:: rubric-3
.. rubric:: Take a Tally

Another approach to checking cluster integrity is to compare the values of the ``wsrep_cluster_conf_id`` status variable on all nodes. This will show the total number of changes that have occurred in the cluster |---| changes that the node on which it's executed is aware. Basically, comparing this variable will determine whether a node is a part of the Primary Component.

.. code-block:: mysql

   SHOW GLOBAL STATUS LIKE 'wsrep_cluster_conf_id';

   +-----------------------+--------+
   | Variable_name         | Value  |
   +-----------------------+--------+
   | wsrep_cluster_conf_id | 82     |
   +-----------------------+--------+

Each node in the cluster should provide the same value. Otherwise, it indicates that the cluster is partitioned. This is not good. If this value is some outrageously high number (e.g., in excess of a trillion), it may indicate that the nodes are dropping and restarting themselves over and over.


.. rst-class:: rubric-2
.. rubric:: Each Node's Status

In addition to checking cluster integrity, you should also monitor the status of individual nodes |---| as in, not necessarily in relation to the cluster as a whole.

Basically, you would look to see whether a node received and processed updates from the cluster write-sets. There are a few status variables that will give such insights:  ``wsrep_ready``; ``wsrep_connected``; and ``wsrep_local_state_comment``.


.. rst-class:: rubric-3
.. rubric:: Ready & Connected

The first two status variables are pretty straightforward: they're either ``ON`` or ``OFF``.  If ``wsrep_ready`` returns ``OFF``, it's not ready and almost all queries will fail.  You'll receive error messages like this one:

.. code-block:: mysql

   ERROR 1047 (08501) Unknown Command

When ``wsrep_connected`` returns a value ``OFF``, the node doesn't have a connection to any other nodes or cluster components. The reason for lost connection could be more physical (i.e., the network is down, a cable is disconnected, etc.).  Or it could be that the node's configuration file is incorrect or inconsistent with the other nodes.

For instance, the values of the ``wsrep_cluster_address`` and ``wsrep_cluster_name`` parameters may be entered incorrectly in the MySQL configuration file. The error log should provide details to help troubleshoot the problem.  This is usually, ``/var/log/mysqld.log`` |---| or whatever the value is for ``log_error`` variable.


.. rst-class:: rubric-3
.. rubric:: Easily Understood

To make the node status much clearer, you can check the value of the ``wsrep_local_state_comment`` status variable. Its value will be easy to understand.

.. code-block:: mysql

   SHOW GLOBAL STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_local_state_comment | Synced |
   +---------------------------+--------+

That's pretty clear |---| Synced |---| and reassuring.

When a node is part of the Primary Component, it will return ``Joining``, ``Waiting on SST``, ``Joined``, ``Synced`` or ``Donor``. If you don't like the results you get, try again. It changes quickly and generally won't take long to get to ``Synced``. If a node is part of a non-operational component, though, it will return ``Initialized``. If it stays that way, it might be a problem.


.. rst-class:: rubric-2
.. rubric:: Replication Health

Monitoring cluster integrity and node status can show issues that may prevent or otherwise block replication. These status variables will help in identifying performance issues and identifying problem areas so that you can get the most from your cluster.

So that things don't get too hectic for a node, Galera will trigger a feedback mechanism called, *Flow Control* to manage the replication process. When there are too many write-sets in the queue, the node engages Flow Control to pause replication until it can get caught up.

The status variables you'd check for this are ``wsrep_local_recv_queue_avg``, ``wsrep_flow_control_paused``, and ``wsrep_cert_deps_distance``. Unlike the previously mentioned status variables, these are variables reset when the servers are restarted or the ``FLUSH STATUS`` statement is executed.


.. rst-class:: rubric-3
.. rubric:: Bunching of Writes

The ``wsrep_local_recv_queue_avg`` variable shows the average size of the local received queue since the last status query. When this is greater than 0, it indicates that the node can't apply write-sets as fast as it's receiving them.  If you're detecting a problem here, you might also check ``wsrep_local_recv_queue_min`` and ``wsrep_local_recv_queue_max`` to get a range of values, rather than just the average.

In addition to checking the node's status related to incoming write-sets, it could check how outgoing connectivity is looking.  Mainly, you would check the ``wsrep_local_send_queue_avg`` variable to get an average of the send queue length since the last time the status variables were flushed.  However, sending is rarely a bottleneck.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_send_queue_avg | 0.145000 |
   +----------------------------+----------+

A value greater than 0 indicates replication throttling or network throughput issues. It could be the physical network cards and cables, or the operating system's configuration. Similar to the received queue above, you can check the ``wsrep_local_send_queue_min`` and ``wsrep_local_send_queue_max`` status parameters to see the range, and not just the average.


.. rst-class:: rubric-3
.. rubric:: Flow Control Paused

If you sense a node is getting overwhelmed, you might execute ``FLUSH STATUS`` on it and then check the value of the ``wsrep_flow_control_paused`` variable |---| after waiting a bit for a better sample.  It will return the percentage of time the node was paused because of Flow Control since you just flushed the status.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_paused';

   +---------------------------+----------+
   | Variable_name             | Value    |
   +---------------------------+----------+
   | wsrep_flow_control_paused | 0.184353 |
   +---------------------------+----------+

In the results here, it shows that for a little more than 18 percent of the time elapsed, the replication was paused.  A value of 1 would indicate that the node was paused 100% of the time. Anything greater than 0 indicates the node's replication health may be weak. You should closely monitor it |---| flushing occasionally |---| until you start seeing 0 values.  If it doesn't resolve itself, you might increase the number of slave threads (i.e., ``wsrep_slave_threads``).


.. rst-class:: rubric-3
.. rubric:: Sequentially in Parallel

Last, you might monitor ``wsrep_cert_deps_distance``. It will tell you the average distance between the lowest and highest sequence number, values a node can potentially apply in parallel.

Basically, this is the optimal value to set ``wsrep_slave_threads``, since it's pointless to assign more slave threads than the number of transactions that can be applied in parallel.


.. rst-class:: rubric-1
.. rubric:: Utilizing Server Logs to Troubleshoot

As you can see, the status variables provide you with plenty of information for detecting problems.  However, they don't generally indicate a pattern |---| they're mostly the current state when you happen to look.  Historical information, though, can make it easier to see a problem developing. Additionally, the status variables do little to help you to determine the cause of problems, or provide you with recommendations on how to solve them.

For seeing a pattern, you'll have to record the results from querying the status variables at regular intervals, recording them in a database or a log for later review. For consistency of intervals, it should be automated. You could either write your own scripts to do this, or you could use one of the many database monitoring programs (e.g., Monyog).


.. rst-class:: rubric-3
.. rubric:: Enabling the Error Log & Special Logging

For determining the cause of a problem, the server logs are generally the most helpful. Use ``SHOW VARIABLES`` to check the value of the ``log_error`` variable |---| and determine the path and name of the log file. If it returns nothing, you'll need to enable it by adding ``log-error`` to the MySQL configuration file. It will set the path and file name on its own.

In addition to the information recorded in the error log, there are parameters and options you can use to enable error logging on events specific to replication: ``wsrep_log_conflicts``, ``cert.log_conflicts``, and ``wsrep_debug``. Setting these will cause MySQL to record information about conflicts in the replication process.

The ``wsrep_log_conflicts`` parameter enables conflict logging for error logs. For instance, it will record when two nodes attempt to write to the same row in the same table at the same time. It will do this even if this conflict is resolved before it can be committed. Without logging this information, you would be unaware that there was temporarily a conflict.

The ``cert.log_conflicts`` is a wsrep Provider option that enables logging of certification failures during replication.

The ``wsrep_debug`` parameter enables debugging information, providing much more verbose entries in the log files. However, this parameter can also cause the database server to record passwords and similar authentication data to the error logs. Don’t enable it in production environments since it’s a security vulnerability.

Below is how these entries would look in the MySQL configuration file:

.. code-block:: ini

   wsrep_log_conflicts=ON
   wsrep_provider_options="cert.log_conflicts=ON"
   wsrep_debug=ON

There is one more type of log you should check. When a node is unable to complete a transaction or some other event, the database server will create a special binary log file with details of that failure. This file is placed in the data directory and is named something like, ``GRA_*.log``. You should periodically see if these log files are generated.  When they are, review them right away.


.. rst-class:: rubric-1
.. rubric:: Notification Command

Although checking status variables and logs will provide you information you'll need, retrieving and reviewing such information is a manual process. Plus, you may have to examine status variables and logs on each determine and resolve a problem. This is one of the appealing aspects of third-party monitoring software.

To assist you in monitoring a cluster and its nodes, Galera includes a mechanism for alerting you of a problem.  To make use of it, you'll need to create a script |---| or copy someone else's script |---| that will process values passed to it from Galera.  Then you have to set the ``wsrep_notify_cmd`` parameter with the path and name of the script |---| put this in the MySQL configuration file.

Galera will call the script and pass a set of values to it whenever a node joins or leaves the cluster, and whenever the cluster or node's status changes.  Your script can then send you an alert, log the data it receives in a table or a log file |---| this is a way to accumulate data for determining a pattern we just mentioned |---| or adjusting traffic flow through a load balancer.


.. rst-class:: rubric-3
.. rubric:: Notification Script Example

When a change occurs in a node or the cluster and triggers the notification script or command, it will pass certain parameters to the script. Of particular interest are the ``--status`` and ``--members`` parameters. The status will be that of the node on which the script is running. It will indicate, among other things, if the node is synchronized or not. See the [Documentation on Notification Status](https://galeracluster.com/library/documentation/notification-cmd.html#node-status) for a list of all values.

Below is a very simple bash script that will serve as a notification command. It collects only some of the information available and records it to a log file, with labels.

.. code-block:: bash

   #!/bin/bash

   log_file='/var/log/galera-node-monitor.log'

   while [ $# -gt 0 ]
      do
      case $1 in
         --status)
            node_status=$2
            shift
            ;;
         --members)
            members=$2
            shift
            ;;
            esac
            shift
      done

   declare idx=0
   declare -a node_names

   for node in $(echo $members | sed s/,/\ /g)
     do
       node_name=$(echo "'$node'" | sed  s/\\//,/g| cut -d',' -f 2)
       node_names+=($node_name)

       idx=$(( $idx + 1 ))
     done

   if [ -z "${idx}" ];
     then
        idx=0
   fi

   node_names=( $(printf "%s\n" ${node_names[@]} | sort ) )
   node_name=(`grep wsrep_node_name /etc/my.cnf`)
   node_name=${node_name:17:7}

   echo "Cluster Size: $idx nodes" >> $log_file
   echo "Cluster Members:" ${node_names[@]} | sort -g >> $log_file
   echo "Node Name: $node_name" >> $log_file
   echo "Node Status: $node_status" >> $log_file
   echo "----------------------" >> $log_file

   exit

To keep this script simple, it parses only two of the parameters that are passed to it. It manipulates that data a little bit, and then writes it to a log file in the data directory. To initiate this script, you'll have to use touch to start that log file and then change the ownership to ``mysql``.

A more useful version of this script would include code which sends you an email message if the node's status is disconnected. Again, we wanted to keep this script simple as an example. The result of it would look like this excerpt below from the log file it appends as events happen:

.. code-block:: text

   ----------------------
   Cluster Size: 3 nodes
   Cluster Members: galera1 galera2 galera3
   Node Name: galera1
   Node Status: synced
   ----------------------

This entry shows three nodes are running and lists their names |---| there are in fact only three nodes in this cluster.  It also shows that the notification script was run on the ``galera1`` node and that node is synchronized.

The next two entries show that ``mysqld`` was shut down on this node.

.. code-block:: text

   ----------------------
   Cluster Size: 1 nodes
   Cluster Members: galera1
   Node Name: galera1
   Node Status: disconnecting
   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: disconnected
   ----------------------

Notice that the number of nodes is now at 1, although the other two nodes are operating fine and maintaining the cluster. This is because it's no longer in communication with the cluster.

The next set of entries below reflect ``mysqld`` starting again. Notice here that after being connected, it becomes a joiner, as well as other steps to become synchronized.

.. code-block:: text

   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: connected
   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: joiner
   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: initializing
   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: initialized
   ----------------------
   Cluster Size: 0 nodes
   Cluster Members:
   Node Name: galera1
   Node Status: joined
   ----------------------
   Cluster Size: 3 nodes
   Cluster Members: galera1 galera2 galera3
   Node Name: galera1
   Node Status: synced
   ----------------------

You would have to copy this script to each node and set it to run with the ``wsrep_notify_cmd`` parameter on each.  The problem with this approach is that the data will be in separate logs.

A better solution would be to have the script connect with the database and insert these log entries into a table.  Remember, entries made on one table are made on all and thereby joined together as part of the replication process. However, Galera seems to trip over itself when the notification command tries to replicate its own writes. It results in the nodes becoming non-operational and out-of-sync. An alternative would be to create a table on each node that doesn't use the InnoDB storage engine (e.g., use a MyISAM table). These tables would be unique to each node and not replicated, but they wouldn't choke Galera.  You could write another script |---| activated instead by ``cron`` |---| that would query the table on each node to produce reports and alerts. You could be alerted by email or some other method. It's a little cumbersome, but it works.


.. rst-class:: rubric-1
.. rubric:: Conclusion

With busy and large databases, keeping them running smoothly and consistently can be a little intimidating.  However, Galera provides plenty of information for you to be able to monitor the status of each node and the cluster. You need only develop a habit of checking, or a system to check automatically and with regularity.  Plus, it provides a method of reacting to changes in node and cluster status.

Yes, you'll need to know how to read the warning signs and know what to do to resolve problems before they affect the entire cluster, but the sooner you are made aware of a situation developing, the better and less stressful it will be for you.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
