.. meta::
   :title: Galera Cluster Parameters, Status, and Functions
   :description:
   :language: en-US
   :keywords: galera cluster, mysql, mariadb, wsrep options, wsrep functions
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      - :doc:`galera-parameters`
      - :doc:`galera-status-variables`
      - :doc:`system-tables`
      - :doc:`GLB Parameters <glb-parameters>`
      - :doc:`mysql-wsrep-options`
      - :doc:`mysql-wsrep-functions`
      - :doc:`versioning-information`
      - :doc:`xtrabackup-options`

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`reference`:

===========
Reference
===========

In the event that you need more information about particular variables or parameters or status variable or would like a clearer explanation about various terms used in the documentation, these chapters provide general reference material to Galera Cluster configuration and use.

.. _`ref-vars`:
.. rst-class:: rubric-1
.. rubric:: Variable Reference

Defining persistent configurations in Galera Cluster is done through the underlying database server, using the ``[mysqld]`` unit in the ``my.cnf`` configuration file.  These chapters provide reference guides to the base replication status and configuration variables as well as the specific wsrep Provider options implemented through the Galera Replication Plugin.

- :doc:`mysql-wsrep-options`

  In addition to the standard configuration variables available through the database server, Galera Cluster implements several that are unique and specific to fine-tuning database replication.  This chapter provides a reference guide to these new configuration variables in Galera Cluster

- :doc:`mysql-wsrep-functions`

  There are a few Galera specific functions. This page lists and explains them, as well as gives examples of their use.

- :doc:`galera-parameters`

  The Galera Replication Plugin, which acts as the wsrep Provider, includes a number of parameters specific to its operation.  This chapter provides a reference guide to the various wsrep Provider options available.

- :doc:`galera-status-variables`

  In addition to the standard status variables available through the database server, Galera Cluster also implements several that you can use in determining the status and health of the node and the cluster.  This chapter provides a reference guide to these new status variables in Galera Cluster.


.. _`ref-utils`:
.. rst-class:: rubric-1
.. rubric:: Utility Reference

In some cases your configuration or implementation may require that you work with external utilities in your deployment of Galera Cluster.  These chapters provide reference guides for two such utilities: XtraBackup and Galera Load Balancer.

- :doc:`glb-parameters`

  In high availability situations or similar cases where nodes are subject to high traffic situations, you may find it beneficial to set up a load balancer between your application servers and the cluster.  This chapter provides a reference guide to the Codership implementation: the Galera Load Balancer.

- :doc:`xtrabackup-options`

  When you manage State Snapshot Transfers using Percona XtraBackup, it allows you to set various parameters on the state transfer script the node uses from the ``my.cnf`` configuration file.  This chapter provides a reference guide to options available to XtraBackup.

- :doc:`system-tables`

  This page provides information on the Galera specific system tables.  These were added as of version 4 of Galera.

.. _`ref-misc`:
.. rst-class:: rubric-1
.. rubric:: Miscellaneous References

- :doc:`versioning-information`

  While the documentation follows a convention of 3.x in speaking of release versions for Galera Cluster, in practice the numbering system is somewhat more complicated: covering releases of the underlying database server, the wsrep Provider and the wsrep API.  This chapter provides a more thorough explanation of versioning with Galera Cluster.

- :doc:`legal-notice`

  This page provides information on the documentation copyright.

- :doc:`glossary`

  In the event that you would like clarification on particular topics, this chapter provides reference information on core concepts in Galera Cluster.

- :ref:`genindex`

  In the event that you would like to check these concepts against related terms to find more information in the docs, this chapter provides a general index of the site.


.. toctree::
   :maxdepth: 2
   :hidden:

   mysql-wsrep-options
   mysql-wsrep-functions
   galera-parameters
   galera-status-variables
   system-tables
   xtrabackup-options
   glb-parameters
   versioning-information
   legal-notice
   glossary
