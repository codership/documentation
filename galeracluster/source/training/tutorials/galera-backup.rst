
.. meta::
   :title: Making Back-Ups with Galera Cluster
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2019. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../../documentation/index>`
      - :doc:`Knowledge Base <../../kb/index>`
      - :doc:`Training <../index>`

        .. cssclass:: sub-links

           .. cssclass:: here

           - :doc:`Tutorial Articles <./index>`

        .. cssclass:: sub-links

           - :doc:`Training Videos <../videos/index>`

      - :doc:`FAQ <../../faq>`

      Related Documents

      - :doc:`Install MySQL Galera <../../documentation/install-mysql>`

      Related Articles

      - :doc:`Galera Back-Ups (video) <../videos/galera-backup>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`galera-backup`:

=====================================
Making Back-Ups with Galera Cluster
=====================================

.. rst-class:: article-stats

   Length: 2693 words; Writer: Russell J.T Dyer: November 4, 2019; Topic: Administration

Galera Cluster is a reliable, stable database replication clustering system. Nevertheless, there's always the possibility that something will go wrong |---| in fact, it's inevitable and unavoidable.  Therefore, as a database administrator, you should ensure that back-ups of the databases and related systems are made regularly and often.

Using Galera Cluster, there are a few ways in which you might make a back-up. In this article, we'll first look at the basics of back-ups. We'll then look at some other methods involving replication and how to automate back-ups by using the functionality of Galera itself.


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Back-Up Basics

Back-ups are important for many reasons:  User errors are inevitable |---| such as tables dropped and rows deleted inadvertently |---| and there’s always the chance that a server crashes or is physically damaged in some other way. As a result, to ensure regular and good back-ups, you should develop some back-up policies.

First, make sure your back-ups are complete. If you're using binary logs, be sure that you make a back-up of them.  Also, make back-up copies of the database configuration files.

Second, don’t rely on making back-ups manually. Instead, automate your back-ups by using a scheduling tool like ``cron``.  Set the frequency to something reasonable, such as daily or twice a day. Make sure back-up files are stored in a different location than on the production server.

There are two basic types of back-ups that can be made of a database: a physical back-up and logical back-up. We'll consider each in the next two sections. Whatever method you use, occasionally check your back-ups by performing recovery tests.  This has the advantage of helping you to become more proficient at restoring data, which will be useful when under pressure to do so quickly.

.. rst-class:: sub-heading
.. rubric:: Physical Back-Ups

A physical back-up is fast; It’s intuitive and simple:  You just copy the data directory using ``cp`` or ``rsync``. It seems perfect, but there are many inherent problems with this method.

To get a consistent back-up, you have to stop the ``mysqld`` daemon. That means no one can access the data while the back-up is being made. If any of the files are corrupted, you won’t know until you try to restore the back-up.

.. rst-class:: sub-heading
.. rubric:: Logical Backups

Logical back-ups are generally preferred. They're generated with a utility like ``mysqldump`` and produce text files with SQL statements which may be used to rebuild databases.

One drawbacks to logical back-ups is that the back-up process requires tables or rows to be locked. This means that tables may be temporarily inaccessible for write traffic. Even read traffic may experience slow results.

You’ll have to decide which method works best for you. Let’s see how you might make simple back-ups of a Galera node using both of these methods.

.. rst-class:: sub-heading
.. rubric:: Simple Galera Node Back-Ups

Many DBAs will simply run ``mysqldump`` on one of the nodes without removing it from the cluster. This is definitely not a good idea since they may not get consistent data and it will slow the node and thereby affect the performance of the cluster.

A beter method is to instruct Galera to desynchronize the node to use for making a back-up.  This is done by setting globally the ``wsrep_desync`` parameter to ``ON``, as you see here:

.. code-block:: text

   mysql -p -u root --execute "SET wsrep_desync = ON"

Thus will stop the node from processing new transactions, although it will remain part of the cluster.  It will ensure consistency of data across tables while we make a back-up, but continue to receive transactions from the other nodes for when we’re finished what we’re doing.

After that's done, we can run whatever tool or utility we prefer to make a back-up of the databases on the node.  Two popular and simple utilities are ``mysqldump`` and ``rsync``. Here's how we might make a back-up with ``mysqldump``:

.. code-block:: text

   mysqldump -p -u admin_backup \
             --flush-logs --all-databases \
             > /backups/db-backup-20191025.sql

When it's finished, we’ll set ``wsrep_desync`` back to ``OFF``. The node will then process any transactions that are queued and waiting to be executed on the node.

This simple method of making back-ups of a Galera node works well, but it still require us to take a node out of service. It supposes we're using a load balancer to redirect traffic away from the node to the other nodes. Let's look at some other methods.


.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Using Standard Replication

Even though Galera is running on a node, it’s possible for it also to be running standard replication and act as a master to another server that’s not part of the cluster, that’s not using Galera software.

With such an arrangement, the replication slave can be used to make back-ups without disturbing the Galera cluster.  When you want to make a back-up, just stop the slave from replicating. Then run whatever back-up utility you prefer. When you’re finished, just start the slave replicating again.

.. rst-class:: sub-heading
.. rubric:: Galera Master Configuration

For a Galera node to be able also to serve as a standard replication master, we will have to add some extra parameters to the configuration file.  Let's look at those settings.  Below is an excerpt from a database configuration file on the node that's to be the master:

.. code-block:: text

   [mysqld]
   ...
   server-id = 01

   log-bin = /var/lib/mysql/master-bin
   log-bin-index = /var/lib/mysql/master-bin.index

   log_slave_updates = ON


Standard replication requires each server to have a unique identification number. This is set with the ``server-id`` parameter. Actually, so that any of the other nodes can be used as a master, you might add these parameters to all of the nodes, with the same values.  It'll be fine as long as only one is part of the standard replication.

Next, we’ll add the ``log-bin`` parameter on all nodes, to enable the binary log. Even though Galera doesn't need this, it's essential to the standard replication process. This will be a performance drain, but not much.

So that Galera understands what's going on, we'll need to set the ``log_slave_updates`` parameter to ``ON``.

When we’re finished making these additions, we’ll have to restart all of the nodes and the cluster.  That means we’ll have to shut down all of the nodes first, before we start them again, so that there’s a new cluster.

We'll neeed to export the data from the master using a utility like ``mysqldump`` with the ``--flush-logs`` and ``--master-data`` options.  We'll also need to create a user account on the master that has the IP address of the slave |---| with the ``REPLICATION SLAVE`` privilege.

.. code-block:: text

   GRANT REPLICATION SLAVE ON *.*
   TO 'replicator'@'172.31.31.75'
   IDENTIFIED BY 'Rover123!';

Now we can configure the slave. Again, the slave is not a node in the Galera cluster.  It’s an extra server that will be replicating the transactions of one of the Galera nodes.


.. rst-class:: sub-heading
.. rubric:: Galera Slave Configuration & Preparation

To attach a server to a Galera node, so that it may act as a slave, we'll need to add a few lines to its configuration file.  Actually, we only need ``server-id`` and ``log-bin``.  You can see them below.  The rest are somewhat optional; They're for choosing the name and path of logs and other files.

.. code-block:: text

   [mysqld]
   ...
   server-id = 02

   log-bin = /var/log/mysql/slave-bin
   log-bin-index = /var/log/mysql/slave-bin.index
   binlog_format = MIXED

   relay-log-index = /var/lib/mysql/slave-relay-bin.index
   relay-log = /var/lib/mysql/slave-relay-bin

   read-only = 1
   innodb-read-only = 1

The only other parameter worth mentioning is the ``read-only`` option to make sure no one will edit the data.

Once we've configured the slave, we'll need to restart it.  Then we have to load the data back-up dump file we made on the master, using the ``mysql`` client. And we'll have to execute the CHANGE MASTER statement on the slave to tell it who is the master:

.. code-block:: mysql

   CHANGE MASTER TO
   MASTER_HOST='172.31.31.202',
   MASTER_PORT=3306,
   MASTER_USER='replicator',
   MASTER_PASSWORD='Rover123!';

Once all of this is done, we’ll be ready to start replication and using the slave as a back-up source.


.. rst-class:: sub-heading
.. rubric:: Backing-Up a Slave

With replication working, making back-ups is easy.  We just need to stop the slave from replicating and then start whatever back-up utility we want to use.  We'll also copy the database configuration files.  Here's how that might be done:

.. code-block:: text

   mysql -p -u root -e "STOP SLAVE"

   mysqldump -p -u admin_backup --flush-logs --all-databases \
             > /backups/temp/backup-20191025.sql

   cp -r /etc/my.cnf* /backups/temp/

In this example, everything it being copied into a temporary sub-directory. We would then use ``tar`` to make a single archive file and zip it:

.. code-block:: text

   cd /backups

   tar -czf mysql-backup-20191025.tgz ./temp/*

That's all we have to do, except start the slave again. Actually, we could have started it before starting ``tar``.

This method works well, but it requires an extra server just for back-ups.  A better choice is to use Galera Arbitrator, to use it to conduct the back-ups.  Let’s look at its purpose and how we might utilize it for back-ups.

.. container:: banner

   .. rst-class:: section-heading
   .. rubric:: Using Galera Arbitrator

The primary function of Galera Arbitrator, the daemon called, ``garbd``, is to act as a virtual node.  When there’s a tie vote among nodes about two conflicting transactions, the Arbitrator will cast the deciding vote.  Then all of the nodes will execute the winning transaction and Galera will continue with all nodes in agreement. This is function is portrayed in the diagram here.

Another function of Galera Arbitrator is to decide whether a joining node is in need of updates or a complete snapshot.  The former is known as an Increment State Transfer, an IST.  The latter is known as a State Snapshot Transfer, an SST.  New nodes will obviously need an SST.  The Arbitrator will then choose which node or nodes will provide the state transfer to the joining node.

This second function of Galera Arbitrator can be used in the same way to make back-ups, but with a little bit of coding.  Let’s look at how that might be done.


.. rst-class:: sub-heading
.. rubric:: Back-Ups with Galera Arbitrator

Although you can make a back-up fairly easily with ``mysqldump`` by removing a node from the cluster, and you can also make a back-up with ``rsync`` by shutting down ``mysqld`` on a node, it can be done more gracefully and with minimal interference with the Galera Cluster by using Galera Arbitrator.

Galera Arbitrator can receive a request to make a back-up, manually from the command-line using the ``garbd`` daemon, or it can be initiated automatically by a scheduling tool like ``cron``.

The Arbitrator chooses a node to be the donor |---| unless we tell it which to use. That node is then desynced. Incidentally, the back-up can be requested from any node in the cluster, and any node can be used to make the back-up.

The donor node will then execute the back-up script.  We’ll have to create such a script to use whatever tools we prefer and back-up how and where we want. Once the back-up is completed, the node will be re-synchronized.

Let’s take a look at how to configure Galera Arbitrator. Then we’ll look at how to create a back-up script.


.. rst-class:: sub-heading
.. rubric:: Configure Galera Arbitrator

Galera Arbitrator is included in the Galera Cluster software.  The Galera Arbitrator daemon may be called upon from the command-line for single functions, like making a back-up. To do this, we’ll have to construct a simple script to run whichever tool we prefer, such as ``mysqldump``.

First, using a plain text editor, we’ll create a configuration file for the Arbitrator daemon. Its file name and location aren't important, but ``/etc/garbd.cnf`` is a good choice. Below is an example:

.. code-block:: text

   group='galera-training'
   address="gcomm://172.31.30.39:4567,172.31.18.53:4567,172.31.26.106:4567"
   options="gmcast.listen_addr=tcp://0.0.0.0:4444"
   donor=“galera-3"
   log='/var/log/garbd.log'
   sst='backup_mysqldump'

The group parameter is to give the name of the cluster. This is equivalent to the parameter ``wsrep_cluster_name``. The address parameter is equivalent to the ``wsrep_cluster_address`` parameter, for listing the IP addresses of the nodes in the cluster and the ports to use.

The ``options`` parameter is equivalent to ``wsrep_provider_options``, but we have to specify ``gmcast.listen_addr`` and the address and port on which ``garbd`` daemon will listen for connections from other nodes.

The ``donor`` parameter is used to specify which node will perform the backup. The ``log`` parameter is used to specify the path and name of the log file.

The ``sst`` option provides the suffix of the back-up script.  It must be in the ``/usr/bin`` directory and start with the name ``wsrep_sst_``. So in the example here, the script’s name is ``wsrep_sst_backup_mysqldump``.

Those are all of the settings we need for Galera Arbitrator. We can actually set any or all of them from the command-line, but a configuration file is more convenient.  Now we need a back-up script.

.. rst-class:: sub-heading
.. rubric:: Back-Up Script

Below is a very simple back-up script which uses ``bash`` and ``mysqldump``. However, any scripting language and back-up utility is acceptable.  For some readers, this may be a little complicated.  Don't worry; we'll go through it.  For other readers, this is amateurish. It’s meant to be simple. What’s important is the basic concepts of how a script might be constructed to use Galera Arbitrator to make a back-up of a node.

.. code-block:: text

   #!/bin/bash

   # SET VARIABLES
   db_user='admin_backup'
   db_passwd='Rover123!'

   backup_dir='/backup'
   backup_sub_dir='temp'

   today=`date +"%Y%m%d"`
   backup_today="galera-mysqldump-$today.sql"
   gtid_file="gtid-$today.dat"


   # LOAD COMMON SCRIPT
   . /usr/bin/wsrep_sst_common


   # COPY CONFIGURATION FILES & SAVE GTID
   cp /etc/my.cnf $backup_dir/$backup_sub_dir/
   cp /etc/garb.cnf $backup_dir/$backup_sub_dir/

   echo "GTID: ${WSREP_SST_OPT_GTID}" > $backup_dir/$backup_sub_dir/$gtid_file


   # SAVE DATABASE TO DUMP FILE
   mysqldump --user="$db_user" --password="$db_passwd" \
             --flush-logs --all-databases \
             > $backup_dir/$backup_sub_dir/$backup_today

   # ARCHIVE BACK-UP FILES
   cd $backup_sub_dir
   tar -czf $backup_dir/$backup_today.tgz * --transform "s,^,$backup_today/,"


The first section defines some variables:  the user name and password it will use with ``mysqldump``.  There are more secure ways to do this, but we're trying to keep this script very straightforward. The next pair of variables contain the paths for storing the back-ups.  Then there's a variables that will store today's date to be part of the name of the back-up file.

The next stanza assembles the names of files: the dump file (e.g., ``galera-mysqldump-20191025.sql``), the data file for the GTID (e.g., ``gtid-20191025.dat``)

The second section is small, but it's important. It loads the common SST script that Galera Arbitrator uses.  Among other things, it will contain some variables we can use. In particular, it has the variable which contains the GTID.

In the third section, the script makes copies of the database configuration files (e.g., ``my.cnf``) and the Galera Arbitrator configuration file (e.g., ``garb.cnf``).  The last line in this section gets the GTID variable from the common script, and writes it to a text file.

The next section uses ``mysqldump`` to generate a dump file containing all of the databases on the node. We looked at the options already, so we'll move on.

In the last section, the script will use the tar command to create an archive file that will contain all of the files in the back-up sub-directory, and then zip that file (e.g., ``galera-mysqldump-20191025.tgz``). The ``--transform`` option is so that when it's extracted, it will put everything in a directory named based on today’s date.

That's everything:  it's everything we need.  Below is how we would execute this script from the command line, in conjunction with Galera Arbitrator:

.. code-block:: text

   garbd --cfg /etc/garb.cnf

This one option, ``--cfg`` is to give the path and name of the Galera Arbitrator configuration file.  The daemon will read it before doing anything.

.. rst-class:: section-heading
.. rubric:: Conclusion

Those are the primary ways in which DBAs can make back-ups when using Galera Cluster. There are some third-party software that provide some more advanced methods (e.g., XtraBackup).  But these are the more straightforward and most common methods.

.. container:: bottom-links

   Related Documents

   - :doc:`Install MySQL Galera <../../documentation/install-mysql>`

   Related Articles

   - :doc:`Galera Back-Ups (video) <../videos/galera-backup>`


.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
