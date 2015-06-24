==================================================
Cluster Stalls on ``ALTER``
==================================================
.. _`cluster-stalls-on-alter`:

The cluster stalls when you run an ``ALTER`` query on an unused table.



.. rubric:: Situation


You attempt to run an ``ALTER`` command on one node.  The command takes a long time to execute.  During that period all other nodes stall leading to performance issues throughout the cluster.

What's happening is a side effect of a multi-master cluster with several appliers.  The cluster needs to control when a :abbr:`DDL (Data Definition Language)` statement ends in relation to other transactions, in order to deterministically detect conflicts and schedule parallel appliers.  Effectively, the DDL statement must execute in isolation.

Galera Cluster has a 65K window of tolerance for transactions applied in parallel, but the cluster must wait when ``ALTER`` commands take too long.



.. rubric:: Solution


Given that this is a consequence of something intrinsic to how replication works in Galera Cluster, there is no direct solution to the problem.  However, you can implement a workaround.

In the event that you can guarantee that no other session will try to modify the table `and` that there are no other :abbr:`DDL (Data Definition Language)` statements running, you can shift the schema upgrade method from :term:`Total Order Isolation` to :term:`Rolling Schema Upgrade` for the duration of the ``ALTER`` statement.  This applies the changes to each node individually, without affecting cluster performance.

To run an ``ALTER`` statement in this manner, on each node run the following queries:

#. Change the Schema Upgrade method to Rolling Schema Upgrade.

   .. code-block:: mysql

      SET wsrep_OSU_method='RSU';

#. Run the ``ALTER`` statement.


#. Reset the Schema Upgrade method back to Total Order Isolation.

   .. code-block:: mysql

      SET wsrep_OSU_method='TOI';

The cluster now runs with the desired updates.
