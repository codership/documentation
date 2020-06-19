.. meta::
   :title: Galera Cluster Documentation
   :description:
   :language: en-US
   :keywords: galera cluster, documentation, docs, mysql, mariadb
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

.. cssclass:: library-index
.. _`documentation`:

=============================
The Codership Documentation
=============================

.. index::
   pair: Certification based replication; Descriptions
.. index::
   pair: Virtual synchrony; Descriptions

This is the Codership Documentation. It documents the latest version of Galera Cluster, as well as related Galera tools, such as the Galera Arbitrator. It also includes, at times, information on features available in upcoming versions of Galera Cluster that haven't been released yet. For such text, the new version number is noted.

.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: :doc:`Installation & Configuration <technical-description>`

.. csv-table::
   :class: doc-links

   ":doc:`tech-desc-introduction`", ":doc:`state-transfer`"
   ":doc:`architecture`", ":doc:`node-states`"
   ":doc:`install`", ":doc:`recovery`"
   ":doc:`certification-based-replication`", ":doc:`weighted-quorum`"
   ":doc:`isolation-levels`", ":doc:`streaming-replication`"


.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: :doc:`Administration <administration>`

.. csv-table::
   :class: doc-links

   ":doc:`node-provisioning`", ":doc:`pc-recovery`"
   ":doc:`sst`", ":doc:`quorum-reset`"
   ":doc:`scriptable-sst`", ":doc:`managing-fc`"
   ":doc:`system-tables`", ":doc:`auto-eviction`"
   ":doc:`schema-upgrades`", ":doc:`using-sr`"
   ":doc:`upgrading`", ":doc:`backup-cluster`"


.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: :doc:`Deployment <deployment>`

.. csv-table::
   :class: doc-links

   ":doc:`load-balancing`", ":doc:`deployment-variants`"
   ":doc:`containers`", ":doc:`arbitrator`"


.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: :doc:`Monitoring <monitor>`

.. csv-table::
   :class: doc-links

   ":doc:`monitoring-cluster`", ":doc:`log`"
   ":doc:`galera-manager`", ":doc:`security`"
   ":doc:`notification-cmd`", ""


.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: :doc:`Reference <reference>`

.. csv-table::
   :class: doc-links

   ":doc:`mysql-wsrep-options`", ":doc:`glb-parameters`"
   ":doc:`wsrep-functions`", ":doc:`xtrabackup-options`"
   ":doc:`galera-parameters`", ":doc:`system-tables`"
   ":doc:`galera-status-variables`", ":doc:`versioning-information`"


.. container:: banner

   .. rst-class:: section-heading list-sub-header
   .. rubric:: Miscellaneous

.. csv-table::
   :class: doc-links

   ":doc:`glossary`", ":doc:`legal-notice`"
   ":ref:`genindex`", ":ref:`search`"
   ":doc:`../whats-new`", ""

For resolving problems you might have with the software, you can also check our :doc:`Knowledge Base <../kb/index>`. There you will find troubleshooting and best practices articles.  You can also post questions on the `Codership Forum <https://galeracluster.com/community/>`_. The community, as well as our staff monitor and respond to posts made there.

If you need more immediate and personalized assistance, you can get a Support contract with us at Codership.  For a quote on the cost of support, write us at info@codership.com or use our on-line form `to send us a message <https://galeracluster.com/contact-us/#send-us-a-message>`_.


.. toctree::
   :maxdepth: 3
   :hidden:

   overview
   technical-description
   install
   administration
   deployment
   monitor
   security
   reference


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
