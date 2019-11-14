.. meta::
   :title: Codership Library Mission & Goals
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`
      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`
   - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-index
.. _`library-new-questions`:

======================================
New Questions for the FAQ
======================================

This page is where we record ideas for new Frequently Asked Questions (i.e., the :doc:`FAQ <../faq>`).  The questions are entered here, perhaps in rough form, in the same categories of the FAQ.  We will answer that later, when we have more time or more information.

If you have any suggestions for new FAQs, please email us at library@galeracluster.com.

.. _`faq-general-pending`:
.. rst-class:: section-heading
.. rubric:: General Questions

.. _`faq-pending-1`:
.. rst-class:: rubric-2
.. rubric:: In simple terms, what is Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   A plugin that allows synchronous multi-master replication for InnoDB tables. It works differently from the standard MySQL replication, which provides Master and Slave structure. The Galera Cluster replication is able to manage true parallel read and write to any cluster node, managing conflicts using a Global Transaction ID mechanism.


.. _`faq-pending-2`:
.. rst-class:: rubric-2
.. rubric:: Is Galera Cluster difficult to install, configure, use, and maintain?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-3`:
.. rst-class:: rubric-2
.. rubric:: Advantages & Disadvantages of Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Among the advantages: synchronous data replication across all nodes; scalability; high availability; auto failover with the database serving requests as long as one node remains active; all nodes are masters so you could read/write on any node. On the other hand there are some limitations to be considered: the replica provided by Galera Cluster currently is available only for InnoDB tables; it does not support explicit lock tables statement (LOCK TABLES, FLUSH TABLES); all tables must have a primary key in order to replicate correctly the DELETE queries and get the same display order for the SELECT queries on all nodes; you will notice an increase in latency for write transactions linearly with the increase of the number of nodes. However there are solutions to minimize the effects of these limitations.


.. _`faq-pending-2a`:
.. rst-class:: rubric-2
.. rubric:: How Synchronous is Galera Cluster?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer. (see https://stackoverflow.com/questions/49430029)


.. _`faq-learning-training-pending`:
.. rst-class:: section-heading
.. rubric:: Learning & Training Questions

.. _`faq-pending-4`:
.. rst-class:: rubric-2
.. rubric:: Are there on-line videos, screencasts or webinars in which I can learn about Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-assistance-pending`:
.. rst-class:: section-heading
.. rubric:: Assistance Questions

No new  questions in this category.


.. _`faq-install-migrate-pending`:
.. rst-class:: section-heading
.. rubric:: Installation & Migration


.. _`faq-pending-5`:
.. rst-class:: rubric-2
.. rubric:: Which database software will work with Galera?  Are they only relational database system, or will a NoSQL system function with Galera?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.



.. _`faq-usage-pending`:
.. rst-class:: section-heading
.. rubric:: Usage Questions

.. _`faq-pending-6`:
.. rst-class:: rubric-2
.. rubric:: How do I make a backup, and will it effect performance?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-7`:
.. rst-class:: rubric-2
.. rubric:: Can nodes for a Galera Cluster be installed in containers such as Docker and how would they interact with each other?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-8`:
.. rst-class:: rubric-2
.. rubric:: What kind of organization would use Galera Cluster?  What size and type?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-9`:
.. rst-class:: rubric-2
.. rubric:: Why three nodes?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   To prevent a peculiar condition called split-brain. Galera Cluster uses a "quorum" mechanism every time suspects a problem on a node and so decide whether or not to exclude it from the cluster. In a 2-node cluster there would not be the majority to make these kinds of decisions. Moreover if a node is excluded, on his return on the cluster, another node may not be available to transfer data because it is busy with an another data alignment. Whereas two of the members are involved in this operation, the presence of the third continues to serve client requests.



.. _`faq-pending-10`:
.. rst-class:: rubric-2
.. rubric:: What is SST and IST?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   There are two different way to get data replica. The State Snapshot Transfer is used to replicate the entire database, e.g. when you add a node to the cluster for the first time. The Incremental State Transfer is used to align smaller portions of the database and uses an internal caching mechanism. After the first State Snapshot Transfer, Galera Cluster prefers to use Incremental State Transfer because it is faster.



.. _`faq-admin-pending`:
.. rst-class:: section-heading
.. rubric:: Administrative Questions

.. _`faq-pending-11`:
.. rst-class:: rubric-2
.. rubric:: What if I decide I don't like Galera and want to migrate to something else?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.



.. _`faq-pending-12`:
.. rst-class:: rubric-2
.. rubric:: How stable is Galera?  Does it fail easily?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.



.. _`faq-pending-13`:
.. rst-class:: rubric-2
.. rubric:: Is there a method by which I can be notified of nodes failing, of the entire cluster down?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-14`:
.. rst-class:: rubric-2
.. rubric:: Is it difficult to add a new node to a cluster? How much trouble is it to take a node down for maintenance and then rejoin the cluster?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-15`:
.. rst-class:: rubric-2
.. rubric:: What's involved in start a cluster after it's been down?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. _`faq-pending-16`:
.. rst-class:: rubric-2
.. rubric:: How are nodes that were temporarily off-line caught up with the cluster?  How are new nodes jump started? (IST, SST, rsync)?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.



.. _`faq-trivia-pending`:
.. rst-class:: section-heading
.. rubric:: Galera Trivia

.. _`faq-pending-17`:
.. rst-class:: rubric-2
.. rubric:: Why is Codership, the maker of Galera based in Finland?  Why are so many software companies and programmers from Scandinavia?

.. rst-class:: list-stats

   Level: Intermediate; Interested: DBAs; Category: General

.. rst-class:: list-abstract

   Some answer.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
