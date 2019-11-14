.. meta::
   :title: Training Video Exercises |---| Monitoring a Galera Cluster
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

      - :doc:`Galera Monitoring <../tutorials/galera-monitoring>`

      Other Resources

      - `Galera Repository <http://releases.galeracluster.com/>`_

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
.. _`exercises-galera-monitoring`:

==========================
Training Video Exercises
==========================

-----------------------------
Monitoring a Galera Cluster
-----------------------------

.. container:: video-abstract list-col2-3

   These exercises are part of the training video, *Monitoring a Galera Cluster*.  They correspond to what was taught, and should be done after viewing each section, unless otherwise noted.

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


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Exercises

Before starting an exercise, read it fully and carefully. The headings for each set of exercises corresponds generally to the section with the same name in training video.


.. rst-class:: sub-heading
.. rubric:: Galera Status Variables

Do these exercises after viewing the first two sections of the training video:  *Galera Monitoring Overview*, and *Galera Status Variables*.

.. rst-class:: list-exercises

1. With MySQL or MariaDB, and Galera running on all three nodes, execute the ``SHOW STATUS`` statement with the ``LIKE`` operator to obtain a list of all variables with the prefix wsrep. Scroll through the variables to familiarize yourself with them.  Make note of ones you think would be useful to monitor.

2. Execute ``SHOW STATUS`` again, but retrieve the variables which will tell you the status of the cluster and another for the state of the node on which it's executed. Do it again, but this time get only the cluster size.

3. Check the replication health by checking the flow control, the ``wsrep_local_recv_%`` and the ``wsrep_local_send_%`` status variables.

.. rst-class:: sub-heading
.. rubric:: Server Logs

Do these exercises after viewing the section of the training video entitled, *Server Logs*. MySQL or MariaDB should running on all nodes.

.. rst-class:: list-exercises

4. On one of the nodes, execute the ``SHOW VARIABLES`` statement to determine the path and name of the error log.  Use a tool like ``more`` or ``less`` to view the contents of the log.  Search for error messages and warnings.  Familiarize yourself with how Galera records information in the log.

5. In the database configuration file for one of the nodes, set Galera to log information about conflicts. Also, enable debugging.  In a separate terminal window, use ``tail`` with the ``-f`` option to monitor entries in the error log.  Then restart the database software and Galera.  Enter some transactions and observe the new entries in the error log.

.. rst-class:: sub-heading
.. rubric:: Notification Command & Customized Scripts

These exercises will take some time to do, but they'll be a good exercise for learning how to develop a notification command of your own.

.. rst-class:: list-exercises

6. Create a notification command script using ``bash`` or another shell scripting language. You may use the example from the video as a starting point. There's a link to it at the top under Student Materials.  You'll have to modify it for your system. Set it to record information in a simple text file. Try executing it manually by giving it the parameters it expects from the command-line.  Check its log file to see the results.

7. Once you have the notification script in good shape, add the ``wsrep_notify_cmd`` paramter to the database configuration file for one of the nodes and provide the path and name of the script. Do this while all three nodes are running. Restart the node that is hosting the script.

8. With all three nodes running and the notification script in place on one node, take down one of the other nodes.  Check the notification command's log to see what it recorded.  Start the node that's down and check the log again.  Notice how much it recorded and didn't record.  Try to improve the information logged.

9. Modify your script to alert you of a node down.  Use your imagination and skills to use some method that would be fairly dependable.  When you have it done, test it by shutting down a node.

.. rst-class:: sub-heading
.. rubric:: Third-Party Software

This exercise is meant to acquaint you with the third-party software for monitoring Galera, and to get you thinking about using them in production.

.. rst-class:: list-exercises

10. Look into one of the third-party software available for monitoring a Galera Cluster.  Familiarize yourself with what's available |---| for free and at a price.  Try to find a free one |---| or one that at least allows for free trials |---| that might work for your situation.  If you're not sure, try the Nagios scripts (see link in margin). Whatever you choose,  download it and try it on your test servers.

.. container:: bottom-links

   Related Documents

   - :doc:`Firewall Settings <../../documentation/firewall-settings>`
   - :doc:`firewalld <../../documentation/firewalld>`
   - :doc:`Installing Galera <../../documentation/install>`
   - :doc:`Node Provisioning <../../documentation/node-provisioning>`
   - :doc:`SELinux <../../documentation/selinux>`
   - :doc:`State Transfer <../../documentation/state-transfer>`
   - :doc:`wsrep Options <../../documentation/mysql-wsrep-options>`

   Related Articles

   - :doc:`Galera Monitoring <../tutorials/galera-monitoring>`

   Other Resources

   - `Galera Repository <http://releases.galeracluster.com/>`_


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:

.. |br| raw:: html

  <br/>
