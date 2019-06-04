========================
SQL Syntax Errors
========================
.. _`kb-trouble-sql-syntax-error`:

When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a :term:`State Snapshot Transfer` (SST) method to provide a full data copy to the new node, known as the joiner. To get this snapshot, some administrators opt to use a :term:`Logical State Transfer Method`, in particular ``mysqldump``. This doesn't always work well.


.. rubric:: Scenario
   :class: kb

Suppose a new node joins a cluster and fails to get a copy of the database, the :term:`State Snapshot Transfer` fails using ``mysqldump``. Suppose further you check the database logs (e.g., ``/var/log/mysqld.log``) and you see a message
 mentioned an ``SQL SYNTAX``.


.. rubric:: Troubleshooting
   :class: kb

This SQL statement that was logged is not the actual SQL statement; it's a pseudo-statement.  You can find the actual error message the state transfer returned within the ``SQL SYNTAX`` entry.  It will provide the underlying SQL statement and other informaiton for correcting the problem.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :doc:`SST <../../documentation/sst>`
- :doc:`SST Logical <../../documentation/sst-logical>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
