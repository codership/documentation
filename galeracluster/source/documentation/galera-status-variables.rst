.. meta::
   :title: Galera Cluster Status Variables
   :description:
   :language: en-US
   :keywords: galera cluster, status variables, options, monitoring
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

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`galera-status-variables`:

=========================
Galera Status Variables
=========================

These variables are *Galera Cluster* 0.8.x status variables. There are two types of wsrep-related status variables:

- Galera Cluster-specific variables exported by Galera Cluster

- Variables exported by MySQL. These variables are for the general wsrep provider.

This distinction is of importance for developers only.  For convenience, all status variables are presented as a single list below. They're noted as to whether they are exported by Galera or by MySQL.

.. csv-table::
   :class: doc-options
   :header: "|br| Status Variable", "|br| Exporter", "Example |br| Value", "Initial |br| Version"
   :widths: 40, 15, 30, 15

   ":ref:`wsrep_apply_oooe <wsrep_apply_oooe>`", "Galera", "``0.671120``", "1.0"
   ":ref:`wsrep_apply_oool <wsrep_apply_oool>`", "Galera", "``0.195248``", "1.0"
   ":ref:`wsrep_apply_window <wsrep_apply_window>`", "Galera", "``5.163966``", "1.0"
   ":ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`", "Galera", "``23.88889``", "1.0"
   ":ref:`wsrep_cert_index_size <wsrep_cert_index_size>`", "Galera", "``30936``", "1.0"
   ":ref:`wsrep_cert_interval  <wsrep_cert_interval>`", "Galera", "", "1.0"
   ":ref:`wsrep_cluster_conf_id <wsrep_cluster_conf_id>`", "MySQL", "``34``", "1.0"
   ":ref:`wsrep_cluster_size <wsrep_cluster_size>`", "MySQL", "", "1.0"
   ":ref:`wsrep_cluster_state_uuid <wsrep_cluster_state_uuid>`", "MySQL", "", "1.0"
   ":ref:`wsrep_cluster_status <wsrep_cluster_status>`", "MySQL", "``Primary``", "1.0"
   ":ref:`wsrep_cluster_weight <wsrep_cluster_weight>`", "MySQL", "``3``", "3.24"
   ":ref:`wsrep_commit_oooe <wsrep_commit_oooe>`", "Galera", "``0.000000``", "1.0"
   ":ref:`wsrep_commit_oool <wsrep_commit_oool>`", "Galera", "``0.000000``", "1.0"
   ":ref:`wsrep_commit_window <wsrep_commit_window>`", "Galera", "``0.000000``", "1.0"
   ":ref:`wsrep_connected <wsrep_connected>`", "Galera", "``ON``", "1.0"
   ":ref:`wsrep_desync_count <wsrep_desync_count>`", "Galera", "``0``", "3.0"
   ":ref:`wsrep_evs_delayed <wsrep_evs_delayed>`", "Galera", "", "3.8"
   ":ref:`wsrep_evs_evict_list <wsrep_evs_evict_list>`", "Galera", "", "3.0"
   ":ref:`wsrep_evs_repl_latency <wsrep_evs_repl_latency>`", "Galera", "", "3.0"
   ":ref:`wsrep_evs_state <wsrep_evs_state>`", "Galera", "", "3.8"
   ":ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>`", "Galera", "``0.184353``", "1.0"
   ":ref:`wsrep_flow_control_paused_ns <wsrep_flow_control_paused_ns>`", "Galera", "``20222491180``", "1.0"
   ":ref:`wsrep_flow_control_recv <wsrep_flow_control_recv>`", "Galera", "``11``", "1.0"
   ":ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>`", "Galera", "``7`` ", "1.0"
   ":ref:`wsrep_gcomm_uuid <wsrep_gcomm_uuid>`", "Galera", "", "1.0"
   ":ref:`wsrep_incoming_addresses <wsrep_incoming_addresses>`", "Galera", "", "1.0"
   ":ref:`wsrep_last_committed <wsrep_last_committed>`", "Galera", "``409745`` ", "1.0"
   ":ref:`wsrep_local_bf_aborts <wsrep_local_bf_aborts>`", "Galera", "``960`` ", "1.0"
   ":ref:`wsrep_local_cached_downto <wsrep_local_cached_downto>`", "Galera", "", "1.0"
   ":ref:`wsrep_local_cert_failures <wsrep_local_cert_failures>`", "Galera", "``333`` ", "1.0"
   ":ref:`wsrep_local_commits <wsrep_local_commits>`", "Galera", "``14981``", "1.0"
   ":ref:`wsrep_local_index <wsrep_local_index>`", "Galera", "``1`` ", "1.0"
   ":ref:`wsrep_local_recv_queue <wsrep_local_recv_queue>`", "Galera", "``0`` ", "1.0"
   ":ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`", "Galera", "``3.348452``", "1.0"
   ":ref:`wsrep_local_recv_queue_max <wsrep_local_recv_queue_max>`", "Galera", "``10``", "1.0"
   ":ref:`wsrep_local_recv_queue_min <wsrep_local_recv_queue_min>`", "Galera", "``0``", "1.0"
   ":ref:`wsrep_local_replays <wsrep_local_replays>`", "Galera", "``0``", "1.0"
   ":ref:`wsrep_local_send_queue <wsrep_local_send_queue>`", "Galera", "``1`` ", "1.0"
   ":ref:`wsrep_local_send_queue_avg <wsrep_local_send_queue_avg>`", "Galera", "``0.145000``", "1.0"
   ":ref:`wsrep_local_send_queue_max <wsrep_local_send_queue_max>`", "Galera", "``10``", "1.0"
   ":ref:`wsrep_local_send_queue_min <wsrep_local_send_queue_min>`", "Galera", "``0``", "1.0"
   ":ref:`wsrep_local_state <wsrep_local_state>`", "Galera", "``4`` ", "1.0"
   ":ref:`wsrep_local_state_comment <wsrep_local_state_comment>`", "Galera", "``Synced``", "1.0"
   ":ref:`wsrep_local_state_uuid <wsrep_local_state_uuid>`", "Galera", "", "1.0"
   ":ref:`wsrep_open_connections <wsrep_open_connections>`", "Galera", "``3``", "3.24"
   ":ref:`wsrep_open_transactions <wsrep_open_transactions>`", "Galera", "``25``", "3.24"
   ":ref:`wsrep_protocol_version <wsrep_protocol_version>`", "Galera", "``4``", "1.0"
   ":ref:`wsrep_provider_name <wsrep_provider_name>`", "MySQL", "``Galera``", "1.0"
   ":ref:`wsrep_provider_vendor <wsrep_provider_vendor>`", "MySQL", "", "1.0"
   ":ref:`wsrep_provider_version <wsrep_provider_version>`", "MySQL", "", "1.0"
   ":ref:`wsrep_ready <wsrep_ready>`", "MySQL", "``ON``", "1.0"
   ":ref:`wsrep_received <wsrep_received>`", "Galera", "``17831``", "1.0"
   ":ref:`wsrep_received_bytes <wsrep_received_bytes>`", "Galera", "``6637093``", "1.0"
   ":ref:`wsrep_repl_data_bytes <wsrep_repl_data_bytes>`", "Galera", "``265035226``", "1.0"
   ":ref:`wsrep_repl_keys <wsrep_repl_keys>`", "Galera", "``797399``", "1.0"
   ":ref:`wsrep_repl_keys_bytes <wsrep_repl_keys_bytes>`", "Galera", "``11203721``", "1.0"
   ":ref:`wsrep_repl_other_bytes <wsrep_repl_other_bytes>`", "Galera", "``0``", "1.0"
   ":ref:`wsrep_replicated <wsrep_replicated>`", "Galera", "``16109``", "1.0"
   ":ref:`wsrep_replicated_bytes <wsrep_replicated_bytes>`", "Galera", "``6526788``", "1.0"


.. _`wsrep_apply_oooe`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_apply_oooe``

.. index::
   pair: Status Variables; wsrep_apply_oooe

How often applier started write-set applying out-of-order (parallelization efficiency).

.. csv-table::
   :class: doc-options

   "Example Value", "``0.671120``"
   "Location", "Galera"
   "Initial Version", "1.0"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_oooe';

   +------------------+----------+
   | Variable_name    | Value    |
   +------------------+----------+
   | wsrep_apply_oooe | 0.671120 |
   +------------------+----------+


.. _`wsrep_apply_oool`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_apply_oool``

.. index::
   pair: Status Variables; wsrep_apply_oool

How often write-set was so slow to apply that write-set with higher seqno's were applied earlier. Values closer to 0 refer to a greater gap between slow and fast write-sets.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.195248``"
   "Location", "Galera"
   "Initial Version", "1.0"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_oool';

   +------------------+----------+
   | Variable_name    | Value    |
   +------------------+----------+
   | wsrep_apply_oool | 0.195248 |
   +------------------+----------+


.. _`wsrep_apply_window`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_apply_window``

.. index::
   pair: Status Variables; wsrep_apply_window

Average distance between highest and lowest concurrently applied seqno.

.. csv-table::
   :class: doc-options

   "Example Value", "``5.163966``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_apply_window';

   +--------------------+----------+
   | Variable_name      | Value    |
   +--------------------+----------+
   | wsrep_apply_window | 5.163966 |
   +--------------------+----------+


.. _`wsrep_cert_deps_distance`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cert_deps_distance``

.. index::
   pair: Status Variables; wsrep_cert_deps_distance

Average distance between highest and lowest seqno value that can be possibly applied in parallel (potential degree of parallelization).

.. csv-table::
   :class: doc-options

   "Example Value", "``23.888889``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_deps_distance';

   +--------------------------+----------+
   | Variable_name            | Value    |
   +--------------------------+----------+
   | wsrep_cert_deps_distance | 23.88889 |
   +--------------------------+----------+


.. _`wsrep_cert_index_size`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cert_index_size``

.. index::
   pair: Status Variables; wsrep_cert_index_size

The number of entries in the certification index.

.. csv-table::
   :class: doc-options

   "Example Value", "``30936``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_certs_index_size';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_certs_index_size | 30936 |
   +------------------------+-------+


.. _`wsrep_cert_interval`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cert_interval``

.. index::
   pair: Status Variables; wsrep_cert_interval

Average number of transactions received while a transaction replicates.

.. csv-table::
   :class: doc-options

   "Example Value", "``1.0``"
   "Location", "Galera"
   "Initial Version", "???"

When a node replicates a write-set to the cluster, it can take some time before all the nodes in the cluster receive it.  By the time a given node receives, orders and commits a write-set, it may receive and potentially commit others, changing the state of the database from when the write-set was sent and rendering the transaction inapplicable.

To prevent this, Galera Cluster checks write-sets against all write-sets within its certification interval for potential conflicts.  Using the :ref:`wsrep_cert_interval <wsrep_cert_interval>` status variable, you can see the average number of transactions with the certification interval.

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_interval';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_cert_interval | 1.0   |
   +---------------------+-------+

This shows you the number of write-sets concurrently replicating to the cluster. In a fully synchronous cluster, with one write-set replicating at a time, :ref:`wsrep_cert_interval <wsrep_cert_interval>` returns a value of ``1.0``.


.. _`wsrep_cluster_conf_id`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cluster_conf_id``

.. index::
   pair: Status Variables; wsrep_cluster_conf_id

Total number of cluster membership changes happened.

.. csv-table::
   :class: doc-options

   "Example Value", "``34``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_conf_id';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_cluster_conf_id | 34    |
   +-----------------------+-------+


.. _`wsrep_cluster_size`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cluster_size``

.. index::
   pair: Status Variables; wsrep_cluster_size

Current number of members in the cluster.

.. csv-table::
   :class: doc-options

   "Example Value", "``3``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 15    |
   +--------------------+-------+


.. _`wsrep_cluster_state_uuid`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cluster_state_uuid``

.. index::
   pair: Status Variables; wsrep_cluster_state_uuid

Provides the current State UUID.  This is a unique identifier for the current state of the cluster and the sequence of changes it undergoes.

.. csv-table::
   :class: doc-options

   "Example Value", "``e2c9a15e-5485-11e00900-6bbb637e7211``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_state_uuid';

   +--------------------------+--------------------------------------+
   | Variable_name            | Value                                |
   +--------------------------+--------------------------------------+
   | wsrep_cluster_state_uuid | e2c9a15e-5485-11e0-0800-6bbb637e7211 |
   +--------------------------+--------------------------------------+

For more information on the state UUID, see :ref:`wsrep API <wsrep-api>`.


.. _`wsrep_cluster_status`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cluster_status``

.. index::
   pair: Status Variables; wsrep_cluster_status

Status of this cluster component.  That is, whether the node is part of a ``PRIMARY`` or ``NON_PRIMARY`` component.

.. csv-table::
   :class: doc-options

   "Example Value", "``Primary``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_status';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_cluster_status | Primary |
   +----------------------+---------+


.. _`wsrep_cluster_weight`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_cluster_weight``

.. index::
   pair: Status Variables; wsrep_cluster_weight

The total weight of the current members in the cluster. The value is counted as a sum of
of :ref:`pc.weight <pc.weight>` of the nodes in the current :term:`Primary Component`.

.. csv-table::
   :class: doc-options

   "Example Value", "``3``"
   "Location", "Galera"
   "Initial Version", "3.24"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_weight';

   +----------------------+-------+
   | Variable_name        | Value |
   +----------------------+-------+
   | wsrep_cluster_weight | 3     |
   +----------------------+-------+


.. _`wsrep_commit_oooe`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_commit_oooe``

.. index::
   pair: Status Variables; wsrep_commit_oooe

How often a transaction was committed out of order.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.000000``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_oooe';

   +-------------------+----------+
   | Variable_name     | Value    |
   +-------------------+----------+
   | wsrep_commit_oooe | 0.000000 |
   +-------------------+----------+


.. _`wsrep_commit_oool`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_commit_oool``

.. index::
   pair: Status Variables; wsrep_commit_oool

No meaning.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.000000``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_oool';

   +-------------------+----------+
   | Variable_name     | Value    |
   +-------------------+----------+
   | wsrep_commit_oool | 0.000000 |
   +-------------------+----------+


.. _`wsrep_commit_window`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_commit_window``

.. index::
   pair: Status Variables; wsrep_commit_window

Average distance between highest and lowest concurrently committed seqno.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.000000``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_commit_window';

   +---------------------+----------+
   | Variable_name       | Value    |
   +---------------------+----------+
   | wsrep_commit_window | 0.000000 |
   +---------------------+----------+


.. _`wsrep_connected`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_connected``

.. index::
   pair: Status Variables; wsrep_connected

If the value is ``OFF``, the node has not yet connected to any of the cluster components. This may be due to misconfiguration. Check the error log for proper diagnostics.

.. csv-table::
   :class: doc-options

   "Example Value", "``ON``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_connected';

   +-----------------+-------+
   | Variable_name   | Value |
   +-----------------+-------+
   | wsrep_connected | ON    |
   +-----------------+-------+


.. _`wsrep_desync_count`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_desync_count``

.. index::
   pair: Status Variables; wsrep_desync_count

Returns the number of operations in progress that require the node to temporarily desync from the cluster.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "3.8"

Certain operations, such as DDL statements issued when :ref:`wsrep_OSU_method <wsrep_OSU_method>` is set to Rolling Schema Upgrade or when you enable :ref:`wsrep_desync <wsrep_desync>`, cause the node to desync from the cluster.  This status variable shows how many of these operations are currently running on the node.  When all of these operations complete, the counter returns to its default value ``0`` and the node can sync back to the cluster.

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_desync_count';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_desync_count | 1     |
   +--------------------+-------+


.. _`wsrep_evs_delayed`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_evs_delayed``

.. index::
   pair: Status Variables; wsrep_evs_delayed

Provides a comma separated list of all the nodes this node has registered on its delayed list.

.. csv-table::
   :class: doc-options

   "Example Value", ""
   "Location", "Galera"
   "Initial Version", "3.8"

The node listing format is as follows:

.. code-block:: text

   uuid:address:count

This refers to the UUID and IP address of the delayed node, with a count of the number of entries it has on the delayed list.


.. _`wsrep_evs_evict_list`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_evs_evict_list``

.. index::
   pair: Status Variables; wsrep_evs_evict_list

Lists the UUID's of all nodes evicted from the cluster.  Evicted nodes cannot rejoin the cluster until you restart their ``mysqld`` processes.

.. csv-table::
   :class: doc-options

   "Example Value", ""
   "Location", "Galera"
   "Initial Version", "3.8"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_evs_evict_list';

   +----------------------+-------+
   | Variable_name        | Value |
   +----------------------+-------+
   | wsrep_evs_evict_list |       |
   +----------------------+-------+


.. _`wsrep_evs_repl_latency`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_evs_repl_latency``

.. index::
   pair: Parameters; wsrep_evs_repl_latency

This status variable provides figures for the replication latency on group communication.  It measures latency from the time point when a message is sent out to the time point when a message is received.  As replication is a group operation, this essentially gives you the slowest ACK and longest RTT in the cluster.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.00243433/0.144033/0.581963/0.215724/13``"
   "Location", "Galera"
   "Initial Version", "3.0"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

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


.. _`wsrep_evs_state`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_evs_state``

.. index::
   pair: Status Variables; wsrep_evs_state

Shows the internal state of the EVS Protocol.

.. csv-table::
   :class: doc-options

   "Example Value", ""
   "Location", "Galera"
   "Initial Version", "3.8"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_evs_state';

   +-----------------+-------------+
   | Variable_name   | Value       |
   +-----------------+-------------+
   | wsrep_evs_state | OPERATIONAL |
   +-----------------+-------------+


.. _`wsrep_flow_control_paused`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_flow_control_paused``

.. index::
   pair: Status Variables; wsrep_flow_control_paused

The fraction of time since the last ``FLUSH STATUS`` command that replication was paused due to flow control.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.174353``"
   "Location", "Galera"
   "Initial Version", ""

Basically, this is how much the slave lag is slowing down the cluster.

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_paused';

   +---------------------------+----------+
   | Variable_name             | Value    |
   +---------------------------+----------+
   | wsrep_flow_control_paused | 0.184353 |
   +---------------------------+----------+


.. _`wsrep_flow_control_paused_ns`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_flow_control_paused_ns``

.. index::
   pair: Status Variables; wsrep_flow_control_paused_ns

The total time spent in a paused state measured in nanoseconds.

.. csv-table::
   :class: doc-options

   "Example Value", "``20222491180``"
   "Location", "Galera"
   "Initial Version", ""

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_paused_ns';

   +------------------------------+-------------+
   | Variable_name                | Value       |
   +------------------------------+-------------+
   | wsrep_flow_control_paused_ns | 20222491180 |
   +------------------------------+-------------+


.. _`wsrep_flow_control_recv`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_flow_control_recv``

.. index::
   pair: Status Variables; wsrep_flow_control_recv

Returns the number of ``FC_PAUSE`` events the node has received, including those the node has sent.  Unlike most status variables, the counter for this one does not reset every time you run the query.

.. csv-table::
   :class: doc-options

   "Example Value", "``11``"
   "Location", "Galera"
   "Initial Version", ""

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_recv';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_flow_control_recv | 11    |
   +-------------------------+-------+


.. _`wsrep_flow_control_sent`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_flow_control_sent``

.. index::
   pair: Status Variables; wsrep_flow_control_sent

Returns the number of ``FC_PAUSE`` events the node has sent.  Unlike most status variables, the counter for this one does not reset every time you run the query.

.. csv-table::
   :class: doc-options

   "Example Value", "``7``"
   "Location", "Galera"
   "Initial Version", ""

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_flow_control_sent';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_flow_control_sent | 7     |
   +-------------------------+-------+


.. _`wsrep_gcomm_uuid`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_gcomm_uuid``

.. index::
   pair: Status Variables; wsrep_gcomm_uuid

Displays the group communications UUID.

.. csv-table::
   :class: doc-options

   "Example Value", "``7e729708-605f-11e5-8ddd-8319a704b8c4``"
   "Location", "Galera"
   "Initial Version", "1.0"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_gcomm_uuid';

   +------------------+--------------------------------------+
   | Variable_name    | Value                                |
   +------------------+--------------------------------------+
   | wsrep_gcomm_uuid | 7e729708-605f-11e5-8ddd-8319a704b8c4 |
   +------------------+--------------------------------------+


.. _`wsrep_incoming_addresses`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_incoming_addresses``

.. index::
   pair: Status Variables; wsrep_incoming_addresses

Comma-separated list of incoming server addresses in the cluster component.

.. csv-table::
   :class: doc-options

   "Example Value", "``10.0.0.1:3306,10.0.0.2:3306,undefined``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_incoming_addresses';

   +--------------------------+--------------------------------------+
   | Variable_name            | Value                                |
   +--------------------------+--------------------------------------+
   | wsrep_incoming_addresses | 10.0.0.1:3306,10.0.02:3306,undefined |
   +--------------------------+--------------------------------------+


.. _`wsrep_last_committed`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_last_committed``

.. index::
   pair: Status Variables; wsrep_last_committed

The sequence number, or seqno, of the last committed transaction. See :ref:`wsrep API <wsrep-api>`.

.. csv-table::
   :class: doc-options

   "Example Value", "``409745``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

For more information, see :ref:`wsrep API <wsrep-api>`.


.. _`wsrep_local_bf_aborts`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_bf_aborts``

.. index::
   pair: Status Variables; wsrep_local_bf_aborts

Total number of local transactions that were aborted by slave transactions while in execution.

.. csv-table::
   :class: doc-options

   "Example Value", "``960``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_bf_aborts';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_local_bf_aborts | 960   |
   +-----------------------+-------+


.. _`wsrep_local_cached_downto`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_cached_downto``

.. index::
   pair: Status Variables; wsrep_local_cached_downto

The lowest sequence number, or seqno, in the write-set cache (GCache).

.. csv-table::
   :class: doc-options

   "Example Value", "``18446744073709551615``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_cached_downto';

   +---------------------------+----------------------+
   | Variable_name             | Value                |
   +---------------------------+----------------------+
   | wsrep_local_cached_downto | 18446744073709551615 |
   +---------------------------+----------------------+


.. _`wsrep_local_cert_failures`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_cert_failures``

.. index::
   pair: Status Variables; wsrep_local_cert_failures

Total number of local transactions that failed certification test.

.. csv-table::
   :class: doc-options

   "Example Value", "``333``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_cert_failures';

   +---------------------------+-------+
   | Variable_name             | Value |
   +---------------------------+-------+
   | wsrep_local_cert_failures | 333   |
   +---------------------------+-------+


.. _`wsrep_local_commits`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_commits``

.. index::
   pair: Status Variables; wsrep_local_commits

Total number of local transactions committed.

.. csv-table::
   :class: doc-options

   "Example Value", "``14981``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_commits';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_local_commits | 14981 |
   +---------------------+-------+


.. _`wsrep_local_index`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_index``

.. index::
   pair: Status Variables; wsrep_local_index

This node index in the cluster (base 0).

.. csv-table::
   :class: doc-options

   "Example Value", "``1``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_index';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_local_index | 1     |
   +-------------------+-------+


.. _`wsrep_local_recv_queue`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_recv_queue``

.. index::
   pair: Status Variables; wsrep_local_recv_queue

Current (instantaneous) length of the recv queue.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_local_recv_queue | 0     |
   +------------------------+-------+


.. _`wsrep_local_recv_queue_avg`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_recv_queue_avg``

.. index::
   pair: Status Variables; wsrep_local_recv_queue_avg

Recv queue length averaged over interval since the last ``FLUSH STATUS`` command. Values considerably larger than ``0.0`` mean that the node cannot apply write-sets as fast as they are received and will generate a lot of replication throttling.

.. csv-table::
   :class: doc-options

   "Example Value", "``3.348452``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_recv_queue_avg | 3.348452 |
   +----------------------------+----------+


.. _`wsrep_local_recv_queue_max`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_recv_queue_max``

.. index::
   pair: Status Variables; wsrep_local_recv_queue_max

The maximum length of the recv queue since the last FLUSH STATUS command.

.. csv-table::
   :class: doc-options

   "Example Value", "``10``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_max';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_recv_queue_max | 10    |
   +----------------------------+-------+


.. _`wsrep_local_recv_queue_min`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_recv_queue_min``

.. index::
   pair: Status Variables; wsrep_local_recv_queue_min

The minimum length of the recv queue since the last ``FLUSH STATUS`` command.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_recv_queue_min';

   +-----------------------------+-------+
   | Variable_name               | Value |
   +-----------------------------+-------+
   | wsrep_local_recev_queue_min | 0     |
   +-----------------------------+-------+


.. _`wsrep_local_replays`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_replays``

.. index::
   pair: Status Variables; wsrep_local_replays

Total number of transaction replays due to *asymmetric lock granularity*.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_replays';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_lcoal_replays | 0     |
   +---------------------+-------+


.. _`wsrep_local_send_queue`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_send_queue``

.. index::
   pair: Status Variables; wsrep_local_send_queue

Current (instantaneous) length of the send queue.

.. csv-table::
   :class: doc-options

   "Example Value", "``1``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_local_send_queue | 1     |
   +------------------------+-------+


.. _`wsrep_local_send_queue_avg`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_send_queue_avg``

.. index::
   pair: Status Variables; wsrep_local_send_queue_avg

Send queue length averaged over time since the last ``FLUSH STATUS`` command. Values considerably larger than 0.0 indicate replication throttling or network throughput issue.

.. csv-table::
   :class: doc-options

   "Example Value", "``0.145000``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_avg';

   +----------------------------+----------+
   | Variable_name              | Value    |
   +----------------------------+----------+
   | wsrep_local_send_queue_avg | 0.145000 |
   +----------------------------+----------+


.. _`wsrep_local_send_queue_max`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_send_queue_max``

.. index::
   pair: Status Variables; wsrep_local_send_queue_max

The maximum length of the send queue since the last ``FLUSH STATUS`` command.

.. csv-table::
   :class: doc-options

   "Example Value", "``10``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_max';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_send_queue_max | 10    |
   +----------------------------+-------+


.. _`wsrep_local_send_queue_min`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_send_queue_min``

.. index::
   pair: Status Variables; wsrep_local_send_queue_min

The minimum length of the send queue since the last ``FLUSH STATUS`` command.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_send_queue_min';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_local_send_queue_min | 0     |
   +----------------------------+-------+


.. _`wsrep_local_state`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_state``

.. index::
   pair: Status Variables; wsrep_local_state

Internal Galera Cluster FSM state number.

.. csv-table::
   :class: doc-options

   "Example Value", "``4``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_local_state | 4     |
   +-------------------+-------+

For more information on the possible node states, see :ref:`Node State Changes <node-state-changes>`.


.. _`wsrep_local_state_comment`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_state_comment``

.. index::
   pair: Status Variables; wsrep_local_state_comment

Human-readable explanation of the state.

.. csv-table::
   :class: doc-options

   "Example Value", "``Synced``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_local_state_comment | Synced |
   +---------------------------+--------+


.. _`wsrep_local_state_uuid`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_local_state_uuid``

.. index::
   pair: Status Variables; wsrep_local_state_uuid

The UUID of the state stored on this node.

.. csv-table::
   :class: doc-options

   "Example Value", "``e2c9a15e-5385-11e0-0800-6bbb637e7211``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_uuid';

   +------------------------+--------------------------------------+
   | Variable_name          | Value                                |
   +------------------------+--------------------------------------+
   | wsrep_local_state_uuid | e2c9a15e-5485-11e0-0800-6bbb637e7211 |
   +------------------------+--------------------------------------+

For more information on the state UUID, see :ref:`wsrep API <wsrep-api>`.


.. _`wsrep_open_connections`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_open_connections``

.. index::
   pair: Status Variables; wsrep_open_connections

The number of open connection objects inside the wsrep provider.

.. csv-table::
   :class: doc-options

   "Example Value", "``1``"
   "Location", "Galera"
   "Initial Version", "3.24"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_open_connections';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_open_connections | 1     |
   +------------------------+-------+


.. _`wsrep_open_transactions`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_open_transactions``

.. index::
   pair: Status Variables; wsrep_open_transactions

The number of locally running transactions which have been registered inside the wsrep provider. This means transactions which have made operations which have caused write set population to happen. Transactions which are read only are not counted.

.. csv-table::
   :class: doc-options

   "Example Value", "``6``"
   "Location", "Galera"
   "Initial Version", "3.24"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_open_transactions';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_open_transactions | 6     |
   +-------------------------+-------+


.. _`wsrep_protocol_version`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_protocol_version``

.. index::
   pair: Status Variables; wsrep_protocol_version

The version of the wsrep Protocol used.

.. csv-table::
   :class: doc-options

   "Example Value", "``4``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_protocol_version';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_protocol_version | 4     |
   +------------------------+-------+


.. _`wsrep_provider_name`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_provider_name``

.. index::
   pair: Status Variables; wsrep_provider_name

The name of the wsrep Provider.

.. csv-table::
   :class: doc-options

   "Example Value", "``Galera``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_name';

   +---------------------+--------+
   | Variable_name       | Value  |
   +---------------------+--------+
   | wsrep_provider_name | Galera |
   +---------------------+--------+


.. _`wsrep_provider_vendor`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_provider_vendor``

.. index::
   pair: Status Variables; wsrep_provider_vendor

The name of the wsrep Provider vendor.

.. csv-table::
   :class: doc-options

   "Example Value", "``Codership Oy <info@codership.com>``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_vendor';

   +-----------------------+-----------------------------------+
   | Variable_name         | Value                             |
   +-----------------------+-----------------------------------+
   | wsrep_provider_vendor | Codership Oy <info@codership.com> |
   +-----------------------+-----------------------------------+


.. _`wsrep_provider_version`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_provider_version``

.. index::
   pair: Status Variables; wsrep_provider_version

The name of the wsrep Provider version string.

.. csv-table::
   :class: doc-options

   "Example Value", "``25.3.5-wheezy(rXXXX)``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_provider_version';

   +------------------------+----------------------+
   | Variable_name          | Value                |
   +------------------------+----------------------+
   | wsrep_provider_version | 25.3.5-wheezy(rXXXX) |
   +------------------------+----------------------+


.. _`wsrep_ready`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_ready``

.. index::
   pair: Status Variables; wsrep_ready

Whether the server is ready to accept queries. If this status is ``OFF``, almost all of the queries will fail with:

.. csv-table::
   :class: doc-options

   "Example Value", "``ON``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

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


.. _`wsrep_received`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_received``

.. index::
   pair: Status Variables; wsrep_received

Total number of write-sets received from other nodes.

.. csv-table::
   :class: doc-options

   "Example Value", "``17831``"
   "Location", "MySQL"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_received';

   +----------------+-------+
   | Variable_name  | Value |
   +----------------+-------+
   | wsrep_received | 17831 |
   +----------------+-------+


.. _`wsrep_received_bytes`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_received_bytes``

.. index::
   pair: Status Variables; wsrep_received_bytes

Total size of write-sets received from other nodes.

.. csv-table::
   :class: doc-options

   "Example Value", "``6637093``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_received_bytes';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_received_bytes | 6637093 |
   +----------------------+---------+


.. _`wsrep_repl_data_bytes`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_repl_data_bytes``

.. index::
   pair: Status Variables; wsrep_repl_data_bytes

Total size of data replicated.

.. csv-table::
   :class: doc-options

   "Example Value", "``6526788``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_data_bytes';

   +-----------------------+---------+
   | Variable_name         | Value   |
   +-----------------------+---------+
   | wsrep_repl_data_bytes | 6526788 |
   +-----------------------+---------+


.. _`wsrep_repl_keys`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_repl_keys``

.. index::
   pair: Status Variables; wsrep_repl_keys

Total number of keys replicated.

.. csv-table::
   :class: doc-options

   "Example Value", "``797399``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-blocK:: mysql

   SHOW STATUS LIKE 'wsrep_repl_keys';

   +-----------------+--------+
   | Variable_name   | Value  |
   +-----------------+--------+
   | wsrep_repl_keys | 797399 |
   +-----------------+--------+


.. _`wsrep_repl_keys_bytes`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_repl_keys_bytes``

.. index::
   pair: Status Variables; wsrep_repl_keys_bytes

Total size of keys replicated.

.. csv-table::
   :class: doc-options

   "Example Value", "``11203721``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_keys_bytes';

   +-----------------------+----------+
   | Variable_name         | Value    |
   +-----------------------+----------+
   | wsrep_repl_keys_bytes | 11203721 |
   +-----------------------+----------+


.. _`wsrep_repl_other_bytes`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_repl_other_bytes``

.. index::
   pair: Status Variables; wsrep_repl_other_bytes

Total size of other bits replicated.

.. csv-table::
   :class: doc-options

   "Example Value", "``0``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_repl_other_bytes';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_repl_other_bytes | 0     |
   +------------------------+-------+


.. _`wsrep_replicated`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_replicated``

.. index::
   pair: Status Variables; wsrep_replicated

Total number of write-sets replicated (sent to other nodes).

.. csv-table::
   :class: doc-options

   "Example Value", "``16109``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_replicated';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_replicated | 16109 |
   +------------------+-------+


.. _`wsrep_replicated_bytes`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_replicated_bytes``

.. index::
   pair: Status Variables; wsrep_replicated_bytes

Total size of write-sets replicated.

.. csv-table::
   :class: doc-options

   "Example Value", "``6526788``"
   "Location", "Galera"
   "Initial Version", "???"

To see retrieve the value of this status variable, execute the ``SHOW STATUS`` statement like so:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_replicated_bytes';

   +------------------------+---------+
   | Variable_name          | Value   |
   +------------------------+---------+
   | wsrep_replicated_bytes | 6526788 |
   +------------------------+---------+


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

   <br />
