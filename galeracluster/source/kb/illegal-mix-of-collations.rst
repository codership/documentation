.. meta::
   :title: Illegal Mix of Collations
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


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

      Related Documents

      - :ref:`wsrep_debug <wsrep_debug>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-illegal-mix-of-collations`:

================================
Illegal Mix of Collations
================================

.. rst-class:: article-stats

   Length: 240 words; Published: October 21, 2024; Updated: October 21, 2024; Category: Schema & SQL; Type: Troubleshooting

A mismatch in collations used in incoming replication and the table structure in the node itself causes an error.


.. rst-class:: section-heading
.. rubric:: Scenario

You get an error such as the one below:

.. code-block:: text

   2021-03-25T16:09:32.856092+01:00 37 [ERROR] [MY-010584] [Repl] Slave SQL for channel ‘’: Error ‘Illegal mix of collations (utf8_general_ci,IMPLICIT) and (latin1_swedish_ci,EXPLICIT) for operation ‘=’' on query. Default database: ‘farao_achmea_hdod_a’. Query: ’UPDATE tblDocument SET LockedBy = NULL , LockedDT = NULL , LockExpirationDT = NULL WHERE LockedBy = NAME_CONST(‘inLockedBy’,_latin1'AchmeaHdodEnrichFaraoFile:123646188' COLLATE ‘latin1_swedish_ci’)‘, Error_code: MY-001267
   2021-03-25T16:09:32.879162+01:00 37 [ERROR] [MY-010584] [Repl] Slave SQL for channel ‘’: Node has dropped from cluster, Error_code: MY-001047 <<<

This error is likely caused by a mismatch in collations used in incoming replication and the table structure in the node itself.

For example, the following WHERE clause may cause the error:

.. code-block:: mysql

   WHERE 'A' COLLATE utf8_general_ci,IMPLICIT = 'A' COLLATE latin1_swedish_ci,EXPLICIT


.. rst-class:: section-heading
.. rubric:: Work-Arounds & Solution

To mitigate such errors, there are a couple of things you can do. 

#. Modify the table structure to use the ``utf8_general_ci`` collation, to match the incoming data:
   
   .. code-block:: mysql
   
      ALTER TABLE tblDocument
      CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
   
#. Modify the replication source to use the ``latin1_swedish_ci`` collation to match the table structure.
   
#. Use an explicit COLLATE clause in the replication query to convert the incoming data:
   
   .. code-block:: mysql
   
      UPDATE tblDocument
      SET LockedBy = NULL, LockedDT = NULL, LockExpirationDT = NULL
      WHERE LockedBy = NAME_CONST(‘inLockedBy’,_latin1'AchmeaHdodEnrichFaraoFile:123646188' COLLATE ‘utf8_general_ci’);
   
#. Consider converting the entire database to use a consistent character set and collation, preferably ``utf8mb4`` with an appropriate collation, such as ``utf8mb4_unicode_ci``.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_debug <wsrep_debug>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
