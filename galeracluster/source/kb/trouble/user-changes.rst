======================================
User Changes not Replicating
======================================
.. _`kb-trouble-user-changes`:

Galera replicates only InnoDB tables.  Therefore, databases should not use other storage engines.  However, the system tables contained in the ``mysql`` database use the MyISAM storage engine. This includes the ``user`` table and other tables containing user permissions.  Since these tables are not replicated, you must make changes to them manually on each node.


.. rubric:: Scenario
   :class: kb

Suppose you have made some changes to database users, but when you check the other nodes, you find they have not replicated to the cluster. For instance, suppose you want to change the host address from which a user, *Bob* may access the cluster.  Suppose further that you had logged into a node and use an ``UPDATE`` statement to update the ``mysql.user`` table.

.. code-block:: mysql

   UPDATE mysql.user (User,Host, Password)
   SET Host = '127.0.12.34'
   WHERE User = 'Bob' AND Host = '127.0.56.78';

   FLUSH PRIVILEGES;

When finished, you ask the user to log in from the new host.  They attempt to connect to the cluster, but through a different host. He cannot log in and he is given this error message:

.. code-block:: mysql

   Enter password:
   ERROR 1045 (28000): Access denied for user 'bob'@'localhost'
   (using password: YES)

You then tell him to log into the cluster through the same node through which  you made the update.  He is then successful. This means you had the correct IP address and he used the correct password. The problem is that the change didn't replicate to the other nodes because you used the wrong SQL statement to make this change.


.. rubric:: Solution
   :class: kb

While direct modifications to the system tables do not replicate, :abbr:`DDL (Data Definition Language)` statements replicate at the statement level.  Meaning, changes made to the system tables in this manner are made to the entire cluster.

Therefore, to make changes to the ``mysql.user`` table, use statements like  ``CREATE USER``, ``RENAME USER`` ``DROP USER``. And use the ``GRANT`` statement to set user privileges.  So instead of using the ``UPDATE`` statement in the previous example, you should have used the ``RENAME USER`` statement like so:

.. code-block:: mysql

   RENAME USER 'bob'@'127.0.12.34'
   TO 'bob'@'127.0.56.78';

This change the host address for the user in a way that replicates through the cluster.  The user may now access the database from the given IP address through any node in the cluster.


.. rubric:: Additional Information
   :class: kb


For more information related to this KB article, see the following documents:

- :doc:`Migration <../../documentation/migration>`
