---
title: "Azure File CSI Driver Operator"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-csi-azure-file
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-csi-azure-file
version: 4.22
family: storage
documentKind: "Documentation"
---

# Azure File CSI Driver Operator

[id="persistent-storage-csi-azure-file"]
= Azure File CSI Driver Operator

== Overview

OpenShift Container Platform is capable of provisioning persistent volumes (PVs) by using the Container Storage Interface (CSI) driver for Microsoft Azure File Storage.

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI Operator and driver.

To create CSI-provisioned PVs that mount to Azure File storage assets, OpenShift Container Platform installs the Azure File CSI Driver Operator and the Azure File CSI driver by default in the `openshift-cluster-csi-drivers` namespace.

* The _Azure File CSI Driver Operator_ provides a storage class that is named `azurefile-csi` that you can use to create persistent volume claims (PVCs). You can disable this default storage class if desired (see Managing the default storage class).

* The _Azure File CSI driver_ enables you to create and mount Azure File PVs. The Azure File CSI driver supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage.

Azure File CSI Driver Operator does not support:

* Virtual hard disks (VHD)

* Running on nodes with Federal Information Processing Standard (FIPS) mode enabled for Server Message Block (SMB) file share. However, Network File System (NFS) does support FIPS mode.

For more information about supported features, see Supported CSI drivers and features.

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
// * storage/container_storage_interface/persistent_storage-csi-azure-file.adoc
//

[id="persistent-storage-csi-azure-file-nfs_{context}"]
= NFS support

[role="_abstract"]
OpenShift Container Platform supports the Azure File Container Storage Interface (CSI) Driver Operator with Network File System (NFS) with the following restrictions:

* If you create a volume smaller than 100GiB, the CSI driver rounds it up to 100GiB.

* Creating pods with Azure File NFS volumes that are scheduled to the control plane node causes the mount to be denied.
+
To work around this issue: If your control plane nodes are schedulable, and the pods can run on worker nodes, use `nodeSelector` or Affinity to schedule the pod in worker nodes.

* FS Group policy behavior:
+
[IMPORTANT]
=====
Azure File CSI with NFS does not honor the fsGroupChangePolicy requested by pods. Azure File CSI with NFS applies a default OnRootMismatch FS Group policy regardless of the policy requested by the pod.
=====
* The Azure File CSI Operator does not automatically create a storage class for NFS. You must create it manually. Use a file similar to the following:
+
[source, yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name> <1>
provisioner: file.csi.azure.com <2>
parameters:
  protocol: nfs <3>
  skuName: Premium_LRS  # available values: Premium_LRS, Premium_ZRS
mountOptions:
  - nconnect=4
----
<1> Storage class name.
<2> Specifies the Azure File CSI provider.
<3> Specifies NFS as the storage backend protocol.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi-azure-file.adoc
//

[id="persistent-storage-csi-azure-file-cross-sub-overview_{context}"]
= Azure File cross-subscription support

Cross-subscription support allows you to have an OpenShift Container Platform cluster in one Azure subscription and mount your Azure file share in another Azure subscription by using the Azure File Container Storage Interface (CSI) driver.

[IMPORTANT]
====
Both the OpenShift Container Platform cluster and the Azure File share (pre-provisioning or to be provisioned) should be inside the same tenant.
====

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi-azure-file.adoc
//
[id="persistent-storage-csi-azure-file-cross-sub-dynamic-provisioning-procedure_{context}"]
= Dynamic provisioning across subscriptions for Azure File

To use Azure File dynamic provisioning across subscriptions by completing this procedure.

.Prerequisites
* Installed OpenShift Container Platform cluster on Azure with the service principal or managed identity as an Azure identity in one subscription (call it Subscription A)

* Access to another subscription (call it Subscription B) with the storage that is in the same tenant as the cluster

* Logged in to the Azure CLI

.Procedure

. Record the Azure identity (service principal or managed identity) by running the following applicable commands. The Azure identity is needed in a later step:
+
* If using the _service principal_ as the Azure identity when installing the cluster:
+
[source,terminal]
----
$ sp_id=$(oc -n openshift-cluster-csi-drivers get secret azure-file-credentials -o jsonpath='{.data.azure_client_id}' | base64 --decode)
----
+
[source,terminal]
----
$ az ad sp show --id ${sp_id} --query displayName --output tsv
----
+
* If using the _managed identity_ as the Azure identity when installing the cluster:
+
[source,terminal]
----
$ mi_id=$(oc -n openshift-cluster-csi-drivers get secret azure-file-credentials -o jsonpath='{.data.azure_client_id}' | base64 --decode)
----
+
[source,terminal]
----
$ az identity list --query "[?clientId=='${mi_id}'].{Name:name}" --output tsv
----

. Grant the Azure identity (service principal or managed identity) permission to access the resource group in another Subscription B where you want to provision the Azure File share by doing one of the following:

* Run the following Azure CLI command:
+
[source,terminal]
----
az role assignment create \
  --assignee <object-id-or-app-id> \
  --role <role-name> \
  --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<storage-account-name>
----
+
Where:
+
`<object-id-or-app-id>`: The service principal or managed identity that you obtained from the previous step, such as `sp_id` or `mi_id`.
+
`<role-name>`: Role name. Contributor or your own role with required permissions.
+
`<subscription-id>`: Subscription B ID.
+
`<resource-group-name>`: Subscription B resource group name.
+
Or
+
* Log in to the Azure portal and on the left menu, click *Resource groups*:

.. Choose the resource group in Subscription B to which you want to assign a role by clicking *resource group* -> *Access control (IAM)* -> *Role assignments* tab to view current assignments, and then click *Add* > *Add role assignment*.

.. On the *Role* tab, choose the contributor role to assign, and then click *Next*. You can also create and choose your own role with required permission.

.. On the *Members* tab:
... Choose an assignee by selecting the type of assignee: user, group, or service principal (or managed identity).
... Click *Select members*.
... Search for, and then select the desired service principal or managed identity recorded in the previous step.
... Click *Select* to confirm.
.. On the *Review + assign* tab, review the settings.

.. To finish the role assignment, click *Review + assign*.
+
[NOTE]
====
If you only want to use a specific storage account to provision the Azure File share, you can also obtain the Azure identity (service principal or managed identity) permission to access the storage account by using similar steps.
====

. Create an Azure File storage class by using a similar configuration to the following:
+
.Example Azure File storage class YAML file
[source, yaml]
----
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <sc-name> <1>
mount options:
  - mfsymlinks
  - cache=strict
  - nosharesock
  - actimeo=30
parameters:
  subscriptionID: <xxxx-xxxx-xxxx-xxxx-xxxx> <2>
  resourceGroup: <resource group name> <3>
  storageAccount: <storage account> <4>
  skuName: <skuName> <5>
provisioner: file.csi.azure.com
reclaimPolicy: Delete
volumeBindingMode: Immediate
----
<1> The name of the storage class
<2> The subscription B ID
<3> The Subscription B resource group name
<4> The storage account name, if you want to specify your own
<5> The name of the SKU type

. Create a persistent volume claim (PVC) that specifies the Azure File storage class that you created in the previous step by using a similar configuration to the following:
+
.Example PVC YAML file
[source, yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <pvc-name> <1>
spec:
  storageClassName: <sc-name-cross-sub> <2>
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
----
<1> The name of the PVC.
<2> The name of the storage class that you created in the previous step.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi-azure-file.adoc
//
[id="persistent-storage-csi-azure-file-cross-sub-dynamic-pre-provisioning-pv-pvc-procedure_{context}"]
= Static provisioning across subscriptions for Azure File by creating a PV and PVC:

.Prerequisites
* Installed OpenShift Container Platform cluster on Azure with the service principal or managed identity as an Azure identity in one subscription (call it Subscription A)

* Access to another subscription (call it Subscription B) with the storage that is in the same tenant as the cluster

* Logged in to the Azure CLI

.Procedure
. For your Azure File share, record the resource group, storage account, storage account key, and Azure File name. These values are used for the next steps.

. Create a secret for the persistent volume parameter `spec.csi.nodeStageSecretRef.name` by running the following command:
+
[source, terminal]
----
$ oc create secret generic azure-storage-account-<storageaccount-name>-secret --from-literal=azurestorageaccountname="<azure-storage-account-name>" --from-literal azurestorageaccountkey="<azure-storage-account-key>" --type=Opaque
----
+
Where:
`<azure-storage-account-name>` and `<azure-storage-account-key>` are the Azure storage account name and key respectively that you recorded in Step 1.

. Create a persistent volume (PV) by using a similar configuration to the following example file:
+
.Example PV YAML file
[source,terminal]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: file.csi.azure.com
  name: <pv-name> <1>
spec:
  capacity:
    storage: 10Gi <2>
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: <sc-name> <3>
  mountOptions:
    - cache=strict
    - nosharesock
    - actimeo=30
    - nobrl
  csi:
    driver: file.csi.azure.com
    volumeHandle: "{resource-group-name}#{storage-account-name}#{file-share-name}" <4>
    volumeAttributes:
      shareName: <existing-file-share-name> <5>
    nodeStageSecretRef:
      name: <secret-name>  <6>
      namespace: <secret-namespace>  <7>
----
<1> The name of the PV.
<2> The size of the PV.
<3> The storage class name.
<4> Ensure that `volumeHandle` is unique for every identical share in the cluster.
<5> For `<existing-file-share-name>, use only the file share name and not the full path.
<6> The secret name created in the previous step.
<7> The namespace where the secret resides.

. Create a persistent value claim (PVC) specifying the existing Azure File share referenced in Step 1 using a similar configuration to the following:
+
.Example PVC YAML file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <pvc-name> <1>
spec:
  storageClassName: <sc-name> <2>
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
----
<1> The name of the PVC.
<2> The name of the storage class that you specified for the PV in the previous step.

.Recommendation to use a storage class
In the preceding example of static provisioning across subscriptions, the storage class referenced in the PV and PVC is not strictly necessary, as storage classes are not required to accomplish static provisioning. However, it is advisable to use a storage class to avoid cases where a manually created PVC accidentally does not match a manually created PV, and thus potentially triggers dynamic provisioning of a new PV. Other ways to avoid this issue would be to create a storage class with `provisioner: kubernetes.io/no-provisioner` or reference a non-existing storage class, which in both cases ensures that dynamic provisioning does not occur. When using either of these strategies, if a mis-matched PV and PVC occurs, the PVC stays in a pending state, and you can correct the error.

// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi-azure-file.adoc
//
[id="persistent-storage-csi-azure-file-static-provisioning-procedure_{context}"]
= Static provisioning for Azure File

For static provisioning, cluster administrators create persistent volumes (PVs) that define the details of the real storage. Cluster users can then create persistent volume claims (PVCs) that consume these PVs.

.Prerequisites
* Access to an OpenShift Container Platform cluster with administrator rights

.Procedure
To use static provisioning for Azure File:

. If you have not yet created a secret for the Azure storage account, create it now:
+
This secret must contain the Azure Storage Account name and key with the following very specific format with two key-value pairs:

* `azurestorageaccountname`: <storage_account_name>
* `azurestorageaccountkey`: <account_key>
+
To create a secret named _azure-secret_, run the following command:
+
[source,terminal]
----
oc create secret generic azure-secret  -n <namespace_name> --type=Opaque --from-literal=azurestorageaccountname="<storage_account_name>" --from-literal=azurestorageaccountkey="<account_key>" <1> <2>
----
<1> Set `<namespace_name>` to the namespace where the PV is consumed.
<2> Provide your values for `<storage_account_name>` and `<account_key>`.

. Create a PV by using the following example YAML file:
+
.Example PV YAML file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: file.csi.azure.com
  name: pv-azurefile
spec:
  capacity:
    storage: 5Gi <1>
  accessModes:
    - ReadWriteMany <2>
  persistentVolumeReclaimPolicy: Retain <3>
  storageClassName: <sc-name> <4>
  mountOptions:
    - dir_mode=0777  <5>
    - file_mode=0777
    - uid=0
    - gid=0
    - cache=strict  <6>
    - nosharesock  <7>
    - actimeo=30  <8>
    - nobrl  <9>
  csi:
    driver: file.csi.azure.com
    volumeHandle: "{resource-group-name}#{account-name}#{file-share-name}" <10>
    volumeAttributes:
      shareName: EXISTING_FILE_SHARE_NAME  <11>
    nodeStageSecretRef:
      name: azure-secret <12>
      namespace: <my-namespace> <13>
----
<1> Volume size.
<2> Access mode. Defines the read-write and mount permissions. For more information, under _Additional resources_, see _Access modes_.
<3> Reclaim policy. Tells the cluster what to do with the volume after it is released. Accepted values are `Retain`, `Recycle`, or `Delete`.
<4> Storage class name. This name is used by the PVC to bind to this specific PV. For static provisioning, a `StorageClass` object does not need to exist, but the name in the PV and PVC must match.
<5> Modify this permission if you want to enhance the security.
<6> Cache mode. Accepted values are `none`, `strict`, and `loose`. The default is `strict`.
<7> Use to reduce the probability of a reconnect race.
<8> The time (in seconds) that the CIFS client caches attributes of a file or directory before it requests attribute information from a server.
<9> Disables sending byte range lock requests to the server, and for applications which have challenges with POSIX locks.
<10> Ensure that `volumeHandle` is unique across the cluster. The `resource-group-name` is the Azure resource group where the storage account resides.
<11> File share name. Use only the file share name; do not use full path.
<12> Provide the name of the secret created in step 1 of this procedure. In this example, it is _azure-secret_.
<13> The namespace that the secret was created in. This must be the namespace where the PV is consumed.

. Create a PVC that references the PV using the following example file:
+
.Example PVC YAML file
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <pvc-name> <1>
  namespace: <my-namespace> <2>
spec:
  volumeName: pv-azurefile <3>
  storageClassName: <sc-name> <4>
  accessModes:
    - ReadWriteMany <5>
  resources:
    requests:
      storage: 5Gi <6>
----
<1> PVC name.
<2> Namespace for the PVC.
<3> The name of the PV that you created in the previous step.
<4> Storage class name. This name is used by the PVC to bind to this specific PV. For static provisioning, a `StorageClass` object does not need to exist, but the name in the PV and PVC must match.
<5> Access mode. Defines the requested read-write access for the PVC. Claims use the same conventions as volumes when requesting storage with specific access modes. For more information, under _Additional resources_, see _Access modes_.
<6> PVC size.

. Ensure that the PVC is created and in `Bound` status after a while by running the following command:
+
[source,terminal]
----
$ oc get pvc <pvc-name> <1>
----
<1> The name of your PVC.
+
.Example output
[source,terminal]
----
NAME       STATUS    VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS   AGE
pvc-name   Bound     pv-azurefile   5Gi        ReadWriteMany  my-sc          7m2s
----

[role="_additional-resources"]
.Additional resources
* Persistent storage using Azure File
* Configuring CSI volumes
* Access modes
