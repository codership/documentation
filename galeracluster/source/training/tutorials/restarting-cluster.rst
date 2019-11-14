.. meta::
   :title: Restarting Galera Cluster
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

      - :ref:`gcache.recover <gcache.recover>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`restarting-cluster`:

================================
Restarting the Cluster
================================

.. rst-class:: article-stats

   Length:  791 words; Published: October 20, 2014; Topic: General; Level: Beginner

Occasionally, you may have to restart an entire Galera Cluster.  This may happen, for example, when there is a power failure in which every node is shut down and you have no ``mysqld`` process.  Restarting a cluster, starting nodes in the wrong order, starting the wrong nodes first, can be devastating and lead to loss of data.

When restarting an entire Galera Cluster, you'll need to determine which node has the most advanced node state ID. This is covered in the next section.  Once you've identified the most advanced node, you'll need to start that node first.  Then you can start the rest of the nodes in any order.  They will each look to the first node as the most up-to-date node.


.. _`Identify Most Advanced Node`:
.. rst-class:: section-heading
.. rubric:: Identifying the Most Advanced Node

Identifying the most advanced node state ID is done by comparing the :term:`Global Transaction ID` values on each node in your cluster.  You can find this in the ``grastate.dat`` file, located in the data directory for your database.

If the ``grastate.dat`` file looks like the example below, you have found the most advanced node state ID:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   8204503945773
	cert_index:

To find the sequence number of the last committed transaction, run ``mysqld`` with the ``--wsrep-recover`` option.  This recovers the InnoDB table space to a consistent state, prints the corresponding Global Transaction ID value into the error log, and then exits.  Here's an example of this:

.. code-block:: console

	130514 18:39:13 [Note] WSREP: Recovered position: 5ee99582-bb8d-11e2-b8e3-
	23de375c1d30:8204503945771

This value is the node state ID.  You can use it to update manually the ``grastate.dat`` file, by entering it in the value of the ``seqno`` field. As an alternative, you can just let ``mysqld_safe`` recover automatically and pass the value to your database server the next time you start it.


.. _`'Safe to Bootstrap' Protection`:
.. rst-class:: section-heading
.. rubric:: 'Safe to Bootstrap' Protection

Starting with provider version 3.19, Galera has an additional protection against attempting to boostrap the cluster using a node that may not have been the last node remaining in the cluster prior to cluster shutdown.

If Galera can conclusively determine which node was the last node standing, it will be marked as 'safe to bootstrap', as seen in this example ``grastate.dat``:

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5981f182-a4cc-11e6-98cc-77fabedd360d
	seqno:   1234
	safe_to_bootstrap: 1

Such a node can be used to bootstrap the cluster. Attempting to boostrap using any other node will cause the following error message:

.. code-block:: console

	2016-11-07 01:49:19 5572 [ERROR] WSREP: It may not be safe to bootstrap the cluster from this node.
	It was not the last one to leave the cluster and may not contain all the updates.
	To force cluster bootstrap with this node, edit the grastate.dat file manually and set safe_to_bootstrap to 1 .

To override this protection, edit the ``safe_to_bootstrap`` line in the ``grastate.dat`` file of the node you intend to use as the first node.

In the case when all nodes crashed simultaneously, no node will be considered safe to bootstrap until the ``grastate.dat`` file is edited manually.


.. rst-class:: section-heading
.. rubric:: Gcache Recovery

Starting with provider version 3.19, Galera provides the :ref:`gcache.recover <gcache.recover>` parameter. If set to ``yes``, Galera will attempt to recover the gcache on node startup.

If gcache recovery is successful, the node will be in position to provide IST to other joining nodes, which can speed up the overall restart time for the entire cluster.

Gcache recovery requires that the entire gcache file is read twice. For large gcache files located on slow disks, this operation may take some time.

Gcache recovery is a "best effort" operation. If recovery was not successful, the node will continue to operate normally however other nodes will fall back to SST when attempting to join.


.. _`Identify Crashed Node`:
.. rst-class:: section-heading
.. rubric:: Identifying Crashed Nodes

You can easily determine if a node has crashed by looking at the contents of the ``grastate.dat`` file. If it looks like the example below, the node has either crashed during execution of a non-transactional operation (e.g., ``ALTER TABLE``), or the node aborted due to a database inconsistency.

.. code-block:: text

	# GALERA saved state
	version: 2.1
	uuid:    5ee99582-bb8d-11e2-b8e3-23de375c1d30
	seqno:   -1
	cert_index:

It's possible for you to recover the :term:`Global Transaction ID` of the last committed transaction from InnoDB, as described above. However, the recovery is rather meaningless.  After the crash, the node state is probably corrupted and may not prove functional.

If there are no other nodes in the cluster with a well-defined state, there is no need to preserve the node state ID.  You must perform a thorough database recovery procedure, similar to that used on stand-alone database servers.  Once you recover one node, use it as the first node in a new cluster.

.. container:: bottom-links

   Related Documents

   - :ref:`gcache.recover <gcache.recover>`
