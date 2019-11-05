.. meta::
   :title: Galera Cluster Best Practices Articles
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

      .. cssclass:: sub-links

         - :doc:`Troubleshooting <../trouble/index>`

         .. cssclass:: here

         - :doc:`Best Practices <./index>`

      - :doc:`Training <../../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`


.. cssclass:: library-index
.. _`kb-best`:

===================================
Codership Best Practices Articles
===================================

Whereas the :doc:`Troubleshooting <../trouble/index>` section relates to handling problems with a cluster, this section of the KB provide information and guidance on improving the performance of a cluster and optimizing configuration of the nodes.


.. _`kb-best-performance`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Performance


.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Group Commit <group-commit>`

   .. rst-class:: list-stats

      Length: 322 words; Published:

   .. rst-class:: list-abstract

      If there are several transactions trying to commit at the same time, group commit will force them to be flushed to the disk with a single system call, rather than one system call for each commit. This can greatly reduce the need for flush operations, and greatly improve the throughput of TPS.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Large Transactions <large-transactions>`

   .. rst-class:: list-stats

      Length: 443 words; Published:

   .. rst-class:: list-abstract

      Large transactions, especially ones which delete millions of rows from a table at once, can lead to diminished performance. One reason is that the table may reindexed and rescanned after each row is deleted.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Parallel Slave Threads <parallel-slave-threads>`

   .. rst-class:: list-stats

      Length: 366 words; Published:

   .. rst-class:: list-abstract

      There is no rule about how many slave threads you need for replication.  Parallel threads do not guarantee better performance, but they don't impair regular operation performance and they may in fact speed up the synchronization of new nodes joining a cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Slow Nodes <detecting-slow-node>`

   .. rst-class:: list-stats

   Length: 297 words; Published:

   .. rst-class:: list-abstract

   By design, the performance of a cluster cannot be higher than the performance of the slowest node in the cluster. Even if you have only one node, its performance can be considerably slower when compared with running the same server in a standalone mode (i.e., without a wsrep Provider).

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`WAN Latency <wan-latency>`

   .. rst-class:: list-stats

      Length: 221 words; Published:

   .. rst-class:: list-abstract

      When using Galera Cluster over a WAN (Wide Area Network), remember that WAN links can have exceptionally high latency. You can check this by taking Round-Trip Time (RTT) measurements between cluster nodes. If there is a latency, you can correct for this by adjusting all of the temporal parameters.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`WAN Replication <wan-replication>`

   .. rst-class:: list-stats

      Length: 161 words; Published:

   .. rst-class:: list-abstract

      When running the cluster over a WAN (Wide Area Network), you may frequently experience transient network connectivity failures. To prevent this from partitioning the cluster, you may want to increase the *keepalive* timeouts.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Write-Set Cache Size <customizing-gcache-size>`

   .. rst-class:: list-stats

      Length: 467 words; Published:

   .. rst-class:: list-abstract

      You can define the size of the write-set cache using the ``gcache.size`` parameter. Set the size to one less than that of the data directory.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Write-Set Caching during State Transfers <gcache-during-state-transfers>`

   .. rst-class:: list-stats

      Length: 156 words; Published:

   .. rst-class:: list-abstract

      Under normal operations, nodes do not consume much more memory than the regular stand-alone database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable. Write-set caching during state transfers is the exception.



.. _`kb-best-topology`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Topology

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Multi-Master Setup <multi-master-setup>`

   .. rst-class:: list-stats

      Length: 55 words; Published:

   .. rst-class:: list-abstract

      A master is a node that can simultaneously process writes from clients. The more masters in a cluster, the higher the probability of certification conflicts.  This can lead to undesirable rollbacks and performance degradation.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Single Master Setup <single-master-setup>`

   .. rst-class:: list-stats

      Length: 81 words; Published:

   .. rst-class:: list-abstract

      If a cluster uses only one node as a master, there are certain requirements (e.g., the slave queue size) that can be relaxed.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Two-Node Clusters <two-node-clusters>`

   .. rst-class:: list-stats

      Length: 399 words; Published:

   .. rst-class:: list-abstract

      Although it may seem simple to maintain a cluster of only two nodes, there is an inherent potential problem. In a two-node cluster, when one node fails, it will cause the other to stop.



.. _`kb-best-security`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Other

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`SELinux with Galera Cluster <galera-with-selinux>`

   .. rst-class:: list-stats

      Length: 180 words; Published:

   .. rst-class:: list-abstract

      When you first enable Galera Cluster on a node that runs SELinux, it will prohibit all cluster activities.  In order to enable replication on the node, you need a policy so that SELinux can recognize cluster activities as legitimate.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Synchronization Functions <using-sync-functions>`

   .. rst-class:: list-stats

      Length: 391 words; Published: 

   .. rst-class:: list-abstract

      Occasionally, an application may need to perform a critical read--queries that require that the local database reaches the most up-to-date state possible before they're executed. You can use synchronization functions to tie the synchronization process to specific transactions so that the node waits only until a specific transaction is applied before executing the query.




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
