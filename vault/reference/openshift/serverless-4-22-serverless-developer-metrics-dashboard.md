---
title: "Dashboard for service metrics"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developer-metrics-dashboard
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developer-metrics-dashboard
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Dashboard for service metrics

[id="serverless-developer-metrics-dashboard"]
= Dashboard for service metrics

You can examine the metrics using a dedicated dashboard that aggregates queue proxy metrics by namespace.

// Module is included in the following assemblies:
//
// * /serverless/monitor/serverless-developer-metrics.adoc

[id="serverless-monitoring-services-examining-metrics-dashboard_{context}"]
= Examining metrics of a service in the dashboard

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* You have installed the {ServerlessOperatorName} and Knative Serving.

.Procedure

. In the web console, navigate to the *Observe* -> *Metrics* interface.

. Select the `Knative User Services (Queue Proxy metrics)` dashboard.

. Select the *Namespace*, *Configuration*, and *Revision* that correspond to your application.

. Observe the visualized metrics:
+
image::serverless-monitoring-service-example-dashboard.png[Observing metrics of a service using a dashboard]
