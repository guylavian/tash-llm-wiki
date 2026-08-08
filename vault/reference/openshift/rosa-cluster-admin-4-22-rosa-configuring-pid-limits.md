---
title: "Configuring PID limits"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-configuring-pid-limits
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-configuring-pid-limits
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Configuring PID limits

[id="rosa-configuring-pid-limits"]
= Configuring PID limits

[role="_abstract"]
A process identifier (PID) is a unique identifier assigned by the Linux kernel to each process or thread currently running on a system. The number of processes that can run simultaneously on a system is limited to 4,194,304 by the Linux kernel. This number might also be affected by limited access to other system resources such as memory, CPU, and disk space.

In OpenShift Container Platform 4.11 and later, by default, a pod can have a maximum of 4,096 PIDs. If your workload requires more than that, you can increase the allowed maximum number of PIDs by configuring a `KubeletConfig` object.

OpenShift Container Platform clusters running versions earlier than 4.11 use a default PID limit of `1024`.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc
// * nodes/nodes-nodes-resources-configuring.adoc

[id="understanding-process-id-limits_{context}"]
= Understanding process ID limits

[role="_abstract"]
You can review the following information to learn how to limit the number of processes running on your nodes. Configuring an appropriate number of processes can help keep the nodes in your cluster running efficiently.

A process identifier (PID) is a unique identifier assigned by the Linux kernel to each process or thread currently running on a system. The number of processes that can run simultaneously on a system is limited to 4,194,304 by the Linux kernel. This number might also be affected by limited access to other system resources such as memory, CPU, and disk space.

In OpenShift Container Platform, consider these two supported limits for process ID (PID) usage before you schedule work on your cluster:

* Maximum number of PIDs per pod.
+
The default value is 4,096 in OpenShift Container Platform 4.11 and later. This value is controlled by the `podPidsLimit` parameter set on the node.
+
You can view the current PID limit on a node by running the following command in a `chroot` environment:
+
[source,terminal]
----
sh-5.1# cat /etc/kubernetes/kubelet.conf | grep -i pids
----
+
.Example output
[source,terminal]
----
"podPidsLimit": 4096,
----
+
You can change the `podPidsLimit` by using a `KubeletConfig` object. See "Creating a KubeletConfig CR to edit kubelet parameters".
+
Containers inherit the `podPidsLimit` value from the parent pod, so the kernel enforces the lower of the two limits. For example, if the container PID limit is set to the maximum, but the pod PID limit is `4096`, the PID limit of each container in the pod is confined to 4096.

* Maximum number of PIDs per node.
+
The default value depends on node resources. In OpenShift Container Platform, this value is controlled by the `systemReserved` parameter in a kubelet configuration, which reserves PIDs on each node based on the total resources of the node. For more information, see "Allocating resources for nodes in an OpenShift Container Platform cluster".
* Maximum number of PIDs per node.
+
The default value depends on node resources. In OpenShift Container Platform, this value is controlled by the `--system-reserved` parameter, which reserves PIDs on each node based on the total resources of the node.

When a pod exceeds the allowed maximum number of PIDs per pod, the pod might stop functioning correctly and might be evicted from the node. See the Kubernetes documentation for eviction signals and thresholds for more information.

When a node exceeds the allowed maximum number of PIDs per node, the node can become unstable because new processes cannot have PIDs assigned. If existing processes cannot complete without creating additional processes, the entire node can become unusable and require reboot. This situation can result in data loss, depending on the processes and applications being run. Customer administrators and Red{nbsp}Hat Site Reliability Engineering are notified when this threshold is reached, and a `Worker node is experiencing PIDPressure` warning will appear in the cluster logs.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc
// * nodes/nodes-nodes-resources-configuring.adoc

[id="risks-setting-higher-process-id-limits_{context}"]
= Risks of setting higher process ID limits for OpenShift Container Platform pods

[role="_abstract"]
You can review the following information to learn about some considerations about allowing a high maximum number of processes to run on your nodes. Configuring an appropriate number of processes can help keep the nodes in your cluster running efficiently.

You can increase the value for `podPidsLimit` from the default of 4,096 to a maximum of 16,384. Changing this value might incur downtime for applications, because changing the `podPidsLimit` requires rebooting the affected node.

If you are running a large number of pods per node, and you have a high `podPidsLimit` value on your nodes, you risk exceeding the PID maximum for the node.

To find the maximum number of pods that you can run simultaneously on a single node without exceeding the PID maximum for the node, divide 3,650,000 by your `podPidsLimit` value. For example, if your `podPidsLimit` value is 16,384, and you expect the pods to use close to that number of process IDs, you can safely run 222 pods on a single node.

[NOTE]
====
Memory, CPU, and available storage can also limit the maximum number of pods that can run simultaneously, even when the `podPidsLimit` value is set appropriately.
====
[NOTE]
====
Memory, CPU, and available storage can also limit the maximum number of pods that can run simultaneously, even when the `podPidsLimit` value is set appropriately. For more information, see "Planning your environment" and "Limits and scalability".
====

[role="_additional-resources"]
.Additional resources

* Instance types

* Planning your environment

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc

[id="setting-higher-pid-limit-on-existing-cluster_{context}"]
= Setting a higher process ID limit on an existing OpenShift Container Platform cluster

You can set a higher `podPidsLimit` on an existing OpenShift Container Platform cluster by creating or editing a `KubeletConfig` object that changes the `--pod-pids-limit` parameter.

[IMPORTANT]
====
Changing the `podPidsLimit` on an existing cluster will trigger non-control plane nodes in the cluster to reboot one at a time. Make this change outside of peak usage hours for your cluster and avoid upgrading or hibernating your cluster until all nodes have rebooted.
====

.Prerequisites

* You have a OpenShift Container Platform cluster.
* You have installed the {rosa-cli-first}.
* You have installed the OpenShift CLI (`oc`).
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.

.Procedure
. Create or edit the `KubeletConfig` object to change the PID limit.
+
--
** If this is the first time you are changing the default PID limit, create the `KubeletConfig` object and set the `--pod-pids-limit` value by running the following command:
+
[source,terminal]
----
$ rosa create kubeletconfig -c <cluster_name> --name <kubeletconfig_name> --pod-pids-limit=<value>
----
+
NOTE: The `--name` parameter is optional on ROSA Classic clusters, because only one `KubeletConfig` object is supported per ROSA Classic cluster.
+
For example, the following command sets a maximum of 16,384 PIDs per pod for cluster `my-cluster`:
+
[source,terminal]
----
$ rosa create kubeletconfig -c my-cluster --name set-high-pids --pod-pids-limit=16384
----
** If you previously created a `KubeletConfig` object, edit the existing `KubeletConfig` object and set the `--pod-pids-limit` value by running the following command:
+
[source,terminal]
----
$ rosa edit kubeletconfig -c <cluster_name> --name <kubeletconfig_name> --pod-pids-limit=<value>
----
--
+
A cluster-wide rolling reboot of worker nodes is triggered.

. Verify that all of the worker nodes rebooted by running the following command:
+
[source,terminal]
----
$ oc get machineconfigpool
----
+
.Example output
[source,terminal]
----
NAME      CONFIG                    UPDATED  UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT  AGE
master    rendered-master-06c9c4…   True     False      False     3             3                  3                   0                     4h42m
worker    rendered-worker-f4b64…    True     False      False     4             4                  4                   0                     4h42m
----

.Verification

When each node in the cluster has rebooted, you can verify that the new setting is in place.

* Check the Pod Pids limit in the `KubeletConfig` object:
+
[source,terminal]
----
$ rosa describe kubeletconfig --cluster=<cluster_name>
----
+
The new PIDs limit appears in the output, as shown in the following example:
+
.Example output
[source,terminal]
----
Pod Pids Limit:                       16384
----
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc

[id="removing-custom-config-from-cluster_{context}"]
= Removing custom configuration from a cluster

You can remove custom configuration from your cluster by removing the `KubeletConfig` object that contains the configuration details.

.Prerequisites
* You have an existing OpenShift Container Platform cluster.
* You have installed the ROSA CLI (rosa).
* You have logged in to your Red Hat account by using the ROSA CLI.

.Procedure

* Remove custom configuration from the cluster by deleting the relevant custom `KubeletConfig` object:
+
[source,terminal]
----
$ rosa delete kubeletconfig --cluster <cluster_name> --name <kubeletconfig_name>
----

.Verification steps
* Confirm that the custom `KubeletConfig` object is not listed for the cluster:
+
[source,terminal]
----
$ rosa describe kubeletconfig --name <cluster_name>
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc

[id="setting-higher-pid-limit-on-machine-pool_{context}"]
= Setting a higher process ID limit on a machine pool in a OpenShift Container Platform cluster

You can set a higher `podPidsLimit` for machine pools in an existing OpenShift Container Platform cluster by creating or editing a `KubeletConfig` object that changes the `--pod-pids-limit` parameter.

[IMPORTANT]
====
Changing the `podPidsLimit` on an existing machine pool triggers nodes in the machine pool to reboot one at a time. Make this change outside of peak usage hours for workloads in your machine pool and avoid upgrading or hibernating your cluster until all nodes have rebooted.
====

.Prerequisites

* You have a OpenShift Container Platform cluster.
* You have installed the {rosa-cli-first}.
* You have logged in to your Red Hat account by using the {rosa-cli}.

.Procedure

. Create a new `KubeletConfig` object for your cluster that specifies a new `--pod-pids-limit`:
+
[source,terminal]
----
$ rosa create kubeletconfig -c <cluster_name> --name=<kubeletconfig_name> --pod-pids-limit=<value>
----
+
For example, the following command creates a `set-high-pids` `KubeletConfig` object for the `my-cluster` cluster that sets a maximum of 16,384 PIDs per pod:
+
[source,terminal]
----
$ rosa create kubeletconfig -c my-cluster --name=set-high-pids --pod-pids-limit=16384
----

. Associate the new `KubeletConfig` object with a new or existing machine pool.
+
--
** For a new machine pool:
+
[source,terminal]
----
$ rosa create machinepool -c <cluster_name> --name <machinepool_name> --kubelet-configs=<kubeletconfig_name>
----
** For an existing machine pool:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster_name> --kubelet-configs=<kubeletconfig_name> <machinepool_name>
----
+
.Example output
[source,terminal]
----
Editing the kubelet config will cause the Nodes for your Machine Pool to be recreated. This may cause outages to your applications. Do you wish to continue? (y/N)
----
--
+
For example, the following command associates the `set-high-pids` `KubeletConfig` object with the `high-pid-pool` machine pool in the `my-cluster` cluster:
+
[source,terminal]
----
$ rosa edit machinepool -c my-cluster --kubelet-configs=set-high-pids high-pid-pool
----
+
A rolling reboot of worker nodes is triggered when a new `KubeletConfig` object is attached to an existing machine pool. You can check the progress of the rollout in the machine pool description:
+
[source,terminal]
----
$ rosa describe machinepool --cluster <cluster_name> --machinepool <machinepool_name>
----

.Verification

* Confirm that the new setting is in place on nodes in the machine pool:
+
[source,terminal]
----
$ rosa describe kubeletconfig --cluster=<cluster_name> --name <kubeletconfig_name>
----
+
The new PIDs limit appears in the output, as shown in the following example:
+
.Example output
[source,terminal]
----
Pod Pids Limit:                       16384
----
// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-configuring-pid-limits.adoc

[id="removing-custom-config-from-machinepool_{context}"]
= Removing custom configuration from a machine pool

You can remove custom configuration on your machine pools by removing the `KubeletConfig` object that contains the configuration details.

.Prerequisites
* You have an existing OpenShift Container Platform cluster.
* You have installed the ROSA CLI (rosa).
* You have logged in to your Red Hat account by using the ROSA CLI.

.Procedure

* Edit the machine pool and set the `--kubeletconfigs` parameter so that the `KubeletConfig` object you want to remove is omitted.
+
To remove all `KubeletConfig` objects from the machine pool, set an empty value for the `--kubeletconfigs` parameter, for example:
+
[source,terminal]
----
$ rosa edit machinepool -c <cluster_name> --kubelet-configs="" <machinepool_name>
----

.Verification steps
* Confirm that the `KubeletConfig` object you removed is not visible in the machine pool description:
+
[source,terminal]
----
$ rosa describe machinepool --cluster <cluster_name> --machinepool=<machinepool_name>
----
