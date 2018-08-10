==================
SSL Settings
==================
.. _`ssl-settings`:
.. index::
   pair: Parameters; socket.ssl_compression
.. index::
   pair: Parameters; socket.ssl_cipher
.. index::
   pair: Parameters; socket.ssl_cert
.. index::
   pair: Parameters; socket.ssl_key

Galera Cluster supports secure encrypted connections between nodes using :abbr:`SSL (Secure Socket Layer)` protocol.  This includes both the connections between database clients and servers through the standard :abbr:`SSL (Secure Socket Layer)` support in MySQL as well as encrypting replication traffic particular to Galera Cluster itself.

The :abbr:`SSL (Secure Sockets Layer)` implementation is cluster-wide and does not support authentication for replication traffic.  You must enable :abbr:`SSL (Secure Sockets Layer)` for all nodes in the cluster or none of them.

.. toctree::

   sslcert
   sslconfig
   sslsst

