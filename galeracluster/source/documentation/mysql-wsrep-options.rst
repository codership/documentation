.. cssclass:: library-document

======================
 MySQL wsrep Options
======================
.. _`mysql-wsrep-options`:
.. index::
   single: Drupal
.. index::
   pair: Logs; Debug log


These are MySQL system variables introduced by wsrep API patch version 0.8. Almost all of the variables are global except for a few. Those are session variables.  If you click on a particular variable in this table, your web browser will scroll down to the entry for it with more details and an explanation.


.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic", "Initial |br| Version", "Version |br| Deprecated"
   :widths: 30, 42, 6, 6, 8, 8

   ":ref:`wsrep_auto_increment_control <wsrep_auto_increment_control>`", "``ON``", "Yes", "", "1.0", ""
   ":ref:`wsrep_causal_reads <wsrep_causal_reads>`", "``OFF``", "", "", "1.0", "3.6"
   ":ref:`wsrep_certify_nonPK <wsrep_certify_nonPK>`", "``ON``", "", "Yes", "1.0", ""
   ":ref:`wsrep_cluster_address <wsrep_cluster_address>`", "``ON``", "Yes", "", "1.0", ""
   ":ref:`wsrep_cluster_name <wsrep_cluster_name>`", "``example_cluster``", "Yes", "", "1.0", ""
   ":ref:`wsrep_convert_LOCK_to_trx <wsrep_convert_LOCK_to_trx>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_data_home_dir <wsrep_data_home_dir>`", "``/path/to/datadir``", "Yes", "", "1.0", ""
   ":ref:`wsrep_dbug_option <wsrep_dbug_option>`", "", "Yes", "", "1.0", ""
   ":ref:`wsrep_debug <wsrep_debug>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_desync <wsrep_desync>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_dirty_reads <wsrep_dirty_reads>`", "``OFF``", "Yes", "Yes", "1.0", ""
   ":ref:`wsrep_drupal_282555_workaround <wsrep_drupal_282555_workaround>`", "``ON``", "Yes", "", "1.0", ""
   ":ref:`wsrep_forced_binlog_format <wsrep_forced_binlog_format>`", "``NONE``", "Yes", "", "1.0", ""
   ":ref:`wsrep_load_data_splitting <wsrep_load_data_splitting>`", "``ON``", "Yes", "", "1.0", ""
   ":ref:`wsrep_log_conflicts <wsrep_log_conflicts>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_max_ws_rows <wsrep_max_ws_rows>`", "``0``", "Yes", "", "1.0", ""
   ":ref:`wsrep_max_ws_size <wsrep_max_ws_size>`", "``1G``", "Yes", "", "1.0", ""
   ":ref:`wsrep_node_address <wsrep_node_address>`", "*host address:default port*", "Yes", "", "1.0", ""
   ":ref:`wsrep_node_incoming_address <wsrep_node_incoming_address>`", "*host address:mysqld port*", "Yes", "", "1.0", ""
   ":ref:`wsrep_node_name <wsrep_node_name>`", "``<hostname>``", "Yes", "", "1.0", ""
   ":ref:`wsrep_notify_cmd <wsrep_notify_cmd>`", "", "Yes", "", "1.0", ""
   ":ref:`wsrep_on <wsrep_on>`", "``ON``", "Yes", "", "1.0", ""
   ":ref:`wsrep_OSU_method <wsrep_OSU_method>`", "``TOI``", "", "", "3.0", ""
   ":ref:`wsrep_preordered <wsrep_preordered>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_provider <wsrep_provider>`", "``NONE``", "Yes", "", "1.0", ""
   ":ref:`wsrep_provider_options <wsrep_provider_options>`", "", "Yes", "", "1.0", ""
   ":ref:`wsrep_reject_queries <wsrep_reject_queries>`", "``NONE``", "Yes", "Yes", "???", ""
   ":ref:`wsrep_restart_slave <wsrep_restart_slave>`", "``OFF``", "Yes", "Yes", "1.0", ""
   ":ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>`", "``1``", "Yes", "", "1.0", ""
   ":ref:`wsrep_slave_FK_checks <wsrep_slave_FK_checks>`", "``ON``", "Yes", "Yes", "1.0", ""
   ":ref:`wsrep_slave_threads <wsrep_slave_threads>`", "``1``", "Yes", "", "1.0", ""
   ":ref:`wsrep_slave_UK_checks <wsrep_slave_UK_checks>`", "``OFF``", "Yes", "Yes", "1.0", ""
   ":ref:`wsrep_sst_auth <wsrep_sst_auth>`", "", "Yes", "", "1.0", ""
   ":ref:`wsrep_sst_donor <wsrep_sst_donor>`", "", "Yes", "", "1.0", ""
   ":ref:`wsrep_sst_donor_rejects_queries <wsrep_sst_donor_rejects_queries>`", "``OFF``", "Yes", "", "1.0", ""
   ":ref:`wsrep_sst_method <wsrep_sst_method>`", "``mysqldump``", "Yes", "", "1.0", ""
   ":ref:`wsrep_sst_receive_address <wsrep_sst_receive_address>`", "*node IP address*", "Yes", "", "1.0", ""
   ":ref:`wsrep_start_position <wsrep_start_position>`", "*see reference entry*", "Yes", "", "1.0", ""
   ":ref:`wsrep_sync_wait <wsrep_sync_wait>`", "``0``", "Yes", "Yes", "3.6", ""
   ":ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`", "``0``", "Yes", "Yes", "4.0", ""
   ":ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>`", "``bytes``", "Yes", "Yes", "4.0", ""
   ":ref:`wsrep_ws_persistency <wsrep_ws_persistency>`", "", "Yes", "", "1.0", ""


You can execute the ``SHOW VARIABLES`` statement with the ``LIKE`` operator as shown below to get list of all Galera related variables on your server:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep%';

The results will vary depending on which version of Galera is running on your server. All of the parameters and variables possible are listed above, but they're listed below with explanations of each.


.. _`wsrep_auto_increment_control`:
.. rubric:: ``wsrep_auto_increment_control``
.. index::
   pair: Parameters; wsrep_auto_increment_control

This parameter enables the automatic adjustment of auto increment system variables with changes in cluster membership.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-auto-increment-control``"
   "System Variable", "``wsrep_auto_increment_control``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``ON`` "
   "Initial Version", "Version 1.0"

The node manages auto-increment values in a table using two variables: ``auto_increment_increment`` and ``auto_increment_offset``.  The first relates to the value auto-increment rows count from the offset. The second relates to the offset it should use in moving to the next position.

The :ref:`wsrep_auto_increment_control <wsrep_auto_increment_control>` parameter enables additional calculations to this process, using the number of nodes connected to the :term:`Primary Component` to adjust the increment and offset.  This is done to reduce the likelihood that two nodes will attempt to write the same auto-increment value to a table.

It significantly reduces the rate of certification conflicts for ``INSERT`` statements. You can execute the following ``SHOW VARIABLES`` statement to see how its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_auto_increment_control';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | wsrep_auto_increment_control | ON    |
    +------------------------------+-------+


.. _`wsrep_causal_reads`:
.. rubric:: ``wsrep_causal_reads``
.. index::
   pair: Parameters; wsrep_causal_reads

This parameter enables the enforcement of strict cluster-wide ``READ COMMITTED`` semantics on non-transactional reads. It results in larger read latencies.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-causal-reads``"
   "System Variable", "``wsrep_causal_reads``"
   "Variable Scope", "Session"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF`` "
   "Initial Version", "Version 1.0, Deprecated in Version 3.6"

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_causal_reads';

.. warning:: The ``wsrep_causal_reads`` option has been **deprecated**.  It has been replaced by :ref:`wsrep_sync_wait <wsrep_sync_wait>`.


.. _`wsrep_certification_rules`:
.. rubric:: ``wsrep_certification_rules``
.. index::
   pair: Parameters; wsrep_certification_rules

Certification rules to use in the cluster.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-certification-rules``"
   "System Variable", "``wsrep_certification_rules``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Enumeration"
   "Default Value", "``STRICT``"
   "Valid Value", "``OPTIMIZED``, ``STRICT``"
   "Initial Version", "Version ???"

Controls how certification is done in the cluster, in particular this affects how foreign keys are handled: with the ``STRICT`` option two INSERTs that happen at about the same time on two different nodes in a child table, that insert different (non conflicting rows), but both rows point to the same row in the parent table could result in certification failure. With the ``OPTIMIZED`` option such certification failure is avoided.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_certification_rules';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_certification_rules | STRICT |
   +---------------------------+--------+

.. note:: This is a MySQL wsrep parameter. It was introduced in 5.5.61-25.24, 5.6.41-25.23, 5.7.23-25.15.


.. _`wsrep_certify_nonPK`:
.. rubric:: ``wsrep_certify_nonPK``
.. index::
   pair: Parameters; wsrep_certify_nonPK

This parameter is used to define whether the node should generate primary keys on rows without them for the purposes of certification.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-certify-nonpk``"
   "System Variable", "``wsrep_certify_nonpk``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``ON`` "
   "Initial Version", "Version 1.0"

Galera Cluster requires primary keys on all tables.  The node uses the primary key in replication to allow for the parallel applying of transactions to a table.  This parameter tells the node that when it encounters a row without a primary key, it should create one for replication purposes.  However, as a rule don't use tables without primary keys.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_certify_nonpk';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_certify_nonpk | ON    |
   +---------------------+-------+


.. _`wsrep_cluster_address`:
.. rubric:: ``wsrep_cluster_address``
.. index::
   pair: Parameters; wsrep_cluster_address
.. index::
   single: my.cnf

This parameter sets the back-end schema, IP addresses, ports and options the node uses in connecting to the cluster.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-cluster-address``"
   "System Variable", "``wsrep_cluster_address``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

Galera Cluster uses this parameter to determine the IP addresses for the other nodes in the cluster, the back-end schema to use and additional options it should use in connecting to and communicating with those nodes.  Currently, the only back-end schema supported for production is ``gcomm``.

Below is the syntax for this the values of this parameter:

.. code-block:: text

    <backend schema>://<cluster address>[?option1=value1[&option2=value2]]

Here's an example of how that might look:

.. code-block:: ini

   wsrep_cluster_address="gcomm://192.168.0.1:4567?gmcast.listen_addr=0.0.0.0:5678"

Changing this variable while Galera is running will cause the node to close the connection to the current cluster, and reconnect to the new address. Doing this at runtime may not be possible, though, for all SST methods. As of Galera Cluster 23.2.2, it is possible to provide a comma-separated list of other nodes in the cluster as follows:

.. code-block:: text

    gcomm://node1:port1,node2:port2,...[?option1=value1&...]

Using the string ``gcomm://`` without any address will cause the node to startup alone, thus initializing a new cluster--that the other nodes can join to.  Using ``--wsrep-new-cluster`` is the newer, preferred way.

.. warning:: Never use an empty ``gcomm://`` string with the ``wsrep_cluster_address`` option in the configuration file. If a node restarts, it will cause the node not to rejoin the cluster. Instead, it will initialize a new one-node cluster and cause a split brain. To bootstrap a cluster, you should only pass the ``--wsrep-new-cluster`` string at the command-line--instead of using ``--wsrep-cluster-address="gcomm://"``. For more information, see :doc:`Starting the Cluster <../training/tutorials/starting-cluster>`.

You can execute the following SQL statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_cluster_address';

   +-----------------------+---------------------------------------------+
   | Variable_name         | Value                                       |
   +-----------------------+---------------------------------------------+
   | wsrep_cluster_address | gcomm://192.168.1.1,192.168.1.2,192.168.1.3 |
   +-----------------------+---------------------------------------------+


.. _`wsrep_cluster_name`:
.. rubric:: ``wsrep_cluster_name``
.. index::
   pair: Parameters; wsrep_cluster_name

This parameter defines the logical cluster name for the node.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-cluster-name``"
   "System Variable", "``wsrep_cluster_name``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "``exmaple_cluster``"
   "Initial Version", "Version 1.0"

This parameter allows you to define the logical name the node uses for the cluster.  When a node attempts to connect to a cluster, it checks the value of this parameter against that of the cluster.  The connection is only made if the names match.  If they don't match, the connection fails.  Because of this, the cluster name must be the same on all nodes.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_cluster_name';

   +--------------------+-----------------+
   | Variable_name      | Value           |
   +--------------------+-----------------+
   | wsrep_cluster_name | example_cluster |
   +--------------------+-----------------+


.. _`wsrep_convert_lock_to_trx`:
.. rubric:: ``wsrep_convert_lock_to_trx``
.. index::
   pair: Parameters; wsrep_convert_lock_to_trx

This parameter is used to set whether the node converts ``LOCK/UNLOCK TABLES`` statements into ``BEGIN/COMMIT`` statements.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-convert-lock-to-trx``"
   "System Variable", "``wsrep_convert_lock_to_trx``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version 1.0"

This parameter determines how the node handles ``LOCK/UNLOCK TABLES`` statements, specifically whether or not you want it to convert these statements into ``BEGIN/COMMIT`` statements.  It tells the node to convert implicitly locking sessions into transactions within the database server. By itself, this is not the same as support for locking sections, but it does prevent the database from resulting in a logically inconsistent state.

This parameter may help sometimes to get old applications working in a multi-master setup.

.. note:: Loading a large database dump with ``LOCK`` statements can result in abnormally large transactions and cause an out-of-memory condition.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_convert_lock_to_trx';

   +---------------------------+-------+
   | Variable_name             | Value |
   +---------------------------+-------+
   | wsrep_convert_lock_to_trx | OFF   |
   +---------------------------+-------+


.. _`wsrep_data_home_dir`:
.. rubric:: ``wsrep_data_home_dir``
.. index::
   pair: Parameters; wsrep_data_home_dir

Use this parameter to set the directory the wsrep Provider uses for its files.

.. csv-table::
   :class: doc-options

   "Command-line Format", "???"
   "System Variable", "``wsrep_data_home_dir``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Directory"
   "Default Value", "/path/mysql_datadir"
   "Initial Version", "Version 1.0"

During operation, the wsrep Provider needs to save various files to disk that record its internal state.  This parameter defines the path to the directory that you want it to use.  If not set, it defaults the MySQL ``datadir`` path.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_data_home_dir';

   +---------------------+----------------+
   | Variable_name       | Value          |
   +---------------------+----------------+
   | wsrep_data_home_dir | /var/lib/mysql |
   +---------------------+----------------+


.. _`wsrep_dbug_option`:
.. rubric:: ``wsrep_dbug_option``
.. index::
   pair: Parameters; wsrep_dbug_option

You can set debug options to pass to the wsrep Provider with this parameter.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-dbug-option``"
   "System Variable", "``wsrep_dbug_option``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set, if its set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_dbug_option';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_dbug_option |       |
   +-------------------+-------+


.. _`wsrep_debug`:
.. rubric:: ``wsrep_debug``
.. index::
   pair: Parameters; wsrep_debug

This parameter enables additional debugging output for the database server error log.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-debug``"
   "System Variable", "``wsrep_debug``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version 1.0"

Under normal operation, error events are logged to an error log file for the database server.  By default, the name of this file is the server hostname with the ``.err`` extension.  You can define a custom path using the `log_error <https://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_log_error>`_ parameter. When you enable :ref:`wsrep_debug <wsrep_debug>`, the database server logs additional events surrounding these errors to help in identifying and correcting problems.

.. warning:: In addition to useful debugging information, the ``wsrep_debug`` parameter also causes the database server to print authentication information (i.e., passwords) to the error logs.  Don't enable it in production environments.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see if this variable is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_debug';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_debug   | OFF   |
   +---------------+-------+


.. _`wsrep_desync`:
.. rubric:: ``wsrep_desync``
.. index::
   pair: Parameters; wsrep_desync

This parameter is used to set whether or not the node participates in Flow Control.

.. csv-table::
   :class: doc-options

   "Command-line Format", "???"
   "System Variable", "``wsrep_desync``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version 1.0"

When a node receives more write-sets than it can apply, the transactions are placed in a received queue.  In the event that the node falls too far behind, it engages Flow Control.  The node takes itself out of sync with the cluster and works through the received queue until it reaches a more manageable size.

For more information on Flow Control and how to configure and manage it in a cluster, see :doc:`node-states` and :doc:`managing-fc`.

When set to ``ON``, this parameter disables Flow Control for the node.  The node will continue to receive write-sets and fall further behind the cluster.  The cluster doesn't wait for desynced nodes to catch up, even if it reaches the ``fc_limit`` value.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see if this variable is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_desync';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_desync  | OFF   |
   +---------------+-------+


.. _`wsrep_dirty_reads`:
.. rubric:: ``wsrep_dirty_reads``
.. index::
   pair: Parameters; wsrep_dirty_reads

This parameter defines whether the node accepts read queries when in a non-operational state.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-dirty-reads``"
   "System Variable", "``wsrep_dirty_reads``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "???"


When a node loses its connection to the :term:`Primary Component`, it enters a non-operational state.  Given that it can't keep its data current while in this state, it rejects all queries with an ``ERROR: Unknown command`` message.  This parameter determines whether or not the node permits reads while in a non-operational state.

.. note:: Remember that by its nature, data reads from nodes in a non-operational state are stale.  Current data in the Primary Component remains inaccessible to these nodes until they rejoin the cluster.

When enabling this parameter, the node only permits reads. It still rejects any command that modifies or updates the database.  When in this state, the node allows ``USE``, ``SELECT``, ``LOCK TABLE`` and ``UNLOCK TABLES`` statements.  It doesn't allow DDL statements.  It also rejects DML statements (i.e., ``INSERT``, ``DELETE`` and ``UPDATE``).

You must set the :ref:`wsrep_sync_wait <wsrep_sync_wait>` parameter to ``0`` when using this parameter, else it raises a deadlock error.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see if this variable is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_dirty_reads';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_dirty_reads | ON    |
   +-------------------+-------+

.. note:: This is a MySQL wsrep parameter.  It was introduced in version 5.6.29.


.. _`wsrep_drupal_282555_workaround`:
.. rubric:: ``wsrep_drupal_282555_workaround``
.. index::
   pair: Parameters; wsrep_drupal_282555_workaround

This parameter enables workaround for a bug in MySQL InnoDB that affects Drupal installations.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-drupal-282555-workaround``"
   "System Variable", "``wsrep_drupal_282555_workaround``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "Version 1.0"

Drupal installations using MySQL are subject to a bug in InnoDB, tracked as `MySQL Bug 41984 <http://bugs.mysql.com/bug.php?id=41984>`_ and `Drupal Issue 282555 <http://drupal.org/node/282555>`_.  Specifically, inserting a `DEFAULT` value into an `AUTO_INCREMENT` column may return duplicate key errors.

This parameter enables a workaround for the bug on Galera Cluster.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see if this variable is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_drupal_28255_workaround';

   +-------------------------------+-------+
   | Variable_name                 | Value |
   +-------------------------------+-------+
   | wsrep_drupal_28255_workaround | ON    |
   +-------------------------------+-------+


.. _`wsrep_forced_binlog_format`:
.. rubric:: ``wsrep_forced_binlog_format``
.. index::
   pair: Parameters; wsrep_forced_binlog_format

This parameter defines the binary log format for all transactions.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-forced-binlog-format``"
   "System Variable", "``wsrep_forced_binlog_format``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Enumeration"
   "Default Value", "``NONE``"
   "Valid Values", "``ROW``, ``STATEMENT``, ``MIXED``, ``NONE``"
   "Initial Version", "Version 1.0"

The node uses the format given by this parameter regardless of the client session variable `binlog_format <https://dev.mysql.com/doc/refman/5.5/en/binary-log-setting.html>`_.  Valid choices for this parameter are: ``ROW``, ``STATEMENT``, and ``MIXED``.  Additionally, there is the special value ``NONE``, which means that there is no forced format in effect for the binary logs. When set to a value other than ``NONE``, this parameter forces all transactions to use a given binary log format.

This variable was introduced to support ``STATEMENT`` format replication during :term:`Rolling Schema Upgrade`.  In most cases, however, ``ROW`` format replication is valid for asymmetric schema replication.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_forced_binlog_format';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_forced_binlog_format | NONE  |
   +----------------------------+-------+


.. _`wsrep_load_data_splitting`:
.. rubric:: ``wsrep_load_data_splitting``
.. index::
   pair: Parameters; wsrep_load_data_splitting

This parameter defines whether the node splits large ``LOAD DATA`` commands into more manageable units.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-load-data-splitting``"
   "System Variable", "``wsrep_load_data_splitting``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "Version 1.0"

When loading huge amounts of data creates problems for Galera Cluster, in that they eventually reach a size that is too large for the node to rollback completely the operation in the event of a conflict and whatever gets committed stays committed.

This parameter tells the node to split ``LOAD DATA`` commands into transactions of 10,000 rows or less, making the data more manageable for the cluster.  This deviates from the standard behavior for MySQL.

You can execute the following ``SHOW VARIABLES`` statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_load_data_splitting';

   +---------------------------+-------+
   | Variable_name             | Value |
   +---------------------------+-------+
   | wsrep_load_data_splitting | ON    |
   +---------------------------+-------+


.. _`wsrep_log_conflicts`:
.. rubric:: ``wsrep_log_conflicts``
.. index::
   pair: Parameters; wsrep_log_conflicts

This parameter defines whether the node logs additional information about conflicts.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-log-conflicts``"
   "System Variable", "``wsrep_log_conflicts``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF`` "
   "Initial Version", "Version 1.0"


In Galera Cluster, the database server uses the standard logging features of MySQL, MariaDB and Percona XtraDB.  This parameter enables additional information for the logs pertaining to conflicts. You may find this useful in troubleshooting replication problems. You can also log conflict information with the wsrep Provider option :ref:`cert.log_conflicts <cert.log_conflicts>`.

The additional information includes the table and schema where the conflict occurred, as well as the actual values for the keys that produced the conflict.

You can execute the following ``SHOW VARIABLES`` statement to see if this feature is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_log_conflicts';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_log_conflicts | OFF   |
   +---------------------+-------+


.. _`wsrep_max_ws_rows`:
.. rubric:: ``wsrep_max_ws_rows``
.. index::
   pair: Parameters; wsrep_max_ws_rows


With this parameter you can set the maximum number of rows the node allows in a write-set.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-max-ws-rows``"
   "System Variable", "``wsrep_max_ws_rows``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "``0``"
   "Initial Version", "Version 1.0"

If set to a value greater than ``0``, this parameter sets the maximum number of rows that the node allows in a write-set.

You can execute the following ``SHOW VARIABLES`` statement to see the current value of this parameter:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_max_ws_rows';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_max_ws_rows | 128   |
   +-------------------+-------+


.. _`wsrep_max_ws_size`:
.. rubric:: ``wsrep_max_ws_size``
.. index::
   pair: Parameters; wsrep_max_ws_size

You can set the maximum size the node allows for write-sets with this parameter.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-max-ws-size``"
   "System Variable", "``wsrep_max_ws_size``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "``2G``"
   "Initial Version", "Version 1.0"

This parameter sets the maximum size that the node allows for a write-set.  Currently, this value limits the supported size of transactions and of ``LOAD DATA`` statements.

The maximum allowed write-set size is ``2G``.  You can execute the following ``SHOW VARIABLES`` statement to see the current value of this parameter:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_max_ws_size';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_max_ws_size | 2G    |
   +-------------------+-------+


.. _`wsrep_node_address`:
.. rubric:: ``wsrep_node_address``
.. index::
   pair: Parameters; wsrep_node_address


This parameter is used to note the IP address and port of the node.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-node-address``"
   "System Variable", "``wsrep_node_address``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "Server IP Address, Port ``4567``"
   "Initial Version", "Version 1.0"

The node passes its IP address and port number to the :term:`Galera Replication Plugin`, where it's used as the base address in cluster communications.  By default, the node pulls the address of the first network interface and uses the default port for Galera Cluster.  Typically, this is the address of ``eth0`` or ``enp2s0`` on port ``4567``.

While the default behavior is often sufficient, there are situations in which this auto-guessing function produces unreliable results.  Some common reasons are the following:

- Servers with multiple network interfaces;
- Servers that run multiple nodes;
- Network Address Translation (NAT);
- Clusters with nodes in more than one region;
- Container deployments, such as with Docker and jails; and
- Cloud deployments, such as with Amazon EC2 and OpenStack.

In these scenarios, since auto-guess of the IP address does not produce the correct result, you will need to provide an explicit value for this parameter.

.. note:: In addition to defining the node address and port, this parameter also provides the default values for the :ref:`wsrep_sst_receive_address <wsrep_sst_receive_address>` parameter and the :ref:`ist.recv_addr <ist.recv_addr>` option.

In some cases, you may need to provide a different value.  For example, Galera Cluster running on Amazon EC2 requires that you use the global DNS name instead of the local IP address.

You can execute the ``SHOW VARIABLES`` statement as shown below to get the current value of this parameter:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_node_address';

   +--------------------+-------------+
   | Variable_name      | Value       |
   +--------------------+-------------+
   | wsrep_node_address | 192.168.1.1 |
   +--------------------+-------------+


.. _`wsrep_node_incoming_address`:
.. rubric:: ``wsrep_node_incoming_address``
.. index::
   pair: Parameters; wsrep_node_incoming_address

This parameter is used to provide the IP address and port from which the node should expect client connections.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-node-incoming-address``"
   "System Variable", "``wsrep_node_incoming_address``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

This parameter defines the IP address and port number at which the node should expect to receive client connections.  It's intended for integration with load balancers. For now, it's otherwise unused by the node.

You can execute the ``SHOW VARIABLES`` statement with the ``LIKE`` operator as shown below to get the IP address and port setting of this parameter:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_node_incoming_address';

   +-----------------------------+------------------+
   | Variable_name               | Value            |
   +-----------------------------+------------------+
   | wsrep_node_incoming_address | 192.168.1.1:3306 |
   +-----------------------------+------------------+


.. _`wsrep_node_name`:
.. rubric:: ``wsrep_node_name``
.. index::
   pair: Parameters; wsrep_node_name

You can set the logical name that the node uses for itself with this parameter.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-node-name``"
   "System Variable", "``wsrep_node_name``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "Server Hostname"
   "Initial Version", "Version 1.0"

This parameter defines the logical name that the node uses when referring to itself in logs and in the cluster.  It's for convenience, to help you in identifying nodes in the cluster by means other than the node address.

By default, the node uses the server hostname.  In some situations, you may need explicitly to set it. You would do this when using container deployments with Docker or FreeBSD jails, where the node uses the name of the container rather than the hostname.

You can execute the ``SHOW VARIABLES`` statement with the ``LIKE`` operator as shown below to get the node name:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_node_name';

   +-----------------+-------------+
   | Variable_name   | Value       |
   +-----------------+-------------+
   | wsrep_node_name | GaleraNode1 |
   +-----------------+-------------+


.. _`wsrep_notify_cmd`:
.. rubric:: ``wsrep_notify_cmd``
.. index::
   pair: Parameters; wsrep_notify_cmd

Defines the command the node runs whenever cluster membership or the state of the node changes.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-notify-cmd``"
   "System Variable", "``wsrep_notify_cmd``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

Whenever the node registers changes in cluster membership or its own state, this parameter allows you to send information about that change to an external script defined by the value.  You can use this to reconfigure load balancers, raise alerts and so on, in response to node and cluster activity.

.. warning:: The node will block and wait until the script completes and returns before it can proceed. If the script performs any potentially blocking or long-running operations, such as network communication, you may wish initiate such operations in the background and have the script return immediately.

For an example script that updates two tables on the local node, with changes taking place at the cluster level, see the :doc:`notification-cmd`.

When the node calls the command, it passes one or more arguments that you can use in configuring your custom notification script and how it responds to the change.  Below are these options and explanations of each:

.. csv-table::
   :class: doc-options
   :header: "Option", "Purpose", "Possible Values"
   :widths: 25, 25, 50

   "``--status <status str>``", "The status of this node.", "``Undefined`` The node has just started up and is not connected to any :term:`Primary Component`."
   "", "", "``Joiner`` The node is connected to a primary component and now is receiving state snapshot."
   "", "", "``Donor`` The node is connected to primary component and now is sending state snapshot."
   "", "", "``Joined`` The node has a complete state and now is catching up with the cluster."
   "", "", "``Synced`` The node has synchronized itself with the cluster."
   "", "", "``Error(<error code if available>)`` The node is in an error state."
   "``--uuid <state UUID>``", "The cluster state UUID.", ""
   "``--primary <yes/no>``", "Whether the current cluster component is primary or not.", ""
   "``--members <list>``", "A comma-separated list of the component member UUIDs.", "``<node UUID>``; A unique node ID. The wsrep Provider automatically assigns this ID for each node."
   "", "", "``<node name>``; The node name as it is set in the ``wsrep_node_name`` option."
   "", "", "``<incoming address>``; The address for client connections as it is set in the ``wsrep_node_incoming_address`` option."
   "``--index``", "The index of this node in the node list.", ""

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_notify_cmd';

   +------------------+--------------------------+
   | Variable_name    | Value                    |
   +------------------+--------------------------+
   | wsrep_notify_cmd | /usr/bin/wsrep_notify.sh |
   +------------------+--------------------------+


.. _`wsrep_on`:
.. rubric:: ``wsrep_on``
.. index::
   pair: Parameters; wsrep_on

Defines whether replication takes place for updates from the current session.

.. csv-table::
   :class: doc-options

   "Command-line Format", "???"
   "System Variable", "``wsrep_on``"
   "Variable Scope", "Session"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "Version 1.0"

This parameter defines whether or not updates made in the current session replicate to the cluster.  It does not cause the node to leave the cluster and the node continues to communicate with other nodes.  Additionally, it is a session variable.  Defining it through the ``SET GLOBAL`` syntax also affects future sessions.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_on';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_on      | ON    |
   +---------------+-------+


.. _`wsrep_OSU_method`:
.. rubric:: ``wsrep_OSU_method``
.. index::
   pair: Parameters; wsrep_OSU_method

Defines the Online Schema Upgrade method the node uses to replicate :abbr:`DDL (Data Definition Language)` statements.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-OSU-method``"
   "System Variable", "``wsrep_OSU_method``"
   "Variable Scope", "Global, Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Enumeration"
   "Default Value", "``TOI``"
   "Valid Values", "``TOI``, ``RSU``"
   "Initial Version", "Version 3, Patch 5.5.17-22.3"

DDL statements are non-transactional and as such don't replicate through write-sets.  There are two methods available that determine how the node handles replicating these statements:

- ``TOI``  In the :term:`Total Order Isolation` method, the cluster runs the DDL statement on all nodes in the same total order sequence, blocking other transactions from committing while the DDL is in progress.

- ``RSU`` In the :term:`Rolling Schema Upgrade` method, the node runs the DDL statements locally, thus blocking only the one node where the statement was made.  While processing the DDL statement, the node is not replicating and may be unable to process replication events due to a table lock.  Once the DDL operation is complete, the node catches up and syncs with the cluster to become fully operational again.  The DDL statement or its effects are not replicated; the user is responsible for manually executing this statement on each node in the cluster.

For more information on DDL statements and OSU methods, see :doc:`schema-upgrades`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_OSU_method';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_OSU_method | TOI   |
   +------------------+-------+


.. _`wsrep_preordered`:
.. rubric:: ``wsrep_preordered``
.. index::
   pair: Parameters; wsrep_preordered

Defines whether the node uses transparent handling of preordered replication events.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-preordered``"
   "System Variable", "``wsrep_preordered``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version 1.0"

This parameter enables transparent handling of preordered replication events, such as replication events arriving from traditional asynchronous replication. When this option is ``ON``, such events will be applied locally first before being replicated to the other nodes of the cluster. This could increase the rate at which they can be processed which would be otherwise limited by the latency between the nodes in the cluster.

Preordered events should not interfere with events that originate on the local node. Therefore, you should not run local update queries on a table that is also being updated through asynchronous replication.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_preordered';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_preordered | OFF   |
   +------------------+-------+


.. _`wsrep_provider`:
.. rubric:: ``wsrep_provider``
.. index::
   pair: Parameters; wsrep_provider

Defines the path to the :term:`Galera Replication Plugin`.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-provider``"
   "System Variable", "``wsrep_provider``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "File"
   "Default Value", ""
   "Initial Version", "Version 1.0"

When the node starts, it needs to load the wsrep Provider in order to enable replication functions.  The path defined in this parameter tells it what file it needs to load and where to find it.  In the event that you do not define this path or you give it an invalid value, the node bypasses all calls to the wsrep Provider and behaves as a standard standalone instance of MySQL.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_provider';

   +----------------+----------------------------------+
   | Variable_name  | Value                            |
   +----------------+----------------------------------+
   | wsrep_provider | /usr/lib/galera/libgalera_smm.so |
   +----------------+----------------------------------+


.. _`wsrep_provider_options`:
.. rubric:: ``wsrep_provider_options``
.. index::
   pair: Parameters; wsrep_provider_options

Defines optional settings the node passes to the wsrep Provider.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-provider-options``"
   "System Variable", "``wsrep_provider_options``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

When the node loads the wsrep Provider, there are several configuration options available that affect how it handles certain events.  These allow you to fine tune how it handles various situations.

For example, you can use :ref:`gcache.size <gcache.size>` to define how large a write-set cache the node keeps or manage group communications timeouts.

.. note:: All ``wsrep_provider_options`` settings need to be specified on a single line. In case of multiple instances of ``wsrep_provider_options``, only the last one is used.

For more information on the wsrep Provider options, see :doc:`galera-parameters`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_provider_options';

   +------------------------+-----------------------------------------------+
   | Variable_name          | Value                                         |
   +------------------------+-----------------------------------------------+
   | wsrep_provider_options | ... evs.user_send_window=2,gcache.size=128Mb  |
   |                        | evs.auto_evict=0,debug=OFF, evs.version=0 ... |
   +------------------------+-----------------------------------------------+


.. _`wsrep_reject_queries`:
.. rubric:: ``wsrep_reject_queries``:

Defines whether the node rejects client queries while participating in the cluster.

.. csv-table::
   :class: doc-options

   "Command-line Format", ""
   "System Variable", "``wsrep_reject_queries``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Array"
   "Default Value", "``NONE``"
   "Valid Values", "``NONE``, ``ALL``, ``ALL_KILL``"
   "Initial Version", "Version ???"

When in use, this parameter causes the node to reject queries from client connections.  The node continues to participate in the cluster and apply write-sets, but client queries generate ``Unknown command`` errors.  For instance,

.. code-block:: mysql

   SELECT * FROM my_table;

   Error 1047: Unknown command

You may find this parameter useful in certain maintenance situations.  In enabling it, you can also decide whether or not the node maintains or kills any current client connections.

- ``NONE`` The node disables this feature.

- ``ALL`` The node enables this feature. It rejects all queries, but maintains any existing client connections.

- ``ALL_KILL`` The node enables this feature.  It rejects all queries and kills existing client connections without waiting, including the current connection.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_reject_queries';

   +----------------------+-------+
   | Variable_name        | Value |
   +----------------------+-------+
   | wsrep_reject_queries | NONE  |
   +----------------------+-------+

.. note:: This is a MySQL wsrep parameter.  It was introduced in version 5.6.29.


.. _`wsrep_restart_slave`:
.. rubric:: ``wsrep_restart_slave``
.. index::
   pair: Parameters; wsrep_restart_slave

Defines whether the replication slave restarts when the node joins the cluster.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-restart-slave``"
   "System Variable", "``wsrep_restart_slave``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version ???"

Enabling this parameter tells the node to restart the replication slave when it joins the cluster.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_restart_slave';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_restart_slave | OFF   |
   +---------------------+-------+


.. _`wsrep_retry_autocommit`:
.. rubric:: ``wsrep_retry_autocommit``
.. index::
   pair: Parameters; wsrep_retry_autocommit

Defines the number of retries the node attempts when an autocommit query fails.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-retry-autocommit``"
   "System Variable", "``wsrep_retry_autocommit``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Integer"
   "Default Value", "``1``"
   "Initial Version", "Version 1.0"

When an autocommit query fails the certification test due to a cluster-wide conflict, the node can retry it without returning an error to the client.  This parameter defines how many times the node retries the query.  It is analogous to rescheduling an autocommit query should it go into deadlock with other transactions in the database lock manager.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_retry_autocommit';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_retry_autocommit | 1     |
   +------------------------+-------+


.. _`wsrep_slave_FK_checks`:
.. rubric:: ``wsrep_slave_FK_checks``
.. index::
   pair: Parameters; wsrep_slave_FK_checks

Defines whether the node performs foreign key checking for applier threads.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-FK-checks``"
   "System Variable", "``wsrep_slave_FK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "Version 1.0"

This parameter enables foreign key checking on applier threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_slave_FK_checks';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_slave_FK_checks | ON    |
   +-----------------------+-------+


.. _`wsrep_slave_threads`:
.. rubric:: ``wsrep_slave_threads``
.. index::
   pair: Parameters; wsrep_slave_threads

Defines the number of threads to use in applying slave write-sets.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-threads``"
   "System Variable", "``wsrep_slave_threads``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Integer"
   "Default Value", "``1``"
   "Initial Version", "Version 1.0"

This parameter allows you to define how many threads the node uses when applying slave write-sets.  Performance on the underlying system and hardware, the size of the database, the number of client connections, and the load your application puts on the server all factor in the need for threading, but not in a way that makes the scale of that need easy to predict.  Because of this, there is no strict formula to determine how many slave threads your node actually needs.

Instead of concrete recommendations, there are some general guidelines that you can use as a starting point in finding the value that works best for your system:

- It is rarely beneficial to use a value that is less than twice the number of CPU cores on your system.

- Similarly, it is rarely beneficial to use a value that is more than one quarter the total number of client connections to the node.  While it is difficult to predict the number of client connections, being off by as much as 50% over or under is unlikely to make a difference.

- From the perspective of resource utilization, it's recommended that you keep to the lower end of slave threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_slave_threads';

   +---------------------+-------+
   | Variable_name       | Value |
   +---------------------+-------+
   | wsrep_slave_threads | 1     |
   +---------------------+-------+


.. _`wsrep_slave_UK_checks`:
.. rubric:: ``wsrep_slave_UK_checks``
.. index::
   pairs: Parameters; wsrep_slave_UK_checks

Defines whether the node performs unique key checking on applier threads.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-UK-checks``"
   "System Variable", "``wsrep_slave_UK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version ???"

This parameter enables unique key checking on applier threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_slave_UK_checks';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_slave_UK_checks | OFF   |
   +-----------------------+-------+


.. _`wsrep_sst_auth`:
.. rubric:: ``wsrep_sst_auth``
.. index::
   pair: Parameters; wsrep_sst_auth

Defines the authentication information to use in :term:`State Snapshot Transfer`.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sst-auth``"
   "System Variable", "``wsrep_sst_auth``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

When the node attempts a state snapshot transfer using the :term:`Logical State Transfer Method`, the transfer script uses a client connection to the database server in order to obtain the data it needs to send.  This parameter provides the authentication information, (that is, the username and password), that the script uses to access the database servers of both sending and receiving nodes.

.. note:: Galera Cluster only uses this parameter for State Snapshot Transfers that use the Logical transfer method.  Currently, the only method to use the Logical transfer method is ``mysqldump``.  For all other methods, the node doesn't need this parameter.

Format this value to the pattern: ``username:password``.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_auth'

   +----------------+---------------------------+
   | Variable_name  | Value                     |
   +----------------+---------------------------+
   | wsrep_sst_auth | wsrep_sst_user:mypassword |
   +----------------+---------------------------+


.. _`wsrep_sst_donor`:
.. rubric:: ``wsrep_sst_donor``
.. index::
   pair: Parameters; wsrep_sst_donor

Defines the name of the node that this node uses as a donor in state transfers.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sst-donor``"
   "System Variable", "``wsrep_sst_donor``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version 1.0"

When the node requires a state transfer from the cluster, it looks for the most appropriate one available.  The group communications module monitors the node state for the purposes of Flow Control, state transfers and quorum calculations.  The node can be a donor if it is in the ``SYNCED`` state.  The first node in the ``SYNCED`` state in the index becomes the donor and is made unavailable for requests while serving as such.

If there are no free ``SYNCED`` nodes at the moment, the joining node reports in the logs:

.. code-block:: text

   Requesting state transfer failed: -11(Resource temporarily unavailable).
    Will keep retrying every 1 second(s)

It continues retrying the state transfer request until it succeeds.  When the state transfer request does succeed, the node makes the following entry in the logs:

.. code-block:: text

   Node 0 (XXX) requested state transfer from '*any*'. Selected 1 (XXX) as donor.

Using this parameter, you can tell the node which cluster node or nodes it should use instead for state transfers.  The names used in this parameter must match the names given with :ref:`wsrep_node_name <wsrep_node_name>` on the donor nodes.  The setting affects both Incremental State Transfers (IST) and Snapshot State Transfers (SST).

If the list contains a trailing comma, the remaining nodes in the cluster will also be considered if the nodes from the list are not available.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_donor';

   +-----------------+--------------------------------+
   | Variable_name   | Value                          |
   +-----------------+--------------------------------+
   | wsrep_sst_donor | my_donor_node1,my_donor_node2, |
   +-----------------+--------------------------------+


.. _`wsrep_sst_donor_rejects_queries`:
.. rubric:: ``wsrep_sst_donor_rejects_queries``
.. index::
   pair: Parameters; wsrep_sst_donor_rejects_queries
.. index::
   pair: Errors; ER_UNKNOWN_COM_ERROR

Defines whether the node rejects blocking client sessions on a node when it is serving as a donor in a blocking state transfer method, such as ``mysqldump`` and ``rsync``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sst-donor-rejects-queries``"
   "System Variable", "``wsrep_sst_donor_rejects_queries``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "Version 1.0"

This parameter determines whether the node rejects blocking client sessions while it is sending state transfers using methods that block it as the donor.  In these situations, all queries return the error ``ER_UNKNOWN_COM_ERROR``, that is they respond with ``Unknown command``, just like the joining node does.

Given that a :term:`State Snapshot Transfer` is scriptable, there is no way to tell whether the requested method is blocking or not.  You may also want to avoid querying the donor even with non-blocking state transfers.  As a result, when this parameter is enabled the donor node rejects queries regardless the state transfer and even if the initial request concerned a blocking-only transfer, (meaning, it also rejects during ``xtrabackup``).

.. warning:: The ``mysqldump`` state transfer method does not work with the ``wsrep_sst_donor_rejects_queries`` parameter, given that ``mysqldump`` runs queries on the donor and there is no way to differentiate its session from the regular client session.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_donor_rejects_queries';

   +---------------------------------+-------+
   | Variable_name                   | Value |
   +---------------------------------+-------+
   | wsrep_sst_donor_rejects_queries | OFF   |
   +---------------------------------+-------+


.. _`wsrep_sst_method`:
.. rubric:: ``wsrep_sst_method``
.. index::
   pair: Parameters; wsrep_sst_method

Defines the method or script the node uses in a :term:`State Snapshot Transfer`.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sst-method``"
   "System Variable", "``wsrep_sst_method``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "``rsync``"
   "Initial Version", "Version 1.0"

When the node makes a state transfer request it calls on an external shell script to establish a connection a with the donor node and transfer the database state onto the local database server.  This parameter allows you to define what script the node uses in requesting state transfers.

Galera Cluster ships with a number of default scripts that the node can use in state snapshot transfers. The supported methods are:

- ``mysqldump`` This is slow, except for small data-sets, but is the most tested option.

- ``rsync`` This option is much faster than ``mysqldump`` on large data-sets.

  .. note:: You can only use ``rsync`` when anode is starting.  You cannot use it with a running InnoDB storage engine.

- ``rsync_wan`` This option is almost the same as ``rsync``, but uses the ``delta-xfer`` algorithm to minimize network traffic.

- ``xtrabackup`` This option is a fast and practically non-blocking state transfer method based on the Percona ``xtrabackup`` tool.  If you want to use it, the following settings must be present in the ``my.cnf`` configuration file on all nodes:

  .. code-block:: ini

     [mysqld]
     wsrep_sst_auth=YOUR_SST_USER:YOUR_SST_PASSWORD
     wsrep_sst_method=xtrabackup
     datadir=/path/to/datadir

     [client]
     socket=/path/to/socket

In addition to the default scripts provided and supported by Galera Cluster, you can also define your own custom state transfer script.  The naming convention that the node expects is for the value of this parameter to match ``wsrep_%.sh``.  For instance, giving the node a transfer method of ``MyCustomSST`` causes it to look for ``wsrep_MyCustomSST.sh`` in ``/usr/bin``.

Bear in mind, the cluster uses the same script to send and receive state transfers.  If you want to use a custom state transfer script, you need to place it on every node in the cluster.

For more information on scripting state snapshot transfers, see :doc:`scriptable-sst`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_method';

   +------------------+-----------+
   | Variable_name    | Value     |
   +------------------+-----------+
   | wsrep_sst_method | mysqldump |
   +------------------+-----------+


.. _`wsrep_sst_receive_address`:
.. rubric:: ``wsrep_sst_receive_address``
.. index::
   pair: Parameters; wsrep_sst_receive_address

Defines the address from which the node expects to receive state transfers.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sst-receive-address``"
   "System Variable", "``wsrep_sst_receive_address``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ":ref:`wsrep_node_address <wsrep_node_address>`"
   "Initial Version", "Version 1.0"

This parameter defines the address from which the node expects to receive state transfers.  It is dependent on the :term:`State Snapshot Transfer` method the node uses.

For example, ``mysqldump`` uses the address and port on which the node listens, which by default is set to the value of :ref:`wsrep_node_address <wsrep_node_address>`.

.. note:: Check that your firewall allows connections to this address from other cluster nodes.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_receive_address';

   +---------------------------+-------------+
   | Variable_name             | Value       |
   +---------------------------+-------------+
   | wsrep_sst_receive_address | 192.168.1.1 |
   +---------------------------+-------------+


.. _`wsrep_start_position`:
.. rubric:: ``wsrep_start_position``
.. index::
   pair: Parameters; wsrep_start_position

Defines the node start position.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-start-position``"
   "System Variable", "``wsrep_start_position``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", "``00000000-0000-0000-0000-00000000000000:-1``"
   "Initial Version", "Version 1.0"

This parameter defines the node start position.  It exists for the sole purpose of notifying the joining node of the completion of a state transfer.

For more information on scripting state snapshot transfers, see :doc:`scriptable-sst`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_start_position';

   +----------------------+-----------------------------------------+
   | Variable_name        | Value                                   |
   +----------------------+-----------------------------------------+
   | wsrep_start_position | 00000000-0000-0000-0000-000000000000:-1 |
   +----------------------+-----------------------------------------+


.. _`wsrep_sync_wait`:
.. rubric:: ``wsrep_sync_wait``
.. index::
  pair: Parameters; wsrep_sync_wait
.. index::
  pair: Parameters; wsrep_causal_reads

Defines whether the node enforces strict cluster-wide causality checks.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-sync-wait``"
   "System Variable", "``wsrep_sync_wait``"
   "Variable Scope", "Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Bitmask"
   "Default Value", "``0``"
   "Initial Version", "Version 3.6"

When you enable this parameter, the node triggers causality checks in response to certain types of queries.  During the check, the node blocks new queries while the database server catches up with all updates made in the cluster to the point where the check was begun.  Once it reaches this point, the node executes the original query.

.. note:: Causality checks of any type can result in increased latency.

This value of this parameter is a bitmask, which determines the type of check you want the node to run.

.. csv-table::
   :class: doc-options
   :header: "Bitmask", "Checks"

   "``0``", "Disabled."
   "``1``", "Checks on ``READ`` statements, including ``SELECT``, and ``BEGIN`` / ``START TRANSACTION``. Checks on ``SHOW`` (up to versions 5.5.54, 5.6.35, 5.7.17)"
   "``2``", "Checks made on ``UPDATE`` and ``DELETE`` statements."
   "``3``", "Checks made on ``READ``, ``UPDATE`` and ``DELETE`` statements."
   "``4``", "Checks made on ``INSERT`` and ``REPLACE`` statements."
   "``8``", "Checks made on ``SHOW`` statements."

For example, say that you have a web application.  At one point in its run, you need it to perform a critical read.  That is, you want the application to access the database server and run a ``SELECT`` query that must return the most up to date information possible.

.. code-block:: mysql

   SET SESSION wsrep_sync_wait=1;
   SELECT * FROM example WHERE field = "value";
   SET SESSION wsrep_sync_wait=0

In the example, the application first runs a ``SET`` command to enable :ref:`wsrep_sync_wait <wsrep_sync_wait>` for ``READ`` statements, then it makes a ``SELECT`` query.  Rather than running the query, the node initiates a causality check, blocking incoming queries while it catches up with the cluster.  When the node finishes applying the new transaction, it executes the ``SELECT`` query and returns the results to the application.  The application, having finished the critical read, disables :ref:`wsrep_sync_wait <wsrep_sync_wait>`, returning the node to normal operation.

.. note:: Setting :ref:`wsrep_sync_wait <wsrep_sync_wait>` to ``1`` is the same as :ref:`wsrep_causal_reads <wsrep_causal_reads>` to ``ON``.  This deprecates :ref:`wsrep_causal_reads <wsrep_causal_reads>`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sync_wait';

   +-----------------+-------+
   | Variable_name   | Value |
   +-----------------+-------+
   | wsrep_sync_wait | 0     |
   +-----------------+-------+


.. _`wsrep_trx_fragment_size`:
.. rubric:: ``wsrep_trx_fragment_size``
.. index::
   pair: Parameters; wsrep_trx_fragment_size
.. index::
   pair: Galera Cluster 4.x; Streaming Replication
.. index::
   pair: wsrep_trx_fragment_size; Streaming Replication

Defines the number of replication units needed to generate a new fragment in Streaming Replication.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-trx-fragment-size``"
   "System Variable", "``wsrep_trx_fragment_size``"
   "Variable Scope", "Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Integer"
   "Default Value", "``0``"
   "Initial Version", "Version 4.0"

In :term:`Streaming Replication`, the node breaks transactions down into fragments, then replicates and certifies them while the transaction is in progress.  Once certified, a fragment can no longer be aborted due to conflicting transactions.  This parameter determines the number of replication units to include in a fragment.  To define what these units represent, use :ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>`. A value of ``0`` indicates that streaming replication will not be used.

.. code-block:: mysql

   SHOW VARIABLE LIKE 'wsrep_trx_fragment_size';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_trx_fragment_size | 5     |
   +-------------------------+-------+


.. _`wsrep_trx_fragment_unit`:
.. rubric:: ``wsrep_trx_fragment_unit``
.. index::
   pair: Parameters; wsrep_trx_fragment_unit
.. index::
   pair: Galera Cluster 4.x; Streaming Replication
.. index::
   pair: wsrep_trx_fragment_unit; Streaming Replication

Defines the replication unit type to use in Streaming Replication.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-trx-fragment-unit``"
   "System Variable", "``wsrep_trx_fragment_unit``"
   "Variable Scope", "Session"
   "Dynamic Variable", "Yes"
   "Permitted Values", "String"
   "Default Value", "``bytes``"
   "Valid Values", "``bytes``, ``events``, ``rows``, ``statements``"
   "Initial Version", "Version 4.0"

In :term:`Streaming Replication`, the node breaks transactions down into fragments, then replicates and certifies them while the transaction is in progress.  Once certified, a fragment can no longer be aborted due to conflicting transactions.  This parameter determines the unit to use in determining the size of the fragment.  To define the number of replication units to use in the fragment, use :ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`.

Supported replication units are:

- **bytes**: Refers to the fragment size in bytes.

- **events**: Refers to the number of binary log events in the fragment.

- **rows**: Refers to the number of rows updated in the fragment.

- **statements**: Refers to the number of SQL statements in the fragment.

.. code-block:: mysql

   SHOW VARIABLE LIKE 'wsrep_trx_fragment_unit';

   +-------------------------+--------+
   | Variable_name           | Value  |
   +-------------------------+--------+
   | wsrep_trx_fragment_unit | bytes  |
   +-------------------------+--------+


.. _`wsrep_ws_persistency`:
.. rubric:: ``wsrep_ws_persistency``
.. index::
   pair: Parameters; wsrep_ws_persistency

Defines whether the node stores write-sets locally for debugging.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-ws-persistency``"
   "System Variable", "``wsrep_ws_persistency``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "Version ???, Deprecated in Version 0.8"

This parameter defines whether the node stores write-sets locally for debugging purposes.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_ws_persistency';

   +----------------------+-------+
   | Variable_name        | Value |
   +----------------------+-------+
   | wsrep_ws_persistency | ON    |
   +----------------------+-------+


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

   <br />
