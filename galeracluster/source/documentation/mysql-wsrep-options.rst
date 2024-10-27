.. meta::
   :title: MySQL wsrep Options
   :description:
   :language: en-US
   :keywords: galera cluster, mysql wsrep options, galera options
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

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`mysql-wsrep-options`:

======================
MySQL wsrep Options
======================
.. index::
   single: Drupal
.. index::
   pair: Logs; Debug log


These are MySQL system variables starting from wsrep API patch version 21.1
for MySQL 5.1.58. Although there were earlier versions of MySQL-wsrep, this
was the first one to use consistent versioning scheme as was chosen as
the starting point.

Almost all of the variables are global except for a few.
Those are session variables. If you click on a particular variable in this
table, your web browser will scroll down to the entry for it with more details
and an explanation.


.. csv-table::
   :class: doc-options tight-header
   :header: "|br| Option", "|br| Default Value", "|br| Global ", "|br| Dynamic"
   :widths: 30, 30, 12, 12
   ":ref:`innodb-wsrep-applier-lock-wait-timeout <innodb-wsrep-applier-lock-wait-timeout>`", "``0``", "Yes", "Yes"
   ":ref:`wsrep_applier_FK_failure_retries <wsrep_applier_FK_failure_retries>`", "``1``", "Yes", "Yes"
   ":ref:`wsrep_auto_increment_control <wsrep_auto_increment_control>`", "``ON``", "Yes", ""
   ":ref:`wsrep_causal_reads <wsrep_causal_reads>`", "``OFF``", "", ""
   ":ref:`wsrep_certify_nonPK <wsrep_certify_nonPK>`", "``ON``", "", "Yes"
   ":ref:`wsrep_certification_rules <wsrep_certification_rules>`", "", "", "Yes"
   ":ref:`wsrep_cluster_address <wsrep_cluster_address>`", "``ON``", "Yes", ""
   ":ref:`wsrep_cluster_name <wsrep_cluster_name>`", "``example_cluster``", "Yes", ""
   ":ref:`wsrep_convert_LOCK_to_trx <wsrep_convert_LOCK_to_trx>`", "``OFF``", "Yes", ""
   ":ref:`wsrep_data_home_dir <wsrep_data_home_dir>`", "``/path/to/datadir``", "Yes", ""
   ":ref:`wsrep_dbug_option <wsrep_dbug_option>`", "", "Yes", ""
   ":ref:`wsrep_debug <wsrep_debug>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_desync <wsrep_desync>`", "``OFF``", "Yes", ""
   ":ref:`wsrep_dirty_reads <wsrep_dirty_reads>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_drupal_282555_workaround <wsrep_drupal_282555_workaround>`", "``ON``", "Yes", ""
   ":ref:`wsrep_forced_binlog_format <wsrep_forced_binlog_format>`", "``NONE``", "Yes", ""
   ":ref:`wsrep_ignore_apply_errors <wsrep_ignore_apply_errors>`", "``7``", "Yes", "Yes"
   ":ref:`wsrep_info_level <wsrep_info_level>`", "``0``", "Yes", "Yes"
   ":ref:`wsrep_load_data_splitting <wsrep_load_data_splitting>`", "``ON``", "Yes", ""
   ":ref:`wsrep_log_conflicts <wsrep_log_conflicts>`", "``OFF``", "Yes", ""
   ":ref:`wsrep_max_ws_rows <wsrep_max_ws_rows>`", "``0``", "Yes", ""
   ":ref:`wsrep_max_ws_size <wsrep_max_ws_size>`", "``1G``", "Yes", ""
   ":ref:`wsrep_mode <wsrep_mode>`", "``ON``", "Yes", ""
   ":ref:`wsrep_node_address <wsrep_node_address>`", "*host address:default port*", "Yes", ""
   ":ref:`wsrep_node_incoming_address <wsrep_node_incoming_address>`", "*host address:mysqld port*", "Yes", ""
   ":ref:`wsrep_node_name <wsrep_node_name>`", "``<hostname>``", "Yes", ""
   ":ref:`wsrep_notify_cmd <wsrep_notify_cmd>`", "", "Yes", ""
   ":ref:`wsrep_on <wsrep_on>`", "``ON``", "Yes", ""
   ":ref:`wsrep_OSU_method <wsrep_OSU_method>`", "``TOI``", "", "Yes"
   ":ref:`wsrep_preordered <wsrep_preordered>`", "``OFF``", "Yes", ""
   ":ref:`wsrep_provider <wsrep_provider>`", "``NONE``", "Yes", ""
   ":ref:`wsrep_provider_options <wsrep_provider_options>`", "", "Yes", ""
   ":ref:`wsrep_recover <wsrep_recover>`", "``OFF``", "Yes", "No"
   ":ref:`wsrep_reject_queries <wsrep_reject_queries>`", "``NONE``", "Yes", "Yes"
   ":ref:`wsrep_restart_replica <wsrep_restart_replica>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_restart_slave <wsrep_restart_slave>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_retry_autocommit <wsrep_retry_autocommit>`", "``1``", "Yes", ""
   ":ref:`wsrep_applier_FK_checks <wsrep_applier_FK_checks>`", "``ON``", "Yes", "Yes"
   ":ref:`wsrep_slave_FK_checks <wsrep_slave_FK_checks>`", "``ON``", "Yes", "Yes"
   ":ref:`wsrep_applier_threads <wsrep_applier_threads>`", "``1``", "Yes", ""
   ":ref:`wsrep_slave_threads <wsrep_slave_threads>`", "``1``", "Yes", ""
   ":ref:`wsrep_applier_UK_checks <wsrep_applier_UK_checks>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_slave_UK_checks <wsrep_slave_UK_checks>`", "``OFF``", "Yes", "Yes"
   ":ref:`wsrep_sst_auth <wsrep_sst_auth>`", "", "Yes", ""
   ":ref:`wsrep_sst_donor <wsrep_sst_donor>`", "", "Yes", ""
   ":ref:`wsrep_sst_donor_rejects_queries <wsrep_sst_donor_rejects_queries>`", "``OFF``", "Yes", ""
   ":ref:`wsrep_sst_method <wsrep_sst_method>`", "``mysqldump``", "Yes", ""
   ":ref:`wsrep_sst_receive_address <wsrep_sst_receive_address>`", "*node IP address*", "Yes", ""
   ":ref:`wsrep_start_position <wsrep_start_position>`", "*see reference entry*", "Yes", ""
   ":ref:`wsrep_status_file <wsrep_status_file>`", "", "Yes", "No"
   ":ref:`wsrep_sync_server_uuid <wsrep_sync_server_uuid>`", "``0``", "Yes", "Yes"
   ":ref:`wsrep_sync_wait <wsrep_sync_wait>`", "``0``", "Yes", "Yes"
   ":ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`", "``0``", "Yes", "Yes"
   ":ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>`", "``bytes``", "Yes", "Yes"


You can execute the ``SHOW VARIABLES`` statement with the ``LIKE`` operator as shown below to get list of all Galera related variables on your server:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep%';

The results will vary depending on which version of Galera is running on your server. All of the parameters and variables possible are listed above, but they're listed below with explanations of each.


  .. only:: html

           .. image:: ../images/support.jpg
              :target: https://galeracluster.com/support/#galera-cluster-support-subscription
              :width: 740

  .. only:: latex
 
           .. image:: ../images/support.jpg
              :target: https://galeracluster.com/support/#galera-cluster-support-subscription


.. _`innodb-wsrep-applier-lock-wait-timeout`:
.. rst-class:: section-heading
.. rubric:: ``innodb-wsrep-applier-lock-wait-timeout``

.. index::
   pair: Parameters; innodb-wsrep-applier-lock-wait-timeout

The ``innodb-wsrep-applier-lock-wait-timeout`` parameter defines the timeout in seconds, after which the ``wsrepw`` watchdog starts killing local transactions that are blocking the applier. Value ``0`` disables the watchdog.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--innodb-wsrep-applier-lock-wait-timeout``"
   "System Variable", "``innodb-wsrep-applier-lock-wait-timeout``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "0 or timeout in seconds"
   "Default Value", "``0`` "
   "Initial Version", "MySQL-wsrep 8.0.26-26.8"

You can execute the following ``SHOW VARIABLES`` statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'innodb-wsrep-applier-lock-wait-timeout';

    +----------------------------------------+-------+
    | Variable_name                          | Value |
    +----------------------------------------+-------+
    | innodb-wsrep-applier-lock-wait-timeout | 10    |
    +----------------------------------------+-------+

.. _`wsrep_applier_FK_failure_retries`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_applier_FK_failure_retries``

.. index::
   pair: Parameters; wsrep_applier_FK_failure_retries

Occasionally, foreign key constrains may fail even though the constraints themselves are not violated (for example, if the same transaction inserts in the parent table, and the next insert into the child table fails in FK checks). With this foreign key constraint check retrying implementation, you can control the number of retries. If the constraint check fails despite retires, the final retry prints out a warning with an error code and InnoDB system monitor output for further troubleshooting.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_applier_FK_failure_retries``"
   "System Variable", "``wsrep_applier_FK_failure_retries``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Integer"
   "Default Value", "``1`` "
   "Initial Version", "MySQL-wsrep 8.0.35"

You can execute the following ``SHOW VARIABLES`` statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_applier_FK_failure_retries';

    +----------------------------------------+-------+
    | Variable_name                          | Value |
    +----------------------------------------+-------+
    | wsrep_applier_FK_failure_retries       | 1     |
    +----------------------------------------+-------+



.. _`wsrep_auto_increment_control`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

The node manages auto-increment values in a table using two variables: ``auto_increment_increment`` and ``auto_increment_offset``.  The first relates to the value auto-increment rows count from the offset. The second relates to the offset it should use in moving to the next position.

The :ref:`wsrep_auto_increment_control <wsrep_auto_increment_control>` parameter enables additional calculations to this process, using the number of nodes connected to the :term:`Primary Component` to adjust the increment and offset.  This is done to reduce the likelihood that two nodes will attempt to write the same auto-increment value to a table.

It significantly reduces the rate of certification conflicts for ``INSERT`` statements. You can execute the following ``SHOW VARIABLES`` statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_auto_increment_control';

    +------------------------------+-------+
    | Variable_name                | Value |
    +------------------------------+-------+
    | wsrep_auto_increment_control | ON    |
    +------------------------------+-------+


.. _`wsrep_causal_reads`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"
   "Deprecated Version", "MySQL-wsrep: 5.5.42-25.12"

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_causal_reads';

.. warning:: The ``wsrep_causal_reads`` option has been **deprecated**.  It has been replaced by :ref:`wsrep_sync_wait <wsrep_sync_wait>`.


.. _`wsrep_certification_rules`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.61-25.24, 5.6.41-25.23, 5.7.23-25.15"
   "Deprecated Version", "MySQL-wsrep: 8.0.19-26.3"

Controls how certification is done in the cluster. To be more specific, this parameter affects how foreign keys are handled: with the ``STRICT`` option, two INSERTs that happen at about the same time on two different nodes in a child table, and insert different (non conflicting) rows, but both rows point to the same row in the parent table, could result in certification failure. With the ``OPTIMIZED`` option, such certification failure is avoided.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_certification_rules';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_certification_rules | STRICT |
   +---------------------------+--------+



.. _`wsrep_certify_nonPK`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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

.. warning:: Never use an empty ``gcomm://`` string with the ``wsrep_cluster_address`` option in the configuration file. If a node restarts, it will cause the node not to rejoin the cluster. Instead, it will initialize a new one-node cluster and cause a :term:`Split Brain`. To bootstrap a cluster, you should only pass the ``--wsrep-new-cluster`` string at the command-line--instead of using ``--wsrep-cluster-address="gcomm://"``. For more information, see :doc:`Starting the Cluster <../training/tutorials/starting-cluster>`.

You can execute the following SQL statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_cluster_address';

   +-----------------------+---------------------------------------------+
   | Variable_name         | Value                                       |
   +-----------------------+---------------------------------------------+
   | wsrep_cluster_address | gcomm://192.168.1.1,192.168.1.2,192.168.1.3 |
   +-----------------------+---------------------------------------------+


.. _`wsrep_cluster_name`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"
   "Deprecated Version", "MySQL-wsrep: 8.0.19-26.3"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.15-21.1, MariaDB: 5.5.21"

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set, if it is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_dbug_option';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_dbug_option |       |
   +-------------------+-------+


.. _`wsrep_debug`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_debug``

.. index::
   pair: Parameters; wsrep_debug

This parameter enables additional debugging output for the database server error log.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-debug``"
   "System Variable", "``wsrep_debug``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

Under normal operation, error events are logged to an error log file for the database server.  By default, the name of this file is the server hostname with the ``.err`` extension.  You can define a custom path using the `log_error <https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_log_error>`_ parameter. When you enable :ref:`wsrep_debug <wsrep_debug>`, the database server logs additional events surrounding these errors to help in identifying and correcting problems. 

DDL statements are also logged. See below for an example:

.. code-block:: console

   2024-09-06 14:37:57 13 [Note] WSREP: TOI Begin: CREATE SEQUENCE seq start with 1 minvalue 1 maxvalue 1000000 increment by 0 cache 1000 nocycle ENGINE=InnoDB
   2024-09-06 14:37:57 13 [Note] WSREP: enter_toi_local: enter(13,exec,local,success,0,toi: -1,nbo: -1)
   2024-09-06 14:37:57 13 [Note] WSREP: poll_enter_toi: 3,0
   2024-09-06 14:37:57 13 [Note] WSREP: enter_toi_local: leave(13,exec,toi,success,0,toi: 3,nbo: -1)
   2024-09-06 14:37:57 13 [Note] WSREP: avoiding binlog rotate due to TO isolation: 1
   2024-09-06 14:37:57 13 [Note] WSREP: TO END: 3: CREATE SEQUENCE seq start with 1 minvalue 1 maxvalue 1000000 increment by 0 cache 1000 nocycle ENGINE=InnoDB

.. warning:: In addition to useful debugging information, the ``wsrep_debug`` parameter also causes the database server to print authentication information (that is, passwords) to the error logs. Do not enable it in production environments. This, however, does not concern MariaDB, as the "wsrep_thd_query()", where the user query is exposed, does not print all information when the "SQL_COMMAND" is "SET" (such as "SET PASSWORD") or "SQLCOM_CREATE_USER", where "CREATE USER" is only logged.

See below for an example of ``wsrep_debug`` output:

.. code-block:: console

   2024-09-06 14:26:19 2 [Note] WSREP: open: enter(4,none,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: open: leave(4,idle,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: before_command: enter(4,idle,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 4 [Note] WSREP: before_command: success(4,exec,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 4 [Note] WSREP: Cluster table is empty, not recovering transactions
   2024-09-06 14:26:19 2 [Note] WSREP: after_command_before_result: enter(4,exec,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: after_command_before_result: leave(4,result,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: after_command_after_result_enter(4,result,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: after_command_after_result: leave(4,idle,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: close: enter(4,idle,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 2 [Note] WSREP: close: leave(4,quit,high priority,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 4 [Note] WSREP: cleanup: enter(4,quit,local,success,0,toi: -1,nbo: -1)
   2024-09-06 14:26:19 4 [Note] WSREP: cleanup: leave(4,none,local,success,0,toi: -1,nbo: -1)

The ``wsrep_debug`` options are:

- ``SERVER`` - ``WSREP_DEBUG`` log writes from the source code will be added to the error log.

- ``TRANSACTION`` - Logging from ``wsrep-lib`` transactions will be added to the error log.

- ``STREAMING`` - Logging from streaming transactions in ``wsrep-lib`` will be added to the error log.

- ``CLIENT`` - Logging from ``wsrep-lib`` client state will be added to the error log.

See also :ref:`evs.debug_log_mask <evs.debug_log_mask>`.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see if this variable is enabled:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_debug';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_debug   | OFF   |
   +---------------+-------+


.. _`wsrep_desync`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.33-23.7.6, MariaDB: 5.5.33"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.6.29-25.14, MariaDB: 10.1.3"


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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

Drupal installations using MySQL are subject to a bug in InnoDB, tracked as `MySQL Bug 41984 <https://bugs.mysql.com/bug.php?id=41984>`_ and `Drupal Issue 282555 <https://drupal.org/node/282555>`_.  Specifically, inserting a `DEFAULT` value into an `AUTO_INCREMENT` column may return duplicate key errors.

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.17-22.3, MariaDB: 5.5.21"

The node uses the format given by this parameter regardless of the client session variable `binlog_format <https://dev.mysql.com/doc/refman/8.4/en/binary-log-setting.html>`_.  Valid choices for this parameter are: ``ROW``, ``STATEMENT``, and ``MIXED``.  Additionally, there is the special value ``NONE``, which means that there is no forced format in effect for the binary logs. When set to a value other than ``NONE``, this parameter forces all transactions to use a given binary log format.

This variable was introduced to support ``STATEMENT`` format replication during :term:`Rolling Schema Upgrade`.  In most cases, however, ``ROW`` format replication is valid for asymmetric schema replication.

If you turn on ``wsrep_forced_binlog_format``, it is effective only for DML operations, to avoid any possible binlog corruption. In addition, since MySQL-wsrep 8.0.37-26.19, it is also deprecated, as ``binlog_format`` has been deprecated upstream since MySQL 8.0.34. As the only possible logging format is ROW, it makes this option redundant.

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_forced_binlog_format';

   +----------------------------+-------+
   | Variable_name              | Value |
   +----------------------------+-------+
   | wsrep_forced_binlog_format | NONE  |
   +----------------------------+-------+


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

For example, if you want to ignore some DDL errors (option 1) and skip DML errors (option 2), you would calculate 1+2=3, and use ``--wsrep-wsrep_ignore_apply_errors=3``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-wsrep_ignore_apply_errors``"
   "System Variable", "``wsrep_ignore_apply_errors``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Data Type", "Numeric"
   "Default Value", "``7`` "
   "Range", "``0`` to ``7``"
   "Initial Version", "Version 1.0"

You can execute the following ``SHOW VARIABLES`` statement with a ``LIKE`` operator to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep-wsrep_ignore_apply_errors';

   +---------------------------------+-------+
   | Variable_name                   | Value |
   +---------------------------------+-------+
   | wsrep-wsrep_ignore_apply_errors |  7    |
   +---------------------------------+-------+




.. _`wsrep_info_level`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_info_level``

.. index::
   pair: Parameters; wsrep_info_level

This parameter defines how to log ``INFO``-level wsrep messages.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_info_level``"
   "System Variable", "``wsrep_info_level``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Numeric"
   "Default Value", "``0``"
   "Initial Version", "MySQL-wsrep: 8.0.34"

``INFO``-level wsrep messages are logged with ``SYSTEM_LEVEL`` priority by default, as WSREP information level messages are crucial for troubleshooting replication issues. However, if you need to use ``INFORMATION_LEVEL`` logging, you can use this variable to change the logging priority.

The options are:

- ``0`` Use ``SYSTEM_LEVEL`` logging.

- ``3`` Use ``INFORMATION_LEVEL`` logging.

You can execute the following ``SHOW VARIABLES`` statement to see how this variable is set:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_info_level';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_info_level | 0     |
   +------------------+-------+







.. _`wsrep_load_data_splitting`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.34-25.29, MariaDB: 5.5.32"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.28-23.7, MariaDB: 5.5.27"


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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

This parameter sets the maximum size that the node allows for a write-set.  Currently, this value limits the supported size of transactions and of ``LOAD DATA`` statements.

The maximum allowed write-set size is ``2G``.  You can execute the following ``SHOW VARIABLES`` statement to see the current value of this parameter:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_max_ws_size';

   +-------------------+-------+
   | Variable_name     | Value |
   +-------------------+-------+
   | wsrep_max_ws_size | 2G    |
   +-------------------+-------+


.. _`wsrep_mode`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_mode``

.. index::
   pair: Parameters; wsrep_mode

Extends node behaviour with provided values.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_mode``"
   "System Variable", "``wsrep_mode``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Set"
   "Default Value", "APPLIER_IGNORE_MISSING_TABLE"
   "Initial Version", "MySQL-wsrep: 5.7.32-25.24, 8.0.22-26.5, MariaDB: 10.6.0"

.. csv-table::
   :class: doc-options
   :header: "Value", "Behaviour"
   :widths: 25, 50

   "``IGNORE_NATIVE_REPLICATION_FILTER_RULES``", "Ignore replication filter rules for cluster events."
   "``IGNORE_CASCADING_FK_DELETE_MISSING_ROW_ERROR``", "Ignore missing row errors when applying a cascading delete write set. This a workaround for https://bugs.mysql.com/bug.php?id=80821."
   "``APPLIER_IGNORE_MISSING_TABLE``", "MySQL has an anomaly to sometimes add an excessive tablemap event in the binlog. This can happen in use cases related to multi-table updates and trigger definitions to a third table, which is not effectively needed in applying of the replication events. With wsrep_mode "APPLIER_IGNORE_MISSING_TABLE", the replication applier will ignore the failure to open such a table, which would not be used in the actual applying."

.. code-block:: mysql

   SET GLOBAL wsrep_mode = IGNORE_NATIVE_REPLICATION_FILTER_RULES;

   SHOW VARIABLES LIKE 'wsrep_mode';

   +---------------+----------------------------------------+
   | Variable_name | Value                                  |
   +---------------+----------------------------------------+
   | wsrep_mode    | IGNORE_NATIVE_REPLICATION_FILTER_RULES |
   +---------------+----------------------------------------+


.. _`wsrep_node_address`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.20-23.4, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

This parameter defines whether or not updates made in the current session replicate to the cluster.  It does not cause the node to leave the cluster and the node continues to communicate with other nodes.  Additionally, it is a session variable.  Defining it through the ``SET GLOBAL`` syntax also affects future sessions.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_on';

   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | wsrep_on      | ON    |
   +---------------+-------+


.. _`wsrep_OSU_method`:
.. rst-class:: section-heading
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
   "Valid Values", "``TOI``, ``RSU``, ``NBO``"
   "Initial Version", "MySQL-wsrep: 5.5.17-22.3, MariaDB: 5.5.21"
   "Initial Version, NBO", "MariaDB Enterprise Server Version 10.5, MySQL-wsrep 8.0.28-26.10 Enterprise Edition, Percona XtraDB Cluster 8.0.25-15.1"

DDL statements are non-transactional and as such don't replicate through write-sets.  There are two methods available that determine how the node handles replicating these statements:

- ``TOI``  In the :term:`Total Order Isolation` method, the cluster runs the DDL statement on all nodes in the same total order sequence, blocking other transactions from committing while the DDL is in progress.

- ``RSU`` In the :term:`Rolling Schema Upgrade` method, the node runs the DDL statements locally, thus blocking only the one node where the statement was made.  While processing the DDL statement, the node is not replicating and may be unable to process replication events due to a table lock.  Once the DDL operation is complete, the node catches up and syncs with the cluster to become fully operational again.  The DDL statement or its effects are not replicated; the user is responsible for manually executing this statement on each node in the cluster.

- ``NBO`` In the :term:`Non-Blocking Operations` method, the cluster runs the DDL statement on all nodes in the same total order sequence, blocking other transactions from committing while the DDL is in progress. In comparison with TOI, the NBO method has more efficient locking for several operations, as the NBO method issues metadata locks on all nodes at the start of the DDL operation, to ensure consistency. This prevents the TOI issue of long-running DDL statements, which block cluster updates.

For more information on DDL statements and OSU methods, see :doc:`schema-upgrades`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_OSU_method';

   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | wsrep_OSU_method | TOI   |
   +------------------+-------+


.. _`wsrep_preordered`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.6.21-25.9"
   "Deprecated Version", "MySQL-wsrep: 8.0.19-26.3, MariaDB: 10.1.1"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

When the node starts, it needs to load the wsrep Provider in order to enable replication functions.  The path defined in this parameter tells it what file it needs to load and where to find it.  In the event that you do not define this path or you give it an invalid value, the node bypasses all calls to the wsrep Provider and behaves as a standard standalone instance of MySQL.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_provider';

   +----------------+----------------------------------+
   | Variable_name  | Value                            |
   +----------------+----------------------------------+
   | wsrep_provider | /usr/lib/galera/libgalera_smm.so |
   +----------------+----------------------------------+


.. _`wsrep_provider_options`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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


.. _`wsrep_recover`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_recover``

If ``ON``, when the server starts, the server will recover the sequence number of the most recent write set applied by Galera, and it will be output to ``stderr``, which is usually redirected to the error log. At that point, the server will exit. This sequence number can be provided to the ``wsrep_start_position`` system variable.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-recover``"
   "System Variable", "``wsrep_recover``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Permitted Values", "0 | 1"
   "Default Value", "OFF"
   "Initial Version", "MySQL-wsrep: 5.5.23-23.5, MariaDB: 5.5.21"

See also :doc:`Restarting the Cluster <../training/tutorials/restarting-cluster>` and :ref:`wsrep_recover Script <wsrep_recover_script>`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_recover';

   +------------------------+-----------------------------------------------+
   | Variable_name          | Value                                         |
   +------------------------+-----------------------------------------------+
   | wsrep_recover          | OFF                                           |
   +------------------------+-----------------------------------------------+


.. _`wsrep_reject_queries`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_reject_queries``

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
   "Initial Version", "MySQL-wsrep: 5.6.29-25.14, MariaDB: 10.1.32"

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


.. _`wsrep_restart_replica`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_restart_replica``

.. index::
   pair: Parameters; wsrep_restart_replica

Defines whether the replica restarts when the node joins the cluster.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-restart-replica``"
   "System Variable", "``wsrep_restart_replica``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "MySQL-wsrep: 8.0.26-26.8"

Enabling this parameter tells the node to restart the replica when it joins the cluster.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_restart_replica';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_restart_replica | OFF   |
   +-----------------------+-------+

.. _`wsrep_restart_slave`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_restart_slave``

.. index::
   pair: Parameters; wsrep_restart_slave

Deprecated as of Galera Cluster 4.10/MySQL-wsrep 8.0.26-26.8 in favor of :ref:`wsrep_restart_replica <wsrep_restart_replica>`.


.. _`wsrep_retry_autocommit`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

When an autocommit query fails the certification test due to a cluster-wide conflict, the node can retry it without returning an error to the client.  This parameter defines how many times the node retries the query.  It is analogous to rescheduling an autocommit query should it go into deadlock with other transactions in the database lock manager.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_retry_autocommit';

   +------------------------+-------+
   | Variable_name          | Value |
   +------------------------+-------+
   | wsrep_retry_autocommit | 1     |
   +------------------------+-------+


.. _`wsrep_applier_FK_checks`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_applier_FK_checks``

.. index::
   pair: Parameters; wsrep_applier_FK_checks

Defines whether the node performs foreign key checking for applier threads.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-applier-FK-checks``"
   "System Variable", "``wsrep_applier_FK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "MySQL-wsrep: 8.0.26-26.8"

This parameter enables foreign key checking on applier threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_applier_FK_checks';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_applier_FK_checks | ON    |
   +-------------------------+-------+


.. _`wsrep_slave_FK_checks`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_slave_FK_checks``

.. index::
   pair: Parameters; wsrep_slave_FK_checks

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-FK-checks``"
   "System Variable", "``wsrep_slave_FK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``ON``"
   "Initial Version", "MySQL-wsrep: 5.5.42-25.11, MariaDB: 10.0.12"
   "Deprecated Version", "MySQL-wsrep: 8.0.26-26.8"

Deprecated as of Galera Cluster 4.10/MySQL-wsrep 8.0.26-26.8 in favor of :ref:`wsrep_applier_FK_checks <wsrep_applier_FK_checks>`.

.. _`wsrep_applier_threads`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_applier_threads``

.. index::
   pair: Parameters; wsrep_applier_threads

Defines the number of threads to use in applying of write-sets.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-applier-threads``"
   "System Variable", "``wsrep_applier_threads``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Integer"
   "Default Value", "``1``"
   "Initial Version", "MySQL-wsrep: 8.0.26-26.8"

This parameter allows you to define how many threads the node uses when applying write-sets.  Performance on the underlying system and hardware, the size of the database, the number of client connections, and the load your application puts on the server all factor in the need for threading, but not in a way that makes the scale of that need easy to predict.  Because of this, there is no strict formula to determine how many applier threads your node actually needs.

Instead of concrete recommendations, there are some general guidelines that you can use as a starting point in finding the value that works best for your system:

- It is rarely beneficial to use a value that is less than twice the number of CPU cores on your system.

- Similarly, it is rarely beneficial to use a value that is more than one quarter the total number of client connections to the node.  While it is difficult to predict the number of client connections, being off by as much as 50% over or under is unlikely to make a difference.

- From the perspective of resource utilization, it's recommended that you keep to the lower end of applier threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_applier_threads';

   +-----------------------+-------+
   | Variable_name         | Value |
   +-----------------------+-------+
   | wsrep_applier_threads | 1     |
   +-----------------------+-------+

.. _`wsrep_slave_threads`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_slave_threads``

.. index::
   pair: Parameters; wsrep_slave_threads

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-threads``"
   "System Variable", "``wsrep_slave_threads``"
   "Variable Scope", "Global"
   "Dynamic Variable", ""
   "Permitted Values", "Integer"
   "Default Value", "``1``"
   "Initial Version", "MySQL-wsrep: 5.1.58-25.11, MariaDB: 5.5.21"
   "Deprecated Version", "MySQL-wsrep: 8.0.26-26.8"

Deprecated as of MySQL-wsrep 8.0.26-26.8 in favor of :ref:`wsrep_applier_threads <wsrep_applier_threads>`. See also :doc:`Setting Parallel Slave Threads <../kb/parallel-applier-threads>`.

.. _`wsrep_applier_UK_checks`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_applier_UK_checks``

.. index::
   pairs: Parameters; wsrep_applier_UK_checks

Defines whether the node performs unique key checking on applier threads.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-applier-UK-checks``"
   "System Variable", "``wsrep_applier_UK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "MySQL-wsrep: 8.0.26-26.8"

This parameter enables unique key checking on applier threads.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_applier_UK_checks';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_applier_UK_checks | OFF   |
   +-------------------------+-------+

.. _`wsrep_slave_UK_checks`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_slave_UK_checks``

.. index::
   pairs: Parameters; wsrep_slave_UK_checks

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-slave-UK-checks``"
   "System Variable", "``wsrep_slave_UK_checks``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "Boolean"
   "Default Value", "``OFF``"
   "Initial Version", "MySQL-wsrep: 5.5.42-25.11, MariaDB: 5.5.21"
   "Deprecated Version", "MySQL-wsrep: 8.0.26-26.8"

Deprecated as of MySQL-wsrep 8.0.26-26.8 in favor of :ref:`wsrep_applier_UK_checks <wsrep_applier_UK_checks>`.


.. _`wsrep_sst_auth`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

When the node requires a state transfer from the cluster, it looks for the most appropriate one available.  The group communications module monitors the node state for the purposes of Flow Control, state transfers and :term:`Quorum` calculations.  The node can be a donor if it is in the ``SYNCED`` state.  The first node in the ``SYNCED`` state in the index becomes the donor and is made unavailable for requests while serving as such.

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.28-23.7, MariaDB: 5.5.28"

This parameter determines whether the node rejects blocking client sessions while it is sending state transfers using methods that block it as the donor.  In these situations, all queries return the error ``ER_UNKNOWN_COM_ERROR``, that is they respond with ``Unknown command``, just like the joining node does.

Given that a :term:`State Snapshot Transfer` is scriptable, there is no way to tell whether the requested method is blocking or not.  You may also want to avoid querying the donor even with non-blocking state transfers.  As a result, when this parameter is enabled the :term:`Donor Node` rejects queries regardless the state transfer and even if the initial request concerned a blocking-only transfer, (meaning, it also rejects during ``xtrabackup``).

.. warning:: The ``mysqldump`` state transfer method does not work with the ``wsrep_sst_donor_rejects_queries`` parameter, given that ``mysqldump`` runs queries on the donor and there is no way to differentiate its session from the regular client session.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_donor_rejects_queries';

   +---------------------------------+-------+
   | Variable_name                   | Value |
   +---------------------------------+-------+
   | wsrep_sst_donor_rejects_queries | OFF   |
   +---------------------------------+-------+


.. _`wsrep_sst_method`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

When the node makes a state transfer request it calls on an external shell script to establish a connection a with the donor node and transfer the database state onto the local database server.  This parameter allows you to define what script the node uses in requesting state transfers.

Galera Cluster ships with a number of default scripts that the node can use in state snapshot transfers. The supported methods are:

- ``mysqldump`` This is slow, except for small data-sets, but is the most tested option.

- ``rsync`` This option is much faster than ``mysqldump`` on large data-sets.

  .. note:: You can only use ``rsync`` when anode is starting.  You cannot use it with a running InnoDB storage engine.

- ``rsync_wan`` This option is almost the same as ``rsync``, but uses the ``delta-xfer`` algorithm to minimize network traffic.

- ``mariabackup`` This option uses the Mariabackup utility for performing SSTs. See :doc:`mariabackup-options`.

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

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
.. rst-class:: section-heading
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
   "Default Value", "``00000000-0000-0000-0000-000000000000:-1/0/0/00000000-0000-0000-0000-000000000000``"
   "Initial Version", "MySQL-wsrep: 5.1.58-21.1, MariaDB: 5.5.21"

This parameter defines the node start position. It contains the wsrep GTID position, local seqno for asynchronous replication, server ID and server UUID all in one, slash-separated argument. It exists for the sole purpose of notifying the joining node of the completion of a state transfer.

For more information on scripting state snapshot transfers, see :doc:`scriptable-sst`.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_start_position';

   +----------------------+----------------------------------------------------------------------------------+
   | Variable_name        | Value                                                                            |
   +----------------------+----------------------------------------------------------------------------------+
   | wsrep_start_position | 00000000-0000-0000-0000-000000000000:-1/0/0/00000000-0000-0000-0000-000000000000 |
   +----------------------+----------------------------------------------------------------------------------+


.. _`wsrep_status_file`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_status_file``

.. index::
   pair: Parameters; wsrep_status_file

Defines the file name for node status output.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep-status-file``"
   "System Variable", "``wsrep_status_file``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Permitted Values", "String"
   "Default Value", ""
   "Initial Version", "MySQL-wsrep 8.0.26-26.8"

If defined, the file will contain JSON formatted output of node status. The purpose of the file is to provide
a machine readable view of the current node status which is available all the time after the node is started.

The contents of the file are subject to change.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_status_file';

   --------------------+-------------------+
   | Variable_name     | Value             |
   +-------------------+-------------------+
   | wsrep_status_file | wsrep-status.json |
   +-------------------+-------------------+





.. _`wsrep_sync_server_uuid`:
.. rst-class:: section-heading
.. rubric:: ``wsrep_sync_server_uuid``

.. index::
   pair: Parameters; wsrep_sync_server_uuid

Sets the node to use the server UUID received from the donor node.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--wsrep_sync_server_uuid``"
   "System Variable", "``wsrep_sync_server_uuid``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Permitted Values", "String"
   "Default Value", "0"
   "Initial Version", "MySQL-wsrep 8.0.26-26.8"

Unless this variable is set, the wsrep nodes generate individual server UUIDs, which are used on binlog events, such as rolling schema upgrades, that are not replicated through wsrep. This makes individual node histories incomparable and complicates switching asynchronous slave MASTER between the nodes in the cluster. 

When set, this variable forces the nodes to use the same server UUID (generated on the seed node) to binlog events that are not replicated through wsrep. This makes the histories comparable, provided that the user executes such operations in agreed order on all the nodes..

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sync_server_uuid';

   --------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_sync_server_uuid  | 1     |
   +-------------------------+-------+





.. _`wsrep_sync_wait`:
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 5.5.42-25.12, MariaDB: 10.0.13"

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
.. rst-class:: section-heading
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
   "Initial Version", "MySQL-wsrep: 8.0.19-26.3, MariaDB: 10.4.2"

In :term:`Streaming Replication`, the node breaks transactions down into fragments, then replicates and certifies them while the transaction is in progress.  Once certified, a fragment can no longer be aborted due to conflicting transactions.  This parameter determines the number of replication units to include in a fragment.  To define what these units represent, use :ref:`wsrep_trx_fragment_unit <wsrep_trx_fragment_unit>`. A value of ``0`` indicates that streaming replication will not be used.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_trx_fragment_size';

   +-------------------------+-------+
   | Variable_name           | Value |
   +-------------------------+-------+
   | wsrep_trx_fragment_size | 5     |
   +-------------------------+-------+


.. _`wsrep_trx_fragment_unit`:
.. rst-class:: section-heading
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
   "Valid Values", "``bytes``, ``rows``, ``statements``"
   "Initial Version", "MySQL-wsrep: 8.0.19-26.3, MariaDB: 10.4.2"

In :term:`Streaming Replication`, the node breaks transactions down into fragments, then replicates and certifies them while the transaction is in progress.  Once certified, a fragment can no longer be aborted due to conflicting transactions.  This parameter determines the unit to use in determining the size of the fragment.  To define the number of replication units to use in the fragment, use :ref:`wsrep_trx_fragment_size <wsrep_trx_fragment_size>`.

Supported replication units are:

- **bytes**: Refers to the fragment size in bytes.

- **rows**: Refers to the number of rows updated in the fragment.

- **statements**: Refers to the number of SQL statements in the fragment.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_trx_fragment_unit';

   +-------------------------+--------+
   | Variable_name           | Value  |
   +-------------------------+--------+
   | wsrep_trx_fragment_unit | bytes  |
   +-------------------------+--------+


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

   <br />

