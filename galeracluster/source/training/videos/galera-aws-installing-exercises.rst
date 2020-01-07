.. meta::
   :title: Training Video Exercises |---| Installing a Galera Cluster on AWS
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Training Courses <../courses/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      - :doc:`Firewall Settings <../../documentation/firewall-settings>`
      - :doc:`firewalld <../../documentation/firewalld>`
      - :doc:`Installing Galera <../../documentation/install>`
      - :doc:`Node Provisioning <../../documentation/node-provisioning>`
      - :doc:`SELinux <../../documentation/selinux>`
      - :doc:`State Transfer <../../documentation/state-transfer>`
      - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

      Other Resources

      - `MariaDB Repo. Generator <https://downloads.mariadb.org/mariadb/repositories/>`_
      - `Galera Repository <http://releases.galeracluster.com/>`_
      - `Configure Repo File <../../documentation/install-mysql.html#mysql-yum-repo>`_

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article training-exercises
.. _`exercises-galera-aws-installing`:

==========================
Training Video Exercises
==========================

---------------------------------------
Installing a Galera Cluster on AWS
---------------------------------------

.. container:: video-abstract list-col2-3

   These exercises are part of the training video, *Installing a Galera Cluster on AWS*.  They correspond to what is presented, and should be done after each section is viewed, unless otherwise noted.

   Before starting these exercises, make sure you have all of the requirements and preparations in place.

.. container:: list-col1-3

   .. rst-class:: training-video-resources
   .. rubric:: Requirements & Preparation

   .. rst-class:: training-video-resources

      - AWS account with access to the EC2 console.

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - `Example Configuration <galera-mariadb-installing-examples.html>`_
      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Exercises

Before starting an exercise, read it fully and carefully. The headings for each set of exercises corresponds to the section with the same name in the training video.  Make notes for yourself, after successfully performing each exercise, for when you have to do these tasks later for yourself.


.. rst-class:: sub-heading
.. rubric:: Creating AWS Instances

Do these exercises after viewing the first three sections of the training video:  *Galera Cluster Overview*, *Encryption Key*, and *Creating AWS Instances*. Don’t install any software or configure the nodes, yet.

.. rst-class:: list-exercises

1. Generate an encryption key for accessing nodes.  Then log into AWS and create three instances with a distribution of Linux you prefer.

2. Create a security group to use with your instances. Add rules to allow traffic among them, using their internal IP addresses. Open TCP ports 22, 3306, 4444, 4567, and 4568 for each node. Also open UDP port 4567 for each.

.. rst-class:: sub-heading
.. rubric:: Installing Software on Nodes

Do these exercises after viewing *Installing Software on Nodes* on the training video. Don’t configure the nodes until the next section.

.. rst-class:: list-exercises

3. If you prefer to use MySQL, use a web browser to go to Codership’s web site (see links in margin) to get the URL’s for the latest wsrep-MySQL and the Galera Cluster packages.  Use a text editor to create a repository file on each node and include the URLs you copied.  See the margin for links to the Codership’s documentation page which shows how to construct a repository file.  If you prefer to use MariaDB, go to The MariaDB Foundation page to construct a repository file based on the Linux distribution and version you’re using. Get at least version 10.4 of MariaDB.

4. Install MySQL or MariaDB, and Galera on each node.  When finished, start ``mysqld`` on each node |---| don’t bootstrap Galera. For MySQL, grep the MySQL log for root’s temporary password.  For MariaDB, there is no password, initially. Run ``mysql_secure_install`` on each node and change the root password, as well as respond to the other questions it asks.  Then try logging into MySQL or MariaDB with the mysql client as root with the new password.  Exit and shutdown ``mysqld``.


.. rst-class:: sub-heading
.. rubric:: Configuring Nodes & Opening Ports

Do these exercises after viewing the two sections related to this combined title. MySQL or MariaB should be down on each node; don’t start ``mysqld`` again until the next section.

.. rst-class:: list-exercises

5. Edit the database configuration file to include settings needed for Galera Cluster.  There’s a link at the top under Student Materials for an example configuration file. Don’t start ``mysqld`` yet. Configure each node before proceeding to the next exercise.

6. Configure either SELinux or Firewalld or both to open the following ports:  TCP 22, TCP 3306. TCP 4444, TCP & UDP 4567, and TCP 4568. If you want to use only SELinux or only Firewalld, disable the one not used.

.. rst-class:: sub-heading
.. rubric:: Starting Galera

This is the core of the training video. You may encounter problems as you do these exercises. Don’t let it frustrate you, but don’t stop trying to complete them. This is important. Keep at it until you’re able to do them.

.. rst-class:: list-exercises

7. Choose a node to be the seed node |---| anyone will be fine. Start MySQL and Galera on the one node by using the ``mysqld_bootstrap`` script.  If you’re using MariaDB, start it with Galera by using the ``galera_new_cluster`` script. If there are any errors, shutdown ``mysqld`` and read the full error messages, as well as look through the database log for clues. Resolve any problems and keep trying until you get it started. Then execute ``SHOW STATUS`` with the ``LIKE`` operator to see if Galera is running.

8. Once you have the first node running MySQL or MariaDB, and Galera, start mysqld on one of the other nodes |---| don’t use the ``mysqld_bootstrap`` and ``galera_new_cluster`` scripts.  If there are any errors, shutdown mysqld and resolve them until you get it started. Execute the ``SHOW STATUS`` statement with the ``LIKE`` operator to see the ``wsrep_cluster_size``. It should have a value of 2.

9. Download the dump file containing the ``company`` database (see link at the top under Student Materials) onto the first node.  There’s one for MySQL and another for MariaDB: use the one that matches your database system. Both were created with ``mysqldump``, so use the ``mysql`` client to load the data.  When it’s finished, check the second node to see if it replicated the data.

10. Start ``mysqld`` on the third node.  After it has successfully joined the cluster, look to see if it has replicated the ``company`` database. Enter the ``CREATE DATABASE`` statement to create a database without tables. Check that the other nodes replicated it.

11. Shut down all of the nodes and restart them, using ``mysqld_bootstrap`` to start only the first node, which should be the last one that was shutdown. If you have problems, check the ``grastate.dat`` file in the data directory to ensure the ``safe_to_bootstrap`` parameter is set to 1.


.. note::

  If you struggled at any point in doing these exercises, especially in getting the Galera nodes started, you might want to do them again.  Start with fresh installations of the servers, without MySQL or MariaDB or Galera Cluster.  If you use the same servers, before doing the exercises again, uninstall the database software and Galera, and delete the data directory.  Do the exercises multiple times until you’re able to install, configure, and start a Galera cluster without any problems.

.. container:: bottom-links

   Related Documents

   - :doc:`Firewall Settings <../../documentation/firewall-settings>`
   - :doc:`firewalld <../../documentation/firewalld>`
   - :doc:`Installing Galera <../../documentation/install>`
   - :doc:`Node Provisioning <../../documentation/node-provisioning>`
   - :doc:`SELinux <../../documentation/selinux>`
   - :doc:`State Transfer <../../documentation/state-transfer>`
   - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

   Other Resources

   - `MariaDB Repo. Generator <https://downloads.mariadb.org/mariadb/repositories/>`_
   - `Galera Repository <http://releases.galeracluster.com/>`_
   - `Configure Repo File <../../documentation/install-mysql.html#mysql-yum-repo>`_


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
