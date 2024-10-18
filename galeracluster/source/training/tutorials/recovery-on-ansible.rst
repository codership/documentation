.. meta::
   :title: Recovering a Galera Node or Cluster on Ansible
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


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
      - :ref:`search`

      Related Documents

      - :ref:`gcache.recover <gcache.recover>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../../documentation/index>`
   - :doc:`KB <../../kb/index>`

   .. cssclass:: here nav-wider

      - :doc:`Training <../index>`

   - :doc:`FAQ <../../faq>`


.. cssclass:: library-article
.. _`recovery-on-ansible`:

=========================================================
Recovering a Galera Node or the Entire Cluster on Ansible
=========================================================

Occasionally, you may have to recover a cluster node or an entire Galera Cluster. This tutorial describes how to recover a node or the cluster when using the Ansible automation software application.

Run the ``galera-bootstrap`` playbook to automatically recover a node or an entire environment. Run the ``galera install`` playbook using the galera-bootstrap tag to auto recover a node or an entire environment.

Run the following Ansible command to show the failed nodes:

.. code-block:: console

   # openstack-ansible galera-install.yml --tags galera-bootstrap

The cluster comes back online after completion of this command.

.. _`single-node-failure`:
.. rst-class:: section-heading
.. rubric:: Single-node Failure

If a single node fails, the other nodes maintain quorum and continue to process SQL requests.

Run the following Ansible command to determine the failed node:

.. code-block:: console

   # ansible galera_container -m shell -a "mysql -h localhost \
   -e 'show status like \"%wsrep_cluster_%\";'"
   node3_galera_container-3ea2cbd3 | FAILED | rc=1 >>
   ERROR 2002 (HY000): Can't connect to local MySQL server through
   socket '/var/run/mysqld/mysqld.sock' (111)
   
   node2_galera_container-49a47d25 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     17
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     17
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary

In this example, node 3 has failed.

Restart MariaDB on the failed node and verify that it rejoins the cluster.

If MariaDB fails to start, run the mysqld command and perform further analysis on the output. As a last resort, rebuild the container for the node.

.. _`'multi-node-failure`:
.. rst-class:: section-heading
.. rubric:: Multi-node Failure

When all but one node fails, the remaining node cannot achieve quorum and stops processing SQL requests. In this situation, failed nodes that recover cannot join the cluster because it no longer exists.

Run the following Ansible command to show the failed nodes:

.. code-block:: console
   
   # ansible galera_container -m shell -a "mysql \
   -h localhost -e 'show status like \"%wsrep_cluster_%\";'"
   node2_galera_container-49a47d25 | FAILED | rc=1 >>
   ERROR 2002 (HY000): Can't connect to local MySQL server
   through socket '/var/run/mysqld/mysqld.sock' (111)
   
   node3_galera_container-3ea2cbd3 | FAILED | rc=1 >>
   ERROR 2002 (HY000): Can't connect to local MySQL server
   through socket '/var/run/mysqld/mysqld.sock' (111)
   
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     18446744073709551615
   wsrep_cluster_size        1
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      non-Primary

In this example, nodes 2 and 3 have failed. The remaining operational server indicates non-Primary because it cannot achieve quorum.

Run the following command to ``rebootstrap`` the operational node into the cluster:

.. code-block:: console
   
   # mysql -e "SET GLOBAL wsrep_provider_options='pc.bootstrap=yes';"
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     15
   wsrep_cluster_size        1
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node3_galera_container-3ea2cbd3 | FAILED | rc=1 >>
   ERROR 2002 (HY000): Can't connect to local MySQL server
   through socket '/var/run/mysqld/mysqld.sock' (111)
   
   node2_galera_container-49a47d25 | FAILED | rc=1 >>
   ERROR 2002 (HY000): Can't connect to local MySQL server
   through socket '/var/run/mysqld/mysqld.sock' (111)

The remaining operational node becomes the primary node and begins processing SQL requests.

Restart MariaDB on the failed nodes and verify that they rejoin the cluster:

.. code-block:: console
   
   # ansible galera_container -m shell -a "mysql \
   -h localhost -e 'show status like \"%wsrep_cluster_%\";'"
   node3_galera_container-3ea2cbd3 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     17
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node2_galera_container-49a47d25 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     17
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     17
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary

If MariaDB fails to start on any of the failed nodes, run the ``mysqld`` command and perform further analysis on the output. As a last resort, rebuild the container for the node.


.. _`complete-failure`:
.. rst-class:: section-heading
.. rubric:: Complete Failure

Restore from backup if all of the nodes in a Galera Cluster fail (do not shutdown gracefully). Run the following command to determine if all nodes in the cluster have failed:

.. code-block:: console
   
   # ansible galera_container -m shell -a "cat /var/lib/mysql/grastate.dat"
   node3_galera_container-3ea2cbd3 | success | rc=0 >>
   # GALERA saved state
   version: 2.1
   uuid:    338b06b0-2948-11e4-9d06-bef42f6c52f1
   seqno:   -1
   cert_index:
   
   node2_galera_container-49a47d25 | success | rc=0 >>
   # GALERA saved state
   version: 2.1
   uuid:    338b06b0-2948-11e4-9d06-bef42f6c52f1
   seqno:   -1
   cert_index:
   
   node4_galera_container-76275635 | success | rc=0 >>
   # GALERA saved state
   version: 2.1
   uuid:    338b06b0-2948-11e4-9d06-bef42f6c52f1
   seqno:   -1
   cert_index:

All the nodes have failed if ``mysqld`` is not running on any of the nodes and all of the nodes contain a ``seqno`` value of -1.

If any single node has a positive ``seqno`` value, then that node can be used to restart the cluster. However, because there is no guarantee that each node has an identical copy of the data, we do not recommend to restart the cluster using the ``--wsrep-new-cluster`` command on one node.


.. _`rebuilding-a-container`:
.. rst-class:: section-heading
.. rubric:: Rebuilding a Container

Recovering from certain failures require rebuilding one or more containers.

Disable the failed node on the load balancer.

.. note:: Do not rely on the load balancer health checks to disable the node. If the node is not disabled, the load balancer sends SQL requests to it before it rejoins the cluster and cause data inconsistencies.

Destroy the container and remove MariaDB data stored outside of the container:

.. code-block:: console
   
   # lxc-stop -n node3_galera_container-3ea2cbd3
   # lxc-destroy -n node3_galera_container-3ea2cbd3
   # rm -rf /openstack/node3_galera_container-3ea2cbd3/*

In this example, node 3 failed.

Run the host setup playbook to rebuild the container on node 3:

.. code-block:: console
   
   # openstack-ansible setup-hosts.yml -l node3 \
   -l node3_galera_container-3ea2cbd3

The playbook restarts all other containers on the node.

Run the infrastructure playbook to configure the container specifically on node 3:

.. code-block:: console
   
   # openstack-ansible setup-infrastructure.yml \
   -l node3_galera_container-3ea2cbd3

.. warning:: The new container runs a single-node Galera Cluster, which is a dangerous state because the environment contains more than one active database with potentially different data.

.. code-block:: console
   
   # ansible galera_container -m shell -a "mysql \
   -h localhost -e 'show status like \"%wsrep_cluster_%\";'"
   node3_galera_container-3ea2cbd3 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     1
   wsrep_cluster_size        1
   wsrep_cluster_state_uuid  da078d01-29e5-11e4-a051-03d896dbdb2d
   wsrep_cluster_status      Primary
   
   node2_galera_container-49a47d25 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     4
   wsrep_cluster_size        2
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     4
   wsrep_cluster_size        2
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary

Restart MariaDB in the new container and verify that it rejoins the cluster.

.. note:: In larger deployments, it may take some time for the MariaDB daemon to start in the new container. It will be synchronizing data from the other MariaDB servers during this time. You can monitor the status during this process by tailing the ``/var/log/mysql_logs/galera_server_error.log`` log file.

   Lines starting with ``WSREP_SST`` will appear during the sync process and you should see a line with ``WSREP: SST complete, seqno: <NUMBER>`` if the sync was successful.

.. code-block:: console
   
   # ansible galera_container -m shell -a "mysql \
   -h localhost -e 'show status like \"%wsrep_cluster_%\";'"
   node2_galera_container-49a47d25 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     5
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node3_galera_container-3ea2cbd3 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     5
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary
   
   node4_galera_container-76275635 | success | rc=0 >>
   Variable_name             Value
   wsrep_cluster_conf_id     5
   wsrep_cluster_size        3
   wsrep_cluster_state_uuid  338b06b0-2948-11e4-9d06-bef42f6c52f1
   wsrep_cluster_status      Primary

Enable the failed node on the load balancer.

.. note:: This documentation is distributed under the `Creative Commons Attribution-ShareAlike 2.0 Generic license <http://creativecommons.org/licenses/by-sa/2.0/>`_.


.. container:: bottom-links

   Related Documents

   - :ref:`gcache.recover <gcache.recover>`
