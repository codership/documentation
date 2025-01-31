.. meta::
   :title: Mariabackup Options
   :description:
   :language: en-US
   :keywords: galera cluster, mariadb, mariabackup, parameters
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`mariabackup-options`:

======================
Mariabackup Options
======================

The ``mariabackup`` SST method uses the ``Mariabackup`` utility for performing SSTs. It does not block the donor node.

To use the ``mariabackup`` SST method, you must set the ``wsrep_sst_method=mariabackup`` on both the donor and joiner node. It can be changed dynamically with ``SET GLOBAL`` on the node that you intend to be a SST donor. For example:

.. code-block:: mysql

   SET GLOBAL wsrep_sst_method='mariabackup';

For an SST to work properly, the donor and joiner node must use the same SST method.





.. _`mariabackup-cpat`:
.. rst-class:: section-heading
.. rubric:: ``cpat``

Defines what files to exclude from the clean up from the datadir during state transfers.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``cpat``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", "See below"

When the donor node begins a :term:`State Snapshot Transfer`, it cleans up various files from the datadir. This ensures that the joiner node can cleanly apply the state transfer. With this parameter, you can define what files you want the node to exclude from being deleted, before the state transfer.

.. code-block:: ini

   cpat=".*\.pem$\|.*init\.ok$\|.*galera\.cache$\|.*sst_in_progress$\|.*\.sst$\|.*gvwstate\.dat$\|.*grastate\.dat$\|.*\.err$\|.*\.log$\|.*RPM_UPGRADE_MARKER$\|.*RPM_UPGRADE_HISTORY$"


