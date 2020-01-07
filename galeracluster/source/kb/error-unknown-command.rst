.. meta::
   :title: Troubleshooting Unknown Command Errors
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

      - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
      - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
      - :ref:`wsrep_last_committed <wsrep_last_committed>`
      - :ref:`wsrep_on <wsrep_on>`
      - :ref:`wsrep_provider <wsrep_provider>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-error-unknown-command`:

=========================================
Unknown Command Errors
=========================================

.. rst-class:: article-stats

   Length: 971 words; Published: April 1, 2014; Updated: November 1, 2019; Category: Splits & Topology; Type: Troubleshooting

A frustrating situation is when you enter a valid SQL statement through the ``mysql`` client on a node, and instead of receiving the results you'd expect, you receive ``Unknown command`` errors |---| in fact,  you receive it for all queries on the node. This is because the node has lost confidence in the cluster and is thereby unwilling to execute any transactions.

.. rst-class:: section-heading
.. rubric:: Scenario

Although it's not common, when trying to execute a query using the ``mysql`` client or any other client, you may get an ```Unknown command`` error message. This may happen regardless of the query entered, each returns the same error message:

.. code-block:: mysql

   SELECT * FROM store.toys;

   ERROR: Unknown command '\\'

Generally, nodes will return ``Unknown command`` error messages if the cluster is experiencing a temporary split |---| that is to say, a portion of the nodes lose connectivity to the :term:`Primary Component`. You can confirm this by executing a ``SHOW STATUS`` statement on a node that's having this problem:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+-------------+
   | Variable_name             | Value       |
   +---------------------------+-------------+
   | wsrep_local_state_comment | Initialized |
   +---------------------------+-------------+

A value of ``Inialized`` is a weak result; ``Synced`` is preferred.  This node is not associated with the Primary Component.  The node realizes it's part of a cluster, but considers itself out-of-sync with the global state of the cluster.

This problem occurs when you have explicitly set the wsrep Provider (i.e., the :ref:`wsrep_provider <wsrep_provider>`), but the wsrep Provider rejects service.  This will happen when the node is unable to connect to the :term:`Primary Component`.  It will occur if the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter is unset.  It can also happen due to networking problems.

You can't resolve the problem by restarting the node. Nodes that were part of non-operational component, that are not part of the Primary Component, will drop any previous client connections.  Any new client connections to the nodes will receive ``Unknown command`` errors.  There isn't a more appropriate error message because MySQL and MariaDB don't have an error code for the node lacking Primary status. So it defaults to an ``Unknown command`` message.

The node will not process any SQL statements, writes or reads, except for ``SET`` and ``SHOW`` statements.  These two types of SQL statements are what's needed to resolve the problem so that the node can resynchronize with the cluster.


.. rst-class:: section-heading
.. rubric:: Work-Around

Given the above scenario, the only resolution is for nodes that are in a non-operational component, to regain network connectivity with the Primary Component. Then they can process a state transfer and be resynchronized with the cluster. Only then can they can resume normal operation and process SQL statements from clients.

There is one work-around for this situation:  You can set the :ref:`wsrep_on <wsrep_on>` variable to ``OFF``. This will have it bypass the wsrep Provider check. You can do this on the fly from the mysql client, but it would be better to do so by editing the configuration file on the problem node:

.. code-block:: text

   wsrep_on=OFF
   read_only=ON

This tells ``mysqld`` to ignore the :ref:`wsrep_provider <wsrep_provider>` setting and behave as a standard stand-alone database server.  It will disable replication, though.  Since it's not synchronizing with the other nodes, it's the same effect.  The difference is that clients will have access to the local database to execute ``SELECT`` statements.

The problem with this work-around is that the node will not only execute reads, it will process writes from clients connected to it. This can lead to data inconsistency with the other nodes whenever you're able to reconnect it to the cluster.  That's why the second line here is included: setting the ``read_only`` parameter to ON will prevent any users other than super users from being able to change data.


.. rst-class:: section-heading
.. rubric:: Solution

If you know or suspect that a cluster doesn't have a :term:`Primary Component`, you need to bootstrap a new one.  There are a couple of queries you'll need to run on each node in the cluster.

First you will need to confirm which nodes, if any, are not part of the Primary Component.  You can do this by checking the :ref:`wsrep_cluster_status <wsrep_cluster_status>` status variable.  Execute the following ``SHOW STATUS`` statement on each node:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_status';

   +----------------------+-------------+
   | Variable_name        | Value       |
   +----------------------+-------------+
   | wsrep_cluster_status | Non_primary |
   +----------------------+-------------+

If this query returns a value of ``Primary``, the node is part of the Primary Component.  If it returns any other value, it indicates the node is part of a non-operational component. In the example here, the results clearly show that it's not part of the Primary Component.

Given the scenario described above, none of the nodes will probably show ``Primary`` for the results of this SQL statement. If any nodes do, you still have a viable cluster. It's just a matter of determining what's preventing the other nodes from not connecting:  network problems, security obstructions from SELinux or the firewall, etc.

Assuming none of the nodes are part of the Primary Component, you will need restart the cluster. To prepare for this, find the sequence number of the last committed transaction on each node.  You can do this by getting the value of the :ref:`wsrep_last_committed <wsrep_last_committed>` status variable. Execute the ``SHOW STATUS`` statement on each node like this:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

You're trying to determine which node has the highest sequence number.  You can assume that that node is the most up-to-date one.  It will be the node you'll use to bootstrap a new cluster, to be the seed node with which all of the other nodes will synchronize.

On that most advanced node, execute the following ``SET`` statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

This node will now operate as the starting point in a new Primary Component.  Nodes that are part of non-operational components and have network connectivity will attempt to initiate a state transfer to bring their own databases up-to-date with this node.  At that point, the cluster will begin accepting SQL requests again.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
   - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
   - :ref:`wsrep_last_committed <wsrep_last_committed>`
   - :ref:`wsrep_on <wsrep_on>`
   - :ref:`wsrep_provider <wsrep_provider>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
