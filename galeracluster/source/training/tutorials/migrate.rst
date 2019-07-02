.. cssclass:: tutorial-article
.. _`migrate`:

============
Migration
============

.. rst-class:: list-stats

   Length: 173 words; Published: October 20, 2014; Topic: Migration; Level: Beginner


In the :doc:`Getting Started Guide <getting-started>`, the installation guides were written on the assumption that Galera Cluster is the first database in your infrastructure. However, this won't always be the case.  Sometimes, you may need to migrate to Galera Cluster from an existing database infrastructure: such as a single MySQL server or several database servers that were part of a MySQL master-slave cluster.


- :doc:`differences`

  .. rst-class:: list-stats

     Length:  808 words; Writer: Staff; Published: October 20, 2014; Topic: Migration; Level: Beginner

  While clusters operate as distributed database servers, there are some key differences between them and the standard stand-alone MySQL implementations.


- :doc:`migration`

  .. rst-class:: list-stats

     Length:  1106 words; Writer: Staff; Published: October 20, 2014; Topic: Migration; Level: Beginner

  When migrating from the standard MySQL implementations to Galera Cluster, there are some additional steps that you need to take to ensure that you safely transfer the data from the existing database to the new cluster.  This section covers the procedure to update system tables and how to migrate from stand-alone MySQL, as well as from MySQL master-slave replication clusters.


For more information on the installation and basic management of Galera Cluster, see the :doc:`Getting Started Guide <getting-started>`.


.. toctree::
   :maxdepth: 2
   :hidden:

   differences
   migration
