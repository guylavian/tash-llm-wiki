---
title: "Viewing Operator metrics"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-metrics
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Viewing Operator metrics

[id="nodes-cma-autoscaling-custom-metrics"]
= Viewing Operator metrics

The Custom Metrics Autoscaler Operator exposes ready-to-use metrics that it pulls from the on-cluster monitoring component. You can query the metrics by using the Prometheus Query Language (PromQL) to analyze and diagnose issues. All metrics are reset when the controller pod restarts.

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-metrics.adoc
// Modeled after migration-accessing-performance-metrics.adoc

[id="nodes-cma-autoscaling-custom-metrics-access_{context}"]
= Accessing performance metrics

You can access the metrics and run queries by using the OpenShift Container Platform web console.

.Procedure

. Select the *Administrator* perspective in the OpenShift Container Platform web console.

. Select *Observe* -> *Metrics*.

. To create a custom query, add your PromQL query to the *Expression* field.

. To add multiple queries, select *Add Query*.

// Procedure copied from monitoring-querying-metrics-for-all-projects-as-an-administrator

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-metrics.adoc

[id="nodes-cma-autoscaling-custom-metrics-provided_{context}"]
= Provided Operator metrics

The Custom Metrics Autoscaler Operator exposes the following metrics, which you can view by using the OpenShift Container Platform web console.

.Custom Metric Autoscaler Operator metrics

[cols="3,7",options="header"]
|===
|Metric name
|Description

|`keda_scaler_activity`
|Whether the particular scaler is active or inactive. A value of `1` indicates the scaler is active; a value of `0` indicates the scaler is inactive.

|`keda_scaler_metrics_value`
|The current value for each scaler’s metric, which is used by the Horizontal Pod Autoscaler (HPA) in computing the target average.

|`keda_scaler_metrics_latency`
|The latency of retrieving the current metric from each scaler.

|`keda_scaler_errors`
|The number of errors that have occurred for each scaler.

|`keda_scaler_errors_total`
|The total number of errors encountered for all scalers.

|`keda_scaled_object_errors`
|The number of errors that have occurred for each scaled obejct.

|`keda_resource_totals`
|The total number of Custom Metrics Autoscaler custom resources in each namespace for each custom resource type.

|`keda_trigger_totals`
|The total number of triggers by trigger type.

|===

.Custom Metrics Autoscaler Admission webhook metrics

The Custom Metrics Autoscaler Admission webhook also exposes the following Prometheus metrics.

[cols="3,7"options="header"]
|===
|Metric name
|Description

|`keda_scaled_object_validation_total`
|The number of scaled object validations.

|`keda_scaled_object_validation_errors`
|The number of validation errors.

|===
