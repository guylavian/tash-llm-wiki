---
title: "{ServerlessProductShortName} administrator metrics"
type: reference
domain: openshift
slug: serverless-4-22-serverless-admin-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-admin-metrics
version: 4.22
family: serverless
documentKind: "Documentation"
---

# {ServerlessProductShortName} administrator metrics

[id="serverless-admin-metrics"]
= {ServerlessProductShortName} administrator metrics

Metrics enable cluster administrators to monitor how {ServerlessProductName} cluster components and workloads are performing.

You can view different metrics for {ServerlessProductName} by navigating to *Dashboards* in the OpenShift Container Platform web console *Administrator* perspective.

You can view different metrics for {ServerlessProductName} by navigating to *Dashboards* in the OpenShift Container Platform web console *Administrator* perspective.

[id="prerequisites_serverless-admin-metrics"]
== Prerequisites

* See the OpenShift Container Platform documentation on Accessing metrics as an administrator for information about enabling metrics for your cluster.

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster or dedicated administrator access.

* You have access to the *Administrator* perspective in the OpenShift Container Platform web console.

[WARNING]
====
If {SMProductShortName} is enabled with mTLS, metrics for Knative Serving are disabled by default because Service Mesh prevents Prometheus from scraping metrics.

For information about resolving this issue, see Enabling Knative Serving metrics when using Service Mesh with mTLS.

Scraping the metrics does not affect autoscaling of a Knative service, because scraping requests do not go through the activator. Consequently, no scraping takes place if no pods are running.
====
