.. meta::
   :title: AUTO_INCREMENT Increases by Multiples
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :ref:`wsrep_debug <wsrep_debug>`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-auto-increment-multiples`:

=======================================
AUTO_INCREMENT Increasing by Multiples
=======================================

.. rst-class:: article-stats

   Length: 995 words; Published: October 22, 2019; Category: Schema & SQL; Type: Troubleshooting

The numeric value of a column which is a key index and uses the ``AUTO_INCREMENT`` attribute, will be increased automatically. Normally, it's increased by a factor of one.  So, for the first row, the key auto_increment column should have a value of 1, the second a value of 2, and the third a value of 3.

However, when using Galera, an auto_increment column will increase by a greater amount.  This isn't a problem, but it's something you need to understand and it's something of which you need to be aware.


.. rst-class:: section-heading
.. rubric:: Scenario

Suppose we're developing a database for a store which sells many things, including toys.  Related to this, we decide to create a simple table called, ``toys``. Our intention is to store a list of toys that we sell, including how many we have in stock and the prices.

Below is a description of this new table:

.. code-block:: mysql

   DESC toys;

   +----------+--------------+------+-----+---------+----------------+
   | Field    | Type         | Null | Key | Default | Extra          |
   +----------+--------------+------+-----+---------+----------------+
   | toy_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
   | toy_name | char(25)     | NO   |     |         |                |
   | quantity | int(11)      | NO   |     | 0       |                |
   | price    | decimal(6,2) | NO   |     | 0.00    |                |
   +----------+--------------+------+-----+---------+----------------+

As you can see, the first column, called ``toy_id``, uses auto_increment.  Let's see what happens when three rows of data are inserted into the table.  Keep in mind that this is a new table which has never contained data.

.. code-block:: mysql

   INSERT INTO toys
   VALUES(NULL, 'Baseball', 12, 6.15),
   (NULL, 'Frisbee', 6, 12.45),
   (NULL, 'Slinky', 8, 6.95);

   SELECT * FROM toys;

   +--------+----------+----------+-------+
   | toy_id | toy_name | quantity | price |
   +--------+----------+----------+-------+
   |      3 | Baseball |       12 |  6.15 |
   |      6 | Frisbee  |        6 | 12.45 |
   |      9 | Slinky   |        8 |  6.95 |
   +--------+----------+----------+-------+

Look at the values for the ``toy_id`` column. Instead of having values of 1, 2, 3, they have values of 3, 6, 9. They're incrementing by a factor of three.  The first time encountering this, it may seem to be a problem, possibly a bug in the software.  It's not.  It's intentional, by design.


.. rst-class:: section-heading
.. rubric:: Explanation

In a Galera Cluster, all nodes may write data to the tables.  Imagine a situation in which all nodes in the cluster simultaneously try to insert rows in the same table at the same time.  The result could potentially be duplicate values for any columns which use auto_increment.  To avoid such conflicts, Galera increments values for the columns based on the number of nodes in the cluster.

Let's see how many there in the cluster we're using.  We would enter the following SQL statement to get the number of nodes in the cluster:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_size';

   +--------------------+-------+
   | Variable_name      | Value |
   +--------------------+-------+
   | wsrep_cluster_size | 3     |
   +--------------------+-------+

There are three nodes. This explains why the ``toy_id`` column is incrementing 3 at a time. It doesn't explain why the first three rows didn't have values of 1, 4, and 7.  The reason for that is each node has a different starting point.  The node on which the ``INSERT`` statement above was entered, happened to have been the third node to join the cluster.  Let's get a list of variables related to auto_increment.  It'll make more sense.

.. code-block:: mysql

   SHOW VARIABLES LIKE '%auto_increment_%';

   +------------------------------+-------+
   | Variable_name                | Value |
   +------------------------------+-------+
   | auto_increment_increment     | 3     |
   | auto_increment_offset        | 3     |
   | wsrep_auto_increment_control | ON    |
   +------------------------------+-------+

The ``auto_increment_increment`` variable indicates that the node is set to increase any auto_increment field by a factor of 3. The ``auto_increment_offset`` variables provides it's starting point from the value of the last row inserted. Notice that ``wsrep_auto_increment_control`` is enabled. This feature is what adjusts these other two variables based on the number of nodes in the cluster. If a node leaves the cluster, it will adjust them accordingly.


If we were to get the ``AUTO_INCREMENT`` value on each of the three nodes for the ``toys`` table, the value would be different for each.  Below shows the results for the initial node in the cluster:

.. code-block:: mysql

   SELECT AUTO_INCREMENT
   FROM INFORMATION_SCHEMA.TABLES
   WHERE TABLE_SCHEMA = 'store'
   AND TABLE_NAME = 'toys';

   +----------------+
   | AUTO_INCREMENT |
   +----------------+
   |             10 |
   +----------------+

The value of the second node in the cluster is 11; for the third it's 12. These values are set as the starting point for each column, the value that will be given to the next row entered from each respective node. With these starting points in mind, let's look at the auto_increment system variables on the node which started the cluster:

.. code-block:: mysql

   SHOW VARIABLES LIKE '%auto_increment_%';

   +------------------------------+-------+
   | Variable_name                | Value |
   +------------------------------+-------+
   | auto_increment_increment     | 3     |
   | auto_increment_offset        | 1     |
   | wsrep_auto_increment_control | ON    |
   +------------------------------+-------+

You can see here that the auto_increment_offset on this node differs from the third node in the cluster.  On the second node in the cluster, it has a value of 2.

Let's add three more rows to the table, but this time from the first node:

.. code-block:: mysql

   INSERT INTO toys
   VALUES(NULL, 'Ping Pong Paddle', 4, 18.95),
   (NULL, 'Gumby & Pokey', 3, 10.25),
   (NULL, 'Etch-A-Sketch', 2, 14.25);

   SELECT * FROM toys;

   +--------+------------------+----------+-------+
   | toy_id | toy_name         | quantity | price |
   +--------+------------------+----------+-------+
   |      3 | Baseball         |       12 |  6.15 |
   |      6 | Frisbee          |        6 | 12.45 |
   |      9 | Slinky           |        8 |  6.95 |
   |     10 | Ping Pong Paddle |        4 | 18.95 |
   |     13 | Gumby & Pokey    |        3 | 10.25 |
   |     16 | Etch-A-Sketch    |        2 | 14.25 |
   +--------+------------------+----------+-------+

Notice that the first new row has a ``toy_id`` of 10, which matches the ``AUTO_INCREMENT`` value for the table.  For the next row, it jumps to 13, and then 16.  It doesn't have the symetry of the results of the first ``INSERT`` statement, but it's logical.

Let's insert two more rows, but on the second node:

.. code-block:: mysql

   INSERT INTO toys
   VALUES(NULL, 'Tonka Dump Truck', 2, 24.95),
   (NULL, 'Airport Playset', 1, 18.95);

   SELECT * FROM toys LIMIT 6, 2;

   +--------+------------------+----------+-------+
   | toy_id | toy_name         | quantity | price |
   +--------+------------------+----------+-------+
   |     17 | Tonka Dump Truck |        2 | 24.95 |
   |     20 | Airport Playset  |        1 | 18.95 |
   +--------+------------------+----------+-------+


To save space, we used the ``LIMIT`` clause to select the last two rows, the two new rows inserted.  As you can see, the second node used the next ``toy_id`` in the sequence (i.e., 17) and then just three just in case the other two nodes were inserting rows.

The result of setting the value of ``auto_increment_increment`` to the number of nodes, and the ``auto_increment_offset`` from 1 to the number of nodes, is that there will be no conflicts between the nodes.  Just don't manually change the value of these two variables or use ``ALTER TABLE`` to change the value of AUTO_INCREMENT for any table.  That would cause problems.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_debug <wsrep_debug>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
