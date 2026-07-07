---
title: "Introduction to {oadp-full}"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-intro
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-intro
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Introduction to {oadp-full}

[id="oadp-introduction"]
= Introduction to {oadp-full}

[role="_abstract"]
Use {oadp-first} to safeguard applications, application-related cluster resources, persistent volumes, and internal images on OpenShift Container Platform. {oadp-short} backs up containerized applications and virtual machines (VMs). This helps you ensure disaster recovery.

However, {oadp-short} does not serve as a disaster recovery solution for `etcd` or {OCP-short} Operators.

[IMPORTANT]
====
{oadp-short} support is applicable to customer workload namespaces and cluster scope resources.

Full cluster `backup` and `restore` are not supported.
====

[id="oadp-apis_{context}"]
== {oadp-full} APIs

{oadp-short} provides APIs that enable multiple approaches to customizing backups and preventing the inclusion of unnecessary or inappropriate resources.

{oadp-short} provides the following APIs. See the _Additional resources_ section for more details.

* `Backup`
* `Restore`
* `Schedule`
* `BackupStorageLocation`
* `VolumeSnapshotLocation`

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-intro.adoc

[id="oadp-operator-supported_{context}"]
= Support for {oadp-full}

[role="_abstract"]
Review the {oadp-short} support matrix for version compatibility with OpenShift Container Platform releases and lifecycle policy information, including Extended Update Support (EUS) options.

.Supported versions of {oadp-short}
[width="100%",cols="10%,12%,12%,13%,13%,20%,20%,options="header"]
|===

|Version
|OpenShift Container Platform version
|General availability
|Full support ends
|Maintenance ends
|Extended Update Support (EUS)
|Extended Update Support Term 2 (EUS Term 2)

|1.5
a|
* 4.19
* 4.20
* 4.21
| 17 June 2025
|Release of 1.6
|Release of 1.7
a|

EUS must be on OpenShift Container Platform 4.21
a|
EUS Term 2 must be on OpenShift Container Platform 4.21

|1.4
a|
* 4.14
* 4.15
* 4.16
* 4.17
* 4.18
|10 Jul 2024
|Release of 1.5
|Release of 1.6
a|
27 Jun 2026

EUS must be on OpenShift Container Platform 4.16
a|
27 Jun 2027

EUS Term 2 must be on OpenShift Container Platform 4.16

|1.3
a|
* 4.12
* 4.13
* 4.14
* 4.15
|29 Nov 2023
|10 Jul 2024
|Release of 1.5
a|
31 Oct 2025

EUS must be on OpenShift Container Platform 4.14
a|
31 Oct 2026

EUS Term 2 must be on OpenShift Container Platform 4.14
|===

[id="oadp-operator-unsupported_{context}"]
== Unsupported versions of the {oadp-short} Operator

.Previous versions of the {oadp-short} Operator which are no longer supported
[width="100%",cols="25%,25%,25%,25%,options="header"]
|===
|Version
|General availability
|Full support ended
|Maintenance ended

|1.2
|14 Jun 2023
|29 Nov 2023
|10 Jul 2024

|1.1
|01 Sep 2022
|14 Jun 2023
|29 Nov 2023

|1.0
|09 Feb 2022
|01 Sep 2022
|14 Jun 2023
|===

For more details about EUS, see Extended Update Support.

For more details about EUS Term 2, see Extended Update Support Term 2.

[role="_additional-resources"]
.Additional resources

* Backup
* Restore
* Schedule

* BackupStorageLocation
* VolumeSnapshotLocation
* Backing up etcd
// once finished re-work come back and add doc links to the APIs
