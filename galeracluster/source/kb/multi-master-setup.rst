.. meta::
   :title: Galera Cluster Multi-Primary Setup
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.

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

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-multi-master-setup`:

====================
Multi-Primary Setup
====================

.. rst-class:: article-stats

   Length: 55 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Topology; Type: Best Practices


A primary is a node that can simultaneously process writes from clients. The more primaries in a cluster, the higher the probability of certification conflicts. This can lead to undesirable rollbacks and performance degradation.

If you find you experience frequent certification conflicts, consider reducing the number of nodes the cluster uses as primaries.
