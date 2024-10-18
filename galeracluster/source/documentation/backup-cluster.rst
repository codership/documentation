.. meta::
   :title: Back-up a Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, sst backup, state snapshot transfer
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.

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

      - :doc:`Scriptable SST <scriptable-sst>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`backup-cluster`:

=========================
 Backing Up Cluster Data
=========================

.. index::
   pair: Logs; mysqld error log
.. index::
   pair: Parameters; gmcast.listen_addr
.. index::
   pair: Parameters; wsrep_cluster_name
.. index::
   pair: Parameters; wsrep_node_name
.. index::
   single: Galera Arbitrator

You can perform backups with Galera Cluster at the same regularity as with a standard database server, using a backup script. Since replication ensures that all nodes have the exact same data, running a backup script on one node will backup the data on all nodes in the cluster.

The problem with such a simple backup method, though, is that it lacks a :term:`Global Transaction ID` (GTID). You can use backups of this kind to recover data, but they are insufficient for use in recovering nodes to a well-defined state. Furthermore, some backup procedures can block cluster operations during the backup.

Getting backups with the associated Global Transaction ID requires a different approach.


.. _`sst-backup`:
.. rst-class:: section-heading
.. rubric:: State Snapshot Transfer as Backup

Taking a full data backup is very similar to node provisioning through a :term:`State Snapshot Transfer`. In both cases, the node creates a full copy of the database contents, using the same mechanism to associate a :term:`Global Transaction ID` with the database state. Invoking backups through the state snapshot transfer mechanism has the following benefits:

- The node initiates the backup at a well-defined point.
- The node associates a Global Transaction ID with the backup.
- The node desyncs from the cluster to avoid throttling performance while making the backup, even if the backup process blocks the node.
- The cluster knows that the node is performing a backup and won't choose the node as a donor for another node.

In order to use this method for backups, you will need to use a script that implements both your preferred backup procedure and the Galera Arbitrator daemon, triggering it in a manner similar to a state snapshot transfer. You would execute such a script from the command-line, as described below:

On the node where you want to have a backup, start the original SST script manually in "joiner" mode. This command opens a socket listening for a connection from "donor":

.. code-block:: console

   $ wsrep_sst_rsync --role 'joiner' --address '10.21.32.1:3333' --datadir '/tmp/backup/' \
     --defaults-file '' --defaults-group-suffix '' --parent $$

Note the output:

.. code-block:: console

   $ ready 10.21.32.1:3333/rsync_sst

Next, on any node, give the command:

.. code-block:: console

   $ garbd --address gcomm://10.21.32.1:4567?gmcast.listen_addr=tcp://0.0.0.0:4560 \
     --group my_cluster --sst rsync:10.21.32.1:3333/rsync_sst

.. note:: In the command, ``?gmcast.listen_addr=tcp://0.0.0.0:4560`` is an arbitrary listen socket address that Galera Arbitrator opens to communicate with the cluster. You only need to specify this in the event that the default socket address (that is, ``0.0.0.0:4567``) is busy.

.. note:: In the command, the value of the ``--sst`` option is ``<sst_method>:<sst_address>``, where ``<sst_address>`` is given in the output of the joiner script above.

.. note:: You may find it useful to create your backup script using a modified version of the standard state snapshot transfer script. For information on scripts of this kind, see :doc:`scriptable-sst`.

.. container:: bottom-links

   Related Documents

   - :doc:`Scriptable SST <scriptable-sst>`
