=============================
Replication Configuration
=============================
.. _`wsrep-config`:

In addition to the configuration for the database server, there are some specific options that you need to set to enable write-set replication.  You must apply these changes to the configuration file, that is ``my.cnf``, for each node in your cluster.

- :ref:`wsrep_cluster_name <wsrep_cluster_name>` Use this parameter to set the logical name for your cluster.  You must use the same name for every node in your cluster.  The connection fails on nodes that have different values for this parameter.

- :ref:`wsrep_cluster_address <wsrep_cluster_address>` Use this parameter to define the IP addresses for the cluster in a comma separated list.

  .. note:: **See Also**: There are additional schemas and options available through this parameter.  For more information on the syntax, see :ref:`Understanding Cluster Addresses <understanding-cluster-addresses>` below.

- :ref:`wsrep_node_name <wsrep_node_name>` Use this parameter to define the logical name for the individual node |---| for convenience.

- :ref:`wsrep_node_address <wsrep_node_address>` Use this parameter to explicitly set the IP address for the individual node.  It gets used in the event that the auto-guessing does not produce desirable results.


.. code-block:: ini

   [mysql]
   wsrep_cluster_name=MyCluster
   wsrep_cluster_address="gcomm://192.168.0.1,192.168.0.2,192.168.0.3"
   wsrep_node_name=MyNode1
   wsrep_node_address="192.168.0.1"



-------------------------------------
Understanding Cluster Addresses
-------------------------------------
.. _`understanding-cluster-addresses`:

For each node in the cluster, you must provide IP addresses for all other nodes in the cluster, using the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter.  Cluster addresses are listed using a particular syntax:

.. code-block:: ini

	<backend schema>://<cluster address>[?<option1>=<value1>[&<option2>=<value2>]]

^^^^^^^^^^^^^^^^^^^
Backend Schema
^^^^^^^^^^^^^^^^^^^
.. _`backend-schema`:

There are two backend schemas available for Galera Cluster.

- ``dummy`` Which provides a pass-through back-end for testing and profiling purposes.  It does not connect to any other nodes.  It ignores any values given to it.

- ``gcomm`` Which provides the group communications back-end for use in production.  It takes an address and has several settings that you can enable through the option list, or by using the :ref:`wsrep_provider_options <wsrep_provider_options>` parameter.


^^^^^^^^^^^^^^^^^^^^^^^^^^
Cluster Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`cluster-addresses`:

For this section, provide a comma separate list of IP addresses for nodes in the cluster.  The values here can indicate,

- The IP addresses of any current members, in the event that you want to connect to an existing cluster; or,

- The IP addresses of any possible cluster members, assuming that the list members can belong to no more than one Primary Component;

If you start the node without an IP address for this parameter, the node assumes that it is the first node of a new cluster.  It initializes a cluster as though you launched ``mysqld`` with the ``--wsrep-new-cluster`` option. 


^^^^^^^^^^^^^^^^^^^^^^^^^^^
Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`cluster-address-options`:

You can also use the options list to set backend parameters, such as the listen address and timeout values.  

.. note:: **See Also**: The :ref:`wsrep_cluster_address <wsrep_cluster_address>` options list is not durable.  The node must resubmit the options on every connection to the cluster.  To make these options durable, set them in the configuration file using the :ref:`wsrep_provider_options <wsrep_provider_options>` parameter. 

The options list set in the URL take precedent over parameters set elsewhere.  Parameters that you can set through the options list are prefixed by ``evs``, ``pc`` and ``gmcast``.

.. note:: **See Also**: For more information on the available parameters, see :doc:`Galera Parameters <galeraparameters>`.

You can set the options with a list of ``key=value`` pairs according to the URL standard.  For example,

.. code-block:: ini

   wsrep_cluster_address="gcomm://192.168.0.1, 192.168.0.2, 192.168.0.3 ? gmcast.segment=0 & evs.max_install_timeouts=1" 


.. note:: If the listen address and port are not set in the parameter list, ``gcomm`` will listen on all interfaces.  The listen port will be taken from the cluster address.  If it is not specified in the cluster address, the default port is ``4567``.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
