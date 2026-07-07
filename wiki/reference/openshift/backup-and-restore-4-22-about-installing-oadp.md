---
title: "About installing OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-about-installing-oadp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/about-installing-oadp
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# About installing OADP

[id="about-installing-oadp"]
= About installing OADP

[role="_abstract"]
As a cluster administrator, you install the OpenShift API for Data Protection (OADP) by installing the OADP Operator. The OADP Operator installs {velero-link}.

To back up Kubernetes resources and internal images, you must have object storage as a backup location, such as one of the following storage types:

* Amazon Web Services
* Microsoft Azure
* {gcp-full}
* Multicloud Object Gateway
* {ibm-cloud-name} Object Storage S3
* AWS S3 compatible object storage, such as Multicloud Object Gateway or MinIO

You can configure multiple backup storage locations within the same namespace for each individual OADP deployment.

You can back up persistent volumes (PVs) by using snapshots or a File System Backup (FSB).

To back up PVs with snapshots, you must have a cloud provider that supports either a native snapshot API or Container Storage Interface (CSI) snapshots, such as one of the following cloud providers:

* Amazon Web Services
* Microsoft Azure
* {gcp-full}
* CSI snapshot-enabled cloud provider, such as {rh-storage}

If your cloud provider does not support snapshots or if your storage is NFS, you can back up applications with File System Backup: Kopia or Restic on object storage.

You create a default `Secret` and then you install the Data Protection Application.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc
// * backup_and_restore/application_backup_and_restore/installing/about-installing-oadp.adoc

[id="oadp-s3-compatible-backup-storage-providers_{context}"]
= AWS S3 compatible backup storage providers

{oadp-short} works with many S3-compatible object storage providers. Several object storage providers are certified and tested with every release of {oadp-short}. Various S3 providers are known to work with {oadp-short} but are not specifically tested and certified. These providers will be supported on a best-effort basis. Additionally, there are a few S3 object storage providers with known issues and limitations that are listed in this documentation.

[NOTE]
====
Red Hat will provide support for {oadp-short} on any S3-compatible storage, but support will stop if the S3 endpoint is determined to be the root cause of an issue.
====

[id="oadp-certified-backup-storage-providers_{context}"]
== Certified backup storage providers

The following AWS S3 compatible object storage providers are fully supported by {oadp-short} through the AWS plugin for use as backup storage locations:

* MinIO
* Multicloud Object Gateway (MCG)
* Amazon Web Services (AWS) S3
* {ibm-cloud-name} Object Storage S3
* Ceph RADOS Gateway (Ceph Object Gateway)
* Red Hat Container Storage
* {odf-full}
* NetApp ONTAP S3 Object Storage
* Scality ARTESCA S3 object storage

[NOTE]
====
The following compatible object storage providers are supported and have their own Velero object store plugins:

* {gcp-first}
* Microsoft Azure
====

[id="oadp-s3-compatible-backup-storage-providers-unsupported"]
== Unsupported backup storage providers

The following AWS S3 compatible object storage providers, are known to work with Velero through the AWS plugin, for use as backup storage locations, however, they are unsupported and have not been tested by Red Hat:

* Oracle Cloud
* DigitalOcean
* NooBaa, unless installed using Multicloud Object Gateway (MCG)
* Tencent Cloud
* Ceph RADOS v12.2.7
* Quobyte
* Cloudian HyperStore

[id="oadp-s3-compatible-backup-storage-providers-known-limitations"]
== Backup storage providers with known limitations

[role="_abstract"]
The following AWS S3 compatible object storage providers are known to work with Velero through the AWS plugin with a limited feature set:

* Swift - It works for use as a backup storage location for backup storage, but is not compatible with Restic for filesystem-based volume backup and restore.

[role="_additional-resources"]
== Additional resources

* Scality ARTESCA S3 object storage (Scality documentation)

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-configuring-noobaa-for-dr_{context}"]
= Configuring Multicloud Object Gateway (MCG) for disaster recovery on {rh-storage}

[role="_abstract"]
If you use cluster storage for your MCG bucket `backupStorageLocation` on {rh-storage}, configure MCG as an external object store.

[WARNING]
====
Failure to configure MCG as an external object store might lead to backups not being available.
====

.Procedure

* Configure MCG as an external object store as described in Adding storage resources for hybrid or Multicloud.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Installing OADP on Amazon Web Services
* Installing OADP on Microsoft Azure
* Installing OADP on {gcp-full}
* Installing OADP on Multicloud Object Gateway
* Installing OADP on {rh-storage}
* Backing up applications with File System Backup: Kopia or Restic
* Cluster service version

// Module included in the following assemblies:
//
// * backup_and_restore/installing/about-installing-oadp.adoc

[id="about-oadp-update-channels_{context}"]
= About {oadp-short} update channels

[role="_abstract"]
When you install an {oadp-short} Operator, you choose an update channel. This channel determines which upgrades to the {oadp-short} Operator and to Velero you receive.

The following update channels are available:

* The *stable-1.3* channel contains `{oadp-short}.v1.3.z`, the most recent {oadp-short} 1.3 `ClusterServiceVersion`.

* The *stable-1.4* channel contains `{oadp-short}.v1.4.z`, the most recent {oadp-short} 1.4 `ClusterServiceVersion`.

* Starting with {oadp-short} 1.5 on OpenShift Container Platform v4.19, {oadp-short} reintroduces the *stable* channel which contains a single supported {oadp-short} version for a particular OpenShift Container Platform version.

For more information, see _OpenShift Operator Life Cycles_.

*Which update channel is right for you?*

* If you are already using the *stable* channel, you will continue to get updates from `{oadp-short}.v1.5.z`.

* Choose the *stable-1.y* update channel to install {oadp-short} 1.y and to continue receiving patches for it. If you choose this channel, you will receive all z-stream patches for version 1.y.z.

*When must you switch update channels?*

* If you have {oadp-short} 1.y installed, and you want to receive patches only for that y-stream, you must switch from the *stable* update channel to the *stable-1.y* update channel. You will then receive all z-stream patches for version 1.y.z.

* If you have {oadp-short} 1.0 installed, want to upgrade to {oadp-short} 1.1, and then receive patches only for {oadp-short} 1.1, you must switch from the *stable-1.0* update channel to the *stable-1.1* update channel. You will then receive all z-stream patches for version 1.1.z.

* If you have {oadp-short} 1.y installed, with _y_ greater than 0, and want to switch to {oadp-short} 1.0, you must uninstall your {oadp-short} Operator and then reinstall it using the *stable-1.0* update channel. You will then receive all z-stream patches for version 1.0.z.

[NOTE]
====
You cannot switch from {oadp-short} 1.y to OADP 1.0 by switching update channels. You must uninstall the Operator and then reinstall it.
====

[role="_additional-resources"]
.Additional resources

* OpenShift Operator Life Cycles
// Module included in the following assemblies:
//
// * backup_and_restore/installing/about-installing-oadp.adoc

[id="about-installing-oadp-on-multiple-namespaces_{context}"]
= Installation of {oadp-short} on multiple namespaces

[role="_abstract"]
You can install {oadp-full} into multiple namespaces on the same cluster so that multiple project owners can manage their own {oadp-short} instance. This use case has been validated with File System Backup (FSB) and Container Storage Interface (CSI).

You install each instance of {oadp-short} as specified by the per-platform procedures contained in this document with the following additional requirements:

* All deployments of {oadp-short} on the same cluster must be the same version, for example, 1.4.0. Installing different versions of {oadp-short} on the same cluster is *not* supported.

* Each individual deployment of {oadp-short} must have a unique set of credentials and at least one `BackupStorageLocation` configuration. You can also use multiple `BackupStorageLocation` configurations within the same namespace.

* By default, each {oadp-short} deployment has cluster-level access across namespaces. {OCP} administrators need to carefully review potential impacts, such as not backing up and restoring to and from the same namespace concurrently.
// Module included in the following assemblies:
//
// * backup_and_restore/installing/about-installing-oadp.adoc

[id="oadp-support-backup-data-immutability_{context}"]
= OADP support for backup data immutability

[role="_abstract"]
Starting with {oadp-short} 1.4, you can store {oadp-short} backups in an {aws-short} S3 bucket with enabled versioning. The versioning support is only for {aws-short} S3 buckets and not for S3-compatible buckets.

See the following list for specific cloud provider limitations:

* AWS S3 service supports backups because an S3 object lock applies only to versioned buckets. You can still update the object data for the new version. However, when backups are deleted, old versions of the objects are not deleted.

* {oadp-short} backups are not supported and might not work as expected when you enable immutability on Azure Storage Blob.

* {gcp-short} storage policy only supports bucket-level immutability. Therefore, it is not feasible to implement it in the {gcp-short} environment.

Depending on your storage provider, the immutability options are called differently:

* S3 object lock
* Object retention
* Bucket versioning
* Write Once Read Many (WORM) buckets

The primary reason for the absence of support for other S3-compatible object storage is that {oadp-short} initially saves the state of a backup as _finalizing_ and then verifies whether any asynchronous operations are in progress.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

[id="oadp-velero-cpu-memory-requirements_{context}"]
= Velero CPU and memory requirements based on collected data

[role="_abstract"]
The following recommendations are based on observations of performance made in the scale and performance lab. The backup and restore resources can be impacted by the type of plugin, the amount of resources required by that backup or restore, and the respective data contained in the persistent volumes (PVs) related to those resources.

== CPU and memory requirement for configurations
|===
|Configuration types | ^[1]^ Average usage |^[2]^ Large usage |resourceTimeouts

|CSI
|Velero:

CPU- Request 200m, Limits 1000m

Memory - Request 256Mi, Limits 1024Mi

|Velero:

CPU- Request 200m, Limits 2000m

Memory- Request  256Mi, Limits 2048Mi

|N/A

|Restic
|^[3]^ Restic:

CPU- Request 1000m, Limits 2000m

Memory - Request 16Gi, Limits 32Gi

|^[4]^ Restic:

CPU - Request 2000m, Limits 8000m

Memory - Request 16Gi, Limits 40Gi

|900m

|^[5]^ Data Mover
|N/A
|N/A
|10m - average usage

60m - large usage
|===

[.small]
--
1. Average usage - use these settings for most usage situations.

2. Large usage - use these settings for large usage situations, such as a large PV (500GB Usage), multiple namespaces (100+), or many pods within a single namespace (2000 pods+), and for optimal performance for backup and restore involving large datasets.

3. Restic resource usage corresponds to the amount of data, and type of data. For example, many small files or large amounts of data can cause Restic to use large amounts of resources. The Velero documentation references 500m as a supplied default, for most of our testing we found a 200m request suitable with 1000m limit. As cited in the Velero documentation, exact CPU and memory usage is dependent on the scale of files and directories, in addition to environmental limitations.

4. Increasing the CPU has a significant impact on improving backup and restore times.

5. Data Mover - Data Mover default resourceTimeout is 10m. Our tests show that for restoring a large PV (500GB usage), it is required to increase the resourceTimeout to 60m.
--

[NOTE]
====
The resource requirements listed throughout the guide are for average usage only. For large usage, adjust the settings as described in the table above.
====

[role="_additional-resources"]
== Additional resources

* Customize Velero Install (Velero documentation)

// Module included in the following assemblies:
// * backup_and_restore/application_backup_and_restore/installing/about-installing-oadp.adoc

[id="oadp-backup-restore-for-large-usage_{context}"]
= NodeAgent CPU for large usage

[role="_abstract"]
Testing shows that increasing `NodeAgent` CPU can significantly improve backup and restore times when using {oadp-first}.

[IMPORTANT]
====
You can tune your OpenShift Container Platform environment based on your performance analysis and preference. Use CPU limits in the workloads when you use Kopia for file system backups.

If you do not use CPU limits on the pods, the pods can use excess CPU when it is available. If you specify CPU limits, the pods might be throttled if they exceed their limits. Therefore, the use of CPU limits on the pods is considered an anti-pattern.

Ensure that you are accurately specifying CPU requests so that pods can take advantage of excess CPU. Resource allocation is guaranteed based on CPU requests rather than CPU limits.

Testing showed that running Kopia with 20 cores and 32 Gi memory supported backup and restore operations of over 100 GB of data, multiple namespaces, or over 2000 pods in a single namespace. Testing detected no CPU limiting or memory saturation with these resource specifications.
====

In some environments, you might need to adjust Ceph MDS pod resources to avoid pod restarts, which occur when default settings cause resource saturation.

[role="_additional-resources"]
== Additional resources

* Changing the CPU and memory resources on the rook-ceph pods
