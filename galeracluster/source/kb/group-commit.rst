.. meta::
   :title: Group Commit with Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


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


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-group-commit`:

=============
Group Commit
=============

.. rst-class:: article-stats

   Length: 322 words; Published: May 30, 2019; Updated: October 22, 2019; Category: Performance; Type: Best Practices

After each transaction is committed, InnoDB will typically flush changes to its redo log and the binary log to the disk--it does this typically by calling `fsync()`, `fdatasync()`. This method is used to ensure data changes are stored durably on the disk. Disk flushing, however, can have an effect on performance and the number of transactions-per-second (TPS) that can be committed.

Starting with version 5.3 of MariaDB, Group Commit was introduced. If there are several transactions trying to commit at the same time, group commit will force them to be flushed to the disk with a single system call, rather than one system call for each commit. This can greatly reduce the need for flush operations, and greatly improve the throughput of TPS.

In Galera transactions are committed sequentially in total order determined by the group communication between nodes. Sequential commit ordering is implemented with commit monitor, which allows only single transaction to proceed at the time.

Prior to version 4 of Galera, even with MariaDB 5.3 or later, transactions were committed strictly in sequence: group commit had no effect of Galera. In Galera 3, the commit monitor was held until the transaction was completely finished. This disabled the MariaDB group commit optimization and it was not possible to amortize expensive disk operations (i.e., `fsync()`, `fdatasync()`).

As of version 4 of Galera, the commit time concurrency control was reworked so that the commit monitor is released as soon as the commit has been queued for group commit. This allows transactions to be committed in groups while still respecting sequential commit order.

In essence, MariaDB's group commit operates now with Galera--starting with version 4--by providing better integration with existing functionality. The same will also apply to MySQL-wsrep when it's implemented: Galera 4 provides a better way to integrate with native binary log group commit.

.. note:: **See Also**: For more information, see the `MariaDB Documentation on Group Commit <https://mariadb.com/kb/en/mariadb/group-commit-for-the-binary-log/>`_.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
