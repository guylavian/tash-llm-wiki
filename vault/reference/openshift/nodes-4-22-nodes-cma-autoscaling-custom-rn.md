---
title: "Custom Metrics Autoscaler Operator release notes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-rn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-rn
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Custom Metrics Autoscaler Operator release notes

[id="nodes-cma-autoscaling-custom-rn"]
= Custom Metrics Autoscaler Operator release notes

[role="_abstract"]
You can review the following release notes to learn about changes in the Custom Metrics Autoscaler Operator version 2.19.0-1. The release notes for the Custom Metrics Autoscaler Operator for Red Hat OpenShift describe new features and enhancements, deprecated features, and known issues.

The Custom Metrics Autoscaler Operator uses the Kubernetes-based Event Driven Autoscaler (KEDA) and is built on top of the OpenShift Container Platform horizontal pod autoscaler (HPA).

[NOTE]
====
The Custom Metrics Autoscaler Operator for Red Hat OpenShift is provided as an installable component, with a distinct release cycle from the core OpenShift Container Platform. The Red Hat OpenShift Container Platform Life Cycle Policy outlines release compatibility.
====

[id="nodes-pods-autoscaling-custom-rn-versions_{context}"]
== Supported versions

The following table defines the Custom Metrics Autoscaler Operator versions for each OpenShift Container Platform version.

[cols="3,7,3",options="header"]
|===
|Version
|OpenShift Container Platform version
|General availability

|2.19.0-1
|4.21
|General availability

|2.19.0-1
|4.20
|General availability

|2.19.0-1
|4.19
|General availability

|2.19.0-1
|4.18
|General availability

|2.19.0-1
|4.17
|General availability

|2.19.0-1
|4.16
|General availability

|2.19.0-1
|4.15
|General availability

|2.19.0-1
|4.14
|General availability

|2.19.0-1
|4.13
|General availability

|2.19.0-1
|4.12
|General availability
|===

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-rn/nodes-cma-autoscaling-custom-rn.adoc

[id="nodes-pods-autoscaling-custom-rn-2190_{context}"]
= Custom Metrics Autoscaler Operator 2.19.0-1 release notes

Issued: 17 June 2026

[role="_abstract"]
You can review the following release notes to learn about the bug fixes provided in this release of the Custom Metrics Autoscaler Operator.

The following advisory is available for the Custom Metrics Autoscaler Operator:

* RHSA-2026:26636

[IMPORTANT]
====
Before installing this version of the Custom Metrics Autoscaler Operator, remove any previously installed Technology Preview versions or the community-supported version of Kubernetes-based Event Driven Autoscaler (KEDA).
====

New features and enhancements::

Note the new features and enhancements in this release:

* Support for the `s390x` and `ppc64le` architectures
+
The Operator can now run on the `s390x` and `ppc64le` architectures. Previously it ran on `amd64` or `arm64` only. (AUTOSCALE-498)

* Network policy support for the Custom Metrics Autoscaler Operator
+
The Operator now has multiple network policies that control network traffic to and from the Operator and operand pods. These policies restrict traffic to only traffic that is explicitly allowed or required.

* Additional events for scaled objects and scaled jobs
+
Several new events have been added for scaled objects and scaled jobs. See ScaledObject/ScaledJob: emit more Events (KEDA PR) for the new events. See the KEDA Events reference (KEDA documentation) for the full list of events. (KEDA issue 7347)

* New status field for scaled objects and scaled jobs
+
A new `TriggersActivity` status field in scaled objects and scaled jobs reports the activity of each trigger in that object or job. Having per-activity tracking helps you understand which trigger is active and which is not. (KEDA issue 7382)

* New metric is now included in the raw metrics
+
A new metric has been added to the raw metrics stream that reports the current activity status of the triggers in a scaled object or scaled job. This metric indicates if the metric for the trigger is active, that is, above the `activationThreshold` value. This metric can help make the scaling decisions between KEDA and the metric consumer more consistent. (KEDA issue 7369)

Bug fixes::

* Before this update, the `accurateScalingStrategy` function in a scaled job was not considering the `pendingJobCount` value when checking if the `maxReplicaCount` value would be exceeded. This caused redundant idle jobs. With this release, this issue has been resolved and no longer causes redundant jobs. (KEDA bug 7329)

* Before this update, if the Azure Event Hub did not return partition information in the offset response, the Operator was accessing partition offsets without checking if the partitions exist. This caused incorrect lag calculations, which caused the Kafka scaler to error out. With this release, lag calculation treats missing partitions as having `0` lag instead of returning an error, resolving this issue. (KEDA bug 7309)
