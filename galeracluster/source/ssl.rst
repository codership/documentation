==================
Enabling SSL
==================
.. _`enabling-ssl`:
.. index::
   pair: Parameters; socket.ssl_compression
.. index::
   pair: Parameters; socket.ssl_cipher
.. index::
   pair: Parameters; socket.ssl_cert
.. index::
   pair: Parameters; socket.ssl_key
   
   
For the encryption of replication traffic, Galera Cluster supports :abbr:`SSL (Secure Sockets Layer)`.  It does not support authentication.  SSL is a cluster-wide option.  You must enable it for all nodes in the cluster or none at all.

.. warning:: Galera Cluster SSL support only covers Galera Cluster communications.  State Snapshot Transfers happen outside of Galera Cluster, so you must protect them separately.  For example, consider using the internal SSL support of the MySQL client or the ``stunnel`` program to protect ``rsync`` traffic.

---------------------------------
Generating SSL Certificate
---------------------------------
.. _`generating-ssl-cert`:

Before you can enable encryption for your replication traffic, you first need to generate the relevant certificates for SSL to use.  These commands assumes that you are using OpenSSL.

To create an SSL certificate, for each node complete the following steps:

#. In the ``/etc/mysql`` directory, use ``openssl`` to generate a server key.

   .. code-block:: console

      # openssl genrsa -des3 -out key.pem 4096
      
      ...........................................
      ...........................................
      ...........................................
      Enter pass phrase for key.pem:
      Verifying - Enter pass phrase for key.pem:

   When prompted for a passphrase, enter a long one with punctuation marks, numbers and capital and lower case letters.  Length and complexity will make it more difficult to crack.

#. Create the certificate signing request:

   .. code-block:: console

      # openssl req -new -key key.pem -out cert.pem
      
      Enter pass phrase for key.pem:
      You are about to be asked to enter information that
      will be incorporated into your certificate request.
      What you are about to enter is what is called a
      Distinguished Name or a DN. There are quite a few
      fields but you can leave some blank For some fields
      there will be a default value,
      If you enter '.', the field will be left blank.
      -----
      Country Name (2 letter code) [AU]:
      State or Province Name (full name) [Some-State]:
      Locality Name (eg, city) []:
      Organization Name (eg, company) [Internet Widgits Pty Ltd]:
      Organizational Unit Name (eg, section) []:
      Common Name (e.g. server FQDN or YOUR name) []: 
      Email Address []:

      Please enter the following 'extra' attributes
      to be sent with your certificate request
      A challenge password []:
      An optional company name []:

   Answer each of the questions as prompted.  For the ``Common Name`` field, use the hostname for the node.

#. Sign the certificate.

   .. code-block:: console

      # openssl x509 req -new -days 365000 \
            -in cert.pem -signkey key.pem \
	    -out cacert.pem

   When prompted, enter the ``key.pem`` pass phrase.

   .. note:: When the certificate expires, there is no way to update the cluster without a complete shutdown.  Use a large value for the ``-days`` parameter.

You now have three files added to your node:  The SSL key ``key.pem``, the certificate signing request ``cert.pem``, and the signed certificate ``cacert.pem``.

---------------------------
Starting the Node with SSL
---------------------------
.. _`starting-with-ssl`:

Once you have the relevant certificate files ready, you can enable SSL for the node.  You need to add the paths to each file to the :ref:`wsrep_provider_options<wsrep_provider_options>` parameter.  To do so, use the following parameters:


- :ref:`socket.ssl_key<socket.ssl_key>` The SSL key file, ``key.pem``.

- :ref:`socket.ssl_cert<socket.ssl_cert>` The certification signing request, ``cert.pem``.
  
- :ref:`socket.ssl_ca<socket.ssl_ca>` The signed certificate, ``cacert.pem``.


.. code-block:: ini

   wsrep_provider_options="socket.ssl_ca=/path/to/key.pem,socket.ssl_cert=/path/to/cert.pem,socket.ssl_ca=/path/to/cacert.pem"

When the database server starts, it now uses encryption for replication traffic between the nodes.


.. seealso:: For information on other parameters for SSL, see :ref:`socket.ssl_compression <socket.ssl_compression>` and :ref:`socket.ssl_cipher <socket.ssl_cipher>`.


In the event that you already have a cluster running, you need to restart the entire cluster with the new configuration.  For servers that use ``init``, you can restart the node with the following command:

.. code-block:: console

   # service mysql restart

For servers using ``systemd``, instead run this command:

.. code-block:: console

   # systemctl restart mysql

   


