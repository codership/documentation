.. meta::
   :title: Gaps in GTID Sequence Numbers
   :description:
   :language: en-US
   :keywords:
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


.. container:: left-margin

   .. container:: left-margin-top

      :doc:`The Library <../index>`

   .. container:: left-margin-content

      - :doc:`Documentation <../documentation/index>`

      .. cssclass:: here

         - :doc:`Knowledge Base <./index>`

      - :doc:`Training <../training/index>`

      .. cssclass:: sub-links

         - :doc:`Training Courses <../training/courses/index>`
         - :doc:`Tutorial Articles <../training/tutorials/index>`
         - :doc:`Training Videos <../training/videos/index>`

      - :doc:`FAQ <../faq>`
      - :ref:`search`

      Related Documents

      - :doc:`Schema Upgrades <../../documentation/schema-upgrades>`
      - :ref:`wsrep_OSU_method <wsrep_OSU_method>`

.. container:: top-links

   - `Home <https://galeracluster.com>`_
   - :doc:`Docs <../documentation/index>`

   .. cssclass:: here

      - :doc:`KB <./index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-article
.. _`kb-trouble-gaps-in-gtid-sequence-numbers`:

================================
Gaps in GTID Sequence Numbers
================================

.. rst-class:: article-stats

   Length: 421 words; Published: October 22, 2024; Updated: October 22, 2024; Category: State Transfers; Type: Troubleshooting

GTID gaps may occur if ``gtid_next`` is set to a specific value, and a transaction fails.

.. rst-class:: section-heading
.. rubric:: Scenario

When a failing DDL statement with a GTID seqno is replicated by TOI, the failed DDL is not logged in the binary log and, therefore, the binlog will contain GTID event gaps.

Below is an example of a failing DDL statement:

.. code-block:: mysql

   create table t_fail (i int primary key, j int, foreign key(j) references non_existing(i))

And an example of binlog events after the statement has been issued:

.. code-block:: mysql

   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:1'
   use `test`; create table t1 (i int primary key, j int) /* xid=3 */
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:2'
   use `test`; create table t2 (i int primary key, j int, foreign key(j) references t1(i)) /* xid=4 */
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:4'
   use `test`; create table t3 (i int primary key, j int, foreign key(j) references t1(i)) /* xid=6 */

Here, GTID seqno 3 is allocated for the ``create table`` statement, but the related GTID event is missing from the binlog file.

The excerpt from the binlog suggests that the ``gtid_next`` value is manually set before every executed transaction. For a failed transaction, this GTID value is not binlogged, although it is counted as used.

In other words, for GTID values manually set with ``gtid_next``, there is a possibility of creating a gap in the binlog. This is allowed to happen, as the replication subsystem is based on the ``gtid_executed`` variable, when determining which events should be replicated between the primary and the replica, and not on the binlog contents. Binlog solely becomes a storage for all GTIDs executed, to transfer them over to the replica.

.. rst-class:: section-heading
.. rubric:: Solution

The solution to mitigate GTID gaps is to re-assign the same ``gtid_next`` value to the next successful transaction after the failed one:

.. code-block:: mysql

   # Record some GTID
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:1';
   CREATE TABLE t1 (i INT PRIMARY KEY, j INT) ENGINE=InnoDB;
   
   # Now miss a GTID value by failing a transaction
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:2';
   --error 0, 1824
   CREATE TABLE t_fail (i INT PRIMARY KEY, j INT, FOREIGN KEY(j) REFERENCES NON_EXISTING(i)) ENGINE=InnoDB;
   
   # Write successful transaction with the same GTID
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:2';
   DROP TABLE t1;

   # Rotate binlog file to generate Previous_gtids_log_event
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:3';
   FLUSH LOGS;
   
This results in a binlog with no GTID gaps:

.. code-block:: mysql

   #241021 11:49:48 server id 1 end_log_pos 197 CRC32 0x5912150c Previous-GTIDs
   # a9264492-7be5-11ef-b353-ca382343a2f9:1-2
   # at 197
   ...
   
   SET @@SESSION.GTID_NEXT= 'a9264492-7be5-11ef-b353-ca382343a2f9:3'/*!*/;
   # at 274
   ...


.. container:: bottom-links

   Related Documents

   - :doc:`State Transfers <../../documentation/sst>`
   - :doc:`TCP/UDP Ports </../../documentation/firewall-settings>`
   - :ref:`wsrep_node_name <wsrep_node_name>`
   - :ref:`wsrep_sst_donor <wsrep_sst_donor>`
   - :ref:`gmcast.segment <gmcast.segment>`

.. |---|   unicode:: U+2014 .. EM DASH
   :trim:
