.. cssclass:: tutorial-article
.. _`debug-problems-with-sst`:

=============================
Debugging Problems with SST
=============================

.. rst-class:: list-stats

   Length:  985 words; Writer: Philip Stoev; Published: July 6, 2015; Topic: Troubleshooting; Level: Intermediate

Galera Cluster has the ability to add new nodes to the cluster by handling internally the transfer of the entire dataset to the new node. The same procedure, called State Snapshot Transfer (SST), applies to nodes that are rejoining the cluster after being down for a longer period of time.

A lot of operations happen during SST and there are various things that could go wrong. This article describes how to configure our server optimally for SST and how to debug any issues that arise.

---------------
The Basics
---------------

Let’s first consider all the items that play a role in the preparation and configuration of SST.

**Selecting an SST Method**

Galera Cluster supports several different methods for performing SST so, before adding a new node, it is worth examining the alternatives:

- rsync is the default method and requires the least amount of setup. Its disadvantage is that the donor node remains locked for all operations while the SST is in progress.
- mysqldump transfers the data in the form of SQL INSERT statements. Such statements can take considerable time to execute on the joining node for any non-trivial dataset size. Some measures can be applied to improve insert performance, however they do not remove the major handicap that the data is transferred row-by-row rather than file-by-file.
- xtrabackup-v2 uses the Percona XtraBackup tool to obtain a non-blocking snapshot of the donor node and then uses that snapshot to start the joining node. It is a bit more complicated to set up, but, as the donor remains mostly available for queries throughout the process, is the recommended method for any production setup where donor downtime is not acceptable.

**Third-party Dependencies**

The tools required for mysqldump are part of the mysql-wsrep-client package that is usually installed as part of the Galera Server installation. rsync uses tools that are part of the operating system distribution.

xtrabackup needs to be installed separately along with some dependencies that should be handled automatically if a package manager is used.

**TCP Ports and Firewall**

Adding a new node and performing SST can involve several TCP ports. Make sure every node can talk to every other node on the following ports: 3306, 4567, 4568, 4444.

**Network Capacity**

Make sure the network connectivity is good enough to transfer the entire data set in a reasonable amount of time. Even if your cluster has been operating fine under a low write load with a narrow network pipe, sending a large data set over the wire will use quite a bit of bandwidth.

Since it is the data directory that is being transferred under the rsync and xtrabackup-v2 SST methods, you can check the size of the directory to get an idea on how much time the SST will take.

Xtrabackup supports compact snapshots that do not include secondary indexes and would consume less bandwidth. However, the indexes will need to be recreated after the data transfer, which may take a while.

**SQL Permissions**

Xtrabackup and mysqldump require an SQL user to be created on the cluster. Once you create it, you need to set the username and the password in the wsrep_sst_auth variable, separated by a semicolon.

The user needs to have full root permissions for the entire database are required for mysqldump SST. For xtrabackup SST, the following permissions are required.

**Selecting a Donor Node**

By default, Galera Cluster can select any operational node to serve as a donor node. It is possible to select a specific node by setting the wsrep_sst_donor variable.

For a geo-distributed cluster, appropriately setting the gmcast.segment wsrep_provider_option on each node will cause Galera to prefer donor nodes from the same segment as the joining node, avoiding cross-datacenter traffic.

**Encryption**

If you have any security considerations and the SST data will travel over an untrusted link, such as the public Internet between two data centers, note that setting ``socket.ssl_key`` and ``socket.ssl_cert`` in ``wsrep_provider_options`` will not cause data sent during SST to be encrypted.

Encrypting the SST is different for each method:

- For xtrabackup-v2 you can use a shared secret or a a key.
- For mysqldump you need to set up SSL client connections and set up your MySQL configuration file’s [client] section so that mysqldump uses SSL by default.

End-to-end encryption via VPN can also be used. Tunnelling individual ports over SSH would be more complicated as more than one TCP port may be used during the process.

----------------------
Debugging SST Errors
----------------------

SST is a complex process that internally involves running scripts and calling third-party binaries, so there are various opportunities for a failure.
The first step when debugging is to examine the MySQL error logs, and you should look at the logs from both the joining node and the donor node in order to figure out what is going on. Both nodes participate equally in the process, so an error could happen on either side.

**Xtrabackup Errors**

In addition to writing diagnostics information to the MySQL error log, xtrabackup SST also writes the entire output from the utility into the following log files:

- on the joining node: ``innobackup.prepare.log`` and ``innobackup.move.log``
- on the donor node: ``innobackup.backup.log``

Those log files are located in the data directory and should all end with the string completed OK! if the particular phase of SST was successful. If a log file does not end that way, there should be some error condition reported in that log file.

**Rsync Errors**

Rsync errors will be written to the MySQL error log. A frequent problem is the rsync ports being in use or a hanging rsync process. Clean up any stale rsync processes before attempting to start the joining node again.

**mysqldump Errors**

Mysqldump errors will be written to the MySQL error log. Authentication and permission errors are the ones most frequently encountered, so make sure that the user you have specified part of the wsrep_sst_auth variable (the user name is the portion of the value that is before the semicolon) exists, has full rights to the entire server and can be connected using the password (which is the second part of the value).
