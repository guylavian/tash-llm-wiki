---
title: "OpenStack Manila CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-manila
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-manila
version: 4.22
family: storage
documentKind: "Documentation"
---

# OpenStack Manila CSI Driver Operator

[id="persistent-storage-csi-manila"]
= OpenStack Manila CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) using the Container Storage Interface (CSI) driver for the OpenStack Manila shared file system service.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a Container Storage Interface (CSI) Operator and driver.

To create CSI-provisioned PVs that mount to Manila storage assets, OpenShift Container Platform installs the Manila CSI Driver Operator and the Manila CSI driver by default on any OpenStack cluster that has the Manila service enabled.

* The _Manila CSI Driver Operator_ creates the required storage class that is needed to create PVCs for all available Manila share types. The Operator is installed in the `openshift-cluster-csi-drivers` namespace.

* The _Manila CSI driver_ enables you to create and mount Manila PVs. The driver is installed in the `openshift-manila-csi-driver` namespace.

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
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc
//

[id="persistent-storage-csi-manila-limitations_{context}"]
= Manila CSI Driver Operator limitations

The following limitations apply to the Manila Container Storage Interface (CSI) Driver Operator:

Only NFS is supported:: OpenStack Manila supports many network-attached storage protocols, such as NFS, CIFS, and CEPHFS, and these can be selectively enabled in the OpenStack cloud. The Manila CSI Driver Operator in OpenShift Container Platform only supports using the NFS protocol. If NFS is not available and enabled in the underlying OpenStack cloud, you cannot use the Manila CSI Driver Operator to provision storage for OpenShift Container Platform.

Snapshots are not supported if the back end is CephFS-NFS:: To take snapshots of persistent volumes (PVs) and revert volumes to snapshots, you must ensure that the Manila share type that you are using supports these features. A Red Hat OpenStack administrator must enable support for snapshots (`share type extra-spec snapshot_support`) and for creating shares from snapshots (`share type extra-spec create_share_from_snapshot_support`) in the share type associated with the storage class you intend to use.

FSGroups are not supported:: Since Manila CSI provides shared file systems for access by multiple readers and multiple writers, it does not support the use of FSGroups. This is true even for persistent volumes created with the ReadWriteOnce access mode. It is therefore important not to specify the `fsType` attribute in any storage class that you manually create for use with Manila CSI Driver.

[IMPORTANT]
====
In Red Hat OpenStack Platform 16.x and 17.x, the Shared File Systems service (Manila) with CephFS through NFS fully supports serving shares to OpenShift Container Platform through the Manila CSI. However, this solution is not intended for massive scale. Be sure to review important recommendations in CephFS NFS Manila-CSI Workload Recommendations for Red Hat OpenStack Platform.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc

[id="persistent-storage-csi-manila-dynamic-provisioning_{context}"]
= Dynamically provisioning Manila CSI volumes

OpenShift Container Platform installs a storage class for each available Manila share type.

The YAML files that are created are completely decoupled from Manila and from its Container Storage Interface (CSI) plugin. As an application developer, you can dynamically provision ReadWriteMany (RWX) storage and deploy pods with applications that safely consume the storage using YAML manifests.

You can use the same pod and persistent volume claim (PVC) definitions on-premise that you use with OpenShift Container Platform on AWS, {gcp-short}, Azure, and other platforms, with the exception of the storage class reference in the PVC definition.

[IMPORTANT]
====
By default, the access rule that is assigned to a volume is `0.0.0.0/0`, which allows access from all IPv4 clients. To limit client access, create custom storage classes that use specific client IP addresses or subnets. For more information, see Section _Customizing Manila share access rules_.
====

[NOTE]
====
Manila service is optional. If the service is not enabled in {rh-openstack-first}, the Manila CSI driver is not installed and the storage classes for Manila are not created.
====

.Prerequisites

* {rh-openstack} is deployed with appropriate Manila share infrastructure so that it can be used to dynamically provision and mount volumes in OpenShift Container Platform.

.Procedure (UI)

To dynamically create a Manila CSI volume using the web console:

. In the OpenShift Container Platform console, click *Storage* → *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume Claim*.

. Define the required options on the resulting page.

.. Select the appropriate storage class.

.. Enter a unique name for the storage claim.

.. Select the access mode to specify read and write access for the PVC you are creating.
+
[IMPORTANT]
====
Use RWX if you want the PV that fulfills this PVC to be mounted to multiple pods on multiple nodes in the cluster.
====

. Define the size of the storage claim.

. Click *Create* to create the PVC and generate a PV.

.Procedure (CLI)

To dynamically create a Manila CSI volume using the command-line interface (CLI):

. Create and save a file with the `PersistentVolumeClaim` object described by the following YAML:

+
.pvc-manila.yaml
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-manila
spec:
  accessModes: <1>
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  storageClassName: csi-manila-gold <2>
----
+
<1> Use RWX if you want the PV that fulfills this PVC to be mounted to multiple pods on multiple nodes in the cluster.
<2> The name of the storage class that provisions the storage back end. Manila storage classes are provisioned by the Operator and have the `csi-manila-` prefix.

. Create the object you saved in the previous step by running the following command:
+
[source,terminal]
----
$ oc create -f pvc-manila.yaml
----
+
A new PVC is created.

. To verify that the volume was created and is ready, run the following command:
+
[source,terminal]
----
$ oc get pvc pvc-manila
----
+
The `pvc-manila` shows that it is `Bound`.

You can now use the new PVC to configure a pod.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-manila.adoc

[id="persistent-storage-csi-manila-share-access-rules_{context}"]
= Customizing Manila share access rules

By default, OpenShift Container Platform creates Manila storage classes that provide access to all IPv4 clients. To limit client access, you can define custom storage classes that use specific client IP addresses or subnets by using the `nfs-ShareClient` parameter.

[IMPORTANT]
====
When using custom storage classes with restricted access rules, ensure that:

* The specified IP addresses or subnets include all OpenShift Container Platform nodes that need to access the storage.

* The Manila service in {rh-openstack} supports the share type specified in the storage class.

* Network connectivity exists between the allowed clients and the Manila share servers.
====

.Prerequisites

* {rh-openstack-first} is deployed with appropriate Manila share infrastructure.
* Access to a cluster with administrator privileges.

.Procedure

. Create a YAML file for your custom storage class based on the following example:
+
.Example custom storage class file
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: csi-manila-gold-restricted <1>
provisioner: manila.csi.openstack.org
parameters:
  type: gold <2>
  nfs-ShareClient: "10.0.0.0/24,192.168.1.100" <3>
  csi.storage.k8s.io/provisioner-secret-name: manila-csi-secret
  csi.storage.k8s.io/provisioner-secret-namespace: openshift-manila-csi-driver
  csi.storage.k8s.io/controller-expand-secret-name: manila-csi-secret
  csi.storage.k8s.io/controller-expand-secret-namespace: openshift-manila-csi-driver
  csi.storage.k8s.io/node-stage-secret-name: manila-csi-secret
  csi.storage.k8s.io/node-stage-secret-namespace: openshift-manila-csi-driver
  csi.storage.k8s.io/node-publish-secret-name: manila-csi-secret
  csi.storage.k8s.io/node-publish-secret-namespace: openshift-manila-csi-driver
allowVolumeExpansion: true
----
<1> Descriptive name for your custom storage class.
<2> The Manila share type. This type must match an existing share type in your {rh-openstack} environment.
<3> Comma-separated list of IP addresses or CIDR subnets allowed to access the NFS shares. The `nfs-ShareClient` parameter accepts various formats:
+
** Single IP address: `192.168.1.100`
** CIDR subnet: `10.0.0.0/24`
** Multiple entries: `10.0.0.0/24,192.168.1.100,172.16.0.0/16`
+
Ensure that the specified IP addresses or subnets include the OpenShift Container Platform cluster nodes to allow proper mounting of the persistent volumes.
+
In this example, access is restricted to the `10.0.0.0/24` subnet, and the specific IP address is `192.168.1.100`.

. Apply the storage class from the file by running the following command:
+
[source,terminal]
----
$ oc apply -f custom-manila-storageclass.yaml
----

. Verify that the storage class was created by running the following command:
+
[source,terminal]
----
$ oc get storageclass csi-manila-gold-restricted
----
+
.Example output
[source,terminal]
----
NAME                 		    PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
csi-manila-gold-restricted	manila.csi.openstack.org   Delete          Immediate           true                   43m
----

. Create a persistent volume claim (PVC) that uses the custom storage class based on the following example:
+
.Example PVC file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-manila-restricted
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  storageClassName: csi-manila-gold-restricted <1>
----
<1> The name of your custom storage class that has restricted access. In this example, the name is `csi-manila-gold-restricted`.

. Apply the PVC from the file by running the following command:
+
[source,terminal]
----
$ oc apply -f pvc-manila-restricted.yaml
----

[role="_additional-resources"]
.Additional resources
* Configuring CSI volumes
