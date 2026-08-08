---
title: "Disaster recovery for a hosted cluster by using {oadp-short}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-disaster-recovery-oadp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-disaster-recovery-oadp
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Disaster recovery for a hosted cluster by using {oadp-short}

[id="hcp-disaster-recovery-oadp"]
= Disaster recovery for a hosted cluster by using {oadp-short}

You can use the {oadp-first} Operator to perform disaster recovery on {aws-first} and bare metal.

The disaster recovery process with {oadp-first} involves the following steps:

. Preparing your platform, such as {aws-full} or bare metal, to use {oadp-short}
. Backing up the data plane workload
. Backing up the control plane workload
. Restoring a hosted cluster by using {oadp-short}

[id="prerequisites_{context}"]
== Prerequisites

You must meet the following prerequisites on the management cluster:

* You installed the {oadp-short} Operator.
* You created a storage class.
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {oadp-short} subscription through a catalog source.
* You have access to a cloud storage provider that is compatible with {oadp-short}, such as S3, {azure-full}, {gcp-full}, or MinIO.
* In a disconnected environment, you have access to a self-hosted storage provider, for example {odf-full} or MinIO, that is compatible with {oadp-short}.
* Your {hcp} pods are up and running.
* You are using a supported version of {oadp-short} for your management cluster. For example, if your management cluster is on OpenShift Container Platform 4.20, you must use {oadp-short} version 1.5. For more information, see Support for {oadp-first}.

[id="prepare-aws-oadp_{context}"]
== Preparing {aws-short} to use {oadp-short}

To perform disaster recovery for a hosted cluster, you can use {oadp-first} on {aws-first} S3 compatible storage. After creating the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

To prepare {aws-short} to use {oadp-short}, see "Configuring the {oadp-full} with Multicloud Object Gateway".

[role="_additional-resources"]
.Additional resources

* Configuring the {oadp-full} with Multicloud Object Gateway

.Next steps

* Backing up the data plane workload
* Backing up the control plane workload

[id="prepare-bm-dr-oadp_{context}"]
== Preparing bare metal to use {oadp-short}

To perform disaster recovery for a hosted cluster, you can use {oadp-first} on bare metal. After creating the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

To prepare bare metal to use {oadp-short}, see "Configuring the {oadp-full} with AWS S3 compatible storage".

[role="_additional-resources"]
.Additional resources

* Configuring the {oadp-full} with AWS S3 compatible storage

.Next steps

* Backing up the data plane workload
* Backing up the control plane workload

[id="backing-up-data-plane-oadp_{context}"]
== Backing up the data plane workload

If the data plane workload is not important, you can skip this procedure. To back up the data plane workload by using the {oadp-short} Operator, see "Backing up applications".

[role="_additional-resources"]
.Additional resources

* Backing up applications

.Next steps

* Restoring a hosted cluster by using {oadp-short}

[id="backing-up-cp-oadp_{context}"]
== Backing up the control plane workload

You can back up the control plane workload by creating the `Backup` custom resource (CR). The steps vary depending on whether your platform is {aws-short} or bare metal.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc

[id="hcp-dr-oadp-backup-cp-workload-aws_{context}"]
= Backing up the control plane workload on {aws-short}

You can back up the control plane workload by creating the `Backup` custom resource (CR).

To monitor and observe the backup process, see "Observing the backup and restore process".

.Procedure

. Pause the reconciliation of the `HostedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
----

. Get the infrastructure ID of your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get hostedcluster -n local-cluster <hosted_cluster_name> -o=jsonpath="{.spec.infraID}"
----
+
Note the infrastructure ID to use in the next step.

. Pause the reconciliation of the `cluster.cluster.x-k8s.io` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch cluster.cluster.x-k8s.io \
  -n local-cluster-<hosted_cluster_name> <hosted_cluster_infra_id> \
  --type json -p '[{"op": "add", "path": "/spec/paused", "value": true}]'
----

. Pause the reconciliation of the `NodePool` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
  --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
----

. Pause the reconciliation of the `AgentCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentcluster -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused=true --all'
----

. Pause the reconciliation of the `AgentMachine` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentmachine -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused=true --all'
----

. Annotate the `HostedCluster` resource to prevent the deletion of the hosted control plane namespace by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  hypershift.openshift.io/skip-delete-hosted-controlplane-namespace=true
----

. Create a YAML file that defines the `Backup` CR:
+
.Example `backup-control-plane.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup_resource_name> <1>
  namespace: openshift-adp
  labels:
    velero.io/storage-location: default
spec:
  hooks: {}
  includedNamespaces: <2>
  - <hosted_cluster_namespace> <3>
  - <hosted_control_plane_namespace> <4>
  includedResources:
  - sa
  - role
  - rolebinding
  - pod
  - pvc
  - pv
  - bmh
  - configmap
  - infraenv <5>
  - priorityclasses
  - pdb
  - agents
  - hostedcluster
  - nodepool
  - secrets
  - hostedcontrolplane
  - cluster
  - agentcluster
  - agentmachinetemplate
  - agentmachine
  - machinedeployment
  - machineset
  - machine
  excludedResources: []
  storageLocation: default
  ttl: 2h0m0s
  snapshotMoveData: true <6>
  datamover: "velero" <6>
  defaultVolumesToFsBackup: true <7>
----
====
<1> Replace `backup_resource_name` with the name of your `Backup` resource.
<2> Selects specific namespaces to back up objects from them. You must include your hosted cluster namespace and the hosted control plane namespace.
<3> Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, for example, `clusters`.
<4> Replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, for example, `clusters-hosted`.
<5> You must create the `infraenv` resource in a separate namespace. Do not delete the `infraenv` resource during the backup process.
<6> Enables the CSI volume snapshots and uploads the control plane workload automatically to the cloud storage.
<7> Sets the `fs-backup` backing up method for persistent volumes (PVs) as default. This setting is useful when you use a combination of Container Storage Interface (CSI) volume snapshots and the `fs-backup` method.
+
[NOTE]
====
If you want to use CSI volume snapshots, you must add the `backup.velero.io/backup-volumes-excludes=<pv_name>` annotation to your PVs.
====

. Apply the `Backup` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f backup-control-plane.yaml
----

.Verification

* Verify if the value of the `status.phase` is `Completed` by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io <backup_resource_name> -n openshift-adp \
  -o jsonpath='{.status.phase}'
----

.Next steps

* Restoring a hosted cluster by using OADP
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc

[id="hcp-dr-oadp-backup-cp-workload-bm_{context}"]
= Backing up the control plane workload on a bare-metal platform

You can back up the control plane workload by creating the `Backup` custom resource (CR).

To monitor and observe the backup process, see "Observing the backup and restore process".

.Procedure

. Pause the reconciliation of the `HostedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
----

. Get the infrastructure ID of your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  get hostedcluster -n <hosted_cluster_namespace> \
  <hosted_cluster_name> -o=jsonpath="{.spec.infraID}"
----

. Note the infrastructure ID to use in the next step.

. Pause the reconciliation of the `cluster.cluster.x-k8s.io` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate cluster -n <hosted_control_plane_namespace> \
  <hosted_cluster_infra_id> cluster.x-k8s.io/paused=true
----

. Pause the reconciliation of the `NodePool` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
  --type json -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "true"}]'
----

. Pause the reconciliation of the `AgentCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentcluster -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused=true --all
----

. Pause the reconciliation of the `AgentMachine` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentmachine -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused=true --all
----

. If you are backing up and restoring to the same management cluster, annotate the `HostedCluster` resource to prevent the deletion of the hosted control plane namespace by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  hypershift.openshift.io/skip-delete-hosted-controlplane-namespace=true
----

. Create a YAML file that defines the `Backup` CR:
+
.Example `backup-control-plane.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup_resource_name> # <1>
  namespace: openshift-adp
  labels:
    velero.io/storage-location: default
spec:
  hooks: {}
  includedNamespaces: # <2>
  - <hosted_cluster_namespace> # <3>
  - <hosted_control_plane_namespace> # <4>
  - <agent_namespace> # <5>
  includedResources:
  - sa
  - role
  - rolebinding
  - pod
  - pvc
  - pv
  - bmh
  - configmap
  - infraenv
  - priorityclasses
  - pdb
  - agents
  - hostedcluster
  - nodepool
  - secrets
  - services
  - deployments
  - hostedcontrolplane
  - cluster
  - agentcluster
  - agentmachinetemplate
  - agentmachine
  - machinedeployment
  - machineset
  - machine
  excludedResources: []
  storageLocation: default
  ttl: 2h0m0s
  snapshotMoveData: true # <6>
  datamover: "velero" # <6>
  defaultVolumesToFsBackup: true # <7>
----
====
<1> Replace `backup_resource_name` with the name of your `Backup` resource.
<2> Selects specific namespaces to back up objects from them. You must include your hosted cluster namespace and the hosted control plane namespace.
<3> Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, for example, `clusters`.
<4> Replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, for example, `clusters-hosted`.
<5> Replace `<agent_namespace>` with the namespace where your `Agent`, `BMH`, and `InfraEnv` CRs are located, for example, `agents`.
<6> Enables the CSI volume snapshots and uploads the control plane workload automatically to the cloud storage.
<7> Sets the `fs-backup` backing up method for persistent volumes (PVs) as default. This setting is useful when you use a combination of Container Storage Interface (CSI) volume snapshots and the `fs-backup` method.
+
[NOTE]
====
If you want to use CSI volume snapshots, you must add the `backup.velero.io/backup-volumes-excludes=<pv_name>` annotation to your PVs.
====

. Apply the `Backup` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f backup-control-plane.yaml
----

.Verification

* Verify if the value of the `status.phase` is `Completed` by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io <backup_resource_name> -n openshift-adp \
  -o jsonpath='{.status.phase}'
----

.Next steps

* Restore a hosted cluster by using OADP.

[id="hcp-restoring-oadp_{context}"]
== Restoring a hosted cluster by using {oadp-short}

You can restore a hosted cluster into the same management cluster or into a new management cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc

[id="hcp-dr-oadp-restore_{context}"]
= Restoring a hosted cluster into the same management cluster by using {oadp-short}

You can restore the hosted cluster by creating the `Restore` custom resource (CR).

* If you are using an _in-place_ update, InfraEnv does not need spare nodes. You need to re-provision the worker nodes from the new management cluster.
* If you are using a _replace_ update, you need some spare nodes for InfraEnv to deploy the worker nodes.

[IMPORTANT]
====
After you back up your hosted cluster, you must destroy it to initiate the restoring process. To initiate node provisioning, you must back up workloads in the data plane before deleting the hosted cluster.
====

.Prerequisites

* You completed the steps in Removing a cluster by using the console to delete your hosted cluster.
* You completed the steps in Removing remaining resources after removing a cluster.

To monitor and observe the backup process, see "Observing the backup and restore process".

.Procedure

. Verify that no pods and persistent volume claims (PVCs) are present in the hosted control plane namespace by running the following command:
+
[source,terminal]
----
$ oc get pod pvc -n <hosted_control_plane_namespace>
----
+
.Expected output
[source,terminal]
----
No resources found
----

. Create a YAML file that defines the `Restore` CR:
+
.Example `restore-hosted-cluster.yaml` file
[source,yaml]
----
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: <restore_resource_name> <1>
  namespace: openshift-adp
spec:
  backupName: <backup_resource_name> <2>
  restorePVs: true <3>
  existingResourcePolicy: update <4>
  excludedResources:
  - nodes
  - events
  - events.events.k8s.io
  - backups.velero.io
  - restores.velero.io
  - resticrepositories.velero.io
----
<1> Replace `<restore_resource_name>` with the name of your `Restore` resource.
<2> Replace `<backup_resource_name>` with the name of your `Backup` resource.
<3> Initiates the recovery of persistent volumes (PVs) and its pods.
<4> Ensures that the existing objects are overwritten with the backed up content.
+
[IMPORTANT]
====
You must create the `infraenv` resource in a separate namespace. Do not delete the `infraenv` resource during the restore process. The `infraenv` resource is mandatory for the new nodes to be reprovisioned.
====

. Apply the `Restore` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f restore-hosted-cluster.yaml
----

. Verify if the value of the `status.phase` is `Completed` by running the following command:
+
[source,terminal]
----
$ oc get hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace> \
  -o jsonpath='{.status.phase}'
----

. After the restore process is complete, start the reconciliation of the `HostedCluster` and `NodePool` resources that you paused during backing up of the control plane workload:

.. Start the reconciliation of the `HostedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type json \
  -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "false"}]'
----

.. Start the reconciliation of the `NodePool` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
  --type json \
  -p '[{"op": "add", "path": "/spec/pausedUntil", "value": "false"}]'
----

. Start the reconciliation of the Agent provider resources that you paused during backing up of the control plane workload:

.. Start the reconciliation of the `AgentCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentcluster -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused- --overwrite=true --all
----

.. Start the reconciliation of the `AgentMachine` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate agentmachine -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused- --overwrite=true --all
----

. Remove the `hypershift.openshift.io/skip-delete-hosted-controlplane-namespace-` annotation in the `HostedCluster` resource to avoid manually deleting the hosted control plane namespace by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <management_cluster_kubeconfig_file> \
  annotate hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  hypershift.openshift.io/skip-delete-hosted-controlplane-namespace- \
  --overwrite=true --all
----
// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc

[id="hcp-dr-oadp-restore-new-mgmt_{context}"]
= Restoring a hosted cluster into a new management cluster by using {oadp-short}

You can restore the hosted cluster into a new management cluster by creating the `Restore` custom resource (CR).

* If you are using an in-place update, the `InfraEnv` resource does not need spare nodes. Instead, you need to re-provision the worker nodes from the new management cluster.
* If you are using a replace update, you need some spare nodes for the `InfraEnv` resource to deploy the worker nodes.

.Prerequisites

* You configured the new management cluster to use {oadp-first}. The new management cluster must have the same Data Protection Application (DPA) as the management cluster that you backed up from so that the `Restore` CR can access the backup storage.
* You configured the networking settings of the new management cluster to resolve the DNS of the hosted cluster.

** The DNS of the host must resolve to the IP of both the new management cluster and the hosted cluster.
** The hosted cluster must resolve to the IP of the new management cluster.

To monitor and observe the backup process, see "Observing the backup and restore process".

[IMPORTANT]
====
Complete the following steps on the new management cluster that you are restoring the hosted cluster to, not on the management cluster that you created the backup from.
====

.Procedure

. Create a YAML file that defines the `Restore` CR:
+
.Example `restore-hosted-cluster.yaml` file
[source,yaml]
----
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: <restore_resource_name> # <1>
  namespace: openshift-adp
spec:
  includedNamespaces: # <2>
  - <hosted_cluster_namespace> # <3>
  - <hosted_control_plane_namespace> # <4>
  - <agent_namespace> # <5>
  backupName: <backup_resource_name> # <6>
  cleanupBeforeRestore: CleanupRestored
  veleroManagedClustersBackupName: <managed_cluster_name> # <7>
  veleroCredentialsBackupName: <credentials_backup_name>
  veleroResourcesBackupName: <resources_backup_name>
  restorePVs: true # <8>
  preserveNodePorts: true
  existingResourcePolicy: update # <9>
  excludedResources:
  - pod
  - nodes
  - events
  - events.events.k8s.io
  - backups.velero.io
  - restores.velero.io
  - resticrepositories.velero.io
  - pv
  - pvc
----
<1> Replace `<restore_resource_name>` with the name of your `Restore` resource.
<2> Selects specific namespaces to back up objects from them. You must include your hosted cluster namespace and the hosted control plane namespace.
<3> Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, for example, `clusters`.
<4> Replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, for example, `clusters-hosted`.
<5> Replace `<agent_namespace>` with the namespace where your `Agent`, `BMH`, and `InfraEnv` CRs are located, for example, `agents`.
<6> Replace `<backup_resource_name>` with the name of your `Backup` resource.
<7> You can omit this field if you are not using {rh-rhacm-title}.
<8> Initiates the recovery of persistent volumes (PVs) and its pods.
<9> Ensures that the existing objects are overwritten with the backed up content.

. Apply the `Restore` CR by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> apply -f restore-hosted-cluster.yaml
----

. Verify that the value of the `status.phase` is `Completed` by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  get restore.velero.io <restore_resource_name> \
  -n openshift-adp -o jsonpath='{.status.phase}'
----

. Verify that all CRs are restored by running the following commands:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get infraenv -n <agent_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get agent -n <agent_namespace>
----
+
[source,terminal]
----
$  oc --kubeconfig <restore_management_kubeconfig> get bmh -n <agent_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get hostedcluster -n <hosted_cluster_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get nodepool -n <hosted_cluster_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get agentmachine -n <hosted_controlplane_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get agentcluster -n <hosted_controlplane_namespace>
----

. If you plan to use the new management cluster as your main management cluster going forward, complete the following steps. Otherwise, if you plan to use the management cluster that you backed up from as your main management cluster, complete steps 5 - 8 in "Restoring a hosted cluster into the same management cluster by using {oadp-short}".

.. Remove the Cluster API deployment from the management cluster that you backed up from by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> delete deploy cluster-api \
  -n <hosted_control_plane_namespace>
----
+
Because only one Cluster API can access a cluster at a time, this step ensures that the Cluster API for the new management cluster functions correctly.

.. After the restore process is complete, start the reconciliation of the `HostedCluster` and `NodePool` resources that you paused during backing up of the control plane workload:

... Start the reconciliation of the `HostedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  patch hostedcluster -n <hosted_cluster_namespace> <hosted_cluster_name> \
  --type json \
  -p '[{"op": "replace", "path": "/spec/pausedUntil", "value": "false"}]'
----

... Start the reconciliation of the `NodePool` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  patch nodepool -n <hosted_cluster_namespace> <node_pool_name> \
  --type json \
  -p '[{"op": "replace", "path": "/spec/pausedUntil", "value": "false"}]'
----

... Verify that the hosted cluster is reporting that the hosted control plane is available by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> get hostedcluster
----

... Verify that the hosted cluster is reporting that the cluster operators are available by running the following command:
+
[source,terminal]
----
$ oc get co --kubeconfig <hosted_cluster_kubeconfig>
----

.. Start the reconciliation of the Agent provider resources that you paused during backing up of the control plane workload:

... Start the reconciliation of the `AgentCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  annotate agentcluster -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused- --overwrite=true --all
----

... Start the reconciliation of the `AgentMachine` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  annotate agentmachine -n <hosted_control_plane_namespace>  \
  cluster.x-k8s.io/paused- --overwrite=true --all
----

... Start the reconciliation of the `Cluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  annotate cluster -n <hosted_control_plane_namespace> \
  cluster.x-k8s.io/paused- --overwrite=true --all
----

.. Verify that the node pool is working as expected by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <restore_management_kubeconfig> \
  get nodepool -n <hosted_cluster_namespace>
----
+
.Example output
[source,terminal]
----
NAME       CLUSTER    DESIRED NODES   CURRENT NODES   AUTOSCALING   AUTOREPAIR   VERSION   UPDATINGVERSION   UPDATINGCONFIG   MESSAGE
hosted-0   hosted-0   3               3               False         False        4.17.11   False             False
----

.. Optional: To ensure that no conflicts exist and that the new management cluster has continued functionality, remove the `HostedCluster` resources from the backup management cluster by completing the following steps:

... In the management cluster that you backed up from, in the `ClusterDeployment` resource, set the `spec.preserveOnDelete` parameter to `true` by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> patch \
  -n <hosted_control_plane_namespace> \
  ClusterDeployment/<hosted_cluster_name> -p \
  '{"spec":{"preserveOnDelete":'true'}}' \
  --type=merge
----
+
This step ensures that the hosts are not deprovisioned.

... Delete the machines by running the following commands:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> patch \
  <machine_name> -n <hosted_control_plane_namespace> -p \
  '[{"op":"remove","path":"/metadata/finalizers"}]' \
  --type=merge
----
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  delete machine <machine_name> \
  -n <hosted_control_plane_namespace>
----

... Delete the `AgentCluster` and `Cluster` resources by running the following commands:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  delete agentcluster <hosted_cluster_name> \
  -n <hosted_control_plane_namespace>
----
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  patch cluster <cluster_name> \
  -n <hosted_control_plane_namespace> \
  -p '[{"op":"remove","path":"/metadata/finalizers"}]' \
  --type=json
----
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  delete cluster <cluster_name> \
  -n <hosted_control_plane_namespace>
----

... If you use {rh-rhacm-title}, delete the managed cluster by running the following commands:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  patch managedcluster <hosted_cluster_name> \
  -n <hosted_cluster_namespace> \
  -p '[{"op":"remove","path":"/metadata/finalizers"}]' \
  --type=json
----
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  delete managedcluster <hosted_cluster_name> \
  -n <hosted_cluster_namespace>
----

... Delete the `HostedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig <backup_management_kubeconfig> \
  delete hostedcluster \
  -n <hosted_cluster_namespace> <hosted_cluster_name>
----

[role="_additional-resources"]
.Additional resources
* Removing a cluster by using the console
* Removing remaining resources after removing a cluster

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-oadp-observe_{context}"]
= Observing the backup and restore process

When using {oadp-first} to backup and restore a hosted cluster, you can monitor and observe the process.

.Procedure

. Observe the backup process by running the following command:
+
[source,terminal]
----
$ watch "oc get backups.velero.io -n openshift-adp <backup_resource_name> -o jsonpath='{.status}'"
----

. Observe the restore process by running the following command:
+
[source,terminal]
----
$ watch "oc get restores.velero.io -n openshift-adp <backup_resource_name> -o jsonpath='{.status}'"
----

. Observe the Velero logs by running the following command:
+
[source,terminal]
----
$ oc logs -n openshift-adp -ldeploy=velero -f
----

. Observe the progress of all of the {oadp-short} objects by running the following command:
+
[source,terminal]
----
$ watch "echo BackupRepositories:;echo;oc get backuprepositories.velero.io -A;echo; echo BackupStorageLocations: ;echo; oc get backupstoragelocations.velero.io -A;echo;echo DataUploads: ;echo;oc get datauploads.velero.io -A;echo;echo DataDownloads: ;echo;oc get datadownloads.velero.io -n openshift-adp; echo;echo VolumeSnapshotLocations: ;echo;oc get volumesnapshotlocations.velero.io -A;echo;echo Backups:;echo;oc get backup -A; echo;echo Restores:;echo;oc get restore -A"
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp.adoc
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-oadp-observe-velero_{context}"]
= Using the velero CLI to describe the Backup and Restore resources

When using {oadp-full}, you can get more details of the `Backup` and `Restore` resources by using the `velero` command-line interface (CLI).

.Procedure

. Create an alias to use the `velero` CLI from a container by running the following command:
+
[source,terminal]
----
$ alias velero='oc -n openshift-adp exec deployment/velero -c velero -it -- ./velero'
----

. Get details of your `Restore` custom resource (CR) by running the following command:
+
[source,terminal]
----
$ velero restore describe <restore_resource_name> --details <1>
----
<1> Replace `<restore_resource_name>` with the name of your `Restore` resource.

. Get details of your `Backup` CR by running the following command:
+
[source,terminal]
----
$ velero restore describe <backup_resource_name> --details <1>
----
<1> Replace `<backup_resource_name>` with the name of your `Backup` resource.
