.. meta::
   :title: The Galera Manager
   :description: An overview of installing and using Galera Manager
   :language: en-US
   :keywords: galera cluster, gmd, galera manager, gui
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Galera Manager Documents

      .. cssclass:: here

         - :doc:`Getting Started <./galera-manager>`

      - :doc:`Installing <./gmd-install>`
      - :doc:`gmd Daemon <./gmd>`
      - :doc:`Deploying Clusters <./galera-manager-adding-clusters>`
      - :doc:`Adding Nodes <./galera-manager-adding-nodes>`
      - :doc:`Adding Users <./galera-manager-adding-users>`
      - :doc:`Loading Data <./galera-manager-initializing-data>`
      - :doc:`Monitoring a Cluster <./galera-manager-monitoring-clusters>`
      - :doc:`Upgrading <./gmd-upgrading>`
..      - :doc:`AWS Ports <./galera-manager-ports>` //outdated


.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`galera-manager`:

===================================================
The Galera Manager
===================================================

The Galera Manager is a graphical user interface for provisioning and monitoring Galera Clusters in various environments, like Amazon Web Services (AWS) or on-premises hardware. It allows an administrator to add nodes easily, and without having to configure each node, manually. Perhaps more useful is that Galera Manager provides charts for monitoring host and database metrics to ensure the proper and efficient functioning of a Galera Cluster. There are over a thousand metrics from which to choose. You may use any standard web browser for accessing Galera Manager, to administer and monitor clusters.

   .. only:: html

          .. image:: ../images/galera-manager.jpg
             :target: https://galeracluster.com/galera-mgr/
             :width: 740

   .. only:: latex

          .. image:: ../images/galera-manager.jpg
             :target: https://galeracluster.com/galera-mgr/


This section of the Codership documentation provides detailed information and instructions on how to install and configure Galera Manager.  Below is a brief summary of each aspects of the process to start using Galera Manager, with each heading linked to the related page for much more information |---| there are also links in the margin to all pages of the Galera Manager documentation. However, if you're an advanced administrator and are confident in your abilities, this page will provide you a summary of what you need to install and start using Galera Manager.

.. _`galera-manager-install-steps`:
.. rst-class:: section-heading
.. rubric:: :doc:`Install Galera Manager <./gmd-install>`

The *Galera Manager Installer* is provided to make installation and configuration of Galera Manager as simple as possible.  This section is only a brief summary of the procedure.  Some of this text contains links to other pages where you'll find more detailed information on each step.

   .. rst-class:: sub-heading indented
   .. rubric:: Choose or Create a *Galera Manager Host*

   Galera Manager is a server program (it serves client requests from both the cluster nodes and graphical frontend) so it should be installed on a host (server or other computer) which can be connected to from both the prospective cluster nodes and a computer running the graphical client.  A laptop behind a WiFi NAT is a poor choice.  You may use a local computer (e.g., a desktop or laptop computer), but most administrators would want to use a computer in the same network as the cluster nodes. E.g. if the cluster is in EC2, you'd want to use an EC2 instance, if it is on premises, then you'd use a host in the on-premises network.  It is also possible to use one of the cluster nodes, but it is recommended to have a dedicated *Galera Manager Host*.

   At this point Galera Manager Installer supports the following x86_64 Linux distributions: Ubuntu 18.04 and 20.04, CentOS 7, Debian 10 ("buster") and Debian 11 ("bullseye").

   Future releases of Galera Manager Installer may support other platforms. For now, it's recommended you use one of these distributions for *Galera Manager Host*. The Galera Manager itself will, however, manage or monitor clusters that may run on a different platform and nodes that will run either MySQL or MariaDB.

   .. rst-class:: sub-heading indented
   .. rubric:: Download the *Installer*

   After you've decided on and prepared the *Galera Manager Host*, you'll need to download the *Installer* from Codership's site at this address:

      `https://galeracluster.com/galera-manager/gm-installer <https://galeracluster.com/galera-manager/gm-installer>`_.

   .. rst-class:: sub-heading indented
   .. rubric:: Run the *Installer*

   Once the *Installer* has been downloaded, run it with superuser privileges to install Galera Manager. It will ask you some basic information: an administrative password, as well as a domain name and a site certificate, if you have these and want to use them.

   .. code-block:: console

      chmod a+x gm-installer && sudo ./gm-installer install

   When the Installer is finished, the `gmd` daemon will be running on the *Galera Manager Host*. The *Installer* will print out some bookkeeping information that you may want to save for future reference and also the address at which you can connect to `gmd` from your browser and start using it:

   .. code-block:: console

      INFO[0223] Galera Manager installation finished. Enter http://10.0.3.73 in a web browser to access.

   Check the :doc:`gmd-install` documentation page for more details on using the *Installer* and explanations of the questions you'll be asked, as well as suggestions on how to respond to them. You might also read the :doc:`gmd` page.


.. _`galera-manager-deploying-steps`:
.. rst-class:: section-heading
.. rubric:: :doc:`Deploying a Cluster <./galera-manager-adding-clusters>`

Having installed Galera Manager, you're now ready to use it to deploy a Galera cluster, including adding and configuring nodes.

   .. rst-class:: sub-heading
   .. rubric:: Access Galera Manager

   In the address field of your web browser, enter the address provided in the *Installer* output.

   If you didn't provide a certificate, your web browser may try to protect you from accessing the address. Push past those warnings until you reach the login screen. Then enter the administrative user name and password you gave when installing.

   .. rst-class:: sub-heading
   .. rubric:: Create a Cluster & Add Nodes

   After you log into Galera Manager, you may create a cluster, and then nodes to it.  Typically, one would start with three nodes |---| you can add more nodes later, or delete some if you added too many.  You will be able to choose between several node host types (``locallxd``, ``unmanaged``, ``ec2``), host OS variants and database flavors.  When you create a cluster, be sure to provide an public encryption key to facilitate manual troubleshooting via SSH connection.

   .. rst-class:: sub-heading
   .. rubric:: Log in to cluster

   If you created a cluster from scratch, you'll need to get the login credentials (i.e., user name, host address, password) to access one of the nodes with a MySQL client. This can be found by clicking on one of the nodes in Galera Manager, then its Configuration tab.  There you'll find the *DB Address* and the *DB Root Password* for accessing the database system.

.. [MOVE TO A MORE APPROPRIATE SECTION]
   .. rst-class:: sub-heading
   .. rubric:: :doc:`Secure the Ports <./galera-manager-ports>`

   When first adding hosts, all ports used by Galera Cluster and the database engine, including the administrator (i.e., ``ssh``) are open from any IP address. Someone will still need login credentials to access the hosts, but you may want to tighten the *Inbound Rules* on AWS. You'll find more information on *Inbound Rules* on the :doc:`galera-manager-ports` page.

You can find more details on deploying a cluster on the :doc:`galera-manager-adding-clusters` and the :doc:`galera-manager-adding-nodes` documentation pages. You may also find the :doc:`galera-manager-adding-users` page helpful at some point.


.. [DOES NOT SEEM TO BE USEFUL OR BELONG HERE]
   .. _`galera-manager-loading-cluster`:
   .. rst-class:: section-heading
   .. rubric:: :doc:`Load Initial Data <./galera-manager-initializing-data>`

   After installing and setting up your first Galera Cluster, you'll need to load your data into the cluster.  There are a few ways by which you can do this. Two of the most common methods are highlighted below.

   .. rst-class:: sub-heading
   .. rubric:: Back-Up & Load Data

   Assuming you have an existing MySQL database on a server somewhere, you'll need to make a back-up of its databases and then load it onto one of the new nodes to jump start Galera Cluster.  The most common methods are to use a ``mysqldump`` generated dump file, or use a utility like ``rsync`` to make a physical copy of the data directory.

   If you're using a dump file, copy it to the *Installer Host* and then use a MySQL client (e.g., ``mysql``) to load the data into MySQL or MariaDB on one of the nodes. If you made a physical copy of the data to a zipped archived file, tranfer it to one of the new nodes, stopping the node temporarily on Galera Manager while you do.

   .. rst-class:: sub-heading
   .. rubric:: Ready for Normal Usage

   After the initial data has finished loading, you may access and change data in MySQL with any MySQL client.  You may also access the data using any application you would normally use (e.g., PHP scripts accessed by end-users through a web browser).

   For more details on how to use the methods mentioned above for loading data, see the :doc:`galera-manager-initializing-data` documentation page.


.. _`galera-manager-managing-cluster`:
.. rst-class:: section-heading
.. rubric:: :doc:`Monitor a Cluster <./galera-manager-monitoring-clusters>`

With a Galera Cluster and nodes in place, including the data loaded and accessible to users, you can monitor your cluster using charts of database and host metrics in Galera Manager. Still, you may want to configure these charts or add more to suit your particular needs.

   .. rst-class:: sub-heading
   .. rubric:: Configure Charts

   By default, there are a few charts configured for commonly watched metrics.  However, there are over one-thousand metrics that you may track.  Click on the cluster in Galera Manager and you'll see the default charts. You may click the *X* at the top right of any chart to remove it.  To add a chart, click the vertical ellipsis to access a pull-down menu where you can select *Add Chart*. A dialog box will appear for you to choose the metric you want to monitor.

For more information on adding charts and related information, see the :doc:`galera-manager-monitoring-clusters` documentation page.


.. container:: bottom-links

   Galera Manager Documents

   - :doc:`Getting Started <./galera-manager>`
   - :doc:`Installing <./gmd-install>`
   - :doc:`gmd Daemon <./gmd>`
   - :doc:`Deploying Clusters <./galera-manager-adding-clusters>`
   - :doc:`Adding Nodes <./galera-manager-adding-nodes>`
   - :doc:`Adding Users <./galera-manager-adding-users>`
   - :doc:`Loading Data <./galera-manager-initializing-data>`
   - :doc:`Monitoring a Cluster <./galera-manager-monitoring-clusters>`
   - :doc:`Upgrading <./gmd-upgrading>`
..   - :doc:`Managing Ports <./galera-manager-ports>` //outdated


.. toctree::
   :hidden:
   :maxdepth: 1

   gmd-install
   galera-manager-ports
   gmd-eula
   gmd
   galera-manager-adding-clusters
   galera-manager-adding-nodes
   galera-manager-adding-users
   galera-manager-initializing-data
   galera-manager-monitoring-clusters
   gmd-upgrading


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
