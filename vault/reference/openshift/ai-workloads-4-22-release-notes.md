---
title: "Release notes"
type: reference
domain: openshift
slug: ai-workloads-4-22-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/release-notes
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Release notes

[id="release-notes"]
= Release notes

{kueue-name} is released as an Operator that is supported on OpenShift Container Platform.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc
// * ai_workloads/kueue/release-notes.adoc

[id="compatible-environments_{context}"]
= Compatible environments

Before you install {kueue-name}, review this section to ensure that your cluster meets the requirements.

[id="compatible-environments-arch_{context}"]
== Supported architectures

{kueue-name} version 1.1 and later is supported on the following architectures:

* ARM64
* 64-bit x86
* ppc64le ({ibm-power-name})
* s390x ({ibm-z-name})

[id="compatible-environments-platforms_{context}"]
== Supported platforms

{kueue-name} version 1.1 and later is supported on the following platforms:

* OpenShift Container Platform
* {hcp-capital} for OpenShift Container Platform

[IMPORTANT]
====
Currently, {kueue-name} is not supported on {ms}.
====

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="release-notes-1.3.1_{context}"]
= Release notes for {kueue-name} version 1.3.1

[role="_abstract"]
{kueue-name} version 1.3.1 is a generally available release that is supported on OpenShift Container Platform versions 4.18 and later. {kueue-name} version 1.3 uses Kueue version 0.16.5.

[id="release-notes-1.3.1-fixed-issues_{context}"]
== Fixed issues

kueue.x-k8s.io/queue-name refers to a non-existent queue::
Fixed a bug where referencing a non-existent `LocalQueue via kueue.x-k8s.io/queue-name` could cause a running pod to be terminated and permanently stuck with unremovable scheduling gates.
+
(OCPBUGS-78789)

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="release-notes-1.3_{context}"]
= Release notes for {kueue-name} version 1.3

[role="_abstract"]
{kueue-name} version 1.3 is a generally available release that is supported on OpenShift Container Platform versions 4.18 and later. {kueue-name} version 1.3 uses Kueue version 0.16.

[id="release-notes-1.3-new-features_{context}"]
== New features and enhancements

{lws-operator}::
{kueue-name} version 1.3 provides for the integration of the {lws-operator} with {kueue-name} so you can leverage the {kueue-name} scheduling and resource management functionality when running LeaderWorkerSets. For more information, see Integrating the Leader Worker Set Operator.

{js-operator}::
{kueue-name} version 1.3 provides for the integration of the {js-operator} so you can use the {js-operator} to manage and run large-scale, coordinated workloads like high-performance computing (HPC) and AI training. For more information, see Integrating the JobSet Operator.

Upstream progression of the {kueue-name} API to `v1beta2`::
{kueue-name} version 1.3 provides the `v1beta2` version of the {kueue-name} API. This update continues the evolution of the {kueue-name} APIs with the ultimate goal of graduating the API to `v1`.
+
All new Kueue objects created after the upgrade will be stored using the `v1beta2` version. The earlier version of the API, `v1beta1` is deprecated. Objects can still be created using `v1beta1`, if necessary. In these cases, a deprecation message is shown.
+
However, existing objects are only auto-converted to the new storage version by Kubernetes during a write request. This means that {kueue-name} API objects that rarely receive updates such as Topologies, ResourceFlavors, or long-running Workloads could remain in the older `v1beta1` format indefinitely.

[id="release-notes-1.3-fixed-issues_{context}"]
== Fixed issues

Reconcile jobs only in opt-in namespaces::
OpenShift Container Platform allowed reconciliation of `Job` resources that have the `kueue.x-k8s.io/queue-name` label, even if these resources are in namespaces that are not configured to opt in to being managed by OpenShift Container Platform. With this release, there is ongoing upstream work that updates this behavior so that Jobs with queue-name labels are also ignored unless their namespace matches the `managedJobsNamespaceSelector`. This change makes {kueue-name} behavior consistent across all integrations.
+
(OCPBUGS-58205)

`Kueue` CR description reads as "Not available" in the OpenShift Container Platform web console::
After installing {kueue-name}, in the *Operator details* view, the description for the `Kueue` CR read as "Not available". This issue did not affect or degrade the {kueue-name} Operator functionality. With this release, the "Not available" message no longer displays.
+
(OCPBUGS-62185)

LeaderWorkerSet and Jobset validation errors::
Currently, the {lws-operator} and {js-operator} are only validated after the Operand CR is updated and the full Kueue hierarchy (ResourceFlavor, ClusterQueue, and LocalQueue) is established. Any configuration errors appear only when applying a LeaderWorkerSet or JobSet template.
+
(OCPBUGS-74210)

[id="release-notes-1.3-known-issues_{context}"]
== Known issues

LeaderWorkerSet pods update sequentially by default::
If you have integrated {lws-operator} with your {kueue-name} installation and you are using the rollout strategy option for updating LeaderWorkerSet pods, be aware that the `MaxUnavailable` feature gate in OpenShift Container Platform is disabled by default.
+
When any change is made to LeaderWorkerSet pods, a rolling update is triggered. This action gradually replaces the old pods of a deployment with new ones, keeping as many pods alive as possible to avoid downtime. If `MaxUnavailable` is disabled, which is the OpenShift Container Platform default setting, the pods are updated one at a time.
+
If you want to run updates in parallel instead of running them sequentially, `MaxUnavailable` feature gate must be enabled. For more information, see Enabling feature sets at installation and Rollout Strategy.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="release-notes-1.2_{context}"]
= Release notes for {kueue-name} version 1.2

[role="_abstract"]
{kueue-name} version 1.2 is a generally available release that is supported on OpenShift Container Platform versions 4.18 and later. {kueue-name} version 1.2 uses Kueue version 0.14.

[id="release-notes-1.2-new-features_{context}"]
== New features and enhancements

Monitoring of pending workloads::
{kueue-name} version 1.2 provides the `VisibilityOnDemand` feature to monitor the pipeline of pending jobs in the cluster queue and the local queue, and help users to estimate when their jobs will start. For more information, see Monitoring pending workloads.

[id="release-notes-1.2-fixed-issues_{context}"]
== Fixed issues

Custom resources are not deleted properly when you uninstall {kueue-name}::
After you uninstall the {kueue-op} using the *Delete all operand instances for this operator* option in the OpenShift Container Platform web console, {kueue-name} custom resources were attempted to be deleted. With this release, they are not considered for deletion.
+
(OCPBUGS-62254)

Documentation error in previous versions of {kueue-name}::
In Creating a Kueue custom resource, the optional workload types `Pod`, `Deployment`, `StatefulSet` were omitted. They are now included.
+
(OCPBUGS-62877)

{kueue-name} metrics were not being exposed to Prometheus from version 1.1::
Prometheus was not scraping metrics from the Operator's controller, even though the ServiceMonitor and RBAC resources were successfully created as part of the Operator installation. As a result, none of the Kueue metrics were available in the cluster monitoring stack.
+
The metrics service added during the installation was configured with an incorrect port reference, causing Prometheus to fail in scraping metrics from the Kueue endpoint. The port name has been updated with the correct port name.
+
(OCPBUGS-63441)

[id="release-notes-1.2-known-issues_{context}"]
== Known issues

Reconcile jobs only in opt-in namespaces::
OpenShift Container Platform allows reconciliation of `Job` resources that have the `kueue.x-k8s.io/queue-name` label, even if these resources are in namespaces which are not configured to opt in to being managed by OpenShift Container Platform. This is inconsistent with the behavior for other core integrations like pods, deployments, and stateful sets, which are only reconciled if they are in namespaces which have been configured to opt in to being managed by OpenShift Container Platform by adding the `kueue.openshift.io/managed=true`.
+
(OCPBUGS-58205)

`Kueue` CR description reads as "Not available" in the OpenShift Container Platform web console::
After installing {kueue-name}, in the *Operator details* view, the description for the `Kueue` CR reads as "Not available". This issue does not affect or degrade the {kueue-name} Operator functionality.
+
(OCPBUGS-62185)

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="kueue-release-notes-1.1_{context}"]
= Release notes for {kueue-name} version 1.1

[role="_abstract"]
{kueue-name} version 1.1 is a generally available release that is supported on OpenShift Container Platform versions 4.18 and later. {kueue-name} version 1.1 uses Kueue version 0.12.

[IMPORTANT]
====
If you have a previously installed version of {kueue-name} on your cluster, you must uninstall the Operator and manually install version 1.1. For information see Upgrading {kueue-name}.
====

[id="release-notes-1.1-new-features_{context}"]
== New features and enhancements

Configure a default local queue:: A default local queue serves as the local queue for newly created jobs that do not have the `kueue.x-k8s.io/queue-name` label. After you create a default local queue, any new jobs created in the namespace without a `kueue.x-k8s.io/queue-name` label automatically update to have the `kueue.x-k8s.io/queue-name: default` label.
+
(RFE-7615)

Multi-architecture and {hcp-capital} support:: With this release, {kueue-name} is supported on multiple different architectures, including ARM64, 64-bit x86, ppc64le ({ibm-power-name}), and s390x ({ibm-z-name}), as well as on {hcp-capital} for OpenShift Container Platform.
+
(OCPSTRAT-2103)
+
(OCPSTRAT-2106)

[id="release-notes-1.1-fixed-issues_{context}"]
== Fixed issues

You can create a `Kueue` custom resource by using the OpenShift Container Platform web console:: Before this update, if you tried to use the OpenShift Container Platform web console to create a `Kueue` custom resource (CR) by using the form view, the web console showed an error and the resource could not be created. With this release, the default namespace was removed from the `Kueue` CR template. As a result, you can use the OpenShift Container Platform web console to create a `Kueue` CR by using the form view.
+
(OCPBUGS-58118)

[id="release-notes-1.1-known-issues_{context}"]
== Known issues

`Kueue` CR description reads as "Not available" in the OpenShift Container Platform web console:: After you install {kueue-name}, in the *Operator details* view, the description for the `Kueue` CR reads as "Not available". This issue does not affect or degrade the {kueue-name} Operator functionality.
+
(OCPBUGS-62185)

Custom resources are not deleted properly when you uninstall {kueue-name}:: After you uninstall the {kueue-op} using the *Delete all operand instances for this operator* option in the OpenShift Container Platform web console, some {kueue-name} custom resources are not fully deleted. These resources can be viewed in the *Installed Operators* view with the status *Resource is being deleted*. As a workaround, you can manually delete the resource finalizers to remove them fully.
+
(OCPBUGS-62254)

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="release-notes-1.0.1_{context}"]
= Release notes for {kueue-name} version 1.0.1

{kueue-name} version 1.0.1 is a patch release that is supported on OpenShift Container Platform versions 4.18 and 4.19 on the 64-bit x86 architecture.

{kueue-name} version 1.0.1 uses Kueue version 0.11.

[id="release-notes-1.0.1-bug-fixes_{context}"]
== Bug fixes in {kueue-name} version 1.0.1

* Previously, leader election for {kueue-name} was not configured to tolerate disruption, which resulted in frequent crashing. With this release, the leader election values for {kueue-name} have been updated to match the durations recommended for OpenShift Container Platform. (OCPBUGS-58496)

* Previously, the `ReadyReplicas` count was not set in the reconciler, which meant that the {kueue-name} Operator status would report that there were no replicas ready. With this release, the `ReadyReplicas` count is based on the number of ready replicas for the deployment, which ensures that the Operator shows as ready in the OpenShift Container Platform console when the `kueue-controller-manager` pods are ready. (OCPBUGS-59261)

* Previously, when the `Kueue` custom resource (CR) was deleted from the `openshift-kueue-operator` namespace, the `kueue-manager-config` config map was not deleted automatically and could remain in the namespace. With this release, the `kueue-manager-config` config map, `kueue-webhook-server-cert` secret, and `metrics-server-cert` secret are deleted automatically when the `Kueue` CR is deleted. (OCPBUGS-57960)

// Module included in the following assemblies:
//
// * ai_workloads/kueue/release-notes.adoc

[id="release-notes-1.0_{context}"]
= Release notes for {kueue-name} version 1.0

[role="_abstract"]
{kueue-name} version 1.0 is a generally available release that is supported on OpenShift Container Platform versions 4.18 and 4.19 on the 64-bit x86 architecture. {kueue-name} version 1.0 uses Kueue version 0.11.

[id="release-notes-1.0-new-features_{context}"]
== New features and enhancements

Role-based access control (RBAC):: Role-based access control (RBAC) enables you to control which types of users can create which types of {kueue-name} resources.

Configure resource quotas:: Configuring resource quotas by creating cluster queues, resource flavors, and local queues enables you to control the amount of resources used by user-submitted jobs and workloads.

Control job and workload management:: Labeling namespaces and configuring label policies enable you to control which jobs and workloads are managed by {kueue-name}.

Share borrowable resources between queues:: Configuring cohorts, fair sharing, and gang scheduling settings enable you to share unused, borrowable resources between queues.

[id="release-notes-1.0-known-issues_{context}"]
== Known issues

Jobs in all namespaces are reconciled if they have the `kueue.x-k8s.io/queue-name` label:: {kueue-name} uses the `managedJobsNamespaceSelector` configuration field, so that administrators can configure which namespaces opt in to be managed by {kueue-name}. Because namespaces must be manually configured to opt in to being managed by {kueue-name}, resources in system or third-party namespaces are not impacted or managed by {kueue-name}.
+
The behavior in {kueue-name} 1.0 allows reconciliation of `Job` resources that have the `kueue.x-k8s.io/queue-name` label, even if these resources are in namespaces that are not configured to opt in to being managed by {kueue-name}. This is inconsistent with the behavior for other core integrations like pods, deployments, and stateful sets, which are only reconciled if they are in namespaces that have been configured to opt in to being managed by {kueue-name}.
+
(OCPBUGS-58205)

You cannot create a `Kueue` custom resource by using the OpenShift Container Platform web console:: If you try to use the OpenShift Container Platform web console to create a `Kueue` custom resource (CR) by using the form view, the web console shows an error and the resource cannot be created. As a workaround, use the YAML view to create a `Kueue` CR instead.
+
(OCPBUGS-58118)
