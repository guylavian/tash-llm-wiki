---
title: "APIs used with OADP"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-api
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-api
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# APIs used with OADP

[id="oadp-api"]
= APIs used with OADP

[role="_abstract"]
You can use the following APIs with {oadp-short}:

Velero API::
Velero API documentation is maintained by Velero and is not maintained by Red{nbsp}Hat.

OADP API::

The following are the {oadp-short} APIs:

* `DataProtectionApplicationSpec`
* `BackupLocation`
* `SnapshotLocation`
* `ApplicationConfig`
* `VeleroConfig`
* `CustomPlugin`
* `ResticConfig`
* `PodConfig`
* `Features`
* `DataMover`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="dataprotectionapplicationspec-type_{context}"]
= DataProtectionApplicationSpec type

[role="_abstract"]
The following are `DataProtectionApplicationSpec` {oadp-short} APIs:

.DataProtectionApplicationSpec
[options="header"]
|===
|Property|Type|Description

|`backupLocations`
|[] `BackupLocation`
|Defines the list of configurations to use for `BackupStorageLocations`.

|`snapshotLocations`
|[] `SnapshotLocation`
|Defines the list of configurations to use for `VolumeSnapshotLocations`.

|`unsupportedOverrides`
|map [ UnsupportedImageKey ]  string
|Can be used to override the deployed dependent images for development. Options are `veleroImageFqin`, `awsPluginImageFqin`, `hypershiftPluginImageFqin`, `openshiftPluginImageFqin`, `azurePluginImageFqin`, `gcpPluginImageFqin`, `csiPluginImageFqin`, `dataMoverImageFqin`, `resticRestoreImageFqin`, `kubevirtPluginImageFqin`, and `operator-type`.

|`podAnnotations`
|map [ string ] string
|Used to add annotations to pods deployed by Operators.

|`podDnsPolicy`
|`DNSPolicy`
|Defines the configuration of the DNS of a pod.

|`podDnsConfig`
|`PodDNSConfig`
|Defines the DNS parameters of a pod in addition to those generated from `DNSPolicy`.

|`backupImages`
|*bool
|Used to specify whether or not you want to deploy a registry for enabling backup and restore of images.

|`configuration`
|*`ApplicationConfig`
|Used to define the data protection application's server configuration.

|`features`
|*`Features`
|Defines the configuration for the DPA to enable the Technology Preview features.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the OADP API

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="backuplocation-type_{context}"]
= BackupLocation type

[role="_abstract"]
The following are `BackupLocation` {oadp-short} APIs:

.BackupLocation
[options="header"]
|===
|Property|Type|Description

|`velero`
|*velero.BackupStorageLocationSpec
|Location to store volume snapshots, as described in Backup Storage Location.

|`bucket`
| *CloudStorageLocation
| Automates creation of a bucket at some cloud storage providers for use as a backup storage location.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `BackupLocation`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="snapshotlocation-type_{context}"]
= SnapshotLocation type

[role="_abstract"]
The following are `SnapshotLocation` {oadp-short} APIs:

.SnapshotLocation
[options="header"]
|===
|Property|Type|Description

|`velero`
|*VolumeSnapshotLocationSpec
|Location to store volume snapshots, as described in Volume Snapshot Location.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `SnapshotLocation`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="applicationconfig-type_{context}"]
= ApplicationConfig type

[role="_abstract"]
The following are `ApplicationConfig` {oadp-short} APIs:

.ApplicationConfig
[options="header"]
|===
|Property|Type|Description

|`velero`
|*VeleroConfig
|Defines the configuration for the Velero server.

|`restic`
|*ResticConfig
|Defines the configuration for the Restic server.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `ApplicationConfig`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="veleroconfig-type_{context}"]
= VeleroConfig type

[role="_abstract"]
The following are `VeleroConfig` {oadp-short} APIs:

.VeleroConfig
[options="header"]
|===
|Property|Type|Description

|`featureFlags`
|[] string
|Defines the list of features to enable for the Velero instance.

|`defaultPlugins`
|[] string
|The following types of default Velero plugins can be installed: `aws`,`azure`, `csi`, `gcp`, `kubevirt`, and `openshift`.

|`customPlugins`
|[]CustomPlugin
|Used for installation of custom Velero plugins.

|`restoreResourcesVersionPriority`
|string
|Represents a config map that is created if defined for use in conjunction with the `EnableAPIGroupVersions` feature flag. Defining this field automatically adds `EnableAPIGroupVersions` to the Velero server feature flag.

|`noDefaultBackupLocation`
|bool
|To install Velero without a default backup storage location, you must set the `noDefaultBackupLocation` flag in order to confirm installation.

|`podConfig`
|*`PodConfig`
|Defines the configuration of the `Velero` pod.

|`logLevel`
|string
|Velero server’s log level (use `debug` for the most granular logging, leave unset for Velero default). Valid options are `trace`, `debug`, `info`, `warning`, `error`, `fatal`, and `panic`.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `VeleroConfig`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="customplugin-type_{context}"]
= CustomPlugin type

[role="_abstract"]
The following are `CustomPlugin` {oadp-short} APIs:

.CustomPlugin
[options="header"]
|===
|Property|Type|Description

|`name`
|string
|Name of custom plugin.

|`image`
|string
|Image of custom plugin.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `CustomPlugin`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="resticconfig-type_{context}"]
= ResticConfig type

[role="_abstract"]
The following are `ResticConfig` {oadp-short} APIs:

.ResticConfig
[options="header"]
|===
|Property|Type|Description

|`enable`
|*bool
|If set to `true`, enables backup and restore using Restic. If set to `false`, snapshots are needed.

|`supplementalGroups`
|[]int64
|Defines the Linux groups to be applied to the `Restic` pod.

|`timeout`
|string
|A user-supplied duration string that defines the Restic timeout. Default value is `1hr` (1 hour). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, `-1.5h`, or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.

|`podConfig`
|*`PodConfig`
|Defines the configuration of the `Restic` pod.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `ResticConfig`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="podconfig-type_{context}"]
= PodConfig type

[role="_abstract"]
The following are `PodConfig` {oadp-short} APIs:

.PodConfig
[options="header"]
|===
|Property|Type|Description

|`nodeSelector`
|map [ string ] string
|Defines the `nodeSelector` to be supplied to a `Velero` `podSpec` or a `Restic` `podSpec`.

|`tolerations`
|[]Toleration
|Defines the list of tolerations to be applied to a Velero deployment or a Restic `daemonset`.

|`resourceAllocations`
|ResourceRequirements
|Set specific resource `limits` and `requests` for a `Velero` pod or a `Restic` pod as described in the Setting Velero CPU and memory resource allocations section.

|`labels`
|map [ string ] string
|Labels to add to pods.
|===

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="features-type_{context}"]
= Features type

[role="_abstract"]
The following are `Features` {oadp-short} APIs:

.Features
[options="header"]
|===
|Property|Type|Description

|`dataMover`
|*`DataMover`
|Defines the configuration of the Data Mover.
|===

[role="_additional-resources"]
.Additional resources
* Complete schema definitions for the type `Features`

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/oadp-api.adoc

[id="datamover-type_{context}"]
= DataMover type

[role="_abstract"]
The following are `DataMover` {oadp-short} APIs:

.DataMover
[options="header"]
|===
|Property|Type|Description

|`enable`
|bool
|If set to `true`, deploys the volume snapshot mover controller and a modified CSI Data Mover plugin. If set to `false`, these are not deployed.

|`credentialName`
|string
|User-supplied Restic `Secret` name for Data Mover.

|`timeout`
|string
|A user-supplied duration string for `VolumeSnapshotBackup` and `VolumeSnapshotRestore` to complete. Default is `10m` (10 minutes). A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as `300ms`, `-1.5h`, or `2h45m`. Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.
|===

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Velero API types
* OADP Operator (Go documentation)
* OADP plugins
* Complete schema definitions for the type `PodConfig`
