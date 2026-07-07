---
title: "Troubleshooting CRI-O container runtime issues"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-crio-issues
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-crio-issues
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting CRI-O container runtime issues

[id="troubleshooting-crio-issues"]
= Troubleshooting CRI-O container runtime issues

[role="_abstract"]
Use the following sections to troubleshoot CRI-O container runtime issues.

// About CRI-O container runtime engine
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues.adoc

[id="about-crio_{context}"]
= About CRI-O container runtime engine

[role="_abstract"]
When container runtime issues occur, verify the status of the `crio` systemd service on each node. Gather CRI-O journald unit logs from nodes that have container runtime issues.

// Verifying CRI-O runtime engine status
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues.adoc

[id="verifying-crio-status_{context}"]
= Verifying CRI-O runtime engine status

[role="_abstract"]
You can verify CRI-O container runtime engine status on each cluster node.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Review CRI-O status by querying the `crio` systemd service on a node, within a debug pod.
.. Start a debug pod for a node:
+
[source,terminal]
----
$ oc debug node/my-node
----
+
.. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====
+
.. Check whether the `crio` systemd service is active on the node:
+
[source,terminal]
----
# systemctl is-active crio
----
+
.. Output a more detailed `crio.service` status summary:
+
[source,terminal]
----
# systemctl status crio.service
----

// Prevented from accessing Red Hat managed resources
// Gathering CRI-O journald unit logs
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues.adoc

[id="gathering-crio-logs_{context}"]
= Gathering CRI-O journald unit logs

[role="_abstract"]
If you experience CRI-O issues, you can obtain CRI-O journald unit logs from a node.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).
* You have the fully qualified domain names of the control plane or control plane machines.

.Procedure

. Gather CRI-O journald unit logs. The following example collects logs from all control plane nodes (within the cluster:
+
[source,terminal]
----
$ oc adm node-logs --role=master -u crio
----

. Gather CRI-O journald unit logs from a specific node:
+
[source,terminal]
----
$ oc adm node-logs <node_name> -u crio
----

. If the API is not functional, review the logs using SSH instead. Replace `<node>.<cluster_name>.<base_domain>` with appropriate values:
+
[source,terminal]
----
$ ssh core@<node>.<cluster_name>.<base_domain> journalctl -b -f -u crio.service
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.
====

// Cleaning CRI-O storage
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues

[id="cleaning-crio-storage_{context}"]

= Cleaning CRI-O storage

[role="_abstract"]
You can manually clear the CRI-O ephemeral storage if you experience the following issues:

* A node cannot run any pods and this error appears:
[source,terminal]
+
----
Failed to create pod sandbox: rpc error: code = Unknown desc = failed to mount container XXX: error recreating the missing symlinks: error reading name of symlink for XXX: open /var/lib/containers/storage/overlay/XXX/source,terminal
+
----
can't stat lower layer ...  because it does not exist.  Going through storage to recreate the missing symlinks.
----
+
* Your node is in the `NotReady` state after a cluster upgrade or if you attempt to reboot it.

* The container runtime implementation (`crio`) is not working properly.

* You are unable to start a debug shell on the node using `oc debug node/<node_name>` because the container runtime instance (`crio`) is not working.

Follow this process to completely wipe the CRI-O storage and resolve the errors.

.Prerequisites

  * You have access to the cluster as a user with the `cluster-admin` role.
  * You have installed the OpenShift CLI (`oc`).

.Procedure

. Use `cordon` on the node. This is to avoid any workload getting scheduled if the node gets into the `Ready` status. You will know that scheduling is disabled when `SchedulingDisabled` is in your Status section:
[source,terminal]
+
----
$ oc adm cordon <node_name>
----
+
. Drain the node as the cluster-admin user:
[source,terminal]
+
----
$ oc adm drain <node_name> --ignore-daemonsets --delete-emptydir-data
----
+
[NOTE]
====
The `terminationGracePeriodSeconds` attribute of a pod or pod template controls the graceful termination period. This attribute defaults at 30 seconds, but can be customized for each application as necessary. If set to more than 90 seconds, the pod might be marked as `SIGKILLed` and fail to terminate successfully.
====

. When the node returns, connect back to the node via SSH or Console. Then connect to the root user:
[source,terminal]
+
----
$ ssh core@node1.example.com
$ sudo -i
----
+
. Manually stop the kubelet:
[source,terminal]
+
----
# systemctl stop kubelet
----
+
. Stop the containers and pods:

.. Use the following command to stop the pods that are not in the `HostNetwork`. They must be removed first because their removal relies on the networking plugin pods, which are in the `HostNetwork`.
[source,terminal]
+
----
.. for pod in $(crictl pods -q); do if [[ "$(crictl inspectp $pod | jq -r .status.linux.namespaces.options.network)" != "NODE" ]]; then crictl rmp -f $pod; fi; done
----

.. Stop all other pods:
[source,terminal]
+
----
# crictl rmp -fa
----
+
. Manually stop the crio services:
[source,terminal]
+
----
# systemctl stop crio
----
+
. After you run those commands, you can completely wipe the ephemeral storage:
[source,terminal]
+
----
# crio wipe -f
----
+
. Start the crio and kubelet service:
[source,terminal]
+
----
# systemctl start crio
# systemctl start kubelet
----
+
. You will know if the clean up worked if the crio and kubelet services are started, and the node is in the `Ready` status:
[source,terminal]
+
----
$ oc get nodes
----
+
.Example output
[source,terminal]
+
----
NAME				    STATUS	                ROLES    AGE    VERSION
ci-ln-tkbxyft-f76d1-nvwhr-master-1  Ready, SchedulingDisabled   master	 133m   v1.35.4
----
+
. Mark the node schedulable. You will know that the scheduling is enabled when `SchedulingDisabled` is no longer in status:
[source,terminal]
+
----
$ oc adm uncordon <node_name>
----
+
.Example output
[source,terminal]
+
----
NAME				     STATUS	      ROLES    AGE    VERSION
ci-ln-tkbxyft-f76d1-nvwhr-master-1   Ready            master   133m   v1.35.4
----
