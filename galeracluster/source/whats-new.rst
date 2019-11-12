.. meta::
   :title: What's New in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <./index>`

   .. container:: left-margin-content

      - :doc:`Documentation <./documentation/index>`
      - :doc:`Knowledge Base <./kb/index>`
      - :doc:`Training <./training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <./training/tutorials/index>`
         - :doc:`Training Videos <./training/videos/index>`

      - :doc:`FAQ <./faq>`

      Related Documents

      - :doc:`./documentation/streaming-replication`
      - :doc:`Synchronization Functions <./documentation/wsrep-functions>`
      - :doc:`System Tables <./documentation/system-tables>`
      - :doc:`Using Streaming <./documentation/using-sr>`

      Related Articles


.. cssclass:: library-document
.. _`whats-new`:

=================================
What's New in Galera Cluster 4.x
=================================

.. index::
   pair: Galera Cluster 4.x; Streaming Replication
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions
.. index::
   pair: Galera Cluster 4.x; System Tables

With the latest release of Galera Cluster in the 4.x branch, there are some new features available to you, including the following:

- **Streaming Replication** Under normal operation, the node initiates all replication and certification operations when the transaction commits.  For large transactions, this can result in conflicts: smaller transactions can get in first and cause the large transactions to abort.  With Streaming Replication, the node breaks the transaction into fragments, then certifies and replicates them on all slave nodes while the transaction is still in progress.  Once certified, conflicting transactions can no longer abort the fragment.

  This provides an alternative replication method for handling large or long-running write transactions, or when working with hot records.

  For more information, see :doc:`./documentation/streaming-replication` and :doc:`./documentation/using-sr`.

- **Synchronization Functions**  This version introduces a series of SQL functions for use in wsrep synchronization operations.  You can use them to obtain the :term:`Global Transaction ID`, based on either the last write or last seen transaction, as well as setting the node to wait for a specific GTID to replicate and apply, before initiating the next transaction.

  For more information, see :doc:`Using Synchronization Functions <./documentation/wsrep-functions>`.

- **Galera System Tables**  In version 4 of Galera, three system tables were added to the ``mysql`` database: ``wsrep_cluster``, ``wsrep_cluster_members``, and ``wsrep_streaming_log``.  These tables may be used by database administrators to get a sense the current activity of the nodes in a cluster.

  For more information, see :doc:`System Tables <./documentation/system-tables>`.
