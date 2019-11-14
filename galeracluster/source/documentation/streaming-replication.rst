.. meta::
   :title: Streaming Replication with Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, streaming replication, upgrading
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

      - :ref:`Limitations <sr-limit>`
      - :ref:`Streaming Replication <usr-hot-records>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`streaming-replication`:

======================
Streaming Replication
======================

.. index::
   pair: Galera Cluster 4.x; Streaming Replication

Under normal operation, the node performs all replication and certification events when a transaction commits.  When working with small transactions this is fine. However, it poses an issue with long-running writes and changes to large data-sets.

In :term:`Streaming Replication`, the node breaks the transaction into fragments, then certifies and replicates them on the slaves while the transaction is still in progress.  Once certified, the fragment can no longer be aborted by conflicting transactions.

Additionally, Streaming Replication allows the node to process transaction write-sets greater than 2Gb.

.. note:: Streaming Replication is a new feature introduced in version 4.0 of Galera Cluster.  Older versions do not support these operations.


.. _`when-use-sr`:
.. rst-class:: section-heading
.. rubric:: When to Use Streaming Replication

In most cases, the normal method Galera Cluster uses in replication is sufficient in transferring data from a node to a cluster.  :term:`Streaming Replication` provides you with an alternative for situations in which this is not the case.  Keep in mind that there are some limitations to its use.  It's recommended that you only enable it at a session-level, and then only on specific transactions that require the feature.

For more information on the limitations to Streaming Replication, see :ref:`Limitations <sr-limit>`.


.. _`longrun-write-trx`:
.. rst-class:: sub-heading
.. rubric:: Long-Running Write Transactions

When using normal replication, you may occasionally encounter issues with long-running write transactions.

The longer it takes for a node to commit a transaction, the greater the likelihood that the cluster will apply a smaller, conflicting transaction before the longer one can replicate to the cluster.  When this happens, the cluster aborts the long-running transaction.

Using :term:`Streaming Replication` on long-running transactions mitigates this situation.  Once the node replicates and certifies a fragment, it is no longer possible for other transactions to abort it.


Certification keys are generated from record locks, therefore they don't cover gap locks or next key locks. If the transaction takes a gap lock, it is possible that a transaction, which is executed on another node, will apply a write set which encounters the gap log and will abort the streaming transaction.


.. _`large-write-trx`:
.. rst-class:: sub-heading
.. rubric:: Large Data Write Transactions

When using normal replication, the node locally processes the transaction and doesn't replicate the data until you commit.  This can create problems when updating a large volume of data, especially on nodes with slower network connections.

Additionally, while slave nodes apply a large transaction, they cannot commit other transactions they receive, which may result in Flow Control throttling of the entire cluster.

With :term:`Streaming Replication`, the node begins to replicate the data with each transaction fragment, rather than waiting for the commit.  This allows you to spread the replication over the lifetime of the transaction.

In the case of the slave nodes, after the slave applies a fragment, it's free to apply and commit other, concurrent transactions without blocking.  This allows the slave node to process incrementally the entire large transaction with a minimal impact on the cluster.


.. _`hot-records`:
.. rst-class:: sub-heading
.. rubric:: Hot Records

In situations in which an application frequently updates one and the same records from the same table (e.g., when implementing a locking scheme, a counter, or a job queue), you can use :term:`Streaming Replication` to force critical updates to replicate to the entire cluster.

Running a transaction in this way effectively locks the hot record on all nodes, preventing other transactions from modifying the row.  It also increases the chances that the transaction will commit successfully and that the client in turn will receive the desired outcome.

For more information and an example of how to implement Streaming Replication in situations such as this, see :ref:`Using Streaming Replication with Hot Records <usr-hot-records>`.


.. _`sr-limit`:
.. rst-class:: section-heading
.. rubric:: Limitations

In deciding whether you want to use :term:`Streaming Replication` with your application, consider the following limitations.


.. _`limit-in-trx`:
.. rst-class:: sub-heading
.. rubric:: Performance During a Transaction

When you enable :term:`Streaming Replication`, as of version 4 of Galera, each node in the cluster begins recording its write-sets to the ``wsrep_streaming_log`` table in the ``mysql`` database. Nodes do this to ensure the persistence of Streaming Replication updates in the event that they crash.  However, this operation increases the load on the node, which may adversely affect its performance.

As such, it's recommended that you only enable Streaming Replication at a session-level and then only for transactions that would not run correctly without it.


.. _`limit-rollback`:
.. rst-class:: sub-heading
.. rubric:: Performance During Rollbacks

Occasionally, you may encounter situations in which the cluster needs to roll back a transaction while :term:`Streaming Replication` is in use.  In these situations, the rollback operation consumes system resources on all nodes.

When long-running write transactions frequently need to be rolled back, this can become a performance problem.  Therefore, it's a good application design policy to use shorter transactions whenever possible.  In the event that your application performs batch processing or scheduled housekeeping tasks, consider splitting these into smaller transactions in addition to using Streaming Replication.

.. container:: bottom-links

   Related Documents

   - :ref:`Limitations <sr-limit>`
   - :ref:`Streaming Replication <usr-hot-records>`
