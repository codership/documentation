.. meta::
   :title: Detecting a Slow Node
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

      - :ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>`
      - :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`

      Related Articles


.. cssclass:: library-article
.. _`kb-best-detecting-slow-node`:

=========================
Detecting a Slow Node
=========================

.. rst-class:: article-stats

   Length: 297 words; Published: October 22, 2019; Category: Performance; Type: Best Practices

By design, the performance of a cluster cannot be higher than the performance of the slowest node in the cluster. Even if you have only one node, its performance can be considerably slower when compared with running the same server in a standalone mode (i.e., without a wsrep Provider).

This is particularly true for large transactions---even if they are within transaction size limits. This is why it's important to be able to detect a slow node on a cluster.

.. rst-class:: kb
.. rubric:: Scenario

.. _`finding-slow-nodes`:

Suppose you suspect that your cluster is running slowly, that transactions are slow to commit to all nodes. However, you're not sure which node is the slowest.

There are two status variables you can use to find slow nodes in a cluster: :ref:`wsrep_flow_control_sent <wsrep_flow_control_sent>` and :ref:`wsrep_local_recv_queue_avg <wsrep_local_recv_queue_avg>`. Check these status variables on each node in a cluster.  The node that returns the highest value is the slowest one.  Lower values are preferable.

.. code-block:: mysql

   SELECT * FROM information_schema.GLOBAL_STATUS
   WHERE VARIABLE_NAME LIKE 'wsrep_flow_control_sent'
   OR VARIABLE_NAME LIKE 'wsrep_local_recv_queue_avg';

   +----------------------------+----------------+
   | VARIABLE_NAME              | VARIABLE_VALUE |
   +----------------------------+----------------+
   | WSREP_LOCAL_RECV_QUEUE_AVG | 3.34852        |
   | WSREP_FLOW_CONTROL_SENT    | 7              |
   +----------------------------+----------------+

The ``wsrep_flow_control_sent`` variable provides the number of times a node sent a pause event due to flow control since the last status query. The ``wsrep_local_recv_queue_avg`` varaible returns an average of the received queue length since the last status query. Nodes that return values much higher than ``0.0`` indicate that it cannot apply write-sets as fast as they are received and can generate replication throttling.

Check these status variables on each node in your cluster.  The node that returns the highest value is the slowest node.  Lower values are preferable.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
