.. cssclass:: tutorial-article
.. _`testing-cluster`:

===================
Testing a Cluster
===================

.. rst-class:: list-stats

   Length:  499 words; Published: October 20, 2014; Topic: General; Level: Beginner

When you have a cluster running, you may want to test certain features to ensure that they are working properly or to prepare yourself for handling actual problems that may arise.

-------------------------------------------
Replication Testing
-------------------------------------------
.. _`Replication Testing`:

There are a few step to do to test that Galera Cluster is working as expected.  First, using the database client, verify that all nodes have connected to each other.  To do this, execute the ``SHOW STATUS`` statement like so:

 .. code-block:: mysql

    SHOW STATUS LIKE 'wsrep_%';

    +---------------------------+------------+
    | Variable_name             | Value      |
    +---------------------------+------------+
    ...
    | wsrep_local_state_comment | Synced (6) |
    | wsrep_cluster_size        | 3          |
    | wsrep_ready               | ON         |
    +---------------------------+------------+

Because of the ``LIKE`` operator, only variables beginning with ``wsrep_`` are returned.  The three variables pertinent here are the ones shown in the example above.

  - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`: The value ``Synced`` indicates that the node is connected to the cluster and operational.

  - :ref:`wsrep_cluster_size <wsrep_cluster_size>`: The numeric value returned indicates the number of nodes in the cluster.

  - :ref:`wsrep_ready <wsrep_ready>`: A value of ``ON`` indicates that this node in which the SQL statement was executed is connected to the cluster and able to handle transactions.

For the next test, try creating a table and inserting data into it. Use a database client on ``node1`` to enter these SQL statements:

 .. code-block:: mysql

 CREATE DATABASE galeratest;

 USE galeratest;

 CREATE TABLE test_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
	msg TEXT ) ENGINE=InnoDB;

 INSERT INTO test_table (msg)
	VALUES ("Hello my dear cluster.");

 INSERT INTO test_table (msg)
	VALUES ("Hello, again, cluster dear.");

These statements will create the database ``galeratest`` and the table ``test_table`` within it.  The last two SQL statements inserts data into that table.  After doing this, log into ``node2`` and check that the data was replicated correctly.  You would do this with by executing the following SQL statement on ``node2``:

 .. code-block:: mysql

 SELECT * FROM galeratest.test_table;

 +----+-----------------------------+
 | id | msg                         |
 +----+-----------------------------+
 |  1 | Hello my dear cluster.      |
 |  2 | Hello, again, cluster dear. |
 +----+-----------------------------+

The results returned  from the ``SELECT`` statement indicates that the data entered on ``node1`` was replicated on ``node2``.


-------------------------------------------
Split-Brain Testing
-------------------------------------------
.. _`Split Brain Testing`:

There are a few steps to test Galera Cluster for split-brain situations on a two-node cluster.  First, disconnect the network connection between the two nodes. At this point, the quorum will be lost and the nodes won't serve requests.

Now, reconnect the network connection.  The quorum will remain lost and the nodes still won't serve requests.

To reset the quorum, on one of the database clients, execute the following SQL statement:

 .. code-block:: mysql

 SET GLOBAL wsrep_provider_options='pc.bootstrap=1';

At this point the quorum should be reset and the cluster recovered.


--------------------
 Failure Simulation
--------------------
.. _`Failure Simulation`:

You can also test Galera Cluster by simulating various failure situations on three nodes.  To simulate a crash of a single ``mysqld`` process, execute the following from the command-line on one of the nodes:

 .. code-block:: console

    $ killall -9 mysqld

To simulate a network disconnection, use ``iptables`` or ``netem`` to block all TCP/IP traffic to a node.

To simulate an entire server crash, run each ``mysqld`` in a virtualized guest, and abrubtly terminate the entire virtual instance.

If you have three or more Galera Cluster nodes, the cluster should be able to survive the simulations.
