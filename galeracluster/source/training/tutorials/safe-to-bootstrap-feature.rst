.. meta::
   :title: The Safe-To-Bootstrap Feature in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`
      - :ref:`search`


.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`safe-to-bootstrap-feature`:

===============================
The Safe-To-Bootstrap Feature
===============================

.. rst-class:: article-stats

   Length:  745 words; Writer: Philip Stoev; Published: November 18, 2016; Topic: General; Level: Intermediate

Galera Clusters are generally meant to run non-stop, so shutting down the entire cluster is not required during normal operation. Yet, if there is a need to perform such a procedure, it is likely that it will be happening under pressure, so it is important for it to complete safely and as quickly as possible in order to avoid extended downtime and potential data loss.

Galera 3.19 includes two important improvements to whole-cluster restart: the “Safe-to-Bootstrap” protection and Gcache recovery. In this article, we will describe the first feature.


.. rst-class:: section-heading
.. rubric:: Whole-Cluster Restart

First, a few words on cluster restarts in general. Regardless of whether it was an orderly shutdown or a sudden crash of all nodes, restarting the entire cluster is governed by the following principles:

- Since the old cluster no longer logically exists, a new logical cluster is being created
- The first node that is being started must be bootstrapped
- It is important to select the node that has the last transactions committed as the first node in the new cluster


.. rst-class:: section-heading
.. rubric:: The Safe-to-Bootstrap Protection

In an orderly shutdown, the node that was shut down last will be the one that has the last transaction committed and should be chosen as the first node in the new cluster. Selecting another node for that role may cause errors down the road and open an opportunity for those last transactions to be lost.

To facilitate that decision and prevent unsafe choices, Galera, starting with version 3.19, will keep track of the order in which nodes are being shut down. The node that was shut down last will be marked as “Safe-to-Bootstrap” from. All the other nodes will be marked as unsafe to bootstrap from.

When bootstrapping the new cluster, Galera will refuse to use as a first node a node that was marked as unsafe to bootstrap from. You will see the following message in the logs:

.. code-block:: console

   It may not be safe to bootstrap the cluster from this node. It was not the last one to leave the cluster and may not contain all the updates.

   To force cluster bootstrap with this node, edit the grastate.dat file manually and set safe_to_bootstrap to 1 .

In case of a sudden crash of the entire cluster, all nodes will be considered unsafe to bootstrap from, so operator action will always be required to force the use of a particular node as a bootstrap node.


.. rst-class:: section-heading
.. rubric:: Selecting the Right Node

The procedure to select the right node to bootstrap from depends on how the cluster terminated: via an orderly shutdown or a crash.

In case of an orderly shutdown, it is sufficient to follow the recommendations of the “Safe-to-Bootstrap” feature. Look for the node whose grastate.dat has ``safe_to_bootstrap: 1``:

.. code-block:: console

   # GALERA saved state
   version: 2.1
   uuid:    9acf4d34-acdb-11e6-bcc3-d3e36276629f
   seqno:   15
   safe_to_bootstrap: 1

and use that node.

In case of a hard crash, all nodes will have ``safe_to_bootstrap: 0``, so we will need to consult the InnoDB storage engine to determine which node has committed the last transaction in the cluster. This is achieved by starting mysqld with the ``--wsrep-recover`` variable, which produces an output like this:

.. code-block:: console

   ...
   2016-11-18 01:42:15 36311 [Note] InnoDB: Database was not shutdown normally!
   2016-11-18 01:42:15 36311 [Note] InnoDB: Starting crash recovery.
   ...
   2016-11-18 01:42:16 36311 [Note] WSREP: Recovered position: 37bb872a-ad73-11e6-819f-f3b71d9c5ada:345628
   ...
   2016-11-18 01:42:17 36311 [Note] /home/philips/git/mysql-wsrep-bugs-5.6/sql/mysqld: Shutdown complete

The number after the UUID string on the "Recovered position" line is the one to watch. Pick the node that has the highest such number and edit its grastate.dat to set ``safe_to_bootstrap: 1``:

.. code-block:: console

   # GALERA saved state
   version: 2.1
   uuid:    37bb872a-ad73-11e6-819f-f3b71d9c5ada
   seqno:   -1
   safe_to_bootstrap: 1

By doing that, you indicate to Galera that you have willfully selected that node and it will allow you to bootstrap from it.


.. rst-class:: section-heading
.. rubric:: Practice

Similar to restoring from backup, restarting the entire cluster is an operation that deserves practice. In addition the data consistency protections provided by Galera, having a proven sequence of steps to perform when the occasion arises will reduce downtime and decrease the chance of accidental data loss. Last but not least, it will lower the stress on the administrator, which is an important goal in its own right.
