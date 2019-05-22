=========================================
Unknown Command Errors
=========================================
.. _`query-gives-unknown-command-erros`:

Every query returns the ``Unknown Command`` error.


.. rubric:: Situation

You log into a node and try to execute a query from a database client.  Every query  returns the same error message:

.. code-block:: mysql

   SELECT * FROM example_table;

   ERROR: Unknown command '\\'

The reason for the error is that the node considers itself out of sync with the global state of the cluster.  It is unable to handle SQL statements except for ``SET`` and ``SHOW`` statements.

This occurs when you have explicitly set the wsrep Provider (i.e., the :ref:`wsrep_provider <wsrep_provider>`), but the wsrep Provider rejects service.  This happens in situations in which the node is unable to connect to the :term:`Primary Component`.  It happen when the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter becomes unset.  It can also happen due to networking issues.



.. rubric:: Solution

Using the :ref:`wsrep_on <wsrep_on>` variable dynamically, you can bypass the wsrep Provider check.  However, this disables replication.

.. code-block:: mysql

   SET wsrep_on=OFF;

This SQL statement tells ``mysqld`` to ignore the :ref:`wsrep_provider <wsrep_provider>` setting and behave as a standard stand-alone database server.  Doing this can lead to data inconsistency with the rest of the cluster, but that may be the desired result for modifying the "local" tables.

If you know or suspect that a cluster doesn't have a :term:`Primary Component`, you need to bootstrap a new one.  There are a couple of queries you'll need to run on each node in the cluster.

First, confirm that the node is not part of the Primary Component by checking the :ref:`wsrep_cluster_status <wsrep_cluster_status>` status variable.  Do this by executing the following ``SHOW STATUS`` statement on each node:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_status';

   +----------------------+-------------+
   | Variable_name        | Value       |
   +----------------------+-------------+
   | wsrep_cluster_status | Non_primary |
   +----------------------+-------------+

If this query returns a value of ``Primary``, the node is part of the Primary Component.  If it returns any other value, that indicates the node is part of a non-operational component.

Next, find the sequence number of the last committed transaction on each node by getting the value of the :ref:`wsrep_last_committed <wsrep_last_committed>` status variable. Do this by executing ``SHOW STATUS`` statement on each node like this: 

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

In the event that none of the nodes are the Primary Component, you will need to bootstrap a new one.  The node that returned the largest sequence number is the most advanced in the cluster.  On that node, run the following ``SET`` statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

The node on which you executed this will now operate as the starting point in a new Primary Component.  Nodes that are part of non-operational components and have network connectivity will attempt to initiate a state transfer to bring their own databases up-to-date with this node.  At this point, the cluster will begin accepting SQL requests.




