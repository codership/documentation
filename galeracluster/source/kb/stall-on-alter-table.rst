.. meta::
   :title: Troubleshooting Galera when Stalls on ALTER
   :description: "For huge tables, an ALTER TABLE statement can cause a Galera Cluster to stall. There is a work-around, though."
   :language: en-US
   :keywords: cluster stalls, alter table, performance drain
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

      Related Documents

      - :doc:`Schema Upgrades <../../documentation/schema-upgrades>`
      - :ref:`wsrep_OSU_method <wsrep_OSU_method>`


.. cssclass:: library-article
.. _`kb-trouble-stall-on-alter`:

==================================
Cluster Stalls on ``ALTER TABLE``
==================================

.. rst-class:: article-stats

   Length: 519 words; Updated: October 30, 2019; Category: Schema & SQL; Type: Troubleshooting

The ``ALTER TABLE`` statement requires access to the table to be delayed as the changes are applied, the data sorted and re-indexed.  When executing this SQL statement on a node that using Galera Cluster, the entire cluster may be stalled. It can be confusing and inconvenient.


.. rst-class:: section-heading
.. rubric:: Scenario

Suppose you execute an ``ALTER TABLE`` statement on one node, but it takes a long time to execute |---| at least, much longer than expected. This could be because the table which is being altered contains a huge amount of data and several indexed columns.  While the ``ALTER TABLE`` statement is being processed, all of the other nodes may stall. It could cause a significant performance problem throughout the cluster.

This is a side effect of a multi-master cluster, with several appliers.  The cluster needs to control when a :abbr:`DDL (Data Definition Language)` statement ends in relation to other transactions. It's necessary for the cluster to detect conflicts and then schedule parallel appliers.  Any DDL statement must be executed in isolation. This is known as :term:`Total Order Isolation` or TOI.

Galera Cluster has a 65K window of tolerance for transactions applied in parallel. However, the cluster must wait when an ``ALTER TABLE`` statement take too long.  In a sense, the cluster is paused as it waits for all of the nodes to replicate the ``ALTER TABLE`` statement.


.. rst-class:: section-heading
.. rubric:: Work-Around

Given that stalling due to an ``ALTER TABLE`` statement is a consequence of the intrinsic nature of how replication works with Galera Cluster, there is no direct solution to the problem.  However, you can implement a work-around |---| besides acceptance and patience.

If you're sure that no other session will try to modify the table and that there are no other :abbr:`DDL (Data Definition Language)` statements running, there is something you can do.  You can change the schema upgrade method from :term:`Total Order Isolation` to :term:`Rolling Schema Upgrade` (RSU) before executing the ``ALTER TABLE`` statement. After the ``ALTER TABLE`` is finished, you can switch the upgrade method back to TOI. By doing this, changes will be applied to each node individually, without affecting cluster performance.

Below is an example of what you would enter on each node to do this work-around:

.. code-block:: mysql

   SET wsrep_OSU_method='RSU';

This SQL statement will change the Schema Upgrade method, as mentioned, to *Rolling Schema Upgrade*.  You'll have to execute it on each node since it won't be replicated.  After you've done this on all of the nodes, you can then enter the ``ALTER TABLE`` statement we want to execute:

.. code-block:: mysql

   ALTER TABLE toys
   ADD COLUMN age_range CHAR(10);


This is just a simple example; enter whatever ``ALTER TABLE`` statement you want, but execute it on each node.  Any DDL statements won't be replicated, not even after you reset ``wsrep_OSU_method``.  It's a tedious method, but all other writes and all reads will be allowed.

Once you've finished changing the table schema on each node, execute the ``SET`` statement again to put ``wsrep_OSU_method`` back to ``TOI``:

.. code-block:: mysql

   SET wsrep_OSU_method='TOI';

You'll have to execute this SQL statement on each node.  After that, the cluster should function normally, without any drain on performance.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
