.. cssclass:: kb-list
.. _`kb-trouble`:

===================================
Codership Troubleshooting Articles
===================================

This is the Troubleshooting section of the Galera Knowledge Base (KB). It contains information on resolving problems you might experience with Galera Cluster. It includes articles on how to diagnose and address various performance and replication trouble. For articles related to performance and other ways to improve usage of Galera Cluster, see the :doc:` Best Practices <../best/index>` section of the KB.


.. rubric:: :doc:`Cluster Stalls on ALTER <stall-on-alter>`
   :class: list-sub-header

.. rst-class:: list-abstract

   There may be times in which a cluster will stall when an ``ALTER`` statement is executed on an unused table.


.. rubric:: :doc:`Commit Failed for Reason 3 <commit-failed-reason-3>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When you have ``wsrep_debug`` enabled, you may occasionally see a message noting that a commit has failed due to reason ``3``.


.. rubric:: :doc:`Multi-Master Conflicts <multi-master-conflicts>`
   :class: list-sub-header

.. rst-class:: list-abstract

   These types of conflicts relate to multi-master database environments and typically involve inconsistencies of row amongst nodes.


.. rubric:: :doc:`Node Crashes during rsync SST <node-crash-rsync>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a State Snapshot Transfer (SST) method to provide a full data copy to the new node, known as the joiner.  This should work well, but it doesn't always.


.. rubric:: :doc:`Requested State Transfer Failed <requested-state-transfer-failed>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When a new node joins a cluster, it will try to synchronize with the cluster by getting a full copy of the databases from one of the other nodes.  Sometimes this will fail.


.. rubric:: :doc:`SQL Syntax Errors <sql-syntax-error>`
   :class: list-sub-header

.. rst-class:: list-abstract

   When a new node joins a cluster, it will request data from the cluster.  One node, known as a donor, will use a State Snapshot Transfer (SST) method to provide a full data copy to the new node, known as the joiner. To get this snapshot, some administrators opt to use a Logical State Transfer Method, in particular ``mysqldump``. This doesn't always work well.


.. rubric:: :doc:`Unknown Command Errors <error-unknown-command>`
   :class: list-sub-header

.. rst-class:: list-abstract

   If a cluster experiences a temporary split--that is to say, a portion of the nodes loses connectivity to the Primary Component--when they reconnect, nodes from the former non-operational component drop their client connections.  New connections to the database client will return ``Unknown command`` errors.


.. rubric:: :doc:`User Changes not Replicating <user-changes>`
   :class: list-sub-header

.. rst-class:: list-abstract

   Galera replicates only InnoDB tables.  Therefore, databases should not use other storage engines.  However, the system tables contained in the ``mysql`` database use the MyISAM storage engine. This includes the ``user`` table and other tables containing user permissions.  Since these tables are not replicated, you must make changes to them manually on each node.


.. toctree::
   :hidden:
   :maxdepth: 1

   stall-on-alter
   commit-failed-reason-3
   multi-master-conflicts
   node-crash-rsync
   requested-state-transfer-failed
   sql-syntax-error
   error-unknown-command
   user-changes


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
