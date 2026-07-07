---
title: "{PM-title-c} 0.5 (Technology Preview) release notes"
type: reference
domain: openshift
slug: observability-4-22-power-monitoring-release-notes-tp-0-5
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/power-monitoring-release-notes-tp-0-5
version: 4.22
family: observability
documentKind: "Documentation"
---

# {PM-title-c} 0.5 (Technology Preview) release notes

[id="power-monitoring-assembly-tp-0-5-release-notes_{context}"]
= {PM-title-c} 0.5 (Technology Preview) release notes

//:FeatureName: Power monitoring
//include::snippets/technology-preview.adoc[leveloffset=+2]
{PM-title-c} enables you to monitor the power usage of workloads and identify the most power-consuming namespaces running in an OpenShift Container Platform cluster with key power consumption metrics, such as CPU or DRAM, measured at container level.
These release notes track the development of {PM-title} in the OpenShift Container Platform.

For an overview of the {PM-operator}, see About {PM-shortname}.

// Module included in the following assemblies:

// * power_monitoring/power-monitoring-assembly-tp-0-5-release-notes.adoc

[id="power-monitoring-tp-0-5-overview_{context}"]
= Power monitoring 0.5 (Technology Preview) release notes overview

{PM-title-c} enables you to monitor the power usage of workloads and identify the most power-consuming namespaces running in an OpenShift Container Platform cluster with key power consumption metrics, such as CPU or DRAM, measured at container level.

This release of power monitoring and the {PM-operator} provides more accurate data, includes new dashboards, and removes some features and functionality.

This release of power monitoring and the {PM-operator} is supported on:

* OpenShift Container Platform 4.17+
* Bare metal deployments

//following new release notes template in GDoc from release notes team
// Module included in the following assemblies:

// * power_monitoring/power-monitoring-tp-0-5-release-notes.adoc

[id="power-monitoring-release-notes-tp-0-5-new-features_{context}"]
= Power monitoring Technology Preview 0.5 new features

This release of {PM-title} and the {PM-operator}, based on the Kepler Project, includes the following new feature:

* Deployment and deletion of `PowerMonitor` custom resource definition (CRD).
// Module included in the following assemblies:

// * power_monitoring/power-monitoring-tp-0-5-release-notes.adoc

[id="power-monitoring-tp-0-5-enhancements_{context}"]
= Power monitoring Technology Preview 0.5 enhancements

This release of {PM-title} and the {PM-operator}, based on the Kepler Project, includes the following enhancements:

* Dynamic detection of Nodes Running Average Power Limit (RAPL) zones
* More accurate power measurement based on active CPU usage
* Improved Virtual Machine (VM), container, and pod detection
* More relevant label values for processes, containers, VMs, and pods
* Requires only `readonly` access to host: `/proc` and `/sys`
** No more `CAP_SYSADMIN` and `CAP_BPF`
* Significantly reduced resource usage compared to earlier Kepler implementations
* Multi-level energy tracking for the following levels:
** node
** process
** container
** VM
** pod
* Terminated workload tracking with configurable retention policies
* Energy-based prioritization for terminated resources
* Real-time data collection with configurable intervals and staleness detection

[id="updated-dashboards_{context}"]
== Updated dashboards

With this update, {PM-title} has the following dashboard changes:

* Updated *Power Monitor / Overview* dashboard.
* Updated *Power Monitor / Namespace (Pods)* dashboard.

[IMPORTANT]
====
The older metrics and dashboards are no longer supported. If you are managing your own custom dashboard or queries, you need to update to the newer versions.
====

// Module included in the following assemblies:

// * power_monitoring/power-monitoring-assembly-tp-0-5-release-notes.adoc

[id="power-monitoring-0-5-deprecated-removed-features_{context}"]
= Power monitoring 0.5 (Technology Preview) deprecated and removed features

* In the Red Hat OpenShift power monitoring technology preview 0.5 release, the `Kepler` custom resource has been deprecated, and will be removed in a future release. Use the `PowerMonitor` custom resource instead.

* In the Red Hat OpenShift power monitoring technology preview 0.5 release, the Redfish configuration has been removed. It is no longer supported in previous versions of power monitoring.
// Module included in the following assemblies:

// * power_monitoring/power-monitoring-assembly-tp-0-5-release-notes.adoc

[id="power-monitoring-release-notes-tp-0-5-support-tables_{context}"]
= {PM-shortname-c} 0.5 (Technology Preview) support tables

//may need to update the title
This release includes the following support updates:

.Power Monitoring Operator supported version table
[cols="1,1"]
|===
|{PM-kepler}
|0.10.2
|{PM-operator}
|0.20.0
|===

.Power monitoring supported platforms
[cols="1,1"]
|===
|OpenShift Container Platform
|4.17+
|Bare metal
| X
|===

[IMPORTANT]
====
Installations in virtual machines are not supported and will not function.
====

//* With this update, Red Hat OpenShift power monitoring is only supported on OpenShift Container Platform clusters that are installed on bare metal. Installations in virtual machines are not support and will not function.
//will likely need to create a reference module for a Feature Support Table or some kind for this bullet point on supported cluster installation platforms.
