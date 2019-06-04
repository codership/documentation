================
 Load Balancing
================
.. _`load-balancing`:
.. index::
   single: Load balancing

Galera Cluster guarantees node consistency regardless of where and when the query is issued. In other words, you are free to choose a load-balancing approach that best suits your purposes. If you decide to place the load balancing mechanism between the database and the application, you can consider, for example, the following tools:

- **HAProxy** an open source TCP/HTTP load balancer.

- **Pen** another open source TCP/HTTP load balancer. Pen performs better than HAProxy on SQL traffic.

- **Galera Load Balancer** inspired by Pen, but is limited to balancing generic TCP connections only.

.. note:: For more information or ideas on where to use load balancers in your infrastructure, see :doc:`deployment-variants`.

.. toctree::
   :maxdepth: 2

   ha-proxy
   pen
   glb
