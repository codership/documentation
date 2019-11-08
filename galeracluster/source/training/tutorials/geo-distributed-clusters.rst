.. meta::
   :title: Geo-Distributed Database Clusters with Galera
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           .. cssclass:: here

           - :doc:`Tutorial Articles <./index>`

        .. cssclass:: sub-links

           - :doc:`Training Videos <../videos/index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      Related Articles


.. cssclass:: library-article
.. _`geo-distributed-clusters`:

==================================
Geo-Distributed Database Clusters
==================================

.. rst-class:: article-stats

   Length:  1043 words; Writer: Philip Stoev; Published: October 20, 2014; Topic: General; Level: Intermediate

With Galera you can construct database clusters where each node is located in a different physical or even geographical location. In this blog post we will show some of the benefits from having such a geo-distributed cluster and the specific Galera features that enable practical replication across WAN links.


.. rst-class:: section-heading
.. rubric:: Benefits from Geo-Distribution

Geo-distribution allows database to break out from the single data center, which opens a whole new approach to redundancy and performance.

**Increased Redundancy**

Having database nodes in various geographic locations increases redundancy considerably, so that a local power failure or network outage can not possibly affect all nodes in the cluster. Outages that affect multiple availability zones within a single facility are not unheard of, but Galera allows you to go beyond the availability zones and have a truly multi-datacenter database cluster.

**Database Operations are Local**

In a geo-distributed environment, Galera Cluster provides a complete, consistent and up-to-date copy of the database at each datacenter. Therefore, any query can be answered entirely from the local node using a local copy of the data and incurs no network traffic or latency penalty. Synchronization with remote nodes only takes place during commit operations.

Furthermore, those benefits apply to all queries and the entire data set. Unlike other database systems, Galera Cluster does not partition the data, or cache only part of it locally. It does not need to bring portions of the data to the query or the query to the data on a per-query basis, as the data has been fully replicated in advance.

Having a local database node to talk to also removes the latency from all the phases of the MySQL client protocol and the round-trips that it requires, including connection establishment, issuing multiple SQL statements within the same transaction, and so forth.

**Committing To Network**

If all nodes in a cluster share a common power supply or storage infrastructure, they need to durably commit transactions to disk in order to avoid data loss due to datacenter-wide power failures or, in a cloud deployment, failures affecting the entire storage back-end. Constantly flushing transactions to disk imposes an upper bound on the number of transactions that can be committed per second, unless expensive SSDs or battery-backed write caches are used.

With geographically-distributed nodes, it is possible to skip flushing every transaction to disk altogether and still have transaction persistency even after a catastrophic failure. As long as at least one node in any datacenter survived the outage, the remaining nodes, upon restart, will fetch from it all the transactions they had missed. The ``innodb_flush_log_at_trx_commit`` InnoDB option can be used to configure flushing behavior.


.. rst-class:: section-heading
.. rubric:: Galera Features for Geo-Distribution

Galera Cluster does not just happen to work well in geo-distributed environments. In fact, the transaction certification and replication approach taken by Galera is uniquely suited for high-latency links. The product also includes various features and enhancements targeted specifically for geo-distribution.

**Minimized Latency Penalty**

With Galera Cluster, the penalty for synchronizing the nodes over a high-latency link is only incurred at commit time. There are no delays or communication between the remote nodes during the transaction itself. Galera does not use distributed locking, so each row-level lock does not have to be communicated across datacenters.

While the latency penalty is unavoidable as all servers need to agree to commit every transaction, and the speed of light and routing delays are a fact of life, Galera’s certification protocol achieves synchronization using the smallest number of round-trips, using a protocol that avoids unnecessary chatting.

**Reduced Bandwidth Consumption**

It is possible to tell Galera Cluster how nodes are grouped by physical proximity using the ``gmcast.segment`` setting in the ``wsrep_provider_options`` variable. Galera will then use this information to perform various optimizations:

- messages are sent between two datacenters only once, even if there are multiple nodes at each datacenter, avoiding duplication in inter-data center traffic. The message will be relayed internally within the datacenter so that it reaches all nodes.

- State Snapshot Transfers (SST) and Incremental Snapshot Transfers (IST) will favor using a donor node from the same datacenter as the joining node.

**Configurable Flow Control**

By default, Galera will keep slave lag to a minimum by using various flow control measures in order to keep all nodes moving forward in time together. If WAN network links are involved, Galera can be configured to allow more data to be in flight on the network at any given time by increasing the evs.send_window and evs.user_send_window wsrep provider options. A higher setting will reduce the amount of time nodes wait on each other for acknowledgement, increasing transaction throughput.

Network timeouts can also be configured to tolerate transient WAN outages.

**Split-Brain Avoidance**

An odd-number of data centers (such as three) is preferred when creating a Galera Cluster, however Galera also supports two-data center deployments.

In a two-datacenter cluster, the Galera Arbitrator can be used to make one datacenter have the “majority” so that it will continue to service updates after a network split, avoiding the so-called “split-brain” problem, where neither datacenter knows who is in charge and if it is supposed to accept database updates.

**Built-in Encryption**

Galera provides encryption internally for all types of inter-node traffic:

- replication traffic and Incremental State Transfers (ISTs) are encrypted using SSL key and certificate.

- complete State Snapshot Transfers (SSTs) with using the mysqldump and xtrabackup-v2 methods can be encrypted.

**Public and Private IP addresses**

Galera Cluster can be configured to use public IP addresses if individual nodes are behind NAT or have been assigned private IPs on their network interfaces.

**Compatibility with Asynchronous Replication**

Galera Cluster also supports traditional MySQL replication and GTIDs. In high-latency situations where complete avoidance of slave lag is not required, asynchronous replication can be set up between two otherwise independent Galera clusters, each running in its own datacenter.


.. rst-class:: section-heading
.. rubric:: Summary

The case for building geo-distributed database clusters is strong. The Galera approach to replication and the specific features in the product make it practical to build Galera clusters that span multiple data centers and multiple users have such clusters already in production.
