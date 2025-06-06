.. meta::
   :title: MariaDB Options
   :description:
   :language: en-US
   :keywords: galera cluster, mariadb options, galera options
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
.. _`mariadb-options`:

======================
MariaDB Options
======================

These are MariaDB Server and Enterprise options. If you click a particular variable in this table, your web browser will scroll down to the entry for it with more details and a description.

.. _`mariadb_server_options`:
.. rst-class:: section-heading
.. rubric:: MariaDB Server Options


.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 20, 6, 6, 18, 18

   ":ref:`wsrep_allowlist <wsrep_allowlist>`", "``None``", "Yes", "No", "10.10", ""
   ":ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>`", "``0``", "Yes", "Yes", "10.1.4", ""
   ":ref:`wsrep_gtid_mode <wsrep_gtid_mode>`", "``OFF``", "Yes", "Yes", "10.1.4", ""
   ":ref:`wsrep_gtid_seq_no <wsrep_gtid_seq_no>`", "", "No", "Yes", "10.5.1", ""
   ":ref:`wsrep-mysql-replication-bundle <wsrep-mysql-replication-bundle>`", "``0``", "Yes", "No", "10.2.0", ""
   ":ref:`wsrep_patch_version <wsrep_patch_version>`", "", "Yes", "No", "10.1.5", ""
   ":ref:`wsrep_replicate_myisam <wsrep_replicate_aria>`", "OFF", "Yes", "Yes", "", "10.6"
   ":ref:`wsrep_replicate_myisam <wsrep_replicate_myisam>`", "OFF", "Yes", "Yes", "", "10.6"




.. _`wsrep_allowlist`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_allowlist``

.. index::
   pair: Parameters; wsrep_allowlist

This system variable allows you to add comma-delimited IP addresses to an allow list for Galera Cluster node addresses that can make SST/IST requests.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_allowlist=#``"
   "System Variable", "``wsrep_allowlist``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Data Type", "String"
   "Default Value", "``None`` "
   "MariaDB Version", "Version 10.10"



.. _`wsrep_gtid_domain_id`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_gtid_domain_id``

.. index::
   pair: Parameters; wsrep_gtid_domain_id

This system variable defines the GTID domain ID that is used for wsrep GTID mode.

- When :ref:`wsrep_gtid_mode <wsrep_gtid_mode>` is set to ON, ``wsrep_gtid_domain_id`` is used in place of ``gtid_domain_id`` for all Galera Cluster write sets.

- When :ref:`wsrep_gtid_mode <wsrep_gtid_mode>` is set to OFF, ``wsrep_gtid_domain_id`` is simply ignored to allow for backward compatibility.

- There are some additional requirements that need to be met in order for this mode to generate consistent GTIDs. For more information, see `Using MariaDB GTIDs with MariaDB Galera Cluster <https://mariadb.com/kb/en/using-mariadb-gtids-with-mariadb-galera-cluster/>`_.

|br|

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

- When ``wsrep_gtid_mode`` is set to ON, :ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>` is used in place of ``gtid_domain_id`` for all Galera Cluster write sets.

- When ``wsrep_gtid_mode`` is set to OFF, :ref:`wsrep_gtid_domain_id <wsrep_gtid_domain_id>` is simply ignored to allow for backward compatibility.

- There are some additional requirements that need to be met in order for this mode to generate consistent GTIDs. For more information, see `Using MariaDB GTIDs with MariaDB Galera Cluster <https://mariadb.com/kb/en/using-mariadb-gtids-with-mariadb-galera-cluster/>`_.

|br|

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

   "Command-line Format", "None"
   "System Variable", "``Internal server usage, manually set WSREP GTID seqno.``"
   "Variable Scope", "Session only"
   "Dynamic Variable", "Yes"
   "Data Type", "Numeric"
   "Range", "``0`` to ``18446744073709551615``"
   "MariaDB Version", "Version 10.5.1"


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
   "MariaDB Version", "Version 10.2.0"


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



.. _`wsrep_replicate_aria`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_replicate_aria``

.. index::
   pair: Parameters; wsrep_replicate_aria

Whether or not DML updates for ARIA tables will be replicated. This functionality is still experimental and should not be relied upon in production systems. 

This option is deprecated in MariaDB 10.6, and removed in MariaDB 10.7, use :ref:`wsrep_mode <wsrep_mode>` instead. Together with ``wsrep_mode=REPLICATE_MYISAM``, this parameter enables Galera to replicate both DDL and DML for ARIA and/or MyISAM using TOI. This option requires a primary key for the replicated table. To use this mode, set on ``REQUIRED_PRIMARY_KEY,REPLICATE_MYISAM,REPLICATE_ARIA``.


.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_replicate_aria``"
   "System Variable", "``wsrep_replicate_aria``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean (OFF, ON)"
   "Default Value", "``OFF`` "

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'Parameters; wsrep_replicate_aria';

    +----------------------------------+-------+
    | Variable_name                    | Value |
    +----------------------------------+-------+
    | Parameters; wsrep_replicate_aria | OFF   |
    +----------------------------------+-------+
   
   
.. _`wsrep_replicate_myisam`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_replicate_myisam``

.. index::
   pair: Parameters; wsrep_replicate_myisam

Whether or not DML updates for MyISAM tables will be replicated. This functionality is still experimental and should not be relied upon in production systems. 

This option is deprecated in MariaDB 10.6, and removed in MariaDB 10.7, use :ref:`wsrep_mode <wsrep_mode>` instead. Together with ``wsrep_mode=REPLICATE_ARIA``, this parameter enables Galera to replicate both DDL and DML for ARIA and/or MyISAM using TOI. This option requires a primary key for the replicated table. To use this mode, set on ``REQUIRED_PRIMARY_KEY,REPLICATE_MYISAM,REPLICATE_ARIA``.


.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_replicate_myisam``"
   "System Variable", "``wsrep_replicate_myisam``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean (OFF, ON)"
   "Default Value", "``OFF`` "

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'Parameters; wsrep_replicate_myisam';

    +------------------------------------+-------+
    | Variable_name                      | Value |
    +------------------------------------+-------+
    | Parameters; wsrep_replicate_myisam | OFF   |
    +------------------------------------+-------+




.. _`mariadb_enterprise_options`:
.. rst-class:: section-heading
.. rubric:: MariaDB Enterprise Options

.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 20, 19, 6, 11, 12

   ":ref:`wsrep-OSU-method <wsrep-osu-method>`", "``TOI``", "Global and Session", "Yes", "10.5", ""
   ":ref:`wsrep_strict_ddl <wsrep_strict_ddl>`", "``OFF``", "Yes", "Yes", "10.5", "10.6.0"



.. _`wsrep-osu-method`:
.. rst-class:: section-heading
.. rubric:: ``wsrep-OSU-method``

.. index::
   pair: Parameters; wsrep-OSU-method

This parameter defines the mode for Online Schema Upgrade that the node uses to replicate DDL statements.

DDL statements are non-transactional and as such do not replicate through write-sets. There are three methods available that determine how the node handles replicating these statements:

- ``TOI``  In the :term:`Total Order Isolation` method, the cluster runs the DDL statement on all nodes in the same total order sequence, blocking other transactions from committing while the DDL is in progress.

- ``RSU`` In the :term:`Rolling Schema Upgrade` method, the node runs the DDL statements locally, thus blocking only the one node where the statement was made. While processing the DDL statement, the node is not replicating and may be unable to process replication events due to a table lock. Once the DDL operation is complete, the node catches up and syncs with the cluster to become fully operational again. The DDL statement or its effects are not replicated; the user is responsible for manually executing this statement on each node in the cluster.

- ``NBO`` When the Non Blocking Option is used, DDL statements are processed in three phases:

  1. MDL lock requests for the operation are replicated first

  2. DDL statements are executed, with MDL protection

  3. Finally, the MDL lock release requests are replicated

For more information on DDL statements and OSU methods, see :doc:`schema-upgrades`.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-OSU-method``"
   "System Variable", "``wsrep-osu-method``"
   "Variable Scope", "Global and Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "(TOI | RSU | NBO)"
   "Default Value", "``TOI`` "
   "MariaDB Version", "Version 10.5"
   "MariaDB Enterprise Server (for NBO)", "Version 10.5"

You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'Parameters; wsrep-OSU-method';

    +--------------------------------+-------+
    | Variable_name                  | Value |
    +--------------------------------+-------+
    | Parameters; wsrep-OSU-method   | TOI   |
    +--------------------------------+-------+


.. _`wsrep_strict_ddl`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_strict_ddl``

.. index::
   pair: Parameters; wsrep_strict_ddl

.. note:: This feature has been **deprecated** in MariaDB 10.6.0 and **removed** in MariaDB 10.7. Use ``wsrep_mode=STRICT_REPLICATION`` instead. See :ref:`wsrep_mode <wsrep_mode>`.

If set, rejects DDL on affected tables not supporting Galera replication.


.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_strict_ddl``"
   "System Variable", "``wsrep_strict_ddl``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean (OFF, ON)"
   "Default Value", "``OFF`` "
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

