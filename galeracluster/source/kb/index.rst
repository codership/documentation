.. meta::
   :title: Galera Cluster Knowledge Base
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


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

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-index
.. _`kb`:

=============================
The Codership Knowledge Base
=============================

.. rst-class:: list-stats

   Article Counts: 10 Troubleshooting, 13 Best Practices; Recent Changes: 6 Revised, 2 New Articles

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

      Length: 463 words; Pub: Apr 2014; Revised: Nov 2019

   .. rst-class:: list-abstract

      If a donor node crashes while using ``rsync`` for a state transfers, the joiner node may stall with incomplete databases, and be inaccessibe. This article discusses how to resolve this.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`SST Fails due to SQL Syntax Errors <sst-fails-sql-syntax-error>`

   .. rst-class:: list-stats

      Length: 789 words; Pub: Apr 2014; Revised: Nov 2019

   .. rst-class:: list-abstract

      When using ``mysqldump`` for state transfers for a new node, it may fail. In the database error log, there may be entries that says there were SQL Syntax errors.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Requested State Transfer Failed <requested-state-transfer-failed>`

   .. rst-class:: list-stats

      Length: 649 words; Pub: Apr 2014; Revised: Nov 2019

   .. rst-class:: list-abstract

      When a new node joins a cluster, it will try to get a full copy of the databases from one of the other nodes.  Sometimes its request will be ignored and no node is selected to be the donor.


.. _`kb-trouble-sql-syntax`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Schema & SQL

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Cluster Stalls on ALTER TABLE <stall-on-alter-table>`

   .. rst-class:: list-stats

      Length: 519 words; Pub: Apr 2014; Revised: Oct 2019:

   .. rst-class:: list-abstract

      A cluster will sometimes stall when executing ``ALTER TABLE`` on a table with several columns and indexes. Depending on the number of rows, it can be a major drain on performance.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`User Changes not Replicating <user-changes>`

   .. rst-class:: list-stats

      Length: 518 words; Pub: Apr 2014; Revised: Sep 2019

   .. rst-class:: list-abstract

      Changes to the ``mysql`` database (e.g., user name, host address) are not replicated on other nodes. This can cause problems for users, as well as frustrate the DBA.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`auto-increment-multiples`

   .. rst-class:: list-stats

      Length: 995 words; Pub: Oct 2019

   .. rst-class:: list-abstract

      Key columns using ``AUTO_INCREMENT`` will increase values by more than one with Galera. This can be confusing and worrisome, but this article explains why this is a good method.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`deadlock-found`

   .. rst-class:: list-stats

      Length: 887 words; Pub: Nov 2019

   .. rst-class:: list-abstract

      After starting a transaction involving an SQL statement that changes data, a deadlock error message will be returned indicating another node has already locked the same rows.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`resolve-commit-failure`

   .. rst-class:: list-stats

      Length: 326 words; Pub: Apr 2014; Revised: Nov 2019

   .. rst-class:: list-abstract

      When you have ``wsrep_debug`` turned ``ON``, you may occasionally see a message noting that a commit has failed due to reason ``3``.



.. _`kb-trouble-splits-topology`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Splits & Topology

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Multi-Master Conflicts <multi-master-conflicts>`

   .. rst-class:: list-stats

      Length: 751 words; Pub: Apr 2014

   .. rst-class:: list-abstract

      Multi-master clusters have certain types of conflicts and can involve data inconsistencies among nodes. This article explains the nuances of Galera and how to prevent them.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Unknown Command Errors <error-unknown-command>`

   .. rst-class:: list-stats

      Length: 971 words; Pub: Apr 2014; Revised: Nov 2019

   .. rst-class:: list-abstract

      Instead of receiving results from a valid SQL statement, an error message is returned saying, "Unknown Command" on one node. This error is returned for all queries on the node.


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

      Length: 322 words; Pub: May 2019; Revised: Oct 2019

   .. rst-class:: list-abstract

      When several transactions try to commit simultaneously, ``GROUP COMMIT`` flushes them to the disk with a single system call, rather than a call for each, greatly improving performance.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Large Transactions <large-transactions>`

   .. rst-class:: list-stats

      Length: 443 words; Pub: Apr 2015

   .. rst-class:: list-abstract

      Large transactions can lead to diminished performance. One reason for this is that the table may be reindexing and rescanning after each row is deleted.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Parallel Slave Threads <parallel-slave-threads>`

   .. rst-class:: list-stats

      Length: 366 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      Parallel threads don't ensure better performance, but they don't impair performance and they may actually increase synchronization of new nodes joining a cluster.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Slow Nodes <detecting-slow-node>`

   .. rst-class:: list-stats

   Length: 297 words; Pub: Apr 2014

   .. rst-class:: list-abstract

      By design, cluster performance won't be higher than the slowest node. Even with only one node, its performance can be considerably slower compared to stand-alone mode.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`WAN Latency <wan-latency>`

   .. rst-class:: list-stats

      Length: 221 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      When using Galera over a WAN, links can have exceptionally high latency. Check this by measuring the Round-Trip Time among nodes, and correct it by adjusting temporal parameters.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`WAN Replication <wan-replication>`

   .. rst-class:: list-stats

      Length: 161 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      When running a cluster over a WAN, there may be transient network connectivity failures. To prevent this from partitioning the cluster, try increasing the *keep-alive* timeouts.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Write-Set Cache Size <customizing-gcache-size>`

   .. rst-class:: list-stats

      Length: 467 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      If you have storage issues, there are some guidelines to adjust the ``gcache.size`` parameter, properly. You could also change your state snapshot method.


   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Write-Set Caching during State Transfers <gcache-during-state-transfers>`

   .. rst-class:: list-stats

      Length: 156 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      Galera nodes don't use much more memory than a stand-alone. The certification index and uncommitted write-sets drain some. Write-set caching during state transfers is the exception.


.. _`kb-best-topology`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Topology

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Single Master Setup <single-master-setup>`

   .. rst-class:: list-stats

      Length: 81 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      It's possible to designate one node in a cluster to handle all writes, to be the *master* to the other nodes. To do this, there are certain configuratoin requirements.

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Multi-Master Setup <multi-master-setup>`

   .. rst-class:: list-stats

      Length: 55 words; Pub: Jun 2015

   .. rst-class:: list-abstract

      The more *masters* in a cluster, the higher the probability of certification conflicts. This can lead to undesirable rollbacks and performance degradation.

.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Two-Node Clusters <two-node-clusters>`

   .. rst-class:: list-stats

      Length: 880 words; Pub: Jun 2015; Revised: Nov 2019

   .. rst-class:: list-abstract

      There are potential problems with two-node clusters: A split-brain situation may occur. When one node fails, the remaining node becomes non-operational.


.. _`kb-best-security`:
.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Security & SQL

.. container:: list-col1

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Setting an SELinux Policy <setting-selinux-policy>`

   .. rst-class:: list-stats

      Length: 345 words; Pub: Jun 2015; Revised: Oct 2019

   .. rst-class:: list-abstract

      When you first installing a node, SELinux will prohibit cluster activities. You will need a SELinux policy so it will recognize cluster activities as legitimate.


.. container:: list-col2

   .. rst-class:: rubric-2 list-sub-header
   .. rubric:: :doc:`Synch a Transaction First <sync-transaction-before-another>`

   .. rst-class:: list-stats

      Length: 994 words; Pub: May 2019; Revised: Nov 2019

   .. rst-class:: list-abstract

      When entering a transaction, you may need to ensure a previous transaction has been committed on the current node. Synchronization functions can make this easier to do.


.. toctree::
   :maxdepth: 2
   :hidden:

   node-crash-during-sst
   sst-fails-sql-syntax-error
   requested-state-transfer-failed

   stall-on-alter-table
   user-changes
   auto-increment-multiples
   deadlock-found
   resolve-commit-failure

   multi-master-conflicts
   error-unknown-command


   group-commit
   large-transactions
   parallel-slave-threads
   detecting-slow-node

   wan-latency
   wan-replication
   customizing-gcache-size
   gcache-during-state-transfers

   single-master-setup
   multi-master-setup
   two-node-clusters

   setting-selinux-policy
   sync-transaction-before-another


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
