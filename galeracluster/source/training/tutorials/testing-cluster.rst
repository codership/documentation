.. meta::
   :title: Testing a Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`
      - :ref:`search`

      Related Documents

      - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`
      - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
      - :ref:`wsrep_ready <wsrep_ready>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`testing-cluster`:

===================
Testing a Cluster
===================

.. rst-class:: article-stats

   Length:  499 words; Published: October 20, 2014; Topic: General; Level: Beginner

When you have a cluster running, you may want to test certain features, to ensure that they are working properly or to prepare yourself for handling actual problems that may arise.


.. _`Replication Testing`:
.. rst-class:: section-heading
.. rubric:: Replication Testing

With these steps, you can test that your Galera Cluster is working as expected. First, using the database client, verify that all nodes have connected to each other. To do this, execute the ``SHOW STATUS`` statement as shown below:

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

Because of the ``LIKE`` operator, only variables beginning with ``wsrep_`` are returned. The three variables pertinent here are the ones shown in the example above.

  - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`: The ``Synced`` value indicates that the node is connected to the cluster and operational.

  - :ref:`wsrep_cluster_size <wsrep_cluster_size>`: The numeric value returned indicates the number of nodes in the cluster.

  - :ref:`wsrep_ready <wsrep_ready>`: A value of ``ON`` indicates that this node, in which the SQL statement was executed, is connected to the cluster and able to handle transactions.

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

These statements will create a ``galeratest`` database and a ``test_table`` table within it. The last two SQL statements insert data into that table. After doing this, log into ``node2`` and check that the data was correctly replicated. You would do this with by executing the following SQL statement on ``node2``:

 .. code-block:: mysql

   SELECT * FROM galeratest.test_table;

   +----+-----------------------------+
   | id | msg                         |
   +----+-----------------------------+
   |  1 | Hello my dear cluster.     |
   |  2 | Hello, again, cluster dear. |
   +----+-----------------------------+

The results returned  from the ``SELECT`` statement indicate that the data entered on ``node1`` was replicated on ``node2``.


.. _`Split Brain Testing`:
.. rst-class:: section-heading
.. rubric:: Split-Brain Testing

There are a few steps to test Galera Cluster for split-brain situations on a two-node cluster. First, disconnect the network connection between the two nodes. At this point, the :term:`Quorum` will be lost and the nodes will not serve requests.

Now, reconnect the network connection. The quorum will remain lost and the nodes still will not serve requests.

To reset the quorum, execute the following SQL statement on one of the database clients:

 .. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=1';

At this point, the quorum should be reset and the cluster recovered.


.. _`Failure Simulation`:
.. rst-class:: section-heading
.. rubric:: Failure Simulation

You can also test Galera Cluster by simulating various failure situations on three nodes. To simulate a crash of a single ``mysqld`` process, execute the following command from the command-line on one of the nodes:

 .. code-block:: console

    $ killall -9 mysqld

To simulate a network disconnection, use ``iptables`` or ``netem`` to block all TCP/IP traffic to a node.

To simulate an entire server crash, run each ``mysqld`` in a virtualized guest, and abruptly terminate the entire virtual instance.

If you have three or more Galera Cluster nodes, the cluster should be able to survive the simulations.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_local_state_comment <wsrep_local_state_comment>`
   - :ref:`wsrep_cluster_size <wsrep_cluster_size>`
   - :ref:`wsrep_ready <wsrep_ready>`
