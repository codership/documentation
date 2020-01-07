.. meta::
   :title: Improving WAN Replication with Galera Cluster
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

      - :ref:`evs.suspect_timeout <evs.suspect_timeout>`
      - :ref:`evs.inactive_timeout <evs.inactive_timeout>`
      - :ref:`evs.install_timeout <evs.install_timeout>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-wan-replication`:

==================
WAN Replication
==================

.. rst-class:: article-stats

   Length: 161 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Performance; Type: Best Practices

When running the cluster over a :abbr:`WAN (Wide Area Network)`, you may frequently experience transient network connectivity failures.  To prevent this from partitioning the cluster, you may want to increase the *keepalive* timeouts.

.. rst-class:: section-heading
.. rubric:: Recommendations

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

.. container:: bottom-links

   Related Documents

   - :ref:`evs.suspect_timeout <evs.suspect_timeout>`
   - :ref:`evs.inactive_timeout <evs.inactive_timeout>`
   - :ref:`evs.install_timeout <evs.install_timeout>`
