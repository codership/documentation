.. meta::
   :title: Load Balancing Galera Cluster Nodes
   :description:
   :language: en-US
   :keywords: galera cluster, load balancing, mysql, mariadb
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

      Related Documents

      - :doc:`Deployment Variants <deployment-variants>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`load-balancing`:

================
Load Balancing
================

Galera Cluster guarantees node consistency regardless of where and when the query is issued. In other words, you are free to choose a load-balancing approach that best suits your purposes. If you decide to place the load balancing mechanism between the database and the application, you can consider, for example, the following tools:

- **HAProxy** an open source TCP/HTTP load balancer.

- **Pen** another open source TCP/HTTP load balancer. Pen performs better than HAProxy on SQL traffic.

- **Galera Load Balancer** inspired by Pen, but is limited to balancing generic TCP connections only.

For more information or ideas on where to use load balancers in your infrastructure, see :doc:`deployment-variants`.

.. container:: bottom-links

   Related Documents

   - :doc:`Deployment Variants <deployment-variants>`


.. toctree::
   :maxdepth: 2

   ha-proxy
   pen
   glb
