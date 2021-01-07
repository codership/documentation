.. meta::
   :title: Using SSL for State Snapshot Transfers
   :description:
   :language: en-US
   :keywords: galera cluster, ssl, security, ports, sst, state snapshot transfer
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`

      Related Documents

      - :doc:`ssl-config`
      - :doc:`schema-upgrades`
      - :ref:`wsrep_OSU_method <wsrep_OSU_method>`
      - :ref:`wsrep_sst_auth <wsrep_sst_auth>`
      - :ref:`wsrep_sst_method <wsrep_sst_method>`

      Related Articles

      - :doc:`Starting a Cluster <../training/tutorials/starting-cluster>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`ssl-sst`:

==================================
SSL for State Snapshot Transfers
==================================

When you finish generating the SSL certificates for your cluster, you can begin configuring the node for their use.  Where :doc:`ssl-config` covers how to enable SSL for replication traffic and the database client, this page covers enabling it for :term:`State Snapshot Transfer` scripts.

The particular method you use to secure the State Snapshot Transfer through SSL depends upon the method you use in state snapshot transfers: ``mysqldump``, ``clone`` or ``xtrabackup``.

.. note:: For Gelera Cluster, SSL configurations are not dynamic.  Since they must be set on every node in the cluster, if you want to enable this feature with an existing cluster you need to restart the entire cluster.


.. _`ssl-mysqldump`:
.. rst-class:: section-heading
.. rubric:: Enabling SSL for ``mysqldump``

The procedure for securing ``mysqldump`` is fairly similar to that of securing the database server and client through SSL.  Given that ``mysqldump`` connects through the database client, you can use the same SSL certificates you created for replication traffic.

Before you shut down the cluster, you need to create a user for ``mysqldump`` on the database server and grant it privileges through the cluster.  This ensures that when the cluster comes back up, the nodes have the correct privileges to execute the incoming state snapshot transfers.  In the event that you use the :term:`Total Order Isolation` online schema upgrade method, you only need to execute the following commands on a single node.

#. From the database client, check that you use Total Order Isolation for online schema upgrades.

   .. code-block:: mysql

      SHOW VARIABLES LIKE 'wsrep_OSU_method';

      +------------------+-------+
      | Variable_name    | Value |
      +------------------+-------+
      | wsrep_OSU_method | TOI   |
      +------------------+-------+

   If :ref:`wsrep_OSU_method <wsrep_OSU_method>` is set to :term:`Rolling Schema Upgrade`, or ``ROI``, then you need to execute the following commands on each node individually.

#. Create a user for ``mysqldump``.

   .. code-block:: mysql

      CREATE USER 'sst_user'@'%' IDENTIFIED BY PASSWORD 'sst_password';

   Bear in mind that, due to the manner in which the SST script is called, the user name and password must be the same on all nodes.

#. Grant privileges to this user and require SSL.

   .. code-block:: mysql

      GRANT ALL ON *.* TO 'sst_user'@'%' REQUIRE SSL;


#. From the database client on a different node, check to ensure that the user has replicated to the cluster.

   .. code-block:: mysql

      SELECT User, Host, ssl_type
      FROM mysql.user WHERE User='sst_user';

      +----------+------+----------+
      | User     | Host | ssl_type |
      +----------+------+----------+
      | sst_user | %    | Any      |
      +----------+------+----------+

This configures and enables the ``mysqldump`` user for the cluster.

.. note:: In the event that you find, :ref:`wsrep_OSU_method <wsrep_OSU_method>` set to ``ROI``, you need to manually create the user on each node in the cluster.  For more information on rolling schema upgrades, see :doc:`schema-upgrades`.

With the user now on every node, you can shut the cluster down to enable SSL for ``mysqldump`` State Snapshot Transfers.

#. Using your preferred text editor, update the ``my.cnf`` configuration file to define the parameters the node requires to secure state snapshot transfers.

   .. code-block:: ini

      # MySQL Server
      [mysqld]
      ssl-ca = /path/to/ca-cert.pem
      ssl-key = /path/to/server-key.pem
      ssl-cert = /path/to/server-cert.pem

      # MySQL Client Configuration
      [client]
      ssl-ca = /path/to/ca-cert.pem
      ssl-key = /path/to/client-key.pem
      ssl-cert = /path/to/client-cert.pem

#. Additionally, configure :ref:`wsrep_sst_auth <wsrep_sst_auth>` with the SST user authentication information.

   .. code-block:: ini

      [mysqld]
      # mysqldump SST auth
      wsrep_sst_auth = sst_user:sst_password

This configures the node to use ``mysqldump`` for state snapshot transfers over SSL.  When all nodes are updated to SSL, you can begin restarting the cluster.  For more information on how to do this, see :doc:`Starting a Cluster <../training/tutorials/starting-cluster>`.


.. _`ssl-xtrabackup`:
.. rst-class:: section-heading
.. rubric:: Enabling SSL for ``xtrabackup``

The :term:`Physical State Transfer Method` for state snapshot transfers, uses an external script to copy the physical data directly from the file system on one cluster node into another.  Unlike ``rsync``, ``xtrabackup`` includes support for SSL encryption built in.

Configurations for ``xtrabackup`` are handled through the ``my.cnf`` configuration file, in the same as the database server and client.  Use the ``[sst]`` unit to configure SSL for the script.  You can use the same SSL certificate files as the node uses on the database server, client and with replication traffic.

.. code-block:: ini

   # xtrabackup Configuration
   [sst]
   encrypt = 3
   tca = /path/to/ca.pem
   tkey = /path/to/key.pem
   tcert = /path/to/cert.pem

When you finish editing the configuration file, restart the node to apply the changes.  ``xtrabackup`` now sends and receives state snapshot transfers through SSL.

.. note:: In order to use SSL with ``xtrabackup``, you need to set :ref:`wsrep_sst_method <wsrep_sst_method>` to ``xtrabackup-v2``, instead of ``xtrabackup``.


.. _`ssl-clone`:
.. rst-class:: section-heading
.. rubric:: Enabling SSL for ``clone``

Configurations for ``clone`` are handled through the ``my.cnf`` configuration file, in the same as the database server and client.  Use the ``[sst]`` unit to configure SSL for the script.  You can use the same SSL certificate files as the node uses on the database server, client and with replication traffic.

.. code-block:: ini

    # clone Configuration
    [mysqld]
    ssl-cert= /path/to/server-cert.pem
    ssl-key= /path/to/server-key.pem
    ssl-ca= /path/to/ca.pem

    [client] # or [sst]
    ssl-cert= /path/to/client-cert.pem
    ssl-key= /path/to/client-key.pem
    ssl-ca= /path/to/ca.pem
    ssl-mode= VERIFY_CA

Client SSL configuration on Donor node must match server SSL configuration
on Joiner. (That means: mysql client using client SSL configuration from
Joiner should be able to connect to server on Donor) Client SSL configuration
on Joiner must match CLONE SSL configuration on donor. If CLONE plugin on
Donor is not loaded, or if CLONE SSL configuration is empty then server SSL
configuration on Donor is used.

If for some reason general client SSL configuration is undesirable, client
SSL configuration for ``clone`` SST can be put into the `[sst]` section of
the configuration file. It will be used first.


.. container:: bottom-links

   Related Documents

   - :doc:`ssl-config`
   - :doc:`schema-upgrades`
   - :ref:`wsrep_OSU_method <wsrep_OSU_method>`
   - :ref:`wsrep_sst_auth <wsrep_sst_auth>`
   - :ref:`wsrep_sst_method <wsrep_sst_method>`

   Related Articles

   - :doc:`Starting a Cluster <../training/tutorials/starting-cluster>`
