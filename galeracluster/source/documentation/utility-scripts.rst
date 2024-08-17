.. meta::
   :title: Utility Scripts
   :description:
   :language: en-US
   :keywords: galera cluster, wsrep_recover script, scripts, utility scripts
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


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

      Related Documents

      - :ref:`Recovering Primary Component <pc-recovery>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`utility_scipts`:

===============
Utility Scripts
===============

This page describes Galera Cluster utility scripts.


.. _`wsrep_recover_script`:
.. rst-class:: section-heading
.. rubric:: wsrep_recover Script

The ``wsrep_recover`` utility script simplifies cluster recovery procedures. The script recovers the database to a consistent state, finds the last committed GTID on a crashed or stopped node, and prints the corresponding ``--wsrep-start-position`` option to the standard output, to be used in startup scripts.

Usage:

.. code-block:: ini

   sudo wsrep_recover [options]

The script options are mostly passed through directly to mysqld. However, some options have a special meaning. The options are:

- ``--basedir /x/y/z``  This option additionally sets mysqld binary path to ``/x/y/z/bin/mysqld``.

- ``--mysqld /x/y/z/mysqld``  This option overrides the ``--basedir`` effect on the mysqld binary path.


(NOTE ):

.. note:: Notice the whitespace between the option name and the value

An example from a non-standard setup:

.. code-block:: ini

   sudo wsrep_recover --mysqld /path/to/mysqld --datadir /path/to/datadir --user some_user

By default, the ``mysqld`` binary is expected to be found at '/usr/sbin/mysqld' and will be run as 'mysql' user, using the configuration file from the standard location.


See also wsrep option :ref:`wsrep_recover <wsrep_recover>`.


.. container:: bottom-links

   Related documents
