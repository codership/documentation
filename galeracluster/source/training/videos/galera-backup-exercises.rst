.. meta::
   :title: Training Video Exercises |---| Making Back-Ups with Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.

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

      Related Documents

      - :doc:`Firewall Settings <../../documentation/firewall-settings>`
      - :doc:`firewalld <../../documentation/firewalld>`
      - :doc:`Installing Galera <../../documentation/install>`
      - :doc:`Node Provisioning <../../documentation/node-provisioning>`
      - :doc:`SELinux <../../documentation/selinux>`
      - :doc:`State Transfer <../../documentation/state-transfer>`
      - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

      Other Resources

      - :doc:`Install MySQL Galera (video) <./galera-mysql-installing>`
      - :doc:`Install MariaDB Galera (video) <./galera-mariadb-installing>`
      - `Galera Repository <http://releases.galeracluster.com/>`_

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`
   - :ref:`search`


.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article training-exercises
.. _`exercises-galera-backup`:

==========================
Training Video Exercises
==========================

---------------------------------------
Making Back-Ups with Galera Cluster
---------------------------------------

.. container:: video-abstract list-col2-3

   These exercises are part of the training video, *Making Back-Ups with Galera Cluster*. There are exercises related to what was taught in each section, except for the section entitled *Back-Up & Restoration Plan*. That particular section is in a sense another set of exercises.

   Before starting these exercises, make sure you have all of the requirements and preparations in place.

.. container:: list-col1-3

   .. rst-class:: training-video-resources
   .. rubric:: Requirements & Preparation

   .. rst-class:: training-video-resources

      - Test Servers:  4
      - Operating System:  Linux
      - Open Ports:  TCP 22, TCP 3306. TCP 4444, TCP & UDP 4567, TCP 4568
      - Database Software:  MySQL or MariaDB (vs. 10.4 or higher)
      - Other Software: * Galera (Only 3)

   .. rst-class:: training-video-resources
   .. rubric:: Student Materials

   .. rst-class:: training-video-resources

      - `Company Database <https://galeracluster.com/library-media/databases/company.tgz>`_


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Exercises

Before starting an exercise, read it fully and carefully. The headings for each set of exercises before correspond to the section with the same name in training video.


.. rst-class:: sub-heading
.. rubric:: Back-Up Basics

Do these exercises after viewing the first two sections of the training video:  *Galera Cluster Overview*, and *Installing Software on Nodes*. Don’t configure the nodes until the next section.

.. rst-class:: list-exercises

1. Download the sample database called, ``company`` from the Coderhsip site (see margin) onto one of the nodes. It’s a dump file made with ``mysqldump``. With MySQL or MariaDB and Galera running, use the ``mysql`` client to load the data on one node. When finished, check the other nodes to ensure they have replicated the ``company`` database. Delete the dump file.

2. Make a directory called, ``backups``, and a sub-directory in it called, ``temp``. Use the ``SET`` statement to desync a different node. Execute a ``SHOW STATUS`` statement to check that the node has a status of *Desync*. Execute ``SHOW VARIABLES`` to determine the data directory. Next, use ``rsync`` to back-up of all of the database to the ``temp`` sub-directory, in the ``backups`` directory. When it’s finished, use ``tar`` to create a zipped archive file (for example, ``db-backup.tgz``). Disable desync on the node.

3. On one of the Galera nodes, use the ``DROP DATABASE`` statement to drop the ``company`` database. Check to see that it’s replicated on the other two nodes. Now shutdown all of the nodes. When they’ve all stopped, use the back-up file to restore the data directory on the node where it’s located. Then start that node and check if the ``company`` database is back. After that, start the other two nodes. Give them a couple of minutes before checking that the ``company`` database has been restored on them.

.. rst-class:: sub-heading
.. rubric:: Using Standard Replication

This set of exercises require all four servers mentioned in the requirements above:  three with MySQL or MariaDB, and Galera installed and running; the fourth server with only MySQL or MariaDB.

.. rst-class:: list-exercises

4. On one of the Galera nodes, configure it also to use standard replication, to be a primary. See the link in at the top under Student Materials for an example configuration file. On the fourth server, the one without Galera Cluster, configure it to use standard replication, to be a replica to the primary. If you’re unfamiliar with standard replication, you might watch our training video on *Standard Replication and Galera Cluster* |---| or read the related article on the same topic.

5. Create a user with ``REPLICATION CLIENT`` on the Galera node you’ve designated to be a primary. Use ``mysqldump`` to make a copy of all of the databases on the primary. Be sure to use the ``--flush-logs`` and ``--master-data`` options.

6. Use the ``scp`` command to copy the dump file you created on the primary, to the replica. Load the data on the replica, using the ``mysql`` client. Execute the ``CHANGE MASTER TO`` (MySQL < 8.4) or ``CHANGE REPLICATION SOURCE TO`` (MySQL > 8.4) statement to provide the IP address and port 3306, as well as the replication user name and password. Then start replication by executing either the ``START SLAVE`` (MySQL < 8.4) or ``START REPLICA`` (MySQL > 8.4) statement on the replica. Check that replication is running fine with either ``SHOW SLAVE STATUS`` (MySQL < 8.4) or ``SHOW REPLICA STATUS`` (MySQL > 8.4, MariaDB > 10.5.1) on the replica. Try changing some data on the primary and see if it replicates to the replica.

7. Make a directory called ``backups``, with a sub-directory within it called ``temp``. Stop the replica and use `mysqldump` to make a back-up on it to a the ``backups``, ``temp`` sub-directory. Copy the binary log files, as well as the MySQL configuration file to the temporary back-up sub-directory. Then tar and zip the back-up files. Start the replica again and make sure replication is running.

.. rst-class:: sub-heading
.. rubric:: Using Galera Arbitrator

For the exercises in this section and the remaining sections, you won’t need the replica server. You can shut it down. You’ll only use the three servers with Galera installed on them.

.. rst-class:: list-exercises

8. Create a configuration file for Galera Arbitrator (see link at the top under Student Materials for an example). Write a simple back-up script that will use ``rsync`` |---| or use the one linked above. Execute it using ``garbd`` from the command-line. As soon as it starts, check the status of the :term:`Donor Node` for comments to see if it’s desynced during the back-up.

9. Write another simple back-up script that will use ``mysqldump`` and execute it. Make sure it gives a different name to the back-up file than in the previous exercise.

.. rst-class:: sub-heading
.. rubric:: Restoring Nodes and a Cluster

.. rst-class:: list-exercises

10. Drop the ``company`` database on one of the nodes. Check that the deletion of the database has occurred on all of the Galera nodes and the replica. Choose one Galera node for restoration. Shutdown the ``mysqld`` daemon on the other two nodes.

11. Using the back-up you made with ``rsync``, in the previous set of exercises, restore the data to one of the nodes. Start the other Galera nodes, one at a time. Verify that they’ve been restored.

12. Drop the ``company`` database again. This time restore the data with the dump file, using the ``mysql`` client. After a reasonable amount of time, verify that they’ve all been restored.


.. note::

  If you’re unfamiliar with how to install Galera Cluster, watch our training video on installing Galera with MySQL, or MariaDB (see the margin for links) or read the related articles. You’ll need to configure MySQL or MariaDB and Galera Cluster and start them. There’s a link in the margin for the recommended configuration for certain sections here.

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

   - :doc:`Install MySQL Galera (video) <./galera-mysql-installing>`
   - :doc:`Install MariaDB Galera (video) <./galera-mariadb-installing>`
   - `Galera Repository <http://releases.galeracluster.com/>`_


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
