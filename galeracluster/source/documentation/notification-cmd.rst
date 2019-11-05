.. meta::
   :title: Galera Cluster Notification Command
   :description:
   :language: en-US
   :keywords: galera cluster, notification, notify command, trigger, script
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: sub-links

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      Related Documents

      - :ref:`Notification Script <example-notification-script>`
      - :ref:`wsrep_node_incoming_address <wsrep_node_incoming_address>`
      - :ref:`wsrep_node_name <wsrep_node_name>`
      - :ref:`wsrep_notify_cmd <wsrep_notify_cmd>`

      Related Articles


.. cssclass:: library-document
.. _`notification-cmd`:

======================
Notification Command
======================

You can use the database client (e.g., ``mysql`` client) to check the status of a cluster, individual nodes, and the health of replication. However, you may find it counterproductive to log in on each node to run such checks.

As an alternative and better method, Galera Cluster provides a method to call a notification script. Such a script may be customized to automate the monitoring process of a cluster.

.. note:: For an example of such a custom script and related instructions, see :ref:`Notification Script Example <example-notification-script>`.


.. _`notification-cmd-parameters`:
.. rst-class:: section-heading
.. rubric:: Notification Parameters

When a node registers a change in itself or the cluster, it will trigger the notification script or command. In so doing, it will pass certain parameters to notification script.  Below is a list of them and their basic meaning:

.. rst-class:: no-bull

- ``--status`` The node passes a string indicating its current state.  For a list of the strings it uses, see :ref:`Node Status Strings <node-status>` below.
- ``--uuid`` The node passes a string, `yes` or `no`, to indicate whether it considers itself part of the :term:`Primary Component`.
- ``--members`` The node passes a list of the current cluster members.  For more information on the format of these, see :ref:`Member List Format <member-list-format>` below.
- ``--index`` The node passes a string that indicates its index value in the membership list.

You will have to include code in the notificaiton script to capture the values of these parameters and then have the script act as you wish (e.g., notify you of certain values).

Only nodes in the ``Synced`` state will accept connections from the cluster.  For more information on node states, see :ref:`Node State Changes <node-state-changes>`.


.. _`node-status`:
.. rst-class:: sub-heading
.. rubric:: Node Status Strings

The notification script may pass one of six values for the ``--status`` parameter to indicate the current state of the node:

.. rst-class:: no-bull

- ``Undefined`` indicates a starting node that is not part of the Primary Component.
- ``Joiner`` indicates a node that is part of the Primary Component and is receiving a state snapshot transfer.
- ``Donor`` indicates a node that is part of the Primary Component and is sending a state snapshot transfer.
- ``Joined`` indicates a node that is part of the Primary Component and is in a complete state and is catching up with the cluster.
- ``Synced`` indicates a node that is syncrhonized with the cluster.
- ``Error`` indicates that an error has occurred.  This status string may provide an error code with more information on what occurred.

Again, you will have to prepare your script to capture the value of the ``--status`` parameter and act accordingly.


.. _`member-list-format`:
.. rst-class:: sub-heading
.. rubric:: Members List Format

The notification script will pass with the ``--member`` parameter, a list containing entries for each node connected to the cluster component.  For each entry in the list the node uses this format:

.. code-block:: text

   <node UUID> / <node name> / <incoming address>

.. rst-class:: no-bull

- **Node UUID** refers to the unique identifier the node received from the wsrep Provider.
- **Node Name** refers to the node name, as it's defined with the :ref:`wsrep_node_name <wsrep_node_name>` parameter in the configuration file.
- **Incoming Address** refers to the IP address for client connections, as set with the :ref:`wsrep_node_incoming_address <wsrep_node_incoming_address>` parameter in the configuration file. If this is not set, then the default value will be ``AUTO``.


.. _`enable-notification-command`:
.. rst-class:: section-heading
.. rubric:: Enabling the Notification Script

You can enable your notification script or command through the :ref:`wsrep_notify_cmd <wsrep_notify_cmd>` parameter in the configuration file.  Below is an excerpt from that file showing how it might look:

.. code-block:: ini

   wsrep_notify_cmd=/path/wsrep_notify.sh

The node will call the script for each change in cluster membership and node status.  You can use these status changes in configuring load balancers, raising alerts or scripting for any other situation in which you need your infrastructure to respond to changes to the cluster.

Galera Cluster provides a default script, ``wsrep_notify.sh``, for you to use in handling notifications or as a starting point in writing your own custom notification script.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
