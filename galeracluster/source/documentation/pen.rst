.. meta::
   :title: Pen Load Balancer with Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, load balancer, pen
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


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

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`pen`:

==================
Pen Load Balancer
==================

Pen is a high-scalability, high-availability, robust load balancer for TCP- and UDP-based protocols. You can use it to balance connections between application servers and Galera Cluster.


.. _`pen-install`:
.. rst-class:: section-heading
.. rubric:: Installation

Pen is available in the software repositories of most Linux distributions. You can install it using a package manager.

- For DEB-based Linux distributions (that is, Debian and Ubuntu), run the following from the command-line:

  .. code-block:: console

     # apt-get install pen

- For RPM-based Linux distributions (that is, Red Hat Enterprise Linux and CentOS), use the ``yum`` utility instead by executing the following from the command-line:

  .. code-block:: console

     # yum install pen

Whichever you use, they will install Pen on your system. In the event that the command for your distribution or operating system does not work as expected, check your system's documentation or software repository for information on the correct procedure to install Pen. For instance, on a RPM-based system, you may have to install the ``yum`` utility.


.. _`using-pen`:
.. rst-class:: section-heading
.. rubric:: Using Pen

Once you've installed Pen on the load balancing server, you can launch it from the command-line by entering something like the following:

.. code-block:: console

   # pen -l pen.log -p pen.pid localhost:3306 \
         191.168.1.1:3306 \
	 191.168.1.2:3306 \
	 191.168.1.3:3306

When one of the application servers attempts to connect to the Pen server on port ``3306``, Pen routes that connection to one of the Galera Cluster nodes.

For more information on Pen configuration and use, see its manpage.


.. _`pen-server-selection`:
.. rst-class:: sub-heading
.. rubric:: Server Selection

When Pen receives a new connection from the application servers, it first checks to see where the application was routed on the last connection and attempts to send traffic there. In the event that it cannot establish a connection, it falls back on a round-robin selection policy.

There are a number of options you can use to modify this behavior when you launch Pen.

- **Default Round Robin:** This directs all new connections to the next destination in a cirular order, without determining which server a client used the last time. You can enable this with the ``-r`` option.

- **Stubborn Selection:** In the event that the initial choice is unavailable, Pen closes the client connection. This is enabled with the ``-s`` option.

- **Hash Client IP Address:** Pen applies a hash on the client IP address for the initial server selection, making it more predictable where it routes client connections in the future.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
