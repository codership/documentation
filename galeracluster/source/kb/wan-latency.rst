.. meta::
   :title: Handling WAN Latency in Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2025. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :ref:`evs.join_retrans_period <evs.join_retrans_period>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-best-wan-latency`:

===============
WAN Latency
===============

.. rst-class:: article-stats

   Length: 221 words; Published: June 24, 2015; Updated: October 22, 2019; Category: Performance; Type: Best Practices

When using Galera Cluster over a :abbr:`WAN (Wide Area Network)`, remember that WAN links can have exceptionally high latency. You can check this by taking Round-Trip Time (RTT) measurements between cluster nodes. If there is a latency, you can correct for this by adjusting all of the temporal parameters.

.. rst-class:: section-heading
.. rubric:: Recommendations

To take RTT measurements, use ``ping`` on each cluster node to ping the others. For example, if you were to log into the node at ``192.168.1.1``, you might execute something like the following from the command-line:

.. code-block:: console

   $ ping -c 3 192.168.1.2

     PING 192.168.1.2 (192.168.1.2) 58(84) bytes of data.
     64 bytes from 192.168.1.2: icmp_seq=1 ttl=64 time=0.736 ms
     64 bytes from 192.168.1.2: icmp_seq=2 ttl=64 time=0.878 ms
     64 bytes from 192.168.1.2: icmp_seq=3 ttl=64 time=12.7 ms

     --- 192.168.1.2 ---

     3 packets transmitted, 3 received, 0% packet loss, time 2002ms
     rtt min/avg/max/mdev = 0.736/4.788/12.752/5.631 ms

Repeat this on each node in the cluster and note the highest value among them.

Parameters that relate to periods and timeouts, such as :ref:`evs.join_retrans_period <evs.join_retrans_period>`, must all use values that exceed the highest RTT measurement in the cluster.

.. code-block:: ini

   wsrep_provider_options="evs.join_retrans_period=PT0.5S"

This allows the cluster to compensate for the latency issues of the :abbr:`WAN (Wide Area Network)` links between the cluster nodes.


.. container:: bottom-links

   Related Documents

   - :ref:`evs.join_retrans_period <evs.join_retrans_period>`
