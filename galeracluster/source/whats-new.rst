.. meta::
   :title: What's New in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

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

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <./documentation/index>`
   - :doc:`KB <./kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <./training/index>`

   - :doc:`FAQ <./faq>`


.. cssclass:: library-document
.. _`whats-new`:

=================================
What's New
=================================

At Codership, we're constantly improving our products, in particular Galera Cluster |---| striving to make it the high performing, most stable and secure database cluster system available. We're also always expanding and improving the Codership Library by updating the Documentation for changes to the software and seeking to make the text clearer. In the Library we're working on adding articles to our Knowledge Base to help you quickly solve problems you might encounter, as well publishing more tutorials in our Training section.

On this web page, you can learn what's new in all of these areas, about changes to our software and to our Library.  So check this page every month or so for updates.

---------------------------------
What's New in the Library
---------------------------------

In the past few months we've added a :doc:`Training section <./training/index>`, which includes :doc:`Tutorial Articles <./training/tutorials/index>` and :doc:`Training Videos <./training/videos/index>`.  For now, the Training section is free and wide open. In the future, we will at least require you to register to access them.

Along these lines, we intend to start offering :doc:`Live Virtual Classes <./training/tutorials/index>`, which will be taught by our staff |---| some of whom are the developers of Galera Cluster |---| using a video communcation conferencing systems such Zoom. This will allow you to attend useful and professionally taught training classes from your office or home.


---------------------------------
What's New in Galera Cluster 4.x
---------------------------------

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

.. container:: bottom-links

   Related Documents

   - :doc:`./documentation/streaming-replication`
   - :doc:`Synchronization Functions <./documentation/wsrep-functions>`
   - :doc:`System Tables <./documentation/system-tables>`
   - :doc:`Using Streaming <./documentation/using-sr>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
