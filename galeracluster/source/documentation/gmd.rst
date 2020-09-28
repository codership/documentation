.. meta::
   :title: The Galera Manager Daemon (gmd)
   :description:
   :language: en-US
   :keywords: galera cluster, gmd, galera manager, gui, installation, install
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

      Galera Manager Documents

      - :doc:`Getting Started <./galera-manager>`
      - :doc:`Installing <./gmd-install>`
      - :doc:`AWS Ports <./galera-manager-ports>`

      .. cssclass:: here

        - :doc:`gmd Daemon <./gmd>`

      - :doc:`Deploying Clusters <./galera-manager-adding-clusters>`
      - :doc:`Adding Nodes <./galera-manager-adding-nodes>`
      - :doc:`Adding Users <./galera-manager-adding-users>`
      - :doc:`Loading Data <./galera-manager-initializing-data>`
      - :doc:`Monitoring a Cluster <./galera-manager-monitoring-clusters>`
      - :doc:`Upgrading <./gmd-upgrading>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`galera-manager-daemon-gmd`:

===================================================
Galera Manager Daemon (``gmd``)
===================================================

The Galera Manager is driven by the ``gmd`` daemon running on the server to be used to create clusters, the one used to add and remove nodes, and especially to monitor the Galera Cluster.  For information on installing ``gmd``, see the documentation page, :doc:`gmd-install`.


.. _`gmd-process`:
.. rst-class:: section-heading
.. rubric:: ``gmd`` Process

If Galera Manager was installed on a server or an *AWS Instance*, you can enter something like the following from the command-line to check that it's running:

.. code-block:: console
   :caption: Checking if Galera Manager Daemon is Running (Example 1)

   ps -e |grep gmd

   5810 ?        00:00:18 gmd

The results showing the process identification number and the amount of time ``gmd`` has been running will be different on your server. Although it's unlikely you'll need to restart ``gmd``, to do so you may enter the following from the command-line:

.. code-block:: console
   :caption: Restarting the Galera Manager Daemon (Example 2)

   systemctl restart gmd

You can replace ``restart`` with ``stop`` to shutdown the Galera Manager daemon |---| and use ``start`` to start it later.  If the server is rebooted, ``gmd`` is set to start automatically.


.. _`gmd-configuration`:
.. rst-class:: section-heading
.. rubric:: Configuration File

When you installed Galera Manager, the *Installer* created a configuration file for ``gmd`` based on the responses you gave. You don't have to create it yourself. However, if you want to change some of the information you provided when installing, you can edit the configuration file. It's located in the sub-directory, ``/etc/default/`` and called, ``gmd``.

The ``gmd`` configuration file will look something like this:

.. code-block:: console
   :caption: Contents of Galera Manager Configuration File (Example 3)

   ARGS="--rsa-private-key=/var/lib/gmd/jwt-rsa.key"
   GMD_CONFIG_DIR=/var/lib/gmd
   GMD_LOGS_DIR=/var/log/gmd
   INFLUXDB_URL=https://gmd:8hCh2GeYv9@34.217.207.40:8091
   PROMETHEUS_URL=https://34.217.207.40:8092

There are few settings here.  You can change the values with a simple text editor. Just remember to restart ``gmd`` for the changes to take effect.  See above for how to restart the daemon.



.. _`gmd-logs`:
.. rst-class:: section-heading
.. rubric:: gmd Logs

In the previous section, you may have noticed the location of the log files: ``/var/log/gmd``.  Should you have difficulty starting ``gmd`` or encounter similar problems, you can check this directory for log files containing messages that may indicate the cause.  Below is an example of the contents of that log file directory:

.. code-block:: console
   :caption: List of Galera Manager Log Files (Example 3)
   :emphasize-lines: 3, 4, 9, 10, 13

   ls -1 /var/log/gmd

   cluster-testeroo.log
   default.log
   host-hoster-jfebk-stdout.log
   host-hoster-jfebk.log
   host-hoster-lisvt-stdout.log
   host-hoster-lisvt.log
   host-hoster-mlksh-stdout.log
   host-hoster-mlksh.log
   node-noder-jfebk.log
   node-noder-lisvt.log
   node-noder-mlksh.log

There's a log file for the ``gmd`` daemon (i.e., ``default.log``), one for the cluster, a pair for each host, and one for each node.

You may be confused as to the difference between a host and a node in this context. A host has to do with the computer system on which the Galera Cluster software is installed. This includes software configuration, network traffic, as well as where particular software like Galera Manager and MySQL are running. Whereas, a node has to do with the activities, the interactions of the Galera Cluster: Is the node available and handling database client traffic?  Is it synchronized with the other nodes in the cluster?

What's important to an administrator, though, is knowing where to find log messages to troubleshoot problems that may be encountered.  Below are descriptions of what may be found in each log, with the most information recorded in the host standard output log (e.g., ``host-hoster-mlksh-stdout.log``).


.. _`gmd-log-default`:
.. rst-class:: sub-heading
.. rubric:: Default Log

The main log file for the ``gmd`` daemon, the ``default.log`` file, contains information related to starting and stopping the daemon.  Here's an excerpt from such a log file:

.. code-block:: console
   :caption: Excerpt from Galera Manager's Default Log (Example 4)

   time="2020-05-18T08:05:19Z" level=info msg="Starting gmd"
   time="2020-05-18T08:05:19Z" level=info msg="Listening on 127.0.0.1:8000"
   time="2020-05-18T08:05:19Z" level=info msg="ConfigDir = /var/lib/gmd"
   time="2020-05-18T08:05:19Z" level=info msg="LogsDir = /var/log/gmd"

As you can see, it records when it started the ``gmd`` daemon, on which IP address and port it's listening for connections from users (i.e., ``admin``), and the directories for configuration and log files.


.. _`gmd-log-cluster`:
.. rst-class:: sub-heading
.. rubric:: Cluster Log

As mentioned above, there's a log file for the cluster. It's name contains the name of the cluster appended to it (i.e., ``testeroo`` from the examples on other pages of this documentation section). This log file contains some very basic information on the settings of the cluster. Below is an example of its contents:

.. code-block:: console
   :caption: Excerpt from Galera Manager's Cluster Log (Example 5)

   time="2020-06-07T06:27:39Z" level=info msg="cluster record created" cluster-name=testeroo

It's not much since it's from a new installation of Galera Manager, one used in examples elsewhere in this documentation.  It contains the date and time the cluster was created, as well as the name of the cluster. As a result of that name, this log file is named, ``cluster-testeroo.log``.


.. _`gmd-log-hosts`:
.. rst-class:: sub-heading
.. rubric:: Host Logs

As mentioned earlier, there is a pair of log files for each host in the cluster.  One is labeled ``host``, followed by the name of the host and the extention, ``.log``  This file contains primarily entries showing the data time or changes to the host's status.

Below is an excerpt from the ``host-hoster-mlksh.log`` file from the examples used here in documentation on Galera Manager:

.. code-block:: console
   :caption: Excerpt from a Galera Manager Host Log (Example 6)

   time="2020-06-07T06:28:58Z" level=info
      msg="setting deployment status to pending" host-name=hoster-mlksh
   time="2020-06-07T06:30:04Z" level=info
     msg="setting deployment status to ok" host-name=hoster-mlksh

This is actually two lines of entries, but we broke the lines to fit more easily on the screen. Still, there's not much information here.  Nevertheless, you might write a custom shell script to parse this file to check for the latest entry, looking for when the deployment status is not *ok*, and send you a message saying as much |---| and then have ``cron`` run that script frequently at regular intervals.  Or you could just keep Galera Manager open in a window on your computer.

The other log file for each host is labeled ``host``, followed by the name of the host, then ``stdout`` and the extention, ``.log`` (e.g., ``host-hoster-mlksh-stdout.log``). This log file contains the messages generated by the host server when activities happen, when various commands, utilities and other programs are run by Galera Manager.  If these commands and all were executed manaully, some messages would normally be shown on the screen (i.e., the standard output). However, since they're run in the background, there's no one to see them. So Galera Manager writes them to a log file for each host.

These host ``stdout`` log files are extensive. They contain information on updating Galera Manager software, network traffic, and many other logistical system information related to Galera.  As a result, they can become fairly large files.  But they can also be useful when trying to troubleshoot a problem with Galera Manager software |---| but not the synchronizing and accessing of data within the cluster, on nodes.


.. _`gmd-log-nodes`:
.. rst-class:: sub-heading
.. rubric:: Node Logs

In the log directory for ``gmd``, there is a log file for each node. As mentioned earlier, these log files contain information related to the nodes of the cluster, their interactions with each other.  Below is an excerpt from the ``node-noder-mlksh.log`` file from examples elsewhere in this documentation:

.. code-block:: console
   :caption: Excerpt from a Galera Manager Node Log (Example 7)

   time="2020-06-07T06:31:54Z" level=info msg="updating cluster IPs" ctx=update-cluster-ips node-name=noder-mlksh
   time="2020-06-07T08:15:09Z" level=info msg="checking node status" node-name=noder-mlksh
   time="2020-06-07T08:15:10Z" level=info msg="node status is healthy" node-name=noder-mlksh
   time="2020-06-07T08:15:10Z" level=info msg="already started" node-name=noder-mlksh

Notice these entries are related to nodes in the cluster having started, being ready to accept MySQL client traffic, and insync |---| that is to say, the node's health.

Should one of the nodes have problems that are not reflected in the metrics you're tracking in Galera Manager, you could check the log for that node for an indication of what's wrong with it. Afterwards, you might want to add the appropriate metrics to Galera Manager to monitor the situation more closely and conveniently from within Galera Manager.  For more information on adding metrics to track in Galera Manager, see the :doc:`galera-manager-monitoring-clusters` documentation page.


.. container:: bottom-links

   Galera Manager Documents

   - :doc:`Getting Started <./galera-manager>`
   - :doc:`Installing <./gmd-install>`
   - :doc:`AWS Ports <./galera-manager-ports>`
   - :doc:`gmd Daemon <./gmd>`
   - :doc:`Deploying Clusters <./galera-manager-adding-clusters>`
   - :doc:`Adding Nodes <./galera-manager-adding-nodes>`
   - :doc:`Adding Users <./galera-manager-adding-users>`
   - :doc:`Loading Data <./galera-manager-initializing-data>`
   - :doc:`Monitoring a Cluster <./galera-manager-monitoring-clusters>`
   - :doc:`Upgrading <./gmd-upgrading>`

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
