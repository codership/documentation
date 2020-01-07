.. meta::
   :title: SSL Settings related to Galera Cluster
   :description:
   :language: en-US
   :keywords: galera cluster, ssl, security
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

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


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
