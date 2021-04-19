.. meta::
   :title: Audit Log Plugin
   :description: Galera Audit Log Plugin monitors and logs connection and query activity performed on a specific server.
   :language: en-US
   :keywords: galera cluster, audit log
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

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :doc:`log`
      - :doc:`galera-parameters`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`auditlogplugin`:

=================
 Audit Log Plugin
=================

.. index::
   pair: Descriptions; Audit Log Plugin
.. index::
   pair: Logs; Audit Log

Galera Audit Log Plugin monitors and logs connection and query activity performed on a specific server. Information on the activity is stored in the XML log file, where each event will have a ``NAME`` field, a unique ``RECORD_ID`` field and a ``TIMESTAMP`` field. This implementation is alternative to the MySQL Enterprise Audit Log Plugin.

Audit Log plugin logs events, as follows:

- **Audit**/**NoAudit** - An audit event indicates that audit logging has been started or finished. The ``NAME`` field value is ``Audit`` when the logging has been started and ``NoAudit`` when logging has been finished. The audit record also includes server version and command-line arguments. 
   
   An example of an audit event:
   
   .. code-block:: console
   
      <AUDIT_RECORD
      "NAME"="Audit"
      "RECORD"="1_2014-04-29T09:29:40"
      "TIMESTAMP"="2014-04-29T09:29:40 UTC"
      "MYSQL_VERSION"="5.6.17-65.0-655.trusty"
      "STARTUP_OPTIONS"="--basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib/mysql/plugin --user=mysql --log-error=/var/log/mysql/error.log --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306"
      "OS_VERSION"="x86_64-debian-linux-gnu",
      />

- **Connect**/**Disconnect** - A connect record indicates that a user has logged in or logged out. The ``NAME`` field value is ``Connect`` when the user has logged in or the login failed, or ``Quit`` when connection has been closed. Additional fields for this event are ``CONNECTION_ID``, ``STATUS``, ``USER``, ``PRIV_USER``, ``OS_LOGIN``, ``PROXY_USER``, ``HOST``, and ``IP``. ``STATUS`` is ``0`` for successful logins and non-zero for failed logins.

   An example of a disconnect event:
   
   .. code-block:: console
   
      <AUDIT_RECORD
      "NAME"="Quit"
      "RECORD"="24_2014-04-29T09:29:40"
      "TIMESTAMP"="2014-04-29T10:20:13 UTC"
      "CONNECTION_ID"="49"
      "STATUS"="0"
      "USER"=""
      "PRIV_USER"=""
      "OS_LOGIN"=""
      "PROXY_USER"=""
      "HOST"=""
      "IP"=""
      "DB"=""
      />

- **Query** - Additional fields for the query event are: ``COMMAND_CLASS`` (the values come from the ``com_status_vars`` array in the ``sql/mysqld.cc`` file in a MySQL source distribution. Examples are ``select``, ``alter_table``, ``create_table`` and so on), ``CONNECTION_ID``, ``STATUS`` (indicates sn error when non-zero), ``SQLTEXT`` (text of the SQL statement), ``USER``, ``HOST``, ``OS_USER``, ``IP``. Possible values for the ``NAME`` name field for this event are ``Query``, ``Prepare``, ``Execute``, ``Change user`` and so on. 

   An example of a query event:
   
   .. code-block:: console
   
      <AUDIT_RECORD
      "NAME"="Query"
      "RECORD"="23_2014-04-29T09:29:40"
      "TIMESTAMP"="2014-04-29T10:20:10 UTC"
      "COMMAND_CLASS"="select"
      "CONNECTION_ID"="49"
      "STATUS"="0"
      "SQLTEXT"="SELECT * from mysql.user"
      "USER"="root[root] @ localhost []"
      "HOST"="localhost"
      "OS_USER"=""
      "IP"=""
      />

.. _`audit-log-plugin-installing`:
.. rst-class:: section-heading
.. rubric:: Installation

Galera Audit Log plugin is delivered with Galera Cluster, but it is uninstalled by default. To deploy the plugin, run the command below:

.. code-block:: console

   INSTALL PLUGIN audit_log SONAME 'audit_log.so';

To check if the plugin is correctly loaded, run the command below:

.. code-block:: console

   SHOW PLUGINS;

If audit log is listed in the output, the plugin is installed:

.. code-block:: console

   +--------------------------------+----------+--------------------+--------------+---------+
   | Name                           | Status   | Type               | Library      | License |
   +--------------------------------+----------+--------------------+--------------+---------+
   ...
   | audit_log                      | ACTIVE   | AUDIT              | audit_log.so | GPL     |
   +--------------------------------+----------+--------------------+--------------+---------+

.. _`audit-log-plugin-format`:
.. rst-class:: section-heading
.. rubric:: Log Format

The audit log plugin supports four log formats: ``OLD``, ``NEW``, ``JSON``, and ``CSV``. The ``OLD`` and ``NEW`` formats are based on XML, where the former outputs log record properties as XML attributes and the latter as XML tags. Information logged is the same in all four formats. You can define the log format with the ``audit_log_format`` variable.

An example of the ``OLD`` format:

.. code-block:: console

   <AUDIT_RECORD
    "NAME"="Query"
    "RECORD"="2_2014-04-28T09:29:40"
    "TIMESTAMP"="2014-04-28T09:29:40 UTC"
    "COMMAND_CLASS"="install_plugin"
    "CONNECTION_ID"="47"
    "STATUS"="0"
    "SQLTEXT"="INSTALL PLUGIN audit_log SONAME 'audit_log.so'"
    "USER"="root[root] @ localhost []"
    "HOST"="localhost"
    "OS_USER"=""
    "IP"=""
   />

An example of the ``NEW`` format:

.. code-block:: console

   <AUDIT_RECORD>
    <NAME>Quit</NAME>
    <RECORD>10902_2014-04-28T11:02:54</RECORD>
    <TIMESTAMP>2014-04-28T11:02:59 UTC</TIMESTAMP>
    <CONNECTION_ID>36</CONNECTION_ID>
    <STATUS>0</STATUS>
    <USER></USER>
    <PRIV_USER></PRIV_USER>
    <OS_LOGIN></OS_LOGIN>
    <PROXY_USER></PROXY_USER>
    <HOST></HOST>
    <IP></IP>
    <DB></DB>
   </AUDIT_RECORD>

An example of the ``JSON`` format:

.. code-block:: console

   {"audit_record":{"name":"Query","record":"4707_2014-08-27T10:43:52","timestamp":"2014-08-27T10:44:19 UTC","command_class":"show_databases","connection_id":"37","status":0,"sqltext":"show databases","user":"root[root] @ localhost []","host":"localhost","os_user":"","ip":""}}

An example of the ``CSV`` format:

.. code-block:: console

   "Query","49284_2014-08-27T10:47:11","2014-08-27T10:47:23 UTC","show_databases","37",0,"show databases","root[root] @ localhost []","localhost","",""

.. _`audit-log-plugin-streaming-to-syslog`:
.. rst-class:: section-heading
.. rubric:: Streaming the Audit Log to syslog

To stream the audit log to syslog, set the ``audit_log_handler`` variable to ``SYSLOG``. To control the syslog file handler, use the following variables: ``audit_log_syslog_ident``, ``audit_log_syslog_facility``, and ``audit_log_syslog_priority``. These variables have the same meaning as corresponding parameters described in the `syslog(3) manual <https://linux.die.net/man/3/syslog>`_.

.. note:: Variables: ``audit_log_strategy``, ``audit_log_buffer_size``, ``audit_log_rotate_on_size``, ``audit_log_rotations`` only have effect with ``FILE`` handler.

.. _`audit-log-plugin-filtering-by-user`:
.. rst-class:: section-heading
.. rubric:: Filtering by User

For filtering by user, there are two global variables: ``audit_log_include_accounts`` and ``audit_log_exclude_accounts``, to specify which user accounts should be included or excluded from audit logging.

.. warning:: Only one of these variables can contain a list of users to be either included or excluded, while the other must be ``NULL``. If one of the variables is set to be not ``NULL`` (that is, it contains a list of users), the attempt to set another one will fail. An empty string defines an empty list.

.. note:: Changes to ``audit_log_include_accounts`` and ``audit_log_exclude_accounts`` do not apply to the existing server connections.

The example below describes how to add users to be monitored:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_accounts = 'user1@localhost,root@localhost';
   Query OK, 0 rows affected (0.00 sec)

If you try to add users to both the include and exclude lists, the server gives you the error below:

.. code-block:: console

   mysql> SET GLOBAL audit_log_exclude_accounts = 'user1@localhost,root@localhost';
   ERROR 1231 (42000): Variable 'audit_log_exclude_accounts' can't be set to the value of 'user1@localhost,root@localhost'

To switch from filtering by the included user list to the excluded user list, or back, first set the currently active filtering variable to ``NULL``:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_accounts = NULL;
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_accounts = 'user1@localhost,root@localhost';
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_accounts = "'user'@'host'";
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_accounts = '''user''@''host''';
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_accounts = '\'user\'@\'host\'';
   Query OK, 0 rows affected (0.00 sec)

To see the current users on the list, run:

.. code-block:: console

   mysql> SELECT @@audit_log_exclude_accounts;
   +------------------------------+
   | @@audit_log_exclude_accounts |
   +------------------------------+
   | 'user'@'host'                |
   +------------------------------+
   1 row in set (0.00 sec)

The account names from the ``mysql.user`` table are logged in the audit log. For example, when you create a user:

.. code-block:: console

   mysql> CREATE USER 'user1'@'%' IDENTIFIED BY '111';
   Query OK, 0 rows affected (0.00 sec)

This is what is logged when ``user1`` connects from ``localhost``:

.. code-block:: console

   <AUDIT_RECORD
     NAME="Connect"
     RECORD="4971917_2016-08-22T09:09:10"
     TIMESTAMP="2016-08-22T09:12:21 UTC"
     CONNECTION_ID="6"
     STATUS="0"
     USER="user1" ;; this is a 'user' part of account in 8.0
     PRIV_USER="user1"
     OS_LOGIN=""
     PROXY_USER=""
     HOST="localhost" ;; this is a 'host' part of account in 8.0
     IP=""
     DB=""
   />

To exclude ``user1`` from logging, set:

.. code-block:: console

   SET GLOBAL audit_log_exclude_accounts = 'user1@%';

The value can be ``NULL`` or a comma separated list of accounts in format ``user@host`` or ``'user'@'host'`` (if the user or host contains a comma).


.. _`audit-log-plugin-filtering-by-sql-command-type`:
.. rst-class:: section-heading
.. rubric:: Filtering by SQL Command Type

For filtering by SQL command type, there are two global variables: ``audit_log_include_commands`` and ``audit_log_exclude_commands``, to specify the command types included or excluded from audit logging.

.. warning:: Only one of these variables can contain a list of command types to be either included or excluded, while the other must be ``NULL``. If one of the variables is set to be not ``NULL`` (that is, it contains a list of command types), the attempt to set another one will fail. An empty string defines an empty list.

.. note:: If both ``audit_log_include_commands`` and ``audit_log_exclude_commands`` are ``NULL``, all commands are logged.

The available command types can be listed by running:

.. code-block:: console

   mysql> SELECT name FROM performance_schema.setup_instruments WHERE name LIKE "statement/sql/%" ORDER BY name;
   +------------------------------------------+
   | name                                     |
   +------------------------------------------+
   | statement/sql/alter_db                   |
   | statement/sql/alter_db_upgrade           |
   | statement/sql/alter_event                |
   | statement/sql/alter_function             |
   | statement/sql/alter_procedure            |
   | statement/sql/alter_server               |
   | statement/sql/alter_table                |
   | statement/sql/alter_tablespace           |
   | statement/sql/alter_user                 |
   | statement/sql/analyze                    |
   | statement/sql/assign_to_keycache         |
   | statement/sql/begin                      |
   | statement/sql/binlog                     |
   | statement/sql/call_procedure             |
   | statement/sql/change_db                  |
   | statement/sql/change_master              |
   ...
   | statement/sql/xa_rollback                |
   | statement/sql/xa_start                   |
   +------------------------------------------+
   145 rows in set (0.00 sec)

To add commands to the include filter, run:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_commands= 'set_option,create_db';

If you now create a database:

.. code-block:: console

   mysql> CREATE DATABASE hello-world;

You will see it the audit log:

.. code-block:: console

   <AUDIT_RECORD
     NAME="Query"
     RECORD="10724_2016-08-18T12:34:22"
     TIMESTAMP="2016-08-18T15:10:47 UTC"
     COMMAND_CLASS="create_db"
     CONNECTION_ID="61"
     STATUS="0"
        SQLTEXT="create database hello-world"
     USER="root[root] @ localhost []"
     HOST="localhost"
     OS_USER=""
     IP=""
     DB=""
   />

To switch command type filtering type from the included type list to the excluded type list or back, first reset the currently active list to ``NULL``:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_commands = NULL;
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_commands= 'set_option,create_db';
   Query OK, 0 rows affected (0.00 sec)

.. note:: Invocation of stored procedures has command type ``call_procedure``, and also all the statements executed within the procedure have the same type ``call_procedure``.

.. _`audit-log-plugin-filtering-by-database`:
.. rst-class:: section-heading
.. rubric:: Filtering by Database

The filtering by SQL database is implemented by two global variables: ``audit_log_include_databases`` and ``audit_log_exclude_databases`` to specify the databases included or excluded from audit logging.

.. warning:: Only one of these variables can contain a list of databases to be either included or excluded, while the other must be ``NULL``. If one of the variables is set to be not ``NULL`` (that is, it contains a list of databases), the attempt to set another one will fail. An empty string defines an empty list.

If a query accesses any of the databases listed in ``audit_log_include_databases``, the query will be logged. If a query accesses only databases listed in ``audit_log_exclude_databases``, the query will not be logged. ``CREATE TABLE`` statements are logged unconditionally.

.. note:: Changes of ``audit_log_include_databases`` and ``audit_log_exclude_databases`` do not apply to existing server connections.

To add databases to be monitored, run:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_databases = 'test,mysql,db1';
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_include_databases= 'db1,```db3"`';
   Query OK, 0 rows affected (0.00 sec)

If you try to add databases to both include and exclude lists, the server will give the error below:

.. code-block:: console

   mysql> SET GLOBAL audit_log_exclude_databases = 'test,mysql,db1';
   ERROR 1231 (42000): Variable 'audit_log_exclude_databases can't be set to the value of 'test,mysql,db1'

To switch from filtering by the included database list to the excluded database list, or back, first set the currently active filtering variable to ``NULL``:

.. code-block:: console

   mysql> SET GLOBAL audit_log_include_databases = NULL;
   Query OK, 0 rows affected (0.00 sec)
   
   mysql> SET GLOBAL audit_log_exclude_databases = 'test,mysql,db1';
   Query OK, 0 rows affected (0.00 sec)

.. _`audit-log-plugin-system-variables`:
.. rst-class:: section-heading
.. rubric:: System Variables



.. _`audit_log_strategy`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_strategy``

.. index::
   pair: Parameters; audit_log_strategy

This variable is used to specify the audit log strategy.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_strategy``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Permitted Values", "``ASYNCHRONOUS``, ``PERFORMANCE``, ``SEMISYNCHRONOUS``, ``SYNCHRONOUS``"
   "Default Value", "``ASYNCHRONOUS``"

The possible values are:

- ``ASYNCHRONOUS`` - Log using the memory buffer, do not drop messages if the buffer is full
- ``PERFORMANCE`` - Log using the memory buffer, drop messages if the buffer is full
- ``SEMISYNCHRONOUS`` - Log directly to a file, do not flush and sync every event
- ``SYNCHRONOUS`` - Log directly to file, flush and sync every event

This variable only has effect when ``audit_log_handler`` is set to ``FILE``.



.. _`audit_log_file`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_file``

.. index::
   pair: Parameters; audit_log_file

This variable is used to specify the filename where to store the audit log. It can contain the path relative to the datadir or absolute path.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_file``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Default Value", "``audit.log``"


.. _`audit_log_flush`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_flush``

.. index::
   pair: Parameters; audit_log_flush

When this variable is ``ON``, the log file will be closed and reopened. This can be used for manual log rotation.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_flush``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"
   "Default Value", "``OFF``"
   
   
   
.. _`audit_log_buffer_size`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_buffer_size``

.. index::
   pair: Parameters; audit_log_buffer_size

This variable is used to specify the memory buffer size used for logging. The variable is used, when the ``audit_log_strategy`` variable is set to ``ASYNCHRONOUS`` or ``PERFORMANCE``. This variable only has effect when ``audit_log_handler`` is set to ``FILE``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_buffer_size``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_exclude_accounts`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_exclude_accounts``

.. index::
   pair: Parameters; audit_log_exclude_accounts

This variable is used to specify the list of users for which filtering by user is applied. The value can be ``NULL`` or a comma separated list of accounts in format ``user@host`` or ``'user'@'host'`` (if the user or host name contains a comma). If this variable is set, ``audit_log_include_accounts`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_exclude_accounts``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_exclude_commands`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_exclude_commands``

.. index::
   pair: Parameters; audit_log_exclude_commands

This variable is used to specify the list of commands for which filtering by SQL command type is applied. The value can be ``NULL`` or a comma separated list of commands. If this variable is set, ``audit_log_include_commands`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_exclude_commands``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_exclude_databases`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_exclude_databases``

.. index::
   pair: Parameters; audit_log_exclude_databases

This variable is used to specify the list of databases for which filtering by database is applied. The value can be ``NULL`` or a comma separated list of databases. If this variable is set, ``audit_log_include_databases`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_exclude_databases``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"



.. _`audit_log_format`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_format``

.. index::
   pair: Parameters; audit_log_format

This variable is used to specify the audit log format. The audit log plugin supports four log formats: ``OLD``, ``NEW``, ``JSON``, and ``CSV``. ``OLD`` and ``NEW`` formats are based on XML, where the former outputs log record properties as XML attributes and the latter as XML tags. Information logged is the same in all four formats.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_format``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Permitted Values", "``OLD``, ``NEW``, ``JSON``, ``CSV``"
   "Default Value", "``OLD``"


.. _`audit_log_include_accounts`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_include_accounts``

.. index::
   pair: Parameters; audit_log_include_accounts

This variable is used to specify the list of users for which filtering by user is applied. The value can be ``NULL`` or a comma separated list of accounts in format ``user@host`` or ``'user'@'host'`` (if the user or host name contains a comma). If this variable is set, ``audit_log_exclude_accounts`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_include_accounts``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_include_commands`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_include_commands``

.. index::
   pair: Parameters; audit_log_include_commands

This variable is used to specify the list of commands for which filtering by SQL command type is applied. The value can be ``NULL`` or a comma separated list of commands. If this variable is set, ``audit_log_exclude_commands`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_include_commands``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_include_databases`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_include_databases``

.. index::
   pair: Parameters; audit_log_include_databases

This variable is used to specify the list of databases for which filtering by database is applied. The value can be ``NULL`` or a comma separated list of databases. If this variable is set, ``audit_log_exclude_databases`` must be unset, and vice versa.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_include_databases``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"


.. _`audit_log_policy`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_policy``

.. index::
   pair: Parameters; audit_log_policy

This variable is used to specify the events, which are logged. 

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_policy``"
   "Variable Scope", "Global"
   "Dynamic Variable", "Yes"
   "Variable Type", "String"
   "Permitted Values", "``ALL``, ``LOGINS``, ``QUERIES``, ``NONE``"
   "Default Value", "``ALL``"

The possible values are:

- ``ALL`` - Log all events
- ``LOGINS`` - Log logins only
- ``QUERIES`` - Log queries only
- ``NONE`` - Log no events


.. _`audit_log_rotate_on_size`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_rotate_on_size``

.. index::
   pair: Parameters; audit_log_rotate_on_size

This variable is used to specify the maximum audit log file size. Upon reaching this size, the log will be rotated. The rotated log files are in the same same directory as the current log file. A sequence number is appended to the log file name upon rotation. This variable only has effect when ``audit_log_handler`` is set to ``FILE``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_rotate_on_size``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "Numeric"
   "Default Value", "``0`` (do log rotate the log file)"


.. _`audit_log_rotations`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_rotations``

.. index::
   pair: Parameters; audit_log_rotations

This variable is used to specify how many log files is kept when ``audit_log_rotate_on_size`` variable is set to a non-zero value. This variable only has effect when ``audit_log_handler`` is set to ``FILE``.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_rotations``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "Numeric"
   "Default Value", "``0``"



.. _`audit_log_handler`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_handler``

.. index::
   pair: Parameters; audit_log_handler

This variable is used to configure where the audit log is written. If set to ``FILE``, the log is written into a file specified by the ``audit_log_file`` variable. If set to ``SYSLOG``, the audit log is written to syslog.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_handler``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Permitted Values", "``FILE``, ``SYSLOG``"
   "Default Value", "``FILE``"


.. _`audit_log_syslog_ident`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_syslog_ident``

.. index::
   pair: Parameters; audit_log_syslog_ident

This variable is used to specify the ``ident`` value for syslog. This variable has the same meaning as the corresponding parameter described in the `syslog(3) manual <https://linux.die.net/man/3/syslog>`_.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_syslog_ident``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Default Value", "``percona-audit``"


.. _`audit_log_syslog_facility`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_syslog_facility``

.. index::
   pair: Parameters; audit_log_syslog_facility

This variable is used to specify the ``facility`` value for syslog. This variable has the same meaning as the corresponding parameter described in the `syslog(3) manual <https://linux.die.net/man/3/syslog>`_.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_syslog_facility``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Default Value", "``LOG_USER``"  



.. _`audit_log_syslog_priority`:
.. rst-class:: section-heading
.. rubric:: ``audit_log_syslog_priority``

.. index::
   pair: Parameters; audit_log_syslog_priority

This variable is used to specify the ``priority`` value for syslog. This variable has the same meaning as the corresponding parameter described in the `syslog(3) manual <https://linux.die.net/man/3/syslog>`_.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--audit_log_syslog_priority``"
   "Variable Scope", "Global"
   "Dynamic Variable", "No"
   "Variable Type", "String"
   "Default Value", "``LOG_INFO``"  


.. _`audit-log-plugin-status-variables`:
.. rst-class:: section-heading
.. rubric:: Status Variables


.. _`Audit_log_buffer_size_overflow`:
.. rst-class:: section-heading
.. rubric:: ``Audit_log_buffer_size_overflow``

.. index::
   pair: Parameters; Audit_log_buffer_size_overflow

The number of times an audit log entry was either dropped or written directly to the file, due to its size being bigger than the ``audit_log_buffer_size`` variable.

.. csv-table::
   :class: doc-options

   "Command-line Format", "``--Audit_log_buffer_size_overflow``"
   "Variable Scope", "Global"
   "Variable Type", "Numeric"



.. container:: bottom-links

   Related Documents

   - :doc:`log`
   - :doc:`galera-parameters`
