---
title: "Restoring to a previous cluster state"
type: reference
domain: openshift
slug: backup-and-restore-4-22-scenario-2-restoring-cluster-state
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/scenario-2-restoring-cluster-state
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Restoring to a previous cluster state

//NOTE TO CONTRIBUTORS:
//
//If you update any of the content in this assembly file, be sure to also make the same changes in the assemblies in the following directory: etcd/etcd-backup-restore/etcd-disaster-recovery.adoc.

[id="dr-restoring-cluster-state"]
= Restoring to a previous cluster state

To restore the cluster to a previous state, you must have previously backed up the `etcd` data by creating a snapshot. You will use this snapshot to restore the cluster state. For more information, see "Backing up etcd data".

// About restoring to a previous cluster state
// Module included in the following assemblies:
//
// * backup_and_recovery/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

[id="dr-scenario-2-restoring-cluster-state-about_{context}"]
= About restoring to an earlier cluster state

[role="_abstract"]
To restore the cluster to an earlier state, you must have already backed up the `etcd` data by creating a snapshot. You can use this snapshot to restore the cluster state. For more information, see "Backing up etcd data".

You can use an etcd backup to restore your cluster to an earlier state. This can be used to recover from the following situations:

* The cluster has lost the majority of control plane hosts (quorum loss).
* An administrator has deleted something critical and must restore to recover the cluster.

[WARNING]
====
Restoring to an earlier cluster state is a destructive and destablizing action to take on a running cluster. This should only be used as a last resort.

If you cannot retrieve data using the Kubernetes API server, then etcd is available and you should not restore using an etcd backup.
====

Restoring etcd effectively takes a cluster back in time and all clients will experience a conflicting, parallel history. This can impact the behavior of watching components like kubelets, Kubernetes controller managers, persistent volume controllers, and OpenShift Container Platform Operators, including the network Operator.

It can cause Operator churn when the content in etcd does not match the actual content on disk, causing Operators for the Kubernetes API server, Kubernetes controller manager, Kubernetes scheduler, and etcd to get stuck when files on disk conflict with content in etcd. This can require manual actions to resolve the issues.

In extreme cases, the cluster can lose track of persistent volumes, delete critical workloads that no longer exist, reimage machines, and rewrite CA bundles with expired certificates.

// Restoring to a previous cluster state for a single node
// Module included in the following assemblies:
//
// * disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

[id="dr-restoring-cluster-state-sno_{context}"]
= Restoring to an earlier cluster state for a single node

[role="_abstract"]
You can use a saved etcd backup to restore an earlier cluster state on a single node.

[IMPORTANT]
====
When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform .2 cluster must use an etcd backup that was taken from .2.
====

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation.
* You have SSH access to control plane hosts.
* A backup directory containing both the etcd snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.

.Procedure

. Use SSH to connect to the single node and copy the etcd backup to the `/home/core` directory by running the following command:
+
[source,terminal]
----
$ cp <etcd_backup_directory> /home/core
----

. To restore the cluster from an earlier backup, run the following command on the single node::
+
[source,terminal]
----
$ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd_backup_directory>
----

. Exit the SSH session.

. Monitor the recovery progress of the control plane by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
[NOTE]
====
It can take up to 15 minutes for the control plane to recover.
====

// Restoring to a previous cluster state
// Module included in the following assemblies:
//
// * disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

// Contributors: The documentation for this section changed drastically for 4.18+.

// Contributors: Some changes for the `etcd` restore procedure are only valid for 4.14+.
// In the 4.14+ documentation, OVN-K requires different steps because there is no centralized OVN
// control plane to be converted. For more information, see PR #64939.
// Do not cherry pick from "main" to "enterprise-4.12" or "enterprise-4.13" because the cherry pick
// procedure is different for these versions. Instead, open a separate PR for 4.13 and
// cherry pick to 4.12 or make the updates directly in 4.12.

[id="dr-scenario-2-restoring-cluster-state_{context}"]
= Restoring to an earlier cluster state for more than one node

[role="abstract"]
You can use a saved etcd backup to restore an earlier cluster state or restore a cluster that has lost the majority of control plane hosts.

For a Two-Node with Fencing (TNF) setup, a single surviving node can continue to operate in degraded mode. Use a saved etcd backup to restore an earlier cluster state if only one node is operational, or when both nodes have failed and you need to restart the cluster from a known safe state. In both cases, perform the restore procedure on a single node. The peer node automatically synchronizes its data with the restored node when it rejoins the cluster.

For a 3-node HA cluster, shut down etcd on the following number of hosts:

- For 3-node clusters: Shut down etcd on 2 hosts.
- For 4-node and 5-node clusters: Shut down etcd on 3 hosts.

Quorum requires a simple majority of nodes. The minimum number of nodes required for a quorum is as follows:

- For 3-node HA cluster: 2.
- For 4-node and 5-node HA clusters: 3.

If you start a new cluster from backup on your recovery host, the other etcd members might still form a quorum and continue service.

[NOTE]
====
If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in "Troubleshooting the control plane machine set" for an etcd recovery procedure. For OpenShift Container Platform on a single node, see "Restoring to an earlier cluster state for a single node".
====

[IMPORTANT]
====
When you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform .2 cluster must use an etcd backup that was taken from .2.
====

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role through a certificate-based `kubeconfig` file, like the one that was used during installation.
* A healthy control plane host to use as the recovery host.
* You have SSH access to control plane hosts.
* A backup directory containing both the `etcd` snapshot and the resources for the static pods, which were from the same backup. The file names in the directory must be in the following formats: `snapshot_<datetimestamp>.db` and `static_kuberesources_<datetimestamp>.tar.gz`.
* Nodes must be accessible or bootable.

[IMPORTANT]
====
For non-recovery control plane nodes, it is not required to establish SSH connectivity or to stop the static pods. You can delete and re-create other non-recovery, control plane machines, one by one.
====

.Procedure

. Select a control plane host to use as the recovery host. This is the host that you run the restore operation on.

. Establish SSH connectivity to each of the control plane nodes, including the recovery host.
+
`kube-apiserver` becomes inaccessible after the restore process starts, so you cannot access the control plane nodes. For this reason, it is recommended to establish SSH connectivity to each control plane host in a separate terminal.
+
[IMPORTANT]
====
If you do not complete this step, you cannot access the control plane hosts to complete the restore procedure, and you cannot recover your cluster from this state.
====

. Using SSH, connect to each control plane node and run the following command to disable etcd:
+
[source,terminal]
----
$ sudo -E /usr/local/bin/disable-etcd.sh
----

. Copy the etcd backup directory to the recovery control plane host.
+
This procedure assumes that you copied the `backup` directory containing the etcd snapshot and the resources for the static pods to the `/home/core/` directory of your recovery control plane host.

. Use SSH to connect to the recovery host. To restore the cluster from an earlier backup, run the following command:
+
[source,terminal]
----
$ sudo -E /usr/local/bin/cluster-restore.sh /home/core/<etcd-backup-directory>
----

. Exit the SSH session.

. When the API responds, to turn off the etcd Operator quorum guard, run the following command:

[IMPORTANT]
====
For a TNF setup, do not:

  * Change the etcd Operator quorum setting.

  * Turn the etcd Operator quorum off.

  * Turn the etcd Operator quorum on back.
====
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
----

. Monitor the recovery progress of the control plane by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
[NOTE]
====
It can take up to 15 minutes for the control plane to recover. Wait for the control plane to recover before using the next step.
====

. Enable the quorum guard by running the following command:
+
[source,terminal]
----
$ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
----

.Troubleshooting

If the etcd static pods do not roll out, you can manually force an etcd redeployment from the `cluster-etcd-operator` by running the following command:

[source,terminal]
----
$ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$(date --rfc-3339=ns )"'"}}' --type=merge
----

[role="_additional-resources"]
.Additional resources
* Recovering a degraded etcd Operator

// Module included in the following assemblies:
//
// * disaster_recovery/scenario-2-restoring-cluster-state.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * etcd/etcd-backup-restore/etcd-disaster-recovery.adoc

[id="dr-scenario-cluster-state-issues_{context}"]
= Issues and workarounds for restoring a persistent storage state

If your OpenShift Container Platform cluster uses persistent storage of any form, a state of the cluster is typically stored outside etcd. When you restore from an etcd backup, the status of the workloads in OpenShift Container Platform is also restored. However, if the etcd snapshot is old, the status might be invalid or outdated.

[IMPORTANT]
====
The contents of persistent volumes (PVs) are never part of the etcd snapshot. When you restore an OpenShift Container Platform cluster from an etcd snapshot, non-critical workloads might gain access to critical data, or vice-versa.
====

The following are some example scenarios that produce an out-of-date status:

* MySQL database is running in a pod backed up by a PV object. Restoring OpenShift Container Platform from an etcd snapshot does not bring back the volume on the storage provider, and does not produce a running MySQL pod, despite the pod repeatedly attempting to start. You must manually restore this pod by restoring the volume on the storage provider, and then editing the PV to point to the new volume.

* Pod P1 is using volume A, which is attached to node X. If the etcd snapshot is taken while another pod uses the same volume on node Y, then when the etcd restore is performed, pod P1 might not be able to start correctly due to the volume still being attached to node Y. OpenShift Container Platform is not aware of the attachment, and does not automatically detach it. When this occurs, the volume must be manually detached from node Y so that the volume can attach on node X, and then pod P1 can start.

* Cloud provider or storage provider credentials were updated after the etcd snapshot was taken. This causes any CSI drivers or Operators that depend on the those credentials to not work. You might have to manually update the credentials required by those drivers or Operators.

* A device is removed or renamed from OpenShift Container Platform nodes after the etcd snapshot is taken. The Local Storage Operator creates symlinks for each PV that it manages from `/dev/disk/by-id` or `/dev` directories. This situation might cause the local PVs to refer to devices that no longer exist.
+
To fix this problem, an administrator must:

. Manually remove the PVs with invalid devices.
. Remove symlinks from respective nodes.
. Delete `LocalVolume` or `LocalVolumeSet` objects (see _Storage_ -> _Configuring persistent storage_ -> _Persistent storage using local volumes_ -> _Deleting the Local Storage Operator Resources_).
