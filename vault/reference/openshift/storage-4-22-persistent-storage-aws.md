---
title: "Persistent storage using AWS Elastic Block Store"
type: reference
domain: openshift
slug: storage-4-22-persistent-storage-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/persistent-storage-aws
version: 4.22
family: storage
documentKind: "Documentation"
---

# Persistent storage using AWS Elastic Block Store

[id="persistent-storage-aws"]
= Persistent storage using AWS Elastic Block Store

OpenShift Container Platform clusters are prebuilt with two storage classes that use Amazon Elastic Block Store (Amazon EBS) volumes. These storage classes are ready to use and some familiarity with Kubernetes and AWS is assumed.

The following are the two prebuilt storage classes:
[options="header"]

|===

| Name | Provisioner

| gp2-csi | ebs.csi.aws.com

| gp3-csi (default) | ebs.csi.aws.com

|===
The gp3-csi storage class is set as default; however, you can select any of the storage classes as the default storage class.

OpenShift Container Platform supports Amazon Elastic Block Store (EBS) volumes.
You can provision your OpenShift Container Platform cluster with persistent storage by using Amazon EC2.

The Kubernetes persistent volume framework allows administrators to provision a cluster with persistent storage and gives users a way to request those resources without having any knowledge of the underlying infrastructure.
You can dynamically provision Amazon EBS volumes.
Persistent volumes are not bound to a single project or namespace; they can be shared across the OpenShift Container Platform cluster.
Persistent volume claims are specific to a project or namespace and can be requested by users.
You can define a KMS key to encrypt container-persistent volumes on AWS.
By default, newly created clusters using OpenShift Container Platform version 4.10 and later use gp3 storage and the AWS EBS CSI driver.

[IMPORTANT]
====
High-availability of storage in the infrastructure is left to the underlying
storage provider.
====

[IMPORTANT]
====
OpenShift Container Platform 4.12 and later provides automatic migration for the AWS Block in-tree volume plugin to its equivalent CSI driver.

CSI automatic migration should be seamless. Migration does not change how you use all existing API objects, such as persistent volumes, persistent volume claims, and storage classes. For more information about migration, see CSI automatic migration.
====

// Defining attributes required by the next module

// Be sure to set the :StorageClass: and :Provisioner: value in each assembly
// on the line before the include statement for this module. For example, to
// set the StorageClass value to "AWS EBS", add the following line to the
// assembly:
// :StorageClass: AWS EBS
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc

[id="storage-create-storage-class_{context}"]
= Creating the {StorageClass} storage class

Storage classes are used to differentiate and delineate storage levels and
usages. By defining a storage class, users can obtain dynamically provisioned
persistent volumes.

The _AWS EFS CSI Driver Operator (a Red Hat operator)_, after being installed, does not create a storage class by default. However, you can manually create the AWS EFS storage class.

// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="creating-volume-claim_{context}"]
= Creating the persistent volume claim

.Prerequisites

Storage must exist in the underlying infrastructure before it can be mounted as
a volume in OpenShift Container Platform.

.Procedure

. In the OpenShift Container Platform web console, click *Storage* -> *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume Claim*.

. Define the desired options on the page that appears.

.. Select the previously-created storage class from the drop-down menu.

.. Enter a unique name for the storage claim.

.. Select the access mode. This selection determines the read and write access for the storage claim.

.. Define the size of the storage claim.

. Click *Create* to create the persistent volume claim and generate a persistent
volume.

// Be sure to set the :provider: value in each assembly
// on the line before the include statement for this module.
// For example:
// :provider: AWS
//
// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc
// * storage/persistent_storage-gce.adoc

[id="volume-format-{provider}_{context}"]
= Volume format

Before OpenShift Container Platform mounts the volume and passes it to a container, it checks that the volume contains a file system as specified by the `fsType` arameter in the persistent volume definition. If the device is not formatted with the file system, all data from the device is erased and the device is automatically formatted with the given file system.

This verification enables you to use unformatted {provider} volumes as persistent volumes, because OpenShift Container Platform formats them before the first use.

// Undefined {provider} attribute, so that any mistakes are easily spotted

// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="maximum-number-of-ebs-volumes-on-a-node_{context}"]
= Maximum number of EBS volumes on a node

By default, OpenShift Container Platform supports a maximum of 39 EBS volumes attached to one
node. This limit is consistent with the
AWS volume limits. The volume limit depends on the instance type.

[IMPORTANT]
====
As a cluster administrator, you must use either in-tree or Container Storage Interface (CSI) volumes and their respective storage classes, but never both volume types at the same time. The maximum attached EBS volume number is counted separately for in-tree and CSI volumes, which means you could have up to 39 EBS volumes of each type.
====

For information about accessing additional storage options, such as volume snapshots, that are not possible with in-tree volume plug-ins, see AWS Elastic Block Store CSI Driver Operator.

// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

[id="aws-container-persistent-volumes-encrypt_{context}"]
= Encrypting container persistent volumes on AWS with a KMS key

Defining a KMS key to encrypt container-persistent volumes on AWS is useful when you have explicit compliance and security guidelines when deploying to AWS.

.Prerequisites

* Underlying infrastructure must contain storage.
* You must create a customer KMS key on AWS.

.Procedure

. Create a storage class:
+
[source,yaml]
----
$ cat << EOF | oc create -f -
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name> <1>
parameters:
  fsType: ext4 <2>
  encrypted: "true"
  kmsKeyId: keyvalue <3>
provisioner: ebs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
EOF
----
<1> Specifies the name of the storage class.
<2> File system that is created on provisioned volumes.
<3> Specifies the full Amazon Resource Name (ARN) of the key to use when encrypting the container-persistent volume. If you do not provide any key, but the `encrypted` field is set to `true`, then the default KMS key is used. See Finding the key ID and key ARN on AWS in the AWS documentation.

. Create a persistent volume claim (PVC) with the storage class specifying the KMS key:
+
[source,yaml]
----
$ cat << EOF | oc create -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  storageClassName: <storage-class-name>
  resources:
    requests:
      storage: 1Gi
EOF
----

. Create workload containers to consume the PVC:
+
[source,yaml]
----
$ cat << EOF | oc create -f -
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: httpd
      image: quay.io/centos7/httpd-24-centos7
      ports:
        - containerPort: 80
      volumeMounts:
        - mountPath: /mnt/storage
          name: data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: mypvc
EOF
----

[id="additional-resources_persistent-storage-aws"]
[role="_additional-resources"]
== Additional resources

* See AWS Elastic Block Store CSI Driver Operator for information about accessing additional storage options, such as volume snapshots, that are not possible with in-tree volume plugins.
