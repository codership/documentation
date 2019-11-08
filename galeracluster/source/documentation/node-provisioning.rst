.. meta::
   :title: Provisioning Node for Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, node provisioning, joining a cluster
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

      - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
      - :ref:`wsrep_node_name <wsrep_node_name>`

      Related Articles


.. cssclass:: library-document
.. _`node-provisioning`:

====================
Node Provisioning
====================

.. index::
   pair: Parameters; wsrep_data_dir
.. index::
   pair: Parameters; wsrep_sst_donor
.. index::
   pair: Parameters; wsrep_node_name
.. index::
   single: Total Order Isolation

When the state of a new or failed node differs from that of the cluster's :term:`Primary Component`, the new or failed node must be synchronized with the cluster.  Because of this, the provisioning of new nodes and the recover of failed nodes are essentially the same process as that of joining a node to the cluster Primary Component.

Galera reads the initial node state ID from the **grastate.txt** file, found in the directory assigned by the ``wsrep_data_dir`` parameter.  Each time the node gracefully shuts down, Galera saves to this file.

In the event that the node crashes while in :term:`Total Order Isolation` mode, its database state is unknown and its initial node state remains undefined::

	00000000-0000-0000-0000-000000000000:-1

.. note:: In normal transaction processing, only the seqno part of the GTID remains undefined, (that is, with a value of ``-1``.  The UUID, (that is, the remainder of the node state), remains valid.  In such cases, you can recover the node through an :term:`Incremental State Transfer`.


.. _`node-provisioning-about-joiners`:
.. rst-class:: section-heading
.. rubric:: How Nodes Join the Cluster

When a node joins the cluster, it compares its own :term:`state UUID` to that of the :term:`Primary Component`.  If the state UUID does not match, the joining node requests a state transfer from the cluster.

There are two options available to determining the state transfer donor:

- **Automatic** When the node attempts to join the cluster, the group communication layer determines the state donor it should use from those members available in the Primary Component.

- **Manual** When the node attempts to join the cluster, it uses the :ref:`wsrep_sst_donor <wsrep_sst_donor>` parameter to determine which state donor it should use.  If it finds that the state donor it is looking for is not part of the Primary Component, the state transfer fails and the joining node aborts.  For :ref:`wsrep_sst_donor <wsrep_sst_donor>`, use the same name as you use on the donor node for the :ref:`wsrep_node_name <wsrep_node_name>` parameter.

.. note:: A state transfer is a heavy operation.  This is true not only for the joining node, but also for the donor.  In fact, a state donor may not be able to serve client requests.

	  Thus, whenever possible: manually select the state donor, based on network proximity and configure the load balancer to transfer client connections to other nodes in the cluster for the duration of the state transfer.

When a state transfer is in process, the joining node caches write-sets that it receives from other nodes in a slave queue.  Once the state transfer is complete, it applies the write-sets from the slave queue to catch up with the current Primary Component state.  Since the state snapshot carries a state UUID, it is easy to determine which write-sets the snapshot contains and which it should discard.

During the catch-up phase, flow control ensures that the slave queue shortens, (that is, it limits the cluster replication rates to the write-set application rate on the node that is catching up).

While there is no guarantee on how soon a node will catch up, when it does the node status updates to ``SYNCED`` and it begins to accept client connections.


.. _`node-provisioning-state-transfer`:
.. rst-class:: section-heading
.. rubric:: State Transfers

There are two types of state transfers available to bring the node up to date with the cluster:

- :term:`State Snapshot Transfer` (SST) Where donor transfers to the joining node a snapshot of the entire node state as it stands.

- :term:`Incremental State Transfer` (IST) Where the donor only transfers the results of transactions missing from the joining node.

When using automatic donor selection, starting in Galera Cluster version 3.6, the cluster decides which state transfer method to use based on availability.

- If there are no nodes available that can safely perform an incremental state transfer, the cluster defaults to a state snapshot transfer.

- If there are nodes available that can safely perform an incremental state transfer, the cluster prefers a local node over remote nodes to serve as the donor.

- If there are no local nodes available that can safely perform an incremental state transfer, the cluster chooses a remote node to serve as the donor.

- Where there are several local or remote nodes available that can safely perform an incremental state transfer, the cluster chooses the node with the highest seqno to serve as the donor.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
