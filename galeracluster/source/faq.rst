============================
 Frequently Asked Questions
============================
.. _`kb-faq`:

This page lists a number of frequently asked questions on Galera Cluster and other related matters. They include questions you might have before deciding to use Galera. There are some questions on how to install and migrate to Galera, as well as how to get assistance and learn about Galera.


-----------------------------------------------
General Questions
-----------------------------------------------

.. rubric:: What is Galera Cluster?
.. _`faq-what-is-galera-cluster`:

Galera Cluster is a write-set replication service provider in the form of the *dlopenable* library.  It provides synchronous replication and supports multi-master replication.  Galera Cluster is capable of unconstrained parallel applying (i.e., "parallel replication"), multicast replication and automatic node provisioning.

The primary focus of Galera Cluster is data consistency.  Transactions are either applied to every node or not at all.  Galera Cluster is not a cluster manager, a load balancer or a cluster monitor.  What it does is keep databases synchronized, provided they were properly configured and synchronized in the beginning.


.. rubric:: Why use Galera Cluster instead of Basic MySQL Replication?
.. _`faq-why-galera-over-standard-replication`:

Galera Cluster uses a multi-master method of replication. It allows you to write to any node in a cluster; writes on any node are synchronized to all nodes. Standard MySQL replication uses one master and multiple slaves: although you can read data from any node, you can write only on the master.

With Galera and multi-master replication, any write is either committed to all nodes in the cluster, or rolled back.  With standard MySQL and master-slaves replication, writes to the master might not be synchronized to one or more slave, but users could continue to read from an out-of-sync slave.

With Galera, if one master fails, the cluster continues and users can continue to write and read on other nodes.  With standard MySQL replication, if the master fails, users cannot write until it's restored or replaced--which can involve manual intervention and take good bit of time.


.. rubric:: Can Galera be used with AWS (Amazon Web Services)?
.. _`faq-galera-on-aws`:

Yes, it works just fine.  Through Amazon's EC2 environment, you can create multiple instances, virtual servers running the Linux operating system--any distribution is fine.  After the instances are created, you would log into each instance and install MySQL or MariaDB and Galera, as well as configure them. On AWS, you'll have to set inbound security rules to allow the instances to communicate with each.

.. note:: For more details on installing Galera, see :doc:`./training/tutorials/galera-installation`.


.. rubric:: Can nodes for a Galera Cluster be installed in containers such as Docker?
.. _`faq-galera-containers`:



-----------------------------------------------
Learning & Training Questions
-----------------------------------------------

.. rubric:: How popular is Galera Cluster?
.. _`faq-galera-cluster-popularity`:

Galera Cluster is becoming de-facto-standard for MySQL high availability and scalability solution. In 2016, Galera Cluster downloads passed over 1,000,000.

Major companies all over the world have implemented Galera to protect their data and secure their application and service availability. Galera Cluster is included in Debian Linux distributions and it's the most used high availability solution for OpenStack Cloud platform, according their survey.


.. rubric:: How can I learn to configure and use Galera?
.. _`faq-learn-galera`:

The :doc:`./documentation/index` is the best source for detailed information on Galera. It includes a guide for :doc:`./training/tutorials/getting-started`. Several members of the Galera staff occasionally make presentations at conferences around the globe.

For comprehensive training courses on Galera and related software (e.g., load balancers), check the web sites of our partners (e.g., MariaDB, FromDual, Severalnines). For a list of all of them, along with links to their sites, see the `Support Partners <http://galeracluster.com/support/#support-partners>`_

.. rubric:: Are there articles written about Galera?
.. _`faq-galera-articles`:

You can find many articles on Galera and related software on our `blog <http://galeracluster.com/category/blog/>`_. These are mixed in with information on conferences and press releases, so you'll have to scroll through the list of articles.  Some of our partners regularly publish articles on various aspects of Galera: `MariaDB <https://mariadb.com/resources/blog/tag/galera/>`_, `Severalnines <https://severalnines.com/blog/top-mysql-galera-cluster-resources>`_, and `FromDual <https://www.fromdual.com/search/node/galera>`_.



-----------------------------------------------
Assistance Questions
-----------------------------------------------

.. rubric:: Does Codership offer Support?
.. _`faq-codership-offers-support`:

Codership offers 8/5 and 24/7 support to keep your Galera Cluster installation running. Our support staff includes the core developers of Galera technology. As a result, we’re able to pinpoint and resolve problems, quickly and efficiently.

Annual Galera support subscription include:

- Unlimited support tickets;
- Hot bug fixes;
- Security releases;
- New Releases of the software;
- Contact by email, skype or telephone;
- Remote system login;
- Named support contacts (Galera developers):
- Zendesk support portal and ticket management; and
- 8-hour response time for 8/5, 4-hour response time for 24/7

For a quote on the cost of support, write us at info@codership.com or use our on-line form :ref:`to send us a message <http://galeracluster.com/contact-us/#send-us-a-message>`.

You can also engage one of our `Support Partners <http://galeracluster.com/support/#support-partners>`_. We are very particular as to who we allow to become one of our Support Partner:  they're well qualified, very responsive, and dependable.


.. rubric:: Is it possible to get Codership to assist me in migrating to Galera?
.. _`faq-codership-offers-consulting`:

Yes, we can help you remotely or in person.  Our staff at Galera have years of hands-on experience with database replication and clustering, both in development and management. Putting our expertise to use will help you to avoid trial and error, save you time and money, as well as help you to make the right choices for your project. We're available for both short-term and long-term consulting projects

Consulting is usually done remotely. However, if you require in-person, on-site work, there will be extra charges (e.g., travel and accomodation expenses).


.. rubric:: Are there forums for asking for assistance with Galera?
.. _`faq-galera-forums`:

There are a few forums on Galera and related software. On these forums, you can post questions to the community. It may take a little time, but you will usually receive responses to your posts.

We have a forum in which the community, as well as our staff monitor and post responses:  `Codership Forum <http://galeracluster.com/community/>`_. Some of our partners maintain forums on Galera:  `FromDual <https://www.fromdual.com/forum/513>`_.

You can also post questions on forums unaffiliated with Codership or our partners:  `Stack Exchange (DBA Section) <https://dba.stackexchange.com/questions/tagged/galera>`_, `Stack Overflow <https://stackoverflow.com/questions/tagged/galera>`_,



-----------------------------------------------
Installation & Migration Questions
-----------------------------------------------

.. rubric:: If I'm now using MySQL or MariaDB standard replication, will it be easy to start using Galera?
.. _`faq-easy-migration-standard-to-galera`:

It's potentially very easy. There are a few things to consider, changes you may need to make.

First, you'll have to migrate all of your tables to InnoDB. Although MySQL and MariaDB offer multiple storage engines, Galera only allows InnoDB tables. You'll also have to address how changing to InnoDB will affect your applications.

Next, you should also migrate each server to the same version of MySQL or MariaDB, and to the latest versions. This may affect the schema of your tables, as well as your data and applications.

Last, you may want to make some changes to your hardware. For one, if you have only two servers, you should add a third.  Although it's not necessary, it's recommended that all servers used be the same or faily equal in resources.

Basically, if you're already using the latest database software and only InnoDB tables, implementing Galera will be very easy. Otherwise, implementing Galera will require some thought and effort. However, the result will mean a much better cluster:  all servers will be the same for easier maintenance and better performance; they'll be running the latest software, which will provide advantages; and the data will be better protected and will have high availability.


.. rubric:: How are Upgrades Made to a Cluster?
.. _`faq-upgrading-galera`:

Periodically, updates will become available for Galera Cluster--for the database server itself or the :term:`Galera Replication Plugin`.  To update the software for a node, you would redirect client connections away from it and then stop the node. Then upgrade the node's software.  When finished, just restart the node.

.. note:: For more information on upgrade process, see :doc:`./documentation/upgrading`.


.. rubric:: Is Galera Installed Separately from the Database Software?
.. _`faq-galera-installed-serperately`:

Starting with version 10.4 of MariaDB, Galera software is included in the server installation. See the :doc:`./documentation/install-mariadb` related to installing Galera, version 4. Previous version of MariaDB did require you to install separately Galera. The same document will explain this.

If you'd prefer to use MySQL, see :doc:`./documentation/install-mysql` for information on how to install MySQL and Galera software.  Galera is not yet incorporated into MySQL.


.. rubric:: What's the Minimum and Maximum number of Servers in a Galera Cluster?
.. _`faq-min-max-galera-nodes`:

The minimum number of nodes required for a cluster is two.  However, a minimum of three nodes is recommend. In a two-node cluster, if one node fails or it's taken down for maintenance, the other node will stop since another node is required. There is a work around for two-node cluster issues: see :doc:`./kb/best/two-node-clusters`

As for the maximum number of nodes, there is none. However, a single cluster in excessive of ten nodes may experience lag from the synchronizing of so many nodes across a network or the internet. This can be mitigated based on your network configuration, but then other factors come into play.



-----------------------------------------------
Usage Questions
-----------------------------------------------

.. rubric:: Does Galera balance loads?
.. _`faq-galera-load-balancing`:
For high-traffic clusters, to prevent one node from being overwhelmed with write and read queries, you may want to use a load balancer. Galera Cluster doesn't include this feature. However, we could use MariaDB's MaxScale, ProxySQL, or some other such load balancer.

MaxScale is a database proxy that can extend the high availability, scalability, and security of your database server and cluster.  It also simplifies application development by decoupling it from underlying database infrastructure. It will work with both MariaDB and MySQL.


.. rubric:: How are Failovers Managed?
.. _`faq-how-failovers-managed`:

Galera Cluster is a true synchronous multi-master replication system, which allows the use of any or all of the nodes as master at any time without any extra provisioning.  What this means is that there is no failover in the traditional MySQL master-slave sense.

The primary focus of Galera Cluster is data consistency across the nodes.  This doesn't allow for any modifications to the database that may compromise consistency.  For instance, the node rejects write requests until the joining node synchronizes with the cluster and is ready to process requests.

The results of this is that you can safely use your favorite approach to distribute or migrate connections between the nodes without the risk of causing inconsistency.

.. note:: For more information on connection distribution, see :doc:`./documentation/deployment-variants`.


.. rubric:: Are making backups of databases difficult?
.. _`faq-making-backups`:

Making a backup of the databases in a Galera cluster is easy and simple. One simple method would be to remove one node from the cluster--without shutting down the ``mysqld`` daemon.  From there, you can use ``mysqldump`` to make a logical backup, or whatever backup software you prefer.  It will have little or no effect on overall performance of the cluster. When you're finished, simply reconnect the node to the cluster. The other nodes will quickly provide what's needed for it to be insync with the cluster. For more information on using ``mysqldump`` with Galera, see :doc:`./documentation/mysqldump`.

The problem with such a simple backup method, though, is that it lacks a :term:`Global Transaction ID` (GTID).  You can use backups of this kind to recover data, but they are insufficient for use in recovering nodes to a well-defined state.  Plus, some backup procedures can block cluster operations during the backup.

Including the GTID in a backup requires a different approach. To do this, you can invoke a backup through the state snapshot transfer mechanism. For more information on this method, see :doc:`./documentation/backup-cluster`.


.. rubric:: What InnoDB Isolation Levels does Galera Cluster Support?
.. _`faq-isolation-levels`:

You can use all isolation levels.  Locally, in a given node, transaction isolation works as it does natively with InnoDB.

Globally, with transactions processing in separate nodes, Galera Cluster implements a transaction-level called ``SNAPSHOT ISOLATION``.  The ``SNAPSHOT ISOLATION`` level is between the ``REPEATABLE READ`` and ``SERIALIZABLE`` levels.

The ``SERIALIZABLE`` level cannot be guaranteed in the multi-master use case because Galera Cluster replication does not carry a transaction read set.  Also, ``SERIALIZABLE`` transaction is vulnerable to multi-master conflicts.  It holds read locks and any replicated write to read locked row will cause the transaction to abort.  Hence, it is recommended not to use it in Galera Cluster.

.. note:: For more information, see :doc:`./documentation/isolation-levels`.


.. rubric:: How are DDL's Handled by Galera Cluster?
.. _`faq-ddl-handled-galera`:

For :abbr:`DDL (Data Definition Language)` statements and similar queries, Galera Cluster has two modes of execution:

- :term:`Total Order Isolation`: A query is replicated in a statement before executing on the master.  The node waits for all preceding transactions to commit and then all nodes simultaneously execute the transaction in isolation.

- :term:`Rolling Schema Upgrade`: Schema upgrades run locally, blocking only the node on which they are run.  The changes do not replicate to the rest of the cluster.

.. note:: For more information, see :doc:`./documentation/schema-upgrades`.


.. rubric:: Is GCache a Binlog?
.. _`faq-gcache-binlog`:

The :term:`Write-set Cache`, which is also called GCache, is a memory allocator for write-sets.  Its primary purpose is to minimize the write-set footprint in RAM.  It is not a log of events, but rather a cache.

- GCache is not persistent.
- Not every entry in GCache is a write-set.
- Not every write-set in GCache will be committed.
- Write-sets in GCache are not allocated in commit order.
- Write-sets are not an optimal entry for the binlog, since they contain extra information.

Nevertheless, it is possible to construct a binlog out of the write-set cache.


.. rubric:: Should the binary log be enabled with Galera?
.. _`faq-gcache-binlog`:

Standard MySQL replication uses the binary log for replicating. However, Galera doesn't use the binary log.  Nevertheless, there may be situations in which you might want to use point-in-time recovery methods to restore tables or data since the last backup.

You might also want to attach an asynchronous slave to one of your nodes, using standard MySQL replication and set it on a delay.  This can also help with recovering tables and data lost since the last backup was made.


-----------------------------------------------
Questions about Potential Problems
-----------------------------------------------

.. rubric:: What typically Causes a Cluster to Stop?
.. _`faq-what-causes-galera-to-stop`:

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


.. rubric:: What are the Limitations to Galera Cluster?
.. _`faq-what-are-galera-limits`:

Galera Cluster is a superb replication system when using MySQL or MariaDB for your databases.  However, it does have some limits for which you may want to be aware before migrating to it.

First, it runs only on Linux and Unix-like operating systems.  There isn't a Windows version. Within the database server, other than the system tables, which use MyISAM, only InnoDB tables are allowed.  InnoDB is used because it's an excellent transactional storage engine. All tables must have an explicit primary key, either a single or a multi-column index.

.. note:: For more details on limitations, see :doc:`./documentation/differences`.


.. rubric:: Does the slowest node in a Galera Cluster affect the performance of the other nodes?
.. _`faq-slow-node`:

Integral to Galera Cluster replication, the cluster will wait for all of the nodes in the cluster to return the status of certification test before committing transactions or rolling them back.  Because of this, a node that is innundated with traffic will delay that node from replying to the cluster and delay the other nodes as they wait for it to report.

To alleviate this problem, you would make sure that all of the servers the same physically (i.e., amount of RAM, types of network interfaces), or at least have close the same amout of resources available.  You would also use a load balancer (e.g., MariaDB MaxScale, ProxySQL) to make sure one node is not overloaded with traffic.



-----------------------------------------------
Galera Trivia Questions
-----------------------------------------------

.. rubric:: Why is the software called Galera?
.. _`faq-why-called-is-galera`:

The word *galera* is the Italian word for *galley*.  The galley is a class of naval vessel used in the Mediterranean Sea from the second millennium :sub:`B.C.E.` until the Renaissance.  Although it used sails when the winds were favorable, its principal method of propulsion came from banks of oars.

In order to manage the vessel effectively, rowers had to act synchronously, lest the oars become intertwined and became blocked.  Captains could scale the crew up to hundreds of rowers, making the galleys faster and more maneuverable in combat.

.. note:: For more information on galleys, see `Wikipedia <http://en.wikipedia.org/wiki/Galley>`_.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
