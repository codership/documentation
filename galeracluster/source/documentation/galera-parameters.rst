.. meta::
   :title: Galera Cluster Parameters
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :doc:`auto-eviction`
      - :doc:`ssl-cert`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`galera-parameters`:

==================
Galera Parameters
==================

As of version 0.8, Galera Cluster accepts parameters as semicolon-separated key value pair lists, such as ``key1 = value1; key2 = value2``.  In this way, you can configure an arbitrary number of Galera Cluster parameters in one call. A key consists of parameter group and parameter name: ``<group>.<name>``, where ``<group>`` corresponds roughly to some Galera module.

All ``wsrep_provider_options`` settings need to be specified on a single line. In case of multiple instances of ``wsrep_provider_options``, only the last one is used.

Below is a list of all of the Galera parameters.  Each is also a link to further down the page where you may find more information.  There are a few things to know about this table:

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
   :header: "|br| Parameter", "|br| Default", "|br| Dynamic", "Debug |br| Only", "Initial |br| Version"
   :widths: 30, 40, 10, 10, 10

   ":ref:`base_host <base_host>`", "detected network address", "", "", "1.0"
   ":ref:`base_port <base_port>`", "``4567``", "", "", "1.0"
   ":ref:`cert.log_conflicts <cert.log_conflicts>`", "``NO``", "  Yes", "", "2.0"
   ":ref:`cert.optimistic_pa <cert.optimistic_pa>`", "``YES``", "  Yes", "", "3.25"
   ":ref:`debug <debug>`", "``NO``", "  Yes", "", "2.0"
   ":ref:`evs.auto_evict <evs.auto_evict>`", "``0``", "   No", "", "3.8"
   ":ref:`evs.causal_keepalive_period <evs.causal_keepalive_period>`", "``0``", "   No", "", "1.0"
   ":ref:`evs.consensus_timeout <evs.consensus_timeout>`", "``PT30S``", "   No", "Yes", "1.0, 2.0"
   ":ref:`evs.debug_log_mask <evs.debug_log_mask>`", "``0x1``", "  Yes", "", "1.0"
   ":ref:`evs.delayed_keep_period <evs.delayed_keep_period>`", "``PT30S``", "   No", "", "3.8"
   ":ref:`evs.delayed_margin <evs.delayed_margin>`", "``PT1S``", "   No", "", "3.8"
   ":ref:`evs.evict <evs.evict>`", "", "   No", "", "3.8"
   ":ref:`evs.inactive_check_period <evs.inactive_check_period>`", "``PT1S``", "   No", "", "1.0"
   ":ref:`evs.inactive_timeout <evs.inactive_timeout>`", "``PT15S``", "   No", "", "1.0"
   ":ref:`evs.info_log_mask <evs.info_log_mask>`", "``0``", "   No", "", "1.0"
   ":ref:`evs.install_timeout <evs.install_timeout>`", "``PT15S``", "  Yes", "", "1.0"
   ":ref:`evs.join_retrans_period <evs.join_retrans_period>`", "``PT1S``", "  Yes", "", "1.0"
   ":ref:`evs.keepalive_period <evs.keepalive_period>`", "``PT1S``", "  No", "", "1.0"
   ":ref:`evs.max_install_timeouts <evs.max_install_timeouts>`", "``1``", "  No", "", "1.0"
   ":ref:`evs.send_window <evs.send_window>`", "``4``", "  Yes", "", "1.0"
   ":ref:`evs.stats_report_period <evs.stats_report_period>`", "``PT1M``", "  No", "", "1.0"
   ":ref:`evs.suspect_timeout <evs.suspect_timeout>`", "``PT5S``", "  No", "", "1.0"
   ":ref:`evs.use_aggregate <evs.use_aggregate>`", "``TRUE``", "  No", "", "1.0"
   ":ref:`evs.user_send_window <evs.user_send_window>`", "``2``", "  Yes", "", "1.0"
   ":ref:`evs.view_forget_timeout <evs.view_forget_timeout>`", "``PT5M``", "  No", "", "1.0"
   ":ref:`evs.version <evs.version>`", "``0``", "  No", "Yes", "1.0"
   ":ref:`gcache.dir <gcache.dir>`", "working directory", "  No", "", "1.0"
   ":ref:`gcache.name <gcache.name>`", "``galera.cache``", "  No", "", "1.0"
   ":ref:`gcache.keep_pages_size <gcache.keep_pages_size>`", "``0``", "  No", "", "1.0"
   ":ref:`gcache.page_size <gcache.page_size>`", "``128Mb``", "  No", "", "1.0"
   ":ref:`gcache.recover <gcache.recover>`", "``no``", "  No", "", "3.19"
   ":ref:`gcache.size <gcache.size>`", "``128Mb``", "  No", "", "1.0"
   ":ref:`gcomm.thread_prio <gcomm.thread_prio>`", "", "  No", "", "3.0"
   ":ref:`gcs.fc_debug <gcs.fc_debug>`", "``0``", "  No", "", "1.0"
   ":ref:`gcs.fc_factor <gcs.fc_factor>`", "``1.0``", "  No", "", "1.0"
   ":ref:`gcs.fc_limit <gcs.fc_limit>`", "``16``", "  Yes", "", "1.0"
   ":ref:`gcs.fc_master_slave <gcs.fc_master_slave>`", "``NO``", "  No", "", "1.0"
   ":ref:`gcs.max_packet_size <gcs.max_packet_size>`", "``32616``", "  No", "", "1.0"
   ":ref:`gcs.max_throttle <gcs.max_throttle>`", "``0.25``", "  No", "", "1.0"
   ":ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>`", "``LLONG_MAX``", "  No", "", "1.0"
   ":ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>`", "``0.25``", "  No", "", "1.0"
   ":ref:`gcs.sync_donor <gcs.sync_donor>`", "``NO``", "  No", "", "1.0"
   ":ref:`gmcast.listen_addr <gmcast.listen_addr>`", "``tcp://0.0.0.0:4567``", "  No", "", "1.0"
   ":ref:`gmcast.mcast_addr <gmcast.mcast_addr>`", "", "  No", "", "1.0"
   ":ref:`gmcast.mcast_ttl <gmcast.mcast_ttl>`", "``1``", "  No", "", "1.0"
   ":ref:`gmcast.peer_timeout <gmcast.peer_timeout>`", "``PT3S``", "  No", "", "1.0"
   ":ref:`gmcast.segment <gmcast.segment>`", "``0``", "  No", "", "3.0"
   ":ref:`gmcast.time_wait <gmcast.time_wait>`", "``PT5S``", "  No", "", "1.0"
   ":ref:`gmcast.version <gmcast.version>`", "n/a", "  No", "Yes", "1.0"
   ":ref:`ist.recv_addr <ist.recv_addr>`", "", "  No", "", "1.0"
   ":ref:`ist.recv_bind <ist.recv_bind>`", "", "  No", "", "3.0"
   ":ref:`pc.recovery <pc.recovery>`", "``TRUE``", "  No", "", "3.0"
   ":ref:`pc.bootstrap <pc.bootstrap>`", "n/a", "  No", "", "2.0"
   ":ref:`pc.announce_timeout <pc.announce_timeout>`", "``PT3S``", "  No", "", "2.0"
   ":ref:`pc.checksum <pc.checksum>`", "``FALSE``", "  No", "", "1.0"
   ":ref:`pc.ignore_sb <pc.ignore_sb>`", "``FALSE``", "  Yes", "", "1.0"
   ":ref:`pc.ignore_quorum <pc.ignore_quorum>`", "``FALSE``", "  Yes", "", "1.0"
   ":ref:`pc.linger <pc.linger>`", "``PT2S``", "  No", "", "1.0"
   ":ref:`pc.npvo <pc.npvo>`", "``FALSE``", "  No", "", "1.0"
   ":ref:`pc.wait_prim <pc.wait_prim>`", "``TRUE``", "  No", "", "1.0"
   ":ref:`pc.wait_prim_timeout <pc.wait_prim_timeout>`", "``PT30S``", "  No", "", "2.0"
   ":ref:`pc.weight <pc.weight>`", "``1``", "  Yes", "", "2.4"
   ":ref:`pc.version <pc.version>`", "n/a", "No", "Yes", "1.0"
   ":ref:`protonet.backend <protonet.backend>`", "``asio``", "  No", "", "1.0"
   ":ref:`protonet.version <protonet.version>`", "n/a", "  No", "Yes", "1.0"
   ":ref:`repl.commit_order <repl.commit_order>`", "``3``", "  No", "", "1.0"
   ":ref:`repl.causal_read_timeout <repl.causal_read_timeout>`", "``PT30S``", "  No", "", "1.0"
   ":ref:`repl.key_format <repl.key_format>`", "``FLAT8``", "  No", "", "3.0"
   ":ref:`repl.max_ws_size <repl.max_ws_size>`", "``2147483647``", "  No", "", "3.0"
   ":ref:`repl.proto_max <repl.proto_max>`", "``5``", "  No", "", "2.0"
   ":ref:`socket.recv_buf_size <socket.recv_buf_size>`", "``212992``", "  Yes", "", "3.17"
   ":ref:`socket.ssl_ca <socket.ssl_ca>`", "", "  No", "", "1.0"
   ":ref:`socket.ssl_cert <socket.ssl_cert>`", "", "  No", "", "1.0"
   ":ref:`socket.checksum <socket.checksum>`", "``1`` (vs. 2); ``2`` (vs. 3)", "  No", "", "2.0"
   ":ref:`socket.ssl_cipher <socket.ssl_cipher>`", "``AES128-SHA`` (vs. 1); |br| system default (vs. 3.24)", "  No", "", "1.0"
   ":ref:`socket.ssl_compression <socket.ssl_compression>`", "``YES``", "  No", "", "1.0"
   ":ref:`socket.ssl_key <socket.ssl_key>`", "", "  No", "", "1.0"
   ":ref:`socket.ssl_password_file <socket.ssl_password_file>`", "", "  No", "", "1.0"



.. _`base_host`:
.. rst-class:: rubric-1
.. rubric:: ``base_host``

.. index::
   pair: wsrep Provider Options; base_host

Global variable for internal use.

.. csv-table::
   :class: doc-options

   "Default Value", "detected network address"
   "Dynamic", ""
   "Initial Version", "???"

.. warning:: Since this is for internal use only, don't manually set the ``base_host`` variable.


.. _`base_port`:
.. rst-class:: rubric-1
.. rubric:: ``base_port``

.. index::
   pair: wsrep Provider Options; base_port

Global variable for internal use.

.. csv-table::
   :class: doc-options

   "Default Value", "``4567``"
   "Dynamic", ""
   "Initial Version", "???"

.. warning:: Since this is for internal use only, don't manually set the ``base_port`` variable.


.. _`cert.log_conflicts`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``cert.optimistic_pa``

.. index::
   pair: wsrep Provider Options; cert.optimistic_pa

Controls parallel applying of slave actions. When enabled allows full range
of parallelization as determined by certification algorithm. When disabled
limits parallel applying window to not exceed that seen on master. In other
words, the action starts applying no sooner than all actions it has seen
on the master are committed.

.. csv-table::
   :class: doc-options

   "Default Value", "``YES``"
   "Dynamic", "Yes"
   "Initial Version", "3.25"

.. code-block:: ini

   wsrep_provider_options="cert.optimistic_pa=NO"


.. _`debug`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``evs.auto_evict``

.. index::
   pair: wsrep Provider Options; evs.auto_evict

Defines how many entries the node allows for given a delayed node before it triggers the Auto Eviction protocol.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors the group communication response times from all other nodes.  When the cluster registers delayed response from a given node, it adds an entry for that node to its delayed list.  If the majority of the cluster nodes show the node as delayed, the node is permanently evicted from the cluster.

This parameter determines how many entries a given node can receive before it triggers Auto Eviction.

When this parameter is set to ``0``, it disables the Auto Eviction protocol for this node.  Even when you disable Auto Eviction, though; the node continues to monitor response times from the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.auto_evict=5"

For more information on the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.causal_keepalive_period`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``evs.delayed_keep_period``

.. index::
   pair: wsrep Provider Options; evs.delayed_keep_period

Defines how long this node requires a delayed node to remain responsive before it removes an entry from the delayed list.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors the group communication response times from all other nodes.  When the cluster registered delayed responses from a given node, it adds an entry for that node to its delayed list.  Nodes that remain on the delayed list can trigger Auto Eviction, which removes them permanently from the cluster.

This parameter determines how long a node on the delayed list must remain responsive before it removes one entry. The number of entries on the delayed list and how long it takes before the node removes all entries depends on how long the delayed node was unresponsive.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.delayed_keep_period=PT45S"

For more information on the delayed list and the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.delayed_margin`:
.. rst-class:: rubric-1
.. rubric:: ``evs.delayed_margin``

.. index::
   pair: wsrep Provider Options; evs.delayed_margin

Defines how long the node allows response times to deviate before adding an entry to the delayed list.

.. csv-table::
   :class: doc-options

   "Default Value", "PT1S"
   "Dynamic", "No"
   "Initial Version", "3.8"

Each cluster node monitors group communication response times from all other nodes.  When the cluster registers a delayed response from a given node, it adds an entry for that node to its delayed list.  Delayed nodes can trigger Auto Eviction, which removes them permanently from the cluster.

This parameter determines how long a delay can run before the node adds an entry to the delayed list.  You must set this parameter to a value higher than the round-trip delay time (RTT) between the nodes.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.delayed_margin=PT5S"

For more information on the delayed list and the Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.evict`:
.. rst-class:: rubric-1
.. rubric:: ``evs.evict``

.. index::
   pair: wsrep Provider Options; evs.evict

If set to the gcomm UUID of some node, that node will be evicted from the cluster.  Setting this parameter to an empty string causes the eviction list to be cleared on the node where it is set.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.8"

For more information on the eviction and Auto Eviction process, see :doc:`auto-eviction`.


.. _`evs.inactive_check_period`:
.. rst-class:: rubric-1
.. rubric:: ``evs.inactive_check_period``

.. index::
   pair: wsrep Provider Options; evs.inactive_check_period

Defines how often you want the node to check for peer inactivity.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes.  When the cluster registers a delayed response from a given node, it adds an entry for that node to its delayed list, which can lead to the delayed node's eviction from the cluster.

This parameter determines how often you want the node to check for delays in the group communication responses from other cluster nodes.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.inactive_check_period=PT1S"


.. _`evs.inactive_timeout`:
.. rst-class:: rubric-1
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

Each cluster node monitors group communication response times from all other nodes.  When the cluster registers a delayed response from a given node, it add an entry for that node to its delayed list, which can lead tot he delayed node's eviction from the cluster.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.inactive_timeout=PT15S"

This parameter sets a hard limit for node inactivity.  If a delayed node remains unresponsive for longer than this period, the node pronounces the delayed node as dead.


.. _`evs.info_log_mask`:
.. rst-class:: rubric-1
.. rubric:: ``evs.info_log_mask``

.. index::
   pair: wsrep Provider Options; evs.info_log_mask

Defines additional logging options for the EVS Protocol.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The EVS Protocol monitors group communication response times and controls the node eviction and auto eviction processes.  This parameter allows you to enable additional logging options, through a bitmask value.

- ``0x1`` Provides extra view change info.
- ``0x2`` Provides extra state change info
- ``0x4`` Provides statistics
- ``0x8`` Provides profiling (only in builds with profiling enabled)

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.info_log_mask=0x4"


.. _`evs.install_timeout`:
.. rst-class:: rubric-1
.. rubric:: ``evs.install_timeout``

.. index::
   pair: wsrep Provider Options; evs.install_timeout

Defines the timeout for install message acknowledgments.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT15S``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes, checking whether they are responsive or delayed.  This parameter determines how long you want the node to wait on install message acknowledgments.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.install_timeout=PT15S"

.. note:: This parameter replaces :ref:`evs.consensus_timeout <evs.consensus_timeout>`.


.. _`evs.join_retrans_period`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``evs.keepalive_period``

.. index::
   pair: wsrep Provider Options; evs.keepalive_period

Defines how often the node emits keepalive signals.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT1S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each cluster node monitors group communication response times from all other nodes.  When there is no traffic going out for the cluster to monitor, nodes emit keepalive signals so that other nodes have something to measure.  This parameter determines how often the node emits a keepalive signal, absent any other traffic.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.keepalive_period=PT1S"


.. _`evs.max_install_timeouts`:
.. rst-class:: rubric-1
.. rubric:: ``evs.max_install_timeouts``

.. index::
   pair: wsrep Provider Options; evs.max_install_timeouts

Defines the number of membership install rounds to try before giving up.

.. csv-table::
   :class: doc-options

   "Default Value", "``1``"
   "Dynamic", "No"
   "Initial Version", "1.0"

This parameter determines the maximum number of times that the node tries for a membership install acknowledgment, before it stops trying.  The total number of rounds it tries is this value plus 2.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.max_install_timeouts=1"


.. _`evs.send_window`:
.. rst-class:: rubric-1
.. rubric:: ``evs.send_window``

.. index::
   pair: wsrep Provider Options; evs.send_window

Defines the maximum number of packets at a time in replication.

.. csv-table::
   :class: doc-options

   "Default Value", "``4``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

This parameter determines the maximum number of packets the node uses at a time in replication.  For clusters implemented over :abbr:`WAN (Wide Area Network)`, you can set this value considerably higher, (for example, 512), than for clusters implemented over :abbr:`LAN (Local Area Network)`.

You must use a value that is greater than :ref:`evs.user_send_window <evs.user_send_window>`.  The recommended value is double :ref:`evs.user_send_window <evs.user_send_window>`.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.send_window=4"


.. _`evs.stats_report_period`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``evs.suspect_timeout``

.. index::
   pair: wsrep Provider Options; evs.suspect_timeout

Defines the inactivity period after which a node is *suspected* as dead.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each node in the cluster monitors group communications from all other nodes in the cluster.  This parameter determines the period of inactivity before the node suspects another of being dead.  If all nodes agree on that, the cluster drops the inactive node.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.suspect_timeout=PT5S"


.. _`evs.use_aggregate`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``evs.user_send_window``

.. index::
   pair: Parameters; evs.user_send_window

Defines the maximum number of data packets at a time in replication.

.. csv-table::
   :class: doc-options

   "Default Value", "``2``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

This parameter determines the maximum number of data packets the node uses at a time in replication.  For clusters implemented over :abbr:`WAN (Wide Area Network)`, you can set this to a value considerably higher than cluster implementations over :abbr:`LAN (Local Area Network)`, (for example, 512).

You must use a value that is smaller than :ref:`evs.send_window<evs.send_window>`.  The recommended value is half :ref:`evs.send_window<evs.send_window>`.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.user_send_window=2"

For more information, see :ref:`evs.send_window <evs.send_window>`.


.. _`evs.view_forget_timeout`:
.. rst-class:: rubric-1
.. rubric:: ``evs.view_forget_timeout``

.. index::
   pair: wsrep Provider Options; evs.view_forget_timeout

Defines how long the node saves past views from the view history.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

Each node maintains a history of past views.  This parameter determines how long you want the node to save past views before dropping them from the table.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.view_forget_timeout=PT5M"


.. _`evs.version`:
.. rst-class:: rubric-1
.. rubric:: ``evs.version``

.. index::
   pair: wsrep Provider Options; evs.version

Defines the EVS Protocol version.

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "1.0"

This parameter determines which version of the EVS Protocol the node uses.  In order to ensure backwards compatibility, the parameter defaults to ``0``.  Certain EVS Protocol features, such as Auto Eviction, require you to upgrade to more recent versions.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="evs.version=1"

For more information on the procedure to upgrade from one version to another, see :ref:`Upgrading the EVS Protocol <upgrade-evs>`.


.. _`gcache.dir`:
.. rst-class:: rubric-1
.. rubric:: ``gcache.dir``

.. index::
   pair: wsrep Provider Options; gcache.dir

Defines the directory where the write-set cache places its files.

.. csv-table::
   :class: doc-options

   "Default Value", "``/path/to/working_dir``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state.  Under certain methods, the node that sends the state transfer is similarly blocked.  To prevent the database from falling further behind, GCache saves the incoming write-sets on memory mapped files to disk.

This parameter determines where you want the node to save these files for write-set caching.  By default, GCache uses the working directory for the database server.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.dir=/usr/share/galera"


.. _`gcache.keep_pages_size`:
.. rst-class:: rubric-1
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


.. _`gcache.name`:
.. rst-class:: rubric-1
.. rubric:: ``gcache.name``

.. index::
   pair: wsrep Provider Options; gcache.name

Defines the filename for the write-set cache.

.. csv-table::
   :class: doc-options

   "Default Value", "``galera.cache``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state.  Under certain methods, the node that sends the state transfer is similarly blocked.  To prevent the database from falling further behind, GCache saves the incoming write-sets on memory-mapped files to disk.

This parameter determines the name you want the node to use for this ring buffer storage file.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.name=galera.cache"


.. _`gcache.page_size`:
.. rst-class:: rubric-1
.. rubric:: ``gcache.page_size``

.. index::
   pair: wsrep Provider Options; gcache.page_size

Size of the page files in page storage. The limit on overall page storage is the size of the disk.  Pages are prefixed by ``gcache.page``.

.. csv-table::
   :class: doc-options

   "Default Value", "``128M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.page_size=128Mb"


.. _`gcache.recover`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``gcache.size``

.. index::
   pair: wsrep Provider Options; gcache.size

Defines the disk space you want to node to use in caching write-sets.

.. csv-table::
   :class: doc-options

   "Default Value", "``128M``"
   "Dynamic", "No"
   "Initial Version", "1.0"

When nodes receive state transfers they cannot process incoming write-sets until they finish updating their state.  Under certain methods, the node that sends the state transfer is similarly blocked.  To prevent the database from falling further behind, GCache saves the incoming write-sets on memory-mapped files to disk.

This parameter defines the amount of disk space you want to allocate for the present ring buffer storage.  The node allocates this space when it starts the database server.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcache.size=128Mb"

For more information on customizing the write-set cache, see the :doc:`Best Practice Articles <../kb/best/index>`.


.. _`gcomm.thread_prio`:
.. rst-class:: rubric-1
.. rubric:: ``gcomm.thread_prio``

.. index::
   pair wsrep Provider Options; gcomm.thread_prio

Defines the policy and priority for the gcomm thread.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.0"

Using this option, you can raise the priority of the gcomm thread to a higher level than it normally uses.  You may find this useful in situations where Galera Cluster threads do not receive sufficient CPU time, due to competition with other MySQL threads.  In these cases, when the thread scheduler for the operating system does not run the Galera threads frequently enough, timeouts may occur, causing the node to drop from the cluster.

The format for this option is: ``<policy>:<priority>``.  The priority value is an integer.  The policy value supports the following options:

- ``other`` Designates the default time-sharing scheduling in Linux.  They can run until they are blocked by an I/O request or preempted by higher priorities or superior scheduling designations.

- ``fifo`` Designates first-in out scheduling.  These threads always immediately preempt any currently running other, batch or idle threads.  They can run until they are either blocked by an I/O request or preempted by a FIFO thread of a higher priority.

- ``rr`` Designates round-robin scheduling.  These threads always preempt any currently running other, batch or idle threads.  The scheduler allows these threads to run for a fixed period of a time.  If the thread is still running when this time period is exceeded, they are stopped and moved to the end of the list, allowing another round-robin thread of the same priority to run in their place.  They can otherwise continue to run until they are blocked by an I/O request or are preempted by threads of a higher priority.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcomm.thread_prio=rr:2"


.. _`gcs.fc_debug`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``gcs.fc_limit``

.. index::
   pair: wsrep Provider Options; gcs.fc_limit

Pause replication if recv queue exceeds this number of  writesets. For master-slave setups this number can be increased considerably.

.. csv-table::
   :class: doc-options

   "Default Value", "``16``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_limit=16"


.. _`gcs.fc_master_slave`:
.. rst-class:: rubric-1
.. rubric:: ``gcs.fc_master_slave``

.. index::
   pair: wsrep Provider Options; gcs.fc_master_slave

Defines whether there is only one master node in the group.

.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.fc_master_slave=NO"


.. _`gcs.max_packet_size`:
.. rst-class:: rubric-1
.. rubric:: ``gcs.max_packet_size``

.. index::
   pair: wsrep Provider Options; gcs.max_packet_size

All writesets exceeding that size will be fragmented.

.. csv-table::
   :class: doc-options

   "Default Value", "``32616``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.max_packet_size=32616"


.. _`gcs.max_throttle`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``gcs.sync_donor``

.. index::
   pair: wsrep Provider Options; gcs.sync_donor

Should the rest of the cluster keep in sync with the donor? ``YES`` means that if the donor is blocked by state transfer, the whole cluster is blocked with it.

.. csv-table::
   :class: doc-options

   "Default Value", "``NO``"
   "Dynamic", "No"
   "Initial Version", "1.0"

If you choose to use value ``YES``, it is theoretically possible that the donor node cannot keep up with the rest of the cluster due to the extra load from the SST. If the node lags behind, it may send flow control messages stalling the whole cluster. However, you can monitor this using the :ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>` status variable.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gcs.sync_donor=NO"


.. _`gmcast.listen_addr`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``gmcast.peer_timeout``

.. index::
   pair: wsrep Provider Options; gmcast.peer_timeout

Connection timeout to initiate message relaying.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT3S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.peer_timeout=PT3S"


.. _`gmcast.segment`:
.. rst-class:: rubric-1
.. rubric:: ``gmcast.segment``

.. index::
   pair: wsrep Provider Options; gmcast.segment

Define which network segment this node is in. Optimisations on communication are performed to minimise the amount of traffic between network segments including writeset relaying and IST and SST donor selection.  The :ref:`gmcast.segment <gmcast.segment>` value is an integer from ``0`` to ``255``. By default all nodes are placed in the same segment (``0``).

.. csv-table::
   :class: doc-options

   "Default Value", "``0``"
   "Dynamic", "No"
   "Initial Version", "3.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.segment=0"


.. _`gmcast.time_wait`:
.. rst-class:: rubric-1
.. rubric:: ``gmcast.time_wait``

.. index::
   pair: wsrep Provider Options; gmcast.time_wait

Time to wait until allowing peer declared outside of stable view to reconnect.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT5S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="gmcast.time_wait=PT5S"


.. _`gmcast.version`:
.. rst-class:: rubric-1
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


.. _`ist.recv_addr`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``ist.recv_bind``

.. index::
   pair: wsrep Provider Options; ist.recv_bind

Defines the address that the node binds on for receiving an :term:`Incremental State Transfer`.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "3.16"

This option defines the address to which the node will bind in order to receive Incremental State Transfers.  When this option is not set, it takes its value from :ref:`ist.recv_addr <ist.recv_addr>` or, in the event that that is also not set, from :ref:`wsrep_node_address <wsrep_node_address>`.  You may find it useful when the node runs behind a NAT or in similar cases where the public and private addresses differ.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="ist.recv_bind=192.168.1.1"


.. _`pc.recovery`:
.. rst-class:: rubric-1
.. rubric:: ``pc.recovery``

.. index::
   pair: wsrep Provider Options; pc.recovery
.. index::
   single: gvwstate.dat

When set to ``TRUE``, the node stores the Primary Component state to disk, in the ``gvwstate.dat`` file.  The Primary Component can then recover automatically when all nodes that were part of the last saved state reestablish communications with each other.

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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``pc.announce_timeout``

.. index::
   pair: wsrep Provider Options; pc.announce_timeout

Cluster joining announcements are sent every :math:`\frac{1}{2}` second for this period of time or less if the other nodes are discovered.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT3S``"
   "Dynamic", "No"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.announce_timeout=PT3S"


.. _`pc.checksum`:
.. rst-class:: rubric-1
.. rubric:: ``pc.checksum``

.. index::
   pair: wsrep Provider Options; pc.checksum

Checksum replicated messages.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.checksum=TRUE"


.. _`pc.ignore_sb`:
.. rst-class:: rubric-1
.. rubric:: ``pc.ignore_sb``

.. index::
   pair: wsrep Provider Options; pc.ignore_sb

Should we allow nodes to process updates even in the case of split brain? This is a dangerous setting in multi-master setup, but should simplify things in master-slave cluster (especially if only 2 nodes are used).

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.ignore_sb=FALSE"


.. _`pc.ignore_quorum`:
.. rst-class:: rubric-1
.. rubric:: ``pc.ignore_quorum``

.. index::
   pair: wsrep Provider Options; pc.ignore_quorum

Completely ignore quorum calculations. For example if the master splits from several slaves it still remains operational. Use with extreme caution even in master-slave setups, as slaves will not automatically reconnect to master in this case.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "Yes"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.ignore_quorum=FALSE"


.. _`pc.linger`:
.. rst-class:: rubric-1
.. rubric:: ``pc.linger``

.. index::
   pair: wsrep Provider Options; pc.linger

The period for which the PC protocol waits for the EVS termination.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT2S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.linger=PT2S"


.. _`pc.npvo`:
.. rst-class:: rubric-1
.. rubric:: ``pc.npvo``

.. index::
   pair: Parameters; pc.npvo

If set to ``TRUE``, the more recent primary component overrides older ones in the case of conflicting primaries.

.. csv-table::
   :class: doc-options

   "Default Value", "``FALSE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.npvo=FALSE"


.. _`pc.wait_prim`:
.. rst-class:: rubric-1
.. rubric:: ``pc.wait_prim``

.. index::
   pair: wsrep Provider Options; pc.wait_prim

If set to ``TRUE``, the node waits for the :ref:`pc.wait_prim_timeout <pc.wait_prim_timeout>` time period. Useful to bring up a non-primary component and make it primary with :ref:`pc.bootstrap <pc.bootstrap>`.

.. csv-table::
   :class: doc-options

   "Default Value", "``TRUE``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim=FALSE"


.. _`pc.wait_prim_timeout`:
.. rst-class:: rubric-1
.. rubric:: ``pc.wait_prim_timeout``

.. index::
   pair: wsrep Provider Options; pc.wait_prim_timeout

The period of time to wait for a primary component.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "2.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim_timeout=PT30S"


.. _`pc.weight`:
.. rst-class:: rubric-1
.. rubric:: ``pc.weight``

.. index::
   pair: wsrep Provider Options; pc.weight

As of version 2.4. Node weight for quorum calculation.

.. csv-table::
   :class: doc-options

   "Default Value", "``1``"
   "Dynamic", "Yes"
   "Initial Version", "2.4"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="pc.weight=1"


.. _`pc.version`:
.. rst-class:: rubric-1
.. rubric:: ``pc.version``

.. index::
   pair: wsrep Provider Options; pc.version

This status variable is used to check which pc protocol version is used.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


.. _`protonet.backend`:
.. rst-class:: rubric-1
.. rubric:: ``protonet.backend``

.. index::
   pair: wsrep Provider Options; protonet.backend

Which transport backend to use. Currently only ASIO is supported.

.. csv-table::
   :class: doc-options

   "Default Value", "``asio``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="protonet.backend=asio"


.. _`protonet.version`:
.. rst-class:: rubric-1
.. rubric:: ``protonet.version``

.. index::
   pair: wsrep Provider Options; protonet.version

This status variable is used to check which transport backend protocol version is used.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


.. _`repl.commit_order`:
.. rst-class:: rubric-1
.. rubric:: ``repl.commit_order``

.. index::
   pair: wsrep Provider Options; repl.commit_order

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
.. rst-class:: rubric-1
.. rubric:: ``repl.causal_read_timeout``

.. index::
   pair: wsrep Provider Options; repl.causal_read_timeout

Sometimes causal reads need to timeout.

.. csv-table::
   :class: doc-options

   "Default Value", "``PT30S``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="repl.causal_read_timeout=PT30S"


.. _`repl.key_format`:
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
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
.. rst-class:: rubric-1
.. rubric:: ``socket.recv_buf_size``

.. index::
   pair: wsrep Provider Options;  socket.recv_buf_size

The size of the receive buffer that used on the network sockets between nodes. Galera passes the value to the kernel via the ``SO_RCVBUF`` socket option.

.. csv-table::
   :class: doc-options

   "Default Value", "``212992``"
   "Dynamic", "No"
   "Initial Version", "3.17"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.recv_buf_size=212992"


.. _`socket.ssl_ca`:
.. rst-class:: rubric-1
.. rubric:: ``socket.ssl_ca``

.. index::
   pair: wsrep Provider Options; socket.ssl_ca

Defines the path to the SSL Certificate Authority (CA) file.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the CA file to verify the signature on the certificate.  You can use either an absolute path or one relative to the working directory.  The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options='socket.ssl_ca=/path/to/ca-cert.pem'

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.ssl_cert`:
.. rst-class:: rubric-1
.. rubric:: ``socket.ssl_cert``

.. index::
   pair: wsrep Provider Options; socket.ssl_cert

Defines the path to the :abbr:`SSL (Secure Socket Layer)` certificate.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the certificate as a self-signed public key in encrypting replication traffic over :abbr:`SSL (Secure Socket Layer)`.  You can use either an absolute path or one relative to the working directory.  The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_cert=/path/to/server-cert.pem"

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.checksum`:
.. rst-class:: rubric-1
.. rubric:: ``socket.checksum``

.. index::
   pair: wsrep Provider Options; socket.checksum

Checksum to use on socket layer.

.. csv-table::
   :class: doc-options

   "Default Value", "``1`` (before vs. 3), ``2``"
   "Dynamic", "No"
   "Initial Version", "2.0"

Possible Values;

- ``0`` - disable checksum
- ``1`` - CRC32
- ``2`` - CRC-32C (optimized and potentially HW-accelerated on Intel CPUs)

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.checksum=2"


.. _`socket.ssl_cipher`:
.. rst-class:: rubric-1
.. rubric:: ``socket.ssl_cipher``

.. index::
   pair: wsrep Provider Options; socket.ssl_cipher

Symmetric cipher to use. By default SSL library implementation default cipher is used.

.. csv-table::
   :class: doc-options

   "Default Value", "``AES128-SHA`` (before vs. 3.24), ``system default``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_cipher=AES128-SHA256"


.. _`socket.ssl_compression`:
.. rst-class:: rubric-1
.. rubric:: ``socket.ssl_compression``

.. index::
   pair: wsrep Provider Options; socket.ssl_compression

Whether to enable compression on SSL connections.

.. csv-table::
   :class: doc-options

   "Default Value", "``YES``"
   "Dynamic", "No"
   "Initial Version", "1.0"

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_compression=YES"


.. _`socket.ssl_key`:
.. rst-class:: rubric-1
.. rubric:: ``socket.ssl_key``

.. index::
   pair: wsrep Provider Options; socket.ssl_key

Defines the path to the :abbr:`SSL (Secure Socket Layer)` certificate key.

.. csv-table::
   :class: doc-options

   "Default Value", ""
   "Dynamic", "No"
   "Initial Version", "1.0"

The node uses the certificate key a self-signed private key in encrypting replication traffic over  :abbr:`SSL (Secure Socket Layer)`.  You can use either an absolute path or one relative to the working directory.  The file must use PEM format.

The excerpt below is an example of how this Galera parameter might look in the configuration file:

.. code-block:: ini

   wsrep_provider_options="socket.ssl_key=/path/to/server-key.pem"

For more information on generating :abbr:`SSL (Secure Socket Layer)` certificate files for your cluster, see :doc:`ssl-cert`.


.. _`socket.ssl_password_file`:
.. rst-class:: rubric-1
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

This is useful in master-slave setups.

You can set Galera Cluster parameters through a MySQL client with the following query:

.. code-block:: mysql

	SET GLOBAL wsrep_provider_options="evs.send_window=16";

This query  only changes the :ref:`evs.send_window <evs.send_window>` value.

To check which parameters are used in Galera Cluster, enter the following query:

.. code-block:: mysql

	SHOW VARIABLES LIKE 'wsrep_provider_options';

.. |br| raw:: html

   <br />

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
