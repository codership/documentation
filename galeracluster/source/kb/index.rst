.. meta::
   :title: Galera Cluster Knowledge Base
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

        - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

.. cssclass:: library-index
.. _`kb`:

=============================
The Codership Knowledge Base
=============================

:doc:`The Codership Documentation <../documentation/index>` explains in detail how to deploy and administer a Galera Cluster. This section, the Codership Knowledge Base (KB) contains information on resolving problems and improving use of Galera Cluster.  Here you'll find troubleshooting articles and best practices articles.

In essence, the Documentation is how to use Galera assuming everything goes according to plan; the KB is for when things don't go as expected or when they could be better.

In addition to this KB, you can also post questions on the `Codership Forum <https://galeracluster.com/community/>`_. The community, as well as our staff monitor and respond to posts made there. If you need more immediate and personalized assistance, you can get a Support contract with us at Codership.  For a quote on the cost of support, write us at info@codership.com or use `our on-line form <https://galeracluster.com/contact-us/#send-us-a-message>`_ to send us a message.


.. _`kb-trouble`:

-------------------------
Troubleshooting Articles
-------------------------

This is the Troubleshooting section of the Galera Knowledge Base (KB). It contains information on resolving problems you might experience with Galera Cluster. It includes articles on how to diagnose and address various performance and replication trouble. For articles related to performance and other ways to improve usage of Galera Cluster, see the next section, :ref:`Best Practices <kb-best>`.


.. _`kb-trouble-state-transfers`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: State Transfers

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Node Crashes during SST <node-crash-during-sst>`

   .. rst-class:: list-stats

      Length: 463 words; Updated: November 6, 2019

   .. rst-class:: list-abstract

      When using ``rsync`` for State Snapshot Transfers, if the donor node crashes in the middle of a state transfer, the joiner node may stall, its databases may be incomplete and inaccessible. This article discusses this situation and how to resolve it.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`SST Fails due to SQL Syntax Errors <sst-fails-sql-syntax-error>`

   .. rst-class:: list-stats

      Length: 789 words; Updated: November 7, 2019

   .. rst-class:: list-abstract

      When using ``mysqldump`` for State Snapshot Transfers, and a new node joins a cluster, after it requests data from the cluster, it may fail. Looking at the database error log, there may be entries that says there were SQL Syntax errors.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Requested State Transfer Failed <requested-state-transfer-failed>`

   .. rst-class:: list-stats

      Length: 649 words; Updated: November 6, 2019

   .. rst-class:: list-abstract

      When a new node joins a cluster, it will try to synchronize with the cluster by getting a full copy of the databases from one of the other nodes.  Sometimes its request will be ignored and no node will be selected to be the donor.


.. _`kb-trouble-sql-syntax`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Schema & SQL

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Cluster Stalls on ALTER TABLE <stall-on-alter-table>`

   .. rst-class:: list-stats

      Length: 519 words; Updated: October 30, 2019:

   .. rst-class:: list-abstract

      A cluster will sometimes stall when executing ``ALTER TABLE``. This can happen when changing the schema of a table with several columns and indexes. Depending on the number of rows, it can be a major drain on performance.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`User Changes not Replicating <user-changes>`

   .. rst-class:: list-stats

      Length: 373 words; Published:

   .. rst-class:: list-abstract

      After making changes to the ``mysql`` database (e.g., user name, password, host address), they’re not replicated to the other nodes in the cluster. This can cause problems for users, as well as frustrate the DBA.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`auto-increment-multiples`

   .. rst-class:: list-stats

      Length: 995 words; Published: October 22, 2019

   .. rst-class:: list-abstract

      Tables with key columns that use the ``AUTO_INCREMENT`` attribute will increment values by more than one, when using Galera Cluster. This can be confusing and worrisome, but this article explains how this is a good method.


.. _`kb-trouble-splits-topology`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Splits & Topology

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Multi-Master Conflicts <multi-master-conflicts>`

   .. rst-class:: list-stats

      Length: 751 words; Published:

   .. rst-class:: list-abstract

      Mmlti-master database environments have certain types of conflicts and typically involve inconsistencies of rows amongst nodes. This article explains the nuances of Galera Cluster and how to handle and prevent them.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Unknown Command Errors <error-unknown-command>`

   .. rst-class:: list-stats

      Length: 971 words; Updated: November 6, 2019

   .. rst-class:: list-abstract

      Although a user entered a valid SQL statement, instead of receiving the expected results, an error message is returned saying, "Unknown Command".  It may not do this on all nodes, but error message returned for all queries on some nodes.


.. _`kb-best`:

------------------------
Best Practices Articles
------------------------

Whereas the :ref:`Troubleshooting <kb-trouble>` section relates to handling problems with a cluster, this section of the KB provide information and guidance on improving the performance of a cluster and optimizing configuration of the nodes.


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

      When several transactions try to commit at the same time, ``GROUP COMMIT`` will force them to be flushed to the disk with a single system call, rather than a system call for each commit. This can greatly improves the throughput of TPS.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Large Transactions <large-transactions>`

   .. rst-class:: list-stats

      Length: 443 words; Published:

   .. rst-class:: list-abstract

      Large transactions, especially ones which delete millions of rows from a table at once, can lead to diminished performance. One reason for this is that the table may be reindexing and rescanning after each row is deleted.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Parallel Slave Threads <parallel-slave-threads>`

   .. rst-class:: list-stats

      Length: 366 words; Published:

   .. rst-class:: list-abstract

      There's no rule for how many slave threads are needed. Parallel threads don't ensure better performance, but they don't impair performance and they may in fact speed up the synchronization of new nodes joining a cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Slow Nodes <detecting-slow-node>`

   .. rst-class:: list-stats

   Length: 297 words; Published:

   .. rst-class:: list-abstract

      By design, cluster performance cannot be higher than the performance of the slowest node in the cluster. Even with only one node, its performance can be considerably slower when compared with running the same server in a stand-alone mode.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`WAN Latency <wan-latency>`

   .. rst-class:: list-stats

      Length: 221 words; Published:

   .. rst-class:: list-abstract

      When using Galera Cluster over a Wide Area Network, links can have exceptionally high latency. It can be checked by taking Round-Trip Time measurements between nodes. It can be corrected by adjusting all of the temporal parameters.


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

      The size of the write-set cache can be defined by the ``gcache.size`` parameter. If you have storage issues, there are some guidelines to consider in adjusting this issue. You could change your state snapshot method.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Write-Set Caching during State Transfers <gcache-during-state-transfers>`

   .. rst-class:: list-stats

      Length: 156 words; Published:

   .. rst-class:: list-abstract

      Normally, nodes don't use much more memory than a stand-alone. The certification index and uncommitted write-sets do drain some. Typically, though, this isn't usually noticeable. Write-set caching during state transfers is the exception.


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

      Although Galera is a true multi-master system, it is possible to designate one node to handle all writes, to be the master for all of the other nodes. To do this, there are certain configuratoin requirements, while some aspects that can be relaxed.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Two-Node Clusters <two-node-clusters>`

   .. rst-class:: list-stats

      Length: 399 words; Published:

   .. rst-class:: list-abstract

      Although it may seem simple to maintain a cluster of only two nodes, there is an inherent potential problem. In a two-node cluster, when one node fails, it may cause problems, to distrupt some processes. Mostly, high availability is no longer ensured.


.. _`kb-best-security`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Security & SQL

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Setting an SELinux Policy <setting-selinux-policy>`

   .. rst-class:: list-stats

      Length: 345 words; Updated: October 20, 2019

   .. rst-class:: list-abstract

      When you first enable Galera Cluster on a node that runs SELinux, it will prohibit all cluster activities.  In order to enable replication on the node, you need a policy so that SELinux can recognize cluster activities as legitimate.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Synchronization Functions <using-sync-functions>`

   .. rst-class:: list-stats

      Length: 391 words; Published:

   .. rst-class:: list-abstract

      An application may need to perform a critical read. Synchronization functions can tie the synchronization process to specific transactions so that the node waits only until a specific transaction is applied before executing the query.


.. toctree::
   :maxdepth: 2
   :hidden:

   node-crash-during-sst
   sst-fails-sql-syntax-error
   requested-state-transfer-failed

   stall-on-alter-table
   user-changes
   auto-increment-multiples

   multi-master-conflicts
   error-unknown-command


   group-commit
   large-transactions
   multi-master-setup
   parallel-slave-threads
   single-master-setup
   setting-selinux-policy
   detecting-slow-node
   using-sync-functions
   two-node-clusters
   wan-latency
   wan-replication
   customizing-gcache-size
   gcache-during-state-transfers


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
