.. meta::
   :title: Setting Parallel Slave Threads in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2022. All Rights Reserved.


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

      - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`
      - :ref:`wsrep_applier_threads <wsrep_applier_threads>`
	  - :ref:`wsrep_slave_threads <wsrep_slave_threads>`
      - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-parallel-slave-threads`:

===============================
Setting Parallel Slave Threads
===============================

.. index::
   pair: Performance; innodb_autoinc_lock_mode
.. index::
   pair: Performance; wsrep_applier_threads

.. rst-class:: article-stats

   Length: 381 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Performance; Type: Best Practices

There is no rule about how many slave threads you need for replication.  Parallel threads do not guarantee better performance, but they don't impair regular operation performance and they may in fact speed up the synchronization of new nodes joining a cluster.

.. note:: The ``wsrep_slave_threads`` parameter is still available, but it is deprecated. Use ``wsrep_applier_threads`` for parallel threads, if you use MySQL-wsrep 8.0.26 or newer.

.. rst-class:: section-heading
.. rubric:: Scenario

Suppose you have a cluster of a few nodes, but occasionally you add a couple of new nodes to the cluster to handle unexpected surges in traffic.  When these surges happen, you want the new nodes to be synchronized rapidly and not be a drain on the performance of the cluster in the process.

You may be able to do this, to get new nodes synchronized and handling traffic faster by making changes to a couple of settings.


.. rst-class:: section-heading
.. rubric:: Recommendations

To make state transfers quicker for new nodes, consider changing the number of slave threads. You should start with four slave threads per CPU core:

.. code-block:: ini

   wsrep_applier_threads=4

The logic here is that, in a balanced system, four slave threads can typically saturate a CPU core.  However, I/O performance can increase this figure several times over.  For example, a single-core ThinkPad R51 with a 4200 RPM drive can use thirty-two slave threads.

Next, you should set ``innodb_autoinc_lock_mode`` variable, the lock mode to use for generating auto-increment values.  Setting it to a value of 2 tells InnoDB to use interleaved method. Interleaved is the fastest and most scalable lock mode, but should be used only when ``BINLOG_FORMAT`` is set to ``ROW``.

Basically, setting the auto-increment lock mode for InnoDB to interleaved, you're allowing slaves threads to operate in parallel. You would do this by including the following line in the configuration file:

.. code-block:: ini

   innodb_autoinc_lock_mode=2

You can use the :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>` status variable to determine the maximum number of slave threads possible.  For example:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_deps_distance';

   +----------------------------+-----------+
   | Variable name              | Value     |
   +----------------------------+-----------+
   | wsrep_cert_deps_distance   | 23.88889  |
   +----------------------------+-----------+

This value essentially determines the number of write-sets that the node can apply in parallel on average.

.. warning:: Do not use a value for :ref:`wsrep_applier_threads <wsrep_applier_threads>` that is higher than the average given by the :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>` status variable.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`
   - :ref:`wsrep_applier_threads <wsrep_applier_threads>`
   - :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
