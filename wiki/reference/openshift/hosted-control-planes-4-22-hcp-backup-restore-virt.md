---
title: "Backing up and restoring a hosted cluster on {VirtProductName}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-backup-restore-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-backup-restore-virt
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Backing up and restoring a hosted cluster on {VirtProductName}

[id="hcp-backup-restore-virt"]
= Backing up and restoring a hosted cluster on {VirtProductName}

You can back up and restore a hosted cluster on {VirtProductName} to fix failures.

// Module included in the following assembly:
//
// * hosted_control_planes/hcp_high_availability/hcp-backup-restore-virt.adoc

[id="backup-hosted-cluster-virt_{context}"]
= Backing up a hosted cluster on {VirtProductName}

[role="_abstract"]
When you back up a hosted cluster on {VirtProductName}, the hosted cluster can remain running. The backup contains the hosted control plane components and the etcd for the hosted cluster.

When the hosted cluster is not running compute nodes on external infrastructure, hosted cluster workload data that is stored in persistent volume claims (PVCs) that are provisioned by KubeVirt CSI are also backed up. The backup does not contain any KubeVirt virtual machines (VMs) that are used as compute nodes. Those VMs are automatically re-created after the restore process is completed.

.Procedure

. Create a Velero backup resource by creating a YAML file that is similar to the following example:
+
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: hc-clusters-hosted-backup
  namespace: openshift-adp
  labels:
    velero.io/storage-location: default
spec:
  includedNamespaces:
  - clusters
  - clusters-hosted
  includedResources:
  - sa
  - role
  - rolebinding
  - deployment
  - statefulset
  - pv
  - pvc
  - bmh
  - configmap
  - infraenv
  - priorityclasses
  - pdb
  - hostedcluster
  - nodepool
  - secrets
  - hostedcontrolplane
  - cluster
  - datavolume
  - service
  - route
  excludedResources: [ ]
  labelSelector:
    matchExpressions:
    - key: 'hypershift.openshift.io/is-kubevirt-rhcos'
      operator: 'DoesNotExist'
  storageLocation: default
  preserveNodePorts: true
  ttl: 4h0m0s
  snapshotMoveData: true
  datamover: "velero"
  defaultVolumesToFsBackup: false
----
+
where:
+
`includedNamespaces`:: Specifies the namespaces from the objects to back up. Include namespaces from both the hosted cluster and the hosted control plane. In this example, `clusters` is a namespace from the hosted cluster and `clusters-hosted` is a namespace from the hosted control plane.
+
[IMPORTANT]
====
If you store all hosted cluster information in a shared namespace and then back up and restore a hosted cluster, you might unintentionally change other hosted clusters. To avoid this issue, do not store all hosted cluster information in a shared namespace. Alternatively, you can back up and restore resources based on labels.
====
+
`labelSelector`:: Specifies the boot image of the VMs that are used as the hosted cluster nodes are stored in large PVCs. To reduce backup time and storage size, you can filter those PVCs out of the backup by adding this label selector.
`snapshotMoveData`:: Along with the `datamover` field, specifies that the CSI `VolumeSnapshots` are automatically uploaded to remote cloud storage.
`datamover`:: Along with the `snapshotMoveData` field, specifies that the CSI `VolumeSnapshots` are automatically uploaded to remote cloud storage.
`defaultVolumesToFsBackup`:: Specifies whether pod volume file system backup is used for all volumes by default. Set this value to `false` to back up the PVCs that you want.

. Apply the changes to the YAML file by entering the following command:
+
[source,terminal]
----
$ oc apply -f <backup_file_name>.yaml
----
+
Replace `<backup_file_name>` with the name of your file.

. Monitor the backup process in the backup object status and in the Velero logs.
+
** To monitor the backup object status, enter the following command:
+
[source,terminal]
----
$ watch "oc get backups.velero.io -n openshift-adp <backup_file_name> -o jsonpath='{.status}' | jq"
----
+
** To monitor the Velero logs, enter the following command:
+
[source,terminal]
----
$ oc logs -n openshift-adp -ldeploy=velero -f
----

.Verification

* When the `status.phase` field is `Completed`, the backup process is considered complete.

// Module included in the following assembly:
//
// * hosted_control_planes/hcp_high_availability/hcp-backup-restore-virt.adoc

[id="restore-hosted-cluster-virt_{context}"]
= Restoring a hosted cluster on {VirtProductName}

After you back up a hosted cluster on {VirtProductName}, you can restore the backup.

[NOTE]
====
The restore process can be completed only on the same management cluster where you created the backup.
====

.Procedure

. Ensure that no pods or persistent volume claims (PVCs) are running in the `HostedControlPlane` namespace.

. Delete the following objects from the management cluster:

** `HostedCluster`
** `NodePool`
** PVCs

. Create a restoration manifest YAML file that is similar to the following example:
+
[source,yaml]
----
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: hc-clusters-hosted-restore
  namespace: openshift-adp
spec:
  backupName: hc-clusters-hosted-backup
  restorePVs: true <1>
  existingResourcePolicy: update <2>
  excludedResources:
  - nodes
  - events
  - events.events.k8s.io
  - backups.velero.io
  - restores.velero.io
  - resticrepositories.velero.io
----
+
<1> This field starts the recovery of pods with the included persistent volumes.
<2> Setting `existingResourcePolicy` to `update` ensures that any existing objects are overwritten with backup content. This action can cause issues with objects that contain immutable fields, which is why you deleted the `HostedCluster`, node pools, and PVCs. If you do not set this policy, the Velero engine skips the restoration of objects that already exist.

. Apply the changes to the YAML file by entering the following command:
+
[source,terminal]
----
$ oc apply -f <restore_resource_file_name>.yaml
----
+
Replace `<restore_resource_file_name>` with the name of your file.

. Monitor the restore process by checking the restore status field and the Velero logs.
+
** To check the restore status field, enter the following command:
+
[source,terminal]
----
$ watch "oc get restores.velero.io -n openshift-adp <backup_file_name> -o jsonpath='{.status}' | jq"
----
+
** To check the Velero logs, enter the following command:
+
[source,terminal]
----
$ oc logs -n openshift-adp -ldeploy=velero -f
----

.Verification

* When the `status.phase` field is `Completed`, the restore process is considered complete.

.Next steps

* After some time, the KubeVirt VMs are created and join the hosted cluster as compute nodes. Make sure that the hosted cluster workloads are running again as expected.
