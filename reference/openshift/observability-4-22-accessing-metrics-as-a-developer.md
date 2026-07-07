---
title: "Accessing metrics as a developer"
type: reference
domain: openshift
slug: observability-4-22-accessing-metrics-as-a-developer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/accessing-metrics-as-a-developer
version: 4.22
family: observability
documentKind: "Documentation"
---

# Accessing metrics as a developer

[id="accessing-metrics-as-a-developer"]
= Accessing metrics as a developer

You can access metrics to monitor the performance of your cluster workloads.

[role="_additional-resources"]
.Additional resources

* Understanding metrics

//Viewing a list of available metrics
// Module included in the following assemblies:
//
// * observability/monitoring/managing-metrics.adoc

[id="viewing-a-list-of-available-metrics_{context}"]
= Viewing a list of available metrics

As a cluster administrator or as a user with view permissions for all projects, you can view a list of metrics available in a cluster and output the list in JSON format.

.Prerequisites
* You are a cluster administrator, or you have access to the cluster as a user with the `cluster-monitoring-view` cluster role.
* You have installed the OpenShift Container Platform CLI (`oc`).
* You have obtained the OpenShift Container Platform API route for Thanos Querier.
* You are able to get a bearer token by using the `oc whoami -t` command.
+
[IMPORTANT]
====
You can only use bearer token authentication to access the Thanos Querier API route.
====

.Procedure

. If you have not obtained the OpenShift Container Platform API route for Thanos Querier, run the following command:
+
[source,terminal]
----
$ oc get routes -n openshift-monitoring thanos-querier -o jsonpath='{.status.ingress[0].host}'
----

. Retrieve a list of metrics in JSON format from the Thanos Querier API route by running the following command. This command uses `oc` to authenticate with a bearer token.
+
[source,terminal]
----
$ curl -k -H "Authorization: Bearer $(oc whoami -t)" https://<thanos_querier_route>/api/v1/metadata <1>
----
<1> Replace `<thanos_querier_route>` with the OpenShift Container Platform API route for Thanos Querier.

//Querying metrics for user-defined projects with the OCP web console
// Module included in the following assemblies:
//
// * observability/monitoring/managing-metrics.adoc
// * virt/support/virt-prometheus-queries.adoc

[id="querying-metrics-for-user-defined-projects-with-mon-dashboard_{context}"]
= Querying metrics for user-defined projects with the OpenShift Container Platform web console

[role="_abstract"]
Monitor user-defined workloads by using the OpenShift Container Platform metrics query browser. The query browser uses Prometheus Query Language (PromQL) queries to examine metrics visualized on a plot.

As a developer, you must specify a project name when querying metrics. You must have the required privileges to view metrics for the selected project.

[NOTE]
====
Developers cannot access the third-party UIs provided with OpenShift Container Platform monitoring.
====

.Prerequisites

* You have access to the cluster as a developer or as a user with view permissions for the project that you are viewing metrics for.
* You have enabled monitoring for user-defined projects.
* You have deployed a service in a user-defined project.
* You have created a `ServiceMonitor` custom resource definition (CRD) for the service to define how the service is monitored.

.Procedure

. In the OpenShift Container Platform web console, click *Observe* -> *Metrics*.

. To add one or more queries, perform any of the following actions:
+
|===
|Option |Description

|Select an existing query.
|From the *Select query* drop-down list, select an existing query.

|Create a custom query.
|Add your Prometheus Query Language (PromQL) query to the *Expression* field.

As you type a PromQL expression, autocomplete suggestions appear in a drop-down list. These suggestions include functions, metrics, labels, and time tokens.
Use the keyboard arrows to select one of these suggested items and then press Enter to add the item to your expression. Move your mouse pointer over a suggested item to view a brief description of that item.

|Add multiple queries. |Click *Add query*.

|Duplicate an existing query. |Click the options menu {kebab} next to the query, then choose *Duplicate query*.

|Disable a query from being run. |Click the options menu {kebab} next to the query and choose *Disable query*.
|===

. To run queries that you created, click *Run queries*. The metrics from the queries are visualized on the plot. If a query is invalid, the UI shows an error message.
+
[NOTE]
====
* When drawing time series graphs, queries that operate on large amounts of data might time out or overload the browser. To avoid this, click *Hide graph* and calibrate your query by using only the metrics table. Then, after finding a feasible query, enable the plot to draw the graphs.

* By default, the query table shows an expanded view that lists every metric and its current value. Click the *˅* down arrowhead to minimize the expanded view for a query.
====

. Optional: Save the page URL to use this set of queries again in the future.

. Explore the visualized metrics. Initially, all metrics from all enabled queries are shown on the plot. Select which metrics are shown by performing any of the following actions:
+
|===
|Option |Description

|Hide all metrics from a query. |Click the options menu {kebab} for the query and click *Hide all series*.

|Hide a specific metric. |Go to the query table and click the colored square near the metric name.

|Zoom into the plot and change the time range.
a|Perform one of the following actions:

* Visually select the time range by clicking and dragging on the plot horizontally.
* Use the menu to select the time range.

|Reset the time range. |Click *Reset zoom*.

|Display outputs for all queries at a specific point in time. |Hover over the plot at the point you are interested in. The query outputs appear in a pop-up box.

|Hide the plot. |Click *Hide graph*.
|===

[role="_additional-resources"]
.Additional resources

* Querying Prometheus (Prometheus documentation)

//Reviewing monitoring dashboards as a developer
// Module included in the following assemblies:
//
// * observability/monitoring/reviewing-monitoring-dashboards.adoc

[id="reviewing-monitoring-dashboards-developer_{context}"]
= Reviewing monitoring dashboards as a developer

As a developer, you can view dashboards relating to projects you have permissions for.

.Prerequisites

* You have access to the cluster as a developer or as a user.
* You have view permissions for the project that you are viewing the dashboard for.
* A cluster administrator has enabled the *Developer* perspective in the web console.

.Procedure

. In the *Developer* perspective of the OpenShift Container Platform web console, click *Observe* and go to the *Dashboards* tab.

. Select a project from the *Project:* drop-down list.

. Select a dashboard from the *Dashboard* drop-down list to see the filtered metrics.

. Optional: Select a time range for the graphs in the *Time range* list.

** Select a predefined time period.

** Set a custom time range by clicking *Custom time range* in the *Time range* list.
+
.. Input or select the *From* and *To* dates and times.
+
.. Click *Save* to save the custom time range.

. Optional: Select a *Refresh interval*.

. Hover over each of the graphs within a dashboard to display detailed information about specific items.

[role="_additional-resources"]
.Additional resources

* About monitoring dashboards
* Monitoring project and application metrics using the Developer perspective
