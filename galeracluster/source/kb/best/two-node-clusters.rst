=======================
Two-Node Clusters
=======================
.. _`kb-best-two-node-clusters`:

Although it may seem simple to maintain a cluster of only two nodes, there is an inherent potential problem. In a two-node cluster, when one node fails, it will cause the other to stop.


.. rubric:: Scenario
   :class: kb

Suppose you have a cluster composed of only two nodes.  Suppose further that one of the nodes leaves the cluster, ungracefully.  For instance, instead of being shut down through ``init`` or ``systemd``, it crashes or loses network connectivity.  The node that remains becomes non-operational.  It will remain so until some additional information is provided by a third entity, such as another node or a person.

In a two-node cluster, if one node loses its network connection and other node is still on the network, both will think itself as being the :term:`Primary Component`.  Each will be unaware that the other is still running. This could cause problems once network connectivity is restored. To prevent this, the nodes become non-operational.


.. rubric:: Recommendations
   :class: kb

There are two solutions available.  You can bootstrap the surviving node (i.e., the one with network connectivity) to form a new :term:`Primary Component`. You would do this by using the :ref:`pc.boostrap <pc.bootstrap>` wsrep Provider option.  To do so, log into the database client and run the following SQL statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

This will bootstrap the surviving node as a new Primary Component.  When the other node comes back online or regains network connectivity with this node, it will recognize that it's behind and initiate a state transfer to catch up.

If you want the node to continue to operate, you can use the :ref:`pc.ignore_sb <pc.ignore_sb>` wsrep Provider option.  To do so, log into the database client and run the following SQL statement:

.. code-block:: mysql

   SET GLOBAL wsrep_provider_options='pc.ignore_sb=TRUE';

The node will resume processing updates, even if it suspects a split-brain situation.

.. warning:: Enabling :ref:`pc.ignore_sb <pc.ignore_sb>` is dangerous in a multi-master setup due to the aforementioned risk for split-brain situations.  However, it does simplify things in master-slave clusters--especially in situations with only two nodes.

In addition to the solutions provided here, you can avoid this situation entirely by using Galera Arbitrator.  Galera Arbitrator functions as an odd node in quorum calculations.  If you enable Galera Arbitrator on one node in a two-node cluster, that node will remain the Primary Component, even if the other node fails or loses network connectivity.


.. rubric:: Additional Information
   :class: kb

For more information related to this KB article, see the following documents:

- :doc:`arbitrator`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
