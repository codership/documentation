.. meta::
   :title: Introduction to Database Replication and Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, overview, asynchronous replication, synchronous replication
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

      - :doc:`Certification Replication <certification-based-replication>`
      - :doc:`tech-desc-introduction`
      - :doc:`node-states`
      - :doc:`isolation-levels`
      - :doc:`Node Recovery <recovery>`
      - :doc:`weighted-quorum`
      - :doc:`Replicaiton Architecture <architecture>`
      - :doc:`state-transfer`
      - :doc:`streaming-replication`

      Related Articles


.. cssclass:: library-document
.. _`database-replication`:

======================
Database Replication
======================

.. index::
   pair: Database cluster; Descriptions

Database replication refers to the frequent copying of data from one node |---| a database on a server |---| into another.  Think of a database replication system as a distributed database, where all nodes share the same level of information.  This system is also known as a *database cluster*.

The database clients, such as web browsers or computer applications, do not see the database replication system, but they benefit from close to native :abbr:`DBMS (Database Management System)` behavior.


.. _`masters-slaves`:
.. rst-class:: section-heading
.. rubric:: Masters and Slaves

Many :abbr:`Database Management Systems (DBMS)` replicate the database.

The most common replication setup uses a master/slave relationship between the original data set and the copies.


.. figure:: ../images/asynchronousreplication.png

   *Master/Slave Replication*

In this system, the master database server logs the updates to the data and propagates those logs through the network to the slaves.  The slave database servers receive a stream of updates from the master and apply those changes.

Another common replication setup uses mult-master replication, where all nodes function as masters.

.. figure:: ../images/synchronousreplication.png

   *Multi-master Replication*

In a multi-master replication system, you can submit updates to any database node.  These updates then propagate through the network to other database nodes.  All database nodes function as masters.  There are no logs available and the system provides no indicators sent to tell you if the updates were successful.


.. _`asynchronous-synchronous-replication`:
.. rst-class:: section-heading
.. rubric:: Asynchronous and Synchronous Replication

.. index::
   pair: Eager replication; Descriptions
.. index::
   pair: Lazy replication; Descriptions
.. index::
   pair: Asynchronous replication; Descriptions
.. index::
   pair: Synchronous replication; Descriptions

In addition to the setup of how different nodes relate to one another, there is also the protocol for how they propagate database transactions through the cluster.

- **Synchronous Replication** Uses the approach of eager replication.  Nodes keep all replicas synchronized by updating all replicas in a single transaction.  In other words, when a transaction commits, all nodes have the same value.

- **Asynchronous Replication** Uses the approach of lazy replication.  The master database asynchronously propagates replica updates to other nodes.  After the master node propagates the replica, the transaction commits.  In other words, when a transaction commits, for at least a short time, some nodes hold different values.


.. _`advantages-synchronous-replication`:
.. rst-class:: sub-heading
.. rubric:: Advantages of Synchronous Replication

In theory, there are several advantages that synchronous replication has over asynchronous replication.  For instance:


- **High Availability** Synchronous replication provides highly available clusters and guarantees 24/7 service availability, given that:

  - No data loss when nodes crash.
  - Data replicas remain consistent.
  - No complex, time-consuming failovers.

- **Improved Performance** Synchronous replications allows you to execute transactions on all nodes in the cluster in parallel to each other, increasing performance.

- **Causality across the Cluster** Synchronous replication guarantees causality across the whole cluster.  For example, a ``SELECT`` query issued after a transaction always sees the effects of the transaction, even if it were executed on another node.

.. _`disadvantages-synchronous-replication`:
.. rst-class:: sub-heading
.. rubric:: Disadvantages of Synchronous Replication

Traditionally, eager replication protocols coordinate nodes one operation at a time.  They use a two phase commit, or distributed locking.  A system with :math:`n` number of nodes due to process :math:`o` operations with a throughput of :math:`t` transactions per second gives you :math:`m` messages per second with:

.. math::

   m = n \times o \times t


What this means that any increase in the number of nodes leads to an exponential growth in the transaction response times and in the probability of conflicts and deadlock rates.

For this reason, asynchronous replication remains the dominant replication protocol for database performance, scalability and availability.  Widely adopted open source databases, such as MySQL and PostgreSQL only provide asynchronous replication solutions.


.. _`solving-issues-synchronous-replication`:
.. rst-class:: section-heading
.. rubric:: Solving the Issues in Synchronous Replication

There are several issues with the traditional approach to synchronous replication systems.  Over the past few years, researchers from around the world have begun to suggest alternative approaches to synchronous database replication.

In addition to theory, several prototype implementations have shown much promise.  These are some of the most important improvements that these studies have brought about:

- **Group Communication**  This is a high-level abstraction that defines patterns for the communication of database nodes.  The implementation guarantees the consistency of replication data.

- **Write-sets** This bundles database writes in a single write-set message.  The implementation avoids the coordination of nodes one operation at a time.

- **Database State Machine** This processes read-only transactions locally on a database site.  The implementation updates transactions are first executed locally on a database site, on shallow copies, and then broadcast as a read-set to the other database sites for certification and possibly commits.

- **Transaction Reordering** This reorders transactions before the database site commits and broadcasts them to the other database sites.  The implementation increases the number of transactions that successfully pass the certification test.

The certification-based replication system that Galera Cluster uses is built on these approaches.


.. |times|   unicode:: U+00D7 .. MULTIPLICATION SIGN

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
