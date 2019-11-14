.. meta::
   :title: Customizing the Write-Set Cache Size
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

      - :ref:`gcache.size <gcache.size>`
      - :ref:`wsrep_received_bytes <wsrep_received_bytes>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-customizing-gcache-size`:

=====================================
Customizing the Write-Set Cache Size
=====================================

.. rst-class:: article-stats

   Length: 467 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Performance; Type: Best Practices

You can define the size of the write-set cache using the :ref:`gcache.size <gcache.size>` parameter.  The set the size to one less than that of the data directory.

.. rst-class:: section-heading
.. rubric:: Scenario

If you have storage issues, there are some guidelines to consider in adjusting this issue.  For example, your preferred state snapshot method.  ``rsync`` and ``xtrabackup`` copy the InnoDB log files, while ``mysqldump`` does not.  So, if you use ``mysqldump`` for state snapshot transfers, you can subtract the size of the log files from your calculation of the data directory size.

.. note:: Incremental State Transfers (IST) copies the database five times faster over ``mysqldump`` and about 50% faster than ``xtrabackup``.  Meaning that your cluster can handle relatively large write-set caches.  However, bear in mind that you cannot provision a server with Incremental State Transfers.


.. rst-class:: section-heading
.. rubric:: Recommendations

As a general rule, start with the data directory size, including any possible links, then subtract the size of the ring buffer storage file, which is called ``galera.cache`` by default.

If storage remains an issue, you can further refine these calculations with the database write rate.  The write rate indicates the tail length that the cluster stores in the write-set cache.

You can calculate this using the :ref:`wsrep_received_bytes <wsrep_received_bytes>` status variable.

#. Determine the size of the write-sets the node has received from the cluster:

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_received_bytes';

      +------------------------+-----------+
      | Variable name          | Value     |
      +------------------------+-----------+
      | wsrep_received_bytes   | 6637093   |
      +------------------------+-----------+

   Note the value and time, respective as :math:`recv_1` and :math:`time_1`.

#. Run the same query again, noting the value and time, respectively, as :math:`recv_2` and :math:`time_2`.

#. Apply these values to the following equation:

   .. math::

      writerate = \frac{ recv_2 - recv_1 }{ time_2 - time_1}

From the write rate you can determine the amount of time the cache remains valid.  When the cluster shows a node as absent for a period of time less than this interval, the node can rejoin the cluster through an incremental state transfer. Node that remains absent for longer than this interval will likely require a full state snapshot transfer to rejoin the cluster.

You can determine the period of time the cache remains valid using this equation:

.. math::

   period = \frac{ cachesize } { writerate }


Conversely, if you already know the period in which you want the write-set cache to remain valid, you can use instead this equation:

.. math::

   cachesize = writerate \times time


This equation can show how the size of the write-set cache can improve performance.  For instance, say you find that cluster nodes frequently request state snapshot transfers.  Increasing the :ref:`gcache.size <gcache.size>` parameter extends the period in which the write-set remains valid, allowing the nodes to update instead through incremental state transfers.

.. note:: Consider these configuration tips as guidelines only. For example, in cases where you must avoid state snapshot transfers as much as possible, you may end up using a much larger write-set cache than suggested above.

.. container:: bottom-links

   Related Documents

   - :ref:`gcache.size <gcache.size>`
   - :ref:`wsrep_received_bytes <wsrep_received_bytes>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
