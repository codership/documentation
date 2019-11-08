.. meta::
   :title: Flow Control with Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, node states, joining, synchronizing
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


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

      - :ref:`Catching Up <catching-up>`
      - :ref:`Cluster Sync <cluster-sync>`
      - :ref:`gcs.fc_factor <gcs.fc_factor>`
      - :ref:`gcs.fc_limit <gcs.fc_limit>`
      - :ref:`gcs.max_throttle <gcs.max_throttle>`
      - :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>`
      - :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>`
      - :ref:`No Flow Control <no-flow-control>`
      - :ref:`Write-set Caching <writeset-caching>`
      - :ref:`wsrep_ready <wsrep_ready>`

      Related Articles


.. cssclass:: library-document
.. _`flow-control`:

=============
Flow Control
=============

Galera Cluster manages the replication process using a feedback mechanism, called Flow Control.  Flow Control allows a node to pause and resume replication according to its needs.  This prevents any node from lagging too far behind the others in applying transactions.


.. _`how-flow-control-works`:
.. rst-class:: section-heading
.. rubric:: How Flow Control Works

Galera Cluster achieves synchronous replication by ensuring that transactions copy to all nodes an execute according to a cluster-wide ordering.  That said, the transaction applies and commits occur asynchronously as they replicate through the cluster.

Nodes receive write-sets and organize them into the global ordering.  Transactions that the node receives from the cluster but which it has not applied and committed, are kept in the received queue.

When the received queue reaches a certain size the node triggers Flow Control.  The node pauses replication, then works through the received queue.  When it reduces the received queue to a more manageable size, the node resumes replication.


.. _`node-states`:
.. rst-class:: sub-heading
.. rubric:: Understanding Node States

.. index::
   pair: Node states; OPEN
.. index::
   pair: Node states; PRIMARY
.. index::
   pair: Node states; JOINER
.. index::
   pair: Node states; DONOR
.. index::
   pair: Node states; JOINED
.. index::
   pair: Node states; SYNCED

Galera Cluster implements several forms of Flow Control, depending on the node state.  This ensures temporal synchrony and consistency |---| as opposed to logical, which virtual synchrony provides.

There are four primary kinds of Flow Control:

- :ref:`No Flow Control <no-flow-control>`
- :ref:`Write-set Caching <writeset-caching>`
- :ref:`Catching Up <catching-up>`
- :ref:`Cluster Sync <cluster-sync>`


.. _`no-flow-control`:
.. rst-class:: sub-heading
.. rubric:: No Flow Control

This Flow Control takes effect when nodes are in the ``OPEN`` or ``PRIMARY`` states.

When nodes hold these states, they are not considered part of the cluster.  These nodes are not allowed to replicate, apply or cache any write-sets.


.. _`writeset-caching`:
.. rst-class:: sub-heading
.. rubric:: Write-set Caching

This Flow Control takes effect when nodes are in the ``JOINER`` and ``DONOR`` states.

Nodes cannot apply any write-sets while in this state and must cache them for later.  There is no reasonable way to keep the node synchronized with the cluster, except for stopping all replication.

It is possible to limit the replication rate, ensuring that the write-set cache does not exceed the configured size.  You can control the write-set cache with the following parameters:

- :ref:`gcs.recv_q_hard_limit <gcs.recv_q_hard_limit>` Maximum write-set cache size (in bytes).
- :ref:`gcs.max_throttle <gcs.max_throttle>` Smallest fraction to the normal replication rate the node can tolerate in the cluster.
- :ref:`gcs.recv_q_soft_limit <gcs.recv_q_soft_limit>` Estimate of the average replication rate for the node.


.. _`catching-up`:
.. rst-class:: sub-heading
.. rubric:: Catching Up

This Flow Control takes effect when nodes are in the ``JOINED`` state.

Nodes in this state can apply write-sets.  Flow Control here ensures that the node can eventually catch up with the cluster.  It specifically ensures that its write-set cache never grows.  Because of this, the cluster wide replication rate remains limited by the rate at which a node in this state can apply write-sets.  Since applying write-sets is usually several times faster than processing a transaction, nodes in this state hardly ever effect cluster performance.

The one occasion when nodes in the ``JOINED`` state do effect cluster performance is at the very beginning, when the buffer pool on the node in question is empty.

.. note:: You can significantly speed this up with parallel applying.


.. _`cluster-sync`:
.. rst-class:: sub-heading
.. rubric:: Cluster Sync

This Flow Control takes effect when nodes are in the ``SYNCED`` state.

When nodes enter this state Flow Control attempts to keep the slave queue to a minimum.  You can configure how the node handles this using the following parameters:

- :ref:`gcs.fc_limit <gcs.fc_limit>` Used to determine the point where Flow Control engages.
- :ref:`gcs.fc_factor <gcs.fc_factor>` Used to determine the point where Flow Control disengages.


.. _`node-state-changes`:
.. rst-class:: section-heading
.. rubric:: Changes in the Node State

.. index::
   pair: Node states; Node state changes

The node state machine handles different state changes on different layers of Galera Cluster.  These are the node state changes that occur at the top most layer:

.. figure:: ../images/galerafsm.png

   *Galera Cluster Node State Changes*

1. The node starts and establishes a connection to the :term:`Primary Component`.

2. When the node succeeds with a state transfer request, it begins to cache write-sets.

3. The node receives a :term:`State Snapshot Transfer`.  It now has all cluster data and begins to apply the cached write-sets.

   Here the node enables Flow Control to ensure an eventual decrease in the slave queue.

4. The node finishes catching up with the cluster.  Its slave queue is now empty and it enables Flow Control to keep it empty.

   The node sets the MySQL status variable :ref:`wsrep_ready <wsrep_ready>` to the value ``1``.  The node is now allowed to process transactions.

5. The node receives a state transfer request. Flow Control relaxes to ``DONOR``.  The node caches all write-sets it cannot apply.

6. The node completes the state transfer to joiner node.

For the sake of legibility, certain transitions were omitted from the above description.  Bear in mind the following points:

- **Connectivity** Cluster configuration change events can send a node in any state to ``PRIMARY`` or ``OPEN``.  For instance, a node that is ``SYNCED`` reverts to ``OPEN`` when it loses its connection to the Primary Component due to network partition.

- **Missing Transitions** In the event that the joining node does not require a state transfer, the node state changes from the ``PRIMARY`` state directly to the ``JOINED`` state.

For more information on Flow Control see `Galera Flow Control in Percona XtraDB Cluster <https://www.mysqlperformanceblog.com/2013/05/02/galera-flow-control-in-percona-xtradb-cluster-for-mysql/>`_.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |-->|   unicode:: U+2192 .. RIGHTWARDS ARROW
   :trim:

.. |times|   unicode:: U+00D7 .. MULTIPLICATION SIGN
