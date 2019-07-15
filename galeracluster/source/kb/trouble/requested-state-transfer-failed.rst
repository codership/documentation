.. meta::
   :title: Resolving Requested State Transfer Failures
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

      - :ref:`wsrep_node_name <wsrep_node_name>`
      - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
      - :ref:`gmcast.segment <gmcast.segment>`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: kb-article
.. _`kb-trouble-requested-state-transfer-failed`:

================================
Requested State Transfer Failed
================================

When a new node joins a cluster, it will try to synchronize with the cluster by getting a full copy of the databases from one of the other nodes.  Sometimes this will fail.


.. rst-class:: kb
.. rubric:: Scenario

Suppose a joiner node seeks a donor node to give it a copy of the databases by the :term:`State Snapshot Transfer` (SST) method.  Suppose further that an excessive amount of time passes and it's unsuccessful.

You decide to look at the database server's error log on a joiner node, and it contains the following message:

.. code-block:: text

   Node 0 (XXX) requested state transfer from '*any*'.
   Selected 1 (XXX) as donor.

This indicates that you didn't explicitly set the donor node in the configuration file. As a result, the *Group Communication* module will select a donor based on what it knows about the status of each node.

The joiner node selects a donor from the available synced nodes, nodes in ``SYNCED`` state--preferrably ones that have the same :ref:`gmcast.segment <gmcast.segment>` wsrep Provider option, but otherwise it will select the first in the index.

If the joiner node can't find a free node that shows as ``SYNCED``, it will report the following:

.. code-block:: text

   Requesting state transfer failed: -11(Resource temporarily
   unavailable).  Will keep retrying every 1 second(s).

The joiner node will continue to retry the state transfer request.

.. rst-class:: kb
.. rubric:: Solution

To make the process of finding a donor node faster, you could set one or more donor nodes with the :ref:`wsrep_sst_donor <wsrep_sst_donor>` parameter.  You could do this in the configuration file, or on the fly like so:

.. code-block:: mysql

   SET wsrep_sst_donor = 'node1,node2';

This tells the cluster that one of the nodes named ``node1`` and ``node2`` should be used as the donor. This value is set with the :ref:`wsrep_node_name <wsrep_node_name>` parameter in each node's configuration file.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
