.. meta::
   :title: Troubleshooting SST Fails with SQL Syntax Errors
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

      Related Documents

      - :doc:`SST <../../documentation/sst>`
      - :doc:`SST Logical <../../documentation/sst-logical>`
      - :doc:`SST Physical <../../documentation/sst-physical>`
      - :ref:`wsrep_sst_auth <wsrep_sst_auth>`


.. cssclass:: library-article
.. _`kb-trouble-sst-fails-sql-syntax`:

=================================
SST Fails with SQL Syntax Errors
=================================

.. rst-class:: article-stats

   Length: 789 words; Updated: November 7, 2019; Category: State Transfers; Type: Troubleshooting

When a new node joins a cluster, since it has no data, it will request data from the cluster.  This node is known as the joiner.  One of the nodes that's already part of the cluster and synchronized, will provide the joiner with a full copy of all of the databases. This node is know as a donor.  It will use the :term:`State Snapshot Transfer` (SST) method to provide a full data copy to the new node.

For making snapshots to send to a joiner, the donor will use whatever method designated in advanced by the administrator.  This is done by setting the ``wsrep_sst_method`` variable.  There are two basic methods: :term:`Physical State Transfer Method` and :term:`Logical State Transfer Method`.  For the physical method, most use the utility ``rsync``.  For the logical method, there is the utility ``mysqldump``.  The better choice is to use is to use the physical method and ``rsync``. It's faster and more dependable than using ``mysqldump``.

Nevertheless, since ``mysqldump`` is a popular tool for making back-ups of MySQL and MariaDB databases, many administrators opt to use it. Unfortunately, while it's good for back-ups, it doesn't always work well for synchronizing a joiner. Let's consider a common scenario about this.


.. rst-class:: section-heading
.. rubric:: Scenario

Suppose a cluster has been set to use ``mysqldump`` at part of its SST method.  A new node joins the cluster and requests a copy of the databases, but it fails. When checking the database logs (e.g., ``/var/log/mysqld.log``), we see a message saying there is ``SQL Syntax``.

Remember, ``mysqldump`` creates a text file, a dump file which contains a series of SQL statements meant to rebuild all of the databases and tables, and insert data into them. With so many SQL statements, it's normally not surprising.  But if you're following a policy of using the same version of MySQL or MariaDB on all nodes, a dump file created on one node should work without any SQL syntax errors when being restored on another node.


.. rst-class:: section-heading
.. rubric:: Troubleshooting

As described in the scenario above, there will be an entry in the MySQL or MariaDB error log which says that the state transfer failed because of a ``SQL Syntax`` error. The entry won't say what was the problem. You'll have to deduce the actual SQL error from other entries before or after it.  Look at this excerpt from a log file in which SST failed when ``mysqldump`` was being used:

.. code-block:: text

   2019-10-25T09:22:24.315153Z 0: ERROR 1064 (42000) at line 13:
      You have an error in your SQL syntax; ... 'SST failed to complete'

   2019-10-25T09:22:24.315175Z 0: 160505 18:30:28 [ERROR] WSREP:
      Process completed with error:
      wsrep_sst_mysqldump --host '172.16.0.21' ...
         --gtid '9a4c394d-12ee-11e6-9ffc-4e0406bcb751:363': 1
      (Operation not permitted)

   2019-10-25T09:22:24.315179Z 0: 160505 18:30:28 [ERROR] WSREP:
      Try 1/3: 'wsrep_sst_mysqldump --host '172.16.0.21' ...
         --gtid '9a4c394d-12ee-11e6-9ffc-4e0406bcb751:363'' failed: 1
      (Operation not permitted)

   2019-10-25T09:22:24.315183Z 0: mysqldump: Error:
      'Lock wait timeout exceeded; try restarting transaction'
      when trying to dump tablespaces

   2019-10-25T09:22:24.315186Z 0: mysqldump:
      Couldn't execute 'SHOW DATABASES':
      Lock wait timeout exceeded; try restarting transaction (1205)

In this excerpt, the first entry shown mentioned that there was an error related to SQL syntax, and that as a result, SST failed to complete.  Look at the fourth entry. It mentions that it was unable to execute ``SHOW DATABASES``.  That's one of the lowest level SQL statements, requiring almost no privileges, just a user account. The only way you would get that error is if you somehow tried to execute ``SHOW DATABASES`` without actually having a user account.  And that's the problem:  no user privileges.

When using mysqldump for state transfers, you have to provide a user name and password.  Galera doesn't need a user account, otherwise, to function or to do a state transfer using rsync.  But when using mysqldump, one is required.  Without it you get peudo error messages, the SQL syntax error message resulting from mysqldump failing.

To provide a user name and password, you would use the SET statement to store them in the ``wsrep_sst_auth`` like so:

.. code-block:: mysql

   SET GLOBAL wsrep_sst_auth = "admin_backup:Rovert123!";

   SHOW VARIABLES LIKE 'wsrep_sst_auth';

   +----------------+----------+
   | Variable_name  | Value    |
   +----------------+----------+
   | wsrep_sst_auth | ******** |
   +----------------+----------+

As you can see, the user name and password are obscured.  This ``SET`` statement won't be replicated to the other nodes.  You'll have to set the values for ``wsrep_sst_auth`` on each node.  All of this is a reason why most DBAs prefer to use ``rsync`` for state transfers.

If you're determined to use ``mysqldump``, once you've set the user name and password for using ``mysqldump`` to generate a dump file, as well as restoring one, you should be able to use it without much trouble.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
