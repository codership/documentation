================================
 Versioning Information
================================
.. _`Versioning Information`:



Galera Cluster for MySQL is available in binary software packages for several different Linux distributions, as well as in source code for other distributions and other Unix-like operating systems, such as FreeBSD and Solaris. 

For Linux distributions, binary packages in 32-bit and 64-bit for both the MySQL database server with the wsrep API patch and the :term:`Galera Replication Plugin` are available from the `Codership Repository <http://releases.galeracluster.com>`_.  These include support for:

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

.. note:: For more information on the installation process, see :doc:`galerainstallation`.


---------------------------
 Release Numbering Schemes
---------------------------
.. _`galera-release-number`:

Software packages for Galera Cluster have their own release numbering schemas.  There are two schemas to consider in version numbering:

- **Galera wsrep Provider**  Also, referred to as the :term:`Galera Replication Plugin`.  The wsrep Provider uses the following versioning schema: ``<wsrep API main version>.<Galera version>``.  For example, release 24.2.4 indicates wsrep API version 24.x.x with Galera wsrep Provider version 2.4.


- **MySQL Server with wsrep API patch**  The second versioning schema relates to the database server.  Here, the MySQL server uses the following versioning schema ``<MySQL server version>-<wsrep API version>``.  For example, release 5.5.29-23.7.3 indicates a MySQL database server in 5.5.29 with wsrep API version 23.7.3.
   
For instances of Galera Cluster that use the MariaDB or Percona XtraDB database servers, consult their respective documentation for version and release information.


-----------------------------------------------------
Third-party Implementations of Galera Cluster
-----------------------------------------------------
.. _`third-party-galera`:

In addition to the Galera Cluster for MySQL, the reference implementation from Codership Oy, there are two third party implementations of Galera Cluster.  These are,

- `Percona XtraDB Cluster <http://www.percona.com/software/percona-xtradb-cluster>`_ is a high-availability and high-scalability solution for MySQL users.  Percona XtraDB CLuster integrates Percona XtraDB Server with the Galera library of high-availability solutions in a single product package.

- `MariaDB Galera Cluster <https://mariadb.com>`_ uses the Galera library for the replication implementation.  To interface with the Galera Replication Plugin, MariaDB is enhanced to support the replication API definition in the wsrep API project.  Additionally, releases of MariaDB Server from version 10.1 on are packaged with Galera Cluster.

  For more information, see `What is MariaDB Galera Cluster <https://mariadb.com/kb/en/mariadb/what-is-mariadb-galera-cluster/>`_.






.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
