.. meta::
   :title: Single Master Setup in Galera Cluster
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

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-single-master-setup`:

=======================
Single Master Setup
=======================

.. rst-class:: article-stats

   Length: 81 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Topology; Type: Best Practices

If a cluster uses only one node as a master, there are certain requirements (e.g., the slave queue size) that can be relaxed.


.. rst-class:: section-heading
.. rubric:: Recommendations

To relax flow control, you might use the settings below:

.. code-block:: ini

    wsrep_provider_options = "gcs.fc_limit = 256;
                              gcs.fc_factor = 0.99;
                              gcs.fc_master_slave = YES"

By reducing the rate of flow control events, these settings may improve replication performance.

.. note:: You can also use this setting as sub-optimal in a multi-master setup.
