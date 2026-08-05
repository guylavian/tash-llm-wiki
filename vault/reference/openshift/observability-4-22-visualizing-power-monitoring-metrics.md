---
title: "Visualizing power monitoring metrics"
type: reference
domain: openshift
slug: observability-4-22-visualizing-power-monitoring-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/visualizing-power-monitoring-metrics
version: 4.22
family: observability
documentKind: "Documentation"
---

# Visualizing power monitoring metrics

[id="visualizing-power-monitoring-metrics"]
= Visualizing power monitoring metrics

You can visualize {PM-shortname} metrics in the OpenShift Container Platform web console by accessing {PM-shortname} dashboards or by exploring *Metrics* under the *Observe* tab.

// Module included in the following assemblies:

// * power_monitoring/visualizing-power-monitoring-metrics.adoc

[id="power-monitoring-dashboards-overview_{context}"]
= {PM-shortname-c} dashboards overview

There are two types of {PM-shortname} dashboards. Both provide different levels of details around power consumption metrics for a single cluster:

[id="power-monitoring-overview-dashboard_{context}"]
== Power Monitor / Overview dashboard

This dashboard allows you to view the following information:

Cluster-wide power consumption:: View current total, active, and idle CPU power consumption, grouped by zones.
Node-level power details:: Analyze historical and current power consumption (total, active, and idle) for individual nodes.
Hardware information:: Display CPU model and core counts for each node in the cluster.
Time-series analysis:: Track power consumption trends over time with graphs that can be filtered by node and zone. This provides a comprehensive view of your cluster's energy usage.

[id="power-monitor-namespace-pods-dashboard_{context}"]
== Power Monitor / Namespace (Pods) dashboard

This dashboard allows you to monitor and analyze power consumption for Kubernetes namespaces and pods. It provides the following information:

Top ten power consuming namespaces:: A real-time table showing the top ten namespaces based on their current power usage. This helps you quickly identify the most resource-intensive workloads.
Total namespace power consumption:: A historical graph showing the total power consumption of pods within a selected namespace over time, grouped by zone. This helps you see trends and understand an application's or service's total power use.
Individual pod power consumption:: A detailed graph showing the power consumption of individual pods, so you can analyze them in detail.
// Module included in the following assemblies:

// * power_monitoring/visualizing-power-monitoring-metrics.adoc

[id="power-monitoring-accessing-dashboards-admin_{context}"]
= Accessing {PM-shortname} dashboards as a cluster administrator

You can access {PM-shortname} dashboards of the OpenShift Container Platform web console.

.Prerequisites

* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.
* You have installed the {PM-operator}.
* You have deployed {PM-kepler} in your cluster.
* You have enabled monitoring for user-defined projects.

.Procedure

. In the web console, go to *Observe* -> *Dashboards*.

. From the *Dashboard* drop-down list, select the {PM-shortname} dashboard you want to see:
** *Power Monitor / Overview*
** *Power Monitor / Namespace (Pods)*
// Module included in the following assemblies:

// * power_monitoring/visualizing-power-monitoring-metrics.adoc

[id="power-monitoring-accessing-dashboards-developer_{context}"]
= Accessing {PM-shortname} dashboards as a developer

You can access {PM-shortname} dashboards from OpenShift Container Platform web console.

.Prerequisites

* You have access to the OpenShift Container Platform web console.
* You have access to the cluster as a developer or as a user.
* You have installed the {PM-operator}.
* You have deployed {PM-kepler} in your cluster.
* You have enabled monitoring for user-defined projects.
* You have `view` permissions for the namespace `openshift-power-monitoring`, the namespace where {PM-kepler} is deployed to.

.Procedure

. In the web console, go to *Observe* -> *Dashboard*.

. From the *Dashboard* drop-down list, select the {PM-shortname} dashboard you want to see:
** *Power Monitor / Overview*
//include::modules/power-monitoring-metrics-overview.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_visualizing-power-monitoring-metrics"]
== Additional resources
* Enabling monitoring for user-defined projects
