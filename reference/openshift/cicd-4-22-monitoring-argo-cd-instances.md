---
title: "Monitoring Argo CD instances"
type: reference
domain: openshift
slug: cicd-4-22-monitoring-argo-cd-instances
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/monitoring-argo-cd-instances
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Monitoring Argo CD instances

[id="monitoring-argo-cd-instances"]
= Monitoring Argo CD instances

By default, the {gitops-title} Operator automatically detects an installed Argo CD instance in your defined namespace, for example, `openshift-gitops`, and connects it to the monitoring stack of the cluster to provide alerts for out-of-sync applications.

.Prerequisites
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have installed the {gitops-title} Operator in your cluster.
* You have installed an Argo CD application in your defined namespace, for example, `openshift-gitops`.

// Module included in the following assemblies:
//
// * cicd/gitops/monitoring-argo-cd-instances.adoc

[id="gitops-monitoring-argo-cd-health-using-promethous-metrics_{context}"]
= Monitoring Argo CD health using Prometheus metrics

You can monitor the health status of an Argo CD application by running Prometheus metrics queries against it.

.Procedure

. In the *Developer* perspective of the web console, select the namespace where your Argo CD application is installed, and navigate to *Observe* -> *Metrics*.
. From the *Select query* drop-down list, select *Custom query*.
. To check the health status of your Argo CD application, enter the Prometheus Query Language (PromQL) query similar to the following example in the *Expression* field:
+
.Example
[source,terminal]
----
sum(argocd_app_info{dest_namespace=~"<your_defined_namespace>",health_status!=""}) by (health_status) <1>
----
<1> Replace the `<your_defined_namespace>` variable with the actual name of your defined namespace, for example `openshift-gitops`.
