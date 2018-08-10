=========================
 Detecting a Slow Node
=========================
.. _`Detecting a Slow Node`:

By design, the performance of the cluster cannot be higher than the performance of the slowest node on the cluster. Even if you have one node only, its performance can be considerably lower when compared with running the same server in a standalone mode (without a wsrep Provider).

This is particularly true for big transactions even if they were within the transaction size limits. This is why it is important to be able to detect a slow node on the cluster.

--------------------
Finding Slow Nodes
--------------------
.. _`finding-slow-nodes`:

There are two status variables used in finding slow nodes:

- :ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>` Provides the number of times the node sent a pause event due to flow control since the last status query.

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_flow_control_sent';

     +-------------------------+-------+
     | Variable_name           | Value |
     +-------------------------+-------+
     | wsrep_flow_control_sent | 7     |
     +-------------------------+-------+


- :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>` Provides an average of the received queue length since the last status query.

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_local_recv_queue_avg';

     +----------------------------+---------+
     | Variable_name              | Value   |
     +----------------------------+---------+
     | wsrep_local_recv_queue_avg | 3.34852 |
     +----------------------------+---------+

  Nodes that return values much higher than ``0.0`` inidcates that it cannot apply write-sets as fast as they are received and can generate replication throttling.


Check these status variables on each node in your cluster.  The node that returns the highest value is the slowest node.  Lower values are preferable.


