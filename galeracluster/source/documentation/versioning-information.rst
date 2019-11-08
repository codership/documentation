.. meta::
   :title: Galera Cluster Versioning Information
   :description:
   :language: en-US
   :keywords: galera cluster, versions, versioning information, releases
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


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

      - :doc:`Galera Installation <../training/tutorials/galera-installation>`

      Related Articles


.. cssclass:: library-document
.. _`versioning-information`:

=========================
Versioning Information
=========================

Galera Cluster for MySQL is available in binary software packages for several different Linux distributions, as well as in source code for other distributions and other Unix-like operating systems, such as FreeBSD and Solaris.

For Linux distributions, binary packages in 32-bit and 64-bit for both the MySQL database server with the wsrep API patch and the :term:`Galera Replication Plugin` are available from the `Codership Repository <https://releases.galeracluster.com>`_.  These include support for:

- Red Hat Enterprise Linux
- Fedora
- CentOS
- SUSE Linux Enterprise Server
- openSUSE
- Debian
- Ubuntu

By installing and configuring the Codership Repository on any of these systems, you can install and update Galera Cluster for MySQL through your package manager.  In the event that you use a distribution of Linux that is not supported, or if you use another Unix-like operating system, source files are available on GitHub, at:

- `MySQL Server <https://github.com/codership/mysql-wsrep>`_ with the wsrep API patch.
- `Galera Replication Plugin <https://github.com/codership/galera>`_.
- `glb <https://github.com/codership/glb>`_, the Galera Load Balancer.

For users of FreeBSD and similar operating systems, the Galera Replication Plugin is also available in ports, at ``/usr/ports/databases/galera``, which corrects for certain compatibility issues with Linux dependencies.

For more information on the installation process, see :doc:`Galera Installation <../training/tutorials/galera-installation>`.


.. _`galera-release-number`:
.. rst-class:: section-heading
.. rubric:: Release Numbering Schemes

Software packages for Galera Cluster have their own release numbering schemas.  There are two schemas to consider in version numbering:

- **Galera wsrep Provider**  Also, referred to as the :term:`Galera Replication Plugin`.  The wsrep Provider uses the following versioning schema: ``<wsrep API main version>.<Galera version>``.  For example, release 24.2.4 indicates wsrep API version 24.x.x with Galera wsrep Provider version 2.4.


- **MySQL Server with wsrep API patch**  The second versioning schema relates to the database server.  Here, the MySQL server uses the following versioning schema ``<MySQL server version>-<wsrep API version>``.  For example, release 5.5.29-23.7.3 indicates a MySQL database server in 5.5.29 with wsrep API version 23.7.3.

For instances of Galera Cluster that use the MariaDB database server, consult the MariaDB documentation for version and release information.


.. _`third-party-galera`:
.. rubric:: Third-party Implementations of Galera Cluster
   :class: section-heading

In addition to the Galera Cluster for MySQL, the reference implementation from Codership Oy, there is a third-party implementation of Galera Cluster - `MariaDB Galera Cluster <https://mariadb.com>`_ which uses the Galera library for the replication implementation.  To interface with the Galera Replication Plugin, MariaDB has been enhanced to support the replication API definition in the wsrep API project.  Additionally, releases of MariaDB Server starting from version 10.1 on are packaged with Galera Cluster already included.  For more information, see `What is MariaDB Galera Cluster <https://mariadb.com/kb/en/mariadb/what-is-mariadb-galera-cluster/>`_.

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
