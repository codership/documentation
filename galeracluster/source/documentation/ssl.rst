.. meta::
   :title: SSL Settings related to Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, ssl, security
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <./index>`
      - :doc:`Knowledge Base <../kb/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../kb/trouble/index>`
         - :doc:`Best Practices <../kb/best/index>`

      - :doc:`FAQ <../faq>`
      - :doc:`Training <../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: library-document
.. _`ssl-settings`:

==================
SSL Settings
==================

.. index::
   pair: Parameters; socket.ssl_compression
.. index::
   pair: Parameters; socket.ssl_cipher
.. index::
   pair: Parameters; socket.ssl_cert
.. index::
   pair: Parameters; socket.ssl_key

Galera Cluster supports secure encrypted connections between nodes using :abbr:`SSL (Secure Socket Layer)` protocol.  This includes connections between database clients and servers through the standard :abbr:`SSL (Secure Socket Layer)` support in MySQL. It also includes encrypting replication traffic particular to Galera Cluster itself.

The :abbr:`SSL (Secure Sockets Layer)` implementation is cluster-wide and doesn't support authentication for replication traffic.  You must enable :abbr:`SSL (Secure Sockets Layer)` for all nodes in the cluster or none of them.

.. toctree::

   ssl-cert
   ssl-config
   ssl-sst
