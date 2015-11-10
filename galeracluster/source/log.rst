=====================
Database Server Logs
=====================
.. _`server-log`:

Galera Cluster provides the same database server logging features available to MySQL, MariaDB and Percona XtraDB, depending on which you use.  By default, it writes errors to a ``<hostname>.err`` in the data directory.  You can change this in the ``my.cnf`` configuration file using the `log_error <https://dev.mysql.com/doc/refman/5.6/en/server-options.html#option_mysqld_log-error>`_ parameter, or by using the ``--log-error`` parameter.


------------------------
Log Parameters
------------------------
.. _`server-log-parameters`:

Galera Cluster provides parameters and wsrep Options that allow you to enable error logging on events that are specific to the replication process.  If you have a script monitoring the logs, these entires can provide you with information on conflicts occurring in the replication process.

- :ref:`wsrep_log_conflicts <wsrep_log_conflicts>` This parameter enables conflict logging for your error logs, such as when two nodes attempt to write to the same row of the same table at the same time.

- :ref:`cert.log_conflicts <cert.log_conflicts>` This wsrep Provider option enables logging of information on certification failures during replication.

- :ref:`wsrep_debug <wsrep_debug>` This parameter enables debugging information for the database server logs.

  
  .. note:: **Warning**: In addition to useful debugging information, this parameter also causes the database server to print authentication information, (that is, passwords), to the error logs.  Do not enable it in production environments.

You can enable these through the ``my.cnf`` configuration file.

.. code-block:: ini

   # wsrep Log Options
   wsrep_log_conflicts=ON
   wsrep_provider_options="cert.log_conflicts=ON"
   wsrep_debug=ON



--------------------------
Additional Log Files
--------------------------
.. _`gra.log`:

Whenever the node fails to apply an event on a slave node, the database server creates a special binary log file of the event in the data directory.  The naming convention the node uses for the filename is ``GRA_*.log``. 




