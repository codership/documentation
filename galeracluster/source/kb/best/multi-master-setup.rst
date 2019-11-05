.. meta::
   :title: Galera Cluster Multi-Master Setup
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
.. _`kb-best-multi-master-setup`:

====================
Multi-Master Setup
====================

A master is a node that can simultaneously process writes from clients. The more masters in a cluster, the higher the probability of certification conflicts.  This can lead to undesirable rollbacks and performance degradation.

If you find you experience frequent certification conflicts, consider reducing the number of nodes the cluster uses as masters.
