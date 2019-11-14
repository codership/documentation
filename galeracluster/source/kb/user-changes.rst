.. meta::
   :title: User Changes not Replicating in Galera
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


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

      - :doc:`Migration <../../training/tutorials/migration>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-user-changes`:

=============================
User Changes not Replicating
=============================

.. rst-class:: article-stats

   Length: 518 words; Published: April 1, 2014; Updated: September 12, 2019; Category: Schema & SQL; Type: Troubleshooting

When a DBA make changes to data in the mysql database |---| that's the database that contains user names and privileges |---| if done in a straightforward way (e.g., with an ``UPDATE`` statement), they're not replicated to the other nodes in the cluster. This can cause problems for users, as well as frustrate the DBA.

.. rst-class:: section-heading
.. rubric:: Scenario

Suppose you made some changes to database users, but when you check the other nodes, you find they have not replicated to the cluster. For instance, suppose you want to change the host address from which a user, *bob* may access the cluster. You log into a node and use the ``UPDATE`` statement to change the ``Host`` column in the ``mysql.user`` table for Bob.

.. code-block:: mysql

   UPDATE mysql.user
   SET Host = '12.0.12.34'
   WHERE User = 'bob'
   AND Host = '12.0.56.78';

   FLUSH PRIVILEGES;

When that's finished, you ask Bob to log in from the new host.  He tries to connect to the cluster, but through a different node than the one on which you entered the update. He can't log in, even thought his local IP address is ``12.0.56.78``.  He gets this error message:

.. code-block:: mysql

   Enter password:
   ERROR 1045 (28000): Access denied
     for user 'bob'@'12.0.56.78'
     (using password: YES)

You then tell him to log into the cluster through the same node through which you made the update.  He is then successful. The problem is that the change to the ``user`` table didn't replicate to the other nodes.

Galera replicates only InnoDB tables.  Therefore, any tables you create should not use other storage engines.  However, the system tables contained in the ``mysql`` database use the MyISAM storage engine. This includes the ``user`` table.

Since these tables are not replicated, you shouldn't change them directly by using SQL statements like ``INSERT``, ``UPDATE``, or ``DELETE``.  Instead, you have to use SQL statements like ``CREATE USER``, ``RENAME USER``, ``DROP USER``, and ``GRANT``. If you have difficulty remembering or are unsure which you may not use, just remember that if you have to execute ``FLUSH PRIVILEGES`` for the change to take effect, you're changing the data directly and it won't be replicated.


.. rst-class:: section-heading
.. rubric:: Solution

While direct modifications to the system tables do not replicate, you may use :abbr:`DDL (Data Definition Language)` statements replicate at the statement level.  Changes made to the system tables in this manner will be made to the entire cluster.

Therefore, to make changes to the ``mysql.user`` table, use statements like  ``CREATE USER``, ``RENAME USER`` ``DROP USER``. And use the ``GRANT`` statement to set user privileges.  So instead of using the ``UPDATE`` statement in the previous example, you should have used the ``RENAME USER`` statement like so:

.. code-block:: mysql

   RENAME USER 'bob'@'127.0.12.34'
   TO 'bob'@'127.0.56.78';

This change the host address for the user in a way that will replicate through the cluster.  The user may now access the database from the given IP address through any node in the cluster.

If you have a need to change something directly using a statement such as ``UPDATE``, to circumvent the usual methods, you must execute the statement on each node, including ``FLUSH PRIVILEGES``.

.. container:: bottom-links

   Related Documents

   - :doc:`Migration <../../training/tutorials/migration>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
