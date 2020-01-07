.. meta::
   :title: Use Status Variables to Monitor Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


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

      - :doc:`notification-cmd`
      - :doc:`Reset Quorum <quorum-reset>`
      - :ref:`checking node status <check-node-status>`
      - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`
      - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
      - :ref:`wsrep_cluster_conf_id <wsrep_cluster_conf_id>`
      - :ref:`wsrep_cluster_name <wsrep_cluster_name>`
      - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
      - :ref:`wsrep_cluster_state_uuid <wsrep_cluster_state_uuid>`
      - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
      - :ref:`wsrep_connected <wsrep_connected>`
      - :ref:`wsrep_local_send_queue_avg <wsrep_local_send_queue_avg>`
      - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`
      - :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`
      - :ref:`wsrep_local_recv_queue_max <wsrep_local_recv_queue_max>`
      - :ref:`wsrep_local_recv_queue_min <wsrep_local_recv_queue_min>`
      - :ref:`wsrep_ready <wsrep_ready>`
      - :ref:`wsrep_slave_threads <wsrep_slave_threads>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`monitoring-cluster`:

========================
Using Status Variables
========================

.. index::
   pair: Parameters; wsrep_notify_cmd

From the database client, you can check the status of write-set replication throughout the cluster using standard queries.  Status variables that relate to write-set replication have the prefix ``wsrep_``, meaning that you can display them all using the following query:

.. code-block:: mysql

   SHOW GLOBAL STATUS LIKE 'wsrep_%';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_protocol_version | 5     |
   | wsrep_last_committed   | 202   |
   | ...                    | ...   |
   | wsrep_thread_count     | 2     |
   +------------------------+-------+

.. note:: In addition to checking status variables through the database client, you can also monitor for changes in cluster membership and node status through ``wsrep_notify_cmd.sh``.  For more information on its use, see :doc:`notification-cmd`.


.. _`check-cluster-integrity`:
.. rst-class:: section-heading
.. rubric:: Checking Cluster Integrity

.. index::
   pair: Parameters; wsrep_cluster_state_uuid
.. index::
   pair: Parameters; wsrep_cluster_conf_id
.. index::
   pair: Parameters; wsrep_cluster_size
.. index::
   pair: Parameters; wsrep_cluster_status

The cluster has integrity when all nodes in it receive and replicate write-sets from all other nodes.  The cluster begins to lose integrity when this breaks down, such as when the cluster goes down, becomes partitioned, or experiences a split-brain situation.

You can check cluster integrity using the following status variables:

- :ref:`wsrep_cluster_state_uuid <wsrep_cluster_state_uuid>` shows the cluster :term:`state UUID`, which you can use to determine whether the node is part of the cluster.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_cluster_state_uuid';

     +--------------------------+--------------------------------------+
     | Variable_name            | Value                                |
     +--------------------------+--------------------------------------+
     | wsrep_cluster_state_uuid | d6a51a3a-b378-11e4-924b-23b6ec126a13 |
     +--------------------------+--------------------------------------+

  Each node in the cluster should provide the same value.  When a node carries a different value, this indicates that it is no longer connected to rest of the cluster.  Once the node reestablishes connectivity, it realigns itself with the other nodes.

- :ref:`wsrep_cluster_conf_id <wsrep_cluster_conf_id>` shows the total number of cluster changes that have happened, which you can use to determine whether or not the node is a part of the :term:`Primary Component`.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_cluster_conf_id';

     +-----------------------+-------+
     | Variable_name         | Value |
     +-----------------------+-------+
     | wsrep_cluster_conf_id | 32    |
     +-----------------------+-------+

  Each node in the cluster should provide the same value.  When a node carries a different, this indicates that the cluster is partitioned.  Once the node reestablishes network connectivity, the value aligns itself with the others.

- :ref:`wsrep_cluster_size <wsrep_cluster_size>` shows the number of nodes in the cluster, which you can use to determine if any are missing.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';

     +--------------------+-------+
     | Variable_name      | Value |
     +--------------------+-------+
     | wsrep_cluster_size | 15    |
     +--------------------+-------+

  You can run this check on any node.  When the check returns a value lower than the number of nodes in your cluster, it means that some nodes have lost network connectivity or they have failed.

- :ref:`wsrep_cluster_status <wsrep_cluster_status>` shows the primary status of the cluster component that the node is in, which you can use in determining whether your cluster is experiencing a partition.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';

     +----------------------+---------+
     | Variable_name        | Value   |
     +----------------------+---------+
     | wsrep_cluster_status | Primary |
     +----------------------+---------+

  The node should only return a value of ``Primary``.  Any other value indicates that the node is part of a nonoperational component.  This occurs in cases of multiple membership changes that result in a loss of quorum or in cases of split-brain situations.

  .. note:: If you check all nodes in your cluster and find none that return a value of ``Primary``, see :doc:`quorum-reset`.

When these status variables check out and return the desired results on each node, the cluster is up and has integrity.  What this means is that replication is able to occur normally on every node.  The next step then is :ref:`checking node status <check-node-status>` to ensure that they are all in working order and able to receive write-sets.



.. _`check-node-status`:
.. rst-class:: section-heading
.. rubric:: Checking the Node Status

.. index::
   pair: Parameters; wsrep_cluster_address

.. index::
   pair: Parameters; wsrep_ready

.. index::
   pair: Parameters; wsrep_connected

.. index::
   pair: Parameters; wsrep_local_state_comment

In addition to checking cluster integrity, you can also monitor the status of individual nodes.  This shows whether nodes receive and process updates from the cluster write-sets and can indicate problems that may prevent replication.

- :ref:`wsrep_ready <wsrep_ready>` shows whether the node can accept queries.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_ready';

     +---------------+-------+
     | Variable_name | Value |
     +---------------+-------+
     | wsrep_ready   | ON    |
     +---------------+-------+

  When the node returns a value of ``ON`` it can accept write-sets from the cluster.  When it returns the value ``OFF``, almost all queries fail with the error:

  .. code-block:: text

     ERROR 1047 (08501) Unknown Command

- :ref:`wsrep_connected <wsrep_connected>` shows whether the node has network connectivity with any other nodes.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_connected';

     +-----------------+-------+
     | Variable_name   | Value |
     +-----------------+-------+
     | wsrep_connected | ON    |
     +-----------------+-------+

  When the value is ``ON``, the node has a network connection to one or more other nodes forming a cluster component.  When the value is ``OFF``, the node does not have a connection to any cluster components.

  .. note:: The reason for a loss of connectivity can also relate to misconfiguration.  For instance, if the node uses invalid values for the :ref:`wsrep_cluster_address <wsrep_cluster_address>` or :ref:`wsrep_cluster_name <wsrep_cluster_name>` parameters.

  Check the error log for proper diagnostics.

- :ref:`wsrep_local_state_comment <wsrep_local_state_comment>` shows the node state in a human readable format.

  .. code-block:: mysql

     SHOW GLOBAL STATUS LIKE 'wsrep_local_state_comment';

     +---------------------------+--------+
     | Variable_name             | Value  |
     +---------------------------+--------+
     | wsrep_local_state_comment | Joined |
     +---------------------------+--------+

  When the node is part of the :term:`Primary Component`, the typical return values are ``Joining``, ``Waiting on SST``, ``Joined``, ``Synced`` or ``Donor``.  If the node is part of a nonoperational component, the return value is ``Initialized``.

  .. note:: If the node returns any value other than the one listed here, the state comment is momentary and transient.  Check the status variable again for an update.

In the event that each status variable returns the desired values, the node is in working order.  This means that it is receiving write-sets from the cluster and replicating them to tables in the local database.


.. _`check-replication-health`:
.. rst-class:: section-heading
.. rubric:: Checking the Replication Health

.. index::
   pair: Parameters; wsrep_flow_control_paused
.. index::
   pair: Parameters; wsrep_cert_deps_distance
.. index::
   pair: Parameters; wsrep_local_recv_queue_avg
.. index::
   pair: Parameters; wsrep_local_recv_queue_max
.. index::
   pair: Parameters; wsrep_local_recv_queue_min


Monitoring cluster integrity and node status can show you issues that may prevent or otherwise block replication.  These status variables will help in identifying performance issues and identifying problem areas so that you can get the most from your cluster.


.. note:: Unlike other the status variables, these are differential and reset on every ``FLUSH STATUS`` command.

Galera Cluster triggers a feedback mechanism called Flow Control to manage the replication process.  When the local received queue of write-sets exceeds a certain threshold, the node engages Flow Control to pause replication while it catches up.

You can monitor the local received queue and Flow Control using the following status variables:

- :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>` shows the average size of the local received queue since the last status query.

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_local_recv_queue_avg';

     +--------------------------+----------+
     | Variable_name            | Value    |
     +--------------------------+----------+
     | wsrep_local_recv_que_avg | 3.348452 |
     +--------------------------+----------+

  When the node returns a value higher than ``0.0`` it means that the node cannot apply write-sets as fast as it receives them, which can lead to replication throttling.

  .. note::  In addition to this status variable, you can also use :ref:`wsrep_local_recv_queue_max <wsrep_local_recv_queue_max>` and :ref:`wsrep_local_recv_queue_min <wsrep_local_recv_queue_min>` to see the maximum and minimum sizes the node recorded for the local received queue.

- :ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>` shows the fraction of the time, since ``FLUSH STATUS`` was last called, that the node paused due to Flow Control.

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_flow_control_paused';

     +---------------------------+----------+
     | Variable_name             | Value    |
     +---------------------------+----------+
     | wsrep_flow_control_paused | 0.184353 |
     +---------------------------+----------+

  When the node returns a value of ``0.0``, it indicates that the node did not pause due to Flow Control during this period.  When the node returns a value of ``1.0``, it indicates that the node spent the entire period paused.  If the time between ``FLUSH STATUS`` and ``SHOW STATUS`` was one minute and the node returned ``0.25``, it indicates that the node was paused for a total 15 seconds over that time period.

  Ideally, the return value should stay as close to ``0.0`` as possible, since this means the node is not falling behind the cluster.  In the event that you find that the node is pausing frequently, you can adjust the :ref:`wsrep_slave_threads <wsrep_slave_threads>` parameter or you can exclude the node from the cluster.

- :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>` shows the average distance between the lowest and highest sequence number, or seqno, values that the node can possibly apply in parallel.

  .. code-block:: mysql

     SHOW STATUS LIKE 'wsrep_cert_deps_distance';

     +--------------------------+---------+
     | Variable_name            | Value   |
     +--------------------------+---------+
     | wsrep_cert_deps_distance | 23.8889 |
     +--------------------------+---------+

  This represents the node's potential degree for parallelization.  In other words, the optimal value you can use with the :ref:`wsrep_slave_threads <wsrep_slave_threads>` parameter, given that there is no reason to assign more slave threads than transactions you can apply in parallel.

.. _`check-network-issues`:
.. rst-class:: section-heading
.. rubric:: Detecting Slow Network Issues

.. index::
   pair: Parameters; wsrep_local_send_queue_avg
.. index::
   pair: Parameters; wsrep_local_send_queue_max
.. index::
   pair: Parameters; wsrep_local_send_queue_min

While checking the status of Flow Control and the received queue can tell you how the database server copes with incoming write-sets, you can check the send queue to monitor for outgoing connectivity issues.

.. note:: Unlike other the status variables, these are differential and reset on every ``FLUSH STATUS`` command.


:ref:`wsrep_local_send_queue_avg <wsrep_local_send_queue_avg>` show an average for the send queue length since the last ``FLUSH STATUS`` query.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_send_queue_avg | 0.145000 |
   +----------------------------+----------+

Values much greater than ``0.0`` indicate replication throttling or network throughput issues, such as a bottleneck on the network link.  The problem can occur at any layer from the physical components of your server to the configuration of the operating system.


.. note::  In addition to this status variable, you can also use :ref:`wsrep_local_send_queue_max <wsrep_local_send_queue_max>` and :ref:`wsrep_local_send_queue_min <wsrep_local_send_queue_min>` to see the maximum and minimum sizes the node recorded for the local send queue.

.. container:: bottom-links

   Related Documents

   - :doc:`notification-cmd`
   - :doc:`Reset Quorum <quorum-reset>`
   - :ref:`checking node status <check-node-status>`
   - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`
   - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
   - :ref:`wsrep_cluster_conf_id <wsrep_cluster_conf_id>`
   - :ref:`wsrep_cluster_name <wsrep_cluster_name>`
   - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
   - :ref:`wsrep_cluster_state_uuid <wsrep_cluster_state_uuid>`
   - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
   - :ref:`wsrep_connected <wsrep_connected>`
   - :ref:`wsrep_local_send_queue_avg <wsrep_local_send_queue_avg>`
   - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`
   - :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`
   - :ref:`wsrep_local_recv_queue_max <wsrep_local_recv_queue_max>`
   - :ref:`wsrep_local_recv_queue_min <wsrep_local_recv_queue_min>`
   - :ref:`wsrep_ready <wsrep_ready>`
   - :ref:`wsrep_slave_threads <wsrep_slave_threads>`
