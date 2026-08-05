---
title: "Using Red{nbsp}Hat Lightspeed to identify issues with your cluster"
type: reference
domain: openshift
slug: support-4-22-using-insights-to-identify-issues-with-your-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/using-insights-to-identify-issues-with-your-cluster
version: 4.22
family: support
documentKind: "Documentation"
---

# Using Red{nbsp}Hat Lightspeed to identify issues with your cluster

[id="using-insights-to-identify-issues-with-your-cluster"]
= Using Red{nbsp}Hat Lightspeed to identify issues with your cluster

[role="_abstract"]
{red-hat-lightspeed} repeatedly analyzes the data {insights-operator} sends, which includes workload recommendations from Deployment Validation Operator (DVO). Users of OpenShift Container Platform can display the results in the {insights-advisor-url} service on {hybrid-console}.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="insights-operator-advisor-overview_{context}"]
= About {red-hat-lightspeed} Advisor for OpenShift Container Platform

[role="_abstract"]
You can use the {red-hat-lightspeed} advisor service to assess and monitor the health of your OpenShift Container Platform clusters. Whether you are concerned about individual clusters, or with your whole infrastructure, it is important to be aware of the exposure of your cluster infrastructure to issues that can affect service availability, fault tolerance, performance, or security.

If the cluster has the Deployment Validation Operator (DVO) installed the recommendations also highlight workloads whose configuration might lead to cluster health issues.

The results of the {red-hat-lightspeed} analysis are available in the {red-hat-lightspeed} advisor service on {hybrid-console}. In the {hybrid-console}, you can perform the following actions:

* View clusters and workloads affected by specific recommendations.
* Use robust filtering capabilities to refine your results to those recommendations.
* Learn more about individual recommendations, details about the risks they present, and get resolutions tailored to your individual clusters.
* Share results with other stakeholders.

.Additional resources

* Using the Deployment Validation Operator in your {red-hat-lightspeed} workflow

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="insights-operator-advisor-recommendations_{context}"]
= Understanding {red-hat-lightspeed} advisor service recommendations

[role="_abstract"]
The {red-hat-lightspeed} advisor service bundles information about various cluster states and component configurations that can negatively affect the service availability, fault tolerance, performance, or security of your clusters and workloads. This information set is called a recommendation in the {red-hat-lightspeed} advisor service. Recommendations for clusters includes the following information:

* *Name:* A concise description of the recommendation
* *Added:* When the recommendation was published to the {red-hat-lightspeed} advisor service archive
* *Category:* Whether the issue has the potential to negatively affect service availability, fault tolerance, performance, or security
* *Total risk:* A value derived from the _likelihood_ that the condition will negatively affect your cluster or workload, and the _impact_ on operations if that were to happen
* *Clusters:* A list of clusters on which a recommendation is detected
* *Description:* A brief synopsis of the issue, including how it affects your clusters

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="displaying-potential-issues-with-your-cluster_{context}"]
= Displaying potential issues with your cluster

[role="_abstract"]
This section describes how to display the {red-hat-lightspeed} report in *{red-hat-lightspeed} Advisor* on {cluster-manager-url}.

Note that {red-hat-lightspeed} repeatedly analyzes your cluster and shows the latest results. These results can change, for example, if you fix an issue or a new issue has been detected.

.Prerequisites

* Your cluster is registered on {cluster-manager-url}.
* Remote health reporting is enabled, which is the default.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
+
Depending on the result, the {red-hat-lightspeed} advisor service displays one of the following:
+
* *No matching recommendations found*, if {red-hat-lightspeed} did not identify any issues.
+
* A list of issues {red-hat-lightspeed} has detected, grouped by risk (low, moderate, important, and critical).
+
* *No clusters yet*, if {red-hat-lightspeed} has not yet analyzed the cluster. The analysis starts shortly after the cluster has been installed, registered, and connected to the internet.

. If any issues are displayed, click the *>* icon in front of the entry for more details.
+
Depending on the issue, the details can also contain a link to more information from Red Hat about the issue.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="displaying-all-insights-advisor-recommendations_{context}"]
= Displaying all {red-hat-lightspeed} advisor service recommendations

[role="_abstract"]
The Recommendations view, by default, only displays the recommendations that are detected on your clusters. However, you can view all of the recommendations in the advisor service's archive.

.Prerequisites

* Remote health reporting is enabled, which is the default.
* Your cluster is registered on {hybrid-console}.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
. Click the *X* icons next to the *Clusters Impacted* and *Status* filters.
+
You can now browse through all of the potential recommendations for your cluster.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="insights-operator-advisor-recommendation-filters_{context}"]
= Advisor recommendation filters

[role="_abstract"]
The {red-hat-lightspeed} advisor service can return a large number of recommendations. To focus on your most critical recommendations, you can apply filters to the https://console.redhat.com/openshift/insights/advisor/recommendations[Advisor recommendations] list to remove low-priority recommendations.

By default, filters are set to only show enabled recommendations that are impacting one or more clusters. To view all or disabled recommendations in the {red-hat-lightspeed} library, you can customize the filters.

To apply a filter, select a filter type and then set its value based on the options that are available in the drop-down list. You can apply multiple filters to the list of recommendations.

You can set the following filter types:

* *Name:* Search for a recommendation by name.
* *Total risk:* Select one or more values from *Critical*, *Important*, *Moderate*, and *Low* indicating the likelihood and the severity of a negative impact on a cluster.
* *Impact:* Select one or more values from *Critical*, *High*, *Medium*, and *Low* indicating the potential impact to the continuity of cluster operations.
* *Likelihood:* Select one or more values from *Critical*, *High*, *Medium*, and *Low* indicating the potential for a negative impact to a cluster if the recommendation comes to fruition.
* *Category:* Select one or more categories from *Service Availability*, *Performance*, *Fault Tolerance*, *Security*, and *Best Practice* to focus your attention on.
* *Status:* Click a radio button to show enabled recommendations (default), disabled recommendations, or all recommendations.
* *Clusters impacted:* Set the filter to show recommendations currently impacting one or more clusters, non-impacting recommendations, or all recommendations.
* *Risk of change:* Select one or more values from *High*, *Moderate*, *Low*, and *Very low* indicating the risk that the implementation of the resolution could have on cluster operations.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="filtering-unnecessary-advisor-recommendations_{context}"]
= Filtering {red-hat-lightspeed} advisor service recommendations

[role="_abstract"]
As an OpenShift Container Platform cluster manager, you can filter the recommendations that are displayed on the recommendations list. By applying filters, you can reduce the number of reported recommendations and concentrate on your highest priority recommendations.

The following procedure demonstrates how to set and remove *Category* filters; however, the procedure is applicable to any of the filter types and respective values.

.Prerequisites
You are logged in to the https://console.redhat.com/openshift[{cluster-manager}] in the {hybrid-console-second}.

.Procedure
. Go to *OpenShift* > *Advisor* > *Recommendations*.
. In the main, filter-type drop-down list, select the *Category* filter type.
. Expand the filter-value drop-down list and select the checkbox next to each category of recommendation you want to view. Leave the checkboxes for unnecessary categories clear.
. Optional: Add additional filters to further refine the list.
+
Only recommendations from the selected categories are shown in the list.

.Verification

* After applying filters, you can view the updated recommendations list. The applied filters are added next to the default filters.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="removing-filters-from-insights-recommendations_{context}"]
= Removing filters from {red-hat-lightspeed} advisor service recommendations

[role="_abstract"]
You can apply multiple filters to the list of recommendations. When ready, you can remove them individually or completely reset them.

.Procedure
* Removing filters individually
** Click the *X* icon next to each filter, including the default filters, to remove them individually.

* Removing all non-default filters
** Click *Reset filters* to remove only the filters that you applied, leaving the default filters in place.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="disabling-insights-advisor-recommendations_{context}"]
= Disabling {red-hat-lightspeed} advisor service recommendations

[role="_abstract"]
You can disable specific recommendations that affect your clusters, so that they no longer appear in your reports. It is possible to disable a recommendation for a single cluster or all of your clusters.

[NOTE]
====
Disabling a recommendation for all of your clusters also applies to any future clusters.
====

.Prerequisites

* Remote health reporting is enabled, which is the default.
* Your cluster is registered on {cluster-manager-url}.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
. Optional: Use the *Clusters Impacted* and *Status* filters as needed.
. Disable an alert by using one of the following methods:
+
* To disable an alert:
.. Click the Options menu {kebab} for that alert, and then click *Disable recommendation*.
.. Enter a justification note and click *Save*.
+
* To view the clusters affected by this alert before disabling the alert:
.. Click the name of the recommendation to disable. You are directed to the single recommendation page.
.. Review the list of clusters in the *Affected clusters* section.
.. Click *Actions* -> *Disable recommendation* to disable the alert for all of your clusters.
.. Enter a justification note and click *Save*.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="enabling-insights-advisor-recommendations_{context}"]
= Enabling a previously disabled {red-hat-lightspeed} advisor service recommendation

[role="_abstract"]
When a recommendation is disabled for all clusters, you no longer see the recommendation in the {red-hat-lightspeed} advisor service. You can change this behavior.

.Prerequisites

* Remote health reporting is enabled, which is the default.
* Your cluster is registered on {cluster-manager-url}.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
. Filter the recommendations to display on the disabled recommendations:
.. From the *Status* drop-down menu, select *Status*.
.. From the *Filter by status* drop-down menu, select *Disabled*.
.. Optional: Clear the *Clusters impacted* filter.
. Locate the recommendation to enable.
. Click the Options menu {kebab}, and then click *Enable recommendation*.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="about-insights-advisor-workload-recommendations_{context}"]
= About {red-hat-lightspeed} advisor service recommendations for workloads

[role="_abstract"]
You can use the {red-hat-lightspeed} advisor service to view and manage information about recommendations that affect not only your clusters, but also your workloads. The advisor service takes advantage of deployment validation and helps OpenShift cluster administrators to see all runtime violations of deployment policies. You can see recommendations for workloads at OpenShift > Advisor > Workloads on the {hybrid-console}. For more information, see these additional resources:

* Information about Kubernetes workloads
* https://www.redhat.com/en/blog/boost-your-cluster-operations-with-deployment-validation-and-insights-advisor-for-workloads[Boost your cluster operations with Deployment Validation and {red-hat-lightspeed} Advisor for Workloads]
* Identifying workload recommendations for namespaces in your clusters
* Viewing workload recommendations for namespaces in your cluster
* Excluding objects from workload recommendations in your clusters

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc
// * sd_support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

[id="displaying-the-insights-status-in-the-web-console_{context}"]
= Displaying the {red-hat-lightspeed} status in the web console

[role="_abstract"]
{red-hat-lightspeed} repeatedly analyzes your cluster and you can display the status of identified potential issues of your cluster in the OpenShift Container Platform web console. This status shows the number of issues in the different categories and, for further details, links to the reports in {cluster-manager-url}.

.Prerequisites

* Your cluster is registered in {cluster-manager-url}.
* Remote health reporting is enabled, which is the default.
* You are logged in to the OpenShift Container Platform web console.

.Procedure

. Navigate to *Home* -> *Overview* in the OpenShift Container Platform web console.

. Click *{red-hat-lightspeed}* on the *Status* card.
+
The pop-up window lists potential issues grouped by risk. Click the individual categories or *View all recommendations in {red-hat-lightspeed} Advisor* to display more details.
