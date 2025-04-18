.. meta::
   :title: Handling Multi-Primary Conflicts in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :doc:`Certification Based Replication <../../documentation/certification-based-replication>`
      - :ref:`cert.log_conflicts <cert.log_conflicts>`
      - :ref:`wsrep_debug <wsrep_debug>`
      - :ref:`wsrep_local_bf_aborts <wsrep_local_bf_aborts>`
      - :ref:`wsrep_local_cert_failures <wsrep_local_cert_failures>`
      - :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-multi-master-conflicts`:

======================================
Multi-Primary Conflicts
======================================

.. rst-class:: article-stats

   Length: 751 words; Published: April 1, 2014; Updated: October 7, 2019; Category: Splits & Topology; Type: Troubleshooting

These types of conflicts relate to multi-primary database environments and typically involve inconsistencies of row amongst nodes.

.. rst-class:: section-heading
.. rubric:: Scenario

To understand this better, consider a situation in a multi-primary replication system in which users can submit updates to any database node. There may be an instance in which two nodes attempt to change the same row in a database, but with different values. Galera Cluster copes with situations such as this by using certification-based replication.


.. rst-class:: section-heading
.. rubric:: Troubleshooting

There are a few techniques available to log and monitor problems that may indicate multi-primary conflicts. They can be enabled with the :ref:`wsrep_debug <wsrep_debug>` option. This instructs the node to include additional debugging information in the server output log. You can enable it through the configuration file with a line like so:

.. code-block:: ini

   wsrep_debug=ON

Once you turn debugging on, you can use monitoring software to watch for row conflicts. Below is an example of a log entry that indicates a conflict as described above:

.. code-block:: text

   110906 17:45:01 [Note] WSREP:
       BF kill (1, seqno: 16962377), victim:
       (140588996478720 4) trx: 35525064
   110906 17:45:01 [Note] WSREP:
       Aborting query: commit
   110906 17:45:01 [Note] WSREP:
       kill trx QUERY_COMMITTING for 35525064
   110906 17:45:01 [Note] WSREP:
       commit failed for reason: 3, seqno: -1


.. warning:: In addition to useful debugging information, this parameter also causes the database server to print authentication information, (that is, passwords), to the error logs. Do not enable it in production environments.

If you develop your own notification system, you can use status variables to watch for conflicts. Below is an example of how you might manually retrieve this information. You would simply incorporate something similar into your scripts or customized program.

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_bf_aborts';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_local_bf_aborts | 333   |
   +-----------------------+-------+

   SHOW STATUS LIKE 'wsrep_local_cert_failures';

   +---------------------------+-------+
   | Variable_name             | Value |
   +---------------------------+-------+
   | wsrep_local_cert_failures | 333   |
   +---------------------------+-------+

:ref:`wsrep_local_bf_aborts <wsrep_local_bf_aborts>` returns the total number of local transactions aborted by replica transactions while in execution. :ref:`wsrep_local_cert_failures <wsrep_local_cert_failures>` provides the total number of transactions that have failed certification tests.

You can enable conflict logging features with :ref:`wsrep_log_conflicts <wsrep_log_conflicts>` and :ref:`cert.log_conflicts <cert.log_conflicts>`. Just add the following lines to the configuration file (that is, ``my.cnf``):

.. code-block:: ini

   wsrep_log_conflicts=ON
   wsrep_provider_options="cert.log_conflicts=YES"

These parameters enable different forms of conflict logging on the database server. When turned on, the node logs additional information about the conflicts it encounters. For instance, it will log the name of the table and schema where the conflict occurred and the actual values for the keys that produced the conflict. Below is an example of such a log entry:

.. code-block:: text

   7:51:13 [Note] WSREP: trx conflict for key (1,FLAT8)056eac38 0989cb96:
   source: cdeae866-d4a8-11e3-bd84-479ea1a1e941 version: 3 local: 1 state:
   MUST_ABORT flags: 1 conn_id: 160285 trx_id: 29755710 seqnos (l: 643424,
   g: 8749173, s: 8749171, d: 8749171, ts: 12637975935482109) <--X-->
   source: 5af493da-d4ab-11e3-bfe0-16ba14bdca37 version: 3 local: 0 state:
   APPLYING flags: 1 conn_id: 157852 trx_id: 26224969 seqnos (l: 643423,
   g: 8749172, s: 8749171, d: 8749170, ts: 12637839897662340)


.. rst-class:: section-heading
.. rubric:: Solution

When two transactions are conflicting, the later of the two is rolled back by the cluster. The client application registers this rollback as a deadlock error. Ideally, the client application should retry the deadlocked transaction. However, not all client applications have this logic built in.

If you encounter this problem, you can set the node to attempt to auto-commit the deadlocked transactions on behalf of the client application. You would do this with the :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>` parameter. Just enter the following to the configuration file:

.. code-block:: ini

   wsrep_retry_autocommit=4

When a transaction fails the certification test due to a cluster-wide conflict, this parameter tells the node how many times you want it to retry the transaction before returning a deadlock error. In the example line above, it is set to four times.

Retrying only applies to auto-commit transactions, as retrying is not safe for multi-statement transactions.


.. rst-class:: section-heading
.. rubric:: Work-Around

While Galera Cluster resolves multi-primary conflicts automatically, there are steps you can take to minimize the frequency of their occurrence.

- First, analyze the hot-spot and see if you can change the application logic to catch deadlock exceptions.

- Next, enable retrying logic at the node level using the :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>` parameter.

- Last, limit the number of primary nodes or switch to a primary-replica model.

If you can filter out access to the hot-spot table, it may be enough to treat writes only to the hot-spot table as primary-replica.

.. container:: bottom-links

   Related Documents

   - :doc:`Certification Based Replication <../../documentation/certification-based-replication>`
   - :ref:`cert.log_conflicts <cert.log_conflicts>`
   - :ref:`wsrep_debug <wsrep_debug>`
   - :ref:`wsrep_local_bf_aborts <wsrep_local_bf_aborts>`
   - :ref:`wsrep_local_cert_failures <wsrep_local_cert_failures>`
   - :ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
