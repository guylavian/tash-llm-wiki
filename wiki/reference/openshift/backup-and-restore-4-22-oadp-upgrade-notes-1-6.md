---
title: "Upgrading {oadp-short} 1.5 to 1.6"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-upgrade-notes-1-6
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-upgrade-notes-1-6
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Upgrading {oadp-short} 1.5 to 1.6

[id="oadp-upgrade-notes-1-6"]
= Upgrading {oadp-short} 1.5 to 1.6

[role="_abstract"]
Learn how to upgrade your existing {oadp-full} 1.5 installation to {oadp-short} 1.6.

[NOTE]
====
Always upgrade to the next minor version. Do not skip versions. To update to a later version, upgrade only one channel at a time. For example, to upgrade from {oadp-short} 1.1 to 1.3, upgrade first to 1.2, and then to 1.3.
====

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/release-notes/oadp-upgrade-notes-1-6.adoc

[id="changes-from-oadp-1-5-to-1-6_{context}"]
= Changes from {oadp-short} 1.5 to 1.6

[role="_abstract"]
The Velero server has been updated from version 1.16 to 1.18.

This brings the following changes:

Parallel backup processing::
{oadp-short} supports parallel backup processing. Before this update, {oadp-short} processed backups sequentially where each backup had to complete before the next one could begin. This created bottlenecks for environments with many backup schedules or large-scale data protection needs, increasing the overall time required to complete all backup operations. With this release, multiple backups can run in parallel if they do not share namespaces. As a result, you can now define more granular or frequent backup schedules without worrying about queuing delays.

File-level restore with VMFR from KubeVirt virtual machine backups::
{oadp-short} introduces the virtual machine file restore (VMFR) feature. Before this release, restoring even a single file from a KubeVirt VM backup required restoring the entire VM, which was time-consuming and resource-intensive. With this release, you can selectively recover individual files from KubeVirt VM backups directly within OpenShift Container Platform. VMFR also includes `RestoreItemAction`, a plugin for collision prevention in multi-backup scenarios. This plugin renames PVCs during restore, ensuring unique names and avoiding conflicts, thereby improving the reliability and efficiency of VMFR backups and restores.

File-level backups with VMDP in OpenShift Virtualization environments::
{oadp-short} introduces the virtual machine data protection (VMDP) feature, a command-line tool that runs inside virtual machines (VMs). Before this update, {oadp-short} supported only snapshot-based backup of entire VMs, with no option for granular, user-driven file-level data protection from within a VM. Using VMDP, you can selectively back up and restore individual files and directories by using a Kopia-based client/server architecture without cluster administrator intervention.

{oadp-short} CLI plugin::
{oadp-short} includes a `kubectl` command-line interface (CLI) plugin that provides a `kubectl` native interface for managing backups and restores. Before this update, you aliased to the Velero CLI to perform backup operations. Non-cluster administrators had no way to independently manage their own backups, creating a dependency on cluster admins for routine data protection tasks. As a result, admins can run `kubectl oadp` commands to create, delete, and retrieve logs for backups and restores. Non-cluster admins can independently create, delete, and inspect non-admin backups within their permitted namespaces.

Configurable priority class for node agent and Velero pods::
With this update, you can configure the `priorityClassName` field for node agent and Velero pods in a `DataProtectionApplication` object, prioritizing these pods during resource contention. This is particularly useful after worker node outages, ensuring critical pods are scheduled first.

Wildcard support for namespace selection during backup operations::
You can use wildcard patterns when specifying namespaces in backup operations. Before this update, you had to explicitly list every namespace in the backup object and update it each time a new namespace was created. With this release, you can use patterns such as `*-helm` in the `--include-namespaces` flag to dynamically match multiple namespaces, simplifying backup management and reducing manual configuration overhead.

`VolumeSnapshotClass` no longer required for CSI backup and restore::
The Container Storage Interface (CSI) backup and restore process no longer includes or requires the `VolumeSnapshotClass` resource. Before this update, the `VolumeSnapshotClass` was included in CSI backups and needed to be present during restore, adding an unnecessary dependency. With this update, CSI snapshot-based backups and restores complete successfully without `VolumeSnapshotClass` in the cluster, simplifying the backup resource footprint and improving restore reliability in environments where the `VolumeSnapshotClass` might not be pre-configured.

Optimized Data Mover performance in containerized environments with new Go version::
With the migration to Go 1.25, the Data Mover defaults the `MaxParallelFileReads` value to the `cgroup` CPU bandwidth limit corresponding to the container CPU limit rather than the total number of CPU cores on the node. Before this update, `MaxParallelFileReads` used the full CPU count of the node unless `datamoverConfig.ParallelFilesUpload` was explicitly set in the node-agent-config map, which could lead to overuse of resources in constrained container environments. With this update, Data Mover operations automatically respect container CPU limits, improving resource efficiency and stability without requiring manual configuration changes.

Changing PVC selected-node is removed::
The Changing PVC selected-node feature, which allowed overriding the `volume.kubernetes.io/selected-node` annotation to change the node selected for a persistent volume claim (PVC) during restore, is removed and is no longer supported. You can ensure PVCs are scheduled to the correct node by using the native Kubernetes `WaitForFirstConsumer` volume binding mode instead.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/release-notes/oadp-upgrade-notes-1-6.adoc

[id="oadp-backing-up-dpa-configuration-1-6-0_{context}"]
= Backing up the DPA configuration

[role="_abstract"]
You must back up your current `DataProtectionApplication` (DPA) configuration.

.Procedure

* Save your current DPA configuration by running the following command:
+
.Example command
[source,terminal]
----
$ oc get dpa -n openshift-adp -o yaml > dpa.orig.backup
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/release-notes/oadp-upgrade-notes-1-6.adoc

[id="oadp-upgrading-dpa-operator-1-6-0_{context}"]
= Upgrading the {oadp-short} Operator

[role="_abstract"]
You can upgrade the {oadp-first} Operator by using the following procedure.

[NOTE]
====
Do not install {oadp-short} 1.6.0 on a {OCP-short} 4.21 cluster.
====

.Prerequisites

* You have installed the latest {oadp-short} {oadp-version-1-5}.
* You have backed up your data.

.Procedure

. Upgrade {OCP-short} 4.21 to {OCP-short} 4.22.
. Ensure your subscription channel for the {oadp-short} Operator is `stable`.
. Wait for the Operator and containers to update and restart.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/release-notes/oadp-upgrade-notes-1-6.adoc

[id="converting-dpa-to-the-new-version-for-oadp-1-6-0_{context}"]
= Converting DPA to the new version for {oadp-short} 1.6.0

[role="_abstract"]
{oadp-first} 1.5 is not supported on {OCP-short} 4.22. You can convert {oadp-short} to the new 1.6 version by using the new `spec.configuration.nodeAgent` field and its sub-fields.

.Procedure

. To configure `nodeAgent` daemon set, use the `spec.configuration.nodeAgent` parameter in DPA. See the following example:
+
.Example `DataProtectionApplication` configuration
[source,yaml]
----
...
 spec:
   configuration:
     nodeAgent:
       enable: true
       uploaderType: kopia
...
----

. To configure `nodeAgent` daemon set by using the `ConfigMap` resource named `node-agent-config`, see the following example configuration:
+
.Example config map
[source,yaml]
----
...
 spec:
   configuration:
     nodeAgent:
       backupPVC:
         ...
       loadConcurrency:
         ...
       podResources:
         ...
       restorePVC:
        ...
...
----

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/release-notes/oadp-upgrade-notes-1-6.adoc

[id="verifying-upgrade-1-6-0_{context}"]
= Verifying the upgrade

[role="_abstract"]
You can verify the {oadp-first} upgrade by using the following procedure.

.Procedure

. Verify that the `DataProtectionApplication` (DPA) has been reconciled successfully:
+
[source,terminal]
----
$ oc get dpa dpa-sample -n openshift-adp
----
+
.Example output
[source,terminal]
----
NAME            RECONCILED   AGE
dpa-sample      True         2m51s
----
+
[NOTE]
====
The `RECONCILED` column must be `True`.
====

. Verify that the installation finished by viewing the {oadp-short} resources by running the following command:
+
[source,terminal]
----
$ oc get all -n openshift-adp
----
+
.Example output
[source,terminal]
----
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/node-agent-9pjz9                                    1/1     Running   0          3d17h
pod/node-agent-fmn84                                    1/1     Running   0          3d17h
pod/node-agent-xw2dg                                    1/1     Running   0          3d17h
pod/openshift-adp-controller-manager-76b8bc8d7b-kgkcw   1/1     Running   0          3d17h
pod/velero-64475b8c5b-nh2qc                             1/1     Running   0          3d17h

NAME                                                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/openshift-adp-controller-manager-metrics-service   ClusterIP   172.30.194.192   <none>        8443/TCP   3d17h
service/openshift-adp-velero-metrics-svc                   ClusterIP   172.30.190.174   <none>        8085/TCP   3d17h

NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/node-agent   3         3         3       3            3           <none>          3d17h

NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/openshift-adp-controller-manager   1/1     1            1           3d17h
deployment.apps/velero                             1/1     1            1           3d17h

NAME                                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/openshift-adp-controller-manager-76b8bc8d7b   1         1         1       3d17h
replicaset.apps/openshift-adp-controller-manager-85fff975b8   0         0         0       3d17h
replicaset.apps/velero-64475b8c5b                             1         1         1       3d17h
replicaset.apps/velero-8b5bc54fd                              0         0         0       3d17h
replicaset.apps/velero-f5c9ffb66                              0         0         0       3d17h
----

. Verify the backup storage location and confirm that the `PHASE` is `Available` by running the following command:
+
[source,terminal]
----
$ oc get backupstoragelocations.velero.io -n openshift-adp
----
+
.Example output
[source,terminal]
----
NAME           PHASE       LAST VALIDATED   AGE     DEFAULT
dpa-sample-1   Available   1s               3d16h   true
----
