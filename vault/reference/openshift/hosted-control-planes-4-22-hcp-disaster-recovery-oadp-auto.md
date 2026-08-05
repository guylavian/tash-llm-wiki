---
title: "Automated disaster recovery for a hosted cluster by using {oadp-short}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-disaster-recovery-oadp-auto
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-disaster-recovery-oadp-auto
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Automated disaster recovery for a hosted cluster by using {oadp-short}

[id="hcp-disaster-recovery-oadp-auto"]
= Automated disaster recovery for a hosted cluster by using {oadp-short}

In hosted clusters on bare-metal or {aws-first} platforms, you can automate some backup and restore steps by using the {oadp-first} Operator.

The process involves the following steps:

. Configuring {oadp-short}
. Defining a Data Protection Application (DPA)
. Backing up the data plane workload
. Backing up the control plane workload
. Restoring a hosted cluster by using {oadp-short}

[id="hcp-auto-dr-prereqs_{context}"]
== Prerequisites

You must meet the following prerequisites on the management cluster:

* You installed the {oadp-short} Operator.
* You created a storage class.
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {oadp-short} subscription through a catalog source.
* You have access to a cloud storage provider that is compatible with {oadp-short}, such as S3, {azure-full}, {gcp-full}, or MinIO.
* In a disconnected environment, you have access to a self-hosted storage provider that is compatible with {oadp-short}, for example {odf-full} or MinIO.
* Your {hcp} pods are up and running.
* You are using a supported version of {oadp-short} for your management cluster. For example, if your management cluster is on OpenShift Container Platform 4.20, you must use {oadp-short} version 1.5. For more information, see Support for {oadp-first}.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-prep-oadp-auto_{context}"]
= Configuring {oadp-short}

If your hosted cluster is on {aws-short}, follow the steps in "Configuring the {oadp-full} with Multicloud Object Gateway" to configure {oadp-short}.

If your hosted cluster is on a bare-metal platform, follow the steps in "Configuring the {oadp-full} with AWS S3 compatible storage" to configure {oadp-short}.

[role="_additional-resources"]
.Additional resources

* Configuring the {oadp-full} with Multicloud Object Gateway
* Configuring the {oadp-full} with AWS S3 compatible storage

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-oadp-dpa_{context}"]
= Automating the backup and restore process by using a DPA

You can automate parts of the backup and restore process by using a Data Protection Application (DPA). When you use a DPA, the steps to pause and restart the reconciliation of resources are automated. The DPA defines information including backup locations and Velero pod configurations.

You can create a DPA by defining a `DataProtectionApplication` object.

.Procedure

* If you use a bare-metal platform, you can create a DPA by completing the following steps:

. Create a manifest file similar to the following example:
+
.Example `dpa.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-sample
  namespace: openshift-adp
spec:
  backupLocations:
    - name: default
      velero:
        provider: aws # <1>
        default: true
        objectStorage:
          bucket: <bucket_name> # <2>
          prefix: <bucket_prefix> # <3>
        config:
          region: minio # <4>
          profile: "default"
          s3ForcePathStyle: "true"
          s3Url: "<bucket_url>" # <5>
          insecureSkipTLSVerify: "true"
        credential:
          key: cloud
          name: cloud-credentials
          default: true
  snapshotLocations:
    - velero:
        provider: aws # <1>
        config:
          region: minio # <4>
          profile: "default"
        credential:
          key: cloud
          name: cloud-credentials
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia #<6>
    velero:
      defaultPlugins:
        - openshift
        - aws
        - csi
        - hypershift
      resourceTimeout: 2h
----
====
<1> Specify the provider for Velero. If you are using bare metal and MinIO, you can use `aws` as the provider.
<2> Specify the bucket name; for example, `oadp-backup`.
<3> Specify the bucket prefix; for example, `hcp`.
<4> The bucket region in this example is `minio`, which is a storage provider that is compatilble with the S3 API.
<5> Specify the URL of the S3 endpoint.
<6> Specify `kopia` as the uploader type. The `restic` uploader type is deprecated for {oadp-short} 1.5 and later.

. Create the DPA object by running the following command:
+
[source,terminal]
----
$ oc create -f dpa.yaml
----
+
After you create the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

* If you use {aws-first}, you can create a DPA by completing the following steps:

. Create a manifest file similar to the following example:
+
.Example `dpa.yaml` file
[%collapsible]
====
[source,yaml]
----
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-sample
  namespace: openshift-adp
spec:
  backupLocations:
    - name: default
      velero:
        provider: aws
        default: true
        objectStorage:
          bucket: <bucket_name> # <1>
          prefix: <bucket_prefix> # <2>
        config:
          region: minio # <3>
          profile: "backupStorage"
        credential:
          key: cloud
          name: cloud-credentials
  snapshotLocations:
    - velero:
        provider: aws
        config:
          region: minio # <3>
          profile: "volumeSnapshot"
        credential:
          key: cloud
          name: cloud-credentials
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia # <4>
    velero:
      defaultPlugins:
        - openshift
        - aws
        - csi
        - hypershift
      resourceTimeout: 2h
----
====
<1> Specify the bucket name; for example, `oadp-backup`.
<2> Specify the bucket prefix; for example, `hcp`.
<3> The bucket region in this example is `minio`, which is a storage provider that is compatilble with the S3 API.
<4> Specify `kopia` as the uploader type. The `restic` uploader type is deprecated for {oadp-short} 1.5 and later.

. Create the DPA resource by running the following command:
+
[source,terminal]
----
$ oc create -f dpa.yaml
----
+
After you create the `DataProtectionApplication` object, new `velero` deployment and `node-agent` pods are created in the `openshift-adp` namespace.

.Next steps

* Back up the data plane workload.

[id="backing-up-data-plane-oadp-auto_{context}"]
== Backing up the data plane workload

To back up the data plane workload by using the {oadp-short} Operator, see "Backing up applications". If the data plane workload is not important, you can skip this procedure.

[role="_additional-resources"]
.Additional resources

* Backing up applications

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-oadp-backup-cp-workload-auto_{context}"]
= Backing up the control plane workload

You can back up the control plane workload by creating the `Backup` custom resource (CR).

To monitor and observe the backup process, see "Observing the backup and restore process".

.Procedure

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
  - route
  - clusterdeployment
  excludedResources: []
  storageLocation: default
  ttl: 2h0m0s
  snapshotMoveData: true <6>
  datamover: "velero" <6>
  defaultVolumesToFsBackup: false <7>
----
====
<1> Replace `backup_resource_name` with a name for your `Backup` resource.
<2> Selects specific namespaces to back up objects from them. You must include your hosted cluster namespace and the hosted control plane namespace.
<3> Replace `<hosted_cluster_namespace>` with the name of the hosted cluster namespace, for example, `clusters`.
<4> Replace `<hosted_control_plane_namespace>` with the name of the hosted control plane namespace, for example, `clusters-hosted`.
<5> You must create the `infraenv` resource in a separate namespace. Do not delete the `infraenv` resource during the backup process.
<6> Enables the CSI volume snapshots and uploads the control plane workload automatically to the cloud storage.
<7> Specifies that the `fs-backup` backing up method for persistent volumes (PVs) is not used.
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

* Verify that the value of the `status.phase` is `Completed` by running the following command:
+
[source,terminal]
----
$ oc get backups.velero.io <backup_resource_name> -n openshift-adp \
  -o jsonpath='{.status.phase}'
----

.Next steps

* Restore the hosted cluster by using {oadp-short}.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-disaster-recovery-oadp-auto.adoc

[id="hcp-dr-oadp-restore-auto_{context}"]
= Restoring a hosted cluster by using {oadp-short}

You can restore the hosted cluster by creating the `Restore` custom resource (CR).

* If you are using an in-place update, the `InfraEnv` resource does not need spare nodes. You need to re-provision the worker nodes from the new management cluster.
* If you are using a replace update, you need some spare nodes for the `InfraEnv` resource to deploy the worker nodes.

[IMPORTANT]
====
After you back up your hosted cluster, you must destroy it to initiate the restoring process. To initiate node provisioning, you must back up workloads in the data plane before deleting the hosted cluster.
====

.Prerequisites

* You completed the steps in Removing a cluster by using the console ({rh-rhacm} documentation) to delete your hosted cluster.
* You completed the steps in Removing remaining resources after removing a cluster ({rh-rhacm} documentation).

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
<1> Replace `<restore_resource_name>` with a name for your `Restore` resource.
<2> Replace `<backup_resource_name>` with a name for your `Backup` resource.
<3> Initiates the recovery of persistent volumes (PVs) and its pods.
<4> Ensures that the existing objects are overwritten with the backed up content.
+
[IMPORTANT]
====
You must create the `InfraEnv` resource in a separate namespace. Do not delete the `InfraEnv` resource during the restore process. The `InfraEnv` resource is mandatory for the new nodes to be reprovisioned.
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
