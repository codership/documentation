.. meta::
   :title: Certification-Based Replication
   :description:
   :language: en-US
   :keywords: galera cluster, certification based replication
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

      Related Articles


.. cssclass:: library-document
.. _`certification-based-replication`:

===================================
Certification-Based Replication
===================================

Certification-based replication uses group communication and transaction ordering techniques to achieve synchronous replication.

Transactions execute optimistically in a single node, or replica, and then at commit time, they run a coordinated certification process to enforce global consistency.  It achieves global coordination with the help of a broadcast service that establishes a global total order among concurrent transactions.


.. _`cert-repl-requirements`:
.. rst-class:: section-heading
.. rubric:: Certification-Based Replication Requirements

It's not possible to implement certification-based replication for all database systems.  It requires certain features of the database in order to work;

- **Transactional Database:** The database must be transactional. Specifically, it has to be able to rollback uncommitted changes.

- **Atomic Changes:** Replication events must be able to change the database, atomically.  All of a series of database operations in a transaction must occur, else nothing occurs.

- **Global Ordering:** Replication events must be ordered globally.  Specifically, they are applied on all instances in the same order.


.. _`cert-repl-workings`:
.. rst-class:: section-heading
.. rubric:: How Certification-Based Replication Works

The main idea in certification-based replication is that a transaction executes conventionally until it reaches the commit point, assuming there is no conflict.  This is called optimistic execution.

.. figure:: ../images/certificationbasedreplication.png

   *Certification Based Replication*

When the client issues a ``COMMIT`` command, but before the actual commit occurs, all changes made to the database by the transaction and primary keys of the changed rows, are collected into a write-set.  The database then sends this write-set to all of the other nodes.

The write-set then undergoes a deterministic certification test, using the primary keys.  This is done on each node in the cluster, including the node that originates the write-set.  It determines whether or not the node can apply the write-set.

If the certification test fails, the node drops the write-set and the cluster rolls back the original transaction.  If the test succeeds, though, the transaction commits and the write-set is applied to the rest of the cluster.

.. _`cert-repl-in-galera`:
.. rst-class:: section-heading
.. rubric:: Certification-Based Replication in Galera Cluster

The implementation of certification-based replication in Galera Cluster depends on the global ordering of transactions.

Galera Cluster assigns each transaction a global ordinal sequence number, or ``seqno``, during replication.  When a transaction reaches the commit point, the node checks the sequence number against that of the last successful transaction.  The interval between the two is the area of concern, given that transactions that occur within this interval have not seen the effects of each other.  All transactions in this interval are checked for primary key conflicts with the transaction in question.  The certification test fails if it detects a conflict.

The procedure is deterministic and all replica receive transactions in the same order.  Thus, all nodes reach the same decision about the outcome of the transaction.  The node that started the transaction can then notify the client application whether or not it has committed the transaction.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
