---
title: "Configuring CSI volumes"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi
version: 4.22
family: storage
documentKind: "Documentation"
---

# Configuring CSI volumes

[id="persistent-storage-csi"]
= Configuring CSI volumes

The Container Storage Interface (CSI) allows OpenShift Container Platform to consume
storage from storage back ends that implement the
CSI interface
as persistent storage.

[NOTE]
====
OpenShift Container Platform  supports version 1.6.0 of the CSI specification.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc

[id="persistent-storage-csi-architecture_{context}"]
= CSI architecture

CSI drivers are typically shipped as container images. These containers
are not aware of OpenShift Container Platform where they run. To use CSI-compatible
storage back end in OpenShift Container Platform, the cluster administrator must deploy
several components that serve as a bridge between OpenShift Container Platform and the
storage driver.

The following diagram provides a high-level overview about the components
running in pods in the OpenShift Container Platform cluster.

image::csi-arch-rev1.png["Architecture of CSI components"]

It is possible to run multiple CSI drivers for different storage back ends.
Each driver needs its own external controllers deployment and daemon set
with the driver and CSI registrar.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc

[id="external-csi-contollers_{context}"]
= External CSI controllers

External CSI controllers is a deployment that deploys one or more pods
with five containers:

* The snapshotter container watches `VolumeSnapshot` and `VolumeSnapshotContent` objects and is responsible for the creation and deletion of `VolumeSnapshotContent` object.
* The resizer container is a sidecar container that watches for `PersistentVolumeClaim` updates and triggers `ControllerExpandVolume` operations against a CSI endpoint if you request more storage on `PersistentVolumeClaim` object.
* An external CSI attacher container translates `attach` and `detach`
calls from OpenShift Container Platform to respective `ControllerPublish` and
`ControllerUnpublish` calls to the CSI driver.
* An external CSI provisioner container that translates `provision` and
`delete` calls from OpenShift Container Platform to respective `CreateVolume` and
`DeleteVolume` calls to the CSI driver.
* A CSI driver container.

The CSI attacher and CSI provisioner containers communicate with the CSI
driver container using UNIX Domain Sockets, ensuring that no CSI
communication leaves the pod. The CSI driver is not accessible from
outside of the pod.

[NOTE]
====
The `attach`, `detach`, `provision`, and `delete` operations typically require
the CSI driver to use credentials to the storage backend. Run the CSI
controller pods on infrastructure nodes so the credentials are never leaked
to user processes, even in the event of a catastrophic security breach
on a compute node.
====

[NOTE]
====
The external attacher must also run for CSI drivers that do not support
third-party `attach` or `detach` operations. The external attacher will
not issue any `ControllerPublish` or `ControllerUnpublish` operations to
the CSI driver. However, it still must run to implement the necessary
OpenShift Container Platform attachment API.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc

[id="csi-driver-daemonset_{context}"]
= CSI driver daemon set

The CSI driver daemon set runs a pod on every node that allows
OpenShift Container Platform to mount storage provided by the CSI driver to the node
and use it in user workloads (pods) as persistent volumes (PVs). The pod
with the CSI driver installed contains the following containers:

* A CSI driver registrar, which registers the CSI driver into the
`openshift-node` service running on the node. The `openshift-node` process
running on the node then directly connects with the CSI driver using the
UNIX Domain Socket available on the node.
* A CSI driver.

The CSI driver deployed on the node should have as few credentials to the
storage back end as possible. OpenShift Container Platform will only use the node plugin
set of CSI calls such as `NodePublish`/`NodeUnpublish` and
`NodeStage`/`NodeUnstage`, if these calls are implemented.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi.adoc

[id="persistent-storage-csi-drivers-supported_{context}"]
= CSI drivers supported by OpenShift Container Platform

[role="_abstract"]
OpenShift Container Platform installs certain CSI drivers by default, giving users storage options that are not possible with in-tree volume plugins.

To create CSI-provisioned persistent volumes that mount to these supported storage assets, OpenShift Container Platform installs the necessary CSI driver Operator, the CSI driver, and the required storage class by default. For more details about the default namespace of the Operator and driver, see the documentation for the specific CSI Driver Operator.

[IMPORTANT]
====
The AWS EFS and GCP Filestore CSI drivers are not installed by default, and must be installed manually. For instructions on installing the AWS EFS CSI driver, see Setting up AWS Elastic File Service CSI Driver Operator. For instructions on installing the GCP Filestore CSI driver, see Google Cloud Filestore CSI Driver Operator.
====

[IMPORTANT]
====
The AWS EFS driver is not installed by default, and must be installed manually. For instructions about installing the AWS EFS CSI driver, see "AWS Elastic File Service CSI Driver Operator" in the _Additional resources_ section.
====

The following table describes the CSI drivers that are
installed with OpenShift Container Platform,
supported by OpenShift Container Platform, and which CSI features they support, such as volume snapshots and resize.

[IMPORTANT]
====
If your CSI driver is not listed in the following table, you must follow the installation instructions provided by your CSI storage vendor to use their supported CSI features.
====

For a list of third-party-certified CSI drivers, see the _Red Hat ecosystem portal_ under _Additional resources_.

In addition to the drivers listed in the following table, OpenShift Container Platform functions with CSI drivers from third-party storage vendors. Red Hat does not oversee third-party provisioners or the connected CSI drivers and the vendors fully control source code, deployment, operation, and Kubernetes compatibility. These volume provisioners are considered customer-managed and the respective vendors are responsible for providing support. For more information, see the _Shared responsibilities for OpenShift Container Platform_ in the _Additional resources_ section.

.Supported CSI drivers and features in OpenShift Container Platform
[cols=",^v,^v,^v,^v,^v,^v,^v width="100%",options="header"]
|===
|CSI driver |CSI volume snapshots  |CSI volume group snapshots ^[1]^ |CSI cloning  |CSI resize |Inline ephemeral volumes |User namespaces
|AWS EBS | ✅ |  |  | ✅| |✅
|AWS EFS |  |  |  |  | |
|Google Compute Platform (GCP) persistent disk (PD)|  ✅|  |✅^[2]^ | ✅| |✅
|GCP Filestore | ✅ |  | | ✅| |
|{ibm-power-server-name} Block |   |  |   | ✅ | |✅
|{ibm-cloud-name} Block | ✅^[3]^ |  |   | ✅^[3]^| |✅
|{lvms} | ✅ |  | ✅ | ✅ | |✅
|Microsoft Azure Disk | ✅ |  | ✅ | ✅| |✅
|Microsoft Azure Stack Hub | ✅ |  | ✅ | ✅| |✅
|Microsoft Azure File | ✅  |  | ✅ | ✅| ✅ |
|OpenStack Cinder | ✅ |  | ✅ | ✅| |✅
|{rh-storage} | ✅ | ✅ | ✅ | ✅| |✅ ^[4]^
|OpenStack Manila | ✅ |  |   | ✅  | |
|CIFS/SMB |   |  | ✅  |   | |
|VMware vSphere | ✅^[5]^ |  |   | ✅^[6]^| |✅^[7]^
|===
--
1.

2.

* Cloning is not supported on hyperdisk-balanced disks with storage pools.

3.

* Does not support offline snapshots or resize. Volume must be attached to a running pod.

4.

* RBD supports user namespaces; CephFS does not.

5.

* Requires VMware vSphere version 8.0 Update 1 or later, or VMware vSphere Foundation (VVF) 9, or VMware Cloud Foundation (VCF) 9, for both vCenter Server and ESXi.

* Does not support fileshare volumes.

6.

* Online expansion is supported from VMware vSphere version 8.0 Update 1 and later, or VVF 9, or VCF 9.

7.

* File persistent volumes (PVs), such as vSAN file service, do not support user namespaces.
--

[role="_additional-resources"]
.Additional resources
* Red Hat ecosystem portal
* Third-party support policy

[role="_additional-resources"]
.Additional resources
* AWS Elastic File Service CSI Driver Operator

* Shared responsibilities for OpenShift Container Platform

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc

[id="csi-dynamic-provisioning_{context}"]
= Dynamic provisioning

Dynamic provisioning of persistent storage depends on the capabilities of
the CSI driver and underlying storage back end. The provider of the CSI
driver should document how to create a storage class in OpenShift Container Platform and
the parameters available for configuration.

The created storage class can be configured to enable dynamic provisioning.

.Procedure

* Create a default storage class that ensures all PVCs that do not require
any special storage class are provisioned by the installed CSI driver.
+
[source,shell]
----
# oc create -f - << EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class> <1>
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: <provisioner-name> <2>
parameters:
  csi.storage.k8s.io/fstype: xfs  <3>
EOF
----
<1> The name of the storage class that will be created.
<2> The name of the CSI driver that has been installed.
<3> The vSphere CSI driver supports all of the file systems supported by the underlying Red Hat Core operating system release, including XFS and Ext4.

// Module included in the following assemblies
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc

[id="csi-example-usage_{context}"]
= Example using the CSI driver

The following example installs a default MySQL template without any
changes to the template.

.Prerequisites

* The CSI driver has been deployed.
* A storage class has been created for dynamic provisioning.

.Procedure

* Create the MySQL template:
+
[source,terminal]
----
# oc new-app mysql-persistent
----
+
.Example output
[source,terminal]
----
--> Deploying template "openshift/mysql-persistent" to project default
...
----
+
[source,terminal]
----
# oc get pvc
----
+
.Example output
[source,terminal]
----
NAME              STATUS    VOLUME                                   CAPACITY
ACCESS MODES   STORAGECLASS   AGE
mysql             Bound     kubernetes-dynamic-pv-3271ffcb4e1811e8   1Gi
RWO            cinder         3s
----
.Example output
[source,terminal]
----
NAME           STATUS         VOLUME                                   CAPACITY
mysql          Bound          kubernetes-dynamic-pv-3271ffcb4e1811e8   1Gi

ACCESS MODES   STORAGECLASS   AGE
RWO            gp3-csi        3s
----
