.. meta::
   :title: Inconsistency Voting
   :description:
   :language: en-US
   :keywords: galera cluster, inconsistency voting
   :copyright: Codership Oy, 2014 - 2021. All Rights Reserved.


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

      - :ref:`gcs.vote_policy <gcs.vote_policy>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`inconsistency-voting`:

=================================
Cluster Inconsistency Voting
=================================

.. index::
   pair: Configuration; gcs.vote_policy


Cluster inconsistency voting is a protocol for nodes to decide how the cluster reacts to problems in replication. Inconsistency voting helps, when one or several nodes have an issue to apply an incoming transactions. This can happen, for example, in the case of suspected inconsistency.

If, for example, in a five-node cluster, two nodes fail to apply a transaction, they get removed. When the DBA has corrected the issue, the nodes can rejoin the cluster.

Inconsistency voting works, as follows:

- For transactions:

   - If applying a writeset fails on a secondary node, an error description is passed back to the primary, and it initiates voting in the group. All nodes report the result they get for a given action, and if there is a simple majority about a given result, this result wins and the nodes that have a different result gracefully leave the group.
   
   -  If there is no majority, success wins.
   
   - If there is no node with a successful result, another node wins.

- For TOI operations (DDLs):

   - The operation is the same as for transactions, except that also the primary can initiate a vote, if DDL fails.

- Configuration:

   - The ``wsrep_ignore_apply_errors`` bitmask controls whether the error is reported back to the provider. For example, ``wsrep_ignore_apply_errors=4`` ignores all DDL errors. Otherwise, any DDL error results in a voting round. In this case, a more useful value would be 1, where only reconciling DDL errors are ignored.
   
   - The ``gcs.vote_policy`` parameter defines who wins in a voting round. The default value 0 means simple majority as described above. Any value above 1 means that if the success votes count is >= that value, success wins, even if in minority. For example, if ``gcs.vote_policy=1``, only the node that successfully committed a transaction would remain primary.


.. container:: bottom-links

   Related Documents

   - :ref:`gcs.vote_policy <gcs.vote_policy>`
