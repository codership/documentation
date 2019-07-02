.. cssclass:: kb-list
.. _`kb-best`:

===================================
Codership Best Practices Articles
===================================

Whereas the :doc:`Troubleshooting <../trouble/index>` section relates to handling problems with a cluster, this section of the KB provide information and guidance on improving the performance of a cluster and optimizing configuration of the nodes.


.. rubric:: :doc:`Group Commit <group-commit>`
   :class: list-sub-header

.. rst-class:: list-abstract

   If there are several transactions trying to commit at the same time, group commit will force them to be flushed to the disk with a single system call, rather than one system call for each commit. This can greatly reduce the need for flush operations, and greatly improve the throughput of TPS.


.. rubric:: :doc:`Large Transactions <large-transactions>`
   :class: list-sub-header

.. rst-class:: list-abstract

   Large transactions, especially ones deleting removes millions of rows from a table at once, can lead to diminished performance. One reason is that the table may reindexed and rescanned after each row is deleted.


.. rubric:: :doc:`Multi-Master Setup <multi-master-setup>`
   :class: list-sub-header

.. rst-class:: list-abstract

   A master is a node that can simultaneously process writes from clients. The more masters in a cluster, the higher the probability of certification conflicts.  This can lead to undesirable rollbacks and performance degradation.


.. rubric:: :doc:`Parallel Slave Threads <parallel-slave-threads>`
   :class: list-sub-header

.. rst-class:: list-abstract

   There is no rule about how many slave threads you need for replication.  Parallel threads do not guarantee better performance, but they don't impair regular operation performance and they may in fact speed up the synchronization of new nodes joining a cluster.


.. rubric:: :doc:`Single Master Setup <single-master-setup>`
   :class: list-sub-header

.. rst-class:: list-abstract

   If a cluster uses only one node as a master, there are certain requirements (e.g., the slave queue size) that can be relaxed.


.. rubric:: :doc:`SELinux with Galera Cluster <galera-with-selinux>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When you first enable Galera Cluster on a node that runs SELinux, it will prohibit all cluster activities.  In order to enable replication on the node, you need a policy so that SELinux can recognize cluster activities as legitimate.

.. rubric:: :doc:`Slow Nodes <detecting-slow-node>`
   :class: list-sub-header

.. rst-class:: list-abstract

   By design, the performance of a cluster cannot be higher than the performance of the slowest node in the cluster. Even if you have only one node, its performance can be considerably slower when compared with running the same server in a standalone mode (i.e., without a wsrep Provider).


.. rubric:: :doc:`Synchronization Functions <using-sync-functions>`
   :class: list-sub-header

.. rst-class:: list-abstract

   Occasionally, an application may need to perform a critical read--queries that require that the local database reaches the most up-to-date state possible before they're executed. You can use synchronization functions to tie the synchronization process to specific transactions so that the node waits only until a specific transaction is applied before executing the query.


.. rubric:: :doc:`Two-Node Clusters <two-node-clusters>`
   :class: list-sub-header

.. rst-class:: list-abstract

   Although it may seem simple to maintain a cluster of only two nodes, there is an inherent potential problem. In a two-node cluster, when one node fails, it will cause the other to stop.


.. rubric:: :doc:`WAN Latency <wan-latency>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When using Galera Cluster over a WAN (Wide Area Network), remember that WAN links can have exceptionally high latency. You can check this by taking Round-Trip Time (RTT) measurements between cluster nodes. If there is a latency, you can correct for this by adjusting all of the temporal parameters.


.. rubric:: :doc:`WAN Replication <wan-replication>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When running the cluster over a WAN (Wide Area Network), you may frequently experience transient network connectivity failures. To prevent this from partitioning the cluster, you may want to increase the *keepalive* timeouts.


.. rubric:: :doc:`Write-Set Cache Size <customizing-gcache-size>`
   :class: list-sub-header

.. rst-class:: list-abstract

   You can define the size of the write-set cache using the ``gcache.size`` parameter. The set the size to one less than that of the data directory.


.. rubric:: :doc:`Write-Set Caching during State Transfers <gcache-during-state-transfers>`
   :class: list-sub-header

.. rst-class:: list-abstract

   Under normal operations, nodes do not consume much more memory than the regular standalone MySQL database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable. Write-set caching during state transfers is the exception.


.. toctree::
   :hidden:
   :maxdepth: 1

   group-commit
   large-transactions
   multi-master-setup
   parallel-slave-threads
   single-master-setup
   galera-with-selinux
   detecting-slow-node
   using-sync-functions
   two-node-clusters
   wan-latency
   wan-replication
   customizing-gcache-size
   gcache-during-state-transfers




.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
