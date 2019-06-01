=======================
 Single Master Setup
=======================
.. _`kb-best-single-master-setup`:

In the event that a cluster uses only one node as a master, there are certain requirements (e.g., the slave queue size) that can be relaxed.


.. rubric:: Recommendations
   :class: kb

To relax flow control, you might use the settings below:

.. code-block:: ini

    wsrep_provider_options = "gcs.fc_limit = 256;
                              gcs.fc_factor = 0.99;
                              gcs.fc_master_slave = YES"

By reducing the rate of flow control events, these settings may improve replication performance.

.. note:: You can also use this setting as sub-optimal in a multi-master setup.
