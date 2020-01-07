.. meta::
   :title: Galera Cluster System Configuration
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2020. All Rights Reserved.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../courses/index>`
         - :doc:`Training Videos <../videos/index>`

      .. cssclass:: sub-links

         .. cssclass:: here

         - :doc:`Tutorial Articles <./index>`

      - :doc:`FAQ <../../faq>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`configuration`:

==========================
System Configuration
==========================

.. rst-class:: article-stats

   Length:  964 words; Writer: Staff; Published: October 20, 2014; Topic: General; Level: Beginner

After you finish installing Galera Cluster on your server, you're ready to configure the database itself to serve as a node in a cluster.  To do this, you'll need to edit the MySQL configuration file.

Using a text editor, edit the ``/etc/my.cnf`` file.  You'll need to include entries like the ones shown in this sample excerpt:

.. code-block:: console

   [mysqld]
   datadir=/var/lib/mysql
   socket=/var/lib/mysql/mysql.sock
   user=mysql
   binlog_format=ROW
   bind-address=0.0.0.0
   default_storage_engine=innodb
   innodb_autoinc_lock_mode=2
   innodb_flush_log_at_trx_commit=0
   innodb_buffer_pool_size=122M
   wsrep_provider=/usr/lib/libgalera_smm.so
   wsrep_provider_options="gcache.size=300M; gcache.page_size=300M"
   wsrep_cluster_name="example_cluster"
   wsrep_cluster_address="gcomm://IP.node1,IP.node2,IP.node3"
   wsrep_sst_method=rsync

   [mysql_safe]
   log-error=/var/log/mysqld.log
   pid-file=/var/run/mysqld/mysqld.pid


Depending on your system and the location of your installation of MySQL or MariaDB, you will need to adjust the valuables for variables (e.g., the path to the data directory).


.. _`db-config`:
.. rst-class:: section-heading
.. rubric:: Configuring the Database Server

In addition to settings for the system, there are other basic configurations that you will need to set in the ``/etc/my.cnf`` file.  Make these changes before starting the database server.

First, make sure that ``mysqld`` is not bound to 127.0.0.1.  This is the IP address for localhost.  If the ``bind-address`` variable is in the file, comment it out by adding a hash sign (i.e., ``#``) at the start of the line:

.. code-block:: console

   # bind-address = 127.0.0.1

Next, ensure the configuration file includes the ``conf.d/`` by adding a line with ``!includedir`` at the start, followed by the file path:

.. code-block:: console

   !includedir /etc/mysql/conf.d/

Now, set the binary log format to use row-level replication, as opposed to statement-level replication. You'd do this by adding the following line:

.. code-block:: console

   binlog_format=ROW

Don't change this value later as it affects performance and consistency.  The binary log can only use row-level replication for Galera Cluster.

Galera Cluster will not work with MyISAM or other non-transactional storage engines. So, make sure the default storage engine is InnoDB using the ``default_storage_engine`` variable like so:

.. code-block:: console

   default_storage_engine=InnoDB

Next, ensure the InnoDB locking mode for generating auto-increment values is set to interleaved lock mode. This is designated by a value of ``2`` for the appropriate variable:

.. code-block:: console

   innodb_autoinc_lock_mode=2

Don't change this value afterwards.  Other modes may cause ``INSERT`` statements to fail on tables with ``AUTO_INCREMENT`` columns.

.. warning:: When `innodb_autoinc_lock_mode <https://dev.mysql.com/doc/refman/5.5/en/innodb-parameters.html#sysvar_innodb_autoinc_lock_mode>`_ is set to traditional lock mode (i.e., a value of ``0``) or to consecutive lock mode (i.e., a value of ``1``) it can cause unresolved deadlocks and make the system unresponsive in Galera Cluster.


After all of that, make sure the InnoDB log buffer is written to file once per second, rather than on each commit, to improve performance. To do this, set the ``innodb_flush_log_at_trx_commit`` variable to 0 like so;

.. code-block:: console

   innodb_flush_log_at_trx_commit=0

.. warning:: Although setting `innodb_flush_log_at_trx_commit <https://dev.mysql.com/doc/refman/5.1/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit>`_ to a value of ``0`` or ``2`` improves performance, it also introduces potential problems.  Operating system crashes or power outages can erase the last second of transaction.  Although normally you can recover this data from another node, it can still be lost entirely in the event that the cluster goes down at the same time.

After you make all of these changes and additions to the configuration file, you're ready to configure the database privileges.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configuring the InnoDB Buffer Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`config_innodb_buffer_pool_size`:

The InnoDB storage engine uses its own memory buffer to cache data and for indexes of tables. You can configure this memory buffer through the
`innodb_buffer_pool_size <https://dev.mysql.com/doc/refman/5.1/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size>`_ parameter.  The default value is 128 MB.  To compensate for the increased memory usage of Galera Cluster over a standalone MySQL database server, you should scale your usual value back by five percent.

.. code-block:: console

   innodb_buffer_pool_size=122M


.. _`swap-config`:
.. rst-class:: section-heading
.. rubric:: Configuring Swap Space

Memory requirements for Galera Cluster are difficult to predict with any precision.  The particular amount of memory it uses can vary significantly, depending upon the load the given node receives.  In the event that Galera Cluster attempts to use more memory than the node has available, the ``mysqld`` instance will crash.


The way to protect a node from such crashes is to ensure that there is sufficient swap space available on the server. This can be either in the form of a swap partition or swap files.  To check the available swap space, execute the following from the command-line:

.. code-block:: console

   # swapon --summary

   Filename        Type        Size     Used    Priority
   /dev/sda2       partition   3369980  0       -1
   /swap/swap1     file        524284   0       -2
   /swap/swap2     file        524284   0       -3

If swap is not configured, nothing will be returned from this command. If your system doesn't have swap space available or if the allotted space is insufficient, you can fix this by creating swap files.

First, create an empty file on your disk, set the file size to whatever size you require.  You can do this with the ``fallocate`` tool like so:

.. code-block:: console

   fallocate -l 512M /swapfile

Alternatively, you can manage the same using ``dd`` utility like this:

.. code-block:: console

   dd if=/dev/zero of=/swapfile bs=1M count=512

Be sure to secure the swap file by changing the permissions on the filesystem with ``chmod`` like this:

.. code-block:: console

   chmod 600 /swapfile

   $ ls -a / | grep swapfile

   -rw------- 1 root root 536870912 Feb 12 23:55 swapfile

This sets the file permissions so that only the root user can read and write to the file.  No other user or group member can access it.  Using the ``ls`` command command above shows the results.

Now you're read to format the swap file.  You can do this with the ``mkswap`` utility.  You'll then need to active the swap file.

.. code-block:: console

   mkswap /swapfile
   swapon /swapfile

Using a text editor, update the ``/etc/fstab`` file to include the swap file by adding the following line to the bottom:

.. code-block:: console

   /swapfile none swap defaults 0 0

After you save the ``/etc/fstab`` file, you run ``swapon`` again to see the results:

.. code-block:: console

   swapon --summary

   Filename        Type        Size     Used    Priority
   /swapfile       file        524284   0       -1



.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
