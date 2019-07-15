.. meta::
   :title: Using Galera Cluster with SELinux
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. topic:: The Library
   :name: left-margin

   .. cssclass:: no-bull

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../index>`

      .. cssclass:: no-bull-sub

         - :doc:`Troubleshooting <../trouble/index>`
         - :doc:`Best Practices <./index>`

      - :doc:`FAQ <../../faq>`
      - :doc:`Training <../../training/index>`

      .. cssclass:: no-bull-sub

         - :doc:`Tutorial Articles <../../training/tutorials/index>`
         - :doc:`Training Videos <../../training/videos/index>`

      .. cssclass:: bull-head

         Related Documents

      .. cssclass:: bull-head

         Related Articles


.. cssclass:: kb-article
.. _`kb-best-galera-with-selinux`:

===================================
Using Galera Cluster with SELinux
===================================

.. index::
   pair: Configuration; SELinux

When you first enable Galera Cluster on a node that runs SELinux, it will prohibit all cluster activities.  In order to enable replication on the node, you need a policy so that SELinux can recognize cluster activities as legitimate.

.. rst-class:: kb
.. rubric:: Recommendations

To create a policy for Galera Cluster, set SELinux to run in permissive mode.  Permissive mode does not block cluster activity, but it does log the actions as warnings.  By collecting these warnings, you can iteratively create a policy for Galera Cluster.  You can make this change generally by editing the SELinux configuration file (e.g., ``/etc/selinux/config``) to include an uncommented line like so:

.. code-block:: console

   SELINUX=permissive

Once SELinux no longer registers warnings from Galera Cluster, you can switch it back into enforcing mode.  SELinux then uses the new policy to allow the cluster access to the various ports and files it needs.

.. note:: Almost all Linux distributions ship with a MySQL policy for SELinux.  You can use this policy as a starting point for Galera Cluster and extend it, using the above procedure.
