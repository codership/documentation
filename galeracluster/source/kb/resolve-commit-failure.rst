.. meta::
   :title: Resolving Commit Failures (Reason 3)
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

      - :ref:`wsrep_debug <wsrep_debug>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-resolve-commit-failures`:

================================
Commit Failed for Reason 3
================================

.. rst-class:: article-stats

   Length: 326 words; Published: April 1, 2014; Updated: November 12, 2019; Category: Schema & SQL; Type: Troubleshooting

When you have :ref:`wsrep_debug <wsrep_debug>` turned ``ON``, you may occasionally see a message noting that a commit has failed due to reason ``3``. This problem can be resolved with a change in topology or with an upgrade.


.. rst-class:: section-heading
.. rubric:: Scenario

Suppose you enable  :ref:`wsrep_debug <wsrep_debug>` on the nodes in your cluster. Then you attempt to change locally the data contained in a database, but you encounter problems. When you check the database error log, you see a message saying that a commit has failed due to reason ``3``. Below is an example of an excerpt from a database server's error log showing this:

.. code-block:: text

   110906 17:45:01 [Note] WSREP:
      BF kill (1, seqno: 16962377), victim:  (140588996478720 4) trx: 35525064
   110906 17:45:01 [Note] WSREP:
      Aborting query: commit
   110906 17:45:01 [Note] WSREP:
      kill trx QUERY_COMMITTING for 35525064
   110906 17:45:01 [Note] WSREP:
      commit failed for reason: 3, seqno: -1

When attempting to apply a replicated write-set, replica threads occasionally encounter lock conflicts with local transactions, which may already be in the commit phase. In such cases, the node aborts the local transaction, allowing the replica thread to proceed.

This is a consequence of optimistic transaction execution. The database server executes transactions with the expectation that there are no row conflicts. It is an expected issue in a multi-primary configuration.


.. rst-class:: section-heading
.. rubric:: Work-Arounds & Solution

To mitigate such conflicts, there are a couple of things you can do. You could use the cluster in a primary-replica configuration: you would direct all writes to a single node. The other work-around is to use the same approach as primary-replica read/write splitting.

The solution may be, though, to upgrade to the latest version of MySQL or MariaDB and the latest version of Galera Cluster. This problem seems to have occurred only in older versions of the database and cluster software.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_debug <wsrep_debug>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
