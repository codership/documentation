=================================
Pen
=================================
.. _`pen`:

Pen is a high-scalability, high availability, robust load balancer for TCP- and UDP-based protocols.  You can use it to balance connections between your application servers and Galera Cluster.

---------------
Installation
---------------
.. _`pen-install`:

Pen is available in the software repositories of most Linux distributions.  You can install it using the package manager.

- For DEB-based Linux distributions, such as Debian and Ubuntu, run this command:

  .. code-block:: console

     # apt-get install pen

- For RPM-based Linux distributions, such as Red Hat, Fedora and CentOS, instead run this command:

  .. code-block:: console

     # yum install pen

This installs Pen on your system.  In the event that the command for your distribution or operating system does not work as expected, check your system's documentation or software repository for information on the correct procedure to install Pen.


----------------
Using Pen
----------------
.. _`using-pen`:

Once you have installed Pen on the load balancing server, you can launch it from the command-line.

.. code-block:: console

   # pen -l pen.log -p pen.pid localhost:3306 \
         191.168.1.1:3306 \
	 191.168.1.2:3306 \
	 191.168.1.3:3306

When one of the application servers attempts to connect to the Pen server on port ``3306``, Pen routes that connection out to one of the Galera Cluster nodes.

.. note:: For more information on Pen configuration and use, see the manpage.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Server Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`pen-server-selection`:

When Pen receives a new connection from the application servers, it first checks to see where the application was routed on the last connection and attempts to send traffic there.  In the event that it cannot establish a connection, it falls back on a round-robin selection policy.  

There are a number of options you can use to modify this behavior when you launch Pen.

- **Default Round Robin** Directs all new connections to the next destination in a cirular order list, without looking up which server a client used the last time.  Enable it with the ``-r`` option.
- **Stubborn Selection** In the event that the initial choice is unavailable, Pen closes the client connection.  Enable it with the ``-s`` option.
- **Hash Client IP Address** Pen applies a hash on the client IP address for the initial server selection, making it more predictable where it routes client connections in the future.





