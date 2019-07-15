.. meta::
   :title: The Primary Component in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../../kb/trouble/index>`
         - :doc:`Best Practices <../../kb/best/index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <./index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: bull-head

         Related Documents

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: tutorial-article
.. _`primary-component`:

=========================================
The Primary Component in Galera Cluster
=========================================

.. rst-class:: list-stats

   Length:  782 words; Writer: Philip Stoev; Published: August 25, 2015; Topic: General; Level: Intermediate


In this post, we will describe the Primary Component, a central concept in how Galera ensures that there is no opportunity for database inconsistency or divergence between the nodes in case of a network split.


.. rst-class:: rubric-1
.. rubric:: What is the Primary Component?

The Primary Component is that set of Galera nodes that can communicate with each other over the network and contains the majority of the nodes. In case of a network partition, it is those nodes that can safely commit a transaction. A cluster can only have one such set of nodes, as there can only be one majority. No other set of nodes will commit transactions, thus removing the possibility of two parts of the cluster committing different transactions and thus diverging and becoming inconsistent.


.. rst-class:: rubric-1
.. rubric:: The Healthy Cluster

In a healthy cluster, all nodes nodes can communicate with each other, so they all belong to the Primary Component and can all receive updates. There are no network partitions and therefore there are no nodes which have become separated. The wsrep_cluster_status status variable reports Primary on all nodes.

.. code-block:: console

   MySQL [test]> show status like 'wsrep_cluster_status';

   +----------------------+---------+
   | Variable_name        | Value   |
   +----------------------+---------+
   | wsrep_cluster_status | Primary |
   +----------------------+---------+

``wsrep_cluster_status`` is a good variable to monitor on every node using your monitoring application or load balancer.

On any node that is in the Primary Component, the ``wsrep_cluster_size`` status variable shows the current number of nodes in the cluster:

.. code-block:: console

   MySQL [test]> show status like 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 3     |
   +--------------------+-------+
   1 row in set (0.00 sec)

If you have a need for the data to be replicated to N servers or locations for reliability reasons, configure your monitoring framework to alert you if the value of ``wsrep_cluster_size`` drops below N.


.. rst-class:: rubric-1
.. rubric:: Handling Network Partitions

If one or more nodes becomes separated from the Cluster by a network partition, each node in the cluster will decide if it is on the majority (primary) or the minority side of the partition.

The nodes that detect they are in the minority will transition to a state of Non-Primary and refuse further queries. Writes to those nodes will be prevented as they can no longer guarantee that a conflicting write is not being performed on the Primary Component at the same time.

Reading from the non-Primary nodes will also be disabled, as they are no longer up-to-date with respect to the authoritative data held on the majority portion of the cluster.

Any transactions that were being committed while the network outage was in the process of being detected will return an error and must be retried by the application.

The nodes that detect they are in the majority will remain in a state of Primary and will continue to process future transactions. The value of the ``wsrep_cluster_size`` on those nodes will reflect the size of the now reduced primary component of the cluster.


.. rst-class:: rubric-1
.. rubric:: Recovery after a Network Partition

As soon as the network partition or the outage is healed, any nodes not in the Primary component that have continued to run will synchronize with the nodes from the Primary component and will rejoin the cluster. The ``wsrep_cluster_size`` will increase accordingly with the number of nodes that have rejoined.

Any nodes where the mysqld processes have terminated will need to be restarted in order to rejoin.


.. rst-class:: rubric-1
.. rubric:: The Split Brain Problem

A problem that happens both in theory and in practice is the so called split-brain situation, where the cluster gets split by a network outage into two exactly equal parts. A software system that is not prepared to handle that eventuality could allow conflicting transactions to be executed on the separate parts of the cluster while they are not coordinating. This would cause the databases on each side to diverge without the possibility of an automatic reconciliation later.

Galera Cluster safeguards against this particular problem. As no set of nodes will have the majority, no part of the cluster can be considered Primary, so all parts of the cluster will transition to state of Non-Primary, all refusing further queries in order to protect the integrity of the database.

To prevent split-brain scenarios, never use an even number of nodes or data centers in your setup. If it is not practical to do so, Galera provides several alternatives:

- Install a Galera Arbitrator process to serve for the purpose of breaking ties. Note that this process, even though not a fully-featured database, continues to receive all replication traffic, so must be secured appropriately and provided with sufficient bandwidth.

- Use the ``pc.weight`` setting of ``wsrep_provider_options`` to assign a weight greater than 1 to one of the nodes; This weight will then be considered in majority calculations and ties may be avoided;
