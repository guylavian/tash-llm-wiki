---
title: "Viewing Argo CD logs"
type: reference
domain: openshift
slug: cicd-4-22-viewing-argo-cd-logs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/viewing-argo-cd-logs
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Viewing Argo CD logs

[id="viewing-argo-cd-logs"]
= Viewing Argo CD logs

You can view the Argo CD logs with {logging}. {logging-uc} visualizes the logs on a Kibana dashboard. The {clo} enables logging with Argo CD by default.

// Module included in the following assemblies:
//
// * cicd/gitops/viewing-argo-cd-logs.adoc

[id="gitops-storing-and-retrieving-argo-cd-logs_{context}"]
= Storing and retrieving Argo CD logs

You can use the Kibana dashboard to store and retrieve Argo CD logs.

.Prerequisites

* The {gitops-title} Operator is installed in your cluster.
* {logging-uc} is installed with default configuration in your cluster.

.Procedure

. In the OpenShift Container Platform web console, go to the {rh-app-icon} menu -> *Observability* -> *Logging* to view the Kibana dashboard.

. Create an index pattern.

.. To display all the indices, define the index pattern as `pass:[*]`, and click *Next step*.

.. Select *@timestamp* for *Time Filter field name*.

.. Click *Create index pattern*.

. In the navigation panel of the Kibana dashboard, click the *Discover* tab.

. Create a filter to retrieve logs for Argo CD. The following steps create a filter that retrieves logs for all the pods in the `openshift-gitops` namespace:

.. Click *Add a filter +*.

.. Select the *kubernetes.namespace_name* field.

.. Select the *is* operator.

.. Select the *openshift-gitops* value.

.. Click *Save*.

. Optional: Add additional filters to narrow the search. For example, to retrieve logs for a particular pod, you can create another filter with `kubernetes.pod_name` as the field.

. View the filtered Argo CD logs in the Kibana dashboard.

[role="_additional-resources"]
[id="additional-resources_viewing-argo-cd-logs"]
== Additional resources
* xref :../../observability/logging/cluster-logging-deploying.adoc#cluster-logging-deploy-console_cluster-logging-deploying[Installing {logging} using the web console]
