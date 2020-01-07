.. meta::
   :title: Resolving Node Crashes during SST
   :description: "Discusses how to resolve a problem with rsync or other tool stalling during SST."
   :language: en-US
   :keywords: galera cluster, sst, rsync, stalled, hangs
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`SST <../../documentation/sst>`
      - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
      - :ref:`wsrep_sst_method <wsrep_sst_method>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-node-crash-during-sst`:

==================================================
Node Crashes during SST
==================================================

.. rst-class:: article-stats

   Length: 463 words; Published: April 1, 2014; Updated: November 4, 2019; Category: State Transfers; Type: Troubleshooting

When a new node joins a cluster, it will request data from the cluster.  One node, known as a *donor*, will use a :term:`State Snapshot Transfer` (SST) method to provide a full copy of the data to the new node, known as the *joiner*.  Depending on how the nodes are configured, they will typically use the utilities, ``mysqldump`` or ``rsync`` to transfer the data.  All of this usually works well, but it doesn't always. This KB article will consider a common scenario in which problems may occur.


.. rst-class:: section-heading
.. rubric:: Scenario

You can set the :ref:`wsrep_sst_method <wsrep_sst_method>` option to whatever tool you want to use to make state transfers. DBAs typically set this to ``mysqldump`` or ``rsync``.  When a new node joins, :term:`State Snapshot Transfer` begins, and file system processes are started for the tool used (e.g., ``rsync``). Below is show the results of running ``ps`` on the joining node during a state transfer:

.. code-block:: console

   ps -e | grep rsync

   14718 ? 00:00:00 wsrep_sst_rsync
   14766 ? 00:00:00 rsync
   14799 ? 00:00:00 rsync
   14800 ? 00:00:00 rsync

If the node crashes before the state transfer is complete, it may cause the process or processing running ``rsync``, or whatever tool you're using, to stall, occupying the port and not allowing you to restart the node. When this happens, the error logs for the database server (i.e., ``/var/log/mysqld.log``) will show that the port is in use, although it isn't.  You'll have to fix this problem.

.. rst-class:: section-heading
.. rubric:: Solution

There are a few ways you can resolve this situation.  The simplest way is to kill the stalled processes.  To do this, you'll need to know the process identification number. However, first you may want to stop ``mysqld`` on the joining node, to start fresh. You could enter something like the following on the stalled node, from the command-line:

.. code-block:: console

   systemctl stop mysqld

   ps -e | grep rsync

   14800 ? 00:06:05 rsync

In the example here, the results show that the process identification number is ``14800``.  Using this information, you might enter the following from the command-line:

.. code-block:: console

   kill -9 14800

If there are multiple processes running, which can be the case with ``rsync``, you'll have to kill all of them.  Sometimes the killall command will suffice:

.. code-block:: console

   killall rsync

However, this usually doesn't work.  Instead, you'll have to use the ``kill`` command for each process.  It's tedious, but necessary. Once you have killed the orphaned process, it will free the relevant ports and allow you to start ``mysqld`` on the new node.

After restarting the node, if the processes handling the state transfer stalls again, it wasn't a fluke. There's a persistent problem with the network or security or something else.  Check the server logs and the database logs on the server to determine the cause.

.. container:: bottom-links

   Related Documents

   - :doc:`SST <../../documentation/sst>`
   - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
   - :ref:`wsrep_sst_method <wsrep_sst_method>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
