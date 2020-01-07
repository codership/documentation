.. meta::
   :title: Factors related to Migrating to Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      - :doc:`differences`
      - :doc:`migration`

      Related Articles

      - :doc:`Getting Started Guide <getting-started>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`migrate`:

=================================
Galera Cluster Migration Factors
=================================

.. rst-class:: article-stats

   Length: 173 words; Published: October 20, 2014; Topic: Migration; Level: Beginner


In the :doc:`Getting Started Guide <getting-started>`, the installation guides were written on the assumption that Galera Cluster is the first database in your infrastructure. However, this won't always be the case.  Sometimes, you may need to migrate to Galera Cluster from an existing database infrastructure: such as a single MySQL server or several database servers that were part of a MySQL master-slave cluster.


- :doc:`differences`

  .. rst-class:: list-stats

     Length:  808 words; Writer: Staff; Published: October 20, 2014; Topic: Migration; Level: Beginner

  While clusters operate as distributed database servers, there are some key differences between them and the standard stand-alone MySQL implementations.


- :doc:`migration`

  .. rst-class:: list-stats

     Length:  1106 words; Writer: Staff; Published: October 20, 2014; Topic: Migration; Level: Beginner

  When migrating from the standard MySQL implementations to Galera Cluster, there are some additional steps that you need to take to ensure that you safely transfer the data from the existing database to the new cluster.  This section covers the procedure to update system tables and how to migrate from stand-alone MySQL, as well as from MySQL master-slave replication clusters.


For more information on the installation and basic management of Galera Cluster, see the :doc:`Getting Started Guide <getting-started>`.

.. container:: bottom-links

   Related Documents

   - :doc:`differences`
   - :doc:`migration`

   Related Articles

   - :doc:`Getting Started Guide <getting-started>`

.. toctree::
   :maxdepth: 2
   :hidden:

   differences
   migration
