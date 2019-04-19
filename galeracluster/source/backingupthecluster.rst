=========================
 Backing Up Cluster Data
=========================
.. _`backing-up-cluster-data`:

.. index::
   pair: Logs; mysqld error log
.. index::
   pair: Parameters; gmcast.listen_addr
.. index::
   pair: Parameters; wsrep_cluster_name
.. index::
   pair: Parameters; wsrep_node_name
.. index::
   single: Galera Arbitrator

You can perform backups with Galera Cluster at the same regularity as with a standard database server, using a backup script.  Since replication ensures that all nodes have the exact same data, running a backup script on one node will backup the data on all nodes in the cluster.

The problem with such a simple backup method, though, is that it lacks a :term:`Global Transaction ID` (GTID).  You can use backups of this kind to recover data, but they are insufficient for use in recovering nodes to a well-defined state.  Furthermore, some backup procedures can block cluster operations during the backup.

Getting backups with the associated Global Transaction ID requires a different approach.

----------------------------------
State Snapshot Transfer as Backup
----------------------------------
.. _`sst-backup`:

Taking a full data backup is very similar to node provisioning through a :term:`State Snapshot Transfer`.  In both cases, the node creates a full copy of the database contents, using the same mechanism to associate a :term:`Global Transaction ID` with the database state. Invoking backups through the state snapshot transfer mechanism has the following benefits:

- The node initiates the backup at a well-defined point.
- The node associates a Global Transaction ID with the backup.
- The node desyncs from the cluster to avoid throttling performance while making the backup, even if the backup process blocks the node.
- The cluster knows that the node is performing a backup and won't choose the node as a donor for another node.

In order to use this method for backups, you will need to use a script that implements both your preferred backup procedure and the Galera Arbitrator daemon, triggering it in a manner similar to a state snapshot transfer. You would execute such a script from the command-line like this:

.. code-block:: console
		
   $ garbd --address gcomm://192.168.1.2?gmcast.listen_addr=tcp://0.0.0.0:4444 \
     --group example_cluster --donor example_donor --sst backup

This command triggers donor node to invoke a script with the name ``wsrep_sst_backup.sh``, which it looks for in the ``PATH`` for the ``mysqld`` process.  When the donor reaches a well-defined point, a point where no changes are happening to the database, it runs the backup script passing the GTID corresponding to the current database state.

.. note:: In the command, '``?gmcast.listen_addr=tcp://0.0.0.0:4444``' is an arbitrary listen socket address that Galera Arbitrator opens to communicate with the cluster.  You only need to specify this in the event that the default socket address (i.e., ``0.0.0.0:4567`` is busy).

.. note:: **See Also**: You may find it useful to create your backup script using a modified version of the standard state snapshot transfer script.  For information on scripts of this kind, see :doc:`scriptablesst`.
