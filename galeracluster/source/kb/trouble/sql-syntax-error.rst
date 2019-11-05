.. meta::
   :title: Troubleshooting SQL Syntax Errors in Galera Cluster
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

      - :doc:`SST <../../documentation/sst>`
      - :doc:`SST Logical <../../documentation/sst-logical>`

      Related Articles


.. cssclass:: library-article
.. _`kb-trouble-sql-syntax-error`:

========================
SQL Syntax Errors
========================

When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a :term:`State Snapshot Transfer` (SST) method to provide a full data copy to the new node, known as the joiner. To get this snapshot, some administrators opt to use a :term:`Logical State Transfer Method`, in particular ``mysqldump``. This doesn't always work well.


.. rst-class:: kb
.. rubric:: Scenario

Suppose a new node joins a cluster and fails to get a copy of the database, the :term:`State Snapshot Transfer` fails using ``mysqldump``. Suppose further you check the database logs (e.g., ``/var/log/mysqld.log``) and you see a message
 mentioned an ``SQL SYNTAX``.


.. rst-class:: kb
.. rubric:: Troubleshooting

This SQL statement that was logged is not the actual SQL statement; it's a pseudo-statement.  You can find the actual error message the state transfer returned within the ``SQL SYNTAX`` entry.  It will provide the underlying SQL statement and other informaiton for correcting the problem.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
