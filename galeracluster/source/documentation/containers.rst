.. meta::
   :title: Galera Cluster Container Deployments
   :description:
   :language: en-US
   :keywords: galera cluster, container deployment, docker
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

      - :ref:`wsrep_node_address <wsrep_node_address>`
      - :ref:`wsrep_node_name <wsrep_node_name>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`



.. cssclass:: library-document
.. _`containers`:

=========================
Container Deployments
=========================

In the standard deployment methods for Galera Cluster, a node runs on a server in the same manner as would an individual stand-alone instance of MySQL or MariaDB.  In container deployments, a node runs in a containerized virtual environment on the server.

You may find these methods useful in portable deployments across numerous machines, testing applications that depend on Galera Cluster, process isolation for security, or scripting the installation and configuration process.

The configuration for a node running in a containerized environment remains primarily the same as a node running in the standard manner.  However, there are some parameters that draw their defaults from the base system configurations.  You will need to set these, manually. Otherwise, the jail will be unable to access the host file system.


- :ref:`wsrep_node_address <wsrep_node_address>`: A node determines the default address from the IP address on the first network interface. Jails cannot see the network interfaces on the host system. You need to set this parameter to ensure that the cluster is given the correct IP address for the node.

- :ref:`wsrep_node_name <wsrep_node_name>`: The node determines the default name from the system hostname. Jails have their own hostnames, distinct from that of the host system.

Bear in mind that the configuration file must be placed within the container ``/etc`` directory, not that of the host system.

.. container:: bottom-links

   Related Documents

   - :ref:`wsrep_node_address <wsrep_node_address>`
   - :ref:`wsrep_node_name <wsrep_node_name>`


.. toctree::

   docker
   jails
