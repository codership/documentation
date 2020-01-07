.. meta::
   :title: Resolving Requested State Transfer Failures
   :description:
   :language: en-US
   :keywords:
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

      - :doc:`State Transfers <../../documentation/sst>`
      - :doc:`TCP/UDP Ports </../../documentation/firewall-settings>`
      - :ref:`wsrep_node_name <wsrep_node_name>`
      - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
      - :ref:`gmcast.segment <gmcast.segment>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-requested-state-transfer-failed`:

================================
Requested State Transfer Failed
================================

.. rst-class:: article-stats

   Length: 649 words; Published: April 1, 2014; Updated: November 6, 2019; Category: State Transfers; Type: Troubleshooting

When a new node joins a cluster, it will try to synchronize with the cluster by getting a full copy of the databases from one of the other nodes.  This is known as a :doc:`State Transfer <../../documentation/sst>`.  It will use a tool like ``rsync`` or ``mysqldump``, depending on how the :ref:`wsrep_sst_method <wsrep_sst_method>` option was set. Although this usually works well, sometimes it will fail.  This KB article discusses such a situation.


.. rst-class:: section-heading
.. rubric:: Scenario

Suppose a new node joins a cluster |---| this is known as a joiner node.  This is assuming that the node has in fact joined the cluster, but just hasn't been able to synchronize the data with the other nodes.  When it joins the cluster, it will look for another node, known as a donor, to give it a copy of the databases by the :term:`State Snapshot Transfer` (SST) method.  Normally, this starts almost immediately and is completed fairly quickly, depending on the size of the databases and how busy are the nodes.

Suppose further that an excessive amount of time passes without the SST starting. This can be disconcerting. To see what's going on, you could check the database server's error log, on the joiner node. It may contain a message like this:

.. code-block:: text

   Node 0 (XXX) requested state transfer from '*any*'.
   Selected 1 (XXX) as donor.

This error message indicates that no node was explicitly designated to be the donor node. You may also see this message on the joiner:

.. code-block:: text

   Requesting state transfer failed: -11(Resource temporarily
   unavailable).  Will keep retrying every 1 second(s).


As for the node's status, if you execute the ``SHOW STATUS`` statement, for the ``wsrep_local_state_comment`` variable, you won't see the desired ``Synced`` status:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+----------------+
   | Variable_name             | Value          |
   +---------------------------+----------------+
   | wsrep_local_state_comment | Waiting on SST |
   +---------------------------+----------------+

The joiner node will do its duty and continue to retry the state transfer request.  However, you may need to intercede to resolve the problem, to get the node synchronized for the cluster.


.. rst-class:: section-heading
.. rubric:: Solution

Behind the scenes, the *Group Communication* module will select potential donors based on what it knows about the status of each node. These nodes will have to be in a ``SYNCED`` state.  Nodes that have the same :ref:`gmcast.segment <gmcast.segment>` wsrep Provider option are preferred. Otherwise, the joiner will select the first in the list of available synced nodes. If the joiner node can't find a free node that shows as ``SYNCED``, though, state transfer will not occur.

The first step to resolving this problem is to determine if the other nods are in fact not synchronized.  One way to determine which are synchronized is to execute the following SQL statement on each node:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_local_state_comment';

   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_local_state_comment | Synced |
   +---------------------------+--------+

When you find at least one node that is synchronized, get the node name by executing ``SHOW VARIABLES`` to get the value of :ref:`wsrep_node_name <wsrep_node_name>` on each synchronized node, like so:

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_node_name';

   +-----------------+----------+
   | Variable_name   | Value    |
   +-----------------+----------+
   | wsrep_node_name | galera-2 |
   +-----------------+----------+

Using those node names |---| you can designate more than one |---| to set the donor on the joiner node.  You'd do this by using the SET statement to set the :ref:`wsrep_sst_donor <wsrep_sst_donor>` variable to the synchronized node's name.  Here's an example of how you might do that:

.. code-block:: mysql

   SET GLOBAL wsrep_sst_donor = 'galera-2,galera-5';

This informs the cluster that one of the nodes named (i.e., ``galera-2`` and ``galera-5``) should be used as the donor. You would execute it on one of the synchronized nodes. It will be replicated to all of the nodes. Incidentally, it may be set in the configuration file, but that may not be necessary since the state transfer failing might be a temporary problem.

.. code-block:: mysql

   SHOW VARIABLES LIKE 'wsrep_sst_donor';

   +-----------------+-------------------+
   | Variable_name   | Value             |
   +-----------------+-------------------+
   | wsrep_sst_donor | galera-2,galera-3 |
   +-----------------+-------------------+

Once you've nominated nodes to be donors, assuming the joiner has in fact joined the cluster, initiating state transfer should happen immediately and without any further problem.  If it doesn't, confirm that there aren't any problems with your network connection. Also, confirm that the needed ports aren't being blocked by SELinux or a firewall. In particular, make sure port 4568 is open: it's used for State Snapshot Transfers.

.. container:: bottom-links

   Related Documents

   - :doc:`State Transfers <../../documentation/sst>`
   - :doc:`TCP/UDP Ports </../../documentation/firewall-settings>`
   - :ref:`wsrep_node_name <wsrep_node_name>`
   - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
   - :ref:`gmcast.segment <gmcast.segment>`

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
