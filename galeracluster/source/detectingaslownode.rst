=========================
 Detecting a Slow Node
=========================
.. _`Detecting a Slow Node`:

By design, the performance of a cluster cannot be higher than the performance of the slowest node in the cluster. Even if you have only one node, its performance can be considerably slower when compared with running the same server in a standalone mode (i.e., without a wsrep Provider).

This is particularly true for large transactions---even if they are within transaction size limits. This is why it's important to be able to detect a slow node on a cluster.

--------------------
Finding Slow Nodes
--------------------
.. _`finding-slow-nodes`:

There are two status variables used in finding slow nodes in a cluster: ``wsrep_flow_control_sent`` and ``wsrep_local_recv_queue_avg``. Check these status variables on each node in a cluster.  The node that returns the highest value is the slowest one.  Lower values are preferable.

:ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>`: This variable provides the number of times a node sent a pause event due to flow control since the last status query.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_sent';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_flow_control_sent | 7     |
   +-------------------------+-------+


:ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`: This varaible returns an average of the received queue length since the last status query.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_avg';

     +----------------------------+---------+
     | Variable_name              | Value   |
     +----------------------------+---------+
     | wsrep_local_recv_queue_avg | 3.34852 |
     +----------------------------+---------+

  Nodes that return values much higher than ``0.0`` inidcates that it cannot apply write-sets as fast as they are received and can generate replication throttling.


Check these status variables on each node in your cluster.  The node that returns the highest value is the slowest node.  Lower values are preferable.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
