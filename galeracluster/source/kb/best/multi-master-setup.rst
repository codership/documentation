=====================================
 Multi-Master Setup
=====================================
.. _`kb-best-multi-master-setup`:

A master is a node that can simultaneously process writes from clients. The more masters in a cluster, the higher the probability of certification conflicts.  This can lead to undesirable rollbacks and performance degradation.

If you find you experience frequent certification conflicts, consider reducing the number of nodes the cluster uses as masters.
