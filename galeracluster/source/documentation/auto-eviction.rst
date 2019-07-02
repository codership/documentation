.. cssclass:: library-document
.. _`auto-eviction`:

============================
Auto-Eviction
============================

When Galera Cluster notices erratic behavior in a node (e.g., unusually delayed response times), it can initiate a process to remove the node permanently from the cluster.  This process is called *Auto-Eviction*.


.. _`config-auto-eviction`:

-----------------------------
Configuring Auto-Eviction
-----------------------------

Each node in a cluster monitors the group communication response times from all other nodes in the cluster.  When a cluster registers delayed responses from a node, it makes an entry about the node to the delayed list.

If the delayed node becomes responsive again for a fixed period, entries for that node are removed from the delayed list.  However, if the node receives enough delayed entries and it's found on the delayed list for the majority of the cluster, the delayed node is evicted permanently from the cluster. Evicted nodes cannot rejoin the cluster until restarted.

You can configure the parameters of Auto-Eviction by setting the following options through  :ref:`wsrep_provider_options <wsrep_provider_options>`:

- :ref:`evs.delayed_margin <evs.delayed_margin>`: This sets the time period that a node can delay its response from expectations until the cluster adds it to the delayed list. You must set this parameter to a value higher than the round-trip delay time (RTT) between the nodes.

  The default value is ``PT1S``.

- :ref:`evs.delayed_keep_period <evs.delayed_keep_period>`: This sets the time period you require a node to remain responsive until it's removed from the delayed list.

  The default value is ``PT30S``.

- :ref:`evs.evict <evs.evict>` This sets the point in which the cluster triggers manual eviction to a certain node value.  Setting this parameter as an empty string causes it to clear the evict list on the node where it is set.

- :ref:`evs.auto_evict <evs.auto_evict>`:  This sets the number of entries allowed for a delayed node before Auto-Eviction takes place.  Setting this to ``0`` disables the Auto-Eviction protocol on the node, though the node will continue to monitor node response times.

  The default value is ``0``.

- :ref:`evs.version <evs.version>`: This sets which version of the EVS Protocol the node uses.  Galera Cluster enables Auto-Eviction starting with EVS Protocol version 1.

  The default value is version ``0``, for backwards compatibility.


.. _`eviction-status`:

-------------------------------
Checking Eviction Status
-------------------------------

If you suspect a node is becoming delayed, you can check its eviction status through Galera status variables. You can do this by using the ``SHOW STATUS`` statement from the database client.  You would enter something like this:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_evs_delayed';


Below are the Galera status variables available to you:

- :ref:`wsrep_evs_state <wsrep_evs_state>`: This status variable gives the internal state of the EVS Protocol.

- :ref:`wsrep_evs_delayed <wsrep_evs_delayed>`: This status variable gives a comma separated list of nodes on the delayed list. The format used in that list is ``uuid:address:count``.  The ``count`` refers to the number of entries for the given delayed node.

- :ref:`wsrep_evs_evict_list <wsrep_evs_evict_list>`: This status variable lists the UUID's of evicted nodes.


.. _`upgrade-evs`:

----------------------------------
Upgrading from Previous Versions
----------------------------------

Releases of Galera Cluster prior to version 3.8 use EVS Protocol version 0, which is not directly compatible with version 1.  As such, when you upgrade Galera Cluster for a node, the node continues to use EVS Protocol version 0.

To update the EVS Protocol version, you must first update the Galera Cluster software on each node. Here are the steps to do that:

#. Choose a node to start the upgrade and stop ``mysqld`` on it.  For systems that use ``init``, run the following command:

   .. code-block:: console

      # service mysql stop

   For systems that run ``systemd``, use instead this command:

   .. code-block:: console

      # systemctl stop mysql

#. Once you stop ``mysqld``, update the Galera Cluster software for the node.  This can vary depending on how you installed Galera Cluster and which database server and operating system distribution the server uses.

#. Using a text editor, edit the configuration file, ``/etc/my.cnf``. Set the EVS Protocol version to ``0``.

   .. code-block:: ini

      wsrep_provider_options="evs.version=0"

#. After saving the configuration file, restart the node.  For systems that use ``init``, run the following command:

   .. code-block:: console

      # service mysql start

   For systems that run ``systemd``, instead use this command:

   .. code-block:: console

      # systemctl start mysql

#. Using the database client, check the node state with the ``SHOW STATUS`` statement like so:

   .. code-block:: console

      SHOW STATUS LIKE 'wsrep_local_state_comment';

      +----------------------------+--------+
      | Variable_name              | Value  |
      +----------------------------+--------+
      | wsrep_local_state_comment  | Joined |
      +----------------------------+--------+

   When the node state reads as ``Synced``, the node is back in sync with the cluster.

Repeat the above steps on each node in the cluster to update them.  Once this process is finished, the cluster will have the latest version of Galera Cluster.  You can then begin updating the EVS Protocol version for each node. Below are the steps to do that:

#.  On the first node, edit the configuration file, ``/etc/my.cnf`` with a text editor. Change the EVS Protocol version in it like so:

    .. code-block:: ini

       wsrep_provider_options="evs.version=1"

#. After saving, restart ``mysqld``.  If your system uses ``init``, run the following command:

   .. code-block:: console

      # service mysql restart

   For system that run ``systemd``, use instead this command:

   .. code-block:: console

      # systemctl restart mysql

#. Using the database clinet, execute the ``SHOW STATUS`` statement to see if the EVS Protocol is using version 1. This time give it the new :ref:`wsrep_evs_state <wsrep_evs_state>` status variable.

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_evs_state';

   If the ``SHOW STATUS`` statement returns an empty set, something went wrong and your database server is still using EVS Protocol version 0.  If it returns a results set, the EVS Protocol is on the right version and you can proceed.


#. Once you confirm the server is using the right version, check the node state. Execute the ``SHOW STATUS`` statement like so:

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_local_state_comment';

      +----------------------------+--------+
      | Variable_name              | Value  |
      +----------------------------+--------+
      | wsrep_local_state_comment  | Joined |
      +----------------------------+--------+

   When the node state reads as ``Synced``, the node is back in sync with the cluster.

These steps will update the EVS Protocol version for one node in a cluster. Repeat the process on each of the remaining nodes so that they all use EVS Protocol version 1.


For more information on upgrading in general, see :doc:`upgrading`.
