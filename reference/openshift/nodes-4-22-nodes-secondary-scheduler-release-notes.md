---
title: "{secondary-scheduler-operator-full} release notes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-secondary-scheduler-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-secondary-scheduler-release-notes
version: 4.22
family: nodes
documentKind: "Documentation"
---

# {secondary-scheduler-operator-full} release notes

[id="nodes-secondary-scheduler-release-notes"]
= {secondary-scheduler-operator-full} release notes

[role="_abstract"]
Review the {secondary-scheduler-operator-full} release notes to track its development and learn what is new and changed with each release.

The {secondary-scheduler-operator} allows you to deploy a custom secondary scheduler in your OpenShift Container Platform cluster.

For more information, see About the {secondary-scheduler-operator}.

// Release notes for Secondary Scheduler Operator for Red Hat OpenShift 1.6.0
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-release-notes.adoc

// This release notes module is allowed to contain xrefs. It must only ever be included from one assembly.

[id="secondary-scheduler-operator-release-notes-1.6.0_{context}"]
= Release notes for {secondary-scheduler-operator-full} 1.6.0

[role="_abstract"]
Review the release notes for {secondary-scheduler-operator} 1.6.0 to learn what is new and updated with this release.

Issued: 24 June 2026

The following advisory is available for the {secondary-scheduler-operator-full} 1.6.0:

* RHBA-2026:28915

[id="secondary-scheduler-1.6.0-new-features_{context}"]
== New features and enhancements

* You can now configure high availability for the {secondary-scheduler-operator}, ensuring continuous pod scheduling for specialized workloads during scheduler pod failures or maintenance. High availability eliminates the secondary scheduler as a single point of failure in production environments.
+
To enable high availability, set the topology mode to `HighlyAvailable` in the `SecondaryScheduler` custom resource (CR). In this mode, the Operator deploys multiple secondary scheduler replicas distributed across nodes, up to a configurable maximum. You can optionally set a node selector to target specific nodes or set tolerations for tainted nodes.
+
For more information, see Deploying a secondary scheduler.

* The {secondary-scheduler-operator} now publishes secondary scheduler metrics to Prometheus by default.

* This release of the {secondary-scheduler-operator} updates the Kubernetes version to 1.35.

[id="secondary-scheduler-1.6.0-bug-fixes_{context}"]
== Bug fixes

* This release of the {secondary-scheduler-operator} addresses Common Vulnerabilities and Exposures (CVEs).

[id="secondary-scheduler-operator-1.6.0-known-issues_{context}"]
== Known issues

* Currently, you cannot deploy additional resources, such as config maps, CRDs, or RBAC policies through the {secondary-scheduler-operator}. Any resources other than roles and role bindings that are required by your custom secondary scheduler must be applied externally. (WRKLDS-645)
