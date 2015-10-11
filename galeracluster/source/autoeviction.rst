============================
Auto Eviction
============================
.. _`auto-eviction`:

When Galera Cluster notices erratic behavior in a node, such as unusually delayed response times, it can initiate a process to remove the node permanently from the cluster.  This process is called Auto Eviction.


-----------------------------
Configuring Auto Eviction
-----------------------------
.. _`config-auto-eviction`:

Each node in your cluster monitors the group communication response times from all other nodes in the cluster.  When the cluster registers delayed responses from a node, it adds an entry for the node to the delayed list.

If the delayed node becomes responsive again for a fixed period, entries for that node are removed from the delayed list.  If the node receives enough delayed entries and it is found on the delayed list for the majority of the cluster, the delayed node is evicted permanently from the cluster.

Evicted nodes cannot rejoin the cluster until restarted.

You can configure Auto Eviction by setting options through the :ref:`wsrep_provider_options <wsrep_provider_options>` parameter.

- :ref:`evs.delayed_margin <evs.delayed_margin>` This sets the time period that a node can delay its response from expectations until the cluster adds it to the delayed list. You must set this parameter to a value higher than the round-trip delay time (RTT) between the nodes.

  The default value is ``PT1S``.

- :ref:`evs.delayed_keep_period <evs.delayed_keep_period>` This sets the time period you require a node to remain responsive until one entry is removed from the delayed list.

  The default value is ``PT30S``.
  
- :ref:`evs.evict <evs.evict>` This sets the point where the cluster triggers manual eviction to a certain node value.  Setting this parameter as an empty string causes it to clear the evict list on the node where it is set.

- :ref:`evs.auto_evict <evs.auto_evict>`  This sets the number of entries allowed for a delayed node before Auto Eviction takes place.  Setting this to ``0`` disables the Auto Eviction protocol on the node, though the node will continue to monitor node response times.

  The default value is ``0``.

- :ref:`evs.version <evs.version>` This sets which version of the EVS Protocol the node uses.  Galera Cluster enables Auto Eviction starting with EVS Protocol version 1.

  The default value is version ``0``, for backwards compatibility.



-------------------------------
Checking Eviction Status
-------------------------------
.. _`eviction-status`:


In the event that you suspect the node or a node in your cluster is entering a delayed, you can check its eviction status through Galera status variables.

- :ref:`wsrep_evs_state <wsrep_evs_state>` This status variable gives the internal state of the EVS Protocol.

- :ref:`wsrep_evs_delayed <wsrep_evs_delayed>` This status variable gives a comma separated list of nodes on the delayed list.

  The node listing format is ``uuid:address:count``.  The ``count`` referrs to the number of entries for the given delayed node.

- :ref:`wsrep_evs_evict_list <wsrep_evs_evict_list>` This status variable lists the UUID's of evicted nodes.

You can check these status variables using the ``SHOW STATUS`` query from the database client.  For example,


.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_evs_delayed';
  

----------------------------------
Upgrading from Previous Versions
----------------------------------
.. _`upgrade-evs`:

Releases of Galera Cluster prior to version 3.8 use EVS Protocol version 0, which is not directly compatible with version 1.  As such, when you upgrade Galera Cluster for your node, the node continues to use EVS Protocol version 0.

To update the EVS Protocol version, you must first update the Galera Cluster software on each node:

#. Choose a node to start the upgrade and stop ``mysqld``.  For systems that use ``init``, run the following command:

   .. code-block:: console

      # service mysql stop

   For systems that run ``systemd``, instead use this command:

   .. code-block:: console

      # systemctl stop mysql

#. Once you stop ``mysqld``, update the Galera Cluster software for the node.  This can vary depending upon how you installed Galera Cluster and which distribution and database server you use.

#. Using a text editor, edit your configuration file, ``/etc/my.cnf``, setting the EVS Protocol version to ``0``.

   .. code-block:: ini

      wsrep_provider_options="evs.version=0"

#. Restart the node.  For systems that use ``init``, run the following command:

   .. code-block:: console

      # service mysql start

   For systems that run ``systemd``, instead use this command:

   .. code-block:: console

      # systemctl start mysql

#. Using the database client, check the node state.

   .. code-block:: console

      SHOW STATUS LIKE 'wsrep_local_state_comment';

      +----------------------------+--------+
      | Variable_name              | Value  |
      +----------------------------+--------+
      | wsrep_local_state_comment  | Joined |
      +----------------------------+--------+

   When the node state reads as ``Synced``, the node is back in sync with the cluster.

Repeat the above procedure to update the remaining nodes in the cluster.  Once this process is complete, your cluster will have the latest version of Galera Cluster.  You can then begin updating the EVS Protocol version for each node.

#.  Choose a node to start on, then using a text editor, update the EVS Protocol version in the configuration file, ``/etc/my.cnf``.

    .. code-block:: ini

       wsrep_provider_options="evs.version=1"

#. Restart ``mysqld``.  If your system uses ``init``, run the following command:

   .. code-block:: console

      # service mysql restart

   For system that run ``systemd``, instead use this command:

   .. code-block:: console

      # systemctl restart mysql

#. Using the database clinet, check that the EVS Protocol is using version 1 by running the new :ref:`wsrep_evs_state <wsrep_evs_state>` status variable.

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_evs_state';

   If the ``STATUS`` query returns an empty set, something went wrong and your database server is still on EVS Protocol version 0.  If it returns a set, the EVS Protocol is on the right version and you can proceed.
      

#. Check the node state.

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_local_state_comment';

      +----------------------------+--------+
      | Variable_name              | Value  |
      +----------------------------+--------+
      | wsrep_local_state_comment  | Joined |
      +----------------------------+--------+
      
   When the node state reads as ``Synced``, the node is back in sync with the cluster.

This updates the EVS Protocol version for one node in your cluster.  Repeat the process on the remaining nodes, so that they all use EVS Protocol version 1.


.. note:: **See Also**: For more information on upgrading in general, see :doc:`upgrading`.

