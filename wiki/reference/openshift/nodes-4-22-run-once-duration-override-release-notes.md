---
title: "Run Once Duration Override Operator release notes"
type: reference
domain: openshift
slug: nodes-4-22-run-once-duration-override-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/run-once-duration-override-release-notes
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Run Once Duration Override Operator release notes

[id="run-once-duration-override-release-notes"]
= Run Once Duration Override Operator release notes

[role="_abstract"]
Cluster administrators can use the {run-once-operator} to force a limit on the time that run-once pods can be active. After the time limit expires, the cluster tries to terminate the run-once pods. The main reason to have such a limit is to prevent tasks such as builds to run for an excessive amount of time.

To apply the run-once duration override from the {run-once-operator} to run-once pods, you must enable it on each applicable namespace.

These release notes track the development of the {run-once-operator} for OpenShift Container Platform.

For an overview of the {run-once-operator}, see About the {run-once-operator}.

//1.4.1 release notes
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-release-notes.adoc

[id="rodoo-rn-1-4-1_{context}"]
= {run-once-operator} 1.4.1

[role="_abstract"]
Review the features, enhancements, and advisory for the release of {run-once-operator} 1.4.1.

Issued: 17 June 2026

The following advisory is available for the {run-once-operator} 1.4.1:

* RHBA-2026:26526

[id="rodoo-1-4-1-new-features-and-enhancements_{context}"]
== New features and enhancements

* This release of the {run-once-operator} updates the Kubernetes version to 1.35.

[id="rodoo-rn-1-4-1-bug-fixes_{context}"]
== Bug fixes

* This release of the {run-once-operator} addresses several Common Vulnerabilities and Exposures (CVEs).

//1.4.0 release notes
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-release-notes.adoc

[id="rodoo-rn-1-4-0_{context}"]
= {run-once-operator} 1.4.0

[role="_abstract"]
Review the features, enhancements, and advisory for the release of {run-once-operator} 1.4.0.

Issued: 12 February 2026

The following advisory is available for the {run-once-operator} 1.4.0:

* RHBA-2026:2649

[id="rodoo-1-4-0-new-features-and-enhancements_{context}"]
== New features and enhancements

* This release of the {run-once-operator} updates the Kubernetes version to 1.34.

* Users should set `.spec.managementState: Managed` in {run-once-operator} 1.4.0 custom resources (CR). In a future release, the `spec.managementState` field in the {run-once-operator} CR will be required to be set to `Managed`.

[id="rodoo-rn-1-4-0-bug-fixes_{context}"]
== Bug fixes

* This release of the {run-once-operator} addresses several Common Vulnerabilities and Exposures (CVEs).
