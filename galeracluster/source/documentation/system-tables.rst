.. meta::
   :title: Galera Cluster related System Tables
   :description:
   :language: en-US
   :keywords: galera cluster, system tables, myisam, cluster streaming log
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
.. _`system-tables`:

=========================
Galera System Tables
=========================

.. index::
   pair: Galera Cluster 4.x; System Tables

Starting with version 4 of Galera, three system tables related to Galera replication were added to the ``mysql`` database: ``wsrep_cluster``, ``wsrep_cluster_members``, and ``wsrep_streaming_log``.  As of MariaDB Server 10.10, and MySQL-wsrep 8.4.2, there is yet another, ``wsrep_allowlist``. These system tables may be used by database administrators to get a sense of the current layout of the nodes in a cluster.

To see these tables on your server, execute the following SQL statement one of them using the ``mysql`` client or a similar client:

.. code-block:: mysql

   SHOW TABLES FROM mysql LIKE 'wsrep%';

   +---------------------------+
   | Tables_in_mysql (wsrep%)  |
   +---------------------------+
   | wsrep_allowlist           |
   | wsrep_cluster             |
   | wsrep_cluster_members     |
   | wsrep_streaming_log       |
   +---------------------------+

Database administrators and clients with the access to the ``mysql`` database may read these tables, but they may not modify them: the database itself will make modifications, as needed. If your server doesn't have these tables, it may be that your server is using an older version of Galera.

.. _`allowlist`:
.. rst-class:: section-heading
.. rubric:: Allowlist

The ``wsrep_allowlist`` table stores the allowed IP addresses that can perform an IST/SST, in a comma delimited format. Before the introduction of "wsrep_allowlist", as long as a node has access to Galera Cluster TCP ports, it can make an SST/IST request, without authentication being performed; some users prefer to have a method to make this more robust, and secure, hence with ``wsrep_allowlist`` only if the JOINER node is in the IP list, will it be allowed to join the cluster.

You can either have IPv4 or IPv6 addresses for ``wsrep_allowlist``, but it does not allow wildcard IPs or hostnames.

.. code-block:: mysql

    MariaDB [mysql]> describe wsrep_allowlist\G
    *************************** 1. row ***************************
    Field: ip
    Type: char(64)
    Null: NO
    Key: PRI
    Default: NULL
    Extra: 
    1 row in set (0.001 sec)

To alter the allowlist, execute command:

.. code-block:: mysql

    insert into mysql.wsrep_allowlist(ip) values('18.193.102.155');

and the result will look like:

.. code-block:: mysql

    MariaDB [mysql]> select * from wsrep_allowlist;
    +----------------+
    | ip             |
    +----------------+
    | 18.193.102.155 |
    | 18.194.147.243 |
    +----------------+
    2 rows in set (0.000 sec)

When another node tries to get connected, the potential DONOR nodes will see this in the ``error.log``:

.. code-block:: mysql

    2024-03-18  8:19:02 0 [Warning] WSREP: Connection not allowed, IP 3.70.155.51 not found in allowlist.

On the node trying to be the JOINER not in the allowlist, an error such as the one below should be easily notable:

.. code-block:: mysql

    2024-03-18  8:19:14 0 [ERROR] WSREP: failed to open gcomm backend connection: 110: failed to reach primary view: 110 (Connection timed out) at ./gcomm/src/pc.cpp:connect():160
    2024-03-18  8:19:14 0 [ERROR] WSREP: ./gcs/src/gcs_core.cpp:gcs_core_open():221: Failed to open backend connection: -110 (Connection timed out)
    2024-03-18  8:19:15 0 [ERROR] WSREP: ./gcs/src/gcs.cpp:gcs_open():1674: Failed to open channel 'mariadb' at 'gcomm://18.194.147.243,18.193.102.155': -110 (Connection timed out)
    2024-03-18  8:19:15 0 [ERROR] WSREP: gcs connect failed: Connection timed out

Add the remaining node to the allowlist to fix this:

.. code-block:: mysql

    MariaDB [mysql]> insert into mysql.wsrep_allowlist(ip) values('3.70.155.51');
    Query OK, 1 row affected (0.002 sec)
    
    MariaDB [mysql]> select * from wsrep_allowlist;
    +----------------+
    | ip             |
    +----------------+
    | 18.193.102.155 |
    | 18.194.147.243 |
    | 3.70.155.51    |
    +----------------+
    3 rows in set (0.000 sec)

And now we are back to having a three-node Galera Cluster.

.. _`cluster-view`:
.. rst-class:: section-heading
.. rubric:: Cluster View

One of the new Galera related system tables is the ``wsrep_cluster`` table. This new table, starting in version 4 of Galera, contains a current view of the cluster. That is to say, it stores the UUID of the cluster and some other identification information, as well as the cluster's capabilities.

To see the names of the columns in this table, either use the ``DESCRIBE`` statement or execute the following SQL statement from the ``mysql`` client on one of the nodes in the cluster:

.. code-block:: mysql

   SELECT COLUMN_NAME FROM information_schema.columns
   WHERE table_schema='mysql'
   AND table_name='wsrep_cluster';

   +------------------+
   | COLUMN_NAME      |
   +------------------+
   | cluster_uuid     |
   | view_id          |
   | view_seqno       |
   | protocol_version |
   | capabilities     |
   +------------------+

The ``cluster_uuid`` contains the UUID of the cluster.

The ``view_id`` corresponds to the status value of the ``wsrep_cluster_conf_id``, the number of cluster configuration changes which have occurred in the cluster.  The ``view_seqno`` on the other hand, corresponds to Galera sequence number associated with the cluster view.  The protocol version is the same value as contained in the ``wsrep_protocol_version`` variable.  It's the protocol version of the MySQL-wsrep or the MariaDB wsrep patch. Last, the  ``capabilities`` column contains the capabilities bitmask provided by the Galera library. It's metadata that will be needed to recover node state during crash recovery.

If you execute the following SQL statement from any node in a cluster, you can see the contents of this table:

.. code-block:: console

   SELECT * FROM mysql.wsrep_cluster \G

   *************************** 1. row ***************************
       cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
            view_id: 3
         view_seqno: 2956
   protocol_version: 4
       capabilities: 184703

In the results here, you can see the cluster UUID. This can also be found by using the SQL statement, ``SHOW STATUS`` for the variable, ``wsrep_local_state_uuid``.


.. _`cluster-members`:
.. rst-class:: section-heading
.. rubric:: Cluster Members

Another Galera related system tables is the ``wsrep_cluster_members`` table. This system table will provide the current membership of the cluster; it will contain a row for each node in the cluster.  That is to say, each node in the cluster known to the node upon which the table is queried.

To see the names of columns in this table, either use the ``DESCRIBE`` statement or execute the following SQL statement from the ``mysql`` client on one of the nodes in the cluster:

.. code-block:: mysql

   SELECT COLUMN_NAME FROM information_schema.columns
   WHERE table_schema='mysql'
   AND table_name='wsrep_cluster_members';

   +-----------------------+
   | COLUMN_NAME           |
   +-----------------------+
   | node_uuid             |
   | cluster_uuid          |
   | node_name             |
   | node_incoming_address |
   +-----------------------+


The ``node_uuid`` records the UUID of each node in the cluster. The ``cluster_uuid`` is the UUID of the cluster for which the node belongs--the one on which the table has been queried. This is currently the same as what's contained in the ``wsrep_cluster table``. The ``node_name`` contains the human readable name of each node, Last, the ``node_incoming_address`` stores the IP address and port on which each node is listening for client connections.

If you execute the following SQL statement from any node in a cluster, you can see the contents of this table:

.. code-block:: console

   SELECT * FROM mysql.wsrep_cluster_members ORDER BY node_name \G

   *************************** 1. row ***************************
               node_uuid: e39d1774-7e2b-11e9-b5b2-7696f81d30fb
            cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
               node_name: galera1
   node_incoming_address: AUTO
   *************************** 2. row ***************************
               node_uuid: eb8fc512-7e2b-11e9-bb74-3281cf207f60
            cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
               node_name: galera2
   node_incoming_address: AUTO
   *************************** 3. row ***************************
               node_uuid: 2347a8ac-7e2c-11e9-b6f0-da90a2d0a563
            cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
               node_name: galera3
   node_incoming_address: AUTO


In the results of this example you can see that this cluster is composed of three nodes.  The node UUIDs are unique for each node. Notice that the cluster UUID is the same for all three and corresponds to the related value found in the ``wsrep_cluster`` table shown in the example earlier. Each node has a unique name (e.g., galera1). They were named in the configuration file using the ``wsrep_node_name`` parameter.  The incoming node address is set to ``AUTO`` for all of these nodes, but they can be set individual to specific nodes with the ``wsrep-node-address`` or the ``bind-address`` parameter in each node's configuration file.


.. _`cluster-streaming-log`:
.. rst-class:: section-heading
.. rubric:: Cluster Streaming Log

The last Galera related system tables is the ``wsrep_streaming_log`` table. This system table contains meta data and row events for ongoing streaming transactions, write set fragment per row.

The ``node_uuid`` column contains the node UUID of the hosting node for the transaction (i.e. node where the client is executing the transaction). The ``trx_id`` column stores the transaction identifier, whereas the ``seqno`` stores the sequence number of the write set fragment. Last, the ``flags`` columns records flags associated with the write set fragment, and ``frag`` contains the binary log replication events contained in the write set fragment.

To see the names of columns in this table, either use the ``DESCRIBE`` statement or execute the following SQL statement from the ``mysql`` client on one of the nodes in the cluster:

.. code-block:: mysql

   SELECT COLUMN_NAME FROM information_schema.columns
   WHERE table_schema='mysql'
   AND table_name='wsrep_streaming_log';

   +-------------+
   | COLUMN_NAME |
   +-------------+
   | node_uuid   |
   | trx_id      |
   | seqno       |
   | flags       |
   | frag        |
   +-------------+

If you execute the following SQL statement from any node in a cluster, you can see the contents of this table:

.. code-block:: console

   SELECT * FROM mysql.wsrep_streaming_log \G

Typically, you won't see any results since it will contain entries only for transactions which have streaming replication enabled. For example:

.. code-block:: mysql

   CREATE TABLE table1 (col1 INT PRIMARY KEY);

   SET SESSION wsrep_trx_fragment_size=1;

   START TRANSACTION;

   INSERT INTO table1 VALUES (100);

   SELECT node_uuid, trx_id, seqno, flags
   FROM mysql.wsrep_streaming_log;

   +--------------------------------------+--------+-------+-------+
   | node_uuid                            | trx_id | seqno | flags |
   +--------------------------------------+--------+-------+-------+
   | a006244a-7ed8-11e9-bf00-867215999c7c |     26 |     4 |     1 |
   +--------------------------------------+--------+-------+-------+

You can see in the results from the example here that the node UUID matches that of the third node (i.e., ``galera3``) in the results for the example above related to the ``wsrep_cluster_members`` table. In this example, the ``frag`` column was omitted from the ``SELECT`` statement since it contains binary characters that don't format well.

.. note:: Galera Cluster no longer uses ``INFORMATION_SCHEMA.PROCESSLIST``, since it has been deprecated upstream. Instead, it uses "PERFORMANCE_SCHEMA.PROCESSLIST". See the example below:
   
   .. code-block:: console
   
      SET GLOBAL wsrep_applier_threads = 10;
      SELECT COUNT(*) AS EXPECT_10 FROM performance_schema.threads WHERE NAME = 'thread/sql/wsrep_applier_thread';
   
   Or:
   
   .. code-block:: console

      SELECT COUNT(*) IN (1, 2) FROM performance_schema.processlist WHERE USER = 'system user' AND STATE LIKE '%committed%';

