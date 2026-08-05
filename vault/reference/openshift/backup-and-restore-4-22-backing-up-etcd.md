---
title: "Backing up etcd"
type: reference
domain: openshift
slug: backup-and-restore-4-22-backing-up-etcd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/backing-up-etcd
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Backing up etcd

//NOTE TO CONTRIBUTORS:
//
//If you update any of the content in this assembly file, be sure to also make the same changes in the assemblies in the following file: backup_and_restore/control_plane_backup_and_restore/etcd-backup.adoc.

[id="backup-etcd"]
= Backing up etcd

etcd is the key-value store for OpenShift Container Platform, which persists the state of all resource objects.

Back up your cluster's etcd data regularly and store in a secure location ideally outside the OpenShift Container Platform environment. Do not take an etcd backup before the first certificate rotation completes, which occurs 24 hours after installation, otherwise the backup will contain expired certificates. It is also recommended to take etcd backups during non-peak usage hours because the etcd snapshot has a high I/O cost.

Be sure to take an etcd backup before you update your cluster. Taking a backup before you update is important because when you restore your cluster, you must use an etcd backup that was taken from the same z-stream release. For example, an OpenShift Container Platform 4.17.5 cluster must use an etcd backup that was taken from 4.17.5.

[IMPORTANT]
====
Back up your cluster's etcd data by performing a single invocation of the backup script on a control plane host. Do not take a backup for each control plane host.
====

After you have an etcd backup, you can restore to a previous cluster state.

// Backing up etcd data
// Module included in the following assemblies:
//
// * backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="backing-up-etcd-data_{context}"]
= Backing up etcd data

[role="_abstract"]
Follow these steps to back up etcd data by creating an etcd snapshot and backing up the resources for the static pods. This backup can be saved and used at a later time if you need to restore etcd.

[IMPORTANT]
====
Only save a backup from a single control plane host. Do not take a backup from each control plane host in the cluster.
====

For a Two-Node with Fencing (TNF) setup, follow the steps to back up etcd data on only one node in the cluster. The cluster restore process is driven by data from a single node, so you can perform the etcd backup steps on only one node.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have checked whether the cluster-wide proxy is enabled.
+
[TIP]
====
You can check whether the proxy is enabled by reviewing the output of `oc get proxy cluster -o yaml`. The proxy is enabled if the `httpProxy`, `httpsProxy`, and `noProxy` fields have values set.
====

.Procedure

. Start a debug session as root for a control plane node:
+
[source,terminal]
----
$ oc debug --as-root node/<node_name>
----

. Change your root directory to `/host` in the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. If the cluster-wide proxy is enabled, export the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` environment variables by running the following commands:
+
[source,terminal]
----
$ export HTTP_PROXY=http://<your_proxy.example.com>:8080
----
+
[source,terminal]
----
$ export HTTPS_PROXY=https://<your_proxy.example.com>:8080
----
+
[source,terminal]
----
$ export NO_PROXY=<example.com>
----
+

. Run the `cluster-backup.sh` script in the debug shell and pass in the location to save the backup to.
+
[TIP]
====
The `cluster-backup.sh` script is maintained as a component of the etcd Cluster Operator and is a wrapper around the `etcdctl snapshot save` command.
====
+
[source,terminal]
----
sh-4.4# /usr/local/bin/cluster-backup.sh /home/core/assets/backup
----
+
.Example script output
[source,terminal]
----
found latest kube-apiserver: /etc/kubernetes/static-pod-resources/kube-apiserver-pod-6
found latest kube-controller-manager: /etc/kubernetes/static-pod-resources/kube-controller-manager-pod-7
found latest kube-scheduler: /etc/kubernetes/static-pod-resources/kube-scheduler-pod-6
found latest etcd: /etc/kubernetes/static-pod-resources/etcd-pod-3
ede95fe6b88b87ba86a03c15e669fb4aa5bf0991c180d3c6895ce72eaade54a1
etcdctl version: 3.4.14
API version: 3.4
{"level":"info","ts":1624647639.0188997,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db.part"}
{"level":"info","ts":"2021-06-25T19:00:39.030Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":1624647639.0301006,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"https://10.0.0.5:2379"}
{"level":"info","ts":"2021-06-25T19:00:40.215Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
{"level":"info","ts":1624647640.6032252,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"https://10.0.0.5:2379","size":"114 MB","took":1.584090459}
{"level":"info","ts":1624647640.6047094,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"/home/core/assets/backup/snapshot_2021-06-25_190035.db"}
Snapshot saved at /home/core/assets/backup/snapshot_2021-06-25_190035.db
{"hash":3866667823,"revision":31407,"totalKey":12828,"totalSize":114446336}
snapshot db and kube resources are successfully saved to /home/core/assets/backup
----
+
In this example, two files are created in the `/home/core/assets/backup/` directory on the control plane host:

* `snapshot_<datetimestamp>.db`: This file is the etcd snapshot. The `cluster-backup.sh` script confirms its validity.
* `static_kuberesources_<datetimestamp>.tar.gz`: This file contains the resources for the static pods. If etcd encryption is enabled, it also contains the encryption keys for the etcd snapshot.
+
[NOTE]
====
If etcd encryption is enabled, store this second file separately from the etcd snapshot for security reasons. However, this file is required to restore from the etcd snapshot.

The etcd encryption only encrypts values, not keys. This means that resource types, namespaces, and object names are not encrypted.
====

// [role="_additional-resources"]
// [id="additional-resources_backup-etcd"]
// == Additional resources
// * Recovering an unhealthy etcd cluster

// Creating automated etcd backups
// Module included in the following assemblies:
//
// * backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc

[id="creating-automated-etcd-backups_{context}"]
= Creating automated etcd backups

The automated backup feature for etcd supports both recurring and single backups. Recurring backups create a cron job that starts a single backup each time the job triggers.

Follow these steps to enable automated backups for etcd.

[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster prevents minor version updates. The `TechPreviewNoUpgrade` feature set cannot be disabled. Do not enable this feature set on production clusters.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

.Procedure

. Create a `FeatureGate` custom resource (CR) file named `enable-tech-preview-no-upgrade.yaml` with the following contents:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster
spec:
  featureSet: TechPreviewNoUpgrade
----

. Apply the CR and enable automated backups:
+
[source,terminal]
----
$ oc apply -f enable-tech-preview-no-upgrade.yaml
----

. It takes time to enable the related APIs. Verify the creation of the custom resource definition (CRD) by running the following command:
+
[source,terminal]
----
$ oc get crd | grep backup
----
+
.Example output
[source,terminal]
----
backups.config.openshift.io 2023-10-25T13:32:43Z
etcdbackups.operator.openshift.io 2023-10-25T13:32:04Z
----

// Module included in the following assemblies:
//
// * backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.adoc
// * etcd/etcd-backup-restore/etcd-backup.adoc

[id="creating-single-etcd-backup_{context}"]
= Creating a single automated etcd backup

[role="_abstract"]
Follow these steps to create a single etcd backup by creating and applying a custom resource (CR).

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

.Procedure

* If dynamically-provisioned storage is available, complete the following steps to create a single automated etcd backup:
+
.. Create a persistent volume claim (PVC) named `etcd-backup-pvc.yaml` with contents such as the following example:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
  namespace: openshift-etcd
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: <storage_amount>
  volumeMode: Filesystem
----
+
where:
+
`<storage_amount>`:: Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `200Gi`.
+
.. Apply the PVC by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-pvc.yaml
----
+
.. Verify the creation of the PVC by running the following command:
+
[source,terminal]
----
$ oc get pvc
----
+
.Example output
[source,terminal]
----
NAME              STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
etcd-backup-pvc   Bound                                                       51s
----
+
[NOTE]
====
Dynamic PVCs stay in the `Pending` state until they are mounted.
====
+
.. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: EtcdBackup
metadata:
  name: etcd-single-backup
  namespace: openshift-etcd
spec:
  pvcName: <pvc_name>
----
+
where:
+
`<pvc_name>`:: Specifies the name of the PVC to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`.
+
.. Apply the CR to start a single backup:
+
[source,terminal]
----
$ oc apply -f etcd-single-backup.yaml
----

* If dynamically-provisioned storage is not available, complete the following steps to create a single automated etcd backup:
+
.. Create a `StorageClass` CR file named `etcd-backup-local-storage.yaml` with the following contents:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: etcd-backup-local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate
----
+
.. Apply the `StorageClass` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-local-storage.yaml
----
+
.. Create a PV named `etcd-backup-pv-fs.yaml` with contents such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: etcd-backup-pv-fs
spec:
  capacity:
    storage: <storage_amount>
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: etcd-backup-local-storage
  local:
    path: /mnt
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
      - key: kubernetes.io/hostname
         operator: In
         values:
         - <node_name>
----
+
where:
+
`<storage_amount>`:: Specifies the amount of storage available to the PV. Adjust this value for your requirements, such as `100Gi`.
`<node_name>`:: Specifies the node to attach this PV to. Replace with the actual node name, such as `master-0`.
+
.. Verify the creation of the PV by running the following command:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS                REASON   AGE
etcd-backup-pv-fs       100Gi      RWO            Retain           Available           etcd-backup-local-storage            10s
----
+
.. Create a PVC named `etcd-backup-pvc.yaml` with contents such as the following example:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
  namespace: openshift-etcd
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: <storage_amount>
----
+
where:
+
`<storage_amount>`:: Specifies the amount of storage available to the PVC. Adjust this value for your requirements, such as `10Gi`.
+
.. Apply the PVC by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-pvc.yaml
----
+
.. Create a CR file named `etcd-single-backup.yaml` with contents such as the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: EtcdBackup
metadata:
  name: etcd-single-backup
  namespace: openshift-etcd
spec:
  pvcName: <pvc_name>
----
+
where:
+
`<pvc_name>`:: Specifies the name of the persistent volume claim (PVC) to save the backup to. Adjust this value according to your environment, such as `etcd-backup-pvc`.
+
.. Apply the CR to start a single backup:
+
[source,terminal]
----
$ oc apply -f etcd-single-backup.yaml
----

//Module included in the following assemblies:
//
// * etcd/etcd-backup-restore/etcd-backup.adoc

[id="creating-recurring-etcd-backups_{context}"]
= Creating recurring automated etcd backups

Follow these steps to create automated recurring backups of etcd.

Use dynamically-provisioned storage to keep the created etcd backup data in a safe, external location if possible. If dynamically-provisioned storage is not available, consider storing the backup data on an NFS share to make backup recovery more accessible.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift CLI (`oc`).

.Procedure

. If dynamically-provisioned storage is available, complete the following steps to create automated recurring backups:

.. Create a persistent volume claim (PVC) named `etcd-backup-pvc.yaml` with contents such as the following example:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
  namespace: openshift-etcd
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 200Gi <1>
  volumeMode: Filesystem
  storageClassName: etcd-backup-local-storage
----
<1> The amount of storage available to the PVC. Adjust this value for your requirements.
+
[NOTE]
====
Each of the following providers require changes to the `accessModes` and `storageClassName` keys:

[cols="1,1,1"]
|===
|Provider|`accessModes` value|`storageClassName` value

|AWS with the `versioned-installer-efc_operator-ci` profile
|`- ReadWriteMany`
|`efs-sc`

|{gcp-full}
|`- ReadWriteMany`
|`filestore-csi`

|Microsoft Azure
|`- ReadWriteMany`
|`azurefile-csi`
|===
====

.. Apply the PVC by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-pvc.yaml
----

.. Verify the creation of the PVC by running the following command:
+
[source,terminal]
----
$ oc get pvc
----
+
.Example output
[source,terminal]
----
NAME              STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
etcd-backup-pvc   Bound                                                       51s
----
+
[NOTE]
====
Dynamic PVCs stay in the `Pending` state until they are mounted.
====

. If dynamically-provisioned storage is unavailable, create a local storage PVC by completing the following steps:
+
[WARNING]
====
If you delete or otherwise lose access to the node that contains the stored backup data, you can lose data.
====

.. Create a `StorageClass` CR file named `etcd-backup-local-storage.yaml` with the following contents:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: etcd-backup-local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: Immediate
----

.. Apply the `StorageClass` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-local-storage.yaml
----

.. Create a PV named `etcd-backup-pv-fs.yaml` from the applied `StorageClass` with contents such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  name: etcd-backup-pv-fs
spec:
  capacity:
    storage: 100Gi <1>
  volumeMode: Filesystem
  accessModes:
  - ReadWriteMany
  persistentVolumeReclaimPolicy: Delete
  storageClassName: etcd-backup-local-storage
  local:
    path: /mnt/
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - <example_master_node> <2>
----
<1> The amount of storage available to the PV. Adjust this value for your requirements.
<2> Replace this value with the master node to attach this PV to.
+
[TIP]
====
Run the following command to list the available nodes:

[source,terminal]
----
$ oc get nodes
----
====

.. Verify the creation of the PV by running the following command:
+
[source,terminal]
----
$ oc get pv
----
+
.Example output
[source,terminal]
----
NAME                    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS                REASON   AGE
etcd-backup-pv-fs       100Gi      RWX            Delete           Available           etcd-backup-local-storage            10s
----

.. Create a PVC named `etcd-backup-pvc.yaml` with contents such as the following example:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: etcd-backup-pvc
spec:
  accessModes:
  - ReadWriteMany
  volumeMode: Filesystem
  resources:
    requests:
      storage: 10Gi <1>
  storageClassName: etcd-backup-local-storage
----
<1> The amount of storage available to the PVC. Adjust this value for your requirements.

.. Apply the PVC by running the following command:
+
[source,terminal]
----
$ oc apply -f etcd-backup-pvc.yaml
----

. Create a custom resource definition (CRD) file named `etcd-recurring-backups.yaml`. The contents of the created CRD define the schedule and retention type of automated backups.
+
** For the default retention type of `RetentionNumber` with 15 retained backups, use contents such as the following example:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1alpha1
kind: Backup
metadata:
  name: etcd-recurring-backup
spec:
  etcd:
    schedule: "20 4 * * *" <1>
    timeZone: "UTC"
    pvcName: etcd-backup-pvc
----
<1> The `CronTab` schedule for recurring backups. Adjust this value for your needs.
+
** To use retention based on the maximum number of backups, add the following key-value pairs to the `etcd` key:
+
[source,yaml]
----
spec:
  etcd:
    retentionPolicy:
      retentionType: RetentionNumber <1>
      retentionNumber:
        maxNumberOfBackups: 5 <2>
----
<1> The retention type. Defaults to `RetentionNumber` if unspecified.
<2> The maximum number of backups to retain. Adjust this value for your needs. Defaults to 15 backups if unspecified.
+
[WARNING]
====
A known issue causes the number of retained backups to be one greater than the configured value.
====
+
** For retention based on the file size of backups, use the following:
+
[source,yaml]
----
spec:
  etcd:
    retentionPolicy:
      retentionType: RetentionSize
      retentionSize:
        maxSizeOfBackupsGb: 20 <1>
----
<1> The maximum file size of the retained backups in gigabytes. Adjust this value for your needs. Defaults to 10 GB if unspecified.
+
[WARNING]
====
A known issue causes the maximum size of retained backups to be up to 10 GB greater than the configured value.
====

. Create the cron job defined by the CRD by running the following command:
+
[source,terminal]
----
$ oc create -f etcd-recurring-backup.yaml
----

. To find the created cron job, run the following command:
+
[source,terminal]
----
$ oc get cronjob -n openshift-etcd
----
