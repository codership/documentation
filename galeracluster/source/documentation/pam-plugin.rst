.. meta::
   :title: PAM Authentication Plugin
   :description: Galera PAM Authentication Plugin is a free and Open Source implementation of the MySQL‘s authentication plugin.
   :language: en-US
   :keywords: galera cluster, PAM
   :copyright: This software documentation is (C)2009-2018 Percona LLC and/or its affiliates and is distributed under the Creative Commons Attribution-ShareAlike 2.0 Generic license.

.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      .. cssclass:: here

         - :doc:`Documentation <./index>`

      - :doc:`Knowledge Base <../kb/index>`
      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :doc:`galera-parameters`

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`pam-plugin`:

===========================
 PAM Authentication Plugin
===========================

.. index::
   pair: Descriptions; PAM Authentication Plugin

This software documentation is (C)2009-2018 Percona LLC and/or its affiliates and is distributed under the `Creative Commons Attribution-ShareAlike 2.0 Generic license <http://creativecommons.org/licenses/by-sa/2.0/>`_.

Pluggable Authentication Modules (PAM) Authentication Plugin is a free and Open Source implementation of the MySQL‘s authentication plugin. This plugin acts as a mediator between the MySQL server, the MySQL client, and the PAM stack. The server plugin requests authentication from the PAM stack, forwards any requests and messages from the PAM stack over the wire to the client (in cleartext) and reads back any replies for the PAM stack.

PAM plugin uses dialog as its client side plugin. The dialog plugin can be loaded to any client application that uses the ``libperconaserverclient``/``libmysqlclient`` library.

Some of the benefits of the dialog plugin offers over the default one:

- It correctly recognizes whether PAM wants input to be echoed or not, while the default one always echoes the input on the user’s console.

- It can use the password, which is passed to MySQL client through the ``-p`` parameter.

- Dialog client installation bug has been fixed.

- This plugin works on MySQL and Percona Server.

There are two versions of this plugin:

- Full PAM plugin called *auth_pam*. This plugin uses *dialog.so*. It fully supports the PAM protocol with arbitrary communication between client and server.

- Oracle-compatible PAM called *auth_pam_compat*. This plugin uses *mysql_clear_password*, which is a part of Oracle MySQL client. It also has some limitations, such as, it supports only one password input. You must use the ``-p`` option to pass the password to *auth_pam_compat*.

To choose which plugin version you want to use, use the *IDENTIFIED WITH ‘auth_pam’* for *auth_pam*, and *IDENTIFIED WITH ‘auth_pam_compat’* for *auth_pam_compat*.

.. _`pam-plugin-installing`:
.. rst-class:: section-heading
.. rubric:: Installation

To manually deploy the plugin, run the command below:

.. code-block:: console

   mysql> INSTALL PLUGIN auth_pam SONAME 'auth_pam.so';

After the plugin has been installed, it should be present in the plugins list. To check if the plugin has been correctly installed and active,  run the command below:

.. code-block:: console

   mysql> SHOW PLUGINS;
   ...
   ...
   | auth_pam                       | ACTIVE   | AUTHENTICATION     | auth_pam.so | GPL     |



.. _`pam-plugin-configuration`:
.. rst-class:: section-heading
.. rubric:: Configuration

To use the plugin, configure the authentication method. A simple setup would be to use the standard UNIX authentication method (``pam_unix``).

.. note:: To use ``pam_unix``, mysql must be added to the shadow group, to have enough privileges to read the */etc/shadow*.

A sample */etc/pam.d/mysqld* file:

.. code-block:: console

   auth       required     pam_unix.so
   account    required     pam_unix.so

For added information in *system log*, you can expand it to be:

.. code-block:: console

   auth       required     pam_warn.so
   auth       required     pam_unix.so audit
   account    required     pam_unix.so audit


.. _`pam-plugin-creating-a-user`:
.. rst-class:: section-heading
.. rubric:: Creating a user

After the PAM plugin has been configured, you can create users with the PAM plugin as the authentication method:

.. code-block:: console

   mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED WITH auth_pam;

This will create a user ``newuser`` that can connect from ``localhost``, who will be authenticated using the PAM plugin. If the ``pam_unix`` method is being used, the user must exist on the system.


.. _`pam-plugin-supplementary-groups-support`:
.. rst-class:: section-heading
.. rubric:: Supplementary groups support

The plugin supports supplementary groups. Supplementary or secondary groups are extra groups a specific user is member of. For example, user ``joe`` might be a member of groups: ``joe`` (his primary group) and secondary groups ``developers`` and ``dba``. A complete list of groups and users belonging to them can be checked with the ``cat /etc/group`` command.

This feature enables using secondary groups in the mapping part of the authentication string, like “``mysql, developers=joe, dba=mark``”. Previously, only primary groups could have been specified there. If user is a member of both ``developers`` and ``dba``, the PAM plugin will map it to ``joe``, as ``developers`` matches first.


.. _`pam-plugin-known-issues`:
.. rst-class:: section-heading
.. rubric:: Known issues

The default mysql stack size is not enough to handle the ``pam_ecryptfs`` module. A workaround is to increase the MySQL stack size by setting the ``thread-stack`` variable to at least ``512KB`` or by increasing the old value by ``256KB``.

PAM authentication can fail with ``mysqld: pam_unix(mysqld:account): Fork failed: Cannot allocate memory`` error in ``/var/log/secure`` even when there is enough memory available. Current workaround is to set ``vm.overcommit_memory`` to ``1``:

.. code-block:: console

   echo 1 > /proc/sys/vm/overcommit_memory


and by adding the ``vm.overcommit_memory = 1`` to ``/etc/sysctl.conf`` to make the change permanent after reboot. Authentication of internal (that is, non-PAM) accounts continues to work fine when mysqld reaches this memory utilization level.

.. note:: Setting the ``vm.overcommit_memory`` to ``1`` will cause kernel to perform no memory overcommit handling, which can increase the potential for memory overload and invoking of OOM killer.



.. container:: bottom-links

   Related Documents

   - :doc:`galera-parameters`
