---
title: "Managing alerts as a Developer"
type: reference
domain: openshift
slug: observability-4-22-managing-alerts-as-a-developer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/managing-alerts-as-a-developer
version: 4.22
family: observability
documentKind: "Documentation"
---

# Managing alerts as a Developer

[id="managing-alerts-as-a-developer"]
= Managing alerts as a Developer

In OpenShift Container Platform, the Alerting UI enables you to manage alerts, silences, and alerting rules.

[NOTE]
====
The alerts, silences, and alerting rules that are available in the Alerting UI relate to the projects that you have access to.
====

// Accessing the Alerting UI
// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc
// * logging/logging_alerts/log-storage-alerts.adoc

[id="monitoring-accessing-the-alerting-ui_{context}"]
= Accessing the Alerting UI

The Alerting UI is accessible in the OpenShift Container Platform web console.

* In the OpenShift Container Platform web console, go to *Observe* -> *Alerting*. The three main pages in the Alerting UI in this perspective are the *Alerts*, *Silences*, and *Alerting rules* pages.

[role="_additional-resources"]
.Additional resources

* Searching and filtering alerts, silences, and alerting rules

// Getting information about alerts, silences and alerting rules
// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="getting-information-about-alerts-silences-and-alerting-rules_{context}"]
= Getting information about alerts, silences, and alerting rules

The Alerting UI provides detailed information about alerts and their governing alerting rules and silences.

.Prerequisites

* You have access to the cluster as a user with view permissions for the project that you are viewing alerts for.

.Procedure

To obtain information about alerts:

. In the OpenShift Container Platform web console, go to the *Observe* -> *Alerting* -> *Alerts* page.

. Optional: Search for alerts by name by using the *Name* field in the search list.

. Optional: Filter alerts by state, severity, and source by selecting filters in the *Filter* list.

. Optional: Sort the alerts by clicking one or more of the *Name*, *Severity*, *State*, and *Source* column headers.

. Click the name of an alert to view its *Alert details* page. The page includes a graph that illustrates alert time series data. It also provides the following information about the alert:

* A description of the alert
* Messages associated with the alert
* A link to the runbook page on GitHub for the alert, if the page exists
* Labels attached to the alert
* A link to its governing alerting rule
* Silences for the alert, if any exist

To obtain information about silences:

. In the OpenShift Container Platform web console, go to the *Observe* -> *Alerting* -> *Silences* page.

. Optional: Filter the silences by name using the *Search by name* field.

. Optional: Filter silences by state by selecting filters in the *Filter* list. By default, *Active* and *Pending* filters are applied.

. Optional: Sort the silences by clicking one or more of the *Name*, *Firing alerts*, *State*, and *Creator* column headers.

. Select the name of a silence to view its *Silence details* page. The page includes the following details:

* Alert specification
* Start time
* End time
* Silence state
* Number and list of firing alerts

To obtain information about alerting rules:

. In the OpenShift Container Platform web console, go to the *Observe* -> *Alerting* -> *Alerting rules* page.

. Optional: Filter alerting rules by state, severity, and source by selecting filters in the *Filter* list.

. Optional: Sort the alerting rules by clicking one or more of the *Name*, *Severity*, *Alert state*, and *Source* column headers.

. Select the name of an alerting rule to view its *Alerting rule details* page. The page provides the following details about the alerting rule:

* Alerting rule name, severity, and description.
* The expression that defines the condition for firing the alert.
* The time for which the condition should be true for an alert to fire.
* A graph for each alert governed by the alerting rule, showing the value with which the alert is firing.
* A table of all alerts governed by the alerting rule.

[role="_additional-resources"]
.Additional resources
* GitHub {cmo-full} runbooks repository

[id="managing-silences_{context}"]
== Managing silences

You can create a silence for an alert in the OpenShift Container Platform web console.
After you create silences, you can view, edit, and expire them. You also do not receive notifications about a silenced alert when the alert fires.

[NOTE]
====
When you create silences, they are replicated across Alertmanager pods. However, if you do not configure persistent storage for Alertmanager, silences might be lost. This can happen, for example, if all Alertmanager pods restart at the same time.
====

[role="_additional-resources"]
.Additional resources

* Managing silences

* Configuring persistent storage

* Configuring persistent storage

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="silencing-alerts_{context}"]
= Silencing alerts

You can silence a specific alert or silence alerts that match a specification that you define.

.Prerequisites

* If you are a cluster administrator, you have access to the cluster as a user with the `cluster-admin` role.
* If you are a cluster administrator, you have access to the cluster as a user with the `dedicated-admin` role.
* If you are a non-administrator user, you have access to the cluster as a user with the following user roles:
** The `cluster-monitoring-view` cluster role, which allows you to access Alertmanager.
** The `monitoring-alertmanager-edit` role, which permits you to create and silence alerts.

.Procedure

To silence a specific alert:

. In the OpenShift Container Platform web console, go to *Observe* -> *Alerting* -> *Alerts*.

. For the alert that you want to silence, click {kebab} and select *Silence alert* to open the *Silence alert* page with a default configuration for the chosen alert.

. Optional: Change the default configuration details for the silence.
+
[NOTE]
====
You must add a comment before saving a silence.
====

. To save the silence, click *Silence*.

To silence a set of alerts:

. In the OpenShift Container Platform web console, go to *Observe* -> *Alerting* -> *Silences*.

. Click *Create silence*.

. On the *Create silence* page, set the schedule, duration, and label details for an alert.
+
[NOTE]
====
You must add a comment before saving a silence.
====

. To create silences for alerts that match the labels that you entered, click *Silence*.

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="editing-silences_{context}"]
= Editing silences

You can edit a silence, which expires the existing silence and creates a new one with the changed configuration.

.Prerequisites

* If you are a cluster administrator, you have access to the cluster as a user with the `cluster-admin` role.
* If you are a cluster administrator, you have access to the cluster as a user with the `dedicated-admin` role.
* If you are a non-administrator user, you have access to the cluster as a user with the following user roles:
** The `cluster-monitoring-view` cluster role, which allows you to access Alertmanager.
** The `monitoring-alertmanager-edit` role, which permits you to create and silence alerts.

.Procedure

. In the OpenShift Container Platform web console, go to *Observe* -> *Alerting* -> *Silences*.

. For the silence you want to modify, click {kebab} and select *Edit silence*.
+
Alternatively, you can click *Actions* and select *Edit silence* on the *Silence details* page for a silence.

. On the *Edit silence* page, make changes and click *Silence*. Doing so expires the existing silence and creates one with the updated configuration.

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="expiring-silences_{context}"]
= Expiring silences

You can expire a single silence or multiple silences. Expiring a silence deactivates it permanently.

[NOTE]
====
You cannot delete expired, silenced alerts.
Expired silences older than 120 hours are garbage collected.
====

.Prerequisites

* If you are a cluster administrator, you have access to the cluster as a user with the `cluster-admin` role.
* If you are a cluster administrator, you have access to the cluster as a user with the `dedicated-admin` role.
* If you are a non-administrator user, you have access to the cluster as a user with the following user roles:
** The `cluster-monitoring-view` cluster role, which allows you to access Alertmanager.
** The `monitoring-alertmanager-edit` role, which permits you to create and silence alerts.

.Procedure

. Go to *Observe* -> *Alerting* -> *Silences*.

. For the silence or silences you want to expire, select the checkbox in the corresponding row.

. Click *Expire 1 silence* to expire a single selected silence or *Expire _<n>_ silences* to expire multiple selected silences, where _<n>_ is the number of silences you selected.
+
Alternatively, to expire a single silence you can click *Actions* and select *Expire silence* on the *Silence details* page for a silence.

[id="managing-alerting-rules-for-user-defined-projects-uwm_{context}"]
== Managing alerting rules for user-defined projects

In OpenShift Container Platform, you can create, view, edit, and remove alerting rules for user-defined projects. Those alerting rules will trigger alerts based on the values of the chosen metrics.

[role="_additional-resources"]
.Additional resources

* Creating alerting rules for user-defined projects
* Managing alerting rules for user-defined projects
* Optimizing alerting for user-defined projects

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="creating-alerting-rules-for-user-defined-projects_{context}"]
= Creating alerting rules for user-defined projects

You can create alerting rules for user-defined projects. Those alerting rules will trigger alerts based on the values of the chosen metrics.

[NOTE]
====
To help users understand the impact and cause of the alert, ensure that your alerting rule contains an alert message and severity value.
====

.Prerequisites

* You have enabled monitoring for user-defined projects.
* You are logged in as a cluster administrator or as a user that has the `monitoring-rules-edit` cluster role for the project where you want to create an alerting rule.
* You have installed the {oc-first}.

.Procedure

. Create a YAML file for alerting rules. In this example, it is called `example-app-alerting-rule.yaml`.

. Add an alerting rule configuration to the YAML file.
The following example creates a new alerting rule named `example-alert`. The alerting rule fires an alert when the `version` metric exposed by the sample service becomes `0`:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: example-alert
  namespace: ns1
spec:
  groups:
  - name: example
    rules:
    - alert: VersionAlert # <1>
      for: 1m # <2>
      expr: version{job="prometheus-example-app"} == 0 # <3>
      labels:
        severity: warning # <4>
      annotations:
        message: This is an example alert. # <5>
----
<1> The name of the alerting rule you want to create.
<2> The duration for which the condition should be true before an alert is fired.
<3> The PromQL query expression that defines the new rule.
<4> The severity that alerting rule assigns to the alert.
<5> The message associated with the alert.

. Apply the configuration file to the cluster:
+
[source,terminal]
----
$ oc apply -f example-app-alerting-rule.yaml
----

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="creating-cross-project-alerting-rules-for-user-defined-projects_{context}"]
= Creating cross-project alerting rules for user-defined projects

You can create alerting rules that are not bound to their project of origin by configuring a project in the `user-workload-monitoring-config` config map. The `PrometheusRule` objects created in these projects are then applicable to all projects.

Therefore, you can have generic alerting rules that apply to multiple user-defined projects instead of having individual `PrometheusRule` objects in each user project. You can filter which projects are included or excluded from the alerting rule by using PromQL queries in the `PrometheusRule` object.

.Prerequisites

* If you are a cluster administrator, you have access to the cluster as a user with the `cluster-admin` cluster role.
* If you are a non-administrator user, you have access to the cluster as a user with the following user roles:
** The `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project to edit the `user-workload-monitoring-config` config map.
** The `monitoring-rules-edit` cluster role for the project where you want to create an alerting rule.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
+
[NOTE]
====
If you are a non-administrator user, you can still create cross-project alerting rules if you have the `monitoring-rules-edit` cluster role for the project where you want to create an alerting rule. However, that project needs to be configured in the `user-workload-monitoring-config` config map under the `namespacesWithoutLabelEnforcement` property, which can be done only by cluster administrators.
====
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
* You have installed the {oc-first}.

.Procedure

. Edit the `user-workload-monitoring-config` config map in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring edit configmap user-workload-monitoring-config
----

. Configure projects in which you want to create alerting rules that are not bound to a specific project:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-workload-monitoring-config
  namespace: openshift-user-workload-monitoring
data:
  config.yaml: |
    namespacesWithoutLabelEnforcement: [ <namespace1>, <namespace2> ] # <1>
    # ...
----
<1> Specify one or more projects in which you want to create cross-project alerting rules. Prometheus and Thanos Ruler for user-defined monitoring do not enforce the `namespace` label in `PrometheusRule` objects created in these projects, making the `PrometheusRule` objects applicable to all projects.

. Create a YAML file for alerting rules. In this example, it is called `example-cross-project-alerting-rule.yaml`.

. Add an alerting rule configuration to the YAML file.
The following example creates a new cross-project alerting rule called `example-security`. The alerting rule fires when a user project does not enforce the restricted pod security policy:
+
.Example cross-project alerting rule
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: example-security
  namespace: ns1 #<1>
spec:
  groups:
    - name: pod-security-policy
      rules:
        - alert: "ProjectNotEnforcingRestrictedPolicy" # <2>
          for: 5m # <3>
          expr: kube_namespace_labels{namespace!~"(openshift|kube).*|default",label_pod_security_kubernetes_io_enforce!="restricted"} # <4>
          annotations:
            message: "Restricted policy not enforced. Project {{ $labels.namespace }} does not enforce the restricted pod security policy." #<5>
          labels:
            severity: warning # <6>
----
<1> Ensure that you specify the project that you defined in the `namespacesWithoutLabelEnforcement` field.
<2> The name of the alerting rule you want to create.
<3> The duration for which the condition should be true before an alert is fired.
<4> The PromQL query expression that defines the new rule. You can use label matchers on the `namespace` label to filter which projects are included or excluded from the alerting rule.
<5> The message associated with the alert.
<6> The severity that alerting rule assigns to the alert.
+
[IMPORTANT]
====
Ensure that you create a specific cross-project alerting rule in only one of the projects that you specified in the `namespacesWithoutLabelEnforcement` field.
If you create the same cross-project alerting rule in multiple projects, it results in repeated alerts.
====

. Apply the configuration file to the cluster:
+
[source,terminal]
----
$ oc apply -f example-cross-project-alerting-rule.yaml
----

[role="_additional-resources"]
.Additional resources
* Monitoring stack architecture
* Alerting (Prometheus documentation)

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="accessing-alerting-rules-for-your-project_{context}"]
= Accessing alerting rules for user-defined projects

To list alerting rules for a user-defined project, you must have been assigned the `monitoring-rules-view` cluster role for the project.

.Prerequisites

* You have enabled monitoring for user-defined projects.
* You are logged in as a user that has the `monitoring-rules-view` cluster role for your project.
* You have installed the {oc-first}.

.Procedure

. To list alerting rules in `<project>`:
+
[source,terminal]
----
$ oc -n <project> get prometheusrule
----

. To list the configuration of an alerting rule, run the following:
+
[source,terminal]
----
$ oc -n <project> get prometheusrule <rule> -o yaml
----

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="removing-alerting-rules-for-user-defined-projects_{context}"]
= Removing alerting rules for user-defined projects

You can remove alerting rules for user-defined projects.

.Prerequisites

* You have enabled monitoring for user-defined projects.
* You are logged in as a cluster administrator or as a user that has the `monitoring-rules-edit` cluster role for the project where you want to create an alerting rule.
* You have installed the {oc-first}.

.Procedure

* To remove rule `<alerting_rule>` in `<namespace>`, run the following:
+
[source,terminal]
----
$ oc -n <namespace> delete prometheusrule <alerting_rule>
----

[role="_additional-resources"]
.Additional resources

* Alertmanager (Prometheus documentation)
