=======================
Two-Node Clusters
=======================
.. _`two-node-clusters`:

In a two-node cluster, a single-node failure causes the other to stop working.

.. rubric:: Situation

You have a cluster composed of only two nodes.  One of the nodes leaves the cluster *ungracefully*.  That is, instead of being shut down through ``init`` or ``systemd``, it crashes or suffers a loss of network connectivity.  The node that remains becomes nonoperational.  It remains so until some additional information is provided by a third party, such as a human operator or another node.

If the node remained operational after the other left the cluster ungracefully, there would be the risk that each of the two nodes will think itself as being the :term:`Primary Component`.  To prevent this, the node becomes nonoperational.



.. rubric:: Solutions

There are two solutions available to you:

- You can bootstrap the surviving node to form a new :term:`Primary Component`, using the :ref:`pc.boostrap <pc.bootstrap>` wsrep Provider option.  To do so, log into the database client and run the following command:

  .. code-block:: mysql

     SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';

  This bootstraps the surviving node as a new Primary Component.  When the other node comes back online or regains network connectivity with this node, it will initiate a state transfer and catch up with this node.

- In the event that you want the node to continue to operate, you can use the :ref:`pc.ignore_sb <pc.ignore_sb>` wsrep Provider option.  To do so, log into the database client and run the following command:

  .. code-block:: mysql

     SET GLOBAL wsrep_provider_options='pc.ignore_sb=TRUE';

  The node resumes processing updates and it will continue to do so, even in the event that it suspects a split-brain situation.


  .. note:: **Warning**: Enabling :ref:`pc.ignore_sb <pc.ignore_sb>` is dangerous in a multi-master setup, due to the aforementioned risk for split-brain situations.  However, it does simplify things in master-slave clusters, (especially in cases where you only use two nodes).

In addition to the solutions provided above, you can avoid the situation entirely using Galera Arbitrator.  Galera Arbitrator functions as an odd node in quorum calculations.  Meaning that, if you enable Galera Arbitrator on one node in a two-node cluster, that node remains the Primary Component, even if the other node fails or loses network connectivity.

.. see also:: For more information, see :doc:`arbitrator`.
	    











