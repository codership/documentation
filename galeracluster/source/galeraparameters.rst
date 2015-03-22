==================
 Galera Parameters
==================
.. _`Galera Parameters`:

As of version 0.8, Galera Cluster accepts parameters as semicolon-separated key value pair lists, such as ``key1 = value1; key2 = value2``.  In this way, you can configure an arbitrary number of Galera Cluster parameters in one call. A key consists of parameter group and parameter name::

  <group>.<name>

Where ``<group>`` roughly corresponds to some Galera module.

Table legend:

- **Numeric values** Galera Cluster understands the following numeric modifiers:
  ``K``, ``M``, ``G``, ``T`` standing for |210|, |220|, |230| and |240| respectively.

- **Boolean values** Galera Cluster accepts the following boolean values: ``0``, ``1``, ``YES``, ``NO``, ``TRUE``, ``FALSE``, ``ON``, ``OFF``.

- Time periods must be expressed in the ISO8601 format. See also the examples below.

- **T** indicates parameters that are strictly for use in troubleshooting problems.  You should not implement these in production environments.

.. |210| replace:: 2\ :sup:`10`\
.. |220| replace:: 2\ :sup:`20`\
.. |230| replace:: 2\ :sup:`30`\
.. |240| replace:: 2\ :sup:`40`\

+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| Parameter                             | Default               |  Introduced           | Deprecated         | Dynamic  |
+=======================================+=======================+=======================+====================+==========+
| :ref:`base_host                       | detected network      |                       |                    |          |
| <base_host>`                          | address               |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`base_port                       | ``4567``              |                       |                    |          |
| <base_port>`                          |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`cert.log_conflicts              | ``NO``                | 2.0                   | n/a                | Yes      |
| <cert.log_conflicts>`                 |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`debug                           | ``NO``                | 2.0                   | n/a                | Yes      |
| <debug>`                              |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.auto_evict <evs.auto_evict>`| ``0``                 | 3.8                   | n/a                | No       |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.causal_keepalive_period     |                       | 1.0                   | n/a                | No       |
| <evs.causal_keepalive_period>`        |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.consensus_timeout           | ``PT30S``             | 1.0                   | Yes, as of 2.0     | No       |
| <evs.consensus_timeout>` :sup:`T`     |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.debug_log_mask              | ``0x1``               | 1.0                   | n/a                | Yes      |
| <evs.debug_log_mask>`                 |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.delayed_keep_period         | ``PT30S``             | 3.8                   | n/a                | No       |
| <evs.delayed_keep_period>`            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.delayed_margin              | ``PT1S``              | 3.8                   | n/a                | No       |
| <evs.delayed_margin>`                 |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.evict <evs.evict>`          |                       | 3.8                   | n/a                | No       |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.inactive_check_period       | ``PT1S``              | 1.0                   | n/a                | No       |
| <evs.inactive_check_period>`          |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.inactive_timeout            | ``PT15S``             | 1.0                   | n/a                | No       |
| <evs.inactive_timeout>`               |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.info_log_mask               | ``0``                 | 1.0                   | n/a                | No       |
| <evs.info_log_mask>`                  |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.install_timeout             | ``PT15S``             | 1.0                   | n/a                | Yes      |
| <evs.install_timeout>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.join_retrans_period         | ``PT1S``              | 1.0                   | n/a                | Yes      |
| <evs.join_retrans_period>`            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.keepalive_period            | ``PT1S``              | 1.0                   | n/a                | No       |
| <evs.keepalive_period>`               |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.max_install_timeouts        | ``1``                 | 1.0                   | n/a                | No       |
| <evs.max_install_timeouts>`           |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.send_window                 | ``4``                 | 1.0                   | n/a                | Yes      |
| <evs.send_window>`                    |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.stats_report_period         | ``PT1M``              | 1.0                   | n/a                | No       |
| <evs.stats_report_period>`            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.suspect_timeout             | ``PT5S``              | 1.0                   | n/a                | No       |
| <evs.suspect_timeout>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.use_aggregate               | ``TRUE``              | 1.0                   | n/a                | No       |
| <evs.use_aggregate>`                  |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.user_send_window            | ``2``                 | 1.0                   | n/a                | Yes      |
| <evs.user_send_window>`               |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.view_forget_timeout         | ``PT5M``              | 1.0                   | n/a                | No       |
| <evs.view_forget_timeout>`            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`evs.version                     | ``0``                 | 1.0                   |                    | No       |
| <evs.version>` :sup:`T`               |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.dir                      | working directory     | 1.0                   | n/a                | No       |
| <gcache.dir>`                         |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.name                     | ``galera.cache``      | 1.0                   | n/a                | No       |
| <gcache.name>`                        |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.size                     | ``128Mb``             | 1.0                   | n/a                | No       |
| <gcache.size>`                        |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.page_size                | ``128Mb``             | 1.0                   | n/a                | No       |
| <gcache.page_size>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.keep_pages_size          | ``0``                 | 1.0                   | n/a                | No       |
| <gcache.keep_pages_size>`             |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcache.mem_size                 | ``0``                 | 1.0                   | n/a                | No       |
| <gcache.mem_size>`                    |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.fc_debug                    | ``0``                 | 1.0                   | n/a                | No       |
| <gcs.fc_debug>`                       |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.fc_factor                   | ``0.5``               | 1.0                   | n/a                | Yes      |
| <gcs.fc_factor>`                      |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.fc_limit                    | ``16``                | 1.0                   | n/a                | Yes      |
| <gcs.fc_limit>`                       |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.fc_master_slave             | ``NO``                | 1.0                   | n/a                | No       |
| <gcs.fc_master_slave>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.max_packet_size             | ``32616``             | 1.0                   | n/a                | No       |
| <gcs.max_packet_size>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.max_throttle                | ``0.25``              | 1.0                   | n/a                | No       |
| <gcs.max_throttle>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.recv_q_hard_limit           | ``LLONG_MAX``         | 1.0                   | n/a                | No       |
| <gcs.recv_q_hard_limit>`              |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.recv_q_soft_limit           | ``0.25``              | 1.0                   | n/a                | No       |
| <gcs.recv_q_soft_limit>`              |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gcs.sync_donor                  | ``NO``                | 1.0                   | n/a                | No       |
| <gcs.sync_donor>`                     |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.listen_addr              | ``tcp://0.0.0.0:4567``| 1.0                   | n/a                | No       |
| <gmcast.listen_addr>`                 |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.mcast_addr               |                       | 1.0                   | n/a                | No       |
| <gmcast.mcast_addr>`                  |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.mcast_ttl                | ``1``                 | 1.0                   | n/a                | No       |
| <gmcast.mcast_ttl>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.peer_timeout             | ``PT3S``              | 1.0                   | n/a                | No       |
| <gmcast.peer_timeout>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.segment                  | ``0``                 | 3.0                   | n/a                | No       |
| <gmcast.segment>`                     |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.time_wait                | ``PT5S``              | 1.0                   | n/a                | No       |
| <gmcast.time_wait>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`gmcast.version                  | n/a                   |                       |                    |          |
| <gmcast.version>` :sup:`T`            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`ist.recv_addr                   |                       | 1.0                   | n/a                | No       |
| <ist.recv_addr>`                      |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.recovery                     | ``TRUE``              | 3.0                   | n/a                | No       |
| <pc.recovery>`                        |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.bootstrap                    | n/a                   | 2.0                   | n/a                | Yes      |
| <pc.bootstrap>`                       |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.announce_timeout             | ``PT3S``              | 2.0                   | n/a                | No       |
| <pc.announce_timeout>`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.checksum                     | ``TRUE``              | 1.0                   | n/a                | No       |
| <pc.checksum>`                        |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.ignore_sb                    | ``FALSE``             | 1.0                   | n/a                | Yes      | 
| <pc.ignore_sb>`                       |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.ignore_quorum                | ``FALSE``             | 1.0                   | n/a                | Yes      |
| <pc.ignore_quorum>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.linger                       | ``PT2S``              | 1.0                   | n/a                | No       |
| <pc.linger>`                          |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.npvo                         | ``FALSE``             | 1.0                   | n/a                | No       |
| <pc.npvo>`                            |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.wait_prim                    | ``FALSE``             | 1.0                   | n/a                | No       |
| <pc.wait_prim>`                       |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.wait_prim_timeout            | ``P30S``              | 2.0                   | n/a                | No       |
| <pc.wait_prim_timeout>`               |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.weight                       | ``1``                 | 2.4                   | n/a                | Yes      |
| <pc.weight>`                          |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`pc.version                      | n/a                   |                       |                    |          |
| <pc.version>` :sup:`T`                |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`protonet.backend                | ``asio``              | 1.0                   | n/a                | No       |
| <protonet.backend>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`protonet.version                | n/a                   |                       |                    |          |
| <protonet.version>` :sup:`T`          |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`repl.commit_order               | ``3``                 | 1.0                   | n/a                | No       |
| <repl.commit_order>`                  |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`repl.causal_read_timeout        | ``PT30S``             | 1.0                   | n/a                | No       |
| <repl.causal_read_timeout>`           |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`repl.key_format                 | ``FLAT8``             | 3.0                   | n/a                | No       |
| <repl.key_format>`                    |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`repl.max_ws_size                | ``2147483647``        | 3.0                   | n/a                | No       |
| <repl.max_ws_size>`                   |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`repl.proto_max                  | ``5``                 | 2.0                   | n/a                | No       |
| <repl.proto_max>`                     |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`socket.ssl_cert                 |                       | 1.0                   | n/a                | No       |
| <socket.ssl_cert>`                    |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`socket.ssl_key                  |                       | 1.0                   | n/a                | No       |
| <socket.ssl_key>`                     |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`socket.ssl_compression          | ``YES``               | 1.0                   | n/a                | No       |
| <socket.ssl_compression>`             |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`socket.ssl_cipher               | ``AES128-SHA``        | 1.0                   | n/a                | No       |
| <socket.ssl_cipher>`                  |                       |                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+
| :ref:`socket.checksum                 | ``1`` (for version 2) | 2.0                   | n/a                | No       |
| <socket.checksum>`                    |                       |                       |                    |          |
|                                       | ``2`` (for version 3+)|                       |                    |          |
+---------------------------------------+-----------------------+-----------------------+--------------------+----------+


.. rubric:: ``base_host``
.. _`base_host`:
.. index::
   pair: Parameters; base_host

Global variable for internal use. 

.. warning:: Do not manually set this variable.

+-----------------------+---------+-----------+-------------+
| Default Values        | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| detected network      |         |            |            |
| address               |         |            |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``base_port``
.. _`base_port`:
.. index::
   pair: Parameters; base_port

Global variable for internal use. 

.. warning:: Do not manually set this variable.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``4567``              |         |            |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``cert.log_conflicts``
.. _`cert.log_conflicts`:
.. index::
   pair: Parameters; cert.log_conflicts

Log details of certification failures.

.. code-block:: ini

   wsrep_provider_options="cert.log_conflicts=NO"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``NO``                | Yes     | 2.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``debug``
.. _`debug`:
.. index::
   pair: Parameters; debug

Enable debugging.

.. code-block:: ini

   wsrep_provider_options="debug=NO"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``NO``                | Yes     | 2.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.auto_evict``
.. _`evs.auto_evict`:
.. index::
   pair: Parameters; evs.auto_evict

Defines the number of entries allowed for a delayed node before this node triggers Auto Eviction.  Setting this to ``0`` disables the Auto Eviction protocol on this node, though the node continues to monitor cluster node response times.

.. code-block:: ini

   wsrep_provider_options="evs.auto_evict=5"

**Default Value**: ``0``
   
.. seealso:: For more information on the Auto Eviction process, see :doc:`autoeviction`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 |  No     | 3.8        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.causal_keepalive_period``
.. _`evs.causal_keepalive_period`:
.. index::
   pair: Parameters; evs.causal_keepalive_period

For developer use only. Defaults to ``evs.keepalive_period``.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``evs.consensus_timeout``
.. _`evs.consensus_timeout`:
.. index::
   pair: Parameters; evs.consensus_timeout

Timeout on reaching the consensus about cluster membership.

.. code-block:: ini

   wsrep_provider_options="evs.consensus_timeout=PT30S"

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.

.. seealso:: This feature has been **deprecated**. It is succeeded by :ref:`evs.install_timeout <evs.install_timeout>`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT30S``             | No      | 1.0        | 2.0        |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.debug_log_mask``
.. _`evs.debug_log_mask`:
.. index::
   pair: Parameters; evs.debug_log_mask

Control EVS debug logging, only effective when ``wsrep_debug`` is in use.

.. code-block:: ini

   wsrep_provider_options="evs.debug_log_mask=0x1"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0x1``               | Yes     |  1.0       |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.delayed_keep_period``
.. _`evs.delayed_keep_period`:
.. index::
   pair: Parameters; evs.delayed_keep_period

Defines the time period cluster nodes must remain responsive before this node removes one entry from the delayed list.  The number of entries on the delayed list depends on how long the delayed node was unresponsive.

.. code-block:: ini

   wsrep_provider_options="evs.delayed_keep_period=PT45S"

.. seealso:: For more information on the delayed list and the Auto Eviction process, see :doc:`autoeviction`.
   
+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT30S``             | No      | 3.8        |            |
+-----------------------+---------+------------+------------+



   
.. rubric:: ``evs.delayed_margin``
.. _`evs.delayed_margin`:
.. index::
   pair: Parameters; evs.delayed_margin

Defines the time period that cluster nodes can delay responses from expectations before this node adds them to the delayed list.  You must set this parameter to a value higher than the round-trip delay time (RTT) between the nodes.

.. code-block:: ini

   wsrep_provider_options="evs.delayed_margin=PT5S"

**Default Value**: ``PT1S``

.. seealso:: For more information on the delayed list and the Auto Eviction process, see :doc:`autoeviction`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT1S``              | No      | 3.8        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``evs.evict``
.. _`evs.evict`:
.. index::
   pair:: Parameters; evs.evict

Defines the point at which the cluster triggers manual eviction to a certain node value.  Setting this parameter as an empty string causes it to clear the eviction list on the node where it is set.

.. seealso:: For more information on the eviction and Auto Eviction process, see :doc:`autoeviction`.
   
+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 3.8        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.inactive_check_period``
.. _`evs.inactive_check_period`:
.. index::
   pair: Parameters; evs.inactive_check_period

How often to check for peer inactivity.

.. code-block:: ini

   wsrep_provider_options="evs.inactive_check_period=PT1S"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT1S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``evs.inactive_timeout``
.. _`evs.inactive_timeout`:
.. index::
   pair: Parameters; evs.inactive_timeout

Hard limit on the inactivity period, after which the node is pronounced dead.

.. code-block:: ini

   wsrep_provider_options="evs.inactive_timeout=PT15S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT15S``             | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.info_log_mask``
.. _`evs.info_log_mask`:
.. index::
   pair: Parameters; evs.info_log_mask

Control extra EVS info logging. Bits:
 
- ``0x1`` Provides extra view change info.
- ``0x2`` Provides extra state change info
- ``0x4`` Provides statistics
- ``0x8`` Provides profiling (only in builds with profiling enabled)

.. code-block:: ini

   wsrep_provider_options="evs.info_log_mask=0x4"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``evs.install_timeout``
.. _`evs.install_timeout`:
.. index::
   pair: Parameters; evs.install_timeout

Timeout on waiting for install message acknowledgments. 

.. code-block:: ini

   wsrep_provider_options="evs.install_timeout=PT15S"


.. seealso:: This parameter is the successor to :ref:`evs.consensus_timeout <evs.consensus_timeout>`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT15S``             | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.join_retrans_period``
.. _`evs.join_retrans_period`:
.. index::
   pair: Parameters; evs.join_retrans_period

How often to retransmit EVS join messages when forming the cluster membership.

.. code-block:: ini

   wsrep_provider_options="evs.join_retrans_period=PT1S"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT1S``              |  Yes    | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.keepalive_period``
.. _`evs.keepalive_period`:
.. index::
   pair: Parameters; evs.keepalive_period

How often to emit keepalive beacons (in the absence of any other traffic).

.. code-block:: ini

   wsrep_provider_options="evs.keepalive_period=PT1S"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT1S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.max_install_timeouts``
.. _`evs.max_install_timeouts`:
.. index::
   pair: Parameters; evs.max_install_timeouts

How many membership install rounds to try before giving up (total rounds will be ``evs.max_install_timeouts`` + 2).

.. code-block:: ini

   wsrep_provider_options="evs.max_install_timeouts=1"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``1``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.send_window``
.. _`evs.send_window`:
.. index::
   pair: Parameters; evs.send_window

Maximum packets in replication at a time. For WAN setups may be set considerably higher, e.g. 512.  Must be no less than ``evs.user_send_window``.  If you must use other that the default value, we recommend using double the ``evs.user_send_window`` value.

.. code-block:: ini

   wsrep_provider_options="evs.send_window=4"

.. seealso:: :ref:`evs.user_send_window <evs.user_send_window>`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``4``                 | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``evs.stats_report_period``
.. _`evs.stats_report_period`:
.. index::
   pair: Parameters; evs.stats_report_period

Control period of EVS statistics reporting.  The node is pronounced dead.

.. code-block:: ini

   wsrep_provider_options="evs.stats_report_period=PT1M"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT1M``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.suspect_timeout``
.. _`evs.suspect_timeout`:
.. index::
   pair: Parameters; evs.suspect_timeout

Inactivity period after which the node is *suspected* to be dead. If all remaining nodes agree on that, the node is dropped out of cluster before ``evs.inactive_timeout`` is reached.

.. code-block:: ini

   wsrep_provider_options="evs.suspect_timeout=PT5S"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT5S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.use_aggregate``
.. _`evs.use_aggregate`:
.. index::
   pair: Parameters; evs.use_aggregate

Aggregate small packets into one, when possible.

.. code-block:: ini

   wsrep_provider_options="evs.use_aggregate=TRUE"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``TRUE``              | No      | 1.         |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.user_send_window``
.. _`evs.user_send_window`:
.. index::
   pair: Parameters; evs.user_send_window

Maximum data packets in replication at a time. For WAN setups, this value can be set considerably higher, to, for example, 512.

.. code-block:: ini

   wsrep_provider_options="evs.user_send_window=2"

.. seealso:: :ref:`evs.send_window <evs.send_window>`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``2``                 | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``evs.view_forget_timeout``
.. _`evs.view_forget_timeout`:
.. index::
   pair: Parameters; evs.view_forget_timeout

Drop past views from the view history after this timeout.

.. code-block:: ini

   wsrep_provider_options="evs.view_forget_timeout=PT5M"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT5M``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``evs.version``
.. _`evs.version`:
.. index::
   pair: Parameters; evs.version

This status variable is used to check which ``evs`` protocol version is used. 

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcache.dir``
.. _`gcache.dir`:
.. index::
   pair: Parameters; gcache.dir

Directory where GCache should place its files.  Defaults to the working directory. 


+--------------------------+---------+------------+------------+
| Default Value            | Dynamic | Introduced | Deprecated |
+==========================+=========+============+============+
| ``/path/to/working_dir`` | No      | 1.0        |            |
+--------------------------+---------+------------+------------+



.. rubric:: ``gcache.name``
.. _`gcache.name`:
.. index::
   pair: Parameters; gcache.name

Name of the ring buffer storage file. 

.. code-block:: ini

   wsrep_provider_options="gcache.name=galera.cache"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``galera.cache``      | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gcache.size``
.. _`gcache.size`:
.. index::
   pair: Parameters; gcache.size

Size of the persistent on-disk ring buffer storage. This will be preallocated on start up. 

.. code-block:: ini

   wsrep_provider_options="gcache.size=128Mb"

The buffer file name is ``galera.cache`` by default.

.. seealso:: For more information on customizing the write-set cache, see :ref:`Performance <customizing-gcache-size>`.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``128M``              |  No     | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``gcache.page_size``
.. _`gcache.page_size`:
.. index::
   pair: Parameters; gcache.page_size

Size of the page files in page storage. The limit on overall page storage is the size of the disk.  Pages are prefixed by ``gcache.page``.

.. code-block:: ini

   wsrep_provider_options="gcache.page_size=128Mb"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``128M``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcache.keep_pages_size``
.. _`gcache.keep_pages_size`:
.. index::
   pair: Parameters; gcache.keep_pages_size

Total size of the page storage pages to keep for caching purposes. If only page storage is enabled, one page is always present. 

.. code-block:: ini

   wsrep_provider_options="gcache.keep_pages_size=0"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcache.mem_size``
.. _`gcache.mem_size`:
.. index::
   pair: Parameters; gcache.mem_size

Defines the maximum size for the ``malloc()`` store.  That is, how much :abbr:`RAM (Random Access Memory)` your system has available.
   
.. code-block:: ini

   wsrep_provider_options="gcache.mem_size=0"

.. warning:: This parameter is for use on systems with spare memory.  You should not use it otherwise, as it may lead to unexpected results.

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+

   

.. rubric:: ``gcs.fc_debug``
.. _`gcs.fc_debug`:
.. index::
   pair: Parameters; gcs.fc_debug

Post debug statistics about SST flow every this number of writesets. 

.. code-block:: ini

   wsrep_provider_options="gcs.fc_debug=0"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcs.fc_factor``
.. _`gcs.fc_factor`:
.. index::
   pair: Parameters; gcs.fc_factor

Resume replication after recv queue drops below this fraction of ``gcs.fc_limit``.

.. code-block:: ini

   wsrep_provider_options="gcs.fc_factor=0.5"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0.5``               | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcs.fc_limit``
.. _`gcs.fc_limit`:
.. index::
   pair: Parameters; gcs.fc_limit

Pause replication if recv queue exceeds this number of  writesets. For master-slave setups this number can be increased considerably.

.. code-block:: ini

   wsrep_provider_options="gcs.fc_limit=16"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``16``                | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gcs.fc_master_slave``
.. _`gcs.fc_master_slave`:
.. index::
   pair: Parameters; gcs.fc_master_slave

Defines whether there is only one master node in the group.
   
.. code-block:: ini

   wsrep_provider_options="gcs.fc_master_slave=NO"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``NO``                | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcs.max_packet_size``
.. _`gcs.max_packet_size`:
.. index::
   pair: Parameters; gcs.max_packet_size

All writesets exceeding that size will be fragmented.

.. code-block:: ini

   wsrep_provider_options="gcs.max_packet_size=32616"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``32616``             | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gcs.max_throttle``
.. _`gcs.max_throttle`:

.. index::
   pair: Parameters; gcs.max_throttle

How much to throttle replication rate during state transfer (to avoid running out of memory). Set the value to 0.0 if stopping replication is acceptable for completing state transfer. 

.. code-block:: ini

   wsrep_provider_options="gcs.max_throttle=0.25"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0.25``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gcs.recv_q_hard_limit``
.. _`gcs.recv_q_hard_limit`:
.. index::
   pair: Parameters; gcs.recv_q_hard_limit

Maximum allowed size of recv queue. This should normally be half of (RAM + swap). If this limit is exceeded, Galera Cluster will abort the server.

.. code-block:: ini

   wsrep_provider_options="gcs.recv_q_hard_limit=LLONG_MAX"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``LLONG_MAX``         | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gcs.recv_q_soft_limit``
.. _`gcs.recv_q_soft_limit`:
.. index::
   pair: Parameters; gcs.recv_q_soft_limit

The fraction of :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` after which replication rate will be throttled.

.. code-block:: ini

   wsrep_provider_options="gcs.recv_q_soft_limit=0.25"

The degree of throttling is a linear function of recv queue size and goes from 1.0 (``full rate``)
at :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` to :ref:`gcs.max_throttle <gcs.max_throttle>` at :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` Note that ``full rate``, as estimated between 0 and :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` is a very imprecise estimate of a regular replication rate. 


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0.25``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``gcs.sync_donor``
.. _`gcs.sync_donor`:
.. index::
   pair: Parameters; gcs.sync_donor

Should the rest of the cluster keep in sync with the donor? ``YES`` means that if the donor is blocked by state transfer, the whole cluster is blocked with it.

.. code-block:: ini

   wsrep_provider_options="gcs.sync_donor=NO"

If you choose to use value ``YES``, it is theoretically possible that the donor node cannot keep up with the rest of the cluster due to the extra load from the SST. If the node lags behind, it may send flow control messages stalling the whole cluster. However, you can monitor this using the :ref:`wsrep_flow_control_paused <wsrep_flow_control_paused>` status variable.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``NO``                | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gmcast.listen_addr``
.. _`gmcast.listen_addr`:
.. index::
   pair: Parameters; gmcast.listen_addr

Address at which *Galera Cluster* listens to connections from other nodes. By default the port to listen at is taken from the connection address. This setting can be used to overwrite that.

.. code-block:: ini

   wsrep_provider_options="gmcast.listen_addr=tcp://0.0.0.0:4567"



+------------------------+---------+------------+------------+
| Default Value          | Dynamic | Introduced | Deprecated |
+========================+=========+============+============+
| ``tcp://0.0.0.0"4567`` | No      | 1.0        |            |
+------------------------+---------+------------+------------+



.. rubric:: ``gmcast.mcast_addr``
.. _`gmcast.mcast_addr`:
.. index::
   pair: Parameters; gmcast.mcast_addr

If set, UDP multicast will be used for replication, for example:

.. code-block:: ini

    wsrep_provider_options="gmcast.mcast_addr=239.192.0.11"

The value must be the same on all nodes.

If you are planning to build a large cluster, we recommend using UDP.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``gmcast.mcast_ttl``
.. _`gmcast.mcast_ttl`:
.. index::
   pair: Parameters; gmcast.mcast_ttl

Time to live value for multicast packets.

.. code-block:: ini
	
   wsrep_provider_options="gmcast.mcast_ttl=1"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``1``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gmcast.peer_timeout``
.. _`gmcast.peer_timeout`:
.. index::
   pair: Parameters; gmcast.peer_timeout

Connection timeout to initiate message relaying.

.. code-block:: ini

   wsrep_provider_options="gmcast.peer_timeout=PT3S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT3S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+

.. rubric:: ``gmcast.segment``
.. _`gmcast.segment`:
.. index::
   pair: Parameters; gmcast.segment

Define which network segment this node is in. Optimisations on communication are performed to minimise the amount of traffic between network segments including writeset relaying and IST and SST donor selection.  The :ref:`gmcast.segment <gmcast.segment>` value is an integer from ``0`` to ``255``. By default all nodes are placed in the same segment (``0``).

.. code-block:: ini

   wsrep_provider_options="gmcast.segment=0"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``0``                 | No      | 3.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gmcast.time_wait``
.. _`gmcast.time_wait`:
.. index::
   pair: Parameters; gmcast.time_wait

Time to wait until allowing peer declared outside of stable view to reconnect.

.. code-block:: ini

   wsrep_provider_options="gmcast.time_wait=PT5S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT5S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``gmcast.version``
.. _`gmcast.version`:
.. index::
   pair: Parameters; gmcast.version

This status variable is used to check which gmcast protocol version is used.

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``ist.recv_addr``
.. _`ist.recv_addr`:
.. index::
   pair: Parameters; ist.recv_addr

As of 2.0. Address to listen for Incremental State Transfer. By default this is the ``<address>:<port+1>`` from :ref:`wsrep_node_address <wsrep_node_address>`.

.. code-block:: ini

   wsrep_provider_options="ist.recv_addr=192.168.1.1"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.recovery``
.. _`pc.recovery`:
.. index::
   pair: Parameters; pc.recovery
.. index::
   pair: Parameters; gvwstate.dat


When set to ``TRUE``, the node stores the Primary Component state to disk, in the ``gvwstate.dat`` file.  The Primary Component can then recover automatically when all nodes that were part of the last saved state reestablish communications with each other.  

.. code-block:: ini

   wsrep_provider_options="pc.recovery=TRUE"

This allows for:

- Automatic recovery from full cluster crashes, such as in the case of a data center power outage.

- Graceful full cluster restarts without the need for explicitly bootstrapping a new Primary Component.


.. note:: In the event that the wsrep position differs between nodes, recovery also requires a full State Snapshot Transfer.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``TRUE``              | No      | 3.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.bootstrap``
.. _`pc.bootstrap`:
.. index::
   pair: Parameters; pc.bootstrap

If you set this value to ``TRUE`` is a signal to turn a ``NON-PRIMARY`` component into ``PRIMARY``.

.. code-block:: ini

   wsrep_provider_options="pc.bootstrap=TRUE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | Yes     | 2.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.announce_timeout``
.. _`pc.announce_timeout`:
.. index::
   pair: Parameters; pc.announce_timeout

Cluster joining announcements are sent every :math:`\frac{1}{2}` second for this period of time or less if the other nodes are discovered.

.. code-block:: ini

   wsrep_provider_options="pc.announce_timeout=PT3S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT3S``              | No      | 2.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``pc.checksum``
.. _`pc.checksum`:
.. index::
   pair: Parameters; pc.checksum

Checksum replicated messages.

.. code-block:: ini

   wsrep_provider_options="pc.checksum=TRUE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``TRUE``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``pc.ignore_sb``
.. _`pc.ignore_sb`:
.. index::
   pair: Parameters; pc.ignore_sb

Should we allow nodes to process updates even in the case of split brain? This is a dangerous setting in multi-master setup, but should simplify things in master-slave cluster (especially if only 2 nodes are used).

.. code-block:: ini

   wsrep_provider_options="pc.ignore_sb=FALSE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``FALSE``             | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``pc.ignore_quorum``
.. _`pc.ignore_quorum`:
.. index::
   pair: Parameters; pc.ignore_quorum

Completely ignore quorum calculations. For example if the master splits from several slaves it still remains operational. Use with extreme caution even in master-slave setups, as slaves will not automatically reconnect to master in this case.

.. code-block:: ini

   wsrep_provider_options="pc.ignore_quorum=FALSE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``FALSE``             | Yes     | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.linger``
.. _`pc.linger`:
.. index::
   pair: Parameters; pc.linger

The period for which the PC protocol waits for the EVS termination.

.. code-block:: ini

   wsrep_provider_options="pc.linger=PT2S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT2S``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``pc.npvo``
.. _`pc.npvo`:
.. index::
   pair: Parameters; pc.npvo

If set to ``TRUE``, the more recent primary component overrides older ones in the case of conflicting primaries. 

.. code-block:: ini

   wsrep_provider_options="pc.npvo=FALSE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``FALSE``             | No      | 1.0        |            |
+-----------------------+---------+------------+------------+

.. rubric:: ``pc.wait_prim``
.. _`pc.wait_prim`:
.. index::
   pair: Parameters; pc.wait_prim

If set to ``TRUE``, the node waits for the :ref:`pc.wait_prim_timeout <pc.wait_prim_timeout>` time period. Useful to bring up a non-primary component and make it primary with :ref:`pc.bootstrap <pc.bootstrap>`.

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim=FALSE"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``FALSE``             | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``pc.wait_prim_timeout``
.. _`pc.wait_prim_timeout`:
.. index::
   pair: Parameters; pc.wait_prim_timeout

The period of time to wait for a primary component.

.. code-block:: ini

   wsrep_provider_options="pc.wait_prim_timeout=PT30S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT30S``             | No      | 2.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.weight``
.. _`pc.weight`:
.. index::
   pair: Parameters; pc.weight

As of version 2.4. Node weight for quorum calculation.

.. code-block:: ini

   wsrep_provider_options="pc.weight=1"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``1``                 | Yes     | 2.4        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``pc.version``
.. _`pc.version`:
.. index::
   pair: Parameters; pc.version

This status variable is used to check which pc protocol version is used. 

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``protonet.backend``
.. _`protonet.backend`:
.. index::
   pair: Parameters; protonet.backend

Which transport backend to use. Currently only ASIO is supported.

.. code-block:: ini

   wsrep_provider_options="protonet.backend=asio"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``asio``              | No      | 1.0        |            |
+-----------------------+---------+------------+------------+

.. rubric:: ``protonet.version``
.. _`protonet.version`:
.. index::
   pair: Parameters; protonet.version

This status variable is used to check which transport backend protocol version is used. 

This variable is mostly used for troubleshooting purposes and should not be implemented in a production environment.


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``repl.commit_order``
.. _`repl.commit_order`:
.. index::
   pair: Parameters; repl.commit_order

Whether to allow Out-Of-Order committing (improves parallel applying performance). 

.. code-block:: ini

   wsrep_provider_options="repl.commit_order=2"

Possible settings:

- ``0`` or ``BYPASS`` All commit order monitoring is switched off (useful for measuring performance penalty).

- ``1`` or ``OOOC`` Allows out of order committing for all transactions.

- ``2`` or ``LOCAL_OOOC``  Allows out of order committing only for local transactions.

- ``3`` or ``NO_OOOC`` No out of order committing is allowed (strict total order committing)


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``3``                 | No      | 1.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``repl.causal_read_timeout``
.. _`repl.causal_read_timeout`:
.. index::
   pair: Parameters; repl.causal_read_timeout

Sometimes causal reads need to timeout.

.. code-block:: ini

   wsrep_provider_options="repl.causal_read_timeout=PT30S"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``PT30S``             | No      | 1.0        |            |
+-----------------------+---------+------------+------------+

.. rubric:: ``repl.key_format``
.. _`repl.key_format`:
.. index::
   pair: Parameters; repl.key_format

The hash size to use for key formats (in bytes). An ``A`` suffix annotates the version.

.. code-block:: ini

   wsrep_provider_options="repl.key_format=FLAT8"

Possible settings:

- ``FLAT8``
- ``FLAT8A``
- ``FLAT16``
- ``FLAT16A``


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``FLAT8``             | No      | 3.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``repl.max_ws_size``
.. _`repl.max_ws_size`:
.. index::
   pair: Parameters; repl.max_ws_size

The maximum size of a write-set in bytes. This is limited to 2G.

.. code-block:: ini

   wsrep_provider_options="repl.max_ws_size=2147483647"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``2147483647``        | No      | 3.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``repl.proto_max``
.. _`repl.proto_max`:
.. index::
   pair: Parameters; repl.proto_max

The maximum protocol version in replication. Changes to this parameter will only take effect after a provider restart.

.. code-block:: ini

   wsrep_provider_options="repl.proto_max=5"

+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``5``                 | No      | 2.0        |            |
+-----------------------+---------+------------+------------+


.. rubric:: ``socket.ssl_cert``
.. _`socket.ssl_cert`:
.. index::
   pair: Parameters; socket.ssl_cert

A path (absolute or relative to the working directory )to an SSL certificate (in PEM format). 


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``socket.ssl_key``
.. _`socket.ssl_key`:
.. index::
   pair: Parameters; socket.ssl_key

A path (absolute or relative to the working directory to a private key for a certificate (in PEM format).


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
|                       | No      | 1.0        |            |
+-----------------------+---------+------------+------------+




.. rubric:: ``socket.ssl_compression``
.. _`socket.ssl_compression`:
.. index::
   pair: Parameters; socket.ssl_compression

Whether to enable compression on SSL connections.

.. code-block:: ini

   wsrep_provider_options="socket.ssl_compression=YES"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``YES``               | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``socket.ssl_cipher``
.. _`socket.ssl_cipher`:
.. index::
   pair: Parameters; socket.ssl_cipher

Symmetric cipher to use. AES128 is used by default it is considerably faster and no less secure than AES256.

.. code-block:: ini

   wsrep_provider_options="socket.ssl_cipher=AES128-SHA"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| ``AES128-SHA``        | No      | 1.0        |            |
+-----------------------+---------+------------+------------+



.. rubric:: ``socket.checksum``
.. _`socket.checksum`:
.. index::
   pair: Parameters; socket.checksum

Checksum to use on socket layer:

- ``0`` - disable checksum
- ``1`` - CRC32
- ``2`` - CRC-32C (optimized and potentially HW-accelerated on Intel CPUs)

.. code-block:: ini

   wsrep_provider_options="socket.checksum=2"


+-----------------------+---------+------------+------------+
| Default Value         | Dynamic | Introduced | Deprecated |
+=======================+=========+============+============+
| version 1 : ``1``     | No      | 2.0        |            |
+-----------------------+---------+------------+------------+
| version 3+: ``2``     |         |            |            |
+-----------------------+---------+------------+------------+




-------------------------------------
 Setting Galera Parameters in MySQL
-------------------------------------
.. _`Setting Galera Parameters in MySQL`:

.. index::
   pair: Parameters; Setting
.. index::
   pair: Parameters; Checking
   
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

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
