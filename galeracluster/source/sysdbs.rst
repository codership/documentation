################
System Databases
################
.. _`sysdb`:
.. index::
   pair: Administration; System Databases


When you install Galera Cluster, it creates a set of system databases that it uses to store configuration information.  For instance, the underlying database server uses the ``mysql`` database for system tables, which record such things as user names, passwords and what databases and tables those users can access.

.. note:: Nodes begin using the ``wsrep_schema`` database in version 4.0 of Galera Cluster.  This feature does not exist in older versions of Galera Cluster.

=====================
wsrep Schema Database
=====================
.. _`wsrep_schema_db`:
.. index::
   pair: Administration; wsrep_schema

Similar to the ``performance_schema`` and ``information_schema`` databases, the node uses ``wsrep_schema`` to store information about the state of the cluster, including the nodes that current part of the :term:`Primary Component` as well as a history of nodes that were previously in the cluster. 

You may find this information useful in diagnosing issues or in checking the state of the cluster through a monitoring solution.

.. note:: For more information on monitoring, see :doc:`monitor`.

The database contains the following tables:

- ``cluster``  Table contains the current state of the cluster.  It contains a single row:

  +------------------+----------------------------------------------+
  | Column           | Description                                  |
  +==================+==============================================+
  | ``cluster_uuid`` | Provides the current UUID of the cluster.    |
  +------------------+----------------------------------------------+
  | ``view_id``      | Provides a sequential ID that indicates the  |
  |                  | current topology of the cluster.  This value |
  |                  | increments with changes in cluster           |
  |                  | membership.                                  |
  +------------------+----------------------------------------------+

- ``members`` Table contains the current cluster membership.

  +---------------------------+------------------------------------------+
  | Column                    | Description                              |
  +===========================+==========================================+
  | ``node_uuid``             | Provides the node UUID.                  |
  +---------------------------+------------------------------------------+
  | ``cluster_uuid``          | Provides the cluster UUID.               |
  +---------------------------+------------------------------------------+
  | ``node_name``             | Provides the logical name of the node.   |
  +---------------------------+------------------------------------------+
  | ``node_incoming_address`` | Provides the node IP address and port on |
  |                           | which the node listens for incoming SQL  |
  |                           | client connections.                      |
  +---------------------------+------------------------------------------+

- ``member_history`` Table contains the complete cluster membership, including a row for every node in the current cluster as well as nodes that currently are not members.


  +---------------------------+------------------------------------------+
  | Column                    | Description                              |
  +===========================+==========================================+
  | ``node_uuid``             | Provides the node UUID.                  |
  +---------------------------+------------------------------------------+
  | ``cluster_uuid``          | Provides the cluster UUID.               |
  +---------------------------+------------------------------------------+
  | ``last_view_id``          | Provides the view ID that was in use the |
  |                           | last time the node was in the cluster.   |
  +---------------------------+------------------------------------------+
  | ``node_name``             | Provides the logical name of the node.   |
  +---------------------------+------------------------------------------+
  | ``node_incoming_address`` | Provides the node IP address and port on |
  |                           | which the node listens for incoming SQL  |
  |                           | client connections.                      |
  +---------------------------+------------------------------------------+

  If the value of the ``last_view_id`` column is less than the ``view_id`` on the ``wsrep_schema.cluster`` table, the node is currently not a part of the cluster.

You can query these tables the same as any other.  For instance,

.. code-block:: mysql

   SELECT node_name, node_incoming_address
   FROM wsrep_schema.members;

   +-----------------------+-----------------------+
   | node_name             | node_incoming_address |
   +-----------------------+-----------------------+
   | localhost.localdomain | 127.0.0.1:13000       |
   +-----------------------+-----------------------+
   | localhost.localdomain | 127.0.0.1.13004       |
   +-----------------------+-----------------------+

Would indicate that the cluster current has two nodes, both of which are running on localhost.  Alternatively, you might query ``members_history`` for a more complete membership list:

.. code-block:: mysql

   SELECT node_name, node_incoming_address, last_view_id
   FROM wsrep_schema.members_history;

   +-----------------------+-----------------------+--------------+
   | node_name             | node_incoming_address | last_view_id |
   +-----------------------+-----------------------+--------------+
   | localhost.localdomain | 127.0.0.1:13000       |            4 |
   +-----------------------+-----------------------+--------------+
   | localhost.localdomain | 127.0.0.1:13004       |            4 |
   +-----------------------+-----------------------+--------------+
   | localhost.localdomain | 127.0.0.1:13008       |            3 |
   +-----------------------+-----------------------+--------------+

Indicates that, previously, there was a third node running on localhost that is not present in the current cluster topology.  This is indicated by the ``last_view_id`` on one node being less than the others.
   
