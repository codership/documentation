.. meta::
   :title: Galera Cluster Frequently Asked Questions
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./documentation/index>`
      - :doc:`Knowledge Base <./kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <./kb/trouble/index>`
         - :doc:`Best Practices <./kb/best/index>`

      - :doc:`FAQ <./faq>`
      - :doc:`Training <./training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <./training/tutorials/index>`
         - :doc:`Training Videos <./training/videos/index>`



.. cssclass:: faq-list
.. _`library-faq`:

============================
Frequently Asked Questions
============================

This page lists several frequently asked questions on Galera Cluster and related matters. They include questions you might have before deciding to use Galera. There are some questions on how to install and migrate to Galera, as well as how to get assistance and learn about Galera.

The questions are grouped by a few categories:

- :ref:`General Questions <faq-general-questions>`
- :ref:`Learning & Training Questions <faq-learning-questions>`
- :ref:`Assistance Questions <faq-assistance-questions>`
- :ref:`Installation & Migration Questions <faq-installation-migration-questions>`
- :ref:`Usage Questions <faq-usage-questions>`
- :ref:`Administrative Questions <faq-administrative-questions>`
- :ref:`Galera Trivia Questions <faq-trivial-questions>`

Just below each question is further categorization of the question: the minimum experience level of the person who might be interested |---| if you're new to database clusters, you might want to skip the Intermediate ones; and the type of person who might be interested in such a question (e.g., DBAs, business managers).


.. _`faq-general-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: General Questions

.. _`faq-what-is-galera-cluster`:
.. rst-class:: rubric-2
.. rubric:: What is Galera Cluster?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Galera Cluster is a write-set replication service provider in the form of the *dlopenable* library.  It provides synchronous replication and supports multi-master replication.  Galera Cluster is capable of unconstrained parallel applying (i.e., "parallel replication"), multicast replication and automatic node provisioning.

   The primary focus of Galera Cluster is data consistency.  Transactions are either applied to every node or not at all.  Galera Cluster is not a cluster manager, a load balancer, or a cluster monitor.  What it does is keep databases synchronized, provided they were properly configured and synchronized in the beginning.


.. _`faq-why-galera-over-standard-replication`:
.. rst-class:: rubric-2
.. rubric:: Why use Galera Cluster instead of Basic MySQL Replication?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs, Business Managers; Category: General

.. rst-class:: list-abstract

   Galera Cluster uses a multi-master method of replication. It allows you to write to any node in a cluster; writes on any node are synchronized to all nodes. Standard MySQL replication uses one master and multiple slaves: although you can read data from any node, you can write only on the master.

   With Galera and multi-master replication, any write is either committed to all nodes in the cluster, or rolled back.  With standard MySQL and master-slaves replication, writes to the master might not be synchronized to one or more slave, but users could continue to read from an out-of-sync slave.

   With Galera, if one master fails, the cluster continues and users can continue to write and read on other nodes.  With standard MySQL replication, if the master fails, users cannot write until it's restored or replaced--which can involve manual intervention and take good bit of time.


.. _`faq-galera-on-aws`:
.. rst-class:: rubric-2
.. rubric:: Can Galera be used with AWS (Amazon Web Services)?

.. rst-class:: list-stats

   Level: Newcomer, Intermediate; Interested: DBAs, Business Managers; Category: General

.. rst-class:: list-abstract

   Yes, it works just fine. Through Amazon's EC2 environment, you can create multiple instances, virtual servers running the Linux operating system--any distribution is fine.  After the instances are created, you would log into each instance and install MySQL or MariaDB and Galera, as well as configure them. On AWS, you'll have to set inbound security rules to allow the instances to communicate with each.

   For more details on installing Galera, see :doc:`Installing Galera <./training/tutorials/galera-installation>`.


.. _`faq-galera-cost`:
.. rst-class:: rubric-2
.. rubric:: How much does Galera Software Cost?

.. rst-class:: list-stats

   Level: Newcomer; Interested: Business Managers; Category: General

.. rst-class:: list-abstract

   Galera Cluster software is free to download and use, along with MySQL and MariaDB software for the database component of a cluster. There are no licensing fees.

   The only expense might be the cost of personnel who are in charge of managing a cluster. You might also decide to engage Codership to provide support (see :ref:`Question on Support <faq-codership-offers-support>`).


.. _`faq-large-galera-organizations`:
.. rst-class:: rubric-2
.. rubric:: Which Large Organizations are using Galera Cluster?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: General

.. rst-class:: list-abstract

   Since 2009, there are thousands of Galera Cluster users and over 1.5 million downloads. Enterprises choose Galera Cluster because it provides most robust solution against data loss, MySQL and MariaDB high availability and scalability.

   Because of client confidentiality, we can't name the largest organizations that are using Galera, but there are a few that have agreed to endorsing us. Check out our `References <http://galeracluster.com/references/>`_ page for just a few.


.. _`faq-try-galera`:
.. rst-class:: rubric-2
.. rubric:: How can I Try Galera to see if I Like It?

.. rst-class:: list-stats

   Level: All; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Since the software is free, it costs you only a little bit of time to try the software. To start, you might want to set up three new servers to be part of a cluster. If you have an account with Amazon's AWS, you could create three instances in there system, just for testing Galera. See :ref:`the Question on Using AWS <faq-codership-offers-support>`.

   If you want to see how well it performs, you might copy your existing databases to your test cluster.  See :ref:`Data Migration <migrate-data>` for more details on how you might do that.  You can also use a benchmark tool like, ``sysbench`` (see `How to Benchmark Performance <https://severalnines.com/blog/how-benchmark-performance-mysql-mariadb-using-sysbench>`_) to test Galera.



.. _`faq-learning-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Learning & Training Questions

.. _`faq-galera-cluster-popularity`:
.. rst-class:: rubric-2
.. rubric:: How Popular is Galera Cluster? Will I be able to Find People we Need?

.. rst-class:: list-stats

   Level: All; Interested: Business Managers; Category: Training

.. rst-class:: list-abstract

   Galera Cluster is becoming de-facto-standard for MySQL high availability and scalability solution. In 2016, Galera Cluster downloads passed over 1,000,000.

   Major companies all over the world have implemented Galera to protect their data and secure their application and service availability. Galera Cluster is included in Debian Linux distributions and it's the most used high availability solution for OpenStack Cloud platform, according their survey.


.. _`faq-learn-galera`:
.. rst-class:: rubric-2
.. rubric:: How can I or my Staff Learn to Configure and Use Galera?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: Learning

.. rst-class:: list-abstract

   The :doc:`Galera Cluster Documentation <./documentation/index>` is the best source for detailed information on Galera. It includes a guide for :doc:`Getting Started Guide <./training/tutorials/getting-started>`. Several members of the Galera staff occasionally make presentations at conferences around the globe.

   For comprehensive training courses on Galera and related software (e.g., load balancers), check the web sites of our partners (e.g., MariaDB, FromDual, Severalnines). For a list of all of them, along with links to their sites, see the `Support Partners <http://galeracluster.com/support/#support-partners>`_


.. _`faq-previous-skills-needed`:
.. rst-class:: rubric-2
.. rubric:: What Skills should I or my Staff have Before Learning Galera?

.. rst-class:: list-stats

   Level: Newcomer, Intermediate; Interested: DBAs; Category: Learning

.. rst-class:: list-abstract

   At a minimum, you should know well a relational database system. In particular, advanced knowledge of MySQL or MariaDB would be best.  This is because Galera is an extension of these relational database systems.

   Since Galera uses only the InnoDB tables, knowing how get the most of the InnoDB storage engine will server you well when resolving problems that may occur with transactions and when tweaking a database for better performance.

   Lastly, experience using standard MySQL Replication would make learning Galera Cluster easy. Galera Cluster is similar, but much better.


.. _`faq-train-which-staff`:
.. rst-class:: rubric-2
.. rubric:: Which of our Staff should be Experts on Galera?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: Training

.. rst-class:: list-abstract

   Since end-users won't do anything different from what they already do when adding and changing data in the database, there's nothing new for them to know.  As for database developers, they mostly need to be aware that they can use only InnoDB tables. They can't use other storage engines.  If they don't already, they might want to learn about the features of InnoDB so they can take advantage of them (e.g., transactions).

   Using Galera Cluster will very much be in the purview of DBAs. They need to know how to create a Galera Cluster, how to add and remove nodes from a cluster. Most importantly, they need to be able to restart a cluster properly so data isn't at risk.

   Galera Cluster isn't difficult to maintain, but your DBAs need to know the software well and be confident in their abilities to resolve problems that might occur to be able to ensure high availability of your databases, the consistency and durability of the data. For critical situations, though, you might do well to have a support contract with us at Codership (see :ref:`Question on Support <faq-codership-offers-support>`).


.. _`faq-galera-articles`:
.. rst-class:: rubric-2
.. rubric:: Are there Tutorial Articles Written about Galera?

.. rst-class:: list-stats

   Level: Newcomer, Intermediate; Interested: DBAs; Category: Learning

.. rst-class:: list-abstract

   You can find many articles on Galera and related software on our `blog <http://galeracluster.com/category/blog/>`_. These are mixed in with information on conferences and press releases, so you'll have to scroll through the list of articles.  Some of our partners regularly publish articles on various aspects of Galera: `MariaDB <https://mariadb.com/resources/blog/tag/galera/>`_, `Severalnines <https://severalnines.com/blog/top-mysql-galera-cluster-resources>`_, and `FromDual Articles <https://www.fromdual.com/search/node/galera>`_.


.. _`faq-train-developers`:
.. rst-class:: rubric-2
.. rubric:: Do Developers and others Users Need to Know Anything about Galera?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: Training

.. rst-class:: list-abstract

   In a way, Galera is a behind-the-scene feature.  It's seamless and very much hidden from users. A developer may access any node in a Galera cluster to change table schemata.

   Developers just need to be mindful to use only InnoDB tables. You can guard against this by setting the ``--default-storage-engine option`` and ``enforce_storage_engine`` to InnoDB. Be sure to disable ``enforce_storage_engine``, though, when upgrading the database software.

   Users would insert or change data in a database the same as they would on a stand-alone database server not using Galera or replication. There's no extra login requirements, interfaces, or methods to use a database running on Galera Cluster. Users will be unaware that you're using Galera Cluster |---| other than maybe noticing that your database is much more dependable.



.. _`faq-assistance-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Assistance Questions

.. _`faq-codership-offers-support`:
.. rst-class:: rubric-2
.. rubric:: Does Codership Offer Support?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: Support

.. rst-class:: list-abstract

   Codership offers 8/5 and 24/7 support to keep your Galera Cluster installation running. Our support staff includes the core developers of Galera technology. As a result, we’re able to pinpoint and resolve problems, quickly and efficiently.

   Annual Galera support subscription include:

   - Unlimited support tickets;
   - Hot bug fixes;
   - Security releases;
   - New Releases of the software;
   - Contact by email, Skype or telephone;
   - Remote system login;
   - Named support contacts (Galera developers):
   - Zendesk support portal and ticket management; and
   - 8-hour response time for 8/5, 4-hour response time for 24/7

   For a quote on the cost of support, write us at info@codership.com or use our on-line form `to send us a message <http://galeracluster.com/contact-us/#send-us-a-message>`_.

   You can also engage one of our `Support Partners <http://galeracluster.com/support/#support-partners>`_. We are very particular as to who we allow to become one of our Support Partner:  they're well qualified, very responsive, and dependable.


.. _`faq-codership-offers-consulting`:
.. rst-class:: rubric-2
.. rubric:: Is it Possible to get Codership to Assist Us in Migrating to Galera?

.. rst-class:: list-stats

   Level: All; Interested: DBAs, Business Managers; Category: Consulting

.. rst-class:: list-abstract

   Yes, we can help you remotely or in person.  Our staff at Galera have years of hands-on experience with database replication and clustering, both in development and management. Putting our expertise to use will help you to avoid trial and error, save you time and money, as well as help you to make the right choices for your project. We're available for both short-term and long-term consulting projects

   Consulting is usually done remotely. However, if you require in-person, on-site work, there will be extra charges (e.g., travel and accomodation expenses).


.. _`faq-galera-forums`:
.. rst-class:: rubric-2
.. rubric:: Are there Forums for Asking for Assistance with Galera?

.. rst-class:: list-stats

   Level: Newcomers; Interested: DBAs; Category: Assistance

.. rst-class:: list-abstract

   There are a few forums on Galera and related software. On these forums, you can post questions to the community. It may take a little time, but you will usually receive responses to your posts.

   We have a forum in which the community, as well as our staff monitor and post responses:  `Codership Forum <http://galeracluster.com/community/>`_. Some of our partners maintain forums on Galera:  `FromDual Forum <https://www.fromdual.com/forum/513>`_.

   You can also post questions on forums unaffiliated with Codership or our partners:  `Stack Exchange (DBA Section) <https://dba.stackexchange.com/questions/tagged/galera>`_, `Stack Overflow <https://stackoverflow.com/questions/tagged/galera>`_,



.. _`faq-installation-migration-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Installation & Migration Questions

.. _`faq-easy-migration-standard-to-galera`:
.. rst-class:: rubric-2
.. rubric:: If I'm now using MySQL Standard Replication, will it be Easy to Switch to Galera?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs; Category: Installation

.. rst-class:: list-abstract

   It's potentially very easy. There are a few things to consider, changes you may need to make.

   First, you'll have to migrate all of your tables to InnoDB. Although MySQL and MariaDB offer multiple storage engines, Galera only allows InnoDB tables. You'll also have to address how changing to InnoDB will affect your applications.

   Next, you should also migrate each server to the same version of MySQL or MariaDB, and to the latest versions. This may affect the schema of your tables, as well as your data and applications.

   Last, you may want to make some changes to your hardware. For one, if you have only two servers, you should add a third.  Although it's not necessary, it's recommended that all servers used be the same or faily equal in resources.

   Basically, if you're already using the latest database software and only InnoDB tables, implementing Galera will be very easy. Otherwise, implementing Galera will require some thought and effort. However, the result will mean a much better cluster:  all servers will be the same for easier maintenance and better performance; they'll be running the latest software, which will provide advantages; and the data will be better protected and will have high availability.


.. _`faq-upgrading-galera`:
.. rst-class:: rubric-2
.. rubric:: How are Upgrades Made to a Cluster?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: Upgrading

.. rst-class:: list-abstract

   Periodically, updates will become available for Galera Cluster--for the database server itself or the :term:`Galera Replication Plugin`.  To update the software for a node, you would redirect client connections away from it and then stop the node. Then upgrade the node's software.  When finished, just restart the node.

   For more information on upgrade process, see :doc:`Upgrading Galera Cluster <./documentation/upgrading>`.


.. _`faq-change-apps`:
.. rst-class:: rubric-2
.. rubric:: Do we have to Adjust our Databases or Custom Applications (e.g., PHP Programs)?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs, Developers; Category: Migrating

.. rst-class:: list-abstract

   If you're already using MySQL or MariaDB, along with some custom applications |---| such as programs written in PHP, Perl, Ruby, or another language, that interface with your databases |---| you shouldn't have to make any changes to your software.

   If you're currently using standard MySQL Replication, and your applications connect with specific nodes for writes and others for reads, you probably won't have to do that. Instead, you can write and read to the same nodes. As for load balancing, you could add a load balancer like MaxScale and then direct all traffic to the load balancer and it will direct the traffic for the best performance.



.. _`faq-galera-installed-serperately`:
.. rst-class:: rubric-2
.. rubric:: Is Galera Installed Separately from the Database Software?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs; Category: Installation

.. rst-class:: list-abstract

   Starting with version 10.4 of MariaDB, Galera software is included in the server installation. See the :doc:`Installing MariaDB Galera Cluster <./documentation/install-mariadb>` related to installing Galera, version 4. Previous version of MariaDB did require you to install separately Galera. The same document will explain this.

   If you'd prefer to use MySQL, see :doc:`Installing MySQL Galera Cluster <./documentation/install-mysql>` for information on how to install MySQL and Galera software.  Galera is not yet incorporated into MySQL.


.. _`faq-min-max-galera-nodes`:
.. rst-class:: rubric-2
.. rubric:: What's the Minimum and Maximum Number of Servers in a Galera Cluster?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs; Category: Installation

.. rst-class:: list-abstract

   The minimum number of nodes required for a cluster is two.  However, a minimum of three nodes is recommend. In a two-node cluster, if one node fails or it's taken down for maintenance, the other node will stop since another node is required. There is a work around for two-node cluster issues: see :doc:`Two-Node Clusters <./kb/best/two-node-clusters>`

   As for the maximum number of nodes, there is none. However, a single cluster in excessive of ten nodes may experience lag from the synchronizing of so many nodes across a network or the internet. This can be mitigated based on your network configuration, but then other factors come into play.


.. _`faq-min-galera-equipment`:
.. rst-class:: rubric-2
.. rubric:: What Type of Server or Equipment is Recommended for a Galera Cluster?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs; Category: Installation

.. rst-class:: list-abstract

   Galera runs only on Linux and similar Unix-like operating systems. Physically, any server on which Linux can be installed, may be used as a node in a Galera cluster.  Galera and the storage engine, InnoDB make good use of RAM and Swap Space.  So, the more memory you can allocate, the better.  Since a cluster runs across a network, get the fastest, best ethernet cards you can get.

   The best equipment you can afford to buy, the better. If you're using virtual servers like those through Amazon's AWS, you don't need to be concerned about most of these equipment factors. You will just need to allow your servers enough memory and storage space.

   However you build your server nodes, it's best that they be equal in all ways: physical and virtual equipment; operating system configuration; software installation.



.. _`faq-usage-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Usage Questions

.. _`faq-galera-load-balancing`:
.. rst-class:: rubric-2
.. rubric:: Does Galera Balance Loads?

.. rst-class:: list-stats

   Level: Advanced; Interested: DBAs; Category: Performance

.. rst-class:: list-abstract

   For high-traffic clusters, to prevent one node from being overwhelmed with write and read queries, you may want to use a load balancer. Galera Cluster doesn't include this feature. However, we could use MariaDB's MaxScale, ProxySQL, or some other such load balancer.

   MaxScale is a database proxy that can extend the high availability, scalability, and security of your database server and cluster.  It also simplifies application development by decoupling it from underlying database infrastructure. It will work with both MariaDB and MySQL.


.. _`faq-how-failovers-managed`:
.. rst-class:: rubric-2
.. rubric:: How are Failovers Managed?

.. rst-class:: list-stats

   Level: Advanced; Interested: DBAs; Category: Maintenance

.. rst-class:: list-abstract

   Galera Cluster is a true synchronous multi-master replication system, which allows the use of any or all of the nodes as master at any time without any extra provisioning.  What this means is that there is no failover in the traditional MySQL master-slave sense.

   The primary focus of Galera Cluster is data consistency across the nodes.  This doesn't allow for any modifications to the database that may compromise consistency.  For instance, the node rejects write requests until the joining node synchronizes with the cluster and is ready to process requests.

   The results of this is that you can safely use your favorite approach to distribute or migrate connections between the nodes without the risk of causing inconsistency.

   For more information on connection distribution, see :doc:`Deployment Variants <./documentation/deployment-variants>`.


.. _`faq-making-backups`:
.. rst-class:: rubric-2
.. rubric:: Are making Back-ups of Databases Difficult?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: Maintenance

.. rst-class:: list-abstract

   Making a backup of the databases in a Galera cluster is easy and simple. One simple method would be to remove one node from the cluster--without shutting down the ``mysqld`` daemon.  From there, you can use ``mysqldump`` to make a logical backup, or whatever backup software you prefer.  It will have little or no effect on overall performance of the cluster. When you're finished, simply reconnect the node to the cluster. The other nodes will quickly provide what's needed for it to be insync with the cluster. For more information on using ``mysqldump`` with Galera, see :doc:`mysqldump <./documentation/mysqldump>`.

   The problem with such a simple backup method, though, is that it lacks a :term:`Global Transaction ID` (GTID).  You can use backups of this kind to recover data, but they are insufficient for use in recovering nodes to a well-defined state.  Plus, some backup procedures can block cluster operations during the backup.

   Including the GTID in a backup requires a different approach. To do this, you can invoke a backup through the state snapshot transfer mechanism. For more information on this method, see :doc:`Backing Up Cluster Data <./documentation/backup-cluster>`.


.. _`faq-isolation-levels`:
.. rst-class:: rubric-2
.. rubric:: Which InnoDB Isolation Levels does Galera Cluster Support?

.. rst-class:: list-stats

   Level: Advanced; Interested: DBAs; Category: Performance

.. rst-class:: list-abstract

   You can use all isolation levels.  Locally, in a given node, transaction isolation works as it does natively with InnoDB.

   Globally, with transactions processing in separate nodes, Galera Cluster implements a transaction-level called ``SNAPSHOT ISOLATION``.  The ``SNAPSHOT ISOLATION`` level is between the ``REPEATABLE READ`` and ``SERIALIZABLE`` levels.

   The ``SERIALIZABLE`` level cannot be guaranteed in the multi-master use case because Galera Cluster replication does not carry a transaction read set.  Also, ``SERIALIZABLE`` transaction is vulnerable to multi-master conflicts.  It holds read locks and any replicated write to read locked row will cause the transaction to abort. Hence, it is recommended not to use it in Galera Cluster.

   For more information, see :doc:`./documentation/isolation-levels`.


.. _`faq-ddl-handled-galera`:
.. rst-class:: rubric-2
.. rubric:: How are DDL's Handled by Galera?

.. rst-class:: list-stats

   Level: Advanced; Interested: DBAs; Category: Maintenance

.. rst-class:: list-abstract

   For :abbr:`DDL (Data Definition Language)` statements and similar queries, Galera Cluster has two modes of execution:

   - :term:`Total Order Isolation`: A query is replicated in a statement before executing on the master. The node waits for all preceding transactions to commit and then all nodes simultaneously execute the transaction in isolation.

   - :term:`Rolling Schema Upgrade`: Schema upgrades run locally, blocking only the node on which they are run.  The changes do not replicate to the rest of the cluster.

   For more information, see :doc:`./documentation/schema-upgrades`.


.. _`faq-gcache-binlog`:
.. rst-class:: rubric-2
.. rubric:: Is GCache a Binary Log?

.. rst-class:: list-stats

   Level: Advanced; Interested: DBAs; Category: Performance

.. rst-class:: list-abstract

   The :term:`Write-set Cache`, which is also called *GCache*, is a memory allocator for write-sets.  Its primary purpose is to minimize the write-set footprint in RAM.  It is not a log of events, but rather a cache.

   - GCache is not persistent.
   - Not every entry in GCache is a write-set.
   - Not every write-set in GCache will be committed.
   - Write-sets in GCache are not allocated in commit order.
   - Write-sets are not an optimal entry for the binlog, since they contain extra information.

   Nevertheless, it is possible to construct a binlog out of the write-set cache.


.. _`faq-enable-binlog`:
.. rst-class:: rubric-2
.. rubric:: Should the Binary Log be Enabled with Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: Maintenance

.. rst-class:: list-abstract

   Standard MySQL replication uses the binary log for replicating. However, Galera doesn't use the binary log.  Nevertheless, there may be situations in which you might want to use point-in-time recovery methods to restore tables or data since the last backup.

   You might also want to attach an asynchronous slave to one of your nodes, using standard MySQL replication and set it on a delay.  This can also help with recovering tables and data lost since the last backup was made.



.. _`faq-administrative-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Administrative Questions

.. _`faq-what-causes-galera-to-stop`:
.. rst-class:: rubric-2
.. rubric:: What typically Causes a Cluster to Stop?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs, Business Managers; Category: Maintenance

.. rst-class:: list-abstract

   Although it doesn't happen often, there are several reasons a Galera cluster might crash. Below is a list of them, grouped by type of cause:

   **Physical Server & Related Causes**

   - The nodes are out of disk space;
   - The operating systems are swapping or have a high I/O Wait

   **Storage Engine Causes**

   - The InnoDB storage engine crashes;
   - Using MyISAM tables, which is still experimental;
   - Creating or dropping tables that don't have a primary key

   **Configuration Problems**

   - Incompatible Changes to Parameters in the MySQL Configuration File;
   - Setting binlog_format to only MIXED, instead of ROW. Only ROW format is supported.

   **Galera in General**

   - Excessive deadlocks during heavy load when writing the same set of rows;
   - There isn't a Primary Component;
   - The cluster is out of quorum;
   - A bug with Galera software


.. _`faq-what-are-galera-limits`:
.. rst-class:: rubric-2
.. rubric:: What are the Limitations of Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs, Business Managers; Category: Maintenance

.. rst-class:: list-abstract

   Galera Cluster is a superb replication system when using MySQL or MariaDB for your databases.  However, it does have some limits for which you may want to be aware before migrating to it.

   First, it runs only on Linux and Unix-like operating systems.  There isn't a Windows version. Within the database server, other than the system tables, which use MyISAM, only InnoDB tables are allowed.  InnoDB is used because it's an excellent transactional storage engine. All tables must have an explicit primary key, either a single or a multi-column index.

   For more details on limitations, see :doc:`./training/tutorials/differences`.


.. _`faq-slow-node`:
.. rst-class:: rubric-2
.. rubric:: Does the Slowest Node Affect the Performance of Other Nodes?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: Performance

.. rst-class:: list-abstract

   Integral to Galera Cluster replication, the cluster will wait for all of the nodes in the cluster to return the status of certification test before committing transactions or rolling them back.  Because of this, a node that is inundated with traffic will delay that node from replying to the cluster and delay the other nodes as they wait for it to report.

   To alleviate this problem, you would make sure that all of the servers the same physically (i.e., amount of RAM, types of network interfaces), or at least have close the same amount of resources available.  You would also use a load balancer (e.g., MariaDB MaxScale, ProxySQL) to make sure one node is not overloaded with traffic.



.. _`faq-trivial-questions`:
.. rst-class:: rubric-1 rubric-separated
.. rubric:: Galera Trivia Questions

.. _`faq-why-called-is-galera`:
.. rst-class:: rubric-2
.. rubric:: Why is the Software Called Galera?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs, Business Managers; Category: Background

.. rst-class:: list-abstract

   The word *galera* is the Italian word for *galley*.  The galley is a class of naval vessel used in the Mediterranean Sea from the second millennium :sub:`B.C.E.` until the Renaissance.  Although it used sails when the winds were favorable, its principal method of propulsion came from banks of oars.

   In order to manage the vessel effectively, rowers had to act synchronously, lest the oars become intertwined and became blocked.  Captains could scale the crew up to hundreds of rowers, making the galleys faster and more maneuverable in combat.

   For more information on galleys, see `Wikipedia <http://en.wikipedia.org/wiki/Galley>`_.


.. _`faq-galera-license`:
.. rst-class:: rubric-2
.. rubric:: How is Galera Licensed and is it Open-Source?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs, Business Managers; Category: Background

.. rst-class:: list-abstract

   The Galera software is licensed under the GNU General Public License, version 2 (see `GPL vs. 2 <https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html>`_).  It's open-source software, which can be found at GitHub (see `Codership Github <https://github.com/codership>`_).


.. _`faq-how-codership-started`:
.. rst-class:: rubric-2
.. rubric:: How did Galera Start?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs, Business Managers; Category: Background

.. rst-class:: list-abstract

   Having worked for years with databases and with data clustering environments, the founders all knew each other. Every now and then they would meet and talk about the technology, about their work. In particular, they discussed the shortcomings and pitfalls of the existing solutions available.

   During these discussions, one thing became apparent: They all shared a need to produce something better, something that ”just works”. In May 2007, they released Galera Cluster for MySQL, their new, fast and scalable data replication and clustering solution for open source databases.


.. _`faq-who-owns-galera`:
.. rst-class:: rubric-2
.. rubric:: Who Owns and Develops Galera Software?

.. rst-class:: list-stats

   Level: Newcomer; Interested: DBAs, Business Managers; Category: Background

.. rst-class:: list-abstract

   Galera Cluster software is the intellectural property of Codership Oy of Finland.  The primary owners of Codership are actively involved in the executive management and development of the software.  For more information on copyrights and other legal aspects, see :doc:`./documentation/legal-notice`.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
