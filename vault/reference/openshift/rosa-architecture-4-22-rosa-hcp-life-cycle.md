---
title: "{product-title} update life cycle"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-hcp-life-cycle
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-hcp-life-cycle
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# {product-title} update life cycle

[id="rosa-hcp-life-cycle"]
= OpenShift Container Platform update life cycle

[role="_abstract"]
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="life-cycle-overview_{context}"]
= Overview

[role="_abstract"]
Red{nbsp}Hat provides a published product life cycle for OpenShift Container Platform in order for customers and partners to effectively plan, deploy, and support their applications running on the platform. Red{nbsp}Hat publishes this life cycle to provide as much transparency as possible and might make exceptions from these policies as conflicts arise.

OpenShift Container Platform is a managed deployment of Red{nbsp}Hat OpenShift and maintains an independent release schedule. More details about the managed offering can be found in the OpenShift Container Platform service definition. The availability of Security Advisories and Bug Fix Advisories for a specific version are dependent upon the Red{nbsp}Hat OpenShift Container Platform life cycle policy and subject to the OpenShift Container Platform maintenance schedule.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform service definition

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-life-cycle-definitions_{context}"]
= Definitions

[role="_abstract"]
The following table defines the versioning scheme used for OpenShift Container Platform releases.

.Version reference
[options="header"]
|===
|Version format |Major  |Minor  |Patch  |Major.minor.patch
|               |x      |y      |z      |x.y.z
|Example        |4      |5      |21     |4.5.21
|===

Major releases or X-releases:: Referred to only as _major releases_ or _X-releases_ (X.y.z).
+
--
.Examples
* "Major release 5" -> 5.y.z
* "Major release 4" -> 4.y.z
* "Major release 3" -> 3.y.z
--

Minor releases or Y-releases:: Referred to only as _minor releases_ or _Y-releases_ (x.Y.z).
+
--
.Examples
* "Minor release 4" -> 4.4.z
* "Minor release 5" -> 4.5.z
* "Minor release 6" -> 4.6.z
--

Patch releases or Z-releases:: Referred to only as _patch releases_ or _Z-releases_ (x.y.Z).
+
--
.Examples
* "Patch release 14 of minor release 5" -> 4.5.14
* "Patch release 25 of minor release 5" -> 4.5.25
* "Patch release 26 of minor release 6" -> 4.6.26
--
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-major-versions_{context}"]
= Major versions (X.y.z)

[role="_abstract"]
Major versions of OpenShift Container Platform, for example version 4, are supported for one year following the
release of a subsequent major version or the retirement of the product.

.Example
* If version 5 were made available on OpenShift Container Platform on January 1, version 4 would be allowed to
  continue running on managed clusters for 12 months, until December 31. After this time, clusters
  would need to be upgraded or migrated to version 5.
// Module included in the following assemblies:
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-minor-versions_{context}"]
= Minor versions (x.Y.z)

[role="_abstract"]
Starting with the 4.8 OpenShift Container Platform minor version, Red{nbsp}Hat supports all minor versions for at least a 16 month period following general availability of the given minor version. Patch versions are not affected by the support period.

Customers are notified 60, 30, and 15 days before the end of the support period. Clusters must be upgraded to the latest patch version of the oldest supported minor version before the end of the support period, or
Red{nbsp}Hat will automatically upgrade the control plane to the next supported minor version.
the cluster will enter a "Limited Support" status.

.Example
. A customer's cluster is currently running on 4.13.8. The 4.13 minor version became generally available on May 17, 2023.
. On July 19, August 16, and September 2, 2024, the customer is notified that their cluster will enter "Limited Support" status on September 17, 2024 if the cluster has not already been upgraded to a supported minor version.
. The cluster must be upgraded to 4.14 or later by September 17, 2024.
. If the upgrade has not been performed, the cluster's control plane will be automatically upgraded to 4.14.26, and there will be no automatic upgrades to the cluster's worker nodes.
. If the upgrade has not been performed, the cluster will be flagged as being in a "Limited Support" status.

[role="_additional-resources"]
.Additional resources
* OpenShift Container Platform limited support status

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-patch-versions_{context}"]
= Patch versions (x.y.Z)

[role="_abstract"]
During the period in which a minor version is supported, Red{nbsp}Hat supports all OpenShift Container Platform patch versions unless otherwise specified.

For reasons of platform security and stability, a patch release may be deprecated, which would prevent installations of that release and trigger mandatory upgrades off that release.

.Example
. 4.7.6 is found to contain a critical CVE.
. Any releases impacted by the CVE will be removed from the supported patch release list. In
  addition, any clusters running 4.7.6 will be scheduled for automatic upgrades within 48 hours.
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-limited-support_{context}"]
= Limited support status

[role="_abstract"]
When a cluster transitions to a _Limited Support_ status, Red{nbsp}Hat no longer proactively monitors the cluster, the SLA is no longer applicable, and credits requested against the SLA are denied. It does not mean that you no longer have product support. In some cases, the cluster can return to a fully-supported status if you remediate the violating factors. However, in other cases, you might have to delete and recreate the cluster.

A cluster might transition to a Limited Support status for many reasons, including the following scenarios:

If you do not upgrade a cluster to a supported version before the end-of-life date:: Red{nbsp}Hat does not make any runtime or SLA guarantees for versions after their end-of-life date. To receive continued support, upgrade the cluster to a supported version before the end-of-life date. If you do not upgrade the cluster before the end-of-life date, the cluster transitions to a Limited Support status until it is upgraded to a supported version.
+
Red{nbsp}Hat provides commercially reasonable support to upgrade from an unsupported version to a supported version. However, if a supported upgrade path is no longer available, you might have to create a new cluster and migrate your workloads.

If you remove or replace any native OpenShift Container Platform components or any other component that is installed and managed by Red{nbsp}Hat:: If cluster administrator permissions were used, Red{nbsp}Hat is not responsible for any of your or your authorized users’ actions, including those that affect infrastructure services, service availability, or data loss. If Red{nbsp}Hat detects any such actions, the cluster might transition to a Limited Support status. Red{nbsp}Hat notifies you of the status change and you should either revert the action or create a support case to explore remediation steps that might require you to delete and recreate the cluster.

If you have questions about a specific action that might cause a cluster to transition to a Limited Support status or need further assistance, open a support ticket.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-supported-versions_{context}"]
= Supported versions exception policy

[role="_abstract"]
Red{nbsp}Hat reserves the right to add or remove new or existing versions, or delay upcoming minor release versions, that have been identified to have one or more critical production impacting bugs or security issues without advance notice.
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-install-policy_{context}"]
= Installation policy

[role="_abstract"]
While Red{nbsp}Hat recommends installation of the latest support release, OpenShift Container Platform supports
installation of any supported release as covered by the preceding policy.
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
[id="rosa-delete-policy_{context}"]
= Deletion policy

Red{nbsp}Hat reserves the right to delete OpenShift Container Platform clusters within 15 days if the service notifications requiring actions are not addressed. These actions include upgrading the cluster to a supported OpenShift version or resolving cluster health issues so that the service can auto-upgrade the cluster to a supported OpenShift version.

OpenShift Container Platform services will notify you when the cluster is unhealthy and when the OpenShift version is approaching EOL.

[IMPORTANT]
====
OpenShift Container Platform clusters configured with delete protection enabled can still be deleted based on the deletion policy.
====

If a OpenShift Container Platform cluster is deleted, any applications or business hosted on the cluster will be impacted. Additionally, cloud resources may remain in the AWS account after cluster deletion, which will continue to incur costs.

// Module included in the following assemblies:
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="rosa-mandatory-upgrades_{context}"]
= Mandatory upgrades

[role="_abstract"]
If a critical or important CVE, or other bug identified by Red{nbsp}Hat, significantly impacts the security or stability of the cluster, the customer must upgrade to the next supported patch release within two business days.

In extreme circumstances and based on Red{nbsp}Hat's assessment of the CVE criticality to the environment, Red{nbsp}Hat will notify customers that they have two business days to schedule or manually update their cluster to the latest, secure patch release. In the case that an update is not performed after two business days, Red{nbsp}Hat will automatically update the
cluster's control plane
cluster
to the latest, secure patch release to mitigate potential security breach(es) or instability. Red{nbsp}Hat might, at its own discretion, temporarily delay an automated update if requested by a customer through a support case.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-life-cycle.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-life-cycle.adoc
// * osd_architecture/osd_policy/osd-life-cycle.adoc

[id="sd-life-cycle-dates_{context}"]
= Life cycle dates

[role="_abstract"]
The following table lists the general availability, maintenance support end date, and Extended Update Support Add-On - Term 1 end date for each supported OpenShift Container Platform version.

[options="header"]
|===
|Version    |General availability   |Maintenance support ends  |Extended Update Support Add-On - Term 1 ends
|4.22       |Jun  9, 2026           |Dec 31, 2027              |Jun 30, 2028
|4.21       |Feb  4, 2026           |Aug  3, 2027              |
|4.20       |Oct 21, 2025           |Apr 21, 2027              |Oct 21, 2027
|4.19       |Jun 17, 2025           |Dec 17, 2026              |
|4.18       |Feb 25, 2025           |Aug 25, 2026              |Feb 25, 2027
|4.17       |Oct  1, 2024           |Apr  1, 2026              |
|4.16       |Jun 27, 2024           |Dec 27, 2025              |Jun 27, 2026
|===

The Extended Update Support Add-On - Term 1 is available for OpenShift Container Platform customers using even-numbered versions, starting with 4.16, and is included with your OpenShift Container Platform subscription.

The Extended Update Support Add-On - Term 1 provides the key benefit of extending the support lifecycle for an eligible minor release from 18 months to a total of 24 months. This 6-month extension allows organizations to maintain stability for mission-critical applications, meet complex regulatory validation schedules, and manage limited maintenance windows by providing continued access to critical and important security updates and urgent-priority bug fixes without requiring a full version upgrade.

To apply Extended Update Support Add-On - Term 1 to your OpenShift Container Platform cluster, you must update the channel group to `eus`.

//Conditionalizing the admonition below as the ability to have separate version control for CPs and MPs are a feature of ROSA w/HCP only
[IMPORTANT]
=====
Before upgrading your cluster from version 4.16 to version 4.18, confirm that your control plane and machines pools are using version 4.16.
See _Upgrade options for OpenShift Container Platform clusters_ in the _Additional resources_ section for more information.
=====
[id="govcloud-life-cycle-dates_{context}"]
= Life cycle dates for OpenShift Container Platform in AWS GovCloud

OpenShift Container Platform in AWS GovCloud is subject to FedRAMP high security controls which require the use of cryptographic modules that have received a validation status of active or implementation under test from the Cryptographic Module Validation Program (CMVP). As a result, OpenSSL which is the module that is applicable to RHEL CoreOS in an OpenShift implementation is the determining factor for what OpenShift versions OpenShift Container Platform in AWS GovCloud offers, which may create drift from the standard OpenShift support lifecycle.

[options="header"]
|===
|Version    |General availability   |Maintenance support ends |Extended Update Support Add-On - Term 1 ends
|4.18       |Feb 25, 2025           |Aug 25, 2026              |Feb 25, 2027
|4.17       |Oct  1, 2024           |Apr  1, 2026               |
|4.16       |Oct 20, 2025           |Jun 27, 2026 |Jun 27, 2026
|4.15       |May 9, 2025           |Dec 1, 2025   |
|===

The Extended Update Support Add-On - Term 1 is available for OpenShift Container Platform in AWS GovCloud customers using even-numbered versions, starting with 4.16, and is included with your OpenShift Container Platform in AWS GovCloud subscription.

The Extended Update Support Add-On - Term 1 provides the key benefit of extending the support lifecycle for an eligible minor release from 18 months to a total of 24 months. This 6-month extension allows organizations to maintain stability for mission-critical applications, meet complex regulatory validation schedules, and manage limited maintenance windows by providing continued access to critical and important security updates and urgent-priority bug fixes without requiring a full version upgrade.

To apply Extended Update Support Add-On - Term 1 to your OpenShift Container Platform in AWS GovCloud cluster, you must update the channel group to `eus`.

.Additional resources
* ROSA CLI command reference
* Upgrade options for OpenShift Container Platform clusters
