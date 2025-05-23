.. meta::
   :title: Galera Functions
   :description:
   :language: en-US
   :keywords: galera cluster, mysql wsrep functions, galera functions
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

      - :ref:`repl.causal_read_timeout <repl.causal_read_timeout>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`wsrep-functions`:

=======================
Galera Functions
=======================

Starting with version 4 of Galera Cluster, there are several Galera functions available. At this point, the Galera functions related to :term:`Global Transaction ID` (GTID). They return a GTID or have effect on transactions related to a GTID.

.. csv-table::
   :class: doc-options
   :header: "Function", "Arguments", "Initial Version"
   :widths: 40, 40, 20

   ":ref:`WSREP_LAST_SEEN_GTID() <WSREP_LAST_SEEN_GTID>`", "", "4.0"
   ":ref:`WSREP_LAST_WRITTEN_GTID() <WSREP_LAST_WRITTEN_GTID>`", "", "4.0"
   ":ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`", "``gtid`` ``[timeout]``", "4.0"


.. _`WSREP_LAST_SEEN_GTID`:
.. rst-class:: section-heading
.. rubric:: ``WSREP_LAST_SEEN_GTID()``

.. index::
   pair: Functions; WSREP_LAST_SEE_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

Much like ``LAST_INSERT_ID()`` for getting the identification number of the last row inserted in MySQL, this function returns the :term:`Global Transaction ID` of the last write transaction observed by the client.

.. csv-table::
   :class: doc-options

   "Function", "``WSREP_LAST_SEEN_GTID()``"
   "Arguments", "None"
   "Initial Version", "Version 4.0"

This function returns the :term:`Global Transaction ID` of the last write transaction observed by the client. It can be useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`. You can use this parameter to identify the transaction upon which it should wait before unblocking the client.

Below is an example of how you might use the ``WSREP_LAST_SEEN_GTID()`` function to get the Global Transaction ID of the last write transaction observed:

.. code-block:: mysql

   SELECT WSREP_LAST_SEEN_GTID();


.. _`WSREP_LAST_WRITTEN_GTID`:
.. rst-class:: section-heading
.. rubric:: ``WSREP_LAST_WRITTEN_GTID()``

.. index::
   pair: Functions; WSREP_LAST_WRITTEN_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

This function returns the :term:`Global Transaction ID` of the last write transaction made by the client.

.. csv-table::
   :class: doc-options

   "Function", "``WSREP_LAST_WRITTEN_GTID()``"
   "Arguments", "None"
   "Initial Version", "Version 4.0"

This function returns the Global Transaction ID of the last write transaction made by the client. This can be useful in combination with :ref:`WSREP_SYNC_WAIT_UPTO_GTID() <WSREP_SYNC_WAIT_UPTO_GTID>`. You can use this parameter to identify the transaction upon which it should wait before unblocking the client.

Below is an example of how you might use the ``WSREP_LAST_SEEN_GTID()`` function to get the Global Transaction ID of the last write transaction observed:

.. code-block:: mysql

   BEGIN;

   UPDATE table_name SET id = 0
   WHERE field = 'example';

   COMMIT;

   SELECT WSREP_LAST_WRITTEN_GTID();


.. _`WSREP_SYNC_WAIT_UPTO_GTID`:
.. rst-class:: section-heading
.. rubric:: ``WSREP_SYNC_WAIT_UPTO_GTID()``

.. index::
   pair: Functions; WSREP_SYNC_WAIT_UPTO_GTID()
.. index::
   pair: Galera Cluster 4.x; Synchronization Functions

This function blocks the client until the node applies and commits the given transaction.

.. csv-table::
   :class: doc-options

   "Function", "``WSREP_SYNC_WAIT_UPTO_GTID()``"
   "Required Arguments", "Global Transaction ID"
   "Optional Arguments", "timeout" 
   "Initial Version", "Version 4.0"

This function blocks the client until the node applies and commits the given :term:`Global Transaction ID`. Optional argument accepts timeout in seconds.
If you do not provide a timeout, it will continue to block indefinitely. It returns the following values:

- ``1``: The node applied and committed the given Global Transaction ID.

- ``ER_LOCAL_WAIT_TIMEOUT`` Error: The function times out before the node can apply the transaction.

- ``ER_WRONG_ARGUMENTS`` Error: The function is given an incorrect Global Transaction ID.

Below is an example of how you might use the ``WSREP_SYNC_WAIT_UPTO_GTID()`` function:

.. code-block:: console

   $transaction_gtid = SELECT WSREP_LAST_SEEN_GTID();
   ...
   SELECT WSREP_SYNC_WAIT_UPTO_GTID($transaction_gtid);

..
  .. container:: bottom-links
