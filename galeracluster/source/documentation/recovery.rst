.. meta::
   :title: Node Failure and Recovery in Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, split-brain, recovery
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

      - :ref:`evs.consensus_timeout <evs.consensus_timeout>`
      - :ref:`evs.inactive_check_period <evs.inactive_check_period>`
      - :ref:`evs.inactive_timeout <evs.inactive_timeout>`
      - :ref:`evs.keepalive_period <evs.keepalive_period>`
      - :ref:`evs.suspect_timeout <evs.suspect_timeout>`
      - :doc:`Monitoring the Cluster <monitoring-cluster>`
      - :doc:`Notification Command <notification-cmd>`
      - :ref:`wsrep_local_state <wsrep_local_state>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`recovery`:

==================================
Node Failure and Recovery
==================================

Individual nodes fail to operate when they lose touch with the cluster.  This can occur due to various reasons.  For instance, in the event of hardware failure or software crash, the loss of network connectivity or the failure of a state transfer.  Anything that prevents the node from communicating with the cluster is generalized behind the concept of node failure.  Understanding how nodes fail will help in planning for their recovery.


.. _`single-node-failure-detection`:
.. rst-class:: rubric-2
.. rubric:: Detecting Single Node Failures

.. index::
   pair: Parameters; evs.keepalive_period
.. index::
   pair: Parameters; evs.inactive_check_period
.. index::
   pair: Parameters; evs.suspect_timeout
.. index::
   pair: Parameters; evs.inactive_timeout
.. index::
   pair: Parameters; evs.consensus_timeout

When a node fails the only sign is the loss of connection to the node processes as seen by other nodes.  Thus nodes are considered failed when they lose membership with the cluster's :term:`Primary Component`.  That is, from the perspective of the cluster when the nodes that form the Primary Component can no longer see the node, that node is failed.  From the perspective of the failed node itself, assuming that it has not crashed, it has lost its connection with the Primary Component.

Although there are third-party tools for monitoring nodes |---| such as ping, Heartbeat, and Pacemaker |---| they can be grossly off in their estimates on node failures.  These utilities do not participate in the Galera Cluster group communications and remain unaware of the Primary Component.

If you want to monitor the Galera Cluster node status poll the :ref:`wsrep_local_state <wsrep_local_state>` status variable or through the :doc:`Notification Command <notification-cmd>`.


For more information on monitoring the state of cluster nodes, see the chapter on :doc:`Monitoring the Cluster <monitoring-cluster>`.

The cluster determines node connectivity from the last time it received a network packet from the node.  You can configure how often the cluster checks this using the :ref:`evs.inactive_check_period <evs.inactive_check_period>` parameter.  During the check, if the cluster finds that the time since the last time it received a network packet from the node is greater than the value of the :ref:`evs.keepalive_period <evs.keepalive_period>` parameter, it begins to emit heartbeat beacons.  If the cluster continues to receive no network packets from the node for the period of the :ref:`evs.suspect_timeout <evs.suspect_timeout>` parameter, the node is declared suspect.  Once all members of the Primary Component see the node as suspect, it is declared inactive |---| that is, failed.

If no messages were received from the node for a period greater than the :ref:`evs.inactive_timeout <evs.inactive_timeout>` period, the node is declared failed regardless of the consensus.  The failed node remains non-operational until all members agree on its membership.  If the members cannot reach consensus on the liveness of a node, the network is too unstable for cluster operations.

The relationship between these option values is:

.. csv-table::
   :class: doc-options tight-header
   :widths: 45, 10, 45

   ":ref:`evs.keepalive_period <evs.keepalive_period>`", "<=", ":ref:`evs.inactive_check_period <evs.inactive_check_period>`"
   ":ref:`evs.inactive_check_period <evs.inactive_check_period>`", "<=", ":ref:`evs.suspect_timeout <evs.suspect_timeout>`"
   ":ref:`evs.suspect_timeout <evs.suspect_timeout>`", "<=", ":ref:`evs.inactive_timeout <evs.inactive_timeout>`"
   ":ref:`evs.inactive_timeout <evs.inactive_timeout>`", "<=", ":ref:`evs.consensus_timeout <evs.consensus_timeout>`"

.. note:: Unresponsive nodes that fail to send messages or heartbeat beacons on time |---| for instance, in the event of heavy swapping |---| may also be pronounced failed.  This prevents them from locking up the operations of the rest of the cluster.  If you find this behavior undesirable, increase the timeout parameters.


.. _`availability-partition-tolerance`:
.. rst-class:: rubric-2
.. rubric:: Cluster Availability vs. Partition Tolerance

Within the `CAP theorem <https://en.wikipedia.org/wiki/CAP_theorem>`_, Galera Cluster emphasizes data safety and consistency.  This leads to a trade-off between cluster availability and partition tolerance.  That is, when using unstable networks, such as :abbr:`WAN (Wide Area Network)`, low :ref:`evs.suspect_timeout <evs.suspect_timeout>` and :ref:`evs.inactive_timeout <evs.inactive_timeout>` values may result in false node failure detections, while higher values on these parameters may result in longer availability outages in the event of actual node failures.

Essentially what this means is that the :ref:`evs.suspect_timeout <evs.suspect_timeout>` parameter defines the minimum time needed to detect a failed node.  During this period, the cluster is unavailable due to the consistency constraint.


.. _`recovery-single-node-failure`:
.. rst-class:: rubric-2
.. rubric:: Recovering from Single Node Failures

If one node in the cluster fails, the other nodes continue to operate as usual.  When the failed node comes back online, it automatically synchronizes with the other nodes before it is allowed back into the cluster.

No data is lost in single node failures.


.. _`state-transfer-failure`:
.. rst-class:: rubric-1
.. rubric::  State Transfer Failure

Single node failures can also occur when a :term:`state snapshot transfer` fails.  This failure renders the receiving node unusable, as the receiving node aborts when it detects a state transfer failure.

When the node fails while using ``mysqldump``, restarting may require you to manually restore the administrative tables.  For the ``rsync`` method in state transfers this is not an issue, given that it does not require the database server to be in an operational state to work.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
