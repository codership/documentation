.. meta::
   :title: Single Master Setup in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`

      .. cssclass:: sub-links

         - :doc:`Troubleshooting <../trouble/index>`

         .. cssclass:: here

         - :doc:`Best Practices <./index>`

      - :doc:`Training <../../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      Related Documents

      Related Articles


.. cssclass:: library-article
.. _`kb-best-single-master-setup`:

=======================
Single Master Setup
=======================

If a cluster uses only one node as a master, there are certain requirements (e.g., the slave queue size) that can be relaxed.


.. rst-class:: kb
.. rubric:: Recommendations

To relax flow control, you might use the settings below:

.. code-block:: ini

    wsrep_provider_options = "gcs.fc_limit = 256;
                              gcs.fc_factor = 0.99;
                              gcs.fc_master_slave = YES"

By reducing the rate of flow control events, these settings may improve replication performance.

.. note:: You can also use this setting as sub-optimal in a multi-master setup.
