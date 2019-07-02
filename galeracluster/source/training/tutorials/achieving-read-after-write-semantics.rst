.. cssclass:: tutorial-article
.. _`achieving-read-after-write-semantics`:

===================================================
Achieving Read-After-Write Semantics with Galera
===================================================

.. rst-class:: list-stats

   Length:  599 words; Writer: Philip Stoev; Published: June 17, 2015; Topic: General; Level: Intermediate

Some applications, particularly those written with a single-node database server in mind, attempt to immediately read a value they have just inserted into the database, without making those those operations part of a single transaction. A read/write splitting proxy or a connection pool combined with a load-balancer can direct each operation to a different database node.

Since Galera allows, for performance reasons, a very small amount of “slave lag”, the node that is processing the read may have not yet applied the write. It can return old data, causing an application that did not expect that to misbehave or produce an error.

---------------------------
The Solution
---------------------------

Through the mechanism of flow control, slave lag is kept to a minimum, but additionally Galera provides the causal wait facility for those queries that must always see the most up-to-date view of the database. It allows achieving truly read-after-write semantics, where a read will always see all writes that were performed prior to it, on any node.

Enabling causal wait causes Galera to wait before a query until all transactions that were started prior to the current transaction have been applied on the node. Transactions committed or updates made on other nodes after the start of the current transaction are not taken into account.


---------------------------
Configuring Causal Wait
---------------------------

Causal wait is controlled via the wsrep_sync_wait variable. It is a bitmask that specifies what classes of queries (selects, inserts, updates, or deletes) should wait for complete synchronization. The documentation has a list of allowed values.

wsrep_sync_wait is a session variable, so it can be targeted at the connections, transactions or queries that require it. The remaining application workload, which does not require the extra freshness guarantee can use the default behavior and proceed without any additional waits.


---------------------------
A Practical Example
---------------------------

Consider the case where you have set up a read/write splitting proxy in front of your application so that your writes go to the master and the reads are serviced by the slaves. Such a setup would work for a wide range of queries and applications and you would like to keep it and its performance characteristics.
If access to the source code is available, it is possible to surgically cure problematic queries with as little change as possible. You could do the following:

.. code-block:: console

   SET @wsrep_sync_wait_orig = @@wsrep_sync_wait;

   SET SESSION wsrep_sync_wait = GREATEST(@wsrep_sync_wait_orig, 1);

   SELECT ...

   SET SESSION wsrep_sync_wait = @wsrep_sync_wait_orig;

This sequence of SQL commands preserves the existing value of wsrep_sync_wait and then sets it to at least 1, meaning that SELECTs are subject to causal wait. Once we have issued the SELECT, we restore the previous value of the variable.

If a whole application or connection is affected, it is also possible to enable causal reads at connection time by adding it to the connection DSN or the constructor, either as a literal SQL command or by putting it into a configuration file that will be read at connection time.
Here is how to achieve that in various languages:

PERL:

.. code-block:: console

   $dsn = "DBI:mysql:test;mysql_read_default_file=/etc/mysql/connectors.cnf";
   $dbh = DBI->connect($dsn, $user, $password);

The value for wsrep_sync_wait will be taken from the [client] option group in /etc/mysql/connectors.cnf.

PHP:

.. code-block:: console

   $pdo = new PDO(
    'mysql:host=localhost',
    "username",
    "password",
    array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET SESSION wsrep_sync_wait = 1")
   );

PDO::MYSQL_ATTR_READ_DEFAULT_FILE and PDO::MYSQL_ATTR_READ_DEFAULT_GROUP can also be used.

PYTHON:

.. code-block:: console

   cnx = mysql.connector.connect(option_files='/etc/mysql/connectors.cnf')

The MySQL Manual has more information on Connector/Python and option files.
