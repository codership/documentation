.. meta::
   :title: Upgrading a Schema in Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, schema, alter, upgrade
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :ref:`Total Order Isolation <toi>`
      - :ref:`Rolling Schema Upgrade <rsu>`
	  - :ref:`Non-Blocking Operations <nbo>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`schema-upgrades`:

=================
Schema Upgrades
=================

Schema changes are of particular interest related to Galara Cluster. Schema changes are  :abbr:`DDL (Data Definition Language)` statement executed on a database (for example, ``CREATE TABLE``, ``GRANT``). These :abbr:`DDL (Data Definition Language)` statements change the database itself and are non-transactional.

Galera Cluster processes schema changes by three different methods:

- :ref:`Total Order Isolation <toi>`: Abbreviated as TOI, these are schema changes made on all cluster nodes in the same total order sequence, preventing other transactions from committing for the duration of the operation.

- :ref:`Rolling Schema Upgrade <rsu>` Known also as RSU, these are schema changes run locally, affecting only the node on which they are run. The changes do not replicate to the rest of the cluster.

- :ref:`Non-Blocking Operations <nbo>`: Abbreviated as NBO, these are schema changes made on all cluster nodes in the same total order sequence, preventing other transactions from committing for the duration of the operation, with much more efficient locking strategy that the TOI method.

You can set the method for online schema changes by using the ``wsrep_OSU_method`` parameter in the configuration file, (``my.ini`` or ``my.cnf`, depending on your build) or through the ``mysql`` client. Galera Cluster defaults to the Total Order Isolation method.

.. note:: If you are using Galera Cluster for Percona XtraDB Cluster, see the the `pt-online-schema-change <https://www.percona.com/doc/percona-toolkit/3.0/pt-online-schema-change.html>`_ in the Percona Toolkit.

.. only:: html

          .. image:: ../images/support.jpg
             :target: https://galeracluster.com/support/#galera-cluster-support-subscription
             :width: 740

   .. only:: latex

          .. image:: ../images/support.jpg
		  :target: https://galeracluster.com/support/#galera-cluster-support-subscription


.. _`toi`:
.. rst-class:: section-heading
.. rubric:: Total Order Isolation

.. index::
   pair: Descriptions; Total Order Isolation

When you want an online schema change to replicate through the cluster and do not care that other transactions will be blocked while the cluster processes the :abbr:`DDL (Data Definition Language)` statements, use the :term:`Total Order Isolation` method. You can do this with a global ``SET`` statement, as follows:

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='TOI';

The GLOBAL command does not change the "wsrep_OSU_method" for the running session. If you want to change it for the running session, use the session-based ``SET`` statement, as follows:

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='TOI';


In Total Order Isolation, queries that change the schema replicate as statements to all nodes in the cluster. The nodes wait for all preceding transactions to commit simultaneously, then they execute the schema change in isolation. For the duration of the :abbr:`DDL (Data Definition Language)` processing, no other transactions can commit.

The main advantage of Total Order Isolation is its simplicity and predictability, which guarantees data consistency. Additionally, when using Total Order Isolation, you should take the following particularities into consideration:

- From the perspective of certification, schema upgrades in Total Order Isolation never conflict with preceding transactions, given that they only execute after the cluster commits all preceding transactions. What this means is that the certification interval for schema changes using this method has a zero length. Therefore, schema changes will never fail certification and their execution is guaranteed.

- Transactions that were in progress while the DDL was running and that involved the same database resource will get a deadlock error at commit time and will be rolled back.

- The cluster replicates the schema change query as a statement before its execution. There is no way to know whether or not individual nodes succeed in processing the query. This prevents error checking on schema changes in Total Order Isolation.


.. _`rsu`:
.. rst-class:: section-heading
.. rubric:: Rolling Schema Upgrade

.. index::
   pair: Descriptions; Rolling Schema Upgrade
.. index::
   pair: Parameters; wsrep_OSU_method

When you want to maintain high-availability during schema upgrades and can avoid conflicts between new and old schema definitions, use the :term:`Rolling Schema Upgrade` method. You can do this with a global ``SET`` statement, as follows:

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='RSU';

The GLOBAL command does not change the "wsrep_OSU_method" for the running session. If you want to change it for the running session, use the session-based ``SET`` statement, as follows:

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='RSU';

In Rolling Schema Upgrade, queries that change the schema are only processed on the local node. While the node processes the schema change, it desynchronizes with the cluster. When it finishes processing the schema change, it applies delayed replication events and synchronizes itself with the cluster.

To change a schema cluster-wide, you must manually execute the query on each node in turn. Bear in mind that during a rolling schema change the cluster continues to operate, with some nodes using the old schema structure while others use the new schema structure.

The main advantage of the Rolling Schema Upgrade is that it only blocks one node at a time. The main disadvantage of the Rolling Schema Upgrade is that it is potentially unsafe, and may fail if the new and old schema definitions are incompatible at the replication event level.

.. _`nbo`:
.. rst-class:: section-heading
.. rubric:: Non-Blocking Operations (this feature is part of Galera Cluster Enterprise Edition)

.. index::
   pair: Descriptions; Non-Blocking Operations

When you want an online schema change to replicate through the cluster, but are worried that long-running :abbr:`DDL (Data Definition Language)` statements block cluster updates, use the :term:`Non-Blocking Operations` method. You can do this with a global ``SET`` statement, as follows:

.. code-block:: mysql

   SET GLOBAL wsrep_OSU_method='NBO';

The GLOBAL command does not change the "wsrep_OSU_method" for the running session. If you want to change it for the running session, use the session-based ``SET`` statement, as follows:

.. code-block:: mysql

   SET SESSION wsrep_OSU_method='NBO';

The NBO method resembles the TOI method. Queries that change the schema replicate as statements to all nodes in the cluster. The nodes wait for all preceding transactions to commit simultaneously, then they execute the schema change in isolation. For the duration of the :abbr:`DDL (Data Definition Language)` processing, no other transactions can commit.

The main advantage of Non-Blocking Operations is that it significantly reduces the impact of DDL statements on the cluster. During DDL processing:

   - You can alter another table, using NBO
   - You can continue inserting data, excluding the table(s) you are altering
   - If one node crashes, the operation will continue on the other nodes, and if successful it will persist

When using Non-Blocking Operations, take the following particularities into consideration:

- The supported statements are:

   - ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE} , alter_specification``
   - ``ALTER TABLE table_name LOCK = {SHARED|EXCLUSIVE} PARTITION``. The comma after ``LOCK=SHARED|EXCLUSIVE`` is not used for partition-management ``ALTER``\s.
   - ``ANALYZE TABLE``
   - ``OPTIMIZE TABLE``

- The unsupported statements are:

   - ``ALTER TABLE LOCK = {DEFAULT|NONE}``. This also means that ``ALTER TABLE`` without a ``LOCK`` clause is not supported, as is defaults to ``DEFAULT``.
   - ``CREATE``
   - ``RENAME``
   - ``DROP``
   - ``REPAIR``

- As some DDL statements, such as ``CREATE`` without a ``LOCK`` argument, return an error, it is not recommended to use NBO on a server-wide basis. Only use it for sessions that run compatible DDL statements.

- You cannot perform writes on a table that is being altered under NBO. Write attempts are blocked, until the ``ALTER`` is complete. Under ``LOCK=SHARED``, reading from the table is allowed. Under ``LOCK=EXCLUSIVE``, read operations are also blocked.

- Locking the tables at the beginning of the operation is a blocking operation. The cluster may block, if there is an ongoing long transaction against the table being altered. To avoid this, ensure that no clients have open transactions that include the table, prior to running the ``ALTER`` statement.

- While a DDL operation is running, nodes cannot be donors for SST. Thus, a node cannot join or rejoin the cluster using SST while an NBO DDL is in progress.

- If a node leaves the cluster while an NBO DDL operation is in progress, its data files will be inconsistent and it can only rejoin the cluster through SST, not IST.

- If a DDL statement is expected to take one hour, SST will not be available for one hour, only IST. Set a high-enough value for the ``gcache.size`` so that there is sufficient cached data to use IST.

- Do not use NBO with statements that operate on more than one table at a time.

- Do not perform online schema upgrades using the RSU method while a statement is running under the NBO method.


.. warning:: To avoid conflicts between new and old schema definitions, execute SQL statements such as ``CREATE TABLE`` and ``DROP TABLE`` using the :ref:`Total Order Isolation <toi>` method.

.. note:: Contact Codership sales at sales@galeracluster.com for more information, and to get the Galera Cluster Enterprise Edition software.

.. container:: bottom-links

   Related Documents

   - :ref:`Total Order Isolation <toi>`
   - :ref:`Rolling Schema Upgrade <rsu>`
   - :ref:`Non-Blocking Operations <nbo>`
