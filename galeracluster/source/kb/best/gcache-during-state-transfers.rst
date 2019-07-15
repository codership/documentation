.. meta::
   :title: Write-Set Caching during State Transfers
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../trouble/index>`
         - :doc:`Best Practices <./index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :ref:`Configuring Flow Control <configuring-fc>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: kb-article
.. _`kb-best-gcache-during-state-transfers`:

=========================================
Write-Set Caching during State Transfers
=========================================

.. index::
   pair: Performance; gcache

Under normal operations, nodes do not consume much more memory than the regular standalone MySQL database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable. Write-set caching during state transfers is the exception.

.. rst-class:: kb
.. rubric:: Scenario

When a node receives a state transfer, it cannot process or apply incoming write-sets as it does not yet have a state to apply them to.  Depending on the state transfer method, (``mysqldump``, for instance), the sending node may also be unable to apply write-sets.


.. rst-class:: kb
.. rubric:: Recommendations

The Write-set Cache, (or GCache), caches write-sets on memory-mapped files to disk and Galera Cluster allocates these files as needed.  In other words, the only limit for the cache is the available disk space.  Writing to disk in turn reduces memory consumption.

.. note:: **See Also**: For more information on configuring write-set caching to improve performance, see :ref:`Configuring Flow Control <configuring-fc>`.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
