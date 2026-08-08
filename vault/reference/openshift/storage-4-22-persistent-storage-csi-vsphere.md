---
title: "VMware vSphere CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-vsphere
version: 4.22
family: storage
documentKind: "Documentation"
---

# VMware vSphere CSI Driver Operator

[id="persistent-storage-vsphere"]
= VMware vSphere CSI Driver Operator

== Overview

[role="_abstract"]
OpenShift Container Platform can provision persistent volumes (PVs) using the Container Storage Interface (CSI) VMware vSphere driver for Virtual Machine Disk (VMDK) volumes.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned persistent volumes (PVs) that mount to vSphere storage assets, OpenShift Container Platform installs the vSphere CSI Driver Operator and the vSphere CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* *vSphere CSI Driver Operator*: The Operator provides a storage class, called `thin-csi`, that you can use to create persistent volumes claims (PVCs). The vSphere CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage. You can disable this default storage class if desired (see Managing the default storage class).

* *vSphere CSI driver*: The driver enables you to create and mount vSphere PVs. In OpenShift Container Platform 4.20, the driver version is 3.6.0 The vSphere CSI driver supports all of the file systems supported by the underlying Red Hat Core operating system release, including XFS and Ext4. For more information about supported file systems, see Overview of available file systems.

//Please update driver version as needed with each major OCP release starting with 4.13.

//Listing the VMWare driver version here because it has a more variable set of features. The Operator version does not change independently (is parallel).

[NOTE]
====
For new installations, OpenShift Container Platform 4.13 and later provides automatic migration for the vSphere in-tree volume plugin to its equivalent CSI driver. Updating to OpenShift Container Platform 4.15 and later also provides automatic migration. For more information about updating and migration, see CSI automatic migration.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes.
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
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-limitations_{context}"]
= vSphere CSI limitations

The following limitations apply to the vSphere Container Storage Interface (CSI) Driver Operator:

* The vSphere CSI Driver supports dynamic and static provisioning. However, when using static provisioning in the PV specifications, do not use the key `storage.kubernetes.io/csiProvisionerIdentity` in `csi.volumeAttributes` because this key indicates dynamically provisioned PVs.

* OpenShift Container Platform does not support restoring volume snapshots in a topology domain that does not have access to the datastore where the snapshot resides. You must manually schedule pods that use a persistent volume claim (PVC) that restore a snapshot to a region and zone with the snapshot. Using a shared datastore across all regions and zones meets this requirement.

// Module included in the following assemblies:
//
// persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-stor-policy_{context}"]
= vSphere storage policy

The vSphere CSI Driver Operator storage class uses vSphere's storage policy. OpenShift Container Platform automatically creates a storage policy that targets datastore configured in cloud configuration:
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: thin-csi
provisioner: csi.vsphere.vmware.com
parameters:
  StoragePolicyName: "$openshift-storage-policy-xxxx"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: false
reclaimPolicy: Delete
----

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-rwx_{context}"]
= ReadWriteMany vSphere volume support

If the underlying vSphere environment supports the vSAN file service, then vSphere Container Storage Interface (CSI) Driver Operator installed by
OpenShift Container Platform supports provisioning of ReadWriteMany (RWX) volumes. If vSAN file service is not configured, then ReadWriteOnce (RWO) is the only access mode available. If you do not have vSAN file service configured, and you request RWX, the volume fails to get created and an error is logged.

For more information about configuring the vSAN file service in your environment, see https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-82565B82-C911-42F7-85B1-E9EF973EE90C.html[vSAN File Service].

You can request RWX volumes by making the following persistent volume claim (PVC):

[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  resources:
    requests:
      storage: 1Gi
  accessModes:
     - ReadWriteMany
  storageClassName: thin-csi
----

Requesting a PVC of the RWX volume type should result in provisioning of persistent volumes (PVs) backed by the vSAN file service.

// Module included in the following assemblies for vSphere:
//
// * installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.adoc
// * installing/installing_vsphere/upi/upi-vsphere-installation-reqs.adoc
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc

[id="vsphere-csi-driver-reqs_{context}"]
= VMware vSphere CSI Driver Operator requirements

To install the vSphere Container Storage Interface (CSI) Driver Operator, the following requirements must be met:

* VMware vSphere version 8.0 Update 1 or later; or VMware vSphere Foundation (VVF) 9; or VMware Cloud Foundation (VCF) 5 or later
* vCenter version 8.0 Update 1 or later; or VVF 9; or VCF 5 or later
* Virtual machines of hardware version 15 or later
* No third-party vSphere CSI driver already installed in the cluster

If a third-party vSphere CSI driver is present in the cluster, OpenShift Container Platform does not overwrite it. The presence of a third-party vSphere CSI driver prevents OpenShift Container Platform from updating to OpenShift Container Platform 4.13 or later.

[NOTE]
====
The VMware vSphere CSI Driver Operator is supported only on clusters deployed with `platform: vsphere` in the installation manifest.
====

You can create a custom role for the Container Storage Interface (CSI) driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator. The custom role can include privilege sets that assign a minimum set of permissions to each vSphere object. This means that the CSI driver, the vSphere CSI Driver Operator, and the vSphere Problem Detector Operator can establish a basic interaction with these objects.

[IMPORTANT]
====
Installing an OpenShift Container Platform cluster in a vCenter is tested against a full list of privileges as described in the "Required vCenter account privileges" section. By adhering to the full list of privileges, you can reduce the possibility of unexpected and unsupported behaviors that might occur when creating a custom role with a set of restricted privileges.
====

To remove a third-party CSI driver, see Removing a third-party vSphere CSI Driver.

// Module included in the following assemblies:
//
// persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-install-issues_{context}"]
= Removing a third-party vSphere CSI Driver Operator

OpenShift Container Platform 4.10, and later, includes a built-in version of the vSphere Container Storage Interface (CSI) Operator Driver that is supported by Red Hat. If you have installed a vSphere CSI driver provided by the community or another vendor, updates to the next major version of OpenShift Container Platform, such as 4.13, or later, might be disabled for your cluster.

OpenShift Container Platform 4.12, and later, clusters are still fully supported, and updates to z-stream releases of 4.12, such as 4.12.z, are not blocked, but you must correct this state by removing the third-party vSphere CSI Driver before updates to next major version of OpenShift Container Platform can occur. Removing the third-party vSphere CSI driver does not require deletion of associated persistent volume (PV) objects, and no data loss should occur.

[NOTE]
====
These instructions may not be complete, so consult the vendor or community provider uninstall guide to ensure removal of the driver and components.
====

To uninstall the third-party vSphere CSI Driver:

. Delete the third-party vSphere CSI Driver (VMware vSphere Container Storage Plugin) Deployment and Daemonset objects.
. Delete the configmap and secret objects that were installed previously with the third-party vSphere CSI Driver.
. Delete the third-party vSphere CSI driver `CSIDriver` object:
+
[source,terminal]
----
$ oc delete CSIDriver csi.vsphere.vmware.com
----
+
[source,terminal]
----
csidriver.storage.k8s.io "csi.vsphere.vmware.com" deleted
----

After you have removed the third-party vSphere CSI Driver from the OpenShift Container Platform cluster, installation of Red Hat's vSphere CSI Driver Operator automatically resumes, and any conditions that could block upgrades to OpenShift Container Platform 4.11, or later, are automatically removed. If you had existing vSphere CSI PV objects, their lifecycle is now managed by Red Hat's vSphere CSI Driver Operator.

[id="vsphere-pv-encryption"]
== vSphere persistent disks encryption

You can encrypt virtual machines (VMs) and dynamically provisioned persistent volumes (PVs) on OpenShift Container Platform running on top of vSphere.

[NOTE]
====
OpenShift Container Platform does not support RWX-encrypted PVs. You cannot request RWX PVs out of a storage class that uses an encrypted storage policy.
====

You must encrypt VMs before you can encrypt PVs, which you can do during or after installation.

For information about encrypting VMs, see:

* Requirements for encrypting virtual machines

* During installation: Step 7 of Installing RHCOS and starting the OpenShift Container Platform bootstrap process

* Enabling encryption on a vSphere cluster

After encrypting VMs, you can configure a storage class that supports dynamic encryption volume provisioning using the vSphere Container Storage Interface (CSI) driver. This can be accomplished in one of two ways using:

* Datastore URL: This approach is not very flexible, and forces you to use a single datastore. It also does not support topology-aware provisioning.

* Tag-based placement: Encrypts the provisioned volumes and uses tag-based placement to target specific datastores.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-encryption-datastore-url_{context}"]
= Using datastore URL

.Procedure

To encrypt using the datastore URL:

. Find out the name of the default storage policy in your datastore that supports encryption.
+
This is same policy that was used for encrypting your VMs.

. Create a storage class that uses this storage policy:
+
[source, yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: encryption
provisioner: csi.vsphere.vmware.com
parameters:
 storagePolicyName: <storage-policy-name> <1>
 datastoreurl: "ds:///vmfs/volumes/vsan:522e875627d-b090c96b526bb79c/"
----
<1> Name of default storage policy in your datastore that supports encryption

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-encryption-tag-based_{context}"]
= Using tag-based placement

.Procedure

To encrypt using tag-based placement:

. In vCenter create a category for tagging datastores that will be made available to this storage class. Also, ensure that *StoragePod(Datastore clusters)*, *Datastore*, and *Folder* are selected as Associable Entities for the created category.

. In vCenter, create a tag that uses the category created earlier.

. Assign the previously created tag to each datastore that will be made available to the storage class. Make sure that datastores are shared with hosts participating in the OpenShift Container Platform cluster.

. In vCenter, from the main menu, click *Policies and Profiles*.

. On the *Policies and Profiles* page, in the navigation pane, click *VM Storage Policies*.

. Click *CREATE*.

. Type a name for the storage policy.

. Select *Enable host based rules* and *Enable tag based placement rules*.

. In the *Next* tab:

.. Select *Encryption* and *Default Encryption Properties*.

.. Select the tag category created earlier, and select tag selected. Verify that the policy is selecting matching datastores.

. Create the storage policy.

. Create a storage class that uses the storage policy:
+
[source, yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name:  csi-encrypted
provisioner: csi.vsphere.vmware.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
parameters:
 storagePolicyName: <storage-policy-name> <1>
----
<1> Name of the storage policy that you created for encryption

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-multi-vcenter-support-overview_{context}"]
= Multiple vCenter support for vSphere CSI

Deploying OpenShift Container Platform across multiple vSphere vCenter clusters without shared storage for high availability can be helpful. OpenShift Container Platform v4.17, and later, supports this capability.

[NOTE]
====
Multiple vCenters can only be configured *during* installation. Multiple vCenters *cannot* be configured after installation.
====

The maximum number of supported vCenter clusters is three.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-multi-vcenter-support-procedure-install_{context}"]
= Configuring multiple vCenters during installation

To configure multiple vCenters during installation:

* Specify multiple vSphere clusters during installation. For information, see "Installation configuration parameters for vSphere".

[role="_additional-resources"]
.Additional resources
[id="link_installation_config_parameters_vsphere"]
* Installation configuration parameters for vSphere.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-top-aware-overview_{context}"]
= vSphere CSI topology overview

OpenShift Container Platform provides the ability to deploy OpenShift Container Platform for vSphere on different zones and regions, which allows you to deploy over multiple compute clusters and data centers, thus helping to avoid a single point of failure.

This is accomplished by defining zone and region categories in vCenter, and then assigning these categories to different failure domains, such as a compute cluster, by creating tags for these zone and region categories. After you have created the appropriate categories, and assigned tags to vCenter objects, you can create additional machinesets that create virtual machines (VMs) that are responsible for scheduling pods in those failure domains.

The following example defines two failure domains with one region and two zones:

.vSphere storage topology with one region and two zones
|===
|Compute cluster | Failure domain |Description

|Compute cluster: ocp1,
Data center: Atlanta
|openshift-region: us-east-1 (tag), openshift-zone: us-east-1a (tag)
|This defines a failure domain in region us-east-1 with zone us-east-1a.

|Computer cluster: ocp2,
Data center: Atlanta
|openshift-region: us-east-1 (tag), openshift-zone: us-east-1b (tag)
|This defines a different failure domain within the same region called us-east-1b.
|===

== vSphere CSI topology requirements
The following guidelines are recommended for vSphere CSI topology:

* You are strongly recommended to add topology tags to data centers and compute clusters, and *not* to hosts.
+
`vsphere-problem-detector` provides alerts if the `openshift-region` or `openshift-zone` tags are not defined at the data center or compute cluster level, and each topology tag (`openshift-region` or `openshift-zone`) should occur only once in the hierarchy.
+
[NOTE]
====
Ignoring this recommendation only results in a log warning from the CSI driver and duplicate tags lower in the hierarchy, such as hosts, are ignored; VMware considers this an invalid configuration, and therefore to prevent problems you should not use it.
====

* Volume provisioning requests in topology-aware environments attempt to create volumes in datastores accessible to all hosts under a given topology segment. This includes hosts that do not have Kubernetes node VMs running on them. For example, if the vSphere Container Storage Plug-in driver receives a request to provision a volume in `zone-a`, applied on the data center `dc-1`, all hosts under `dc-1` must have access to the datastore selected for volume provisioning. The hosts include those that are directly under `dc-1`, and those that are a part of clusters inside `dc-1`.

* For additional recommendations, you should read the VMware https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/3.0/vmware-vsphere-csp-getting-started/GUID-162E7582-723B-4A0F-A937-3ACE82EAFD31.html[Guidelines and Best Practices for Deployment with Topology] section.

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-top-aware-during-install_{context}"]
= Creating vSphere storage topology during installation

== Procedure

* Specify the topology during installation. See the _Configuring regions and zones for a VMware vCenter_ section.

No additional action is necessary and the default storage class that is created by OpenShift Container Platform
is topology aware and should allow provisioning of volumes in different failure domains.

[role="_additional-resources"]
.Additional resources
* Configuring regions and zones for a VMware vCenter

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-top-aware-post-install_{context}"]
= Creating vSphere storage topology postinstallation

== Procedure
. In the VMware vCenter vSphere client GUI, define appropriate zone and region catagories and tags.
+
While vSphere allows you to create categories with any arbitrary name, OpenShift Container Platform strongly recommends use of `openshift-region` and `openshift-zone` names for defining topology categories.
+
For more information about vSphere categories and tags, see the VMware vSphere documentation.

. In OpenShift Container Platform, create failure domains. See the _Specifying multiple regions and zones for your cluster on vSphere_ section.

. Create a tag to assign to datastores across failure domains:
+
When an OpenShift Container Platform spans more than one failure domain, the datastore might not be shared across those failure domains, which is where topology-aware provisioning of persistent volumes (PVs) is useful.
+
.. In vCenter, create a category for tagging the datastores. For example, `openshift-zonal-datastore-cat`. You can use any other category name, provided the category uniquely is used for tagging datastores participating in OpenShift Container Platform cluster. Also, ensure that `StoragePod`, `Datastore`, and `Folder` are selected as Associable Entities for the created category.
.. In vCenter, create a tag that uses the previously created category. This example uses the tag name `openshift-zonal-datastore`.
.. Assign the previously created tag (in this example `openshift-zonal-datastore`) to each datastore in a failure domain that would be considered for dynamic provisioning.
+
[NOTE]
====
You can use any names you like for datastore categories and tags. The names used in this example are provided as recommendations. Ensure that the tags and categories that you define uniquely identify only datastores that are shared with all hosts in the OpenShift Container Platform cluster.
====

. As needed, create a storage policy that targets the tag-based datastores in each failure domain:
.. In vCenter, from the main menu, click *Policies and Profiles*.
.. On the *Policies and Profiles* page, in the navigation pane, click *VM Storage Policies*.
.. Click *CREATE*.
.. Type a name for the storage policy.
.. For the rules, choose Tag Placement rules and select the tag and category that targets the desired datastores (in this example, the `openshift-zonal-datastore` tag).
+
The datastores are listed in the storage compatibility table.

. Create a new storage class that uses the new zoned storage policy:
.. Click *Storage* > *StorageClasses*.
.. On the *StorageClasses* page, click *Create StorageClass*.
.. Type a name for the new storage class in *Name*.
.. Under *Provisioner*, select *csi.vsphere.vmware.com*.
.. Under *Additional parameters*, for the StoragePolicyName parameter, set *Value* to the name of the new zoned storage policy that you created earlier.
.. Click *Create*.
+
.Example output
+
[source, yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: zoned-sc <1>
provisioner: csi.vsphere.vmware.com
parameters:
  StoragePolicyName: zoned-storage-policy <2>
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
----
<1> New topology aware storage class name.
<2> Specify zoned storage policy.
+
[NOTE]
====
You can also create the storage class by editing the preceding YAML file and running the command `oc create -f $FILE`.
====

[role="_additional-resources"]
.Additional resources
* Specifying multiple regions and zones for your cluster on vSphere
* https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-vcenter-esxi-management/GUID-16422FF7-235B-4A44-92E2-532F6AED0923.html?hWord=N4IghgNiBcIC5gOYgL5A[VMware vSphere tag documentation]

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-top-aware-infra-top_{context}"]
= Creating vSphere storage topology without an infra topology

[NOTE]
====
OpenShift Container Platform recommends using the infrastructure object for specifying failure domains in a topology aware setup. Specifying failure domains in the infrastructure object and specify topology-categories in the `ClusterCSIDriver` object at the same time is an unsupported operation.
====

== Procedure
. In the VMware vCenter vSphere client GUI, define appropriate zone and region catagories and tags.
+
While vSphere allows you to create categories with any arbitrary name, OpenShift Container Platform strongly recommends use of `openshift-region` and `openshift-zone` names for defining topology.
+
For more information about vSphere categories and tags, see the VMware vSphere documentation.

. To allow the container storage interface (CSI) driver to detect this topology, edit the `clusterCSIDriver` object YAML file `driverConfig` section:
* Specify the `openshift-zone` and `openshift-region` categories that you created earlier.
* Set `driverType` to `vSphere`.
+
[source,terminal]
----
~ $ oc edit clustercsidriver csi.vsphere.vmware.com -o yaml
----
+
.Example output
+
[source,terminal]
----
apiVersion: operator.openshift.io/v1
kind: ClusterCSIDriver
metadata:
  name: csi.vsphere.vmware.com
spec:
  logLevel: Normal
  managementState: Managed
  observedConfig: null
  operatorLogLevel: Normal
  unsupportedConfigOverrides: null
  driverConfig:
    driverType: vSphere <1>
      vSphere:
        topologyCategories: <2>
        - openshift-zone
        - openshift-region
----
<1> Ensure that `driverType` is set to `vSphere`.
<2> `openshift-zone` and `openshift-region` categories created earlier in vCenter.

. Verify that `CSINode` object has topology keys by running the following commands:
+
[source,terminal]
----
~ $ oc get csinode
----
+
.Example output
+
[source,terminal]
----
NAME DRIVERS AGE
co8-4s88d-infra-2m5vd 1 27m
co8-4s88d-master-0 1 70m
co8-4s88d-master-1 1 70m
co8-4s88d-master-2 1 70m
co8-4s88d-worker-j2hmg 1 47m
co8-4s88d-worker-mbb46 1 47m
co8-4s88d-worker-zlk7d 1 47m
----
+
[source,terminal]
----
~ $ oc get csinode co8-4s88d-worker-j2hmg -o yaml
----
+
.Example output
+
[source,terminal]
----
...
spec:
  drivers:
  - allocatable:
      count: 59
  name: csi-vsphere.vmware.com
  nodeID: co8-4s88d-worker-j2hmg
  topologyKeys: <1>
  - topology.csi.vmware.com/openshift-zone
  - topology.csi.vmware.com/openshift-region
----
<1> Topology keys from vSphere `openshift-zone` and `openshift-region` catagories.
+
[NOTE]
=====
`CSINode` objects might take some time to receive updated topology information. After the driver is updated, `CSINode` objects should have topology keys in them.
=====

. Create a tag to assign to datastores across failure domains:
+
When an OpenShift Container Platform spans more than one failure domain, the datastore might not be shared across those failure domains, which is where topology-aware provisioning of persistent volumes (PVs) is useful.
+
.. In vCenter, create a category for tagging the datastores. For example, `openshift-zonal-datastore-cat`. You can use any other category name, provided the category uniquely is used for tagging datastores participating in OpenShift Container Platform cluster. Also, ensure that `StoragePod`, `Datastore`, and `Folder` are selected as Associable Entities for the created category.
.. In vCenter, create a tag that uses the previously created category. This example uses the tag name `openshift-zonal-datastore`.
.. Assign the previously created tag (in this example `openshift-zonal-datastore`) to each datastore in a failure domain that would be considered for dynamic provisioning.
+
[NOTE]
====
You can use any names you like for categories and tags. The names used in this example are provided as recommendations. Ensure that the tags and categories that you define uniquely identify only datastores that are shared with all hosts in the OpenShift Container Platform cluster.
====

. Create a storage policy that targets the tag-based datastores in each failure domain:
.. In vCenter, from the main menu, click *Policies and Profiles*.
.. On the *Policies and Profiles* page, in the navigation pane, click *VM Storage Policies*.
.. Click *CREATE*.
.. Type a name for the storage policy.
.. For the rules, choose Tag Placement rules and select the tag and category that targets the desired datastores (in this example, the `openshift-zonal-datastore` tag).
+
The datastores are listed in the storage compatibility table.

. Create a new storage class that uses the new zoned storage policy:
.. Click *Storage* > *StorageClasses*.
.. On the *StorageClasses* page, click *Create StorageClass*.
.. Type a name for the new storage class in *Name*.
.. Under *Provisioner*, select *csi.vsphere.vmware.com*.
.. Under *Additional parameters*, for the StoragePolicyName parameter, set *Value* to the name of the new zoned storage policy that you created earlier.
.. Click *Create*.
+
.Example output
+
[source, yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: zoned-sc <1>
provisioner: csi.vsphere.vmware.com
parameters:
  StoragePolicyName: zoned-storage-policy <2>
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
----
<1> New topology aware storage class name.
<2> Specify zoned storage policy.
+
[NOTE]
====
You can also create the storage class by editing the preceding YAML file and running the command `oc create -f $FILE`.
====

[role="_additional-resources"]
.Additional resources
* https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-vcenter-esxi-management/GUID-16422FF7-235B-4A44-92E2-532F6AED0923.html?hWord=N4IghgNiBcIC5gOYgL5A[VMware vSphere tag documentation]

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-top-aware-results_{context}"]
= Results

Creating persistent volume claims (PVCs) and PVs from the topology aware storage class are truly zonal, and should use the datastore in their respective zone depending on how pods are scheduled:

[source,terminal]
----
$ oc get pv <pv_name> -o yaml
----

.Example output

[source,terminal]
----
...
nodeAffinity:
  required:
    nodeSelectorTerms:
    - matchExpressions:
      - key: topology.csi.vmware.com/openshift-zone <1>
        operator: In
        values:
        - <openshift_zone>
      - key: topology.csi.vmware.com/openshift-region <1>
        operator: In
        values:
        - <openshift_region>
...
peristentVolumeclaimPolicy: Delete
storageClassName: <zoned_storage_class_name> <2>
volumeMode: Filesystem
...
----
<1> PV has zoned keys.
<2> PV is using the zoned storage class.

// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-vsphere.adoc
// * storage/persistent_storage/persistent-storage-csi-snapshots.adoc

[id="vsphere-change-max-snapshot_{context}"]
= Changing the maximum number of snapshots for vSphere

The default maximum number of snapshots per volume in vSphere Container Storage Interface (CSI) is 3. You can change the maximum number up to 32 per volume.

However, be aware that increasing the snapshot maximum involves a performance trade off, so for better performance use only 2 to 3 snapshots per volume.

For more VMware snapshot performance recommendations, see *_Additional resources_*.

.Prerequisites

* Access to the cluster with administrator rights.

.Procedure

. Check the current secret by the running the following command:
+
[source, terminal]
----
$ oc -n openshift-cluster-csi-drivers get secret/vsphere-csi-config-secret -o jsonpath='{.data.cloud\.conf}' | base64 -d
----
+
.Example output
+
[source, terminal]
----
# Labels with topology values are added dynamically via operator
[Global]
cluster-id = vsphere-01-cwv8p

# Populate VCenters (multi) after here
[VirtualCenter "vcenter.openshift.com"]
insecure-flag           = true
datacenters             = DEVQEdatacenter
password                = "xxxxxxxx"
user                    = "xxxxxxxx@devcluster.openshift.com"
migration-datastore-url = ds:///vmfs/volumes/vsan:52c842f232751e0d-3253aadeac21ca82/
----
+
In this example, the global maximum number of snapshots is not configured, so the default value of 3 is applied.

. Change the snapshot limit by running the following command:
+
* Set *global* snapshot limit:
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"globalMaxSnapshotsPerBlockVolume": 10}}}}'

clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the global limit is being changed to 10 (`globalMaxSnapshotsPerBlockVolume` set to 10).

* Set *Virtual Volume* snapshot limit:
+
This parameter sets the limit on the Virtual Volumes datastore only. The Virtual Volume maximum snapshot limit overrides the global constraint if set, but defaults to the global limit if it is not set.
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"granularMaxSnapshotsPerBlockVolumeInVVOL": 5}}}}'
clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the Virtual Volume limit is being changed to 5 (`granularMaxSnapshotsPerBlockVolumeInVVOL` set to 5).

* Set *vSAN* snapshot limit:
+
This parameter sets the limit on the vSAN datastore only. The vSAN maximum snapshot limit overrides the global constraint if set, but defaults to the global limit if it is not set. You can set a maximum value of 32 under vSAN ESA setup.
+
[source, terminal]
----
$ oc patch clustercsidriver/csi.vsphere.vmware.com --type=merge -p '{"spec":{"driverConfig":{"vSphere":{"granularMaxSnapshotsPerBlockVolumeInVSAN": 7}}}}'
clustercsidriver.operator.openshift.io/csi.vsphere.vmware.com patched
----
+
In this example, the vSAN limit is being changed to 7 (`granularMaxSnapshotsPerBlockVolumeInVSAN` set to 7).

.Verification

* Verify that any changes you made are reflected in the config map by running the following command:
+
[source, terminal]
----
$ oc -n openshift-cluster-csi-drivers get secret/vsphere-csi-config-secret -o jsonpath='{.data.cloud\.conf}' | base64 -d
----
+
.Example output
+
[source, terminal]
----
# Labels with topology values are added dynamically via operator
[Global]
cluster-id = vsphere-01-cwv8p

# Populate VCenters (multi) after here
[VirtualCenter "vcenter.openshift.com"]
insecure-flag           = true
datacenters             = DEVQEdatacenter
password                = "xxxxxxxx"
user                    = "xxxxxxxx@devcluster.openshift.com"
migration-datastore-url = ds:///vmfs/volumes/vsan:52c842f232751e0d-3253aadeac21ca82/

[Snapshot]
global-max-snapshots-per-block-volume = 10 <1>
----
<1> `global-max-snapshots-per-block-volume` is now set to 10.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-migrating-cns-vols-between-datastores_{context}"]
= Migrating CNS volumes between datastores for vSphere

If you are running out of space in your current datastore, or want to move to a more performant datastore, you can migrate VMware vSphere Cloud Native Storage (CNS) volumes between datastores. This applies to both attached and detached volumes.

.Limitations
* Requires VMware vSphere 8.0.2 or later, or VMware vSphere Foundation (VVF) 9, or VMware Cloud Foundation (VCF) 9

* Only one volume can be migrated at a time.

* RWX volumes are not supported.

* CNS volume should only be migrated to a datastore that is shared with all hosts that make up the OpenShift Container Platform cluster.

* Migrating volumes between different datastore in different datacenters is not supported.

* VMware HCX is not supported.

.Additional limitations
* For vSphere 8

* For VCF 9

For more general information, see:

* For vSphere v8.0

* For VCF 9

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-disable-storage-overview_{context}"]
= Disabling and enabling storage on vSphere

Cluster administrators might want to disable the VMware vSphere Container Storage Interface (CSI) Driver as a Day 2 operation, so the vSphere CSI Driver does not interface with your vSphere setup.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-disable-storage-consequences_{context}"]
= Consequences of disabling and enabling storage on vSphere

The consequences of disabling and enabling storage on vSphere are described in the following table.

.Consequences of disabling/enabling storage on vSphere
|===
|Disabling | Enabling

a| * vSphere CSI Driver Operator un-installs the CSI driver.

* Storage container orchestration (CO) should be healthy.

* vSphere-problem-detector continues running, but does not emit alerts or events, and checks less frequently (once per 24 hours).

* All existing persistent volumes (PVs), persistent volume claims (PVCs), and vSphere storage policies are unchanged:

** vSphere PVs cannot be used in new pods.

** vSphere PVs stay mounted and attached forever to existing nodes for existing pods. These pods remain in terminating state indefinitely after deletion.

* Storage classes are removed

|* vSphere CSI Driver Operator re-installs the CSI driver.

* If necessary, the vSphere CSI Driver Operator creates the vSphere storage policy.
|===

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-disable-storage-procedure_{context}"]
= Disabling and enabling storage on vSphere

[IMPORTANT]
====
Before running this procedure, carefully review the preceding "Consequences of disabling and enabling storage on vSphere" table and potential impacts to your environment.
====

.Procedure

To disable or enable storage on vSphere:

. Click *Administration* > *CustomResourceDefinitions*.

. On the *CustomResourceDefinitions* page next to the *Name* dropdown box, type "clustercsidriver".

. Click *CRD ClusterCSIDriver*.

. Click the *Instances* tab.

. Click *csi.vsphere.vmware.com*.

. Click the *YAML* tab.

. For `spec.managementState`, change the value to `Removed` or `Managed`:
+
* `Removed`: storage is disabled
* `Managed`: storage is enabled

. Click *Save*.

. If you are disabling storage, confirm that the driver has been removed:
.. Click *Workloads* > *Pods*.
.. On the *Pods* page, in the *Name* filter box type "vmware-vsphere-csi-driver".
+
The only item that should appear is the operator. For example: "
vmware-vsphere-csi-driver-operator-559b97ffc5-w99fm"

// Module included in the following assemblies:
//
// storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-adding-bm-nodes_{context}"]
= Adding bare-metal nodes

[role="_abstract"]
Adding bare-metal nodes to an OpenShift Container Platform cluster on vSphere is supported as a Technology Preview feature.

However, if you add bare-metal nodes, you must remove the vSphere CSI Driver, otherwise the cluster is marked as degraded. For information about how to remove the driver and the consequences of doing this, see Section _Disabling and enabling storage on vSphere_.

For information about how to add bare-metal nodes, under _Additional resources_, see Section _Adding bare-metal compute machines to a vSphere cluster_.

[role="_additional-resources"]
.Additional resources
* Adding bare-metal compute machines to a vSphere cluster

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-increase-max-vols-per-node-overview_{context}"]
= Increasing maximum volumes per node for vSphere

For vSphere version 8 or later, or VMware vSphere Foundation (VVF) 9, or VMware Cloud Foundation (VCF) 9, you can increase the allowable number of volumes per node to a maximum of 255. Otherwise, the default value remains at 59.

[IMPORTANT]
====
You must have an homogeneous vSphere 8 environment that only contains ESXi 8 hypervisors, or an homogeneous VVF or VCF 9 environment that only contains ESXi 9 hypervisors. Heterogeneous environments that contain a mix of versions of ESXi are not allowed. In such heterogenous environment, if you set a value greater than 59, the cluster degrades.
====

.Limitations

* You must be running VMware vSphere version 8 or later, or VVF 9, or VCF 9.

* You can potentially exceed the limit of 2048 virtual disks per host if you increase the maximum number of volumes per node on enough nodes. This can occur because there is no Distributed Resource scheduler (DRS) validation for vSphere to ensure you do not exceed this limit.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-vsphere.adoc
//

[id="persistent-storage-csi-vsphere-increase-max-vols-per-node_{context}"]
= Increasing the maximum allowable volumes per node for vSphere

.Prerequisites
* Access to the OpenShift Container Platform web console.

* Access to the cluster as a user with the cluster-admin role.

* Access to VMware vSphere vCenter.

* In vCenter, ensure that the parameter `pvscsiCtrlr256DiskSupportEnabled` is set to 'True'.
+
[IMPORTANT]
====
Changing the `pvscsiCtrlr256DiskSupportEnabled` parameter is not fully supported by VMware. Also, the parameter is a cluster-wide option.
====

.Procedure

Use the following procedure to increase the maximum number of volumes per node for vSphere:

. Click *Administration* > *CustomResourceDefinitions*.

. On the *CustomResourceDefinitions* page next to the *Name* dropdown box, type "clustercsidriver".

. Click *CRD ClusterCSIDriver*.

. Click the *Instances* tab.

. Click *csi.vsphere.vmware.com*.

. Click the *YAML* tab.

. Set the parameter `spec.driverConfig.driverType` to `vSphere`.

. Add the parameter `spec.driverConfig.vSphere.maxAllowedBlockVolumesPerNode` to the YAML file, and provide a value for the desired maximum number of volumes per node as in the following sample YAML file:
+
[source,yaml]
.Sample YAML file for adding the parameter maxAllowedBlockVolumesPerNode
----
...
spec:
  driverConfig:
    driverType: vSphere
    vSphere:
      maxAllowedBlockVolumesPerNode: <1>
...
----
<1> Enter the desired value here for the maximum number of volumes per node. The default is 59. The minimum value is 1 and the maximum value is 255.

. Click *Save*.

== Additional resources
* Configuring CSI volumes

* Best practices for using VMware snapshots in the vSphere environment

* VMware vCenter documentation
