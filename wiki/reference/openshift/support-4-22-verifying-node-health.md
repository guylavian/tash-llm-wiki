---
title: "Verifying node health"
type: reference
domain: openshift
slug: support-4-22-verifying-node-health
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/verifying-node-health
version: 4.22
family: support
documentKind: "Documentation"
---

# Verifying node health

[id="verifying-node-health"]
= Verifying node health

[role="_abstract"]
You can verify and troubleshoot node-related issues by reviewing the status, resource usage, and configuration of a node.

// Reviewing node status, resource usage, and configuration
// Module included in the following assemblies:
//
// * support/troubleshooting/verifying-node-health.adoc

[id="reviewing-node-status-use-and-configuration_{context}"]
= Reviewing node status, resource usage, and configuration

[role="_abstract"]
Review cluster node health status, resource consumption statistics, and node logs. Additionally, query `kubelet` status on individual nodes.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

* List the name, status, and role for all nodes in the cluster:
+
[source,terminal]
----
$ oc get nodes
----

* Summarize CPU and memory usage for each node within the cluster:
+
[source,terminal]
----
$ oc adm top nodes
----

* Summarize CPU and memory usage for a specific node:
+
[source,terminal]
----
$ oc adm top node my-node
----

// cannot create resource "namespaces"
// Querying the kubelet's status on a node
// Module included in the following assemblies:
//
// * support/troubleshooting/verifying-node-health.adoc

[id="querying-kubelet-status-on-a-node_{context}"]
= Querying the kubelet's status on a node

[role="_abstract"]
You can review cluster node health status, resource consumption statistics, and node logs. Additionally, you can query `kubelet` status on individual nodes.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. The kubelet is managed using a systemd service on each node. Review the kubelet's status by querying the `kubelet` systemd service within a debug pod.
.. Start a debug pod for a node:
+
[source,terminal]
----
$ oc debug node/my-node
----
+
[NOTE]
====
If you are running `oc debug` on a control plane node, you can find administrative `kubeconfig` files in the `/etc/kubernetes/static-pod-resources/kube-apiserver-certs/secrets/node-kubeconfigs` directory.
====
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
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or `kubelet` is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====
+
.. Check whether the `kubelet` systemd service is active on the node:
+
[source,terminal]
----
# systemctl is-active kubelet
----
+
.. Output a more detailed `kubelet.service` status summary:
+
[source,terminal]
----
# systemctl status kubelet
----

// cannot get resource "nodes/proxy"
// Querying node journal logs
// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc
// * support/troubleshooting/verifying-node-health.adoc

[id="querying-cluster-node-journal-logs_{context}"]
= Querying cluster node journal logs

[role="_abstract"]
You can gather `journald` unit logs and other logs within `/var/log` on individual cluster nodes.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
+
[NOTE]
====
In OpenShift Container Platform deployments, customers who are not using the Customer Cloud Subscription (CCS) model cannot use the `oc adm node-logs` command as it requires `cluster-admin` privileges.
====
+
* You have installed the OpenShift CLI (`oc`).
* Your API service is still functional.
* You have SSH access to your hosts.

.Procedure

. Query `kubelet` `journald` unit logs from OpenShift Container Platform cluster nodes. The following example queries control plane nodes only:
* Query `kubelet` `journald` unit logs from OpenShift Container Platform cluster nodes. The following example queries worker nodes only:
+
[source,terminal]
----
$ oc adm node-logs --role=master -u kubelet  <1>
----
[source,terminal]
----
$ oc adm node-logs --role=worker -u kubelet
----
`kubelet`:: Replace as appropriate to query other unit logs.

. Collect logs from specific subdirectories under `/var/log/` on cluster nodes.
+
.. Retrieve a list of logs contained within a `/var/log/` subdirectory. The following example lists files in `/var/log/openshift-apiserver/` on all control plane nodes:
+
[source,terminal]
----
$ oc adm node-logs --role=master --path=openshift-apiserver
----
+
.. Inspect a specific log within a `/var/log/` subdirectory. The following example outputs `/var/log/openshift-apiserver/audit.log` contents from all control plane nodes:
+
[source,terminal]
----
$ oc adm node-logs --role=master --path=openshift-apiserver/audit.log
----
+
.. If the API is not functional, review the logs on each node using SSH instead. The following example tails `/var/log/openshift-apiserver/audit.log`:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo tail -f /var/log/openshift-apiserver/audit.log
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.
====
