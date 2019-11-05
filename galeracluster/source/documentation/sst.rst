.. meta::
   :title: State Snapshot Transfers among Galera Cluster Nodes
   :description:
   :language: en-US
   :keywords: galera cluster, sst, state snapshot transfer
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: sub-links

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      Related Documents

      - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
      - :ref:`wsrep_sst_method <wsrep_sst_method>`
      - :ref:`gmcast.segment <gmcast.segment>`
      - :ref:`mysqldump <mysqldump>`"
      - :ref:`Logical <sst-logical>`
      - :ref:`rsync <sst-physical-rsync>`
      - :ref:`Physical <sst-physical>`
      - :ref:`xtrabackup <sst-physical-xtrabackup>`
      - :ref:`Physical <sst-physical>`

      Related Articles


.. cssclass:: library-document
.. _`sst`:

===============================
State Snapshot Transfers
===============================

When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a :term:`State Snapshot Transfer` (SST) method to provide a full data copy to the new node, known as the joiner.

You can designate in advance which node should be the donor with the :ref:`wsrep_sst_donor <wsrep_sst_donor>` parameter. If you don't set the donor node, the *Group Communication* module will select a donor based on the information available about the node states.

Group Communication monitors node states for the purposes of flow control, state transfers and quorum calculations.  It ensures that a node that shows as ``JOINING`` doesn't count towards flow control and quorum.

A node can serve as a donor when it is in the ``SYNCED`` state.  The joiner node selects a donor from the available synced nodes.  It shows preference to synced nodes that have the same :ref:`gmcast.segment <gmcast.segment>` wsrep Provider option, or it selects the first in the index.  When a donor node is chosen, its state changes immediately to ``DONOR``. It's no longer available for requests.


.. _`sst-methods`:
.. rst-class:: section-heading
.. rubric:: SST Methods

Galera supports several back-end methods for use in state snapshot transfers.  There are two types: Logical State Snapshots, which interface through the database server and client; and Physical State Snapshots, which directly copy the data files from node to node.


.. csv-table::
   :class: doc-options
   :header: "Method", "Speed", "Blocks Donor", "Live Node Availability", "Type", "DB Root Access"

   ":ref:`mysqldump <mysqldump>`", "Slow", "Blocks", "Available", ":ref:`Logical <sst-logical>`", "Donor and Joiner"
   ":ref:`rsync <sst-physical-rsync>`", "Fastest", "Blocks", "Unavailable", ":ref:`Physical <sst-physical>`", "None"
   ":ref:`xtrabackup <sst-physical-xtrabackup>`", "Fast", "Briefly", "Unavailable", ":ref:`Physical <sst-physical>`", "Only Donor"

To set the State Snapshot Transfer method, use the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter.  In the example below, the method is set to use ``rsync``, along with the default donors:

.. code-block:: ini

   wsrep_sst_method = rsync
   wsrep_sst_donor  = "node1, node2"

There is no single best method for State Snapshot Transfers.  You must decide which suits your particular needs and cluster deployment.  Fortunately, you need only set the method on the receiving node.  So long as the donor has support, it serves the transfer in whatever method the joiner requests.

.. toctree::
   :maxdepth: 1

   sst-logical
   sst-physical
