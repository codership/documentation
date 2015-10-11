=============
 Performance
=============
.. _`Performance`:

.. index::
   pair: Performance; Memory
.. index::
   pair: Performance; Swap size

-----------------------------------------
Write-set Caching during State Transfers
-----------------------------------------
.. _`gcache-during-state-transfers`:
.. index::
   pair: Performance; gcache

Under normal operations, nodes do not consume much more memory than the regular standalone MySQL database server.  The certification index and uncommitted write-sets do cause some additional usage, but in typical applications this is not usually noticeable.

Write-set caching during state transfers is the exception.

When a node receives a state transfer, it cannot process or apply incoming write-sets as it does not yet have a state to apply them to.  Depending on the state transfer method, (``mysqldump``, for instance), the sending node may also be unable to apply write-sets.

The Write-set Cache, (or GCache), caches write-sets on memory-mapped files to disk and Galera Cluster allocates these files as needed.  In other words, the only limit for the cache is the available disk space.  Writing to disk in turn reduces memory consumption.

.. note:: **See Also**: For more information on configuring write-set caching to improve performance, see :ref:`Configuring Flow Control <configuring-fc>`.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Customizing the Write-set Cache Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _`customizing-gcache-size`:
.. index::
   pair: Performance; gcache.size
.. index::
   pair: Performance; wsrep_received_bytes

You can define the size of the write-set cache using the :ref:`gcache.size <gcache.size>` parameter.  The set the size to one less than that of the data directory.


If you have storage issues, there are some guidelines to consider in adjusting this issue.  For example, your preferred state snapshot method.  ``rsync`` and ``xtrabackup`` copy the InnoDB log files, while ``mysqldump`` does not.  So, if you use ``mysqldump`` for state snapshot transfers, you can subtract the size of the log files from your calculation of the data directory size.

.. note:: Incremental State Transfers (IST) copies the database five times faster over ``mysqldump`` and about 50% faster than ``xtrabackup``.  Meaning that your cluster can handle relatively large write-set caches.  However, bear in mind that you cannot provision a server with Incremental State Transfers.

As a general rule, start with the data directory size, including any possible links, then subtract the size of the ring buffer storage file, which is called ``galera.cache`` by default.

In the event that storage remains an issue, you can further refine these calculations with the database write rate.  The write rate indicates the tail length that the cluster stores in the write-set cache.

You can calculate this using the :ref:`wsrep_received_bytes <wsrep_received_bytes>` status variable.

#. Determine the size of the write-sets the node has received from the cluster:

   .. code-block:: mysql

      SHOW STATUS LIKE 'wsrep_received_bytes';

      +------------------------+-----------+
      | Variable name          | Value     |
      +------------------------+-----------+
      | wsrep_received_bytes   | 6637093   |
      +------------------------+-----------+

   Note the value and time, respective as :math:`recv_1` and :math:`time_1`.

#. Run the same query again, noting the value and time, respectively, as :math:`recv_2` and :math:`time_2`.

#. Apply these values to the following equation:

   .. math::

      writerate = \frac{ recv_2 - recv_1 }{ time_2 - time_1}

From the write rate you can determine the amount of time the cache remains valid.  When the cluster shows a node as absent for a period of time less than this interval, the node can rejoin the cluster through an incremental state transfer. Node that remains absent for longer than this interval will likely require a full state snapshot transfer to rejoin the cluster.

You can determine the period of time the cache remains valid using this equation:

.. math::

   period = \frac{ cachesize } { writerate }


Conversely, if you already know the period in which you want the write-set cache to remain valid, you can use instead this equation:

.. math::

   cachesize = writerate \times time

   
This equation can show how the size of the write-set cache can improve performance.  For instance, say you find that cluster nodes frequently request state snapshot transfers.  Increasing the :ref:`gcache.size <gcache.size>` parameter extends the period in which the write-set remains valid, allowing the nodes to update instead through incremental state transfers.

   
      
.. note:: Consider these configuration tips as guidelines only. For example, in cases where you must avoid state snapshot transfers as much as possible, you may end up using a much larger write-set cache than suggested above.

-----------------------------------
Setting Parallel Slave Threads
-----------------------------------
.. _`parallel-slave-threads`:
.. index::
   pair: Performance; innodb_autoinc_lock_mode
.. index::
   pair: Performance; innodb_locks_unsafe_for_binlog
.. index::
   pair: Performance; wsrep_slave_threads

There is no rule about how many slave threads you need for replication.  Parallel threads do not guarantee better performance.  But, parallel applying does not impair regular operation performance and may speed up the synchronization of new nodes with the cluster.

You should start with four slave threads per CPU core:

.. code-block:: ini

   wsrep_slave_threads=4

The logic here is that, in a balanced system, four slave threads can typically saturate a CPU core.  However, I/O performance can increase this figure several times over.  For example, a single-core ThinkPad R51 with a 4200 RPM drive can use thirty-two slave threads.

Parallel applying requires the following settings:

.. code-block:: ini

   innodb_autoinc_lockmode=2
   innodb_locks_unsafe_For_binlog=1

You can use the :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>` status variable to determine the maximum number of slave threads possible.  For example:

.. code-block:: mysql

   SHOW STATUS LIKE 'wsrep_cert_deps_distance';

   +----------------------------+-----------+
   | Variable name              | Value     |
   +----------------------------+-----------+
   | wsrep_cert_deps_distance   | 23.88889  |
   +----------------------------+-----------+

This value essentially determines the number of write-sets that the node can apply in parallel on average.  

.. note:: **Warning**: Do not use a value for :ref:`wsrep_slave_threads <wsrep_slave_threads>` that is higher than the average given by the :ref:`wsrep_cert_deps_distance <wsrep_cert_deps_distance>` status variable.


------------------------------------
 Dealing with Large Transactions
------------------------------------
.. _`large-transactions`:

Large transactions, for instance the transaction caused by a ``DELETE`` query that removes millions of rows from a table at once, can lead to diminished performance.  If you find that you must perform frequently transactions of this scale, consider using ``pt-archiver`` from the Percona Toolkit.

For example, if you want to delete expired tokens from their table on a database called ``keystone`` at ``dbhost``, you might run something like this:

.. code-block:: console

   $ pt-archiver --source h=dbhost,D=keystone,t=token \
      --purge --where "expires < NOW()" --primary-key-only \
      --sleep-coef 1.0 --txn-size 500

This allows you to delete rows efficiently from the cluster.

.. note:: **See Also**: For more information on ``pt-archiver``, its syntax and what else it can do, see the `manpage <http://www.percona.com/doc/percona-toolkit/2.1/pt-archiver.html>`_.

