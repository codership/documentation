.. meta::
   :title: Galera Cluster Parameters
   :description:
   :language: en-US
   :keywords: galera cluster, galera parameters, options
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :doc:`auto-eviction`
      - :doc:`ssl-cert`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`galera-parameters`:

==================
Galera Parameters
==================

As of version 0.8, Galera Cluster accepts parameters as semicolon-separated key value pair lists, such as ``key1 = value1; key2 = value2``. In this way, you can configure an arbitrary number of Galera Cluster parameters in one call. A key consists of parameter group and parameter name: ``<group>.<name>``, where ``<group>`` corresponds roughly to some Galera module.

All ``wsrep_provider_options`` settings need to be specified on a single line. In case of multiple instances of ``wsrep_provider_options``, only the last one is used.

.. only:: html

          .. image:: ../images/support.jpg
             :target: https://galeracluster.com/support/#galera-cluster-support-subscription
             :width: 740

   .. only:: latex

          .. image:: ../images/support.jpg
		  :target: https://galeracluster.com/support/#galera-cluster-support-subscription


Below is a list of all of the Galera parameters. Each is also a link to further down the page where you may find more information. There are a few things to know about this table:

- For numeric values related to memory size, Galera Cluster accepts the numeric modifiers, ``K``, ``M``, ``G``, and ``T`` to represent |210|, |220|, |230| and |240|, respectively.

- Galera Cluster accepts the following boolean values: ``0``, ``1``, ``YES``, ``NO``, ``TRUE``, ``FALSE``, ``ON``, ``OFF``.

- Time periods must be expressed in the ISO8601 format. See some of the examples below.

- The parameters that are noted as for debugging only are strictly for use in troubleshooting problems. You should not implement these in production environments.

.. |210| replace:: 2\ :sup:`10`\
.. |220| replace:: 2\ :sup:`20`\
.. |230| replace:: 2\ :sup:`30`\
.. |240| replace:: 2\ :sup:`40`\

.. csv-table::
   :class: doc-options
   :header: "|br| Parameter", "|br| Default", "|br| Dynamic", "Debug |br| Only", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 30, 12, 12, 12, 14

   ":ref:`base_dir <base_dir>`", "", "", "", "", ""
   ":ref:`base_host <base_host>`", "detected network address", "", "", "1.0", ""
   ":ref:`base_port <base_port>`", "``4567``", "", "", "1.0", ""
   ":ref:`cert.log_conflicts <cert.log_conflicts>`", "``NO``", "  Yes", "", "2.0", ""
   ":ref:`cert.optimistic_pa <cert.optimistic_pa>`", "``YES``", "  Yes", "", "3.25", ""
   ":ref:`debug <debug>`", "``NO``", "  Yes", "", "2.0", ""
   ":ref:`datadir <datadir>`", "``/var/lib/mysql/``", "  Yes", "", "1.0", ""
   ":ref:`evs.auto_evict <evs.auto_evict>`", "``0``", "   No", "", "3.8", ""
   ":ref:`evs.causal_keepalive_period <evs.causal_keepalive_period>`", "``0``", "   No", "", "1.0", ""
   ":ref:`evs.consensus_timeout <evs.consensus_timeout>`", "``PT30S``", "   No", "Yes", "1.0, 2.0", ""
   ":ref:`evs.debug_log_mask <evs.debug_log_mask>`", "``0x1``", "  Yes", "", "1.0", ""
   ":ref:`evs.delayed_keep_period <evs.delayed_keep_period>`", "``PT30S``", "   No", "", "3.8", ""
   ":ref:`evs.delay_margin <evs.delay_margin>`", "``PT1S``", "   No", "", "3.8", ""
   ":ref:`evs.evict <evs.evict>`", "", "   No", "", "3.8", ""
   ":ref:`evs.inactive_check_period <evs.inactive_check_period>`", "``PT1S``", "   No", "", "1.0", ""
   ":ref:`evs.inactive_timeout <evs.inactive_timeout>`", "``PT15S``", "   No", "", "1.0", ""
   ":ref:`evs.info_log_mask <evs.info_log_mask>`", "``0``", "   No", "", "1.0", ""
   ":ref:`evs.install_timeout <evs.install_timeout>`", "``PT7.5S``", "  Yes", "", "1.0", ""
   ":ref:`evs.join_retrans_period <evs.join_retrans_period>`", "``PT1S``", "  Yes", "", "1.0", ""
   ":ref:`evs.keepalive_period <evs.keepalive_period>`", "``PT1S``", "  No", "", "1.0", ""
   ":ref:`evs.max_install_timeouts <evs.max_install_timeouts>`", "``1``", "  No", "", "1.0", ""
   ":ref:`evs.send_window <evs.send_window>`", "``4``", "  Yes", "", "1.0", ""
   ":ref:`evs.stats_report_period <evs.stats_report_period>`", "``PT1M``", "  No", "", "1.0", ""
   ":ref:`evs.suspect_timeout <evs.suspect_timeout>`", "``PT5S``", "  No", "", "1.0", ""
   ":ref:`evs.use_aggregate <evs.use_aggregate>`", "``TRUE``", "  No", "", "1.0", ""
   ":ref:`evs.user_send_window <evs.user_send_window>`", "``2``", "  Yes", "", "1.0", ""
   ":ref:`evs.view_forget_timeout <evs.view_forget_timeout>`", "``PT5M``", "  No", "", "1.0", ""
   ":ref:`evs.version <evs.version>`", "``0``", "  No", "Yes", "1.0", ""
   ":ref:`gcache.dir <gcache.dir>`", "working directory", "  No", "", "1.0", ""
   ":ref:`gcache.name <gcache.name>`", "``galera.cache``", "  No", "", "1.0", ""
   ":ref:`gcache.keep_pages_size <gcache.keep_pages_size>`", "``0``", "  No", "", "1.0", ""
   ":ref:`gcache.mem_size <gcache.mem_size>`", "``0``", "  No", "", "", ""
   ":ref:`gcache.page_size <gcache.page_size>`", "``128M``", "  No", "", "1.0", ""
   ":ref:`gcache.recover <gcache.recover>`", "``yes``", "  No", "", "3.19", ""
   ":ref:`gcache.size <gcache.size>`", "``128M``", "  No", "", "1.0", ""
   ":ref:`gcomm.thread_prio <gcomm.thread_prio>`", "", "  No", "", "3.0", ""
   ":ref:`gcs.fc_debug <gcs.fc_debug>`", "``0``", "  No", "", "1.0", ""
   ":ref:`gcs.fc_factor <gcs.fc_factor>`", "``1.0``", "  No", "", "1.0", ""
   ":ref:`gcs.fc_limit <gcs.fc_limit>`", "``16``", "  Yes", "", "1.0", ""
   ":ref:`gcs.fc_master_slave <gcs.fc_master_slave>`", "``NO``", "  No", "", "1.0", "4.10"
   ":ref:`gcs.fc_single_primary <gcs.fc_single_primary>`", "``NO``", "  No", "", "4.10", ""
   ":ref:`gcs.max_packet_size <gcs.max_packet_size>`", "``64500``", "  No", "", "1.0", ""
   ":ref:`gcs.max_throttle <gcs.max_throttle>`", "``0.25``", "  No", "", "1.0", ""
   ":ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>`", "``LLONG_MAX``", "  No", "", "1.0", ""
   ":ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>`", "``0.25``", "  No", "", "1.0", ""
   ":ref:`gcs.sync_donor <gcs.sync_donor>`", "``NO``", "  No", "", "1.0", ""
   ":ref:`gcs.vote_policy <gcs.vote_policy>`", "``0``", "  No", "", "1.0", ""
   ":ref:`gmcast.isolate <gmcast.isolate>`", "``0``", "  Yes", "Yes", "", ""
   ":ref:`gmcast.listen_addr <gmcast.listen_addr>`", "``tcp://0.0.0.0:4567``", "  No", "", "1.0", ""
   ":ref:`gmcast.mcast_addr <gmcast.mcast_addr>`", "", "  No", "", "1.0", ""
   ":ref:`gmcast.mcast_ttl <gmcast.mcast_ttl>`", "``1``", "  No", "", "1.0", ""
   ":ref:`gmcast.peer_timeout <gmcast.peer_timeout>`", "``PT3S``", "  No", "", "1.0", ""
   ":ref:`gmcast.segment <gmcast.segment>`", "``0``", "  No", "", "3.0", ""
   ":ref:`gmcast.time_wait <gmcast.time_wait>`", "``PT5S``", "  No", "", "1.0", ""
   ":ref:`gmcast.version <gmcast.version>`", "n/a", "  No", "Yes", "1.0", ""
   ":ref:`innodb_flush_log_at_trx_commit <innodb_flush_log_at_trx_commit>`", "1", "  Yes", "", "", ""
   ":ref:`ist.recv_addr <ist.recv_addr>`", "", "  No", "", "1.0", ""
   ":ref:`ist.recv_bind <ist.recv_bind>`", "", "  No", "", "3.0", ""
   ":ref:`pc.announce_timeout <pc.announce_timeout>`", "``PT3S``", "  No", "", "2.0", ""
   ":ref:`pc.bootstrap <pc.bootstrap>`", "n/a", "  No", "", "2.0", ""
   ":ref:`pc.checksum <pc.checksum>`", "``FALSE``", "  No", "", "1.0", ""
   ":ref:`pc.ignore_sb <pc.ignore_sb>`", "``FALSE``", "  Yes", "", "1.0", ""
   ":ref:`pc.ignore_quorum <pc.ignore_quorum>`", "``FALSE``", "  Yes", "", "1.0", ""
   ":ref:`pc.linger <pc.linger>`", "``PT2S``", "  No", "", "1.0", ""
   ":ref:`pc.npvo <pc.npvo>`", "``FALSE``", "  No", "", "1.0", ""
   ":ref:`pc.recovery <pc.recovery>`", "``TRUE``", "  No", "", "3.0", ""
   ":ref:`pc.version <pc.version>`", "n/a", "  No", "Yes", "1.0", ""
   ":ref:`pc.wait_prim <pc.wait_prim>`", "``TRUE``", "  No", "", "1.0", ""
   ":ref:`pc.wait_prim_timeout <pc.wait_prim_timeout>`", "``PT30S``", "  No", "", "2.0", ""
   ":ref:`pc.weight <pc.weight>`", "``1``", "  Yes", "", "2.4", ""
   ":ref:`protonet.backend <protonet.backend>`", "``asio``", "  No", "", "1.0", "4.14"
   ":ref:`protonet.version <protonet.version>`", "n/a", "  No", "Yes", "1.0", "4.14"
   ":ref:`repl.causal_read_timeout <repl.causal_read_timeout>`", "``PT30S``", "  No", "", "1.0", ""
   ":ref:`repl.commit_order <repl.commit_order>`", "``3``", "  No", "", "1.0", ""
   ":ref:`repl.key_format <repl.key_format>`", "``FLAT8``", "  No", "", "3.0", ""
   ":ref:`repl.max_ws_size <repl.max_ws_size>`", "``2147483647``", "  No", "", "3.0", ""
   ":ref:`repl.proto_max <repl.proto_max>`", "``5``", "  No", "", "2.0", ""
   ":ref:`socket.recv_buf_size <socket.recv_buf_size>`", "``auto``", "  Yes", "", "3.17", ""
   ":ref:`socket.send_buf_size <socket.send_buf_size>`", "``auto``", "  Yes", "", "3.29", ""
   ":ref:`socket.ssl <socket.ssl>`", "0", "  No", "", "", ""
   ":ref:`socket.ssl_ca <socket.ssl_ca>`", "", "  No", "", "1.0", ""
   ":ref:`socket.ssl_cert <socket.ssl_cert>`", "", "  No", "", "1.0", ""
   ":ref:`socket.checksum <socket.checksum>`", "``1`` (vs. 2); ``2`` (vs. 3)", "  No", "", "2.0", ""
   ":ref:`socket.dynamic <socket.dynamic>`", "FALSE", "  No", "", "4.8", ""
   ":ref:`socket.ssl_cipher <socket.ssl_cipher>`", "````", "  No", "", "1.0", ""
   ":ref:`socket.ssl_compression <socket.ssl_compression>`", "``YES``", "  No", "", "1.0", "4.14"
   ":ref:`socket.ssl_key <socket.ssl_key>`", "", "  No", "", "1.0", ""
   ":ref:`socket.ssl_password_file <socket.ssl_password_file>`", "", "  No", "", "1.0", ""
   ":ref:`socket.ssl_reload <socket.ssl_reload>`", "", "  No", "", "4.8", ""

.. _`base_dir`:
.. rst-class:: section-heading
.. rubric:: ``base_dir``

.. index::
   pair: wsrep Provider Options; base_dir

Specifies the data directory.


.. _`base_host`:
.. rst-class:: section-heading
.. rubric:: ``base_host``

.. index::
   pair: wsrep Provider Options; base_host

Global variable for internal use.

.. csv-table::
   :class: doc-options

   "Default Value", "detected network address"
   "Dynamic", ""
   "Initial Version", ""

.. warning:: Since this is for internal use only, do not manually set the ``base_host`` variable.


.. _`base_port`:
.. rst-class:: section-heading
.. rubric:: ``base_port``

.. index::
   pair: wsrep Provider Options; base_port

Global variable for internal use.

.. csv-table::
   :class: doc-options

   "Default Value", "``4567``"
   "Dynamic", ""
   "Initial Version", ""

.. warning:: Since this is for internal use only, do not manually set the ``base_port`` variable.


.. _`cert.log_conflicts`:
.. rst-class:: section-heading
.. rubric:: ``cert.log_conflicts``

.. index::
   pair: wsrep Provider Options; cert.log_conflicts

Log details of certification failures.

.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "Yes"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="cert.log_conflicts=NO"


.. _`cert.optimistic_pa`:
.. rst-class:: section-heading
.. rubric:: ``cert.optimistic_pa``

.. index::
   pair: wsrep Provider Options; cert.optimistic_pa

Controls parallel applying of replica actions. When enabled allows full range
of parallelization as determined by certification algorithm. When disabled
limits parallel applying window to not exceed that seen on primary. In other
words, the action starts applying no sooner than all actions it has seen
on the primary are committed.

.. csv-table::
   :class: doc-options

   "Default Value", "``YES``"
   "Dynamic", "Yes"
   "Initial Version", "3.25"

.. code-block:: ini

   wsrep_provider_options="cert.optimistic_pa=NO"


.. _`datadir`:
.. rst-class:: section-heading
.. rubric:: ``datadir``

.. index::
   pair: wsrep Provider Options; datadir

Set the path to the database root directory.

.. csv-table::
   :class: doc-options

   "Default Value", "``/var/lib/mysql/``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the ``my.cnf`` configuration file:

.. code-block:: ini

   datadir=/var/lib/mysql/


.. _`debug`:
.. rst-class:: section-heading
.. rubric:: ``debug``

.. index::
   pair: wsrep Provider Options; debug

Enable debugging.

.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "Yes"
   "Initial Version", "2.0"

.. code-block:: ini

   wsrep_provider_options="debug=NO"


.. _`evs.auto_evict`:
.. rst-class:: section-heading
.. rubric:: ``evs.auto_evict``

.. index::
   pair: wsrep Provider Options; evs.auto_evict

Defines how many entries the node allows for given a delayed node before it triggers the Auto Eviction protocol.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors the group communication response times from all other nodes. When the cluster registers delayed response from a given node, it adds an entry for that node to its delayed list. If the majority of the cluster nodes show the node as delayed, the node is permanently evicted from the cluster.

This parameter determines how many entries a given node can receive before it triggers Auto Eviction.

When this parameter is set to ``0``, it disables the Auto Eviction protocol for this node. Even when you disable Auto Eviction, though; the node continues to monitor response times from the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.auto_evict=5"

For more information on the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.causal_keepalive_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.causal_keepalive_period``

.. index::
   pair: wsrep Provider Options; evs.causal_keepalive_period

For developer use only. Defaults to ``evs.keepalive_period``.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"


.. _`evs.consensus_timeout`:
.. rst-class:: section-heading
.. rubric:: ``evs.consensus_timeout``

.. index::
   pair: wsrep Provider Options; evs.consensus_timeout

Timeout on reaching the consensus about cluster membership.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "1.0"
   "Deprecated", "2.0"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.consensus_timeout=PT30S"

.. note:: This feature has been **deprecated**. It is succeeded by :ref:`evs.install_timeout <evs.install_timeout>`.


.. _`evs.debug_log_mask`:
.. rst-class:: section-heading
.. rubric:: ``evs.debug_log_mask``

.. index::
   pair: wsrep Provider Options; evs.debug_log_mask

Control EVS debug logging, only effective when ``wsrep_debug`` is in use.

.. csv-table::
   :class: doc-options

   "Default Value", "``0x1``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.debug_log_mask=0x1"


.. _`evs.delayed_keep_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.delayed_keep_period``

.. index::
   pair: wsrep Provider Options; evs.delayed_keep_period

Defines how long this node requires a delayed node to remain responsive before it removes an entry from the delayed list.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors the group communication response times from all other nodes. When the cluster registered delayed responses from a given node, it adds an entry for that node to its delayed list. Nodes that remain on the delayed list can trigger Auto Eviction, which removes them permanently from the cluster.

This parameter determines how long a node on the delayed list must remain responsive before it removes one entry. The number of entries on the delayed list and how long it takes before the node removes all entries depends on how long the delayed node was unresponsive.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.delayed_keep_period=PT45S"

For more information on the delayed list and the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.delay_margin`:
.. rst-class:: section-heading
.. rubric:: ``evs.delay_margin``

.. index::
   pair: wsrep Provider Options; evs.delay_margin

Defines how long the node allows response times to deviate before adding an entry to the delayed list.

.. csv-table::
   :class: doc-options

   "Default Value", "PT1S"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors group communication response times from all other nodes. When the cluster registers a delayed response from a given node, it adds an entry for that node to its delayed list. Delayed nodes can trigger Auto Eviction, which removes them permanently from the cluster.

This parameter determines how long a delay can run before the node adds an entry to the delayed list. You must set this parameter to a value higher than the round-trip delay time (RTT) between the nodes.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.delay_margin=PT5S"

For more information on the delayed list and the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.evict`:
.. rst-class:: section-heading
.. rubric:: ``evs.evict``

.. index::
   pair: wsrep Provider Options; evs.evict

If set to the gcomm UUID of some node, that node will be evicted from the cluster. Setting this parameter to an empty string causes the eviction list to be cleared on the node where it is set.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.8"

For more information on the eviction and Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.inactive_check_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.inactive_check_period``

.. index::
   pair: wsrep Provider Options; evs.inactive_check_period

Defines how often you want the node to check for peer inactivity.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes. When the cluster registers a delayed response from a given node, it adds an entry for that node to its delayed list, which can lead to the delayed node's eviction from the cluster.

This parameter determines how often you want the node to check for delays in the group communication responses from other cluster nodes.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.inactive_check_period=PT1S"


.. _`evs.inactive_timeout`:
.. rst-class:: section-heading
.. rubric:: ``evs.inactive_timeout``

.. index::
   pair: wsrep Provider Options; evs.inactive_timeout

Defines a hard limit on node inactivity.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT15S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Hard limit on the inactivity period, after which the node is pronounced dead.

Each cluster node monitors group communication response times from all other nodes. When the cluster registers a delayed response from a given node, it add an entry for that node to its delayed list, which can lead to the delayed node's eviction from the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.inactive_timeout=PT15S"

This parameter sets a hard limit for node inactivity. If a delayed node remains unresponsive for longer than this period, the node pronounces the delayed node as dead.


.. _`evs.info_log_mask`:
.. rst-class:: section-heading
.. rubric:: ``evs.info_log_mask``

.. index::
   pair: wsrep Provider Options; evs.info_log_mask

Defines additional logging options for the EVS Protocol.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The EVS Protocol monitors group communication response times and controls the node eviction and auto eviction processes. This parameter allows you to enable additional logging options, through a bitmask value.

- ``0x1`` Provides extra view change info.
- ``0x2`` Provides extra state change info
- ``0x4`` Provides statistics
- ``0x8`` Provides profiling (only in builds with profiling enabled)

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.info_log_mask=0x4"


.. _`evs.install_timeout`:
.. rst-class:: section-heading
.. rubric:: ``evs.install_timeout``

.. index::
   pair: wsrep Provider Options; evs.install_timeout

Defines the timeout for install message acknowledgments.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT7.5S``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes, checking whether they are responsive or delayed. This parameter determines how long you want the node to wait on install message acknowledgments.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.install_timeout=PT7.5S"

.. note:: This parameter replaces :ref:`evs.consensus_timeout <evs.consensus_timeout>`.


.. _`evs.join_retrans_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.join_retrans_period``

.. index::
   pair: wsrep Provider Options; evs.join_retrans_period

Defines how often the node retransmits EVS join messages when forming cluster membership.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1S``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.join_retrans_period=PT1S"


.. _`evs.keepalive_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.keepalive_period``

.. index::
   pair: wsrep Provider Options; evs.keepalive_period

Defines how often the node emits keepalive signals.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes. When there is no traffic going out for the cluster to monitor, nodes emit keepalive signals so that other nodes have something to measure. This parameter determines how often the node emits a keepalive signal, absent any other traffic.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.keepalive_period=PT1S"


.. _`evs.max_install_timeouts`:
.. rst-class:: section-heading
.. rubric:: ``evs.max_install_timeouts``

.. index::
   pair: wsrep Provider Options; evs.max_install_timeouts

Defines the number of membership install rounds to try before giving up.

.. csv-table::
   :class: doc-options

   "Default Value", "``1``"
   "Dynamic", "No"
   "Initial Version", "1.0"

This parameter determines the maximum number of times that the node tries for a membership install acknowledgment, before it stops trying. The total number of rounds it tries is this value plus 2.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.max_install_timeouts=1"


.. _`evs.send_window`:
.. rst-class:: section-heading
.. rubric:: ``evs.send_window``

.. index::
   pair: wsrep Provider Options; evs.send_window

Defines the maximum number of packets at a time in replication.

.. csv-table::
   :class: doc-options

   "Default Value", "``4``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

This parameter determines the maximum number of packets the node uses at a time in replication. For clusters implemented over :abbr:`WAN (Wide Area Network)`, you can set this value considerably higher, (for example, 512), than for clusters implemented over :abbr:`LAN (Local Area Network)`.

You must use a value that is greater than :ref:`evs.user_send_window <evs.user_send_window>`. The recommended value is double :ref:`evs.user_send_window <evs.user_send_window>`.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.send_window=4"


.. _`evs.stats_report_period`:
.. rst-class:: section-heading
.. rubric:: ``evs.stats_report_period``

.. index::
   pair: wsrep Provider Options; evs.stats_report_period

Control period of EVS statistics reporting. The node is pronounced dead.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.stats_report_period=PT1M"


.. _`evs.suspect_timeout`:
.. rst-class:: section-heading
.. rubric:: ``evs.suspect_timeout``

.. index::
   pair: wsrep Provider Options; evs.suspect_timeout

Defines the inactivity period after which a node is *suspected* as dead.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each node in the cluster monitors group communications from all other nodes in the cluster. This parameter determines the period of inactivity before the node suspects another of being dead. If all nodes agree on that, the cluster drops the inactive node.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.suspect_timeout=PT5S"


.. _`evs.use_aggregate`:
.. rst-class:: section-heading
.. rubric:: ``evs.use_aggregate``

.. index::
   pair: wsrep Provider Options; evs.use_aggregate

Defines whether the node aggregates small packets into one when possible.

.. csv-table::
   :class: doc-options

   "Default Value", "``TRUE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.use_aggregate=TRUE"


.. _`evs.user_send_window`:
.. rst-class:: section-heading
.. rubric:: ``evs.user_send_window``

.. index::
   pair: Parameters; evs.user_send_window

Defines the maximum number of data packets at a time in replication.

.. csv-table::
   :class: doc-options

   "Default Value", "``2``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

This parameter determines the maximum number of data packets the node uses at a time in replication. For clusters implemented over :abbr:`WAN (Wide Area Network)`, you can set this to a value considerably higher than cluster implementations over :abbr:`LAN (Local Area Network)`, (for example, 512).

You must use a value that is smaller than :ref:`evs.send_window<evs.send_window>`. The recommended value is half :ref:`evs.send_window<evs.send_window>`.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.user_send_window=2"

For more information, see :ref:`evs.send_window <evs.send_window>`.


.. _`evs.view_forget_timeout`:
.. rst-class:: section-heading
.. rubric:: ``evs.view_forget_timeout``

.. index::
   pair: wsrep Provider Options; evs.view_forget_timeout

Defines how long the node saves past views from the view history.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each node maintains a history of past views. This parameter determines how long you want the node to save past views before dropping them from the table.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.view_forget_timeout=PT5M"


.. _`evs.version`:
.. rst-class:: section-heading
.. rubric:: ``evs.version``

.. index::
   pair: wsrep Provider Options; evs.version

Defines the EVS Protocol version.

.. csv-table::
   :class: doc-options

   "Default Value", "``0`` (up to Galera Cluster version 3.9) | ``1`` (as of Galera Cluster version 4.0)"
   "Dynamic", "No"
   "Initial Version", "1.0"

This parameter determines which version of the EVS Protocol the node uses. In order to ensure backwards compatibility, the parameter defaults to ``0`` on Galera Cluster versions prior to 3.9. Certain EVS Protocol features, such as Auto Eviction, require you to upgrade to more recent versions. As of Galera Cluster version 4.0, the parameter defaults to ``1``.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.version=1"

For more information on the procedure to upgrade from one version to another, see :ref:`Upgrading the EVS Protocol <upgrade-evs>`.


.. _`gcache.dir`:
.. rst-class:: section-heading
.. rubric:: ``gcache.dir``

.. index::
   pair: wsrep Provider Options; gcache.dir

Defines the directory where the write-set cache places its files.

.. csv-table::
   :class: doc-options

   "Default Value", "``/path/to/working_dir``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state. Under certain methods, the node that sends the state transfer is similarly blocked. To prevent the database from falling further behind, GCache saves the incoming write-sets on memory mapped files to disk.

This parameter determines where you want the node to save these files for write-set caching. By default, GCache uses the working directory for the database server.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.dir=/usr/share/galera"


.. _`gcache.keep_pages_size`:
.. rst-class:: section-heading
.. rubric:: ``gcache.keep_pages_size``

.. index::
   pair: wsrep Provider Options; gcache.keep_pages_size

Total size of the page storage pages to keep for caching purposes. If only page storage is enabled, one page is always present.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.keep_pages_size=0"


.. _`gcache.mem_size`:
.. rst-class:: section-heading
.. rubric:: ``gcache.mem_size``

.. index::
   pair: wsrep Provider Options; gcache.mem_size

The maximum size of size of the ``malloc()`` store for setups that have spare RAM.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"


.. _`gcache.name`:
.. rst-class:: section-heading
.. rubric:: ``gcache.name``

.. index::
   pair: wsrep Provider Options; gcache.name

Defines the filename for the write-set cache.

.. csv-table::
   :class: doc-options

   "Default Value", "``galera.cache``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state. Under certain methods, the node that sends the state transfer is similarly blocked. To prevent the database from falling further behind, GCache saves the incoming write-sets on memory-mapped files to disk.

This parameter determines the name you want the node to use for this ring buffer storage file.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.name=galera.cache"


.. _`gcache.page_size`:
.. rst-class:: section-heading
.. rubric:: ``gcache.page_size``

.. index::
   pair: wsrep Provider Options; gcache.page_size

Size of the page files in page storage. The limit on overall page storage is the size of the disk. Pages are prefixed by ``gcache.page``.

.. csv-table::
   :class: doc-options

   "Default Value", "``128M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.page_size=128M"


.. _`gcache.recover`:
.. rst-class:: section-heading
.. rubric:: ``gcache.recover``

.. index::
   pair: wsrep Provider Options; gcache.recover

Determines whether gcache recovery takes place on node startup. If gcache could be recovered successfully, the node can then provide IST to other joining nodes, which is useful when the whole cluster is being restarted.

.. csv-table::
   :class: doc-options

   "Default Value", "``no``"
   "Dynamic", "No"
   "Initial Version", "3.19"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.recover=yes"


.. _`gcache.size`:
.. rst-class:: section-heading
.. rubric:: ``gcache.size``

.. index::
   pair: wsrep Provider Options; gcache.size

Defines the disk space you want to node to use in caching write-sets.

.. csv-table::
   :class: doc-options

   "Default Value", "``128M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state. Under certain methods, the node that sends the state transfer is similarly blocked. To prevent the database from falling further behind, GCache saves the incoming write-sets on memory-mapped files to disk.

This parameter defines the amount of disk space you want to allocate for the present ring buffer storage. The node allocates this space when it starts the database server.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.size=128M"

For more information on customizing the write-set cache, see the :doc:`Best Practice Articles <../kb/index>`.


.. _`gcomm.thread_prio`:
.. rst-class:: section-heading
.. rubric:: ``gcomm.thread_prio``

.. index::
   pair: wsrep Provider Options; gcomm.thread_prio

Defines the policy and priority for the gcomm thread.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.0"

Using this option, you can raise the priority of the gcomm thread to a higher level than it normally uses. You may find this useful in situations where Galera Cluster threads do not receive sufficient CPU time, due to competition with other MySQL threads. In these cases, when the thread scheduler for the operating system does not run the Galera threads frequently enough, timeouts may occur, causing the node to drop from the cluster.

The format for this option is: ``<policy>:<priority>``. The priority value is an integer. The policy value supports the following options:

- ``other`` Designates the default time-sharing scheduling in Linux. They can run until they are blocked by an I/O request or preempted by higher priorities or superior scheduling designations.

- ``fifo`` Designates first-in out scheduling. These threads always immediately preempt any currently running other, batch or idle threads. They can run until they are either blocked by an I/O request or preempted by a FIFO thread of a higher priority.

- ``rr`` Designates round-robin scheduling. These threads always preempt any currently running other, batch or idle threads. The scheduler allows these threads to run for a fixed period of a time. If the thread is still running when this time period is exceeded, they are stopped and moved to the end of the list, allowing another round-robin thread of the same priority to run in their place. They can otherwise continue to run until they are blocked by an I/O request or are preempted by threads of a higher priority.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcomm.thread_prio=rr:2"


.. _`gcs.fc_debug`:
.. rst-class:: section-heading
.. rubric:: ``gcs.fc_debug``

.. index::
   pair: wsrep Provider Options; gcs.fc_debug

Post debug statistics about replication flow every this number of writesets.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_debug=0"


.. _`gcs.fc_factor`:
.. rst-class:: section-heading
.. rubric:: ``gcs.fc_factor``

.. index::
   pair: wsrep Provider Options; gcs.fc_factor

Resume replication after recv queue drops below this fraction of ``gcs.fc_limit``.

.. csv-table::
   :class: doc-options

   "Default Value", "``0.5``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_factor=0.5"


.. _`gcs.fc_limit`:
.. rst-class:: section-heading
.. rubric:: ``gcs.fc_limit``

.. index::
   pair: wsrep Provider Options; gcs.fc_limit

Pause replication if recv queue exceeds this number of  writesets. For primary-replica setups this number can be increased considerably.

.. csv-table::
   :class: doc-options

   "Default Value", "``16``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_limit=16"


.. _`gcs.fc_master_slave`:
.. rst-class:: section-heading
.. rubric:: ``gcs.fc_master_slave``

.. index::
   pair: wsrep Provider Options; gcs.fc_master_slave


Deprecated as of Galera 4.10 in favor of ``gcs.fc_single_primary``.

.. _`gcs.fc_single_primary`:
.. rst-class:: section-heading
.. rubric:: ``gcs.fc_single_primary``

.. index::
   pair: wsrep Provider Options; gcs.fc_single_primary

Defines whether there is more than one source of replication. 

As the number of nodes in the cluster grows, the larger the calculated ``gcs.fc_limit`` gets. At the same time, the number of writes from the nodes increases.

When this parameter value is set to NO (multi-primary), the ``gcs.fc_limit`` parameter is dynamically modified to give more margin for each node to be a bit further behind applying writes.

The ``gcs.fc_limit`` parameter is modified by the square root of the cluster size, that is, in a four-node cluster it is two times higher than the base value. This is done to compensate for the increasing replication rate noise.


.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_single_primary=NO"


.. _`gcs.max_packet_size`:
.. rst-class:: section-heading
.. rubric:: ``gcs.max_packet_size``

.. index::
   pair: wsrep Provider Options; gcs.max_packet_size

All writesets exceeding that size will be fragmented.

.. csv-table::
   :class: doc-options

   "Default Value", "``64500``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.max_packet_size=64500"


.. _`gcs.max_throttle`:
.. rst-class:: section-heading
.. rubric:: ``gcs.max_throttle``

.. index::
   pair: wsrep Provider Options; gcs.max_throttle

How much to throttle replication rate during state transfer (to avoid running out of memory). Set the value to 0.0 if stopping replication is acceptable for completing state transfer.

.. csv-table::
   :class: doc-options

   "Default Value", "``0.25``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.max_throttle=0.25"


.. _`gcs.recv_q_hard_limit`:
.. rst-class:: section-heading
.. rubric:: ``gcs.recv_q_hard_limit``

.. index::
   pair: wsrep Provider Options; gcs.recv_q_hard_limit

Maximum allowed size of recv queue. This should normally be half of (RAM + swap). If this limit is exceeded, Galera Cluster will abort the server.

.. csv-table::
   :class: doc-options

   "Default Value", "``LLONG_MAX``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.recv_q_hard_limit=LLONG_MAX"


.. _`gcs.recv_q_soft_limit`:
.. rst-class:: section-heading
.. rubric:: ``gcs.recv_q_soft_limit``

.. index::
   pair: wsrep Provider Options; gcs.recv_q_soft_limit

The fraction of :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` after which replication rate will be throttled.

.. csv-table::
   :class: doc-options

   "Default Value", "``0.25``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The degree of throttling is a linear function of recv queue size and goes from 1.0 (``full rate``)
at :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` to :ref:`gcs.max_throttle <gcs.max_throttle>` at :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` Note that ``full rate``, as estimated between 0 and :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` is a very imprecise estimate of a regular replication rate.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.recv_q_soft_limit=0.25"


.. _`gcs.sync_donor`:
.. rst-class:: section-heading
.. rubric:: ``gcs.sync_donor``

.. index::
   pair: wsrep Provider Options; gcs.sync_donor

Should the rest of the cluster keep in sync with the donor? ``YES`` means that if the donor is blocked by state transfer, the whole cluster is blocked with it.

.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "No"
   "Initial Version", "1.0"

If you choose to use value ``YES``, it is theoretically possible that the :term:`Donor Node` cannot keep up with the rest of the cluster due to the extra load from the SST. If the node lags behind, it may send flow control messages stalling the whole cluster. However, you can monitor this using the :ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>` status variable.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.sync_donor=NO"


.. _`gcs.vote_policy`:
.. rst-class:: section-heading
.. rubric:: ``gcs.vote_policy``

.. index::
   pair: wsrep Provider Options; gcs.vote_policy

When a cluster node fails to apply a writeset, it initiates voting on the outcome. Every node casts a vote, that is, a hash of the error message or 0, if there was no error. If a node votes "wrong", the node is considered to be inconsistent and it shuts down. ``gcs.vote_policy`` decides on how the votes are being counted and how to choose the winner:

- ``gcs.vote_policy = 0`` - The outcome that has more votes is chosen as the winner. In other words, simple majority wins. In the case of a tie between 0 (success) and non-0 (error) outcomes, 0 (success) is preferred.
- ``gcs.vote_policy > 0`` - If success gets as many as or more votes that the parameter value defines, it is chosen as the winner, even if in minority. For example, if ``gcs.vote_policy=1``, only the node that successfully committed a transaction would remain primary. Note that if ``gcs.vote_policy=1``, an inconsistent primary may crash all the secondaries.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.vote_policy=0"


.. _`gmcast.isolate`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.isolate``

.. index::
   pair: wsrep Provider Options; gmcast.isolate

.. warning:: This parameter is meant for testing use only, and never meant for production use cases.

Defines how cluster connections are handled.

.. csv-table::
   :class: doc-options

   "Default Value", "0"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The options are:

- ``0`` - Cluster connections are handled as usual.
- ``1`` - The node closes all cluster connections, does not open new cluster connections and rejects all incoming cluster connections.
- ``2`` - The node closes all cluster connections and terminates the group communication, moving the node into disconnected state.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

    wsrep_provider_options="gmcast.isolate=1"


.. _`gmcast.listen_addr`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.listen_addr``

.. index::
   pair: wsrep Provider Options; gmcast.listen_addr

Address at which *Galera Cluster* listens to connections from other nodes. By default the port to listen at is taken from the connection address. This setting can be used to overwrite that.

.. csv-table::
   :class: doc-options

   "Default Value", "``tcp://0.0.0.0:4567``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.listen_addr=tcp://0.0.0.0:4567"


.. _`gmcast.mcast_addr`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.mcast_addr``

.. index::
   pair: wsrep Provider Options; gmcast.mcast_addr

If set, UDP multicast will be used for replication, for example:

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The value must be the same on all nodes.

If you are planning to build a large cluster, we recommend using UDP.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

    wsrep_provider_options="gmcast.mcast_addr=239.192.0.11"


.. _`gmcast.mcast_ttl`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.mcast_ttl``

.. index::
   pair: wsrep Provider Options; gmcast.mcast_ttl

Time to live value for multicast packets.

.. csv-table::
   :class: doc-options

   "Default Value", "``1``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.mcast_ttl=1"


.. _`gmcast.peer_timeout`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.peer_timeout``

.. index::
   pair: wsrep Provider Options; gmcast.peer_timeout

Connection timeout for inactive connections.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT3S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

GMCast module monitors liveness of the socket connections on a regular basis.
Nodes exchange periodically replication and keepalives messages,
which are expected to be received more frequently than
``gmcast.peer_timeout`` duration. The ``gmcast.peer_timeout`` defines the
timeout after which an idle socket connection between two nodes is considered
inactive and will be closed and reopened again. If a socket connection is
closed due to timeout, the relaying protocol is activated as a side effect to
keep messages delivered to all members in the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.peer_timeout=PT3S"


.. _`gmcast.segment`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.segment``

.. index::
   pair: wsrep Provider Options; gmcast.segment

Define which network segment this node is in. Optimisations on communication are performed to minimise the amount of traffic between network segments including writeset relaying and IST and SST donor selection. The :ref:`gmcast.segment <gmcast.segment>` value is an integer from ``0`` to ``255``. By default all nodes are placed in the same segment (``0``).

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "3.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.segment=0"


.. _`gmcast.time_wait`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.time_wait``

.. index::
   pair: wsrep Provider Options; gmcast.time_wait

Time to wait until allowing peer declared outside of stable view to reconnect.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

In case a node leaves or gets partitioned from the cluster, it is kept
isolated from the rest of the cluster for a while to avoid distractions
to membership protocol operation. Option ``gmcast.time_wait`` denotes
the time period during which nodes in the primary component refuse
connection attempts from nodes not in the primary component in the
following way: The nodes which partitioned from the cluster are allowed
to reconnect after ``gmcast.time_wait/2`` seconds, the nodes which
left the group completely are allowed to reconnect after ``gmcast.time_wait``
seconds.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.time_wait=PT5S"


.. _`gmcast.version`:
.. rst-class:: section-heading
.. rubric:: ``gmcast.version``

.. index::
   pair: wsrep Provider Options; gmcast.version

This status variable is used to check which gmcast protocol version is used.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


.. _`innodb_flush_log_at_trx_commit`:
.. rst-class:: section-heading
.. rubric:: ``innodb_flush_log_at_trx_commit``

.. index::
   pair: wsrep Provider Options; innodb_flush_log_at_trx_commit

This variable controls the durability/speed trade-off for commits.

The possible values are:

- ``0`` - Nothing is done on commit; rather the log buffer is written and flushed to the InnoDB redo log once a second. This gives better performance, but a server crash can erase the last second of transactions.
- ``1`` - The log buffer is written to the InnoDB redo log file, and a flush to disk performed after each transaction. This is required for full ACID compliance.
- ``2`` - The log buffer is written to the InnoDB redo log after each commit, but flushing takes place every ``innodb_flush_log_at_timeout``(by default once a second). The performance is better, but an operating system crash or a power outage can cause the last second's transactions to be lost.
- ``3`` - Flush to disk at prepare and at commit. This option is slower and usually redundant. 

Options 0 and 2 can be faster than 1 or 3.

.. csv-table::
   :class: doc-options

   "Default Value", "1"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   innodb_flush_log_at_trx_commit="1"

This variable can also be set dynamically at runtime:

.. code-block:: mysql

   SET GLOBAL innodb_flush_log_at_trx_commit=1;

If you set ``innodb_flush_log_at_trx_commit`` dynamically at runtime, its value will be reset the next time the server restarts. To make the value persist on restart, set it also in a configuration file.

.. note:: If you use MySQL 8 or a later version, you can also use ``SET PERSIST`` to ensure the value persists upon restart.



.. _`ist.recv_addr`:
.. rst-class:: section-heading
.. rubric:: ``ist.recv_addr``

.. index::
   pair: wsrep Provider Options; ist.recv_addr

Address to listen on for Incremental State Transfer. By default this is the ``<address>:<port+1>`` from :ref:`wsrep_node_address <wsrep_node_address>`.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="ist.recv_addr=192.168.1.1"


.. _`ist.recv_bind`:
.. rst-class:: section-heading
.. rubric:: ``ist.recv_bind``

.. index::
   pair: wsrep Provider Options; ist.recv_bind

Defines the address that the node binds on for receiving an :term:`Incremental State Transfer`.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.16"

This option defines the address to which the node will bind in order to receive Incremental State Transfers. When this option is not set, it takes its value from :ref:`ist.recv_addr <ist.recv_addr>` or, in the event that that is also not set, from :ref:`wsrep_node_address <wsrep_node_address>`. You may find it useful when the node runs behind a NAT or in similar cases where the public and private addresses differ.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="ist.recv_bind=192.168.1.1"


.. _`pc.recovery`:
.. rst-class:: section-heading
.. rubric:: ``pc.recovery``

.. index::
   pair: wsrep Provider Options; pc.recovery
.. index::
   single: gvwstate.dat

When set to ``TRUE``, the node stores the Primary Component state to disk, in the ``gvwstate.dat`` file. The Primary Component can then recover automatically when all nodes that were part of the last saved state reestablish communications with each other.

.. csv-table::
   :class: doc-options

   "Default Value", "``TRUE``"
   "Dynamic", "No"
   "Initial Version", "3.0"

This allows for:

- Automatic recovery from full cluster crashes, such as in the case of a data center power outage.

- Graceful full cluster restarts without the need for explicitly bootstrapping a new Primary Component.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.recovery=TRUE"

.. note:: In the event that the wsrep position differs between nodes, recovery also requires a full State Snapshot Transfer.


.. _`pc.bootstrap`:
.. rst-class:: section-heading
.. rubric:: ``pc.bootstrap``

.. index::
   pair: wsrep Provider Options; pc.bootstrap

If you set this value to ``TRUE`` is a signal to turn a ``NON-PRIMARY`` component into ``PRIMARY``.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "Yes"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.bootstrap=TRUE"


.. _`pc.announce_timeout`:
.. rst-class:: section-heading
.. rubric:: ``pc.announce_timeout``

.. index::
   pair: wsrep Provider Options; pc.announce_timeout

Cluster joining announcements are sent every :math:`\frac{1}{2}` second for this period of time or less if the other nodes are discovered.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT3S``"
   "Dynamic", "No"
   "Initial Version", "2.0"

When a node joins the cluster, it will initially broadcast join
messages every half a second to inform other nodes about the joining
attempt, but does not handle its own messages to avoid forming
membership configuration containing only itself. This initial join
message broadcasting will terminate if at least one other node is seen
or if the timeout expires, whichever happens first.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.announce_timeout=PT3S"


.. _`pc.checksum`:
.. rst-class:: section-heading
.. rubric:: ``pc.checksum``

.. index::
   pair: wsrep Provider Options; pc.checksum

Checksum replicated messages.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "No"
   "Initial Version", "1.0"


If set to true, a CRC16 checksum is computed and included into
replicated messages on primary component protocol level. This checksum
is redundant since the checksum does not take into account all
protocol layers, and all messages are checksummed with stronger CRC32C
algorithm when transferred between nodes.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.checksum=TRUE"


.. _`pc.ignore_sb`:
.. rst-class:: section-heading
.. rubric:: ``pc.ignore_sb``

.. index::
   pair: wsrep Provider Options; pc.ignore_sb

Should we allow nodes to process updates even in the case of :term:`Split Brain`? This is a dangerous setting in a multi-primary setup, but should simplify things in a primary-replica cluster (especially if only 2 nodes are used).

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.ignore_sb=FALSE"


.. _`pc.ignore_quorum`:
.. rst-class:: section-heading
.. rubric:: ``pc.ignore_quorum``

.. index::
   pair: wsrep Provider Options; pc.ignore_quorum

Completely ignore :term:`Quorum` calculations. For example if the primary splits from several replicas it still remains operational. Use with extreme caution even in primary-replica setups, as replicas will not automatically reconnect to primary in this case.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.ignore_quorum=FALSE"


.. _`pc.linger`:
.. rst-class:: section-heading
.. rubric:: ``pc.linger``

.. index::
   pair: wsrep Provider Options; pc.linger

The period for which the PC protocol waits for the EVS termination.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT2S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When a node leaves the cluster, it will wait up to ``pc.linger`` duration to
get itself removed gracefully from the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.linger=PT2S"


.. _`pc.npvo`:
.. rst-class:: section-heading
.. rubric:: ``pc.npvo``

.. index::
   pair: Parameters; pc.npvo

Control which primary component is allowed to continue in case of
conflicting primary components after cluster partitioning.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

If the cluster is configured to ignore quorum or split brain, the
nodes may continue processing write sets independently after cluster
partitioning, which leads to diverged states. When the cluster merges
back to the original configuration, the ``pc.npvo`` controls which
partition is allowed to continue after the merge. If the value is
``FALSE``, the partition with the lowest view identifier (the most
immediate successor to the view before partitioning) is allowed to
continue. Otherwise the partition with the highest view identifier
(the one which has gone through more configuration changes or has a
representative with highest node identifier) is allowed to continue.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.npvo=FALSE"


.. _`pc.wait_prim`:
.. rst-class:: section-heading
.. rubric:: ``pc.wait_prim``

.. index::
   pair: wsrep Provider Options; pc.wait_prim

Control whether a joining node is allowed to start in non-primary component
or if it should wait for primary component.

.. csv-table::
   :class: doc-options

   "Default Value", "``TRUE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

This variable can be used to control if a node waits for connecting to
the primary component when joining to the cluster.

With default value ``TRUE``, the joining node waits for the primary
component so that the first event delivered by the group
communication system is the primary component view event, or times
out with error (see :ref:`pc.wait_prim_timeout <pc.wait_prim_timeout>`).

With value ``FALSE``, the joining node completes the initialization
without waiting for the primary component, and may end up in
non-primary component if no other nodes are seen in
:ref:`pc.announce_timeout <pc.announce_timeout>`. This is a useful
setting mainly if it is desirable to start the cluster by starting all
the nodes at once, and bootstrapping the primary component with
:ref:`pc.bootstrap <pc.bootstrap>` after all nodes have been started.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim=FALSE"


.. _`pc.wait_prim_timeout`:
.. rst-class:: section-heading
.. rubric:: ``pc.wait_prim_timeout``

.. index::
   pair: wsrep Provider Options; pc.wait_prim_timeout

The timeout for waiting primary component.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "2.0"

The timeout after which an error is thrown if a primary view event is
not seen when joining a new node into the cluster. This value is
effective only if :ref:`pc.wait_prim <pc.wait_prim>` is set to ``TRUE``.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim_timeout=PT30S"


.. _`pc.weight`:
.. rst-class:: section-heading
.. rubric:: ``pc.weight``

.. index::
   pair: wsrep Provider Options; pc.weight

Node weight for quorum calculation.

.. csv-table::
   :class: doc-options

   "Default Value", "``1``"
   "Dynamic", "Yes"
   "Initial Version", "2.4"

For detailed description about weighted quorum see
https://galeracluster.com/library/documentation/weighted-quorum.html

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.weight=1"


.. _`pc.version`:
.. rst-class:: section-heading
.. rubric:: ``pc.version``

.. index::
   pair: wsrep Provider Options; pc.version

This variable is used to control which PC protocol version is used.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

This variable is mostly used for troubleshooting purposes and should
not be implemented in a production environment.


.. _`protonet.backend`:
.. rst-class:: section-heading
.. rubric:: ``protonet.backend``

.. index::
   pair: wsrep Provider Options; protonet.backend

This parameter is deprecated and will be removed in the future versions.

Which transport backend to use. Currently only ASIO is supported.
This variable is deprecated and will be removed in the future
versions.

.. csv-table::
   :class: doc-options

   "Default Value", "``asio``"
   "Dynamic", "No"
   "Initial Version", "1.0"
   "Version Deprecated", "4.14"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="protonet.backend=asio"


.. _`protonet.version`:
.. rst-class:: section-heading
.. rubric:: ``protonet.version``

.. index::
   pair: wsrep Provider Options; protonet.version

This parameter is deprecated and will be removed in the future versions

This status variable is used to check which transport backend protocol version is used.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"
   "Version Deprecated", "4.14"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


.. _`repl.commit_order`:
.. rst-class:: section-heading
.. rubric:: ``repl.commit_order``

.. index::
   pair: wsrep Provider Options; repl.commit_order

.. warning:: Do not change the default value ``3``, as other values may produce inconsistencies or even lead to server crashes.

Whether to allow Out-Of-Order committing (improves parallel applying performance).

.. csv-table::
   :class: doc-options

   "Default Value", "``3``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Possible settings:

- ``0`` or ``BYPASS`` All commit order monitoring is switched off (useful for measuring performance penalty).

- ``1`` or ``OOOC`` Allows out of order committing for all transactions.

- ``2`` or ``LOCAL_OOOC``  Allows out of order committing only for local transactions.

- ``3`` or ``NO_OOOC`` No out of order committing is allowed (strict total order committing)

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.commit_order=2"


.. _`repl.causal_read_timeout`:
.. rst-class:: section-heading
.. rubric:: ``repl.causal_read_timeout``

.. index::
   pair: wsrep Provider Options; repl.causal_read_timeout

The default timeout for causal read and sync wait operations.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.causal_read_timeout=PT30S"


.. _`repl.key_format`:
.. rst-class:: section-heading
.. rubric:: ``repl.key_format``

.. index::
   pair: wsrep Provider Options; repl.key_format

The hash size to use for key formats (in bytes). An ``A`` suffix annotates the version.

.. csv-table::
   :class: doc-options

   "Default Value", "``FLAT8``"
   "Dynamic", "No"
   "Initial Version", "3.0"

Possible settings:

- ``FLAT8``
- ``FLAT8A``
- ``FLAT16``
- ``FLAT16A``

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.key_format=FLAT8"


.. _`repl.max_ws_size`:
.. rst-class:: section-heading
.. rubric:: ``repl.max_ws_size``

.. index::
   pair: wsrep Provider Options; repl.max_ws_size

The maximum size of a write-set in bytes. This is limited to 2G.

.. csv-table::
   :class: doc-options

   "Default Value", "``2147483647``"
   "Dynamic", "No"
   "Initial Version", "3.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.max_ws_size=2147483647"


.. _`repl.proto_max`:
.. rst-class:: section-heading
.. rubric:: ``repl.proto_max``

.. index::
   pair: wsrep Provider Options; repl.proto_max

The maximum protocol version in replication. Changes to this parameter will only take effect after a provider restart.

.. csv-table::
   :class: doc-options

   "Default Value", "``5``"
   "Dynamic", "No"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.proto_max=5"


.. _`socket.recv_buf_size`:
.. rst-class:: section-heading
.. rubric:: ``socket.recv_buf_size``

.. index::
   pair: wsrep Provider Options;  socket.recv_buf_size

The size of the receive buffer that used on the network sockets between nodes. Galera passes the value to the kernel via the ``SO_RCVBUF`` socket option. The value is either numeric value in bytes or ``auto`` which allows the kernel to autotune the receive buffer. The default was changed from ``212992`` to ``auto`` in 3.29.

.. csv-table::
   :class: doc-options

   "Default Value", "``auto``"
   "Dynamic", "No"
   "Initial Version", "3.17"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.recv_buf_size=212992"

.. _`socket.send_buf_size`:
.. rst-class:: section-heading
.. rubric:: ``socket.send_buf_size``

.. index::
   pair: wsrep Provider Options;  socket.send_buf_size

The size of the send buffer that used on the network sockets between nodes. Galera passes the value to the kernel via the ``SO_SNDBUF`` socket option. The value is either numeric value in bytes or ``auto`` which allows the kernel to autotune the send buffer.

.. csv-table::
   :class: doc-options

   "Default Value", "``auto``"
   "Dynamic", "No"
   "Initial Version", "3.29"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.send_buf_size=212992"


.. _`socket.ssl`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl``

.. index::
   pair: wsrep Provider Options; socket.ssl

Explicitly enables TLS usage by the wsrep provider.

.. csv-table::
   :class: doc-options

   "Default Value", "``No``"
   "Dynamic", "No"


.. _`socket.ssl_ca`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_ca``

.. index::
   pair: wsrep Provider Options; socket.ssl_ca

Defines the path to the SSL Certificate Authority (CA) file.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the CA file to verify the signature on the certificate. You can use either an absolute path or one relative to the working directory. The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options='socket.ssl_ca=/path/to/ca-cert.pem'

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.ssl_cert`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_cert``

.. index::
   pair: wsrep Provider Options; socket.ssl_cert

Defines the path to the :abbr:`SSL (Secure Socket Layer)` certificate.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the certificate as a self-signed public key in encrypting replication traffic over :abbr:`SSL (Secure Socket Layer)`. You can use either an absolute path or one relative to the working directory. The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_cert=/path/to/server-cert.pem"

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.checksum`:
.. rst-class:: section-heading
.. rubric:: ``socket.checksum``

.. index::
   pair: wsrep Provider Options; socket.checksum

Checksum to use on socket layer.

.. csv-table::
   :class: doc-options

   "Default Value", "``1`` (before vs. 3), ``2``"
   "Dynamic", "No"
   "Initial Version", "2.0"

The possible values are:

- ``0`` - Disable checksum
- ``1`` - CRC32
- ``2`` - CRC-32C (optimized and potentially HW-accelerated on Intel CPUs)

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.checksum=2"


.. _`socket.dynamic`:
.. rst-class:: section-heading
.. rubric:: ``socket.dynamic``

.. index::
   pair: wsrep Provider Options; socket.dynamic

Enable connection engine to accept both SSL and TCP connections. 

.. csv-table::
   :class: doc-options

   "Default Value", "false"
   "Dynamic", "No"
   "Initial Version", "4.8"

By enabling this parameter, it should be possible for Galera to communicate with both SSL and TCP connections.
If SSL is enabled it will try to establish/accept SSL connection first and than fallback to TCP connection if
necessary.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.dynamic=true"


.. _`socket.ssl_cipher`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_cipher``

.. index::
   pair: wsrep Provider Options; socket.ssl_cipher

Symmetric cipher to use for encrypted connections.

.. csv-table::
   :class: doc-options

   "Default Value", "````"
   "Dynamic", "No"
   "Initial Version", "1.0"

This parameter defines which cipher to use for encrypted SSL connections.
If left empty, the SSL library implementation default cipher is used.

The value format depends on used SSL implementation. For OpenSSL, see
cipher list format description in
https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html.

The default value was ``AES128-SHA`` until Galera version 3.24.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_cipher=AES128-SHA256"


.. _`socket.ssl_compression`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_compression``

.. index::
   pair: wsrep Provider Options; socket.ssl_compression

This parameter is deprecated and will be removed in the future versions.

Whether to enable compression on SSL connections.

.. csv-table::
   :class: doc-options

   "Default Value", "``YES``"
   "Dynamic", "No"
   "Initial Version", "1.0"
   "Version Deprecated", "4.14"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_compression=YES"


.. _`socket.ssl_key`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_key``

.. index::
   pair: wsrep Provider Options; socket.ssl_key

Defines the path to the :abbr:`SSL (Secure Socket Layer)` certificate key.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the certificate key a self-signed private key in encrypting replication traffic over  :abbr:`SSL (Secure Socket Layer)`. You can use either an absolute path or one relative to the working directory. The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_key=/path/to/server-key.pem"

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.ssl_password_file`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_password_file``

.. index::
   pair: wsrep Provider Options; socket.ssl_password_file

Defines a password file for use in :abbr:`SSL (Secure Socket Layer)` connections.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

In the event that you have your SSL key file encrypted, the node uses the SSL password file to decrypt the key file.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_password_file=/path/to/password-file"


.. _`socket.ssl_reload`:
.. rst-class:: section-heading
.. rubric:: ``socket.ssl_reload``

.. index::
   pair: wsrep Provider Options; socket.ssl_reload

Reinitialize SSL context.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "Yes"
   "Initial Version", "4.8"

Parameter used to dynamically reinitialize the Galera SSL context. This is most useful if you need to 
replace a certificate that is about to expire without restarting the server. You need to change the 
certificate and key files at the relevant paths defined by SSL variables.

The excerpt below is an example of how this Galera parameter can be triggered from running database:

.. code-block:: ini

   SET GLOBAL wsrep_provider_options = 'socket.ssl_reload=1';


.. _`Setting Galera Parameters in MySQL`:

-------------------------------------
 Setting Galera Parameters in MySQL
-------------------------------------

.. index::
   pair: wsrep Provider Options; Setting
.. index::
   pair: wsrep Provider Options; Checking

You can set *Galera Cluster* parameters in the ``my.cnf`` configuration file as follows:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_limit=256;gcs.fc_factor=0.9"

This is useful in primary-replica setups.

You can set Galera Cluster parameters through a MySQL client with the following query:

.. code-block:: mysql

	SET GLOBAL wsrep_provider_options="evs.send_window=16";

This query  only changes the :ref:`evs.send_window <evs.send_window>` value.

To check which parameters are used in Galera Cluster, enter the following query:

.. code-block:: mysql

	SHOW VARIABLES LIKE 'wsrep_provider_options';


.. container:: bottom-links

   Related Documents

   - :doc:`auto-eviction`
   - :doc:`ssl-cert`


.. |br| raw:: html

   <br />

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
