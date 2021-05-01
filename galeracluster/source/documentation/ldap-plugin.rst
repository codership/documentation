.. meta::
   :title: LDAP Authentication Plugin
   :description: Galera LDAP plugin is a free and open source implementation of the MySQL Enterprise Simple LDAP plugin.
   :language: en-US
   :keywords: galera cluster, LDAP
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
.. _`auditlogplugin`:

===========================
 LDAP Authentication Plugin
===========================

.. index::
   pair: Descriptions; LDAP Authentication Plugin

This software documentation is (C)2009-2018 Percona LLC and/or its affiliates and is distributed under the `Creative Commons Attribution-ShareAlike 2.0 Generic license <http://creativecommons.org/licenses/by-sa/2.0/>`_.

LDAP (Lightweight Directory Access Protocol) provides an alternative method to access existing directory servers, which maintain information about individuals, groups, and organizations.

.. _`ldap-plugin-installing`:
.. rst-class:: section-heading
.. rubric:: Installation

To deploy the plugin, run the command below:

.. code-block:: console

   mysql> INSTALL PLUGIN authentication_ldap_simple SONAME 'authentication_ldap_simple.so';

The installation adds the variables below:

.. csv-table::
   :class: doc-options
   :header: "|br| Name", "|br| Description", "|br| Default", "|br| Minimum", "|br| Maximum", "|br| Scope," "|br| Dynamic," "|br| Type,"
   :widths: 30, 30, 20, 10, 10, 10, 10, 10

   "authentication_ldap_simple_bind_base_dn", "Base distinguished name (DN)", "", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_bind_root_dn", "Root distinguished name (DN)", "", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_bind_root_pwd", "Password for the root distinguished name", "", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_ca_path", "Absolute path of the certificate authority file", "", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_group_search_attr", "Name of the attribute that specifies the group names in LDAP directory entries", "CN", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_group_search_filter", "Custom group search filter", "(|(&(objectClass=posixGroup)(memberUid={UA}))(&(objectClass=group)(member={UD})))", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_init_pool_size", "Initial size of the connection pool to the LDAP server", "10", "1", "32767", "global", "Yes", "uint"
   "authentication_ldap_simple_log_status", "Logging level", "1", "1", "5", "global", "Yes", "uint"
   "authentication_ldap_simple_max_pool_size", "Maximum size of the pool of connections to the LDAP server", "1000", "1", "32767", "global", "Yes", "uint"
   "authentication_ldap_simple_server_host", "LDAP server host", "", "", "", "global", "Yes", "string"
   "authentication_ldap_simple_server_port", "LDAP server TCP/IP port number", "389", "1", "65535", "global", "Yes", "uint"
   "authentication_ldap_simple_ssl", "Are connections by the plugin to the LDAP server using the SSL protocol (ldaps://)", "OFF", "", "", "global", "Yes", "bool"
   "authentication_ldap_simple_tls", "Are connections by the plugin to the LDAP server secured with STARTTTLS (ldap://)", "OFF", "", "", "global", "Yes", "bool"
   "authentication_ldap_simple_user_search_attr", "Name of the attribute that specifies user names in LDAP directory entries", "uid", "", "", "global", "Yes", "string"

For simple LDAP authentication, you must specify the ``authentication_ldap_simple`` plugin in the ``CREATE USER`` statement or ``ALTER USER`` statement.

.. code-block:: console

   CREATE USER ... IDENTIFIED WITH authentication_ldap_simple;
   
   or
   
   CREATE USER ... IDENTIFIED WITH authentication_ldap_simple BY 'cn=[user
   name],ou=[organization unit],dc=[domain component],dc=com'

.. note:: If you create a user is with the ``BY ‘cn,ou,dc,dc’``, the variables below are not used:
   - ``authentication_ldap_simple_bind_base_dn``
   - ``authentication_ldap_simple_bind_root_dn``
   - ``authentication_ldap_simple_bind_root_pwd``
   - ``authentication_ldap_simple_user_search_attr``
   - ``authentication_ldap_simple_group_search_attr``
   
   If you create a user with ``IDENTIFIED BY authentication_ldap_simple``, the variables are used.

If a MySQL user *test1* has the following entry in the LDAP directory:

.. code-block:: console

   uid=test1, ou=users, dc=hr, dc=com

To create a MySQL account for *test1*, use the following statement::

.. code-block:: console

   CREATE USER 'test1'@'localhost'
   IDENTIFIED WITH authentication_ldap_simple
   AS 'uid=test1,ou=users,dc=hr,dc=com';

.. note:: For security reasons, the plugin requires sending the password in clear text.


.. _`ldap-plugin-uninstalling`:
.. rst-class:: section-heading
.. rubric:: Uninstallation

To uninstall the plugin, run the command below:

.. code-block:: console

   mysql> UNINSTALL PLUGIN authentication_ldap_simple;

.. container:: bottom-links

   Related Documents

   - :doc:`galera-parameters`
