---
title: "{ServerlessProductShortName} developer metrics overview"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developer-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developer-metrics
version: 4.22
family: serverless
documentKind: "Documentation"
---

# {ServerlessProductShortName} developer metrics overview

[id="serverless-developer-metrics"]
= {ServerlessProductShortName} developer metrics overview

Metrics enable developers to monitor how Knative services are performing. You can use the OpenShift Container Platform monitoring stack to record and view health checks and metrics for your Knative services.

You can view different metrics for {ServerlessProductName} by navigating to *Dashboards* in the OpenShift Container Platform web console *Developer* perspective.

You can view different metrics for {ServerlessProductName} by navigating to *Dashboards* in the OpenShift Container Platform web console *Developer* perspective.

[WARNING]
====
If {SMProductShortName} is enabled with mTLS, metrics for Knative Serving are disabled by default because Service Mesh prevents Prometheus from scraping metrics.

For information about resolving this issue, see Enabling Knative Serving metrics when using Service Mesh with mTLS.

Scraping the metrics does not affect autoscaling of a Knative service, because scraping requests do not go through the activator. Consequently, no scraping takes place if no pods are running.
====

[id="additional-resources_serverless-service-monitoring"]
[role="_additional-resources"]
== Additional resources
* About OpenShift Container Platform monitoring
* Enabling monitoring for user-defined projects
* Specifying how a service is monitored
