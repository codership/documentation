.. meta::
   :title: Installing Galera Manager
   :description:
   :language: en-US
   :keywords: galera cluster, gmd, galera manager, gui, installation, install
   :copyright: Codership Oy, 2014 - 2022. All Rights Reserved.


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

      - :doc:`Getting Started <./galera-manager>`

      .. cssclass:: here

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
.. _`gmd-install`:

===================================================
Installing Galera Manager
===================================================

.. _`galera-manager-installer-requirements`:
.. rst-class:: section-heading
.. rubric:: Galera Manager host requirements.

To use Galera Manager, you need to install it on a computer that
  a) can be accessed from the cluster nodes you want to manage or monitor;
  b) can be accessed from the computer where you'd want to display the GUI.

Normally that would be a computer in the same network as the prospective cluster nodes. Additionally you may want to consider providing sufficient disk space for the  logging and metrics data. Technically Galera Manager can run on one of the cluster nodes, but it is recommended to use a dedicated machine.

Galera manager can use SSL encryption for all communications. However this requires the host to be accessible via a domain name, not just an IP address. Externally resolvable domain name is required to utilize external Certificate Authority.


.. _`galera-manager-installer-download`:
.. rst-class:: section-heading
.. rubric:: Download the *Installer*

The *Installer* is a simple installation program for installing Galera Manager. When you run it, you will be asked a series of questions about configuring Galera Manager. After that it will download, install and configure required software packages. When it's finished, the ``gmd`` daemon will be started on the *Installer Host*, allowing you to use this server to deploy new Galera clusters in different environments, as well as monitor already existing clusters.

Below are more details on these steps to download and run the *Installer*.  The questions you'll be presented when installing are fairly self-explanatory.  However, you may want to read this page before beginning, in case there are questions about which you want to know more before starting the installation.

To install Galera Manager, you'll need to download the *Installer* to the computer chosen as the Galera Manager host. Currently *Installer* runs on the following x86_64 Linux distributions: Ubuntu 18.04 and 20.04, CentOS 7 and 8, Debian 10 ("buster"). Eventually, the *Installer* will be made available for other distributions.

After you've decided on and prepared the *Galera Manager Host*, you'll need to download the *Installer* from Codership's site at this address:

      `https://galeracluster.com/galera-manager/gm-installer <https://galeracluster.com/galera-manager/gm-installer>`_.

.. code-block:: console
   :caption: Making *Galera Manager Installer* Executable (Example 1)

   chmod +x gm-installer

Having downloaded the installation program and made it executable, you're ready to run the *Installer* to install Galera Manager.


.. _`galera-manager-installer-start`:
.. rst-class:: section-heading
.. rubric:: Start the Installer

There are two options available at this time when starting the *Installer*: ``install`` and ``certificates``.  The ``install`` option is necessary to install Galera Manager.  The ``certificates`` option is used to generate your own, self-signed SSL certificates for encryption.  Both options may be given together.

Note that to safely use SSL encryption Galera Manager host needs to be accessible through a valid DNS name (domain names given by Amazon EC2 don't count). The *Installer* will refuse to configure SSL encryption if the host has only an IP address. Galera Manager will retain full functionality working via unencrypted links.

Below is how you would start the *Installer* with only the ``install`` option. You'll have to run it with superuser privileges:

.. code-block:: console
   :caption: Starting Installation of *Galera Manager Installer* (Example 2)

   sudo ./gm-installer install

After starting the *Installer*, you will first be asked to accept the Galera Manager End-User Licensing Agreement (EULA).  Below is how this question will be presented |---| although it might change slightly in future releases:

.. code-block:: console
   :caption: Message about User Agreement from the *Installer* (Example 3)

   To use GMD you must accept EULA.
   Press [a] to accept it, [r] to read the EULA text, [n] to reject EULA.

If you're willing to accept the agreement, enter ``a``.  If you'd like to read the agreement, enter ``r`` and it will be displayed on the screen |---| along with the opportunity again to accept or reject the agreement.  You can also read :doc:`the agreement<./gmd-eula>` in the documentation before even starting to install.


.. _`galera-manager-installer-repositor`:
.. rst-class:: section-heading
.. rubric:: User Names & Passwords

Next you'll be asked for Galera Manager repository address. If you've been given a link to a private repository, you'll have to enter your user name and password for the repository. Then you'll be asked for the login and password of the initial administrator of Galera Manager.  You may want to ensure you have answers to the following questions:

.. code-block:: console
   :caption: Installation Credential Questions from the *Installer* (Example 4)

   GMD Package Repository URL (blank for default):
   GMD Package Repository User:
   GMD Package Repository Password:
   GMD Admin User Login [admin]:
   GMD Admin Password:

The default user name is *admin*.  Enter whatever password you'd like to use for the administrator.  You'll be able to remove this user later and add a replacement administrator later, as well as add other users with lesser privileges. This is covered on the :doc:`galera-manager-adding-users` page.


.. _`galera-manager-installer-domains`:
.. rst-class:: section-heading
.. rubric:: Domains & Certificates

You'll next need to provide either an IP address or a domain name for Galera Manager, the address on which you are running the *Installer*. This is the server where you'll be accessing Galera Manager. Here are the related questions you will be presented:

.. code-block:: console
   :caption: *Installer* Messages about Site Address and Certification (Example 5)

   By what domain name or IP address this service will be reached?
   (Note that an externally resolvable domain name is needed to use an external
   Certification Authority, otherwise we will have to resort to self-signed
   certificates for SSL if encryption is required):
   Enter your domain name or IP of the server:

An IP address works well, but you won't be able to utilize an external certification authority, neither you'll be able to use self-signed certificates.

.. code-block:: console
   :caption: *Installer* Warning using an IP Address (Example 6)

   Since you entered an IP address, SSL won't be available.

As this notification implies, SSL won't be available if Galera Manager host does not have a domain name.

If you chose to provide a resolvable domain name for Galera Manager host, you will have several options to set up SSL encryption (HTTPS protocol) to protect all Galera Manager connections (from both the GUI client and cluster nodes):

.. code-block:: console
   :caption: *Installer* Asking to Use a Secure Protocol (Example 7)

   Enter your domain name or IP of the server: gm.example.com
   Enable https? [Y/n]
   Use LetsEncrypt Certbot to autogenerate the certificates [Y/n]:

Answering *Yes* to the above question will set up automatic certificates generation and renewal using LetsEncrypt site as a Certificate Authority.  *NOTE:* not all domain names are accepted by LetsEncrypt, e.g. domain names autogenerated by AWS EC2 are not.  If you want to set up your own Certificate Authority and/or use your own certificates, answer *No* and you will be offered to provide them:

.. code-block:: console
   :caption: *Installer* Questions about SSL credentials (Example 8)

   Use LetsEncrypt Certbot to autogenerate the certificates [Y/n]: n
   Do you want to provide your own SSL CA? [y/N] y
   Use your own SSL certificate (y), or let installer generate one (n)? [y/N] y
   SSL CA Certificate [ca.crt]:
   SSL CA Certificate Key [ca.key]:
   SSL Host Certificate [ssl.crt]:
   SSL Host Certificate Key [ssl.key]:

NOTE: if you want to specify your own Certificate Authority, you need to make sure that it is known to your GUI frontend as well, otherwise it won't be able to confirm the validity of the Galera Manager certificate and most likely will refuse to connect with the warning about security risk.

Also you will be responsible to re-generate your own SSL certificate after it expires.

.. _`galera-manager-installer-closing-messages`:
.. rst-class:: section-heading
.. rubric:: Closing Messages

After you finish answering all of the questions presented to you by the *Installer*, it will install and configure the software needed and start Galera Manager.  You'll see messages regarding this pass by on the screen.  At the end, if it's successful, you'll see a message like this:

.. code-block:: console
   :caption: Final Messages after Successfully Installing Galera Manager (Example 9)
   :emphasize-lines: 1, 4, 9

   INFO[0223] Galera Manager installation finished. Enter http://10.0.3.73 in a web browser to access. Please note, you chose to use an unencrypted http protocol, such connections are prone to several types of security issues. Always use only trusted networks when connecting to the service.
   INFO[0223] Logs DB url: http://10.0.3.73:8081
   Metrics DB url: http://10.0.3.73:8082
   IMPORTANT: ensure TCP ports 80, 8081, 8082 are open in firewall.
   INFO[0223] Below you can see Logs DB credentials (if once asked):
   DB name: gmd
   DB user: gmd
   DB password: yAl4p84vR8
   The installation log is located at /tmp/gm-installer.log

Note the ports that need to be opened on Galera Manager host.

.. _`galera-manager-installer-ports`:
.. rst-class:: sub-heading
.. rubric:: TCP Ports

Regarding ports, notice the line in the example above about TCP ports 80, 8081, 8082. You'll need to make sure ports 8081, 8082 are accessible from the prospective nodes, and port 80 - from the GUI client.

If you deploy Galera Manager on AWS, those ports are closed by default.  Go to the EC2 console in AWS, and click on *Security Groups* in the left margin.  Then look for the security group for the server on which you installed Galera Manager. Edit the *Inbound Rules* for that group to open those ports (see the screenshot below).

.. figure:: ../images/galera-manager-aws-inbound-rules-gmd.png
   :width: 600px
   :alt: AWS Inbound Rules for Galera Manager
   :class: document-screenshot

   AWS Inbound Rules for Galera Manager (Figure 1)

In the example in this screenshot, notice that we set port 22 to the administrator's IP address to restrict access, in addtion to requiring an encryption key to log in.  The other ports are accessible from anywhere so that you can access Galera Manager from wherever you and other administrators may be located.  You may have noticed that port 3306 or other ports used by MySQL and Galera are not included in the *Inbound Rules* above. Those are needed by the nodes, not Galera Manager. When you add nodes, Galera Manager will add them to each host's *Inbound Rules*.  You'll find more on these nuances by reading the :doc:`galera-manager-ports` page of this documentation.


.. _`galera-manager-installer-logs-failure`:
.. rst-class:: sub-heading
.. rubric:: Logs & Installation Failure

In the last lines of the installation message, there's also the login name and password for accessing the InfluxDB database for the logs for the nodes. You wouldn't normally need to know these unless you're trying to debug something very unusual. They're used by Galera Manager behind-the-scenes. The logs are viewable within Galera Manager.

Should you encounter problems installing Galera Manager, though, check the installation log.  It will be located in your server's temporary directory (e.g., ``/tmp``).  You can see the file path and name of the installation log in the last line of a successful installation, as shown above.  It's a simple and tidy text file that's easy to review, if you need it.


.. _`gmd-running`:
.. rst-class:: section-heading
.. rubric:: Galera Manager Daemon

Once you've answered all of the questions presented to you by the *Installer*, it will finish the installation and start the ``gmd`` daemon.  You can enter something like the following from the command-line to check that it's running:

.. code-block:: console
   :caption: Checking if Galera Manager Daemon is Running (Example 10)

   ps -e |grep gmd

   30472 ?        00:00:40 gmd

The results showing the process identification number and the amount of time ``gmd`` has been running will be different on your server. For more information on the ``gmd`` daemon, or to learn how to make changes to some of its settings, see the documentation page called, :doc:`gmd`.


.. _`galera-manager-deploy`:
.. rst-class:: section-heading
.. rubric:: Connect to Galera Manager

After you've finished installing, you may log into Galera Manager with a standard web browser by entering the address where you installed it.  At the end of the installation, there was a message like this one:

.. code-block:: console
   :caption: Installation Message containing URL for Galera Manager (Example 11)
   :emphasize-lines: 2

   INFO[0213] Galera Manager installation complete.
   Direct your browser to http://34.217.114.37 to use it.
   ...

In the example here, a domain name wasn't used during the installation, so the URL has an IP address. If you provided a domain name, though, you would enter that domain name in your browser:  ``https://my-domain.com``.

If you didn't enable ``https`` when installing, you would instead start the URL with ``http`` (i.e., without the ``s``). Be aware that without that extra security layer, your connections will be vulnerable. Therefore, when using ``http`` for Galera Manager, you should use only trusted networks.

Shortly after you enter the URL for Galera Manager into your web browser, you'll see a simple login screen like the one below.  Here you'll enter the *GMD Admin User* name and password you provided during the installation.

.. figure:: ../images/galera-manager-login.png
   :width: 300px
   :alt: Galera Manager Login
   :class: document-screenshot

   Galera Manager Login (Figure 2)

At the start, after you log into Galera Manager for the first time, you'll see only a fairly empty screen that shows something like the screenshot below.  This is because you haven't yet created a cluster or added any nodes.

.. figure:: ../images/galera-manager-empty-cluster.png
   :width: 300px
   :alt: New Cluster in Galera Manager
   :class: document-screenshot

   New Galera Manager Installation (Figure 3)

To create a cluster,  you would click on the plus-sign icon, or the text below the box where it says, *Create New Cluster*. The process for adding a cluster and nodes is covered on the :doc:`galera-manager-adding-clusters` documentation page.  For information on upgrading Galera Manager, see the :doc:`gmd-upgrading` page.


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


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
