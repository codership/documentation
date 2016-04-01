=========================
 Galera Status Variables
=========================
.. _`MySQL wsrep Options`:

These variables are *Galera Cluster* 0.8.x status variables. There are two types of wsrep-related status variables:

- Galera Cluster-specific variables exported by Galera Cluster

- Variables exported by MySQL. These variables are for the general wsrep provider. 

This distinction is of importance for developers only.  For convenience, all status variables are presented as a single list below.  Variables exported by MySQL are indicated by an *M* in superscript.

+---------------------------------------+------------------------------------------+------------+
| Status Variable                       | Example                                  | Support    |
+=======================================+==========================================+============+
| :ref:`wsrep_apply_oooe                | ``0.671120``                             | 1+         |
| <wsrep_apply_oooe>`                   |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_apply_oool                | ``0.195248``                             | 1+         | 
| <wsrep_apply_oool>`                   |                                          |            | 
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_apply_window              | ``5.163966``                             | 1+         |
| <wsrep_apply_window>`                 |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cert_deps_distance        | ``23.88889``                             | 1+         |
| <wsrep_cert_deps_distance>`           |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cert_index_size           | ``30936``                                | 1+         |
| <wsrep_cert_index_size>`              |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cert_interval             |                                          | 1+         |
| <wsrep_cert_interval>`                |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cluster_conf_id           | ``34``                                   | 1+         |
| <wsrep_cluster_conf_id>` :sup:`M`     |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cluster_size              | ``3``                                    | 1+         |
| <wsrep_cluster_size>` :sup:`M`        |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cluster_state_uuid        |                                          | 1+         |
| <wsrep_cluster_state_uuid>` :sup:`M`  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_cluster_status            | ``Primary``                              | 1+         |
| <wsrep_cluster_status>` :sup:`M`      |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_commit_oooe               | ``0.000000``                             | 1+         |
| <wsrep_commit_oooe>`                  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_commit_oool               | ``0.000000``                             | 1+         |
| <wsrep_commit_oool>`                  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_commit_window             | ``0.000000``                             | 1+         |
| <wsrep_commit_window>`                |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_connected                 | ``ON``                                   | 1+         |
| <wsrep_connected>`                    |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_evs_delayed               |                                          | 3.8+       |
| <wsrep_evs_delayed>`                  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_evs_evict_list            |                                          | 3.8+       |
| <wsrep_evs_evict_list>`               |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_evs_repl_latency          |                                          | 3.0+       |
| <wsrep_evs_repl_latency>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_evs_state                 |                                          | 3.8+       |
| <wsrep_evs_state>`                    |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_desync_count              | ``0``                                    | 3+         |
| <wsrep_desync_count>`                 |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_flow_control_paused       | ``0.184353``                             | 1+         |
| <wsrep_flow_control_paused>`          |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_flow_control_paused_ns    | ``20222491180``                          | 1+         |
| <wsrep_flow_control_paused_ns>`       |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_flow_control_recv         | ``11``                                   | 1+         |
| <wsrep_flow_control_recv>`            |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_flow_control_sent         | ``7``                                    | 1+         |
| <wsrep_flow_control_sent>`            |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_gcomm_uuid                |                                          | 1+         |
| <wsrep_gcomm_uuid>`                   |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_incoming_addresses        |                                          | 1+         |
| <wsrep_incoming_addresses>`           |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_last_committed            | ``409745``                               | 1+         |
| <wsrep_last_committed>`               |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_bf_aborts           | ``960``                                  | 1+         |
| <wsrep_local_bf_aborts>`              |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_cached_downto       |                                          | 1+         |
| <wsrep_local_cached_downto>`          |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_cert_failures       | ``333``                                  | 1+         |
| <wsrep_local_cert_failures>`          |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_commits             | ``14981``                                | 1+         |
| <wsrep_local_commits>`                |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_index               | ``1``                                    | 1+         |
| <wsrep_local_index>`                  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_recv_queue          | ``0``                                    | 1+         |
| <wsrep_local_recv_queue>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_recv_queue_avg      | ``3.348452``                             | 1+         |
| <wsrep_local_recv_queue_avg>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_recv_queue_max      | ``10``                                   | 1+         |
| <wsrep_local_recv_queue_max>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_recv_queue_min      | ``0``                                    | 1+         |
| <wsrep_local_recv_queue_min>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_replays             | ``0``                                    | 1+         |
| <wsrep_local_replays>`                |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_send_queue          | ``1``                                    | 1+         |
| <wsrep_local_send_queue>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_send_queue_avg      | ``0.145000``                             | 1+         |
| <wsrep_local_send_queue_avg>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_send_queue_max      | ``10``                                   | 1+         |
| <wsrep_local_send_queue_max>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_send_queue_min      | ``0``                                    | 1+         |
| <wsrep_local_send_queue_min>`         |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_state               | ``4``                                    | 1+         |
| <wsrep_local_state>`                  |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_state_comment       | ``Synced``                               | 1+         |
| <wsrep_local_state_comment>`          |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_local_state_uuid          |                                          | 1+         |
| <wsrep_local_state_uuid>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_protocol_version          | ``4``                                    | 1+         |
| <wsrep_protocol_version>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_provider_name             | ``Galera``                               | 1+         |
| <wsrep_provider_name>` :sup:`M`       |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_provider_vendor           |                                          | 1+         |
| <wsrep_provider_vendor>` :sup:`M`     |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_provider_version          |                                          | 1+         |
| <wsrep_provider_version>` :sup:`M`    |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_ready                     | ``ON``                                   | 1+         |
| <wsrep_ready>` :sup:`M`               |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_received                  | ``17831``                                | 1+         |
| <wsrep_received>`                     |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_received_bytes            | ``6637093``                              | 1+         |
| <wsrep_received_bytes>`               |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_repl_data_bytes           | ``265035226``                            | 1+         |
| <wsrep_repl_data_bytes>`              |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_repl_keys                 | ``797399``                               | 1+         |
| <wsrep_repl_keys>`                    |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_repl_keys_bytes           | ``11203721``                             | 1+         |
| <wsrep_repl_keys_bytes>`              |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_repl_other_bytes          | ``0``                                    | 1+         |
| <wsrep_repl_other_bytes>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_replicated                | ``16109``                                | 1+         |
| <wsrep_replicated>`                   |                                          |            |
+---------------------------------------+------------------------------------------+------------+
| :ref:`wsrep_replicated_bytes          | ``6526788``                              | 1+         |
| <wsrep_replicated_bytes>`             |                                          |            |
+---------------------------------------+------------------------------------------+------------+





.. rubric:: ``wsrep_apply_oooe``
.. _`wsrep_apply_oooe`:
.. index::
   pair: Status Variables; wsrep_apply_oooe

How often applier started write-set applying out-of-order (parallelization efficiency).

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_oooe';

   +------------------+----------+
   | Variable_name    | Value    |
   +------------------+----------+
   | wsrep_apply_oooe | 0.671120 |
   +------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.671120``       | Galera    |            |            |
+--------------------+-----------+------------+------------+

.. rubric:: ``wsrep_apply_oool``
.. _`wsrep_apply_oool`:
.. index::
   pair: Status Variables; wsrep_apply_oool

How often write-set was so slow to apply that write-set with higher seqno's were applied earlier. Values closer to 0 refer to a greater gap between slow and fast write-sets.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_oool';

   +------------------+----------+
   | Variable_name    | Value    |
   +------------------+----------+
   | wsrep_apply_oool | 0.195248 |
   +------------------+----------+



+-------------------+-----------+------------+------------+
| Example Value     | Location  | Introduced | Deprecated |
+===================+===========+============+============+
| ``0.195248``      | Galera    |            |            |
+-------------------+-----------+------------+------------+


.. rubric:: ``wsrep_apply_window``
.. _`wsrep_apply_window`:
.. index::
   pair: Status Variables; wsrep_apply_window

Average distance between highest and lowest concurrently applied seqno. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_window';

   +--------------------+----------+
   | Variable_name      | Value    |
   +--------------------+----------+
   | wsrep_apply_window | 5.163966 |
   +--------------------+----------+


+-------------------+-----------+------------+------------+
| Example Value     | Location  | Introduced | Deprecated |
+===================+===========+============+============+
| ``5.163966``      | Galera    |            |            |
+-------------------+-----------+------------+------------+

.. rubric:: ``wsrep_cert_deps_distance``
.. _`wsrep_cert_deps_distance`:
.. index::
   pair: Status Variables; wsrep_cert_deps_distance

Average distance between highest and lowest seqno value that can be possibly applied in parallel (potential degree of parallelization). 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_deps_distance';

   +--------------------------+----------+
   | Variable_name            | Value    |
   +--------------------------+----------+
   | wsrep_cert_deps_distance | 23.88889 |
   +--------------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``23.888889``      | Galera    |            |            |
+--------------------+-----------+------------+------------+

.. rubric:: ``wsrep_cert_index_size``
.. _`wsrep_cert_index_size`:
.. index::
   pair: Status Variables; wsrep_cert_index_size

The number of entries in the certification index.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_certs_index_size';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_certs_index_size | 30936 |
   +------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``30936``          | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_cert_interval``
.. _`wsrep_cert_interval`:
.. index::
   pair: Status Variables; wsrep_cert_interval

Average number of transactions received while a transaction replicates.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_interval';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_cert_interval | 1.0   |
   +---------------------+-------+

When a node replicates a write-set to the cluster, it can take some time before all the nodes in the cluster receive it.  By the time a given node receives, orders and commits a write-set, it may receive and potentially commit others, changing the state of the database from when the write-set was sent and rendering the transaction inapplicable.

To prevent this, Galera Cluster checks write-sets against all write-sets within its certification interval for potential conflicts.  Using the :ref:`wsrep_cert_interval <wsrep_cert_interval>` status variable, you can see the average number of transactions with the certification interval.  

This shows you the number of write-sets concurrently replicating to the cluster. In a fully synchronous cluster, with one write-set replicating at a time, :ref:`wsrep_cert_interval <wsrep_cert_interval>` returns a value of ``1.0``.

+---------------+-----------+------------+------------+
| Example Value | Location  | Introduced | Deprecated |
+===============+===========+============+============+
| ``1.0``       | Galera    |            |            |
+---------------+-----------+------------+------------+  
 
.. rubric:: ``wsrep_cluster_conf_id``
.. _`wsrep_cluster_conf_id`:
.. index::
   pair: Status Variables; wsrep_cluster_conf_id

Total number of cluster membership changes happened. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_conf_id';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_cluster_conf_id | 34    |
   +-----------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``34``             | MySQL     |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_cluster_size``
.. _`wsrep_cluster_size`:
.. index::
   pair: Status Variables; wsrep_cluster_size

Current number of members in the cluster.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 15    |
   +--------------------+-------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``3``              | MySQL     |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_cluster_state_uuid``
.. _`wsrep_cluster_state_uuid`:
.. index::
   pair: Status Variables; wsrep_cluster_state_uuid

Provides the current State UUID.  This is a unique identifier for the current state of the cluster and the sequence of changes it undergoes.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_state_uuid';

   +--------------------------+--------------------------------------+
   | Variable_name            | Value                                |
   +--------------------------+--------------------------------------+
   | wsrep_cluster_state_uuid | e2c9a15e-5485-11e0-0800-6bbb637e7211 |
   +--------------------------+--------------------------------------+

.. note:: **See Also**: For more information on the state UUID, see :ref:`wsrep API <wsrep-api>`.


+------------------------+-----------+------------+------------+
| Example Value          | Location  | Introduced | Deprecated |
+========================+===========+============+============+
| ``e2c9a15e-5485-11e0   | MySQL     |            |            |
| 0900-6bbb637e7211``    |           |            |            |
+------------------------+-----------+------------+------------+


.. rubric:: ``wsrep_cluster_status``
.. _`wsrep_cluster_status`:
.. index::
   pair: Status Variables; wsrep_cluster_status

Status of this cluster component.  That is, whether the node is part of a ``PRIMARY`` or ``NON_PRIMARY`` component.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_status';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_cluster_status | Primary |
   +----------------------+---------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``Primary``        | MySQL     |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_commit_oooe``
.. _`wsrep_commit_oooe`:
.. index::
   pair: Status Variables; wsrep_commit_oooe

How often a transaction was committed out of order.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_oooe';

   +-------------------+----------+
   | Variable_name     | Value    |
   +-------------------+----------+
   | wsrep_commit_oooe | 0.000000 |
   +-------------------+----------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.000000``       | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_commit_oool``
.. _`wsrep_commit_oool`:
.. index::
   pair: Status Variables; wsrep_commit_oool

No meaning.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_oool';

   +-------------------+----------+
   | Variable_name     | Value    |
   +-------------------+----------+
   | wsrep_commit_oool | 0.000000 |
   +-------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.000000``       | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_commit_window``
.. _`wsrep_commit_window`:
.. index::
   pair: Status Variables; wsrep_commit_window

Average distance between highest and lowest concurrently committed seqno. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_window';

   +---------------------+----------+
   | Variable_name       | Value    |
   +---------------------+----------+
   | wsrep_commit_window | 0.000000 |
   +---------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.000000``       | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_connected``
.. _`wsrep_connected`:
.. index::
   pair: Status Variables; wsrep_connected

If the value is ``OFF``, the node has not yet connected to any of the cluster components. This may be due to misconfiguration. Check the error log for proper diagnostics.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_connected';

   +-----------------+-------+
   | Variable_name   | Value |
   +-----------------+-------+
   | wsrep_connected | ON    |
   +-----------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``ON``             | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_evs_delayed``	    
.. _`wsrep_evs_delayed`:
.. index::
   pair: Status Variables; wsrep_evs_delayed

Provides a comma separated list of all the nodes this node has registered on its delayed list.

The node listing format is

.. code-block:: text

   uuid:address:count

This refers to the UUID and IP address of the delayed node, with a count of the number of entries it has on the delayed list.
   

+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
|                    | Galera    | 3.8        |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_evs_evict_list``
.. _`wsrep_evs_evict_list`:
.. index::
   pair: Status Variables; wsrep_evs_evict_list

Lists the UUID's of all nodes evicted from the cluster.  Evicted nodes cannot rejoin the cluster until you restart their ``mysqld`` processes.


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
|                    | Galera    | 3.8        |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_evs_repl_latency``
.. _`wsrep_evs_repl_latency`:
.. index::
   pair: Parameters; wsrep_evs_repl_latency

This status variable provides figures for the replication latency on group communication.  It measures latency from the time point when a message is sent out to the time point when a message is received.  As replication is a group operation, this essentially gives you the slowest ACK and longest RTT in the cluster.

For example,

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_evs_repl_latency';

   +------------------------+------------------------------------------+
   | Variable_name          | Value                                    |
   +------------------------+------------------------------------------+
   | wsrep_evs_repl_latency | 0.00243433/0.144022/0.591963/0.215824/13 |
   +------------------------+------------------------------------------+

The units are in seconds.  The format of the return value is:

.. code-block:: text

   Minimum / Average / Maximum / Standard Deviation / Sample Size

This variable periodically resets.  You can control the reset interval using the :ref:`evs.stats_report_period <evs.stats_report_period>` parameter.  The default value is 1 minute.


+-------------------------+-----------+------------+------------+
| Example Value           | Location  | Introduced | Deprecated |
+=========================+===========+============+============+
| ``0.00243433/0.144033/  | Galera    | 3.0        |            |
| 0.581963/0.215724/13``  |           |            |            |
+-------------------------+-----------+------------+------------+



.. rubric:: ``wsrep_evs_state``
.. _`wsrep_evs_state`:
.. index::
   pair: Status Variables; wsrep_evs_state

Shows the internal state of the EVS Protocol.

+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
|                    | Galera    | 3.8        |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_desync_count``
.. _`wsrep_desync_count`:
.. index::
   pair: Status Variables; wsrep_desync_count

Returns the number of operations in progress that require the node to temporarily desync from the cluster.
   
.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_desync_count';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_desync_count | 1     |
   +--------------------+-------+
   
Certain operations, such as DDL statements issued when :ref:`wsrep_OSU_method <wsrep_OSU_method>` is set to Rolling Schema Upgrade or when you enable :ref:`wsrep_desync <wsrep_desync>`  cause the node to desync from the cluster.  The counter on this status variable shows how many of these operations are currently running on the node.  When all of these operations complete, the counter returns to its default value ``0`` and the node can sync back to the cluster.

   
+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    | 3.8        |            |
+--------------------+-----------+------------+------------+



   


.. rubric:: ``wsrep_flow_control_paused``
.. _`wsrep_flow_control_paused`:
.. index::
   pair: Status Variables; wsrep_flow_control_paused

The fraction of time since the last ``FLUSH STATUS`` command that replication was paused due to flow control.

In other words, how much the slave lag is slowing down the cluster. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_paused';

   +---------------------------+----------+
   | Variable_name             | Value    |
   +---------------------------+----------+
   | wsrep_flow_control_paused | 0.184353 |
   +---------------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.174353``       | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_flow_control_paused_ns``
.. _`wsrep_flow_control_paused_ns`:
.. index::
   pair: Status Variables; wsrep_flow_control_paused_ns

The total time spent in a paused state measured in nanoseconds.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_paused_ns';

   +------------------------------+-------------+
   | Variable_name                | Value       |
   +------------------------------+-------------+
   | wsrep_flow_control_paused_ns | 20222491180 |
   +------------------------------+-------------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``20222491180``    | Galera    |            |            |
+--------------------+-----------+------------+------------+


   
.. rubric:: ``wsrep_flow_control_recv``
.. _`wsrep_flow_control_recv`:
.. index::
   pair: Status Variables; wsrep_flow_control_recv

Returns the number of ``FC_PAUSE`` events the node has received, including those the node has sent.  Unlike most status variables, the counter for this one does not reset every time you run the query.


.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_recv';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_flow_control_recv | 11    |
   +-------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``11``             | Galera    |            |            |
+--------------------+-----------+------------+------------+


 
.. rubric:: ``wsrep_flow_control_sent``
.. _`wsrep_flow_control_sent`:
.. index::
   pair: Status Variables; wsrep_flow_control_sent

Returns the number of ``FC_PAUSE`` events the node has sent.  Unlike most status variables, the counter for this one does not reset every time you run the query.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_sent';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_flow_control_sent | 7     |
   +-------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``7``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_gcomm_uuid``
.. _`wsrep_gcomm_uuid`:
.. index::
   pair: Status Variables; wsrep_gcomm_uuid

Displays the group communications UUID.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_gcomm_uuid';

   +------------------+--------------------------------------+
   | Variable_name    | Value                                |
   +------------------+--------------------------------------+
   | wsrep_gcomm_uuid | 7e729708-605f-11e5-8ddd-8319a704b8c4 |
   +------------------+--------------------------------------+

+--------------------------------------------+-----------+------------+------------+
| Example Value                              | Location  | Introduced | Deprecated |
+============================================+===========+============+============+
| ``7e729708-605f-11e5-8ddd-8319a704b8c4``   | Galera    | 1          |            |
+--------------------------------------------+-----------+------------+------------+

.. rubric:: ``wsrep_incoming_addresses``
.. _`wsrep_incoming_addresses`:
.. index::
   pair: Status Variables; wsrep_incoming_addresses

Comma-separated list of incoming server addresses in the cluster component.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_incoming_addresses';

   +--------------------------+--------------------------------------+
   | Variable_name            | Value                                |
   +--------------------------+--------------------------------------+
   | wsrep_incoming_addresses | 10.0.0.1:3306,10.0.02:3306,undefined |
   +--------------------------+--------------------------------------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``10.0.0.1:3306,   | Galera    |            |            |
| 10.0.0.2:3306,     |           |            |            |
| undefined``        |           |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_last_committed``
.. _`wsrep_last_committed`:
.. index::
   pair: Status Variables; wsrep_last_committed

The sequence number, or seqno, of the last committed transaction. See :ref:`wsrep API <wsrep-api>`.  

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

.. note:: **See Also**: For more information, see :ref:`wsrep API <wsrep-api>`.


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``409745``         | Galera    |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_local_bf_aborts``
.. _`wsrep_local_bf_aborts`:
.. index::
   pair: Status Variables; wsrep_local_bf_aborts

Total number of local transactions that were aborted by slave transactions while in execution.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_bf_aborts';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_local_bf_aborts | 960   |
   +-----------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``960``            | Galera    |            |            |
+--------------------+-----------+------------+------------+

   
.. rubric:: ``wsrep_local_cached_downto``
.. _`wsrep_local_cached_downto`:
.. index::
   pair: Status Variables; wsrep_local_cached_downto

The lowest sequence number, or seqno, in the write-set cache (GCache).

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_cached_downto';

   +---------------------------+----------------------+
   | Variable_name             | Value                |
   +---------------------------+----------------------+
   | wsrep_local_cached_downto | 18446744073709551615 |
   +---------------------------+----------------------+


+--------------------------+-----------+------------+------------+
| Example Value            | Location  | Introduced | Deprecated |
+==========================+===========+============+============+
| ``18446744073709551615`` | Galera    |            |            |
+--------------------------+-----------+------------+------------+



.. rubric:: ``wsrep_local_cert_failures``
.. _`wsrep_local_cert_failures`:
.. index::
   pair: Status Variables; wsrep_local_cert_failures

Total number of local transactions that failed certification test.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_cert_failures';

   +---------------------------+-------+
   | Variable_name             | Value |
   +---------------------------+-------+
   | wsrep_local_cert_failures | 333   |
   +---------------------------+-------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``333``            | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_commits``
.. _`wsrep_local_commits`:
.. index::
   pair: Status Variables; wsrep_local_commits

Total number of local transactions committed.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_commits';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_local_commits | 14981 |
   +---------------------+-------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``14981``          | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_index``
.. _`wsrep_local_index`:
.. index::
   pair: Status Variables; wsrep_local_index

This node index in the cluster (base 0).

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_index';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_local_index | 1     |
   +-------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``1``              | MySQL     |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_recv_queue``
.. _`wsrep_local_recv_queue`:
.. index::
   pair: Status Variables; wsrep_local_recv_queue

Current (instantaneous) length of the recv queue. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue';
  
   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_local_recv_queue | 0     |
   +------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_local_recv_queue_avg``
.. _`wsrep_local_recv_queue_avg`:
.. index::
   pair: Status Variables; wsrep_local_recv_queue_avg

Recv queue length averaged over interval since the last ``FLUSH STATUS`` command. Values considerably larger than ``0.0`` mean that the node cannot apply write-sets as fast as they are received and will generate a lot of replication throttling. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_recv_queue_avg | 3.348452 |
   +----------------------------+----------+
   

+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``3.348452``       | Galera    |            |            |
+--------------------+-----------+------------+------------+

   
.. rubric:: ``wsrep_local_recv_queue_max``
.. _`wsrep_local_recv_queue_max`:
.. index::
   pair: Status Variables; wsrep_local_recv_queue_max

The maximum length of the recv queue since the last FLUSH STATUS command. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_max';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_recv_queue_max | 10    |
   +----------------------------+-------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``10``             | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_recv_queue_min``

.. _`wsrep_local_recv_queue_min`:

.. index::
   pair: Status Variables; wsrep_local_recv_queue_min

The minimum length of the recv queue since the last FLUSH STATUS command. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_min';

   +-----------------------------+-------+
   | Variable_name               | Value |
   +-----------------------------+-------+
   | wsrep_local_recev_queue_min | 0     |
   +-----------------------------+-------+

   

+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_replays``
.. _`wsrep_local_replays`:
.. index::
   pair: Status Variables; wsrep_local_replays

Total number of transaction replays due to *asymmetric lock granularity*.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_replays';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_lcoal_replays | 0     |
   +---------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_local_send_queue``
.. _`wsrep_local_send_queue`:
.. index::
   pair: Status Variables; wsrep_local_send_queue

Current (instantaneous) length of the send queue.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_local_send_queue | 1     |
   +------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``1``              | Galera    |            |            |
+--------------------+-----------+------------+------------+

.. rubric:: ``wsrep_local_send_queue_avg``
.. _`wsrep_local_send_queue_avg`:
.. index::
   pair: Status Variables; wsrep_local_send_queue_avg

Send queue length averaged over time since the last ``FLUSH STATUS`` command. Values considerably larger than 0.0 indicate replication throttling or network throughput issue. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_send_queue_avg | 0.145000 |
   +----------------------------+----------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0.145000``       | Galera    |            |            |
+--------------------+-----------+------------+------------+



.. rubric:: ``wsrep_local_send_queue_max``
.. _`wsrep_local_send_queue_max`:
.. index::
   pair: Status Variables; wsrep_local_send_queue_max

The maximum length of the send queue since the last ``FLUSH STATUS`` command. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_max';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_send_queue_max | 10    |
   +----------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``10``             | Galera    |            |            |
+--------------------+-----------+------------+------------+




.. rubric:: ``wsrep_local_send_queue_min``

.. _`wsrep_local_send_queue_min`:

.. index::
   pair: Status Variables; wsrep_local_send_queue_min

The minimum length of the send queue since the last ``FLUSH STATUS`` command. 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_min';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_send_queue_min | 0     |
   +----------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_state``
.. _`wsrep_local_state`:
.. index::
   pair: Status Variables; wsrep_local_state

Internal Galera Cluster FSM state number.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_local_state | 4     |
   +-------------------+-------+

.. note:: **See Also**: For more information on the possible node states, see :ref:`Node State Changes <node-state-changes>`.



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``4``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_local_state_comment``
.. _`wsrep_local_state_comment`:
.. index::
   pair: Status Variables; wsrep_local_state_comment

Human-readable explanation of the state.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_local_state_comment | Synced |
   +---------------------------+--------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``Synced``         | Galera    |            |            |
+--------------------+-----------+------------+------------+

   

.. rubric:: ``wsrep_local_state_uuid``
.. _`wsrep_local_state_uuid`:
.. index::
   pair: Status Variables; wsrep_local_state_uuid

The UUID of the state stored on this node.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_uuid';

   +------------------------+--------------------------------------+
   | Variable_name          | Value                                |
   +------------------------+--------------------------------------+
   | wsrep_local_state_uuid | e2c9a15e-5485-11e0-0800-6bbb637e7211 |
   +------------------------+--------------------------------------+

.. note:: **See Also**: For more information on the state UUID, see :ref:`wsrep API <wsrep-api>`. 


+-----------------------+-----------+------------+------------+
| Example Value         | Location  | Introduced | Deprecated |
+=======================+===========+============+============+
| ``e2c9a15e-5385-11e0- | Galera    |            |            |
| 0800-6bbb637e7211``   |           |            |            |
+-----------------------+-----------+------------+------------+


.. rubric:: ``wsrep_protocol_version``
.. _`wsrep_protocol_version`:
.. index::
   pair: Status Variables; wsrep_protocol_version

The version of the wsrep Protocol used.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_protocol_version';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_protocol_version | 4     |
   +------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``4``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_provider_name``
.. _`wsrep_provider_name`:
.. index::
   pair: Status Variables; wsrep_provider_name

The name of the wsrep Provider.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_name';

   +---------------------+--------+
   | Variable_name       | Value  |
   +---------------------+--------+
   | wsrep_provider_name | Galera |
   +---------------------+--------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``Galera``         | MySQL     |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_provider_vendor``
.. _`wsrep_provider_vendor`:
.. index::
   pair: Status Variables; wsrep_provider_vendor

The name of the wsrep Provider vendor.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_vendor';

   +-----------------------+-----------------------------------+
   | Variable_name         | Value                             |
   +-----------------------+-----------------------------------+
   | wsrep_provider_vendor | Codership Oy <info@codership.com> |
   +-----------------------+-----------------------------------+


+------------------------+-----------+------------+------------+
| Example Value          | Location  | Introduced | Deprecated |
+========================+===========+============+============+
| ``Codership Oy         | MySQL     |            |            |
| <info@codership.com>`` |           |            |            |
+------------------------+-----------+------------+------------+


.. rubric:: ``wsrep_provider_version``
.. _`wsrep_provider_version`:
.. index::
   pair: Status Variables; wsrep_provider_version

The name of the wsrep Provider version string.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_version';
  
   +------------------------+----------------------+
   | Variable_name          | Value                |
   +------------------------+----------------------+
   | wsrep_provider_version | 25.3.5-wheezy(rXXXX) |
   +------------------------+----------------------+


+--------------------------+-----------+------------+------------+
| Example Value            | Location  | Introduced | Deprecated |
+==========================+===========+============+============+
| ``25.3.5-wheezy(rXXXX)`` | MySQL     |            |            |
+--------------------------+-----------+------------+------------+


.. rubric:: ``wsrep_ready``
.. _`wsrep_ready`:
.. index::
   pair: Status Variables; wsrep_ready

Whether the server is ready to accept queries. If this status is ``OFF``, almost all of the queries will fail with:

.. code-block:: text

    ERROR 1047 (08S01) Unknown Command

unless the ``wsrep_on`` session variable is set to ``0``.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_ready';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_ready   | ON    |
   +---------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``ON``             | MySQL     |            |            |
+--------------------+-----------+------------+------------+

   

.. rubric:: ``wsrep_received``
.. _`wsrep_received`:
.. index::
   pair: Status Variables; wsrep_received

Total number of write-sets received from other nodes.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_received';

   +----------------+-------+
   | Variable_name  | Value |
   +----------------+-------+
   | wsrep_received | 17831 |
   +----------------+-------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``17831``          | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_received_bytes``
.. _`wsrep_received_bytes`:
.. index::
   pair: Status Variables; wsrep_received_bytes

Total size of write-sets received from other nodes.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_received_bytes';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_received_bytes | 6637093 |
   +----------------------+---------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``6637093``        | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_repl_data_bytes``
.. _`wsrep_repl_data_bytes`:
.. index::
   pair: Status Variables; wsrep_repl_data_bytes

Total size of data replicated.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_data_bytes';

   +-----------------------+---------+
   | Variable_name         | Value   |
   +-----------------------+---------+
   | wsrep_repl_data_bytes | 6526788 |
   +-----------------------+---------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``6526788``        | Galera    |            |            |
+--------------------+-----------+------------+------------+

   
.. rubric:: ``wsrep_repl_keys``
.. _`wsrep_repl_keys`:
.. index::
   pair: Status Variables; wsrep_repl_keys

Total number of keys replicated.

.. code-blocK:: mysql

   SHOW STATUS LIKE 'wsrep_repl_keys';

   +-----------------+--------+
   | Variable_name   | Value  |
   +-----------------+--------+
   | wsrep_repl_keys | 797399 |
   +-----------------+--------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``797399``         | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_repl_keys_bytes``
.. _`wsrep_repl_keys_bytes`:
.. index::
   pair: Status Variables; wsrep_repl_keys_bytes

Total size of keys replicated.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_keys_bytes';

   +-----------------------+----------+
   | Variable_name         | Value    |
   +-----------------------+----------+
   | wsrep_repl_keys_bytes | 11203721 |
   +-----------------------+----------+



+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``11203721``       | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_repl_other_bytes``
.. _`wsrep_repl_other_bytes`:
.. index::
   pair: Status Variables; wsrep_repl_other_bytes

Total size of other bits replicated.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_other_bytes';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_repl_other_bytes | 0     |
   +------------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``0``              | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_replicated``
.. _`wsrep_replicated`:
.. index::
   pair: Status Variables; wsrep_replicated

Total number of write-sets replicated (sent to other nodes).

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_replicated';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_replicated | 16109 |
   +------------------+-------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``16109``          | Galera    |            |            |
+--------------------+-----------+------------+------------+


.. rubric:: ``wsrep_replicated_bytes``
.. _`wsrep_replicated_bytes`:
.. index::
   pair: Status Variables; wsrep_replicated_bytes

Total size of write-sets replicated.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_replicated_bytes';

   +------------------------+---------+
   | Variable_name          | Value   |
   +------------------------+---------+
   | wsrep_replicated_bytes | 6526788 |
   +------------------------+---------+


+--------------------+-----------+------------+------------+
| Example Value      | Location  | Introduced | Deprecated |
+====================+===========+============+============+
| ``6526788``        | Galera    |            |            |
+--------------------+-----------+------------+------------+



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
