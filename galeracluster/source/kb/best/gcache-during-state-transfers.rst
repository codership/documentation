.. cssclass:: kb-article

=========================================
Write-Set Caching during State Transfers
=========================================
.. _`kb-best-gcache-during-state-transfers`:
.. index::
   pair: Performance; gcache

Under normal operations, nodes do not consume much more memory than the regular standalone MySQL database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable. Write-set caching during state transfers is the exception.

.. rubric:: Scenario
   :class: kb

When a node receives a state transfer, it cannot process or apply incoming write-sets as it does not yet have a state to apply them to.  Depending on the state transfer method, (``mysqldump``, for instance), the sending node may also be unable to apply write-sets.


.. rubric:: Recommendations
   :class: kb

The Write-set Cache, (or GCache), caches write-sets on memory-mapped files to disk and Galera Cluster allocates these files as needed.  In other words, the only limit for the cache is the available disk space.  Writing to disk in turn reduces memory consumption.

.. note:: **See Also**: For more information on configuring write-set caching to improve performance, see :ref:`Configuring Flow Control <configuring-fc>`.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :ref:`Configuring Flow Control <configuring-fc>`

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
