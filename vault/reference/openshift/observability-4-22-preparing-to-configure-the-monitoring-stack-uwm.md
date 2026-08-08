---
title: "Preparing to configure the user workload monitoring stack"
type: reference
domain: openshift
slug: observability-4-22-preparing-to-configure-the-monitoring-stack-uwm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/preparing-to-configure-the-monitoring-stack-uwm
version: 4.22
family: observability
documentKind: "Documentation"
---

# Preparing to configure the user workload monitoring stack

[id="preparing-to-configure-the-monitoring-stack-uwm"]
= Preparing to configure the user workload monitoring stack

This section explains which user-defined monitoring components can be configured
, how to enable user workload monitoring,
and how to prepare for configuring the user workload monitoring stack.

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

// Enabling monitoring for user-defined projects
[id="enabling-monitoring-for-user-defined-projects-uwm_{context}"]
== Enabling monitoring for user-defined projects

In OpenShift Container Platform, you can enable monitoring for user-defined projects in addition to the default platform monitoring. You can monitor your own projects in OpenShift Container Platform without the need for an additional monitoring solution. Using this feature centralizes monitoring for core platform components and user-defined projects.

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="enabling-monitoring-for-user-defined-projects_{context}"]
= Enabling monitoring for user-defined projects

Cluster administrators can enable monitoring for user-defined projects by setting the `enableUserWorkload: true` field in the cluster monitoring `ConfigMap` object.

[IMPORTANT]
====
You must remove any custom Prometheus instances before enabling monitoring for user-defined projects.
====

[NOTE]
====
You must have access to the cluster as a user with the `cluster-admin` cluster role to enable monitoring for user-defined projects in OpenShift Container Platform. Cluster administrators can then optionally grant users permission to configure the components that are responsible for monitoring user-defined projects.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have installed the {oc-first}.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have optionally created and configured the `user-workload-monitoring-config` `ConfigMap` object in the `openshift-user-workload-monitoring` project. You can add configuration options to this `ConfigMap` object for the components that monitor user-defined projects.
+
[NOTE]
====
Every time you save configuration changes to the `user-workload-monitoring-config` `ConfigMap` object, the pods in the `openshift-user-workload-monitoring` project are redeployed. It might sometimes take a while for these components to redeploy.
====

.Procedure

. Edit the `cluster-monitoring-config` `ConfigMap` object:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----

. Add `enableUserWorkload: true` under `data/config.yaml`:
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
    enableUserWorkload: true <1>
----
<1> When set to `true`, the `enableUserWorkload` parameter enables monitoring for user-defined projects in a cluster.

. Save the file to apply the changes. Monitoring for user-defined projects is then enabled automatically.
+
[NOTE]
====
If you enable monitoring for user-defined projects, the `user-workload-monitoring-config` `ConfigMap` object is created by default.
====

. Verify that the `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` pods are running in the `openshift-user-workload-monitoring` project. It might take a short while for the pods to start:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pod
----
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS        RESTARTS   AGE
prometheus-operator-6f7b748d5b-t7nbg   2/2     Running       0          3h
prometheus-user-workload-0             4/4     Running       1          3h
prometheus-user-workload-1             4/4     Running       1          3h
thanos-ruler-user-workload-0           3/3     Running       0          3h
thanos-ruler-user-workload-1           3/3     Running       0          3h
----

[role="_additional-resources"]
.Additional resources

* User workload monitoring first steps

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="granting-users-permission-to-configure-monitoring-for-user-defined-projects_{context}"]
= Granting users permission to configure monitoring for user-defined projects

As a cluster administrator, you can assign the `user-workload-monitoring-config-edit` role to a user. This grants permission to configure and manage monitoring for user-defined projects without giving them permission to configure and manage core OpenShift Container Platform monitoring components.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* The user account that you are assigning the role to already exists.
* You have installed the {oc-first}.

.Procedure

. Assign the `user-workload-monitoring-config-edit` role to a user in the `openshift-user-workload-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring adm policy add-role-to-user \
  user-workload-monitoring-config-edit <user> \
  --role-namespace openshift-user-workload-monitoring
----

. Verify that the user is correctly assigned to the `user-workload-monitoring-config-edit` role by displaying the related role binding:
+
[source,terminal]
----
$ oc describe rolebinding <role_binding_name> -n openshift-user-workload-monitoring
----
+
.Example command
[source,terminal]
----
$ oc describe rolebinding user-workload-monitoring-config-edit -n openshift-user-workload-monitoring
----
+
.Example output
[source,terminal]
----
Name:         user-workload-monitoring-config-edit
Labels:       <none>
Annotations:  <none>
Role:
  Kind:  Role
  Name:  user-workload-monitoring-config-edit
Subjects:
  Kind  Name  Namespace
  ----  ----  ---------
  User  user1           <1>
----
<1> In this example, `user1` is assigned to the `user-workload-monitoring-config-edit` role.

// Enabling alert routing for user-defined projects
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-alert-routing-for-user-defined-projects.adoc

[id="enabling-alert-routing-for-user-defined-projects_{context}"]
= Enabling alert routing for user-defined projects

In OpenShift Container Platform, an administrator can enable alert routing for user-defined projects.
This process consists of the following steps:

* Enable alert routing for user-defined projects:
** Use the default platform Alertmanager instance.
** Use a separate Alertmanager instance only for user-defined projects.
* Enable alert routing for user-defined projects to use a separate Alertmanager instance.
* Grant users permission to configure alert routing for user-defined projects.

After you complete these steps, developers and other users can configure custom alerts and alert routing for their user-defined projects.

[role="_additional-resources"]
.Additional resources

* Understanding alert routing for user-defined projects

// Enabling the platform Alertmanager instance for user-defined alert routing
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-alert-routing-for-user-defined-projects.adoc

[id="enabling-the-platform-alertmanager-instance-for-user-defined-alert-routing_{context}"]
= Enabling the platform Alertmanager instance for user-defined alert routing

You can allow users to create user-defined alert routing configurations that use the main platform instance of Alertmanager.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have installed the {oc-first}.

.Procedure

. Edit the `cluster-monitoring-config` `ConfigMap` object:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----
+
. Add `enableUserAlertmanagerConfig: true` in the `alertmanagerMain` section under `data/config.yaml`:
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
    # ...
    alertmanagerMain:
      enableUserAlertmanagerConfig: true # <1>
    # ...
----
<1> Set the `enableUserAlertmanagerConfig` value to `true` to allow users to create user-defined alert routing configurations that use the main platform instance of Alertmanager.
+
. Save the file to apply the changes. The new configuration is applied automatically.

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-alert-routing-for-user-defined-projects.adoc

[id="enabling-a-separate-alertmanager-instance-for-user-defined-alert-routing_{context}"]
= Enabling a separate Alertmanager instance for user-defined alert routing

In some clusters, you might want to deploy a dedicated Alertmanager instance for user-defined projects, which can help reduce the load on the default platform Alertmanager instance and can better separate user-defined alerts from default platform alerts.
In OpenShift Container Platform, you may want to deploy a dedicated Alertmanager instance for user-defined projects, which provides user-defined alerts separate from default platform alerts.
In these cases, you can optionally enable a separate instance of Alertmanager to send alerts for user-defined projects only.

.Prerequisites

* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have enabled monitoring for user-defined projects.
* You have installed the {oc-first}.

.Procedure

. Edit the `user-workload-monitoring-config` `ConfigMap` object:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring edit configmap user-workload-monitoring-config
----
+
. Add `enabled: true` and `enableAlertmanagerConfig: true` in the `alertmanager` section under `data/config.yaml`:
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
    alertmanager:
      enabled: true # <1>
      enableAlertmanagerConfig: true # <2>
----
<1> Set the `enabled` value to `true` to enable a dedicated instance of the Alertmanager for user-defined projects in a cluster. Set the value to `false` or omit the key entirely to disable the Alertmanager for user-defined projects.
If you set this value to `false` or if the key is omitted, user-defined alerts are routed to the default platform Alertmanager instance.
<2> Set the `enableAlertmanagerConfig` value to `true` to enable users to define their own alert routing configurations with `AlertmanagerConfig` objects.
+
. Save the file to apply the changes. The dedicated instance of Alertmanager for user-defined projects starts automatically.

.Verification

* Verify that the `user-workload` Alertmanager instance has started:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get alertmanager
----
+
.Example output
+
[source,terminal]
----
NAME            VERSION   REPLICAS   AGE
user-workload   0.24.0    2          100s
----

// In ROSA/OSD, a dedicated-admin doesn't have permission to view the alertmanager resource.
* Verify that the `alert-manager-user-workload` pods are running:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pods
----
+
.Example output
+
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
alertmanager-user-workload-0           6/6     Running   0          38s
alertmanager-user-workload-1           6/6     Running   0          38s
...
----

// Module included in the following assemblies:
//
// * observability/monitoring/enabling-alert-routing-for-user-defined-projects.adoc

[id="granting-users-permission-to-configure-alert-routing-for-user-defined-projects_{context}"]
= Granting users permission to configure alert routing for user-defined projects

You can grant users permission to configure alert routing for user-defined projects.

.Prerequisites

* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have enabled monitoring for user-defined projects.
* The user account that you are assigning the role to already exists.
* You have installed the {oc-first}.

.Procedure

* Assign the `alert-routing-edit` cluster role to a user in the user-defined project:
+
[source,terminal]
----
$ oc -n <namespace> adm policy add-role-to-user alert-routing-edit <user> <1>
----
<1> For `<namespace>`, substitute the namespace for the user-defined project, such as `ns1`. For `<user>`, substitute the username for the account to which you want to assign the role.

[role="_additional-resources"]
.Additional resources

* Configuring alert notifications

// Granting users permissions for monitoring for user-defined projects
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="granting-users-permission-to-monitor-user-defined-projects_{context}"]
= Granting users permissions for monitoring for user-defined projects

As a cluster administrator, you can monitor all core OpenShift Container Platform and user-defined projects.

You can also grant developers and other users different permissions:

* Monitoring user-defined projects
* Configuring the components that monitor user-defined projects
* Configuring alert routing for user-defined projects
* Managing alerts and silences for user-defined projects

You can grant the permissions by assigning one of the following monitoring roles or cluster roles:

.Monitoring roles
|===
|Role name |Description |Project

|`user-workload-monitoring-config-edit`
|Users with this role can edit the `user-workload-monitoring-config` `ConfigMap` object to configure Prometheus, Prometheus Operator, Alertmanager, and Thanos Ruler for user-defined workload monitoring.
|`openshift-user-workload-monitoring`

|`monitoring-alertmanager-api-reader`
|Users with this role have read access to the user-defined Alertmanager API for all projects, if the user-defined Alertmanager is enabled.
|`openshift-user-workload-monitoring`

|`monitoring-alertmanager-api-writer`
|Users with this role have read and write access to the user-defined Alertmanager API for all projects, if the user-defined Alertmanager is enabled.
|`openshift-user-workload-monitoring`
|===

.Monitoring cluster roles
|===
|Cluster role name |Description |Project

|`monitoring-rules-view`
|Users with this cluster role have read access to `PrometheusRule` custom resources (CRs) for user-defined projects.
|Can be bound with `RoleBinding` to any user project.

|`monitoring-rules-edit`
|Users with this cluster role can create, modify, and delete `PrometheusRule` CRs for user-defined projects.
|Can be bound with `RoleBinding` to any user project.

|`monitoring-edit`
|Users with this cluster role have the same privileges as users with the `monitoring-rules-edit` cluster role. Additionally, users can create, read, modify, and delete `ServiceMonitor` and `PodMonitor` resources to scrape metrics from services and pods.
|Can be bound with `RoleBinding` to any user project.

|`alert-routing-edit`
|Users with this cluster role can create, update, and delete `AlertmanagerConfig` CRs for user-defined projects.
|Can be bound with `RoleBinding` to any user project.

|`pod-metrics-reader`
|Users with this cluster role can access Thanos API endpoints for user-defined projects.
|Can be bound with `RoleBinding` to any user project.
|===

[role="_additional-resources"]
.Additional resources
* CMO services resources
* Granting users permission to configure monitoring for user-defined projects
* Granting users permission to configure alert routing for user-defined projects

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

// Excluding a user-defined project from monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc
// * observability/monitoring/sd-disabling-monitoring-for-user-defined-projects.adoc

[id="excluding-a-user-defined-project-from-monitoring_{context}"]
= Excluding a user-defined project from monitoring

[role="_abstract"]
Individual user-defined projects can be excluded from user workload monitoring. To do so, add the `openshift.io/user-monitoring` label to the project's namespace with a value of `false`.

.Procedure

. Add the label to the project namespace:
+
[source,terminal]
----
$ oc label namespace my-project 'openshift.io/user-monitoring=false'
----
+
. To re-enable monitoring, remove the label from the namespace:
+
[source,terminal]
----
$ oc label namespace my-project 'openshift.io/user-monitoring-'
----
+
[NOTE]
====
If there were any active monitoring targets for the project, it can take a few minutes for Prometheus to stop scraping them after adding the label.
====

// Disabling monitoring for user-defined projects
// Module included in the following assemblies:
//
// * observability/monitoring/enabling-monitoring-for-user-defined-projects.adoc

[id="disabling-monitoring-for-user-defined-projects_{context}"]
= Disabling monitoring for user-defined projects

After enabling monitoring for user-defined projects, you can disable it again by setting `enableUserWorkload: false` in the cluster monitoring `ConfigMap` object.

[NOTE]
====
Alternatively, you can remove `enableUserWorkload: true` to disable monitoring for user-defined projects.
====

.Procedure

. Edit the `cluster-monitoring-config` `ConfigMap` object:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----
+
.. Set `enableUserWorkload:` to `false` under `data/config.yaml`:
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
    enableUserWorkload: false
----

. Save the file to apply the changes. Monitoring for user-defined projects is then disabled automatically.

. Check that the `prometheus-operator`, `prometheus-user-workload` and `thanos-ruler-user-workload` pods are terminated in the `openshift-user-workload-monitoring` project. This might take a short while:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get pod
----
+
.Example output
[source,terminal]
----
No resources found in openshift-user-workload-monitoring project.
----

[NOTE]
====
The `user-workload-monitoring-config` `ConfigMap` object in the `openshift-user-workload-monitoring` project is not automatically deleted when monitoring for user-defined projects is disabled. This is to preserve any custom configurations that you may have created in the `ConfigMap` object.
====
