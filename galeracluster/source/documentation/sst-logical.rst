.. meta::
   :title: Logical State Snapshots within Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, sst, state snapshot transfer, mysqldump, logical
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

      Related Documents

      - :ref:`wsrep_sst_method <wsrep_sst_method>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`sst-logical`:

========================
Logical State Snapshot
========================

There is one back-end method available for a Logical State Snapshots: ``mysqldump``.

The :term:`Logical State Transfer Method` has the following advantages:

- These transfers are available on live servers. In fact, only a fully initialized server can receive a Logical State Snapshot.

- These transfers do not require the receptor node to have the same configuration as the :term:`Donor Node`. This allows you to upgrade storage engine options.

  For example, when using this transfer method you can migrate from the Antelope to the Barracuda file format, use compression resize, or move iblog* files from one partition into another.

The Logical State Transfer Method has the following disadvantages:

- These transfers are as slow as ``mysqldump``.

- These transfers require that you configure the receiving database server to accept root connections from potential donor nodes.

- The receiving server must have a non-corrupted database.


.. _`sst-mysqldump`:
.. rst-class:: section-heading
.. rubric:: ``mysqldump``

The main advantage of ``mysqldump`` is that you can transfer a state snapshot to a working server. That is, you start the server standalone and then instruct it to join a cluster from within the database client command line. You can also use it to migrate from an older database format to a newer one.

``mysqldump`` requires that the receiving node have a fully functional database, which can be empty. It also requires the same root credentials as the donor and root access from the other nodes.

This transfer method is several times slower than the others on sizable databases, but it may prove faster in cases of very small databases. For instance, on a database that is smaller than the log files.

.. warning:: This transfer method is sensitive to the version of ``mysqldump`` each node uses. It is not uncommon for a given cluster to have installed several versions. A State Snapshot Transfer can fail if the version one node uses is older and incompatible with the newer server.

On occasion, ``mysqldump`` is the only option available. For instance, if you upgrade from a cluster using MySQL 5.1 with the built-in InnoDB support to MySQL 5.5, which uses the InnoDB plugin.

The ``mysqldump`` script only runs on the sending node. The output from the script gets piped to the MySQL client that connects to the :term:`Joiner Node`.

Because ``mysqldump`` interfaces through the database client, configuring it requires several steps beyond setting the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter. For more information on its configuration, see:

For more information on ``mysqldump``, see `mysqldump Documentation <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`_.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_sst_method <wsrep_sst_method>`


.. toctree::
   :hidden:

   mysqldump
