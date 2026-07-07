---
title: "Accessing metrics as an administrator"
type: reference
domain: openshift
slug: observability-4-22-accessing-metrics-as-an-administrator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/accessing-metrics-as-an-administrator
version: 4.22
family: observability
documentKind: "Documentation"
---

# Accessing metrics as an administrator

[id="accessing-metrics-as-an-administrator"]
= Accessing metrics as an administrator

You can access metrics to monitor the performance of cluster components and your workloads.

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

//Querying metrics for all projects with the OCP web console
// Module included in the following assemblies:
//
// * observability/monitoring/managing-metrics.adoc
// * virt/support/virt-prometheus-queries.adoc

[id="querying-metrics-for-all-projects-with-mon-dashboard_{context}"]
= Querying metrics for all projects with the OpenShift Container Platform web console

// The following section will be included in the administrator section, hence there is no need to include "administrator" in the title
[role="_abstract"]

Monitor the state of a cluster and any user-defined workloads by using the OpenShift Container Platform metrics query browser. The query browser uses Prometheus Query Language (PromQL) queries to examine metrics visualized on a plot.

As a
cluster administrator
`dedicated-admin`
or as a user with view permissions for all projects, you can access metrics for all default OpenShift Container Platform and user-defined projects in the Metrics UI.

[NOTE]
====
Only dedicated administrators have access to the third-party UIs provided with OpenShift Container Platform monitoring.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role or with view permissions for all projects.
* You have access to the cluster as a user with the `dedicated-admin` role or with view permissions for all projects.
* You have installed the {oc-first}.

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

//Getting detailed information about a metrics target
// Module included in the following assemblies:
//
// * observability/monitoring/managing-metrics.adoc

[id="getting-detailed-information-about-a-target_{context}"]
= Getting detailed information about a metrics target

You can use the OpenShift Container Platform web console to view, search, and filter the endpoints that are currently targeted for scraping, which helps you to identify and troubleshoot problems. For example, you can view the current status of targeted endpoints to see when OpenShift Container Platform monitoring is not able to scrape metrics from a targeted component.

The *Metrics targets* page shows targets for default OpenShift Container Platform projects and for user-defined projects.
The *Metrics targets* page shows targets for user-defined projects.

.Prerequisites

* You have access to the cluster as an administrator for the project for which you want to view metrics targets.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. In the OpenShift Container Platform web console, go to *Observe* -> *Targets*. The *Metrics targets* page opens with a list of all service endpoint targets that are being scraped for metrics.
+
This page shows details about targets for default OpenShift Container Platform and user-defined projects. This page lists the following information for each target:

** Service endpoint URL being scraped
** The `ServiceMonitor` resource being monitored
** The **up** or **down** status of the target
** Namespace
** Last scrape time
** Duration of the last scrape

. Optional: To find a specific target, perform any of the following actions:
+
|===
|Option |Description

|Filter the targets by status and source.
a|Choose filters in the *Filter* list.

The following filtering options are available:

* **Status** filters:
** **Up**. The target is currently up and being actively scraped for metrics.
** **Down**. The target is currently down and not being scraped for metrics.

* **Source** filters:
** **Platform**. Platform-level targets relate only to default {product-rosa} projects. These projects provide core {product-rosa} functionality.
** **User**. User targets relate to user-defined projects. These projects are user-created and can be customized.

|Search for a target by name or label. |Enter a search term in the **Text** or **Label** field next to the search box.

|Sort the targets. |Click one or more of the **Endpoint Status**, **Namespace**, **Last Scrape**, and **Scrape Duration** column headers.
|===

. Click the URL in the **Endpoint** column for a target to go to its **Target details** page. This page provides information about the target, including the following information:

** The endpoint URL being scraped for metrics
** The current *Up* or *Down* status of the target
** A link to the namespace
** A link to the `ServiceMonitor` resource details
** Labels attached to the target
** The most recent time that the target was scraped for metrics

//Reviewing monitoring dashboards as a cluster administrator
// Module included in the following assemblies:
//
// * observability/monitoring/reviewing-monitoring-dashboards.adoc

[id="reviewing-monitoring-dashboards-admin_{context}"]
= Reviewing monitoring dashboards as a cluster administrator

As an administrator, you can view dashboards relating to core OpenShift Container Platform cluster components.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. In the OpenShift Container Platform web console, go to *Observe* -> *Dashboards*.

. Choose a dashboard in the *Dashboard* list. Some dashboards, such as *etcd* and *Prometheus* dashboards, produce additional sub-menus when selected.

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
