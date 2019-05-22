=======
Support
=======
.. _`support`:



.. rubric:: Troubleshooting
.. _`troubleshooting`:

When you experience difficulties with a Galera Cluster deployment, these sections may provide some assistance. They include frequently asked questions, as well as guides to diagnosing and addressing various performance and replication issues.

- :doc:`faq`

  This section provides an FAQ for Galera Cluster. The questions range from the meaning behind the name Galera, to common issues like failover and how to handle crashes during rsync. 


- :doc:`error`

  Given that Galera Cluster enables a number of new features not present in the standard MySQL implementation, it may on occasion log server errors that are unfamiliar to you.  This section lists common error messages and explains them, as well as what to do about them.

- :doc:`unknowncommand`
  
  When a node encounters issues in loading the wsrep Provider, statements run in a console will generate an unknown command error.  This section covers identifying the source of the problem and how to solve it.

- :doc:`userchanges`

  Galera Cluster doesn't support direct modification of MySQL system tables since they use the MyISAM engine and are thus non-transactional.  For instance, if you add or modify rows in ``mysql.user``, these changes will not replicate to the cluster.  This section explains the correct methods to use in making changes to systems tables in a cluster.


- :doc:`clusterstallonalter`

  Sometimes, when executing ``ALTER`` statements that take a long time, you may encounter issues in which other nodes in the cluster stall.  This section provides information on how to identify this problem and what to do about it.
  
- :doc:`detectingaslownode`

  By design, a cluster's performance is limited by its slowest node.  This section shows you how to identify which node is the slowest and to help determine the cause. It also explains how thereby to improve performance.

- :doc:`dealingwithmultimasterconflicts`

  Multi-master conflicts occur in as a result of application servers writing to different nodes.  This can lead to two nodes attempting to update the same row with different data. This section provides information on diagnosing and correcting these conflicts. 

- :doc:`twonode`

  Optimally, Galera Cluster requires a minimum of three nodes.  If you have a cluster that uses only two nodes, you may sometimes encounter issues in which single-node failures cause the cluster to stop working.  This section gives some pointers in how to manage these cases.

   

.. rubric:: Tutorials
.. _`tutorials`:

Whereas the above sections relate to handling problems with a cluster, these sections provide additional information and guides on improving performance and optimizing configuration.

- :doc:`performance`

  This section provides a series of guides to improving performance, such as optimizing write-set caching for state transfers, configuring parallel slave threads and handling large transactions.


- :doc:`configurationtips`

  This section provides a series of guides for optimizing your configuration, including WAN replication, single-master and multi-master deployments and working with SELinux.



.. toctree::
   :maxdepth: 2
   :hidden:
     
   faq
   error
   unknowncommand
   userchanges
   clusterstallonalter
   detectingaslownode
   dealingwithmultimasterconflicts
   twonode      
   performance
   configurationtips

