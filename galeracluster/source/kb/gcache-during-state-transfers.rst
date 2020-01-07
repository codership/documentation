.. meta::
   :title: Write-Set Caching during State Transfers
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

      Related Documents

      - :ref:`Configuring Flow Control <configuring-fc>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-gcache-during-state-transfers`:

=========================================
Write-Set Caching during State Transfers
=========================================

.. index::
   pair: Performance; gcache

.. rst-class:: article-stats

   Length: 156 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Performance; Type: Best Practices

Under normal operations, nodes do not consume much more memory than the regular standalone MySQL database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable. Write-set caching during state transfers is the exception.

.. rst-class:: section-heading
.. rubric:: Scenario

When a node receives a state transfer, it cannot process or apply incoming write-sets as it does not yet have a state to apply them to.  Depending on the state transfer method, (``mysqldump``, for instance), the sending node may also be unable to apply write-sets.


.. rst-class:: section-heading
.. rubric:: Recommendations

The Write-set Cache, (or GCache), caches write-sets on memory-mapped files to disk and Galera Cluster allocates these files as needed.  In other words, the only limit for the cache is the available disk space.  Writing to disk in turn reduces memory consumption.

.. note:: **See Also**: For more information on configuring write-set caching to improve performance, see :ref:`Configuring Flow Control <configuring-fc>`.

.. container:: bottom-links

   Related Documents

   - :ref:`Configuring Flow Control <configuring-fc>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
