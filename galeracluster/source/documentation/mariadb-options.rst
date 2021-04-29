.. meta::
   :title: MariaDB Options
   :description:
   :language: en-US
   :keywords: galera cluster, mariadb options, galera options
   :copyright: Codership Oy, 2014 - 2021. All Rights Reserved.


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
.. _`mariadb-options`:

======================
MariaDB Options
======================
.. index::
   single: Drupal
.. index::
   pair: Logs; Debug log


These are MariaDB Server and Enterprise options. If you click on a particular variable in this table, your web browser will scroll down to the entry for it with more details and an explanation.

.. _`mariadb_server_options`:
.. rst-class:: section-heading
.. rubric:: MariaDB Server Options


.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 34, 12, 6, 8, 8

   ":ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>`", "``0``", "Yes", "Yes", "", ""
   ":ref:`wsrep_gtid_mode <wsrep_gtid_mode>`", "``OFF``", "Yes", "Yes", "", ""
   ":ref:`wsrep_gtid_seq_no <wsrep_gtid_seq_no>`", "", "No", "Yes", "", ""
   ":ref:`wsrep_ignore_apply_errors <wsrep_ignore_apply_errors>`", "``7``", "Yes", "Yes", "", ""
   ":ref:`wsrep-mysql-replication-bundle <wsrep-mysql-replication-bundle>`", "``0``", "Yes", "No", "", ""
   ":ref:`wsrep_patch_version <wsrep_patch_version>`", "````", "Yes", "No", "", ""
   ":ref:`wsrep_mode=REPLICATE_ARIA <wsrep_mode_replicate_aria>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_mode=REPLICATE_MYISAM <wsrep_mode_replicate_myisam>`", "``OFF``", "Yes", "", "1.0", ""


.. _`wsrep_gtid_domain_id`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_gtid_domain_id``

.. index::
   pair: Parameters; wsrep_gtid_domain_id

This system variable defines the GTID domain ID that is used for wsrep GTID mode.

- When :ref:`wsrep_gtid_mode <wsrep_gtid_mode>` is set to ON, wsrep_gtid_domain_id is used in place of gtid_domain_id for all Galera Cluster write sets.

- When :ref:`wsrep_gtid_mode <wsrep_gtid_mode>` is set to OFF, wsrep_gtid_domain_id is simply ignored to allow for backward compatibility.

- There are some additional requirements that need to be met in order for this mode to generate consistent GTIDs. For more information, see `Using MariaDB GTIDs with MariaDB Galera Cluster <https://mariadb.com/kb/en/using-mariadb-gtids-with-mariadb-galera-cluster/>`_.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-gtid-domain-id=#``"
   "System Variable", "``wsrep_gtid_domain_id``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Data Type", "Numeric"
   "Default Value", "``0`` "
   "Range", "``0`` to ``4294967295``"
   "MariaDB Version", "Version 10.1.4"


.. _`wsrep_gtid_mode`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_gtid_mode``

.. index::
   pair: Parameters; wsrep_gtid_mode

Wsrep GTID mode attempts to keep GTIDs consistent for Galera Cluster write sets on all cluster nodes. GTID state is initially copied to a joiner node during an SST. If you are planning to use Galera Cluster with MariaDB replication, then wsrep GTID mode can be helpful.

- When wsrep_gtid_mode is set to ON, :ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>` is used in place of gtid_domain_id for all Galera Cluster write sets.

- When wsrep_gtid_mode is set to OFF, :ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>` is simply ignored to allow for backward compatibility.

- There are some additional requirements that need to be met in order for this mode to generate consistent GTIDs. For more information, see `Using MariaDB GTIDs with MariaDB Galera Cluster <https://mariadb.com/kb/en/using-mariadb-gtids-with-mariadb-galera-cluster/>`_.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-gtid-mode[={0|1}]``"
   "System Variable", "``wsrep_gtid_mode``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Data Type", "Boolean"
   "Default Value", "``OFF`` "
   "MariaDB Version", "Version 10.1.4"


.. _`wsrep_gtid_seq_no`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_gtid_seq_no``

.. index::
   pair: Parameters; wsrep_gtid_seq_no

Internal server usage, manually set WSREP GTID seqno.

.. csv-table::
   :class: doc-options

   "Command-line Format", "`None"
   "System Variable", "``Internal server usage, manually set WSREP GTID seqno.``"
   "Variable Scope", "Session only"
   "Dynamic Variable", "Yes"
   "Data Type", "Numeric"
   "Range", "``0`` to ``18446744073709551615``"
   "MariaDB Version", "Version 10.5.1"


.. _`wsrep_ignore_apply_errors`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_ignore_apply_errors``

.. index::
   pair: Parameters; wsrep_ignore_apply_errors

A bitmask defining whether errors are ignored, or reported back to the provider

- 0: No errors are skipped.
- 1: Ignore some DDL errors (DROP DATABASE, DROP TABLE, DROP INDEX, ALTER TABLE).
- 2: Skip DML errors (Only ignores DELETE errors).
- 4: Ignore all DDL errors.


.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-wsrep_ignore_apply_errors``"
   "System Variable", "``wsrep_ignore_apply_errors``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Data Type", "Numeric"
   "Default Value", "``7`` "
   "Range", "``0`` to ``7``"
   "MariaDB Version", "Version 10.4.2"


.. _`wsrep-mysql-replication-bundle`:
.. rst-class:: section-heading
.. rubric:: ``wsrep-mysql-replication-bundle``

.. index::
   pair: Parameters; wsrep-mysql-replication-bundle

Defines the number of replication events that are grouped together. This is an experimental implementation aimed to assist with bottlenecks when a single replica faces a large commit time delay. If set to ``0`` (the default), there is no grouping.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-mysql-replication-bundle=#``"
   "System Variable", "``wsrep-mysql-replication-bundle``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Data Type", "Numeric"
   "Default Value", "``0``"
   "Range", "``0`` to ``1000``"


.. _`wsrep_patch_version`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_patch_version``

.. index::
   pair: Parameters; wsrep_patch_version

Wsrep patch version, for example ``wsrep_25.10``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "None"
   "System Variable", "``wsrep_patch_version``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Data Type", "String"
   "Default Value", "None"
   "MariaDB Version", "Version 10.1.5"


.. _`wsrep_mode_replicate_aria`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_mode=REPLICATE_ARIA``

.. index::
   pair: Parameters; wsrep_mode=REPLICATE_ARIA

.. note:: This is an experimental feature. This is documentation for currently unreleased software, that is, MariaDB 10.6.

Together with :ref:`wsrep_mode=REPLICATE_MYISAM <wsrep_mode_replicate_myisam>`, this parameter enables Galera to replicate both DDL and DML for ARIA and/or MyISAM using TOI.

For example:

.. code-block:: mysql

   SET GLOBAL wsrep_mode = "REQUIRED_PRIMARY_KEY,REPLICATE_MYISAM,REPLICATE_ARIA";

Replicates both Aria and MyISAM DML, but requires a primary key for replicated table.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_mode_replicate_aria``"
   "System Variable", "``wsrep_mode_replicate_aria``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF`` "
   "Initial Version", "Version 1.0"
   "MariaDB Version", "Version 10.6"

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_mode_replicate_aria';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | wsrep_mode_replicate_aria    | ON    |
    +------------------------------+-------+


.. _`wsrep_mode_replicate_myisam`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_mode=REPLICATE_MYISAM``

.. index::
   pair: Parameters; wsrep_mode=REPLICATE_MYISAM

.. note:: This is an experimental feature. This is documentation for currently unreleased software, that is, MariaDB 10.6.

Together with :ref:`wsrep_mode=REPLICATE_ARIA <wsrep_mode_replicate_aria>`, this parameter enables Galera to replicate both DDL and DML for MyISAM and/or Aria using TOI.

For example:

.. code-block:: mysql

   SET GLOBAL wsrep_mode = "REQUIRED_PRIMARY_KEY,REPLICATE_MYISAM,REPLICATE_ARIA";

Replicates both MyISAM and Aria DML, but requires a primary key for replicated table.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_mode_replicate_myisam``"
   "System Variable", "``wsrep_mode_replicate_myisam``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF`` "
   "Initial Version", "Version 1.0"
   "MariaDB Version", "Version 10.6"

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_mode_replicate_myisam';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | wsrep_mode_replicate_myisam  | ON    |
    +------------------------------+-------+
	


.. _`mariadb_enterprise_options`:
.. rst-class:: section-heading
.. rubric:: MariaDB Enterprise Options

.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 34, 12, 6, 8, 8

   ":ref:`wsrep-OSU-mode <wsrep-osu-mode>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_strict_ddl <wsrep_strict_ddl>`", "``TOI``", "Global and Session", "Yes", "1.0", ""



.. _`wsrep-osu-mode`:
.. rst-class:: section-heading
.. rubric:: ``wsrep-osu-mode``

.. index::
   pair: Parameters; wsrep-osu-mode

This parameter defines the mode for Online Schema Upgrade that the node uses to replicate DDL statements. The following methods are available:

DDL statements are non-transactional and as such don't replicate through write-sets.  There are two methods available that determine how the node handles replicating these statements:

- ``TOI``  In the :term:`Total Order Isolation` method, the cluster runs the DDL statement on all nodes in the same total order sequence, blocking other transactions from committing while the DDL is in progress.

- ``RSU`` In the :term:`Rolling Schema Upgrade` method, the node runs the DDL statements locally, thus blocking only the one node where the statement was made.  While processing the DDL statement, the node is not replicating and may be unable to process replication events due to a table lock.  Once the DDL operation is complete, the node catches up and syncs with the cluster to become fully operational again.  The DDL statement or its effects are not replicated; the user is responsible for manually executing this statement on each node in the cluster.

- ``NBO`` When the Non Blocking Option is used, DDL statements are processed in three phases:
  
  1. MDL lock requests for the operation are replicated first
  
  2. DDL statements are executed, with MDL protection 
  
  3. Finally, the MDL lock release requests are replicated

For more information on DDL statements and OSU methods, see :doc:`schema-upgrades`.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-osu-mode``"
   "System Variable", "``wsrep-osu-mode``"
   "Variable Scope", "Global and Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "(TOI | RSU | NBO)"
   "Default Value", "``TOI`` "
   "Initial Version", "Version 1.0"
   "MariaDB Version", "Version 10.5"

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'Parameters; wsrep-osu-mode';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | Parameters; wsrep-osu-mode   | TOI   |
    +------------------------------+-------+


.. _`wsrep_strict_ddl`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_strict_ddl``

.. index::
   pair: Parameters; wsrep_strict_ddl

If set, rejects DDL on affected tables not supporting Galera replication.


.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_strict_ddl``"
   "System Variable", "``wsrep_strict_ddl``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean (OFF, ON)"
   "Default Value", "``OFF`` "
   "Initial Version", "Version 1.0"
   "MariaDB Version", "Version 10.5"

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'Parameters; wsrep_strict_ddl';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | Parameters; wsrep_strict_ddl | OFF   |
    +------------------------------+-------+


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

   <br />

