---
title: "Monitoring Argo CD custom resource workloads"
type: reference
domain: openshift
slug: cicd-4-22-monitoring-argo-cd-custom-resource-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/monitoring-argo-cd-custom-resource-workloads
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Monitoring Argo CD custom resource workloads

[id="monitoring-argo-cd-custom-resource-workloads"]
= Monitoring Argo CD custom resource workloads

[role="_abstract"]
With {gitops-title}, you can monitor the availability of Argo CD custom resource workloads for specific Argo CD instances. By monitoring Argo CD custom resource workloads, you have the latest information about the state of your Argo CD instances by enabling alerts for them. When the component workload pods such as application-controller, repo-server, or server of the corresponding Argo CD instance are unable to come up for certain reasons and there is a drift between the number of ready replicas and the number of desired replicas for a certain period of time, the Operator then triggers the alerts.

You can enable and disable the setting for monitoring Argo CD custom resource workloads.

// Prerequisites for monitoring Argo CD custom resource workloads
[discrete]
== Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* {gitops-title} is installed in your cluster.
* The monitoring stack is configured in your cluster in the `openshift-monitoring` project. In addition, the Argo CD instance is in a namespace that you can monitor through Prometheus.
* The `kube-state-metrics` service is running in your cluster.
* Optional: If you are enabling monitoring for an Argo CD instance already present in a user-defined project, ensure that the monitoring is enabled for user-defined projects in your cluster.
+
[NOTE]
====
If you want to enable monitoring for an Argo CD instance in a namespace that is not watched by the default `openshift-monitoring` stack, for example, any namespace that does not start with `openshift-*`, then you must enable user workload monitoring in your cluster. This action enables the monitoring stack to pick up the created PrometheusRule.
====

//Enabling Monitoring for Argo CD custom resource workloads
// Module included in the following assemblies:
//
// * /cicd/gitops/monitoring-argo-cd-custom-resource-workloads.adoc

[id="gitops-enabling-monitoring-for-argo-cd-custom-resource-workloads_{context}"]
= Enabling Monitoring for Argo CD custom resource workloads

By default, the monitoring configuration for Argo CD custom resource workloads is set to `false`.

With {gitops-title}, you can enable workload monitoring for specific Argo CD instances. As a result, the Operator creates a `PrometheusRule` object that contains alert rules for all the workloads managed by the specific Argo CD instances. These alert rules trigger the firing of an alert when the replica count of the corresponding component has drifted from the desired state for a certain amount of time. The Operator will not overwrite the changes made to the `PrometheusRule` object by the users.

.Procedure

. Set the `.spec.monitoring.enabled` field value to `true` on a given Argo CD instance:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  ...
  monitoring:
    enabled: true
  ...
----

. Verify whether an alert rule is included in the PrometheusRule created by the Operator:
+
.Example alert rule

[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: argocd-component-status-alert
  namespace: openshift-gitops
spec:
  groups:
    - name: ArgoCDComponentStatus
      rules:
        ...
        - alert: ApplicationSetControllerNotReady <1>
          annotations:
            message: >-
              applicationSet controller deployment for Argo CD instance in
              namespace "default" is not running
          expr: >-
            kube_statefulset_status_replicas{statefulset="openshift-gitops-application-controller statefulset",
            namespace="openshift-gitops"} !=
            kube_statefulset_status_replicas_ready{statefulset="openshift-gitops-application-controller statefulset",
            namespace="openshift-gitops"}
          for: 1m
          labels:
            severity: critical
----
<1> Alert rule in the PrometheusRule that checks whether the workloads created by the Argo CD instances are running as expected.

//Disabling Monitoring for Argo CD custom resource workloads
// Module included in the following assemblies:
//
// * /cicd/gitops/monitoring-argo-cd-custom-resource-workloads.adoc

[id="gitops-disabling-monitoring-for-argo-cd-custom-resource-workloads_{context}"]
= Disabling Monitoring for Argo CD custom resource workloads

You can disable workload monitoring for specific Argo CD instances. Disabling workload monitoring deletes the created PrometheusRule.

.Procedure

* Set the `.spec.monitoring.enabled` field value to `false` on a given Argo CD instance:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  ...
  monitoring:
    enabled: false
  ...
----

[role="_additional-resources"]
[id="additional-resources_monitoring-argo-cd-custom-resource-workloads"]
== Additional resources
* Enabling monitoring for user-defined projects
