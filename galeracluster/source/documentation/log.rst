.. cssclass:: library-document

=====================
Database Server Logs
=====================
.. _`log`:

Galera Cluster provides the same database server logging features available to MySQL, MariaDB and Percona XtraDB, depending on which you use.  By default, it writes errors to a ``<hostname>.err`` file in the data directory.  You can change this in the ``my.cnf`` configuration file using the `log_error <https://dev.mysql.com/doc/refman/5.6/en/server-options.html#option_mysqld_log-error>`_ option, or by using the ``--log-error`` parameter.


.. _`server-log-parameters`:

------------------------
Log Parameters
------------------------

Galera Cluster provides parameters and wsrep options that allow you to enable error logging on events that are specific to the replication process.  If you have a script monitoring the logs, these entires can give you information on conflicts occurring in the replication process.

- :ref:`wsrep_log_conflicts <wsrep_log_conflicts>`: This parameter enables conflict logging for error logs. An example would be when two nodes attempt to write to the same row of the same table at the same time.

- :ref:`cert.log_conflicts <cert.log_conflicts>`: This wsrep Provider option enables logging of information on certification failures during replication.

- :ref:`wsrep_debug <wsrep_debug>`: This parameter enables debugging information for the database server logs.


  .. warning:: In addition to useful debugging information, this parameter also causes the database server to print authentication information, (i.e., passwords) to the error logs.  Don't enable it in production environments as it's a security vulnerability.

You can enable these through the ``my.cnf`` configuration file.  The excerpt below is an example of these options and how they are enabled:

.. code-block:: ini

   # wsrep Log Options
   wsrep_log_conflicts=ON
   wsrep_provider_options="cert.log_conflicts=ON"
   wsrep_debug=ON


.. _`gra.log`:

--------------------------
Additional Log Files
--------------------------

Whenever a node fails to apply an event on a slave node, the database server creates a special binary log file of the event in the data directory.  The naming convention the node uses for the filename is ``GRA_*.log``.


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
