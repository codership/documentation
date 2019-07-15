.. meta::
   :title: InnoDB Isolation Levels
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

      - :ref:`READ-COMMITTED <read-committed>`
      - :ref:`READ-UNCOMMITTED <read-uncommitted>`
      - :ref:`REPEATABLE-READ <repeatable-read>`
      - :ref:`SERIALIZABLE <serializable>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`isolation-levels`:

======================
Isolation Levels
======================

In a database system, concurrent transactions are processed in "isolation" from each other. The level of isolation determines how transactions can affect each other.

.. rst-class:: rubric-1
.. rubric:: Intra-Node vs. Inter-Node Isolation in Galera Cluster

Before going into details about possible isolation levels which can be set for a client session in Galera Cluster it is important to make a distinction between single node and global cluster transaction isolation. Individual cluster nodes can provide any isolation level *to the extent* it is supported by MySQL/InnoDB. However isolation level *between* the nodes in the cluster is affected by replication protocol, so transactions issued on different nodes may not be isolated *identically* to transactions issued on the same node.

Overall isolation levels that are supported cluster-wide are

- :ref:`READ-UNCOMMITTED <read-uncommitted>`
- :ref:`READ-COMMITTED <read-committed>`
- :ref:`REPEATABLE-READ <repeatable-read>`

For transactions issued on different nodes, isolation is also strengthened by the "first committer wins" rule, which eliminates the "lost update anomaly" inherent to these levels, whereas for transactions issued on the same node this rule does not hold (as per original MySQL/InnoDB behavior). This makes for different outcomes depending on transaction origin (transaction issued on the same node may succeed, whereas the same transaction issued on another node would fail), but in either case it is no weaker than that isolation level on a standalone MySQL/InnoDB.

:ref:`SERIALIZABLE <serializable>`
isolation level is honored only between transactions issued on the same node and thus should be avoided.

Data consistency between the nodes is always guaranteed regardless of the isolation level chosen by the client. However the client logic may break if it relies on an isolation level which is not not supported in the given configuration.

.. rst-class:: rubric-1
.. rubric:: Understanding Isolation Levels

.. warning:: When using Galera Cluster in master-slave mode, all four levels are available to you, to the extend that MySQL supports it.  In multi-master mode, however, you can only use the ``REPEATABLE-READ`` level.


.. _`read-uncommitted`:
.. rst-class:: rubric-2
.. rubric:: READ-UNCOMMITTED

Here transactions can see changes to data made by other transactions that are not yet committed.

In other words, transactions can read data that eventually may not exist, given that other transactions can always rollback the changes without commit.  This is known as a dirty read.  Effectively, ``READ-UNCOMMITTED`` has no real isolation at all.


.. _`read-committed`:
.. rst-class:: rubric-2
.. rubric:: READ-COMMITTED

Here dirty reads are not possible.  Uncommitted changes remain invisible to other transactions until the transaction commits.

However, at this isolation level ``SELECT`` queries use their own snapshots of committed data, that is data committed before the ``SELECT`` query executed.  As a result, ``SELECT`` queries, when run multiple times within the same transaction, can return different result sets.  This is called a non-repeatable read.


.. _`repeatable-read`:
.. rst-class:: rubric-2
.. rubric:: REPEATABLE-READ

Here non-repeatable reads are not possible.  Snapshots taken for the ``SELECT`` query are taken the first time the ``SELECT`` query runs during the transaction.

The snapshot remains in use throughout the entire transaction for the ``SELECT`` query.  It always returns the same result set.  This level does not take into account changes to data made by other transactions, regardless of whether or not they have been committed.  IN this way, reads remain repeatable.


.. _`serializable`:
.. rst-class:: rubric-2
.. rubric:: SERIALIZABLE

Here all records accessed within a transaction are locked.  The resource locks in a way that also prevents you from appending records to the table the transaction operates upon.

``SERIALIZABLE`` prevents a phenomenon known as a phantom read.  Phantom reads occur when, within a transaction, two identical queries execute, and the rows the second query returns differ from the first.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
