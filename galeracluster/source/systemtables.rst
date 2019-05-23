=========================
 Galera System Tables
=========================
.. _`systemtables`:


The ‘mysql’ schema contains new Galera replication related tables:

wsrep_cluster
wsrep_cluster_members
wsrep_streaming_log

.. code-block:: mysql

   SHOW TABLES FROM mysql LIKE 'wsrep%';

   +---------------------------+
   | Tables_in_mysql (wsrep%)  |
   +---------------------------+
   | wsrep_cluster             |
   | wsrep_cluster_members     |
   | wsrep_streaming_log       |
   +---------------------------+



End users may read but not modify these tables.