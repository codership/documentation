=========================================
Unknown Command Errors
=========================================
.. _`query-gives-unknown-command-erros`:

Every query returns the ``Unknown command`` error.


.. rubric:: Situation

For example, you log into a node and try to run a query from the database client.  Every query you run generates the same error:

.. code-block:: mysql

   SELECT * FROM example_table;

   ERROR: Unknown command '\\'

The reason for the error is that the node considers itself out of sync with the global state of the cluster.  It is unable to serve SQL requests except for ``SET`` and ``SHOW``.

This occurs when you have explicitly set the wsrep Provider (through the :ref:`wsrep_provider <wsrep_provider>` parameter), but the wsrep Provider rejects service.  For example, this happens in cases where the node is unable to connect to the :term:`Primary Component`, such as when the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter becomes unset or due to networking issues.



.. rubric:: Solution

Using the :ref:`wsrep_on <wsrep_on>` parameter dynamically, you can bypass the wsrep Provider check.  This disables replication.

.. code-block:: mysql

   SET wsrep_on=OFF;

This command tells ``mysqld`` to ignore the :ref:`wsrep_provider <wsrep_provider>` setting and behave as a standard standalone database server.  Doing this can lead to data inconsistency with the rest of the cluster, but that may be the desired result for modifying the "local" tables.

In the event that you know or suspect that your cluster does not have a :term:`Primary Component`, you need to bootstrap a new one.  On each node in the cluster, run the following queries:

#. Using the :ref:`wsrep_cluster_status <wsrep_cluster_status>` status variable, confirm that the node is not part the Primary Component:

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_cluster_status';

      +----------------------+-------------+
      | Variable_name        | Value       |
      +----------------------+-------------+
      | wsrep_cluster_status | Non_primary |
      +----------------------+-------------+

   If the query returns ``Primary``, the node is part of the Primary Component.  If the query returns any other value, it indicates that the node is part of a nonoperational component.

#. Using the :ref:`wsrep_last_committed <wsrep_last_committed>` status variable, find the sequence number of the last committed transaction.

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_last_committed';

      +----------------------+--------+
      | Variable_name        | Value  |
      +----------------------+--------+
      | wsrep_last_committed | 409745 |
      +----------------------+--------+

In the event that none of the nodes show as the Primary Component,  you need to bootstrap a new one.  The node that returns the largest sequence number is the most advanced in the cluster.  On that node, run the following command:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

The node now operates as the starting point in a new Primary Component.  Nodes that are part of nonoperational components that have network connectivity attempt to initiate a state transfer to bring their own databases up-to-date with this node.  The cluster begins accepting SQL requests again.




