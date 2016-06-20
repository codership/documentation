=======
Support
=======
.. _`support`:



.. rubric:: Troubleshooting
.. _`troubleshooting`:

In the event that you are experiencing technical difficulties with your Galera Cluster deployment, these chapters provide frequently asked questions and guides to diagnosing and addressing various performance and replication issues.

- :doc:`faq`

  This chapter provides an FAQ for Galera Cluster with questions ranging from the meaning behind the name to common issues like failover and how to handle crashes during rsync. 


- :doc:`error`

  Given that Galera Cluster enables a number of new features not present in the standard MySQL implementations, it may on occasion log server errors that are unfamiliar to you.  This chapter covers common error messages, their meaning and what to do about them.

- :doc:`unknowncommand`
  
  When the node encounters issues in loading the wsrep Provider, statements run in the console generate an unknown command error.  This chapter covers identifying the source of the problem and how to solve it.

- :doc:`userchanges`

  Galera Cluster does not support direct modification of the system tables, given that they use the MyISAM engine and are thus non-transactional.  For instance, if you add or modify rows in ``mysql.user``, these changes do not replicate to the cluster.  This chapter covers the correct methods to use in adding users to the cluster.


- :doc:`clusterstallonalter`

  Sometimes when running ``ALTER`` statements that take a long time to run you may encounter issues where other nodes in the cluster stall out.  This chapter provides information on how to identify this issue and what to do about it.
  
- :doc:`detectingaslownode`

  By design, cluster performance is limited by that of its slowest node.  This chapter shows you how to find the slowest node to help in determining the reason and how to improve performance.

- :doc:`dealingwithmultimasterconflicts`

  Multi-master conflicts occur in consequence of application servers writing to different nodes.  This can lead to two nodes attempting to update the same row with different data. This chapter provides information on diagnosing and correcting these conflicts. 

- :doc:`twonode`

  Optimally, Galera Cluster requires a minimum of three nodes.  In the event that you have a cluster that uses only two nodes, you may sometimes encounter issues in which single-node failures cause the cluster to stop working altogether.  This chapter provides some pointers in how to manage these cases.

   

.. rubric:: Tutorials
.. _`tutorials`:

Where the above chapters relate to handling problems on the cluster, these provide additional information and guides on improving performance and optimizing your configuration.

- :doc:`performance`

  This chapter provides a series of guides to improving performance, such as optimizing write-set caching for state transfers, configuring parallel slave threads and handling large transactions.


- :doc:`configurationtips`

  This chapter provides a series of guides to optimizing your configuration, including WAN replication, single- and multi-master deployments and working with SELinux.





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

