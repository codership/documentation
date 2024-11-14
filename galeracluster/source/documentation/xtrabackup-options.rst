.. meta::
   :title: XtraBackup-v2 Parameters
   :description:
   :language: en-US
   :keywords: galera cluster, xtradb, xtrabackup-v2, parameters
   :copyright: Codership Oy, 2014 - 2024. All Rights Reserved.


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

.. container:: top-links

   - `Home <https://galeracluster.com>`_

   .. cssclass:: here

      - :doc:`Docs <./index>`

   - :doc:`KB <../kb/index>`

   .. cssclass:: nav-wider

      - :doc:`Training <../training/index>`

   - :doc:`FAQ <../faq>`


.. cssclass:: library-document
.. _`xtrabackup-parameters`:

======================
XtraBackup-v2 Parameters
======================

When using ``xtrabackup-v2`` as your :term:`State Snapshot Transfer` method, you can fine-tune how the script operates using the ``[sst]`` unit in the ``my.cnf`` configuration file.

.. code-block:: ini

   [mysqld]
   wsrep_sst_method=xtrabackup-v2

   [sst]
   compressor="gzip"
   decompressor="gzip -dc"
   rebuild=ON
   compact=ON
   encrypt=3
   tkey="/path/to/key.pem"
   tcert="/path/to/cert.pem"
   tca="/path/to/ca.pem"

Bear in mind, some ``XtraBackup-v2`` parameters require that you match the configuration on donor and joiner nodes, as designated in the table below.


.. csv-table::
   :class: doc-options
   :header: "Option", "Default", "Match"
   :widths: 30, 20, 20

   ":ref:`compressor <xtra-compressor>`", "", "No"
   ":ref:`compact <xtra-compact>`", "OFF", "No"
   ":ref:`cpat <xtra-cpat>`", "``0``", "No"
   ":ref:`decompressor <xtra-decompressor>`", "", "No"
   ":ref:`encrypt <xtra-encrypt>`", "``0``", "Yes"
   ":ref:`encrypt-algo <xtra-encrypt-algo>`", "0", "No"
   ":ref:`progress <xtra-progress>`", "", "No"
   ":ref:`rebuild <xtra-rebuild>`", "``OFF``", "No"
   ":ref:`rlimit <xtra-rlimit>`", "", "No"
   ":ref:`sockopt <xtra-sockopt>`", "", "No"
   ":ref:`sst_special_dirs <xtra-sst_special_dirs>`", "``1``", "No"
   ":ref:`streamfmt <xtra-streamfmt>`", "``xbstream``", "Yes"
   ":ref:`tca <xtra-tca>`", "", "No"
   ":ref:`tcert <xtra-tcert>`", "", "No"
   ":ref:`time <xtra-time>`", "``OFF``", "No"
   ":ref:`transferfmt <xtra-transferfmt>`", "``socat``", "Yes"
   ":ref:`joiner_timeout <xtra-joiner_timeout>`", "``60``", "No"
   ":ref:`donor_timeout <xtra-donor_timeout>`", "``10``", "No"


.. _`xtra-compressor`:
.. rst-class:: section-heading
.. rubric:: ``compressor``

Defines the compression utility the :term:`Donor Node` uses to compress the state transfer.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``compressor``"
   "", "Match:", "Yes"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", ""

This parameter defines whether the donor node performs compression on the state transfer stream. It also defines what compression utility it uses to perform the operation. You can use any compression utility which works on a stream, such as ``gzip`` or ``pigz``. Given that the :term:`Joiner Node` must decompress the state transfer before attempting to read it, you must match this parameter with the :ref:`decompressor <xtra-decompressor>` parameter, using the appropriate flags for each.

.. code-block:: ini

   compression="gzip"


.. _`xtra-compact`:
.. rst-class:: section-heading
.. rubric:: ``compact``

Defines whether the joiner node performs compaction when rebuilding indexes after applying a :term:`State Snapshot Transfer`.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``compact``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Boolean"
   "", "Default Value:", "``OFF``"

This parameter operates on the joiner node with the :ref:`rebuild <xtra-rebuild>` parameter. When enabled, the node performs compaction when rebuilding indexes after applying a state transfer.

.. code-block:: ini

   rebuild=ON
   compact=ON


.. _`xtra-cpat`:
.. rst-class:: section-heading
.. rubric:: ``cpat``

Defines what files to exclude from the clean up from the datadir during state transfers.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``cpat``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", "See below"

When the donor node begins a :term:`State Snapshot Transfer`, it cleans up various files from the datadir. This ensures that the joiner node can cleanly apply the state transfer. With this parameter, you can define what files you want the node to exclude from being deleted, before the state transfer.

.. code-block:: ini

   cpat='.\*\\.pem$\\|.\*init\\.ok$\\|.\*galera\\.cache$\\|.\*sst_in_progress$\\|.\*\\.sst$\\|.\*gvwstate\\.dat$\\|.\*grastate\\.dat$\\|.\*\\.err$\\|.\*\\.log$\\|.\*RPM_UPGRADE_MARKER$\\|.\*RPM_UPGRADE_HISTORY$'


.. _`xtra-decompressor`:
.. rst-class:: section-heading
.. rubric:: ``decompressor``

Defines the decompression utility the joiner node uses to decompress the state transfer.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``decompressor``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", ""

This parameter defines whether the joiner node performs decompression on the state transfer stream. It also defines what decompression utility it uses to perform the operation. You can use any compression utility which works on a stream, such as ``gzip`` or ``pigz``. Given that the donor node must compress the state transfer before sending it, you must match this parameter with the :ref:`compressor <xtra-compressor>` parameter, using the appropriate flags for each.

.. code-block:: ini

   decompressor="gzip -dc"


.. _`xtra-encrypt`:
.. rst-class:: section-heading
.. rubric:: ``encrypt``

Defines whether the node uses SSL encryption for XtraBackup and what kind of encryption it uses.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``encrypt``"
   "", "Match:", "Yes"
   "**Permitted Values**", "Type:", "Integer"
   "", "Default Value:", "``0``"

This parameter determines the type of SSL encryption the node uses when sending state transfers through xtrabackup. The recommended type is ``2`` when using the cluster over WAN.

.. csv-table::
   :class: doc-options
   :header: "Value", "Description"
   :widths: 10, 90

   "``0``", "No encryption."
   "``1``", "The node encrypts State Snapshot Transfers through XtraBackup."
   "``2``", "The node encrypts State Snapshot Transfers through OpenSSL, using Socat."
   "``3``", "The node encrypts State Snapshot Transfers through the key and certificate files implemented for Galera Cluster."


.. code-block:: ini

   encrypt=3
   tkey="/path/to/key.pem"
   tcert="/path/to/cert.pem"
   tca="/path/to/ca.pem"


.. _`xtra-encrypt-algo`:
.. rst-class:: section-heading
.. rubric:: ``encrypt-algo``

Defines the SSL encryption type the node uses for XtraBackup state transfers.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``encrypt-algo``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Integer"
   "", "Default Value:", "``0``"

When using the :ref:`encrypt <xtra-encrypt>` parameter in both the ``[xtrabackup]`` and ``[sst]`` units, there is a potential issue in it having different meanings according to the unit under which it occurs. That is, in ``[xtrabackup]``, it turns encryption on while in ``[sst]`` it both turns it on and specifies the algorithm.

In the event that you need to clarify the meaning, this parameter allows you to define the encryption algorithm separately from turning encryption on. It is only read in the event that :ref:`encrypt <xtra-encrypt>` is set to ``1``

.. code-block:: ini

   encrypt=1
   encrypt-algo=3



.. _`xtra-progress`:
.. rst-class:: section-heading
.. rubric:: ``progress``

Defines whether where the node reports :term:`State Snapshot Transfer` progress.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``progress``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", ""
   "", "Valid Values:", "``1``; /path/to/file"

When you set this parameter, the node reports progress on XtraBackup progress in state transfers. If you set the value to ``1``, the node makes these reports to the database server stderr. If you set the value to a file path, it writes the progress to that file.

.. note:: Keep in mind, that a ``0`` value is invalid. If you want to disable this parameter, delete or comment it out.

.. code-block:: ini

   progress="/var/log/mysql/xtrabackup-progress.log"


.. _`xtra-rebuild`:
.. rst-class:: section-heading
.. rubric:: ``rebuild``

Defines whether the joiner node rebuilds indexes during a :term:`State Snapshot Transfer`.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``rebuild``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Boolean"
   "", "Default Value:", "``OFF``"

This parameter operates on the joiner node. When enabled, the node rebuilds indexes when applying the state transfer. Bear in mind, this operation is separate from compaction. Due to `Bug #1192834 <https://bugs.launchpad.net/percona-xtrabackup/+bug/1192834>`_, it is recommended that you use this parameter with :ref:`compact <xtra-compact>`.

.. code-block:: ini

   rebuild=ON
   compact=ON


.. _`xtra-rlimit`:
.. rst-class:: section-heading
.. rubric:: ``rlimit``

Defines the rate limit for the donor node.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``rlimit``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Integer"
   "", "Default Value:", ""

This parameter allows you to define the rate-limit for the donor node. This allows you to keep state transfers from blocking regular cluster operations.

.. code-block:: ini

   rlimit=300M

.. _`xtra-sockopt`:
.. rst-class:: section-heading
.. rubric:: ``sockopt``

Defines socket options.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``sockopt``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", ""

This parameter allows you to define one or more socket options for XtraBackup using the Socat transfer format.

.. _`xtra-sst_special_dirs`:
.. rst-class:: section-heading
.. rubric:: ``sst_special_dirs``

Defines whether the node uses special InnoDB home and log directories.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``sst_special_dirs``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Boolean"
   "", "Default Value:", "``OFF``"

This parameter enables support for ``innodb_data_home_dir`` and ``innodb_log_home_dir`` parameters for XtraBackup. It requires that you define ``innodb_data_home_dir`` and ``innodb_log_group_home_dir`` in the ``[mysqld]`` unit.

.. code-block:: ini

   [mysqld]
   innodb_data_home_dir="/var/mysqld/innodb"
   innodb_log_group_home_dir="/var/log/innodb"
   wsrep_sst_method="xtrabackup-v2"

   [sst]
   sst_special_dirs=TRUE

.. _`xtra-streamfmt`:
.. rst-class:: section-heading
.. rubric:: ``streamfmt``

Defines the stream formatting utility.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``streamfmt``"
   "", "Match:", "Yes"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", "``xbstream``"
   "", "Valid Values:", "``tar``; ``xbstream``"

This parameter defines the utility the node uses to archive the node state before the transfer is sent and how to unarchive the state transfers that it receives. There are two methods available: ``tar`` and ``xbstream``. Given that the receiving node needs to know how to read the stream, it is necessary that both nodes use the same values for this parameter.

The default and recommended utility is ``xbstream`` given that it supports encryption, compression, parallel streaming, incremental backups and compaction. ``tar`` does not support these features.


.. code-block:: ini

   streamfmt='xbstream'


.. _`xtra-tca`:
.. rst-class:: section-heading
.. rubric:: ``tca``

Defines the Certificate Authority (CA) to use in SSL encryption.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``tca``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Path"
   "", "Default Value:", ""

This parameter defines the Certificate Authority (CA) file that the node uses with XtraBackup state transfers. In order to use SSL encryption with XtraBackup, you must configure  the :ref:`transferfmt <xtra-transferfmt>` parameter to use ``socat``.

For more information on using Socat with encryption, see `Securing Traffic between Two Socat Instances using SSL <https://www.dest-unreach.org/socat/doc/socat-openssltunnel.html>`_.

.. code-block:: ini

   transferfmt="socat"
   tca="/path/to/ca.pem"


.. _`xtra-tcert`:
.. rst-class:: section-heading
.. rubric:: ``tcert``

Defines the certificate to use in SSL encryption.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``tcert``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", ""

This parameter defines the SSL certificate file that the node uses with SSL encryption on XtraBackup state transfers. In order to use SSL encryption with XtraBackup, you must configure the :ref:`transferfmt <xtra-transferfmt>` parameter to use Socat.

For more information on using Socat with encryption, see `Securing Traffic between Two Socat Instances using SSL <https://www.dest-unreach.org/socat/doc/socat-openssltunnel.html>`_.

.. code-block:: ini

   transferfmt="socat"
   tcert="/path/to/cert.pem"


.. _`xtra-time`:
.. rst-class:: section-heading
.. rubric:: ``time``

Defines whether XtraBackup instruments key stages in the backup and restore process for state transfers.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``time``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Boolean"
   "", "Default Value:", "``OFF``"

This parameter instruments key stages of the backup and restore process for state transfers.

.. code-block:: ini

   time=ON

.. _`xtra-transferfmt`:
.. rst-class:: section-heading
.. rubric:: ``transferfmt``

Defines the transfer stream utility.

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``transferfmt``"
   "", "Match:", "Yes"
   "**Permitted Values**", "Type:", "String"
   "", "Default Value:", "``socat`` "
   "", "Valid Values:", "``socat``; ``nc``"

This parameter defines the utility that the node uses to format transfers sent from donor to joiner nodes. There are two methods supported: ``socat`` and ``nc``. Given that the receiving node needs to know how to interpret the transfer, it is necessary that both nodes use the same values for this parameter.

The default and recommended utility is Socat, given that it allows for socket options, such as transfer buffer size. For more information, see the `socat Documentation <https://www.dest-unreach.org/socat/doc/socat.html>`_.

.. code-block:: ini

   transferfmt="socat"


.. _`xtra-joiner_timeout`:
.. rst-class:: section-heading
.. rubric:: ``joiner_timeout``

How soon the joiner should timeout when waiting for SST (seconds).

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``joiner_timeout``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Integer"
   "", "Default Value:", "``60``"

This parameter determines the initial timeout in seconds for the joiner to receive the first packet in a :term:`State Snapshot Transfer`. This keeps the joiner node from hanging, in the event that the donor node crashes while starting the operation.

.. code-block:: ini

   joiner_timeout=120


.. _`xtra-donor_timeout`:
.. rst-class:: section-heading
.. rubric:: ``donor_timeout``

How soon the donor should timeout on connection to joiner (seconds).

.. csv-table::
   :class: doc-options
   :stub-columns: 1

   "**System Variable**", "Name:", "``donor_timeout``"
   "", "Match:", "No"
   "**Permitted Values**", "Type:", "Integer"
   "", "Default Value:", "``10``"

This parameter determines how soon the donor should timeout on connection to joiner, and return to normal operation in the event that the joiner turns unresponsive.

.. code-block:: ini

   donor_timeout=5

