---
title: "Bare-metal node maintenance"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-bmn-maintenance
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-bmn-maintenance
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Bare-metal node maintenance

[id="troubleshooting-bmn-maintenance"]
= Bare-metal node maintenance

You can connect to a node for general troubleshooting.
However, in some cases, you need to perform troubleshooting or maintenance tasks on certain hardware components.
This section discusses topics that you need to perform for hardware maintenance.

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-bmn-maintenance.adoc

[id="troubleshooting-bmn-connect-to-node_{context}"]
= Connecting to a bare-metal node in your cluster

[role="_abstract"]
You can connect to bare-metal cluster nodes for general maintenance tasks.

[NOTE]
====
Configuring the cluster node from the host operating system is not recommended or supported.
====

To troubleshoot your nodes, you can do the following tasks:

* Retrieve logs from a node
* Use debugging
* Use SSH to connect to a node

[IMPORTANT]
====
Use SSH only if you cannot connect to the node with the `oc debug` command.
====

.Procedure

. Retrieve the logs from a node by running the following command:
+
[source,terminal]
----
$ oc adm node-logs <node_name> -u crio
----

. Use debugging by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----
+
You are now logged in as root on the node.

. Optional: Use SSH to connect to the node by running the following command:
+
[source,terminal]
----
$ ssh core@<node_name>
----
// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-bmn-maintenance.adoc

[id="troubleshooting-bmn-move-apps-to-pods_{context}"]
= Moving applications to pods within the cluster

[role="_abstract"]
For scheduled hardware maintenance, you need to consider how to move your application pods to other nodes within the cluster without affecting the pod workload.

.Procedure

* Mark the node as unschedulable by running the following command:
+
[source,terminal]
----
$ oc adm cordon <node_name>
----
+
When the node is unschedulable, no pods can be scheduled on the node. For more information, see "Working with nodes".
+
[NOTE]
====
When moving CNF applications, you might need to verify ahead of time that there are enough additional worker nodes in the cluster due to anti-affinity and pod disruption budget.
====

[role="_additional-resources"]
.Additional resources

* Working with nodes

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-bmn-maintenance.adoc

[id="troubleshooting-bmn-replace-dimm_{context}"]
= DIMM memory replacement

[role="_abstract"]
Dual in-line memory module (DIMM) problems sometimes only appear after a server reboots.
You can check the log files for these problems.

When you perform a standard reboot and the server does not start, you can see a message in the console that there is a faulty DIMM memory.
In that case, you can acknowledge the faulty DIMM and continue rebooting if the remaining memory is sufficient.
Then, you can schedule a maintenance window to replace the faulty DIMM.

Sometimes, a message in the event logs indicates a bad memory module.
In these cases, you can schedule the memory replacement before the server is rebooted.
// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-bmn-maintenance.adoc

[id="troubleshooting-bmn-replace-disk_{context}"]
= Disk replacement

[role="_abstract"]
If you do not have disk redundancy configured on your node through hardware or software redundant array of independent disks (RAID), you need to check the following:

* Does the disk contain running pod images?
* Does the disk contain persistent data for pods?

For more information, see "OpenShift Container Platform storage overview" in _Storage_.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform storage overview

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-bmn-maintenance.adoc

[id="troubleshooting-bmn-replace-nw-card_{context}"]
= Cluster network card replacement

[role="_abstract"]
When you replace a network card, the MAC address changes.
The MAC address can be part of the DHCP or SR-IOV Operator configuration, router configuration, firewall rules, or cloud-native application configuration.
Before you bring back a node online after replacing a network card, you must verify that these configurations are up-to-date.

[IMPORTANT]
====
If you do not have specific procedures for MAC address changes within the network, contact your network administrator or network hardware vendor.
====
