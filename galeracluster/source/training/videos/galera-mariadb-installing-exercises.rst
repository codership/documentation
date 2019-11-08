.. meta::
   :title: Training Video Exercises |---| Installing Galera Cluster with MariaDB
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      - :doc:`Firewall Settings <../../documentation/firewall-settings>`
      - :doc:`firewalld <../../documentation/firewalld>`
      - :doc:`Installing Galera <../../documentation/install>`
      - :doc:`Node Provisioning <../../documentation/node-provisioning>`
      - :doc:`SELinux <../../documentation/selinux>`
      - :doc:`State Transfer <../../documentation/state-transfer>`
      - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

      Related Articles

      Other Resources

      - `MariaDB Repo. Generator <https://downloads.mariadb.org/mariadb/repositories/>`_
      - `Galera Repository <http://releases.galeracluster.com/>`_

.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article training-exercises
.. _`exercises-galera-mariadb-installing`:

==========================
Training Video Exercises
==========================

---------------------------------------
Installing Galera Cluster with MariaDB
---------------------------------------

.. container:: video-abstract list-col2-3

   These exercises are part of the training video, *Installing Galera Cluster with MariaDB*.  They correspond to what was taught, and should be done after each viewing section, unless otherwise noted.

   Before starting these exercises, make sure you have all of the requirements and preparations in place.

.. container:: list-col1-3

   .. rst-class:: training-video-resources
   .. rubric:: Requirements & Preparation

   .. rst-class:: training-video-resources

      - Test Servers:  3
      - Operating System:  Linux
      - Software:  Don’t install MariaDB or Galera Cluster in preparation.

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - :doc:`Example Configuration <galera-mariadb-installing-examples>`
      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_

.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Exercises

Before starting an exercise, read it fully and carefully. The headings for each set of exercises corresponds to the section with the same name in training video.  Make notes for yourself as you go along, for when you have to do these tasks for your job or for yourself.


.. rst-class:: sub-heading
.. rubric:: Installing Software on Nodes

Do these exercises after viewing the first two sections of the training video:  *Galera Cluster Overview*, and *Installing Software on Nodes*. Don’t configure the nodes until the next section.

.. rst-class:: list-exercises

1. Use a web browser to go to The MariaDB Foundation’s web site (see link in margin) to use their repository generator to get the contents of a repository file for the latest version of MariaDB |---| at  least version 10.4, which includes Galera Cluster.  Use a text editor to create a repository file on each node, using the repo file contents from The Foundation site.

2. Install MariaDB on each node.  When finished, start ``mysqld`` on each |---| don’t bootstrap Galera. Then run ``mysql_secure_install`` on each to set the root password |---| initially, there is no root password |---| as well as respond to the other questions the script asks.  Then try logging into MariaDB with the ``mysql`` client as root with the new password.  Exit and shutdown ``mysqld``.

.. rst-class:: sub-heading
.. rubric:: Configuring Nodes & Opening Ports

Do these exercises after viewing the section with the two titles. MariaDB should be down on each node; don’t start ``mysqld`` again until the next section.

.. rst-class:: list-exercises

3. Edit the MariaDB configuration file to include settings needed for Galera Cluster.  There’s a link in the Student Materials section at the top, for an example configuration file. Don’t start ``mysqld`` yet. Configure each node before proceeding to the next exercise.

4. Configure either SELinux or Firewalld or both to open the following ports:  TCP 22, TCP 3306. TCP 4444, TCP and UDP 4567, and TCP 4568. If you intent to use only SELinux or only Firewalld, disable the one not used.

.. rst-class:: sub-heading
.. rubric:: Starting Galera

This is the core of the training video. You may encounter problems as you do these exercises. Don’t let it frustrate you. It’s important. So don’t stop trying until you’re able to do them.

.. rst-class:: list-exercises

5. Choose a node to be the seed node |---| anyone will be fine. Start MariaDB and Galera on it by using the ``galera_new_cluster`` script.  If there are any errors, shutdown ``mysqld`` and read the full error messages, as well as look through the MariaDB log for clues. Resolve any problems and keep trying until you get it started. Execute ``SHOW STATUS`` with the ``LIKE`` operator to see if Galera is running.

6. Once you have the first node running MariaDB and Galera, start mysqld on one of the other nodes |---| don’t use ``galera_new_cluster``.  If there are any errors, shutdown mysqld on the node and resolve the problems until you get it started. When it’s working properly, ``wsrep_cluster_size`` status variable should have a value of 2.
7. Download the dump file containing the company database (see link at the top under Student Materials) onto the first node.  Since it was made with ``mysqldump``, use the ``mysql`` client to load the data.  When it’s finished, check the second node to see if it replicated the data.

8. Start ``mysqld`` on the third node.  After it has successfully joined the cluster, look to see if it has replicated the company database. Enter the ``CREATE DATABASE`` statement to create a database without tables. Check that the other nodes replicated it.

9. Shut down all of the nodes and restart them, using ``galera_new_cluster`` to start only the first node, which should be the last one that was shutdown. If you have problems, check the ``grastate.dat`` file in the data directory to ensure the ``safe_to_bootstrap`` parameter is set to 1.

.. note::

  If you struggled at any point in doing these exercises, especially in getting the Galera nodes started, you might want to do them again.  Start with fresh installations of the servers, without MariaDB or Galera Cluster.  If you use the same servers, before doing the exercises again, uninstall MariaDB and Galera, and delete MariaDB’s data directory.  Do the exercises multiple times, until you’re able to install, configure, and start a Galera cluster without any problems.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
