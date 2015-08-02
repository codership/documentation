=========================
Using Jails on FreeBSD
=========================
.. _`galera-jails`:

In FreeBSD, jails provides a platform for securely deploying applications within virtual instances.  You may find it useful in portable deployments across numerous machines for testing and security.

Galera Cluster can run from within a jail instance.


------------------------
Initializing ``ezjail``
------------------------
.. _`init-ezjail`:

While FreeBSD does provide a manual interface for creating and managing jails on your servers, ``jail(8)``, it can prove cumbersome in managing multiple instances per server.  The application ``ezjail`` manages this process, automating common tasks and using templates and symbolic links to reduce the need for disk space.  It is available in ports at ``sysutils/ezjail``.

When you have ``ezjail`` installed on your system, you need to initialize the environment.  To do so, run the following command:

.. code-block:: console

   # ezjail-admin install -sp

This creates the base file system for jails to use.  You can view it on the host system at ``/usr/jails``.  This creates a ``basejail``, which is the base operating system all jails use, as well as flavors, which contain additional configuration settings that you may want to use in particular instances.

Since jails managed through ``ezjail`` rely on a base system to which they are tied through symbolic links, you can update all jails together using the following command:

.. code-block:: console

   # ezjail-admin update


-------------------------
Creating a Jail
-------------------------
.. _`jail-create`:

ezjail-admin create

ezjail-admin start

ezjail-admin console



----------------------
Configuring Firewall
----------------------
.. _`jails-config-firewall`:

Stuff




