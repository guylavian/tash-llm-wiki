---
title: "Configuring alerts and notifications for user workload monitoring"
type: reference
domain: openshift
slug: observability-4-22-configuring-alerts-and-notifications-uwm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-alerts-and-notifications-uwm
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring alerts and notifications for user workload monitoring

[id="configuring-alerts-and-notifications-uwm"]
= Configuring alerts and notifications for user workload monitoring

You can configure a local or external Alertmanager instance to route alerts from Prometheus to endpoint receivers. You can also attach custom labels to all time series and alerts to add useful metadata information.

//Configuring external Alertmanager instances
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="monitoring-configuring-external-alertmanagers_{context}"]
= Configuring external Alertmanager instances

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

The OpenShift Container Platform monitoring stack includes a local Alertmanager instance that routes alerts from Prometheus.

// tag::CPM[]
You can add external Alertmanager instances to route alerts for core OpenShift Container Platform projects.
// end::CPM[]
// tag::UWM[]
You can add external Alertmanager instances to route alerts for user-defined projects.
// end::UWM[]

If you add the same external Alertmanager configuration for multiple clusters and disable the local instance for each cluster, you can then manage alert routing for multiple clusters by using a single external Alertmanager instance.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add an `additionalAlertmanagerConfigs` section with configuration details under
// tag::CPM[]
`data/config.yaml/prometheusK8s`:
// end::CPM[]
// tag::UWM[]
`data/config.yaml/<component>`:
// end::UWM[]
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
# tag::CPM[]
    prometheusK8s:
# end::CPM[]
# tag::UWM[]
    <component>: # <2>
# end::UWM[]
      additionalAlertmanagerConfigs:
      - <alertmanager_specification> # <1>
----
<1> Substitute `<alertmanager_specification>` with authentication and other configuration details for additional Alertmanager instances.
Currently supported authentication methods are bearer token (`bearerToken`) and client TLS (`tlsConfig`).
// tag::UWM[]
<2> Substitute `<component>` for one of two supported external Alertmanager components: `prometheus` or `thanosRuler`.
// end::UWM[]
+
The following sample config map configures an additional Alertmanager for {component-name} by using a bearer token with client TLS authentication:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      additionalAlertmanagerConfigs:
      - scheme: https
        pathPrefix: /
        timeout: "30s"
        apiVersion: v1
        bearerToken:
          name: alertmanager-bearer-token
          key: token
        tlsConfig:
          key:
            name: alertmanager-tls
            key: tls.key
          cert:
            name: alertmanager-tls
            key: tls.crt
          ca:
            name: alertmanager-tls
            key: tls.ca
        staticConfigs:
        - external-alertmanager1-remote.com
        - external-alertmanager1-remote2.com
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

//Configuring secrets for Alertmanager
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="monitoring-configuring-secrets-for-alertmanager_{context}"]
= Configuring secrets for Alertmanager

The OpenShift Container Platform monitoring stack includes Alertmanager, which routes alerts from Prometheus to endpoint receivers.
If you need to authenticate with a receiver so that Alertmanager can send alerts to it, you can configure Alertmanager to use a secret that contains authentication credentials for the receiver.

For example, you can configure Alertmanager to use a secret to authenticate with an endpoint receiver that requires a certificate issued by a private Certificate Authority (CA).
You can also configure Alertmanager to use a secret to authenticate with a receiver that requires a password file for Basic HTTP authentication.
In either case, authentication details are contained in the `Secret` object rather than in the `ConfigMap` object.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="monitoring-adding-a-secret-to-the-alertmanager-configuration_{context}"]
= Adding a secret to the Alertmanager configuration

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can add secrets to the Alertmanager configuration by editing the `{configmap-name}` config map in the `{namespace-name}` project.

After you add a secret to the config map, the secret is mounted as a volume at `/etc/alertmanager/secrets/<secret_name>` within the `alertmanager` container for the Alertmanager pods.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` config map.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have created the secret to be configured in Alertmanager in the `{namespace-name}` project.
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add a `secrets:` section under `data/config.yaml/{component}` with the following configuration:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      secrets: # <1>
      - <secret_name_1> # <2>
      - <secret_name_2>
----
<1> This section contains the secrets to be mounted into Alertmanager. The secrets must be located within the same namespace as the Alertmanager object.
<2> The name of the `Secret` object that contains authentication credentials for the receiver. If you add multiple secrets, place each one on a new line.
+
The following sample config map settings configure Alertmanager to use two `Secret` objects named `test-secret-basic-auth` and `test-secret-api-token`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      secrets:
      - test-secret-basic-auth
      - test-secret-api-token
----

. Save the file to apply the changes. The new configuration is applied automatically.

// Unset the source code block attributes just to be safe.

//Attaching additional labels to your time series and alerts
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="attaching-additional-labels-to-your-time-series-and-alerts_{context}"]
= Attaching additional labels to your time series and alerts

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples

// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can attach custom labels to all time series and alerts leaving Prometheus by using the external labels feature of Prometheus.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Define labels you want to add for every metric under `data/config.yaml`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      externalLabels:
        <key>: <value> # <1>
----
<1> Substitute `<key>: <value>` with key-value pairs where `<key>` is a unique name for the new label and `<value>` is its value.
+
[WARNING]
====
* Do not use `prometheus` or `prometheus_replica` as key names, because they are reserved and will be overwritten.

* Do not use `cluster` as a key name. Using it can cause issues where you are unable to see data in the developer dashboards.
====
// tag::UWM[]
+
[NOTE]
====
In the `openshift-user-workload-monitoring` project, Prometheus handles metrics and Thanos Ruler handles alerting and recording rules. Setting `externalLabels` for `prometheus` in the `user-workload-monitoring-config` `ConfigMap` object will only configure external labels for metrics and not for any rules.
====
// end::UWM[]
+
For example, to add metadata about the region and environment to all time series and alerts, use the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      externalLabels:
        region: eu
        environment: prod
----

. Save the file to apply the changes. The pods affected by the new configuration are automatically redeployed.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Enabling monitoring for user-defined projects

[id="configuring-alert-notifications_{context}"]
== Configuring alert notifications

In OpenShift Container Platform, an administrator can enable alert routing for user-defined projects with one of the following methods:

* Use the default platform Alertmanager instance.
* Use a separate Alertmanager instance only for user-defined projects.

In OpenShift Container Platform, the `dedicated-admin` user can enable alert routing for user-defined projects by using a separate Alertmanager instance for user-defined projects.

Developers and other users with the `alert-routing-edit` cluster role can configure custom alert notifications for their user-defined projects by configuring alert receivers.

[NOTE]
====
Review the following limitations of alert routing for user-defined projects:

* User-defined alert routing is scoped to the namespace in which the resource is defined. For example, a routing configuration in namespace `ns1` only applies to `PrometheusRules` resources in the same namespace.

* When a namespace is excluded from user-defined monitoring, `AlertmanagerConfig` resources in the namespace cease to be part of the Alertmanager configuration.
====

[role="_additional-resources"]
.Additional resources

* Understanding alert routing for user-defined projects
* Sending notifications to external systems
* PagerDuty website
* Prometheus Integration Guide (PagerDuty documentation)
* Support version matrix for monitoring components
* Enabling alert routing for user-defined projects

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="configuring-alert-routing-for-user-defined-projects_{context}"]
= Configuring alert routing for user-defined projects

If you are a non-administrator user who has been given the `alert-routing-edit` cluster role, you can create or edit alert routing for user-defined projects.

.Prerequisites

* A cluster administrator has enabled monitoring for user-defined projects.
* A cluster administrator has enabled alert routing for user-defined projects.
* Alert routing has been enabled for user-defined projects.
* You are logged in as a user that has the `alert-routing-edit` cluster role for the project for which you want to create alert routing.
* You have installed the {oc-first}.

.Procedure

. Create a YAML file for alert routing. The example in this procedure uses a file called `example-app-alert-routing.yaml`.

. Add an `AlertmanagerConfig` YAML definition to the file. For example:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1beta1
kind: AlertmanagerConfig
metadata:
  name: example-routing
  namespace: ns1
spec:
  route:
    receiver: default
    groupBy: [job]
  receivers:
  - name: default
    webhookConfigs:
    - url: https://example.org/post
----

. Save the file.

. Apply the resource to the cluster:
+
[source,terminal]
----
$ oc apply -f example-app-alert-routing.yaml
----
+
The configuration is automatically applied to the Alertmanager pods.

[role="_additional-resources"]
.Additional resources

* Send test alerts to Alertmanager in OpenShift 4 (Red{nbsp}Hat Customer Portal)

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="configuring-alert-routing-user-defined-alerts-secret_{context}"]
= Configuring alert routing for user-defined projects with the Alertmanager secret

If you have enabled a separate instance of Alertmanager that is dedicated to user-defined alert routing, you can customize where and how the instance sends notifications by editing the `alertmanager-user-workload` secret in the `openshift-user-workload-monitoring` namespace.

[NOTE]
====
All features of a supported version of upstream Alertmanager are also supported in an OpenShift Container Platform Alertmanager configuration. To check all the configuration options of a supported version of upstream Alertmanager, see Alertmanager configuration (Prometheus documentation).
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have enabled a separate instance of Alertmanager for user-defined alert routing.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the {oc-first}.

.Procedure

. Print the currently active Alertmanager configuration into the file `alertmanager.yaml`:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring get secret alertmanager-user-workload --template='{{ index .data "alertmanager.yaml" }}' | base64 --decode > alertmanager.yaml
----
+
. Edit the configuration in `alertmanager.yaml`:
+
[source,yaml]
----
global:
  http_config:
    proxy_from_environment: true # <1>
route:
  receiver: Default
  group_by:
  - name: Default
  routes:
  - matchers:
    - "service = prometheus-example-monitor" # <2>
    receiver: <receiver> # <3>
receivers:
- name: Default
- name: <receiver>
  <receiver_configuration> # <4>
----
<1> If you configured an HTTP cluster-wide proxy, set the `proxy_from_environment` parameter to `true` to enable proxying for all alert receivers.
<2> Specify labels to match your alerts. This example targets all alerts that have the `service="prometheus-example-monitor"` label.
<3> Specify the name of the receiver to use for the alerts group.
<4> Specify the receiver configuration.
+
. Apply the new configuration in the file:
+
[source,terminal]
----
$ oc -n openshift-user-workload-monitoring create secret generic alertmanager-user-workload --from-file=alertmanager.yaml --dry-run=client -o=yaml |  oc -n openshift-user-workload-monitoring replace secret --filename=-
----

[role="_additional-resources"]
.Additional resources

* Send test alerts to Alertmanager in OpenShift 4 (Red{nbsp}Hat Customer Portal)

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="configuring-different-alert-receivers-for-default-platform-alerts-and-user-defined-alerts_{context}"]
= Configuring different alert receivers for default platform alerts and user-defined alerts

You can configure different alert receivers for default platform alerts and user-defined alerts to ensure the following results:

* All default platform alerts are sent to a receiver owned by the team in charge of these alerts.
* All user-defined alerts are sent to another receiver so that the team can focus only on platform alerts.

You can achieve this by using the `openshift_io_alert_source="platform"` label that is added by the {cmo-full} to all platform alerts:

* Use the `openshift_io_alert_source="platform"` matcher to match default platform alerts.
* Use the `openshift_io_alert_source!="platform"` or `'openshift_io_alert_source=""'` matcher to match user-defined alerts.

[NOTE]
====
This configuration does not apply if you have enabled a separate instance of Alertmanager dedicated to user-defined alerts.
====
