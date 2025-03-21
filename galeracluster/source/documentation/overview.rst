.. meta::
   :title: Overview of Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, mysql, mariadb, overview
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`overview-galera`:

=============================
Overview of Galera Cluster
=============================

Galera Cluster is a synchronous multi-primary database cluster, based on synchronous replication and MySQL and InnoDB. When Galera Cluster is in use, database reads and writes can be directed to any node. Any individual node can be lost without interruption in operations and without using complex failover procedures.

At a high level, Galera Cluster consists of a database server (that is, MySQL or MariaDB) that uses the :term:`Galera Replication Plugin` to manage replication. To be more specific, the MySQL replication plugin API has been extended to provide all the information and hooks required for true multi-primary, synchronous replication. This extended API is called the Write-Set Replication API, or wsrep API.

Through the wsrep API, Galera Cluster provides certification-based replication. A transaction for replication, the write-set not only contains the database rows to replicate, but also includes information on all of the locks that were held by the database during the transaction. Each node then certifies the replicated write-set against other write-sets in the applier queue. The write-set is then applied |---| if there are no conflicting locks. At this point, the transaction is considered committed, after which each node continues to apply it to the tablespace.

This approach is also called virtually synchronous replication, given that while it is logically synchronous, the actual writing and committing to the tablespace happens independently, and thus asynchronously on each node.

   .. only:: html

          .. image:: ../images/training.jpg
             :target: https://galeracluster.com/training-courses/
             :width: 740

   .. only:: latex

          .. image:: ../images/training.jpg
		  :target: https://galeracluster.com/training-courses/


.. _`benefits-galera`:
.. rst-class:: section-heading
.. rubric:: Benefits of Galera Cluster

Galera Cluster provides a significant improvement in high-availability for the MySQL system. The various ways to achieve high-availability have typically provided only some of the features available through Galera Cluster, making the choice of a high-availability solution an exercise in trade-offs.

The following features are available through Galera Cluster:

- **True Multi-Primary**

  You can read and write to any node at any time. Changes to data on one node will be replicated on all.

- **Synchronous Replication**

  There is no replica lag, so no data is lost if a node crashes.

- **Tightly Coupled**

  All nodes hold the same state. There is no diverged data between nodes.

- **Multi-Threaded Replica**

  This allows for better performance and for any workload.

- **No Primary-Replica Failover**

  There is no need for primary/replica operations or to use Virtual IPs (VIP).

- **Hot Standby**

  There is no downtime related to failures or intentionally taking down a node for maintenance since there is no failover.

- **Automatic Node Provisioning**

  There's no need to backup manually the database and copy it to the new node.

- **Supports InnoDB.**

  The InnoDB storage engine provides for transactional tables.

- **Transparent to Applications**

  Generally, you won't have to change an application that will interface with the database as a result of Galera. If you do, it will be minimal changes.

- **No Read and Write Splitting Needed**

  There is no need to split read and write queries.

In summary, Galera Cluster is a high-availability solution that is both robust in terms of data integrity and provides high-performance with instant failovers.


.. _`Galera Cluster Cloud Implementations`:

.. rst-class:: section-heading
.. rubric:: Cloud Implementations with Galera Cluster

An additional benefit of Galera Cluster is good cloud support. Automatic node provisioning makes elastic scale-out and scale-in operations painless. Galera Cluster has been proven to perform extremely well in the cloud, such as when using multiple small node instances, across multiple data centers |---| AWS zones, for example |---| or even over Wider Area Networks.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
