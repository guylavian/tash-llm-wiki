---
title: "Support"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-support
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-support
version: 4.22
family: observability
documentKind: "Documentation"
---

# Support

[id="cluster-logging-support"]
= Support

{logging-uc} {for} is an opinionated collector and normalizer of application, infrastructure, and audit logs. You can use it to forward logs to various supported systems.

{logging-uc} is not:

* A high scale log collection system
* Security Information and Event Monitoring (SIEM) compliant
* A "bring your own" (BYO) log collector configuration
* Historical or long term log retention or storage
* A guaranteed log sink
* Secure storage - audit logs are not stored by default

[id="cluster-logging-support-CRDs_{context}"]
== Supported API custom resource definitions

The following table describes the supported {logging-uc} APIs.

.Loki API support states
[cols="3",options="header"]
|===
|CustomResourceDefinition (CRD)
|ApiVersion
|Support state

|LokiStack
|lokistack.loki.grafana.com/v1
|Supported from 5.5

|RulerConfig
|rulerconfig.loki.grafana/v1
|Supported from 5.7

|AlertingRule
|alertingrule.loki.grafana/v1
|Supported from 5.7

|RecordingRule
|recordingrule.loki.grafana/v1
|Supported from 5.7

|LogFileMetricExporter
|LogFileMetricExporter.logging.openshift.io/v1alpha1
|Supported from 5.8

|ClusterLogForwarder
|clusterlogforwarder.logging.openshift.io/v1
|Supported from 4.5.
|===

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-support.adoc

[id="cluster-logging-maintenance-support-list_{context}"]
= Unsupported configurations

You must set the Red{nbsp}Hat OpenShift Logging Operator to the `Unmanaged` state to modify the following components:

* The `fluent.conf` file

* The Fluentd daemon set

* The `vector.toml` file for Vector collector deployments

Explicitly unsupported cases include:

* *Configuring the collected log location*. You cannot change the location of the log collector output file, which by default is `/var/log/fluentd/fluentd.log`.

* *Throttling log collection*. You cannot throttle down the rate at which the logs are read in by the log collector.

* *Configuring the logging collector using environment variables*. You cannot use environment variables to modify the log collector.

* *Configuring how the log collector normalizes logs*. You cannot modify default log normalization.
// Module included in the following assemblies:
//
// * architecture/architecture-installation.adoc
// * updating/updating-cluster-within-minor.adoc
// * observability/logging/cluster-logging-support.adoc

[id="unmanaged-operators_{context}"]
= Support policy for unmanaged Operators

The _management state_ of an Operator determines whether an Operator is actively
managing the resources for its related component in the cluster as designed. If
an Operator is set to an _unmanaged_ state, it does not respond to changes in
configuration nor does it receive updates.

While this can be helpful in non-production clusters or during debugging,
Operators in an unmanaged state are unsupported and the cluster administrator
assumes full control of the individual component configurations and upgrades.

An Operator can be set to an unmanaged state using the following methods:

* **Individual Operator configuration**
+
Individual Operators have a `managementState` parameter in their configuration.
This can be accessed in different ways, depending on the Operator. For example,
the Red Hat OpenShift Logging Operator accomplishes this by modifying a custom resource
(CR) that it manages, while the Cluster Samples Operator uses a cluster-wide
configuration resource.
+
Changing the `managementState` parameter to `Unmanaged` means that the Operator
is not actively managing its resources and will take no action related to the
related component. Some Operators might not support this management state as it
might damage the cluster and require manual recovery.
+
[WARNING]
====
Changing individual Operators to the `Unmanaged` state renders that particular
component and functionality unsupported. Reported issues must be reproduced in
`Managed` state for support to proceed.
====

* **Cluster Version Operator (CVO) overrides**
+
The `spec.overrides` parameter can be added to the CVO's configuration to allow
administrators to provide a list of overrides to the CVO's behavior for a
component. Setting the `spec.overrides[].unmanaged` parameter to `true` for a
component blocks cluster upgrades and alerts the administrator after a CVO
override has been set:
+
[source,terminal]
----
Disabling ownership via cluster version overrides prevents upgrades. Please remove overrides before continuing.
----
+
[WARNING]
====
Setting a CVO override puts the entire cluster in an unsupported state. Reported
issues must be reproduced after removing any overrides for support to proceed.
====

[id="cluster-logging-support-must-gather_{context}"]
== Collecting logging data for Red Hat Support

When opening a support case, it is helpful to provide debugging information about your cluster to Red{nbsp}Hat Support.

You can use the must-gather tool to collect diagnostic information for project-level resources, cluster-level resources, and each of the {logging} components.
For prompt support, supply diagnostic information for both OpenShift Container Platform and {logging}.

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-support.adoc

[id="about-must-gather_{context}"]
= About the must-gather tool

The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues.

For your {logging}, `must-gather` collects the following information:

* Project-level resources, including pods, configuration maps, service accounts, roles, role bindings, and events at the project level
* Cluster-level resources, including nodes, roles, and role bindings at the cluster level
* OpenShift Logging resources in the `openshift-logging` and `openshift-operators-redhat` namespaces, including health status for the log collector, the log store, and the log visualizer

When you run `oc adm must-gather`, a new pod is created on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local`. This directory is created in the current working directory.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-support.adoc

[id="cluster-logging-must-gather-collecting_{context}"]
= Collecting {logging} data

You can use the `oc adm must-gather` CLI command to collect information about {logging}.

.Procedure

To collect {logging} information with `must-gather`:

. Navigate to the directory where you want to store the `must-gather` information.

. Run the `oc adm must-gather` command against the {logging} image:
+
[source,terminal]
----
$ oc adm must-gather --image=$(oc -n openshift-logging get deployment.apps/cluster-logging-operator -o jsonpath='{.spec.template.spec.containers[?(@.name == "cluster-logging-operator")].image}')
----
[source,terminal]
----
$ oc adm must-gather --image=quay.io/openshift/origin-cluster-logging-operator
----
+
The `must-gather` tool creates a new directory that starts with `must-gather.local` within the current directory. For example:
`must-gather.local.4157245944708210408`.

. Create a compressed file from the `must-gather` directory that was just created. For example, on a computer that uses a Linux operating system, run the following command:
+
[source,terminal]
----
$ tar -cvaf must-gather.tar.gz must-gather.local.4157245944708210408
----

. Attach the compressed file to your support case on the Red Hat Customer Portal.
