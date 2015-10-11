===========================
Managing Flow Control
===========================
.. _`managing-fc`:

The cluster replicates changes synchronously through global ordering, but applies these changes asynchronously from the originating node out.  To prevent any one node from falling too far behind the cluster, Galera Cluster implements a feedback mechanism called Flow Control.

Nodes queue the write-sets they receive in the global order and begin to apply and commit them on the database.  In the event that the received queue grows too large, the node initiates Flow Control.  The node pauses replication while it works the received queue.  Once it reduces the received queue to a more manageable size, the node resumes replication.


---------------------------
Monitoring Flow Control
---------------------------
.. _`monitoring-fc`:

Galera Cluster provides global status variables for use in monitoring Flow Control.  These break down into those status variables that count Flow Control pause events and those that measure the effects of pauses.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_%';

Running these status variables returns only the node's present condition.  You are likely to find the information more useful by graphing the results, so that you can better see the points where Flow Control engages.

For instance, using `myq_gadgets <https://github.com/jayjanssen/myq_gadgets/>`_:

.. code-block:: console

   $ mysql -u monitor -p -e 'FLUSH TABLES WITH READ LOCK;' \
      example_database
   $ myq_status wsrep

   Wsrep    Cluster        Node           Queue  Ops      Bytes   Flow         Conflct
   time     name     P cnf  # name  cmt  sta  Up  Dn  Up  Dn   Up   Dn pau snt dst lcf bfa
   09:22:17 cluster1 P   3  3 node3 Sync T/T   0   0   0   9    0  13K 0.0   0 101   0   0
   09:22:18 cluster1 P   3  3 node3 Sync T/T   0   0   0  18    0  28K 0.0   0 108   0   0
   09:22:19 cluster1 P   3  3 node3 Sync T/T   0   4   0   3    0 4.3K 0.0   0 109   0   0
   09:22:20 cluster1 P   3  3 node3 Sync T/T   0  18   0   0    0    0 0.0   0 109   0   0
   09:22:21 cluster1 P   3  3 node3 Sync T/T   0  27   0   0    0    0 0.0   0 109   0   0
   09:22:22 cluster1 P   3  3 node3 Sync T/T   0  29   0   0    0    0 0.9   1 109   0   0
   09:22:23 cluster1 P   3  3 node3 Sync T/T   0  29   0   0    0    0 1.0   0 109   0   0

You can find the slave queue under the ``Queue Dn`` column and ``FC pau`` refers to Flow Control pauses.  When the slave queue rises to a certain point, Flow Control changes the pause value to ``1.0``.  The node will hold to this value until the slave queue is worked down to a more manageable size.

.. note:: **See Also**: For more information on status variables that relate to flow control, see :doc:`galerastatusvariables`.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Monitoring for Flow Control Pauses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`monitor-pauses`:

When Flow Control engages, it notifies the cluster that it is pausing replication using an ``FC_Pause`` event.  Galera Cluster provides two status variables that monitor for these events.

- :ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>` This status variable shows the number of Flow Control pause events sent by the local node since the last status query.

- :ref:`wsrep_flow_control_recv <wsrep_flow_control_recv>` This status variable shows the number of Flow Control pause events on the cluster, both those from other nodes and those sent by the local node, since the last status query.



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Measuring the Flow Control Pauses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`measure-fc-pauses`:

In addition to tracking Flow Control pauses, Galera Cluster also allows you to track the amount of time since the last ``SHOW STATUS`` query during which replication was paused due to Flow Control.  

You can find this using one of two status variables:

- :ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>` Provides the amount of time replication was paused as a fraction.  Effectively, how much the slave lag is slowing the cluster.  The value ``1.0`` indicates replication is paused now.  

- :ref:`wsrep_flow_control_paused_ns <wsrep_flow_control_paused_ns>` Provides the amount of time replication was paused in nanoseconds.



--------------------------
Configuring Flow Control
--------------------------
.. _`configuring-fc`:

Galera Cluster provides two sets of parameters that allow you to manage how nodes handle the replication rate and Flow Control.  The first set controls the write-set cache, the second relates to the points at which the node engages and disengages Flow Control.  



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Managing the Replication Rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`managing-gcache-fc`:

These three parameters control how nodes respond to changes in the replication rate.  They allow you to manage the write-set cache on an individual node.

- :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` This sets the maximum write-set cache size (in bytes).  The parameter value depends on the amount of RAM, swap size and performance considerations.

  The default value is ``SSIZE_MAX`` minus 2 gigabytes on 32-bit systems.  There is no practical limit on 64-bit systems.

  In the event that a node exceeds this limit and :ref:`gcs.max_throttle <gcs.max_throttle>` is not set at ``0.0``, the node aborts with an out-of-memory error.  If :ref:`gcs.max_throttle <gcs.max_throttle>` is set at ``0.0.``, replication in the cluster stops.

- :ref:`gcs.max_throttle <gcs.max_throttle>` This sets the smallest fraction to the normal replication rate the node can tolerate in the cluster.  If you set the parameter to ``1.0`` the node does not throttle the replication rate.  If you set the parameter for ``0.0``, a complete replication stop is possible.

  The default value is ``0.25``.

- :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` This serves to estimate the average replication rate for the node.  It is a fraction of the :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>`.  When the replication rate exceeds the soft limit, the node calculates the average replication rate (in bytes) during this period.  After that, the node decreases the replication rate linearly with the cache size so that at the :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` it reaches the value of the :ref:`gcs.max_throttle <gcs.max_throttle>` times the average replication rate.

  The default value is ``0.25``.

  .. note:: When the node estimates the average replication rate, it can reach a value that is way off from the sustained replication rate.

The write-set cache grows semi-logarithmically with time after the :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` and the time needed for a state transfer to complete.



^^^^^^^^^^^^^^^^^^^^^^
Managing Flow Control
^^^^^^^^^^^^^^^^^^^^^^
.. _`managing-flow-control`:

These parameters control the point at which the node triggers Flow Control and the factor used in determining when it should disengage Flow Control and resume replication.


- :ref:`gcs.fc_limit <gcs.fc_limit>` This parameter determines the point at which Flow Control engages.  When the slave queue exceeds this limit, the node pauses replication.

  It is essential for multi-master configurations that you keep this limit low.  The certification conflict rate is proportional to the slave queue length.  In master-save setups, you can use a considerably higher value to reduce Flow Control intervention.

  The default value is ``16``.

- :ref:`gcs.fc_factor <gcs.fc_factor>` This parameter is used in determining when the node can disengage Flow Control.  When the slave queue on the node drops below the value of :ref:`gcs.fc_limit <gcs.fc_limit>` times that of :ref:`gcs.fc_factor <gcs.fc_factor>` replication resumes.

  The default value is ``0.5``.

Bear in mind that, while it is critical for multi-master operations that you use as small a slave queue as possible, the slave queue length is not so critical in master-slave setups.  Depending on your application and hardware, the node can apply even 1K of write-sets in a fraction of a second.  The slave queue length has no effect on master-slave failover.

.. note:: **Warning**: Cluster nodes process transactions asynchronously with regards to each other.  Nodes cannot anticipate in any way the amount of replication data.  Because of this, Flow Control is always reactive.  That is, it only comes into affect after the node exceeds certain limits.  It cannot prevent exceeding these limits or, when they are exceeded, it cannot make any guarantee as to the degree they are exceeded.

  Meaning, if you were to configure a node with:

  .. code-block:: ini

    gcs.recv_q_hard_limit=100Mb

  That node can still exceed that limit from a 1Gb write-set.
