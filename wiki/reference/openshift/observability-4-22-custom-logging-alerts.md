---
title: "Custom logging alerts"
type: reference
domain: openshift
slug: observability-4-22-custom-logging-alerts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/custom-logging-alerts
version: 4.22
family: observability
documentKind: "Documentation"
---

# Custom logging alerts

[id="custom-logging-alerts"]
= Custom logging alerts

In logging 5.7 and later versions, users can configure the LokiStack deployment to produce customized alerts and recorded metrics. If you want to use customized alerting and recording rules, you must enable the LokiStack ruler component.

LokiStack log-based alerts and recorded metrics are triggered by providing LogQL expressions to the ruler component. The {loki-op} manages a ruler that is optimized for the selected LokiStack size, which can be `1x.extra-small`, `1x.small`, or `1x.medium`.

To provide these expressions, you must create an `AlertingRule` custom resource (CR) containing Prometheus-compatible alerting rules, or a `RecordingRule` CR containing Prometheus-compatible recording rules.

Administrators can configure log-based alerts or recorded metrics for `application`, `audit`, or `infrastructure` tenants. Users without administrator permissions can configure log-based alerts or recorded metrics for `application` tenants of the applications that they have access to.

Application, audit, and infrastructure alerts are sent by default to the OpenShift Container Platform monitoring stack Alertmanager in the `openshift-monitoring` namespace, unless you have disabled the local Alertmanager instance. If the Alertmanager that is used to monitor user-defined projects in the `openshift-user-workload-monitoring` namespace is enabled, application alerts are sent to the Alertmanager in this namespace by default.

// Module included in the following assemblies:
//
// * observability/logging/logging_alerts/custom-logging-alerts.adoc

[id="configuring-logging-loki-ruler_{context}"]
= Configuring the ruler

When the LokiStack ruler component is enabled, users can define a group of LogQL expressions that trigger logging alerts or recorded metrics.

Administrators can enable the ruler by modifying the `LokiStack` custom resource (CR).

.Prerequisites

* You have installed the {clo} and the {loki-op}.
* You have created a `LokiStack` CR.
* You have administrator permissions.

.Procedure

* Enable the ruler by ensuring that the `LokiStack` CR contains the following spec configuration:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: <name>
  namespace: <namespace>
spec:
# ...
  rules:
    enabled: true <1>
    selector:
      matchLabels:
        openshift.io/<label_name>: "true" <2>
    namespaceSelector:
      matchLabels:
        openshift.io/<label_name>: "true" <3>
----
<1> Enable Loki alerting and recording rules in your cluster.
<2> Add a custom label that can be added to namespaces where you want to enable the use of logging alerts and metrics.
<3> Add a custom label that can be added to namespaces where you want to enable the use of logging alerts and metrics.
// Module included in the following assemblies:
//
// * observability/logging/logging_alerts/custom-logging-alerts.adoc

[id="loki-rbac-rules-permissions_{context}"]
= Authorizing LokiStack rules RBAC permissions

Administrators can allow users to create and manage their own alerting and recording rules by binding cluster roles to usernames.
Cluster roles are defined as `ClusterRole` objects that contain necessary role-based access control (RBAC) permissions for users.

In logging 5.8 and later, the following cluster roles for alerting and recording rules are available for LokiStack:

[options="header"]
|===
|Rule name |Description

|`alertingrules.loki.grafana.com-v1-admin`
|Users with this role have administrative-level access to manage alerting rules. This cluster role grants permissions to create, read, update, delete, list, and watch `AlertingRule` resources within the `loki.grafana.com/v1` API group.

|`alertingrules.loki.grafana.com-v1-crdview`
|Users with this role can view the definitions of Custom Resource Definitions (CRDs) related to `AlertingRule` resources within the `loki.grafana.com/v1` API group, but do not have permissions for modifying or managing these resources.

|`alertingrules.loki.grafana.com-v1-edit`
|Users with this role have permission to create, update, and delete `AlertingRule` resources.

|`alertingrules.loki.grafana.com-v1-view`
|Users with this role can read `AlertingRule` resources within the `loki.grafana.com/v1` API group. They can inspect configurations, labels, and annotations for existing alerting rules but cannot make any modifications to them.

|`recordingrules.loki.grafana.com-v1-admin`
|Users with this role have administrative-level access to manage recording rules. This cluster role grants permissions to create, read, update, delete, list, and watch `RecordingRule` resources within the `loki.grafana.com/v1` API group.

|`recordingrules.loki.grafana.com-v1-crdview`
|Users with this role can view the definitions of Custom Resource Definitions (CRDs) related to `RecordingRule` resources within the `loki.grafana.com/v1` API group, but do not have permissions for modifying or managing these resources.

|`recordingrules.loki.grafana.com-v1-edit`
|Users with this role have permission to create, update, and delete `RecordingRule` resources.

|`recordingrules.loki.grafana.com-v1-view`
|Users with this role can read `RecordingRule` resources within the `loki.grafana.com/v1` API group. They can inspect configurations, labels, and annotations for existing alerting rules but cannot make any modifications to them.

|===

[id="loki-rbac-rules-permissions-examples"]
== Examples

To apply cluster roles for a user, you must bind an existing cluster role to a specific username.

Cluster roles can be cluster or namespace scoped, depending on which type of role binding you use.
When a `RoleBinding` object is used, as when using the `oc adm policy add-role-to-user` command, the cluster role only applies to the specified namespace.
When a `ClusterRoleBinding` object is used, as when using the `oc adm policy add-cluster-role-to-user` command, the cluster role applies to all namespaces in the cluster.

The following example command gives the specified user create, read, update and delete (CRUD) permissions for alerting rules in a specific namespace in the cluster:

.Example cluster role binding command for alerting rule CRUD permissions in a specific namespace
[source,terminal]
----
$ oc adm policy add-role-to-user alertingrules.loki.grafana.com-v1-admin -n <namespace> <username>
----

The following command gives the specified user administrator permissions for alerting rules in all namespaces:

.Example cluster role binding command for administrator permissions
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user alertingrules.loki.grafana.com-v1-admin <username>
----

[role="_additional-resources"]
.Additional resources
* Using RBAC to define and apply permissions

// Module included in the following assemblies:
//
// * observability/logging/logging_alerts/custom-logging-alerts.adoc

[id="logging-enabling-loki-alerts_{context}"]
= Creating a log-based alerting rule with Loki

The `AlertingRule` CR contains a set of specifications and webhook validation definitions to declare groups of alerting rules for a single `LokiStack` instance. In addition, the webhook validation definition provides support for rule validation conditions:

* If an `AlertingRule` CR includes an invalid `interval` period, it is an invalid alerting rule
* If an `AlertingRule` CR includes an invalid `for` period, it is an invalid alerting rule.
* If an `AlertingRule` CR includes an invalid LogQL `expr`, it is an invalid alerting rule.
* If an `AlertingRule` CR includes two groups with the same name, it is an invalid alerting rule.
* If none of above applies, an alerting rule is considered valid.

[options="header"]
|================================================
| Tenant type    | Valid namespaces for `AlertingRule` CRs
| application    |
| audit          | `openshift-logging`
| infrastructure | `openshift-/\*`, `kube-/\*`, `default`
|================================================

.Prerequisites

* {clo} 5.7 and later
* OpenShift Container Platform 4.13 and later

.Procedure

. Create an `AlertingRule` custom resource (CR):
+
.Example infrastructure AlertingRule CR
[source,yaml]
----
  apiVersion: loki.grafana.com/v1
  kind: AlertingRule
  metadata:
    name: loki-operator-alerts
    namespace: openshift-operators-redhat <1>
    labels: <2>
      openshift.io/<label_name>: "true"
  spec:
    tenantID: "infrastructure" <3>
    groups:
      - name: LokiOperatorHighReconciliationError
        rules:
          - alert: HighPercentageError
            expr: | <4>
              sum(rate({kubernetes_namespace_name="openshift-operators-redhat", kubernetes_pod_name=~"loki-operator-controller-manager.*"} |= "error" [1m])) by (job)
                /
              sum(rate({kubernetes_namespace_name="openshift-operators-redhat", kubernetes_pod_name=~"loki-operator-controller-manager.*"}[1m])) by (job)
                > 0.01
            for: 10s
            labels:
              severity: critical <5>
            annotations:
              summary: High Loki Operator Reconciliation Errors <6>
              description: High Loki Operator Reconciliation Errors <7>
----
<1> The namespace where this `AlertingRule` CR is created must have a label matching the LokiStack `spec.rules.namespaceSelector` definition.
<2> The `labels` block must match the LokiStack `spec.rules.selector` definition.
<3> `AlertingRule` CRs for `infrastructure` tenants are only supported in the `openshift-\*`, `kube-\*`, or `default` namespaces.
<4> The value for `kubernetes_namespace_name:` must match the value for `metadata.namespace`.
<5> The value of this mandatory field must be `critical`, `warning`, or `info`.
<6> This field is mandatory.
<7> This field is mandatory.
+
.Example application AlertingRule CR
[source,yaml]
----
  apiVersion: loki.grafana.com/v1
  kind: AlertingRule
  metadata:
    name: app-user-workload
    namespace: app-ns <1>
    labels: <2>
      openshift.io/<label_name>: "true"
  spec:
    tenantID: "application"
    groups:
      - name: AppUserWorkloadHighError
        rules:
          - alert:
            expr: | <3>
            sum(rate({kubernetes_namespace_name="app-ns", kubernetes_pod_name=~"podName.*"} |= "error" [1m])) by (job)
            for: 10s
            labels:
              severity: critical <4>
            annotations:
              summary:  <5>
              description:  <6>
----
<1> The namespace where this `AlertingRule` CR is created must have a label matching the LokiStack `spec.rules.namespaceSelector` definition.
<2> The `labels` block must match the LokiStack `spec.rules.selector` definition.
<3> Value for `kubernetes_namespace_name:` must match the value for `metadata.namespace`.
<4> The value of this mandatory field must be `critical`, `warning`, or `info`.
<5> The value of this mandatory field is a summary of the rule.
<6> The value of this mandatory field is a detailed description of the rule.

. Apply the `AlertingRule` CR:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

[role="_additional-resources"]
[id="additional-resources_custom-logging-alerts"]
== Additional resources
* About OpenShift Container Platform monitoring
* Configuring alert notifications
// maybe need an update to https://docs.openshift.com/container-platform/4.13/observability/monitoring/monitoring-overview.html#default-monitoring-targets_monitoring-overview to talk about Loki and Vector now? Are these part of default monitoring?
