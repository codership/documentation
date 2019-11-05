.. meta::
   :title: Using mysqldump to Synchronize and Provision Nodes
   :description:
   :language: en-US
   :keywords: galera cluster, mysqldump, backup, sst, synchronizing
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

      - :ref:`wsrep_sst_method <wsrep_sst_method>`
      - :ref:`wsrep_sst_auth <wsrep_sst_auth>`

      Related Articles


.. cssclass:: library-document
.. _`mysqldump`:

=======================
Enabling ``mysqldump``
=======================

The :term:`Logical State Transfer Method`, ``mysqldump`` works by interfacing through the database server rather than the physical data.  As such, it requires some additional configuration, besides setting the :ref:`wsrep_sst_method <wsrep_sst_method>` parameter.


.. _`sst-privileges`:
.. rst-class:: section-heading
.. rubric:: Configuring SST Privileges

In order for ``mysqldump`` to interface with the database server, it requires root connections for both the donor and joiner nodes.  You can enable this through the :ref:`wsrep_sst_auth <wsrep_sst_auth>` parameter.

Using a text editor, open the ``wsrep.cnf`` file--it should be in the ``/etc/mysql/conf.d/`` directory.  Add a line like the following to that file:

.. code-block:: ini

   # wsrep SST Authentication
   wsrep_sst_auth = wsrep_sst_username:password

You would use your own authentication parameters in place of ``wsrep_sst_user`` and ``password``. This line will provide authentication information that the node will need to establish connections. Use the same values for every node in the cluster.


.. _`sst_authorization`:
.. rst-class:: section-heading
.. rubric:: Granting SST Privileges

When the database server starts, it will read from the ``wsrep.cnf`` file to get the authentication information it needs to access another database server.  In order for the node to accept connections from the cluster, you must also create and configure the State Snapshot Transfer user through the database client.

In order to do this, you need to start the database server.  If you haven't used this node on the cluster before, start it with replication disabled.  For servers that use ``init``, execute the following from the command-line:

.. code-block:: console

   # service mysql start --wsrep-on=off

For servers that use ``systemd``, instead execute this from the command-line:

.. code-block:: console

   # systemctl start mysql --wsrep-on=OFF

When the database server is running, log into the database using a client and execute the ``GRANT ALL`` statement for the IP address of each node in the cluster.  You would do this like so:

.. code-block:: mysql

   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node1_IP_address'
	IDENTIFIED BY 'password';
   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node2_IP_address'
	IDENTIFIED BY 'password';
   GRANT ALL ON *.* TO 'wsrep_sst_user'@'node3_IP_address'
 	IDENTIFIED BY 'password';

You would, of course, modify the text above to use your user names, IP addresses, and passwords. These SQL statements will grant each node in the cluster access to the database server on this node.  You need to run these SQL statements on each node to allow ``mysqldump`` in state transfers among them.

If you have not yet created the cluster, you can stop the database server while you configure the other nodes.  To stop MySQL on servers that use ``init``, run the execute the following from the command-line:

.. code-block:: console

   # service mysql stop

For servers that use ``systemd``, you would execute the following from the command-line to shutdown MySQL:

.. code-block:: console

   # systemctl stop mysql

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
