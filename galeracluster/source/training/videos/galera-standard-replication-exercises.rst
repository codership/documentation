.. meta::
   :title: Training Video Exercises |---| Standard Replication & Galera Cluster
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

        .. cssclass:: sub-links

           - :doc:`Troubleshooting <../../kb/trouble/index>`
           - :doc:`Best Practices <../../kb/best/index>`

        - :doc:`Training <../index>`

        .. cssclass:: sub-links

           - :doc:`Tutorial Articles <../tutorials/index>`

           .. cssclass:: here

           - :doc:`Training Videos <./index>`

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

        - `Galera Repository <http://releases.galeracluster.com/>`_

.. role:: raw-html(raw)
   :format: html

.. cssclass:: library-article training-exercises
.. _`exercises-galera-standard-replication`:

==========================
Training Video Exercises
==========================

---------------------------------------
Standard Replication & Galera Cluster
---------------------------------------

.. container:: video-abstract list-col2-3

   These exercises are part of the training video, *Standard Replication & Galera Cluster*.  They correspond to what was taught, but they are to be done after each of the two major parts of the training video:  the Standard Replication part, which includes the first three sections; and the Galera Cluster part, which includes the last three sections (see the outline on the page where the video is posted).

   Before starting these exercises, make sure you have all of the requirements and preparations in place.

.. container:: list-col1-3

   .. rst-class:: training-video-resources
   .. rubric:: Requirements & Preparation

   .. rst-class:: training-video-resources

      - Test Servers:  3
      - Operating System:  Linux
      - Open Ports:  TCP 22, TCP 3306. TCP 4444, TCP & UDP 4567, TCP 4568
      - Software:  MySQL or MariaDB, Galera Cluster

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
.. rubric:: Standard Replication Exercises

Do these exercises after viewing the three sections on Standard Replication |---| before starting the Galera Cluster half of the training video.

.. rst-class:: list-exercises

1. Configure two servers to use MySQL or MariaDB and standard replication |---| but not Galera Cluster.  See the link at the top in the Student Materials list for a sample configuration file.  Be sure to run on each the mysqld_secure_installation script to set the password and all. Restart the MySQL daemon on each.

2. Choose one server to be the master and the other to be the slave.   Use the ``CREATE USER`` statement on the master to create a user with the privilege ``REPLICATION CLIENT``.  Set its host address and password.

3. Use mysqldump to dump all of the databases on the master, although it will only have the system databases.  Be sure to use the ``--master-data`` and ``--flush-logs`` option.  Then use ``scp`` to copy the dump file from the master to the slave. Restart ``mysqld`` on the slave when you finish. Use the ``mysql`` client to process the dump file on the slave.

4. Execute the ``CHANGE MASTER`` statement on the slave to provide the slave with the replication user name and password, and the port and IP address for communicating with the master.

5. Use the ``START SLAVE`` statement to start the slave replicating.  Use ``SHOW SLAVE STATUS`` to check the slave’s status and to see if there are any errors.  Execute ``SHOW MASTER STATUS`` on the master.  Compare the name of the master’s binary and position to the corresponding values on the slave in the results of ``SHOW SLAVE STATUS``. If everything agrees and there are no error, enter a ``CREATE DATABASE`` statement on the master and see if it’s replicated on the slave.  If there are any problems, resolve them or start over.  Don’t do the next exercises until replication is working properly.

6. Download the sample database, the ``company`` database to the master server.  There’s one for MySQL and another for MariaDB: use the one that matches your database system. Both were created with mysqldump, so use the ``mysql`` client to load the data onto the master.  When you’re finished, check the slave to see if it has replicated the database and its data.

.. rst-class:: sub-heading
.. rubric:: Galera Cluster Exercises

Do these exercises after completing the previous exercises, and after having viewed the three sections of the training video on Galera Cluster.

.. rst-class:: list-exercises

7. Edit the configuration on the two servers used for the previous exercises: remove anything added for replication.  Configure all three servers for Galera Cluster (see link in Student Materials for example). Drop the ``company`` database on each server.  Shutdown ``myqld`` on all three servers.

8. If you’ve installed MySQL, use ``mysqld_boot_strap`` to start one of the servers, to be the seed. If it won’t start, stop ``mysqld`` and review the error messages and logs to resolve the problem. When it seems to be working, use ``SHOW STATUS``, with the ``LIKE`` operator, to see the wsrep parameters, to check if Galera Cluster is running.

9. Start ``mysqld`` on each of the other two servers.  If you get errors, review the logs to resolve ant problems.  When each starts without an error, check the status parameter, ``wsrep_cluster_size`` to see if the cluster size reflects the number of nodes that are running. Keep trying until you’re able to start the nodes and they all join together to form a cluster.

10. On one of the nodes, use the ``mysql`` client to load the dump file made for your database system.  Do this on only one node.  As soon as you’re finished, log into each of the other nodes to confirm the database and its tables have been replicated on them.



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
