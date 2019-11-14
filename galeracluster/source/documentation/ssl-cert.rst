.. meta::
   :title: SSL Certificates to use with Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, ssl certificate, security, ports
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


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

      Related Documents

      - :doc:`ssl-config`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`ssl-cert`:

===================
SSL Certificates
===================


Before you can enable encryption for your cluster, you first need to generate the relevant certificates for the nodes to use.  This procedure assumes that you are using OpenSSL.

.. note:: This chapter only covers certificate generation.  For information on its use in Galera Cluster, see :doc:`ssl-config`.


.. _`gen-certs`:
.. rst-class:: section-heading
.. rubric:: Generating Certificates

There are three certificates that you need to create in order to secure Galera Cluster: the Certificate Authority (CA) key and cert; the server certificate, to secure ``mysqld`` activity and replication traffic; and the client certificate to secure the database client and ``stunnel`` for state snapshot transfers.

.. note:: When certificates expire there is no way to update the cluster without a complete shutdown.  You can minimize the frequency of this downtime by using large values for the ``-days`` parameter when generating your certificates.


.. _`gen-ca`:
.. rst-class:: sub-heading
.. rubric:: CA Certificate

The node uses the Certificate Authority to verify the signature on the certificates.  As such, you need this key and cert file to generate the server and client certificates.

To create the CA key and cert, complete the following steps:

#. Generate the CA key.

   .. code-block:: console

      openssl genrsa 2048 > ca-key.pem

#. Using the CA key, generate the CA certificate.

   .. code-block:: console

      openssl req -new -x509 -nodes -days 365000 \
            -key ca-key.pem -out ca-cert.pem

This creates a key and certificate file for the Certificate Authority.  They are in the current working directory as ``ca-key.pem`` and ``ca-cert.pem``.  You need both to generate the server and client certificates.  Additionally, each node requires ``ca-cert.pem`` to verify certificate signatures.


.. _`gen-server-cert`:
.. rst-class:: sub-heading
.. rubric:: Server Certificate

The node uses the server certificate to secure both the database server activity and replication traffic from Galera Cluster.

#. Create the server key.

   .. code-block:: console

      openssl req -newkey rsa:2048 -days 365000 \
            -nodes -keyout server-key.pem -out server-req.pem

#. Process the server RSA key.

   .. code-block:: console

      openssl rsa -in server-key.pem -out server-key.pem

#. Sign the server certificate.

   .. code-block:: console

      openssl x509 -req -in server-req.pem -days 365000 \
            -CA ca-cert.pem -CAkey ca-key.pem -set_serial 01 \
            -out server-cert.pem

This creates a key and certificate file for the server.  They are in the current working directory as ``server-key.pem`` and ``server-cert.pem``.  Each node requires both to secure database server activity and replication traffic.


.. _`gen-client-cert`:
.. rst-class:: sub-heading
.. rubric:: Client Certificate

The node uses the client certificate to secure client-side activity.  In the event that you prefer physical transfer methods for state snapshot transfers, ``rsync`` for instance, the node also uses this key and certificate to secure ``stunnel``.

#. Create the client key.

   .. code-block:: console

      openssl req -newkey rsa:2048 -days 365000 \
            -nodes -keyout client-key.pem -out client-req.pem

#. Process client RSA key.

   .. code-block:: console

      openssl rsa -in client-key.pem -out client-key.pem

#. Sign the client certificate.

   .. code-block:: console

      openssl x509 -req -in client-req.pem -days 365000 \
            -CA ca-cert.pem -CAkey ca-key.pem -set_serial 01 \
            -out client-cert.pem

This creates a key and certificate file for the database client.  They are in the current working directory as ``client-key.pem`` and ``client-cert.pem``.  Each node requires both to secure client activity and state snapshot transfers.


.. _`verify-cert`:
.. rst-class:: section-heading
.. rubric:: Verifying the Certificates

When you finish creating the key and certificate files, use ``openssl`` to verify that they were generated correctly:

.. code-block:: console

   openssl verify -CAfile ca-cert.pem \
         server-cert.pem client-cert.pem

   server-cert.pem: OK
   client-cert.pem: OK

In the event that this verification fails, repeat the above process to generate replacement certificates.

Once the certificates pass verification, you can send them out to each node.  Use a secure method, such as ``scp`` or ``sftp``.  The node requires the following files:

- Certificate Authority: ``ca-cert.pem``.
- Server Certificate: ``server-key.pem`` and ``server-cert.pem``.
- Client Certificate: ``client-key.pem`` and ``client-cert.pem``.

Place these files in the ``/etc/mysql/certs`` directory of each node, or a similar location where you can find them later in configuring the cluster to use :abbr:`SSL (Secure Socket Layer)`.

.. container:: bottom-links

   Related Documents

   - :doc:`ssl-config`
