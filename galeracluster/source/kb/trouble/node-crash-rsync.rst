.. cssclass:: kb-article

==================================================
Node Crashes during ``rsync`` SST
==================================================
.. _`kb-trouble-node-crash-rsync`:

When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a :term:`State Snapshot Transfer` (SST) method to provide a full data copy to the new node, known as the joiner.  This should work well, but it doesn't always.


.. rubric:: Scenario
   :class: kb

You can configure :ref:`wsrep_sst_method <wsrep_sst_method>` to use ``rsync`` for :term:`State Snapshot Transfer`.  If the node crashes before the state transfer is complete, it may cause the ``rsync`` process to hang forever, occupying the port and not allowing you to restart the node.

If this occurs, the error logs for the database server will show that the port is in use.


.. rubric:: Solution
   :class: kb

There are a few ways you can resolve this situation.  The simplest way is to kill the orphaned ``rsync`` process.  To do this, you'll first need to know the process identification number.  You could enter something like the following on the stalled node, from the command-line:

.. code-block:: console

   ps -e | grep rsync

   28632 ?        00:06:05 rsync

In the example here, the results show that the process identification number is ``28632``.  Using this information, you might enter the following from the command-line:

.. code-block:: console

   # kill -9 28632

Once you have killed the orphaned process, it will free the relevant ports and allow you to restart the node.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :doc:`SST <../../documentation/sst>`
- :ref:`wsrep_sst_donor <wsrep_sst_donor>` parameter
- :ref:`wsrep_sst_method <wsrep_sst_method>` parameter


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
