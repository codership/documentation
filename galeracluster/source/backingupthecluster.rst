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

You can perform backups with Galera Cluster at the same regularity as with the standard MySQL server, using a backup script.  Given that replication ensures that all nodes carry the same data, running the script on one node backs up the data on all nodes in the cluster.

The problem with such backups is that they lack a :term:`Global Transaction ID`.  You can use backups of this kind to recover data, but they are insufficient for use in recovering nodes to a well-defined state.  Furthermore, some backup procedures can block cluster operations for the duration of the backup.

Getting backups with the associated :term:`Global Transaction ID` requires a different approach.

---------------------------------
State Snapshot Transfer as Backup
---------------------------------

.. _`sst-backup`:

It is easy to see that taking a full data backup is not very different from provisioning a new node via :term:`State Snapshot Transfer (SST)`: in both cases we make a full copy of database contents. So one can use the same mechanism to associate a :term:`Global Transaction ID` (GTID) with your data backups that we use for SST.

For that one needs an SST script that implements the backup procedure of choice and the Galera Arbitrator daemon, to trigger it in a manner similar to SST.

For example,

.. code-block:: console

   $ garbd --address gcomm://192.168.1.2?gmcast.listen_addr=tcp://0.0.0.0:4444 \
     --group example_cluster --donor example_donor --sst backup

When this command runs, it triggers the "donor" node to invoke **wsrep_sst_backup** script (must be in the PATH of ``mysqld`` process) at a well defined point (no changes are happening to the database) and pass the GTID corresponding to the current database state to it. A good starting point to create a backup script would be to modify one of the existing SST scripts.

Invoking backups through SST mechanism has the following benefits:
 #. Backup is initiated at a well defined point and can have a GTID associated with it.
 #. The node knows that it is performing a backup, so it desyncs itself from the cluster and does not throttle cluster performance even if backup is of a blocking nature.
 #. The cluster knows that the node is performing a backup, so it won't be chosen as a donor for another node.

In the command, ``?gmcast.listen_addr=tcp://0.0.0.0:4444`` is an arbitrary listen socket address that the Galera Arbitrator opens to communicate with the cluster.  You only need to specify this in the event that the default socket address, (that is, ``0.0.0.0:4567``), is busy.

.. note:: When you run the **garbd** script, it may exit immediately with confusing diagnostics, even after it manages a successful state snapshot transfer request.  This is not a failure.  The donor **mysqld** still runs the backup script.  You can monitor it's progress through the error and script logs on the donor machine.


