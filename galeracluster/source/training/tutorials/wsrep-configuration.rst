.. meta::
   :title: Galera Cluster Replication Configuration
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           .. cssclass:: here

           - :doc:`Tutorial Articles <./index>`

        .. cssclass:: sub-links

           - :doc:`Training Videos <../videos/index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      - :doc:`Galera Parameters <../../../documentation/galera-parameters>`
      - :ref:`wsrep_cluster_name <wsrep_cluster_name>`
      - :ref:`wsrep_cluster_address <wsrep_cluster_address>`
      - :ref:`wsrep_node_name <wsrep_node_name>`
      - :ref:`wsrep_node_address <wsrep_node_address>`
      - :ref:`wsrep_provider_options <wsrep_provider_options>`

      Related Articles


.. cssclass:: library-article
.. _`wsrep-configuration`:

===========================
Replication Configuration
===========================

.. rst-class:: article-stats

   Length:  964 words; Published: October 20, 2014; Topic: General; Level: Beginner

In addition to the configuration for the database server, there are some specific options that you need to set to enable write-set replication.  You must apply these changes to the configuration file (i.e., ``my.cnf``) for each node in the cluster.

- :ref:`wsrep_cluster_name <wsrep_cluster_name>`: Use this parameter to set the logical name for the cluster.  You must use the same name for each node in the cluster.  The connection will fail on nodes that have different values for this parameter.

- :ref:`wsrep_cluster_address <wsrep_cluster_address>`: Use this parameter to define the IP addresses for the cluster in a comma-separated list.

  .. note:: There are additional schemata and options available through this parameter.  For more information on the syntax, see Cluster Addresses below.

- :ref:`wsrep_node_name <wsrep_node_name>`: Use this parameter to define the logical name for the individual node |---| for convenience.

- :ref:`wsrep_node_address <wsrep_node_address>`: Use this parameter to set explicitly the IP address for the individual node.  It's used when auto-guessing doesn't produce desirable results.


.. code-block:: console

   [mysqld]
   wsrep_cluster_name=MyCluster
   wsrep_cluster_address="gcomm://192.168.0.1,192.168.0.2,192.168.0.3"
   wsrep_node_name=MyNode1
   wsrep_node_address="192.168.0.1"


.. _`backend-schema`:
.. rst-class:: section-heading
.. rubric:: Backend Schema

There are two backend schemata available with Galera Cluster.

- ``dummy``: This provides a pass-through back-end for testing and profiling purposes.  It doesn't connect to other nodes and will ignore any values given to it.

- ``gcomm``: This provides the group communications back-end for use in production.  It accepts an address and has several settings that may be enabled through the option list, or by using the :ref:`wsrep_provider_options <wsrep_provider_options>` parameter.


.. _`cluster-addresses`:
.. rst-class:: section-heading
.. rubric:: Cluster Addresses

For the cluster address section, you have to provide a comma-separate list of IP addresses for all of the nodes in the cluster.  You would do this using the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter.  Cluster addresses are listed in the configuration file using a particular syntax, like so:

.. code-block:: ini

	<backend schema>://<cluster address>[?<option1>=<value1>[&<option2>=<value2>]]

Below is an example of how this line from the configuration file might look:

.. code-block:: ini

   wsrep_cluster_address="gcomm://192.168.0.1,192.168.0.2,192.168.0.3"

Here, the backend schema is ``gcomm``.  The cluster addresses (i.e., ``192.168.0.1``, etc.) are listed next, separted by commas.  You can add options after that, within the quotes. You would start with a question mark, followed by each option setting. Option key/value pairs are separated by an ampersand. This is covered in the Options section below.

The IP addresses given in the configuration file should include any current members of the cluster.  The list may also include the IP addresses of any possible cluster members. Members can belong to no more than one Primary Component;

If you start a node without proving an IP address for this parameter, the node will assume that it's the first node of a new cluster.  It will initialize the cluster as though you launched ``mysqld`` with the ``--wsrep-new-cluster`` option.


.. _`cluster-address-options`:
.. rst-class:: section-heading
.. rubric:: Options

When setting the IP address in the configuration file using the :ref:`wsrep_cluster_address <wsrep_cluster_address>` parameter, you can also set some options. You can set backend parameters, such as the listen address and timeout values.

.. note:: The :ref:`wsrep_cluster_address <wsrep_cluster_address>` options list is not durable.  The node must resubmit the options on each connection to a cluster.  To make these options durable, set them in the configuration file using the :ref:`wsrep_provider_options <wsrep_provider_options>` parameter.

The options set in the URL take precedent over parameters set elsewhere.  Parameters you set through the options list are prefixed by ``evs`` (i.e., Extended Virtual Synchrony), ``pc`` (i.e., Primary Component) and ``gmcast``.

For more information on the available parameters, see :doc:`Galera Parameters <../../../documentation/galera-parameters>`.

When listing options, start with a question mark after the IP address list. Then provide the options in a ``key=value`` format. Key/value pairs must be separated by an ampersand. Below is an example of how this might look:

.. code-block:: ini

   wsrep_cluster_address="gcomm://192.168.0.1, 192.168.0.2, 192.168.0.3 ? gmcast.segment=0 & evs.max_install_timeouts=1"


In this example, the ``segment`` option for ``gcomm`` and the ``max_install_timeouts`` option for ``evs`` are set.

Incidentally, if the listen address and port are not set in the parameter list, ``gcomm`` will listen on all interfaces.  The listen port will be taken from the cluster address.  If it's not specified in the cluster address, the default port is ``4567``.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
