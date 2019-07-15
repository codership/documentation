.. meta::
   :title: Troubleshooting Unknown Command Errors
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <./index>`
         - :doc:`Best Practices <../best/index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
      - :ref:`wsrep_cluster_status <wsrep_cluster_status>`
      - :ref:`wsrep_last_committed <wsrep_last_committed>`
      - :ref:`wsrep_on <wsrep_on>`
      - :ref:`wsrep_provider <wsrep_provider>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: kb-article
.. _`kb-trouble-error-unknown-command`:

=========================================
Unknown Command Errors
=========================================

If a cluster experiences a temporary split--that is to say, a portion of the nodes loses connectivity to the :term:`Primary Component`--when they reconnect, nodes from the former non-operational component drop their client connections.  New connections to the database client will return ``Unknown command`` errors.


.. rst-class:: kb
.. rubric:: Scenario

Consider a situation in which you log into a node and try to execute a query using a database client, perhaps the ``mysql`` client.  Regardless of query you enter, each returns the same error message:

.. code-block:: mysql

   SELECT * FROM table1;

   ERROR: Unknown command '\\'

The reason for this error is that the node considers itself out-of-sync with the global state of the cluster.  It's unable to handle SQL statements except for ``SET`` and ``SHOW`` statements.

This problem occurs when you have explicitly set the wsrep Provider (i.e., the :ref:`wsrep_provider <wsrep_provider>`), but the wsrep Provider rejects service.  This will happen when the node is unable to connect to the :term:`Primary Component`.  It will occur if the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter is unset.  It can also happen due to networking problems.

Even after a disconnect node rejoins, when you receive these errors, it's because the node does not yet consider itself a part of the Primary Component.  While it has restored network connectivity, it still has to resynchronize itself with the cluster.  MySQL doesn't have an error code for the node lacking Primary status. So it defaults to an ``Unknown command`` message.


.. rst-class:: kb
.. rubric:: Work-Around

Nodes in a non-operational component must regain network connectivity with the Primary Component, process a state transfer, and catch up with the cluster before they can resume normal operation.

Using the :ref:`wsrep_on <wsrep_on>` variable dynamically, you can bypass the wsrep Provider check.  However, this disables replication.

.. code-block:: mysql

   SET wsrep_on=OFF;

This tells ``mysqld`` to ignore the :ref:`wsrep_provider <wsrep_provider>` setting and behave as a standard stand-alone database server.  Doing this can lead to data inconsistency with the rest of the cluster, but that may be the desired result for modifying the local tables.


.. rst-class:: kb
.. rubric:: Solution

If you know or suspect that a cluster doesn't have a :term:`Primary Component`, you need to bootstrap a new one.  There are a couple of queries you'll need to run on each node in the cluster.

First, confirm that the node is not part of the Primary Component by checking the :ref:`wsrep_cluster_status <wsrep_cluster_status>` status variable.  Do this by executing the following ``SHOW STATUS`` statement on each node:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cluster_status';

   +----------------------+-------------+
   | Variable_name        | Value       |
   +----------------------+-------------+
   | wsrep_cluster_status | Non_primary |
   +----------------------+-------------+

If this query returns a value of ``Primary``, the node is part of the Primary Component.  If it returns any other value, that indicates the node is part of a non-operational component.

Next, find the sequence number of the last committed transaction on each node by getting the value of the :ref:`wsrep_last_committed <wsrep_last_committed>` status variable. Do this by executing ``SHOW STATUS`` statement on each node like this:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_last_committed';

   +----------------------+--------+
   | Variable_name        | Value  |
   +----------------------+--------+
   | wsrep_last_committed | 409745 |
   +----------------------+--------+

If none of the nodes are the Primary Component, you will need to bootstrap a new one.  The node that returned the largest sequence number is the most advanced in the cluster.  On that node, run the following ``SET`` statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

The node on which you executed this will now operate as the starting point in a new Primary Component.  Nodes that are part of non-operational components and have network connectivity will attempt to initiate a state transfer to bring their own databases up-to-date with this node.  At this point, the cluster will begin accepting SQL requests.
