---
title: "GCP PD CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-gcp-pd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-gcp-pd
version: 4.22
family: storage
documentKind: "Documentation"
---

# GCP PD CSI Driver Operator

[id="persistent-storage-csi-gcp-pd"]
= GCP PD CSI Driver Operator

== Overview

OpenShift Container Platform can provision persistent volumes (PVs) using the Container Storage Interface (CSI) driver for Google Cloud Platform (GCP) persistent disk (PD) storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a Container Storage Interface (CSI) Operator and driver.

To create CSI-provisioned persistent volumes (PVs) that mount to GCP PD storage assets, OpenShift Container Platform installs the GCP PD CSI Driver Operator and the GCP PD CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* *GCP PD CSI Driver Operator*: By default, the Operator provides a storage class that you can use to create PVCs. You can disable this default storage class if desired (see Managing the default storage class). You also have the option to create the GCP PD storage class as described in Persistent storage using GCE Persistent Disk.

* *GCP PD driver*: The driver enables you to create and mount GCP PD PVs.
//
+
GCP PD CSI driver supports the C3 instance type for bare metal and N4 machine series. The C3 instance type and N4 machine series support the hyperdisk-balanced disks and hyperdisk-balanced high-availability disks. For more information, see Section _C3 instance type for bare metal and N4 machine series_.

[NOTE]
====
OpenShift Container Platform provides automatic migration for the GCE Persistent Disk in-tree volume plugin to its equivalent CSI driver. For more information, see CSI automatic migration.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="csi-about_{context}"]
= About CSI

Storage vendors have traditionally provided storage drivers as part of Kubernetes. With the implementation of the Container Storage Interface (CSI), third-party providers can instead deliver storage plugins using a standard interface without ever having to change the core Kubernetes code.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-pd-reduce-permissions_{context}"]
= Reducing permissions while using the GCP PD CSI Driver Operator

[role="_abstract"]
The default installation allows the Google Cloud Platform (GCP) persistent disk (PD) Container Storage Interface (CSI) Driver to impersonate any service account in the Google Cloud project. You can reduce the scope of permissions granted to the GCP PD CSI Driver service account in your Google Cloud project to only the required node service accounts.

To reduce permissions, grant the `iam.serviceAccountUser` role to the control plane and compute node service accounts, and then remove the `iam.serviceAccountUser` role from the project-wide service account, thus reducing the scope of the permission.

[NOTE]
====
Reducing permissions only applies to GCP clusters using Workload Identity Federation (WIF).
====

.Procedure

. Grant scoped `iam.serviceAccountUser` role for node service accounts by running the following Bash commands:
+
[source,terminal]
----
gcloud iam service-accounts add-iam-policy-binding "${MASTER_NODE_SA}" --project="${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
gcloud iam service-accounts add-iam-policy-binding "${WORKER_NODE_SA}" --project="${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
----
+
* `GOOGLE_PROJECT_ID`: The unique ID of your Google Cloud project.

* `SERVICE_ACCOUNT_EMAIL`: The email address of the "Member" (the person or service account) who is being granted the new permissions. To find the service account, on WIF clusters, there is a default service account on GCP for the CSI driver based on the cluster name, for example: `${CLUSTER_NAME}-openshift-gcp-pd-csi-*`.

* `MASTER_NODE_SA`: The email address of the service account used by your cluster's master node.

* `WORKER_NODE_SA`: The email address of the service account used by your cluster's worker nodes.

. Remove project-level `iam.serviceAccountUser` role from the binding created by the installation program by running the following Bash commands:
+
[source,terminal]
----
gcloud projects remove-iam-policy-binding "${GOOGLE_PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/iam.serviceAccountUser" --condition=None
----
+

* `SERVICE_ACCOUNT_EMAIL`: The email address of the account losing the permission. For example, `my-app-sa@my-project.iam.gserviceaccount.com`. To find the service account, on WIF clusters, there is a default service account on GCP for the CSI driver based on the cluster name, for example: `${CLUSTER_NAME}-openshift-gcp-pd-csi-*`.

* `GOOGLE_PROJECT_ID`: The unique ID of the Google Cloud project where this is occurring. For example, `prod-data-789`.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-pd-storage-class-ref_{context}"]
= GCP PD CSI driver storage class parameters

The Google Cloud Platform (GCP) persistent disk (PD) Container Storage Interface (CSI) driver uses the CSI `external-provisioner` sidecar as a controller. This is a separate helper container that is deployed with the CSI driver. The sidecar manages persistent volumes (PVs) by triggering the `CreateVolume` operation.

The GCP PD CSI driver uses the `csi.storage.k8s.io/fstype` parameter key to support dynamic provisioning. The following table describes all the GCP PD CSI storage class parameters that are supported by OpenShift Container Platform.

.CreateVolume Parameters
[cols="2,3,2,4",options="header"]
|===
|Parameter  |Values  |Default  |Description

|`type` | `pd-ssd`, `pd-standard`, `pd-balanced`, or `hyperdisk-balanced`| `pd-standard` | Allows you to choose between standard PVs or solid-state-drive PVs.

The driver does not validate the value, thus all the possible values are accepted.

For `hyperdisk-balanced`, be sure to check the limitations under Section _C3 and N4 instance type limitations_.

|`replication-type`| `none` or `regional-pd` | `none` | Allows you to choose between zonal or regional PVs.
|`disk-encryption-kms-key` | Fully qualified resource identifier for the key to use to encrypt new disks. | Empty string | Uses customer-managed encryption keys (CMEK) to encrypt new disks.
|===

[id="c3-instance-type-for-bare-metal-and-n4-machine-series"]
== C3 instance type for bare metal and N4 machine series

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-hyperdisk-limitations_{context}"]
= C3 and N4 instance type limitations

The GCP PD CSI driver support for the C3 instance type for bare metal and N4 machine series have the following limitations:

* You must set the volume size to at least 4Gi when you create hyperdisk-balanced disks. OpenShift Container Platform does not round up to the minimum size, so you must specify the correct size yourself.

* Cloning volumes is not supported when using storage pools.

* For cloning or resizing, hyperdisk-balanced disks original volume size must be 6Gi or greater.

* The default storage class is standard-csi.
+
[IMPORTANT]
====
You need to manually create a storage class.

For information about creating the storage class, see Step 2 in Section _Setting up hyperdisk-balanced disks_.
====
* Clusters with mixed virtual machines (VMs) that use different storage types, for example, N2 and N4, are not supported. This is due to hyperdisks-balanced disks not being usable on most legacy VMs. Similarly, regular persistent disks are not usable on N4/C3 VMs.

* A GCP cluster with c3-standard-2, c3-standard-4, n4-standard-2, and n4-standard-4 nodes can erroneously exceed the maximum attachable disk number, which should be 16 (JIRA link).

* Additional limitations.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-hyperdisk-ha-overview_{context}"]
= Hyperdisk-balanced high availability disks overview

[role="_abstract"]
OpenShift Container Platform supports Hyperdisk Balanced High Availability volumes.

Hyperdisk Balanced High Availability volumes are useful for:

* Protecting your applications from a zonal outage by synchronously replicating data across two zones in the same region

* When you require write access to the same volume in multiple zones

[NOTE]
====
Volume Attributes Classes (VAC) does not work on Hyperdisk Balanced High Availability disks.
====

To set up Hyperdisk Balanced High Availability disks, see Section _Setting up hyperdisk-balanced disks_.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-hyperdisk-storage-pools-overview_{context}"]
= Storage pools for hyperdisk-balanced disks overview

Hyperdisk storage pools can be used with Compute Engine for large-scale storage. A hyperdisk storage pool is a purchased collection of capacity, throughput, and IOPS, which you can then provision for your applications as needed. You can use hyperdisk storage pools to create and manage disks in pools and use the disks across multiple workloads. By managing disks in aggregate, you can save costs while achieving expected capacity and performance growth. By using only the storage that you need in hyperdisk storage pools, you reduce the complexity of forecasting capacity and reduce management by going from managing hundreds of disks to managing a single storage pool.

To set up storage pools, see Setting up hyperdisk-balanced disks.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-hyperdisk-storage-pools-procedure_{context}"]
= Setting up hyperdisk-balanced disks

.Prerequisites
* Access to the cluster with administrative privileges

.Procedure
Complete the following steps to set up hyperdisk-balanced disks:

. Create an OpenShift Container Platform cluster on {GCP} with attached disks provisioned with hyperdisk-balanced disks. This can be achieved by provisioning the cluster with compute node types that support hyperdisk-balanced disks, such as the C3 and N4 machine series from {GCP}.
. Once the OSD cluster is ready, navigate to the **OpenShift console** for Storage Class creation.
Within the console, navigate to the **Storage** section to create a Storage Class specifying the hyperdisk-balanced disk:
+
.Example StorageClass YAML file
[source, yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: hyperdisk-sc <1>
 annotations:
   storageclass.kubernetes.io/is-default-class: 'true'
provisioner: pd.csi.storage.gke.io <2>
parameters:
 replication-type: none
 storage-pools: projects/myproject/zones/us-east1-c/storagePools/hyperdisk-storagepool <3>
 type: hyperdisk-balanced <4>
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: Immediate
----
<1> Specify the name for your storage class. In this example, the name is `hyperdisk-sc`.
<2> Specify the GCP CSI provisioner as `pd.csi.storage.gke.io`.
<3> If using storage pools, specify a list of specific storage pools that you want to use in the following format: `projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`.
<4> Specify the disk type as `hyperdisk-balanced`.
+
[NOTE]
====
If you use storage pools, you must first create a Hyperdisk Storage Pool of the type "Hyperdisk Balanced" in the Google Cloud console prior to referencing it in the OpenShift Storage Class. The Hyperdisk Storage Pool must be created in the same zone as the compute node supporting Hyperdisk is installed in the cluster configuration. For more information about creating a Hyperdisk Storage Pool, see Create a Hyperdisk Storage Pool in the Google Cloud documentation.
====

. Create a GCP cluster with attached disks provisioned with hyperdisk-balanced disks.

. Create a storage class specifying the hyperdisk-balanced disks during installation:

.. Follow the procedure in the _Installing a cluster on GCP with customizations_ section.
+
For your install-config.yaml file, use the following example file:
+
.Example install-config YAML file
[source, yaml]
----
apiVersion: v1
metadata:
  name: ci-op-9976b7t2-8aa6b

sshKey: |
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
baseDomain: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
platform:
  gcp:
    projectID: XXXXXXXXXXXXXXXXXXXXXX
    region: us-central1
controlPlane:
  architecture: amd64
  name: master
  platform:
    gcp:
      type: n4-standard-4 <1>
      osDisk:
        diskType: hyperdisk-balanced <2>
        diskSizeGB: 200
  replicas: 3
compute:
- architecture: amd64
  name: worker
  replicas: 3
  platform:
    gcp:
      type: n4-standard-4 <1>
      osDisk:
        diskType: hyperdisk-balanced <2>
----
<1> Specifies the node type as n4-standard-4.
<2> Specifies the node has the root disk backed by hyperdisk-balanced disk type. All nodes in the cluster should use the same disk type, either hyperdisks-balanced or pd-*.
+
[NOTE]
====
All nodes in the cluster must support hyperdisk-balanced volumes. Clusters with mixed nodes are not supported, for example N2 and N3 using hyperdisk-balanced disks.
====

.. After step 3 in _Incorporating the Cloud Credential Operator utility manifests_ section, copy the following manifests into the manifests directory created by the installation program:
+
* cluster_csi_driver.yaml - specifies opting out of the default storage class creation
* storageclass.yaml - creates a hyperdisk-specific storage class
+
--
.Example cluster CSI driver YAML file
[source, yaml]
----
apiVersion: operator.openshift.io/v1
kind: "ClusterCSIDriver"
metadata:
  name: "pd.csi.storage.gke.io"
spec:
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
  storageClassState: Unmanaged <1>
----
<1> Specifies disabling creation of the default OpenShift Container Platform storage classes.
--
+
--
.Example storage class YAML file
[source, yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: hyperdisk-sc <1>
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: pd.csi.storage.gke.io <2>
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Delete
parameters:
  type: hyperdisk-balanced <3>
  replication-type: none
  provisioned-throughput-on-create: "140Mi" <4>
  provisioned-iops-on-create: "3000" <5>
  storage-pools: projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c <6>
allowedTopologies: <7>
- matchLabelExpressions:
  - key: topology.kubernetes.io/zone
    values:
    - us-east4-c
...
----
<1> Specify the name for your storage class. In this example, it is `hyperdisk-sc`.
<2> `pd.csi.storage.gke.io` specifies GCP CSI provisioner.
<3> Specifies using hyperdisk-balanced disks. To specify high availability hyperdisk-balanced disk, set the value to `hyperdisk-balanced-high-availability`.
<4> Specifies the throughput value in MiBps using the "Mi" qualifier. For example, if your required throughput is 250 MiBps, specify "250Mi". If you do not specify a value, the capacity is based upon the disk type default.
<5> Specifies the IOPS value without any qualifiers. For example, if you require 7,000 IOPS, specify "7000". If you do not specify a value, the capacity is based upon the disk type default.
<6> If using storage pools, specify a list of specific storage pools that you want to use in the format: projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME.
<7> If using storage pools, set `allowedTopologies` to restrict the topology of provisioned volumes to where the storage pool exists. In this example, `us-east4-c`.
--

. Create a persistent volume claim (PVC) that uses the hyperdisk-specific storage class using the following example YAML file:
+
.Example PVC YAML file
[source, yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: hyperdisk-sc <1>
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 2048Gi <2>
----
<1> PVC references the storage pool-specific storage class. In this example, `hyperdisk-sc`.
<2> Target storage capacity of the hyperdisk-balanced volume. In this example, `2048Gi`.

. Create a deployment that uses the PVC that you just created. Using a deployment helps ensure that your application has access to the persistent storage even after the pod restarts and rescheduling:

.. Ensure a node pool with the specified machine series is up and running before creating the deployment. Otherwise, the pod fails to schedule.

.. Use the following example YAML file to create the deployment:
+
.Example deployment YAML file
[source, yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      nodeSelector:
        cloud.google.com/machine-family: n4 <1>
      containers:
      - name: postgres
        image: postgres:14-alpine
        args: [ "sleep", "3600" ]
        volumeMounts:
        - name: sdk-volume
          mountPath: /usr/share/data/
      volumes:
      - name: sdk-volume
        persistentVolumeClaim:
          claimName: my-pvc <2>
----
<1> Specifies the machine family. In this example, it is `n4`.
<2> Specifies the name of the PVC created in the preceding step. In this example, it is `my-pfc`.

.. Confirm that the deployment was successfully created by running the following command:
+
[source, terminal]
----
$ oc get deployment
----
+
.Example output
[source, terminal]
----
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
postgres   0/1     1            0           42s
----
+
It might take a few minutes for hyperdisk instances to complete provisioning and display a READY status.

.. Confirm that PVC `my-pvc` has been successfully bound to a persistent volume (PV) by running the following command:
+
[source, terminal]
----
$ oc get pvc my-pvc
----
+
.Example output
+
[source, terminal]
----
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       VOLUMEATTRIBUTESCLASS  AGE
my-pvc        Bound    pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6   2Ti        RWO            hyperdisk-sc       <unset>                2m24s
----

.. Confirm the expected configuration of your hyperdisk-balanced disk:
+
[source, terminal]
----
$ gcloud compute disks list
----
+
.Example output
+
[source, terminal]
----
NAME                                        LOCATION        LOCATION_SCOPE  SIZE_GB  TYPE                STATUS
instance-20240914-173145-boot               us-central1-a   zone            150      pd-standard         READY
instance-20240914-173145-data-workspace     us-central1-a   zone            100      pd-balanced         READY
c4a-rhel-vm                                 us-central1-a   zone            50       hyperdisk-balanced  READY <1>
----
<1> Hyperdisk-balanced disk.

.. If using storage pools, check that the volume is provisioned as specified in your storage class and PVC by running the following command:
+
[source, terminal]
----
$ gcloud compute storage-pools list-disks pool-us-east4-c --zone=us-east4-c
----
+
.Example output
+
[source, terminal]
----
NAME                                      STATUS  PROVISIONED_IOPS  PROVISIONED_THROUGHPUT  SIZE_GB
pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6  READY   3000              140                     2048
----

[id="resources-for-gcp-c3-n4-instances"]
[role="_additional-resources"]
=== Additional resources
* Installing a cluster on GCP with customizations

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-pd-encrypted-pv_{context}"]
= Creating a custom-encrypted persistent volume

When you create a `PersistentVolumeClaim` object, OpenShift Container Platform provisions a new persistent volume (PV) and creates a `PersistentVolume` object. You can add a custom encryption key in Google Cloud Platform (GCP) to protect a PV in your cluster by encrypting the newly created PV.

For encryption, the newly attached PV that you create uses customer-managed encryption keys (CMEK) on a cluster by using a new or existing Google Cloud Key Management Service (KMS) key.

.Prerequisites
* You are logged in to a running OpenShift Container Platform cluster.
* You have created a Cloud KMS key ring and key version.

For more information about CMEK and Cloud KMS resources, see Using customer-managed encryption keys (CMEK).

.Procedure
To create a custom-encrypted PV, complete the following steps:

. Create a storage class with the Cloud KMS key. The following example enables dynamic provisioning of encrypted volumes:
+
[source,yaml]
--
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: csi-gce-pd-cmek
provisioner: pd.csi.storage.gke.io
volumeBindingMode: "WaitForFirstConsumer"
allowVolumeExpansion: true
parameters:
  type: pd-standard
  disk-encryption-kms-key: projects/<key-project-id>/locations/<location>/keyRings/<key-ring>/cryptoKeys/<key> <1>
--
<1> This field must be the resource identifier for the key that will be used to encrypt new disks. Values are case-sensitive. For more information about providing key ID values, see Retrieving a resource's ID and Getting a Cloud KMS resource ID.
+
[NOTE]
====
You cannot add the `disk-encryption-kms-key` parameter to an existing storage class. However, you can delete the storage class and recreate it with the same name and a different set of parameters. If you do this, the provisioner of the existing class must be `pd.csi.storage.gke.io`.
====

. Deploy the storage class on your OpenShift Container Platform cluster using the `oc` command:
+
[source,terminal]
--
$ oc describe storageclass csi-gce-pd-cmek
--
+
.Example output
[source,terminal]
--
Name:                  csi-gce-pd-cmek
IsDefaultClass:        No
Annotations:           None
Provisioner:           pd.csi.storage.gke.io
Parameters:            disk-encryption-kms-key=projects/key-project-id/locations/location/keyRings/ring-name/cryptoKeys/key-name,type=pd-standard
AllowVolumeExpansion:  true
MountOptions:          none
ReclaimPolicy:         Delete
VolumeBindingMode:     WaitForFirstConsumer
Events:                none
--

. Create a file named `pvc.yaml` that matches the name of your storage class object that you created in the previous step:
+
[source,yaml]
--
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: podpvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: csi-gce-pd-cmek
  resources:
    requests:
      storage: 6Gi
--
+
[NOTE]
====
If you marked the new storage class as default, you can omit the `storageClassName` field.
====

. Apply the PVC on your cluster:
+
[source,terminal]
--
$ oc apply -f pvc.yaml
--

. Get the status of your PVC and verify that it is created and bound to a newly provisioned PV:
+
[source,terminal]
--
$ oc get pvc
--
+
[source,terminal]
.Example output
--
NAME      STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
podpvc    Bound     pvc-e36abf50-84f3-11e8-8538-42010a800002   10Gi       RWO            csi-gce-pd-cmek  9s
--
+
[NOTE]
====
If your storage class has the `volumeBindingMode` field set to `WaitForFirstConsumer`, you must create a pod to use the PVC before you can verify it.
====

Your CMEK-protected PV is now ready to use with your OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-azure.adoc
// storage/container_storage_interface/persistent-storage-csi-ebs.adoc
// storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="byok_{context}"]
= User-managed encryption

The user-managed encryption feature allows you to provide keys during installation that encrypt OpenShift Container Platform node root volumes, and enables all managed storage classes to use these keys to encrypt provisioned storage volumes. You must specify the custom key in the `platform.<cloud_type>.defaultMachinePlatform` field in the install-config YAML file.

This features supports the following storage types:

* Amazon Web Services (AWS) Elastic Block storage (EBS)

* Microsoft Azure Disk storage

* Google Cloud Platform (GCP) persistent disk (PD) storage

* IBM Virtual Private Cloud (VPC) Block storage

For information about installing with user-managed encryption for GCP PD, see Installation configuration parameters.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-gcp-pd.adoc

[id="persistent-storage-csi-gcp-images-snapshot-class-overview_{context}"]
= Volume snapshot class csi-gce-pd-vsc-images

[role="_abstract"]
By default, you cannot restore more than six volumes per snapshot per hour. So in Kubevirt environments, you normally cannot create more than six VMs per hour from a "golden image" (templates saved as snapshots).

For Google Cloud Platform (GCP) persistent disk (PD) storage  CSI, there is a non-default `VolumeSnapshotClass`, named `csi-gce-pd-vsc-images`, that uses the `snapshot-type`: `images` parameter. When using KubeVirt, it allows you overcome the six VMs per hour restriction, so that you can create VMs from "golden images".

[NOTE]
====
Snapshots using the images snapshot class are strictly limited to ReadWriteOnce (RWO) sources, but you can restore them to ReadWriteMany (RWX)  hyperdisk-balanced disks.
====

For more information, see, under _Additional Resources_, Section _Volume snapshots CRD: VolumeSnapshotClass_.

[id="resources-for-gcp"]
[role="_additional-resources"]
== Additional resources
* Persistent storage using GCE Persistent Disk
* Configuring CSI volumes
* Volume snapshots CRD: VolumeSnapshotClass
