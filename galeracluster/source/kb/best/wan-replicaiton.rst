==================
 WAN Replication
==================
.. _`kb-best-wan-replication`:

When running the cluster over a :abbr:`WAN (Wide Area Network)`, you may frequently experience transient network connectivity failures.  To prevent this from partitioning the cluster, you may want to increase the *keepalive* timeouts.

.. rubric:: Recommendations
   :class: kb

The following parameters can tolerate 30 second connectivity outages:

.. code-block:: ini

  wsrep_provider_options = "evs.keepalive_period = PT3S;
  	                        evs.suspect_timeout = PT30S;
  	                        evs.inactive_timeout = PT1M;
  	                        evs.install_timeout = PT1M"

.. note:: All ``wsrep_provider_options`` settings need to be specified on a single line. In case of multiple instances of ``wsrep_provider_options``, only the last one is used.

In configuring these parameters, consider the following:

- You want the :ref:`evs.suspect_timeout <evs.suspect_timeout>` parameter set as high as possible to avoid partitions.  Partitions cause state transfers, which can effect performance.

- You must set the :ref:`evs.inactive_timeout <evs.inactive_timeout>` parameter to a value higher than that of the :ref:`evs.suspect_timeout <evs.suspect_timeout>` parameter.

- You must set the :ref:`evs.install_timeout <evs.install_timeout>` parameter to a value higher than the value of the :ref:`evs.inactive_timeout <evs.inactive_timeout>` parameter.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :ref:`evs.suspect_timeout <evs.suspect_timeout>` parameter
- :ref:`evs.inactive_timeout <evs.inactive_timeout>` parameter
- :ref:`evs.install_timeout <evs.install_timeout>` parameter
