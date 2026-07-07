---
title: "Preparing to configure core platform monitoring stack"
type: reference
domain: openshift
slug: observability-4-22-preparing-to-configure-the-monitoring-stack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/preparing-to-configure-the-monitoring-stack
version: 4.22
family: observability
documentKind: "Documentation"
---

# Preparing to configure core platform monitoring stack

[id="preparing-to-configure-the-monitoring-stack"]
= Preparing to configure core platform monitoring stack

The OpenShift Container Platform installation program provides only a low number of configuration options before installation. Configuring most OpenShift Container Platform framework components, including the cluster monitoring stack, happens after the installation.

This section explains which monitoring components can be configured and how to prepare for configuring the monitoring stack.

[IMPORTANT]
====
* Not all configuration parameters for the monitoring stack are exposed.
Only the parameters and fields listed in the Config map reference for the {cmo-full} are supported for configuration.

* The monitoring stack imposes additional resource requirements. Consult the computing resources recommendations in Scaling the {cmo-full} and verify that you have sufficient resources.
====

// Configurable monitoring components
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="configurable-monitoring-components_{context}"]
= Configurable monitoring components

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples.
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

This table shows the monitoring components you can configure and the keys used to specify the components in the `{configmap-name}` config map.

// tag::UWM[]
[WARNING]
====
Do not modify the monitoring components in the `cluster-monitoring-config` `ConfigMap` object. Red{nbsp}Hat Site Reliability Engineers (SRE) use these components to monitor the core cluster components and Kubernetes services.
====
// end::UWM[]

// tag::CPM[]
.Configurable core platform monitoring components
// end::CPM[]
// tag::UWM[]
.Configurable monitoring components for user-defined projects
// end::UWM[]
[options="header"]
|====
|Component |{configmap-name} config map key
|Prometheus Operator |`prometheusOperator`
|Prometheus |`{prometheus}`
|Alertmanager |`{alertmanager}`
|{thanosname} | `{thanos}`
// tag::CPM[]
|kube-state-metrics |`kubeStateMetrics`
|monitoring-plugin | `monitoringPlugin`
|openshift-state-metrics |`openshiftStateMetrics`
|Telemeter Client |`telemeterClient`
|Metrics Server |`metricsServer`
// end::CPM[]
|====

[WARNING]
====
Different configuration changes to the `ConfigMap` object result in different outcomes:

* The pods are not redeployed. Therefore, there is no service outage.

* The affected pods are redeployed:

** For single-node clusters, this results in temporary service outage.

** For multi-node clusters, because of high-availability, the affected pods are gradually rolled out and the monitoring stack remains available.

** Configuring and resizing a persistent volume always results in a service outage, regardless of high availability.

Each procedure that requires a change in the config map includes its expected outcome.
====

// Unset the source code block attributes just to be safe.

// Creating a cluster monitoring config map
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="creating-cluster-monitoring-configmap_{context}"]
= Creating a cluster monitoring config map

You can configure the core OpenShift Container Platform monitoring components by creating and updating the `cluster-monitoring-config` config map in the `openshift-monitoring` project. The {cmo-first} then configures the core components of the monitoring stack.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have installed the {oc-first}.

.Procedure

. Check whether the `cluster-monitoring-config` `ConfigMap` object exists:
+
[source,terminal]
----
$ oc -n openshift-monitoring get configmap cluster-monitoring-config
----

. If the `ConfigMap` object does not exist:
.. Create the following YAML manifest. In this example the file is called `cluster-monitoring-config.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
----
+
.. Apply the configuration to create the `ConfigMap` object:
+
[source,terminal]
----
$ oc apply -f cluster-monitoring-config.yaml
----

// Granting users permissions for core platform monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="granting-users-permissions-for-core-platform-monitoring_{context}"]
= Granting users permissions for core platform monitoring

As a cluster administrator, you can monitor all core OpenShift Container Platform and user-defined projects.

You can also grant developers and other users different permissions for core platform monitoring. You can grant the permissions by assigning one of the following monitoring roles or cluster roles:

|===
|Name |Description |Project

|`cluster-monitoring-metrics-api`
|Users with this role have the ability to access Thanos Querier API endpoints. Additionally, it grants access to the core platform Prometheus API and user-defined Thanos Ruler API endpoints.
|`openshift-monitoring`

|`cluster-monitoring-operator-alert-customization`
|Users with this role can manage `AlertingRule` and `AlertRelabelConfig` resources for core platform monitoring. These permissions are required for the alert customization feature.
|`openshift-monitoring`

|`monitoring-alertmanager-edit`
|Users with this role can manage the Alertmanager API for core platform monitoring. They can also manage alert silences in the OpenShift Container Platform web console.
|`openshift-monitoring`

|`monitoring-alertmanager-view`
|Users with this role can monitor the Alertmanager API for core platform monitoring. They can also view alert silences in the OpenShift Container Platform web console.
|`openshift-monitoring`

|`cluster-monitoring-view`
|Users with this cluster role have the same access rights as `cluster-monitoring-metrics-api` role, with additional permissions, providing access to the `/federate` endpoint for the user-defined Prometheus.
|Must be bound with `ClusterRoleBinding` to gain access to the `/federate` endpoint for the user-defined Prometheus.
|===

[role="_additional-resources"]
.Additional resources

* Resources reference for the {cmo-full}
* CMO services resources

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="granting-user-permissions-using-the-web-console_{context}"]
= Granting user permissions by using the web console

You can grant users permissions for the `openshift-monitoring` project or their own projects, by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* The user account that you are assigning the role to already exists.

.Procedure

. In the OpenShift Container Platform web console, go to *User Management* -> *RoleBindings* -> *Create binding*.

. In the *Binding Type* section, select the *Namespace Role Binding* type.

. In the *Name* field, enter a name for the role binding.

. In the *Namespace* field, select the project where you want to grant the access.
+
[IMPORTANT]
====
The monitoring role or cluster role permissions that you grant to a user by using this procedure apply only to the project that you select in the *Namespace* field.
====

. Select a monitoring role or cluster role from the *Role Name* list.

. In the *Subject* section, select *User*.

. In the *Subject Name* field, enter the name of the user.

. Select *Create* to apply the role binding.

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="granting-user-permissions-using-the-cli_{context}"]
= Granting user permissions by using the CLI

You can grant users permissions
// tag::CPM[]
for the `openshift-monitoring` project or
// end::CPM[]
// tag::UWM[]
to monitor
// end::UWM[]
their own projects, by using the {oc-first}.

[IMPORTANT]
====
Whichever role or cluster role you choose, you must bind it against a specific project as a cluster administrator.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* The user account that you are assigning the role to already exists.
* You have installed the {oc-first}.

.Procedure

* To assign a monitoring role to a user for a project, enter the following command:
+
[source,terminal]
----
$ oc adm policy add-role-to-user <role> <user> -n <namespace> --role-namespace <namespace> <1>
----
<1> Substitute `<role>` with the wanted monitoring role, `<user>` with the user to whom you want to assign the role, and `<namespace>` with the project where you want to grant the access.

* To assign a monitoring cluster role to a user for a project, enter the following command:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user <cluster-role> <user> -n <namespace> <1>
----
<1> Substitute `<cluster-role>` with the wanted monitoring cluster role, `<user>` with the user to whom you want to assign the cluster role, and `<namespace>` with the project where you want to grant the access.
