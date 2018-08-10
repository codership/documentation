======================================
User Changes not Replicating
======================================
.. _`user-changes-not-replicating`:

User changes do not replicate to the cluster.


.. rubric:: Situation

You have made some changes to database users, but on inspection find that these changes are only present on the node in which you made them and have not replicated to the cluster.

For instance, say that you want to add a new user to your cluster.  You log into a node and use an ``INSERT`` statement to update the ``mysql.user`` table.

.. code-block:: mysql

   INSERT INTO mysql.user (User,Host, Password)
      VALUES ('user1','localhost', password('my_password'));

When finished, you check your work by running a ``SELECT`` query, to make sure that ``user1`` does in fact exist on the node:

.. code-block:: mysql

   SELECT User, Host, Password FROM mysql.user WHERE User='user1';

   +-------+-------------+-------------------------------------------+
   | User  | Host        | Password                                  |
   +-------+-------------+-------------------------------------------+
   | user1 | localhost   | *00A60C0186D8740829671225B7F5694EA5C08EF5 |
   +-------+-------------+-------------------------------------------+

This checks out fine. However, when you run the same query on a different node, you receive different results:

.. code-block:: mysql

   SELECT User, Host, Password FROM mysql.user WHERE User='user1';

   Empty set (0.00 sec)

The changes you made to the ``mysql.user`` table on the first node do not replicate to the others.  The new user you created can only function when accessing the database on the node where you created it.

Replication currently only works with the InnoDB and XtraDB storage engines.  Multi-master replication cannot support non-transactional storage engines, such as MyISAM.  Writes made to tables that use non-transactional storage engines do not replicate.

The system tables use MyISAM.  This means that any changes you make to the system tables directly, such as in the above example with an ``INSERT`` statement, remain on the node in which they were issued.




.. rubric:: Solution


While direct modifications to the system tables do not replicate, :abbr:`DDL (Data Definition Language)` statements replicate at the statement level.  Meaning, changes made to the system tables in this manner are made to the entire cluster.

For instance, consider the above example where you added a user to node.  If instead of ``INSERT`` you used ``CREATE USER`` or ``GRANT`` you would get very different results:

.. code-block:: mysql

   CREATE USER user1 IDENTIFIED BY 'my_password';

This creates ``user1`` in a way that replicates through the cluster.  If you run ``SELECT`` query to check the ``mysql.user`` table on any node, it returns the same results:

.. code-block:: mysql

   SELECT User, Host, Password FROM mysql.user WHERE User='user1';

   +-------+-------------+-------------------------------------------+
   | User  | Host        | Password                                  |
   +-------+-------------+-------------------------------------------+
   | user1 | localhost   | *00A60C0186D8740829671225B7F5694EA5C08EF5 |
   +-------+-------------+-------------------------------------------+

You can now ``user1`` on any node in the cluster.
