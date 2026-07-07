---
title: "Before you update the telco core CNF cluster"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-update-before-the-update
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/update-before-the-update
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Before you update the telco core CNF cluster

[id="update-before-the-update"]
= Before you update the telco core CNF cluster

[role="_abstract"]
Before you start the cluster update, you must pause worker nodes, back up the etcd database, and do a final cluster health check before proceeding.

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/updating/update-before-the-update.adoc

[id="update-pause-worker-nodes-before-update_{context}"]
= Pausing worker nodes before the update

[role="_abstract"]
You must pause the worker nodes before you proceed with the update.
In the following example, there are 2 `mcp` groups, `mcp-1` and `mcp-2`.
You patch the `spec.paused` field to `true` for each of the `MachineConfigPool` groups.

.Procedure

. Patch the `mcp` CRs to pause the nodes and drain and remove the pods from those nodes by running the following command:
+
[source,terminal]
----
$ oc patch mcp/mcp-1 --type merge --patch '{"spec":{"paused":true}}'
----
+
[source,terminal]
----
$ oc patch mcp/mcp-2 --type merge --patch '{"spec":{"paused":true}}'
----

. Get the status of the paused `mcp` groups:
+
[source,terminal]
----
$ oc get mcp -o json | jq -r '["MCP","Paused"], ["---","------"], (.items[] | [(.metadata.name), (.spec.paused)]) | @tsv' | grep -v worker
----
+
.Example output
[source,terminal]
----
MCP     Paused
---     ------
master  false
mcp-1   true
mcp-2   true
----
+
[NOTE]
====
The default control plane and worker `mcp` groups are not changed during an update.
====

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/updating/update-before-the-update.adoc

[id="update-backup-etcd-database-before-update_{context}"]
= Backup the etcd database before you proceed with the update

[role="_abstract"]
You must backup the etcd database before you proceed with the update.

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

[role="_additional-resources"]
.Additional resources

* Backing up etcd

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/updating/update-before-the-update.adoc

[id="update-checking-cluster-health_{context}"]
= Checking the cluster health

[role="_abstract"]
You should check the cluster health often during the update.
Check for the node status, cluster Operators status and failed pods.

.Procedure
. Check the status of the cluster Operators by running the following command:
+
[source,terminal]
----
$ oc get co
----
+
.Example output
[source,terminal]
----
NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
authentication                             4.14.34   True        False         False      4d22h
baremetal                                  4.14.34   True        False         False      4d22h
cloud-controller-manager                   4.14.34   True        False         False      4d23h
cloud-credential                           4.14.34   True        False         False      4d23h
cluster-autoscaler                         4.14.34   True        False         False      4d22h
config-operator                            4.14.34   True        False         False      4d22h
console                                    4.14.34   True        False         False      4d22h
...
service-ca                                 4.14.34   True        False         False      4d22h
storage                                    4.14.34   True        False         False      4d22h
----

. Check the status of the cluster nodes:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME           STATUS   ROLES                  AGE     VERSION
ctrl-plane-0   Ready    control-plane,master   4d22h   v1.27.15+6147456
ctrl-plane-1   Ready    control-plane,master   4d22h   v1.27.15+6147456
ctrl-plane-2   Ready    control-plane,master   4d22h   v1.27.15+6147456
worker-0       Ready    mcp-1,worker           4d22h   v1.27.15+6147456
worker-1       Ready    mcp-2,worker           4d22h   v1.27.15+6147456
----

. Check that there are no in-progress or failed pods.
There should be no pods returned when you run the following command.
+
[source,terminal]
----
$ oc get po -A | grep -E -iv 'running|complete'
----
