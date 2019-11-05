.. meta::
   :title: Troubleshooting Galera Cluster when it Stalls on ALTER
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

         .. cssclass:: here

         - :doc:`Troubleshooting <./index>`

      .. cssclass:: sub-links

         - :doc:`Best Practices <../best/index>`

      - :doc:`Training <../../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      Related Documents

      - :doc:`Schema Upgrades <../../documentation/schema-upgrades>`
      - :ref:`wsrep_OSU_method <wsrep_OSU_method>`

      Related Articles

.. cssclass:: library-article
.. _`kb-trouble-stall-on-alter`:

==============================
Cluster Stalls on ``ALTER``
==============================

There may be times in which a cluster will stall when an ``ALTER`` statement is executed on an unused table.


.. rst-class:: kb
.. rubric:: Scenario

There may be a situation in which you attempt to execute an ``ALTER`` statement on one node, but it takes a long time to execute--longer than expected.  During that period all of the other nodes may stall, leading to performance problems throughout the cluster.

What's happening is a side effect of a multi-master cluster with several appliers.  The cluster needs to control when a :abbr:`DDL (Data Definition Language)` statement ends in relation to other transactions, in order deterministically to detect conflicts and then schedule parallel appliers.  Basically, the DDL statement must execute in isolation.

Galera Cluster has a 65K window of tolerance for transactions applied in parallel, but the cluster must wait when ``ALTER`` statements take too long.


.. rst-class:: kb
.. rubric:: Solution

Given that stalling due to an ``ALTER`` statement is a consequence of something intrinsic to how replication works in Galera Cluster, there is no direct solution to the problem.  However, you can implement a workaround.

In the event that you can sure that no other session will try to modify the table and that there are no other :abbr:`DDL (Data Definition Language)` statements running, you can shift the schema upgrade method from :term:`Total Order Isolation` to :term:`Rolling Schema Upgrade` for the duration of the ``ALTER`` statement.  This applies the changes to each node individually, without affecting cluster performance.

To run an ``ALTER`` statement in this manner, you will need to execute the ``ALTER`` statement between a paid of ``SET`` statements on each node like so:

   .. code-block:: mysql

      SET wsrep_OSU_method='RSU';

      ALTER TABLE table1
      ADD COLUMN col8 INT;

      SET wsrep_OSU_method='TOI';

The first SQL statement here will change the Schema Upgrade method to *Rolling Schema Upgrade* (i.e., ``RSU``).  The second SQL statement represents an ``ALTER`` statement you want to execute. Once that's finished, the last ``SET`` statement will reset the Schema Upgrade method back to *Total Order Isolation* (i.e., ``TOI``).  After you've done this on each node, the cluster will now run with the desired updates.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
