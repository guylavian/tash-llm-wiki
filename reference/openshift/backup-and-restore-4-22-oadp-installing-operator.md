---
title: "Installing the OADP Operator"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-installing-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-installing-operator
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# Installing the OADP Operator

[id="oadp-installing-operator-doc"]
= Installing the OADP Operator

[role="_abstract"]
Install the {oadp-first} Operator on OpenShift Container Platform  by using Operator Lifecycle Manager (OLM).

The {oadp-short} Operator installs Velero {velero-version}.

[id="installing-operator-oadp_{context}"]
= Installing the OADP Operator

[role="_abstract"]
Install the {oadp-short} Operator by using the OpenShift Container Platform web console.

.Prerequisites

* You must be logged in as a user with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.
. Use the *Filter by keyword* field to find the *OADP Operator*.
. Select the *OADP Operator* and click *Install*.
. Click *Install* to install the Operator in the `openshift-adp` project.
. Click *Ecosystem* -> *Installed Operators* to verify the installation.

// Module included in the following assemblies:
//
// backup_and_restore/application_backup_and_restore/installing/oadp-installing-operator.adoc
// backup_and_restore/application_backup_and_restore/troubleshooting/velero-cli-tool.adoc

[id="velero-oadp-version-relationship_{context}"]
= OADP-Velero-OpenShift Container Platform version relationship

[role="_abstract"]
Review the version relationship between {oadp-short}, Velero, and OpenShift Container Platform to decide compatible version combinations. This helps you select the appropriate {oadp-short} version for your cluster environment.

[cols="3", options="header"]
|===
|OADP version |Velero version |OpenShift Container Platform version
| 1.3.0 | 1.12 | 4.12-4.15
| 1.3.1 | 1.12 | 4.12-4.15
| 1.3.2 | 1.12 | 4.12-4.15
| 1.3.3 | 1.12 | 4.12-4.15
| 1.3.4 | 1.12 | 4.12-4.15
| 1.3.5 | 1.12 | 4.12-4.15
| 1.4.0 | 1.14 | 4.14-4.18
| 1.4.1 | 1.14 | 4.14-4.18
| 1.4.2 | 1.14 | 4.14-4.18
| 1.4.3 | 1.14 | 4.14-4.18
| 1.5.0 | 1.16 | 4.19
|===

[role="_additional-resources"]
== Additional resources

* Velero 1.12 documentation
* Velero 1.14 documentation
* Velero 1.16 documentation

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Velero {velero-version}
