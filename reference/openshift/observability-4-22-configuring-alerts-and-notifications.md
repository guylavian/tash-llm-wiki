---
title: "Configuring alerts and notifications for core platform monitoring"
type: reference
domain: openshift
slug: observability-4-22-configuring-alerts-and-notifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-alerts-and-notifications
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring alerts and notifications for core platform monitoring

[id="configuring-alerts-and-notifications"]
= Configuring alerts and notifications for core platform monitoring

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

// Disabling the local Alertmanager
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="monitoring-disabling-the-local-alertmanager_{context}"]
= Disabling the local Alertmanager

A local Alertmanager that routes alerts from Prometheus instances is enabled by default in the `openshift-monitoring` project of the OpenShift Container Platform monitoring stack.

If you do not need the local Alertmanager, you can disable it by configuring the `cluster-monitoring-config` config map in the `openshift-monitoring` project.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` config map.
* You have installed the {oc-first}.

.Procedure

. Edit the `cluster-monitoring-config` config map in the `openshift-monitoring` project:
+
[source,terminal]
----
$ oc -n openshift-monitoring edit configmap cluster-monitoring-config
----

. Add `enabled: false` for the `alertmanagerMain` component under `data/config.yaml`:
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
    alertmanagerMain:
      enabled: false
----

. Save the file to apply the changes. The Alertmanager instance is disabled automatically when you apply the change.

[role="_additional-resources"]
.Additional resources

* Alertmanager (Prometheus documentation)
* Managing alerts as an Administrator

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

* Preparing to configure core platform monitoring stack

[id="configuring-alert-notifications_{context}"]
== Configuring alert notifications

In OpenShift Container Platform,
In OpenShift Container Platform ,
you can view firing alerts in the Alerting UI. You can configure Alertmanager to send notifications about default platform alerts by configuring alert receivers.

[IMPORTANT]
====
Alertmanager does not send notifications by default. It is strongly recommended to configure Alertmanager to receive notifications by configuring alert receivers through the web console or through the `alertmanager-main` secret.
====

[role="_additional-resources"]
.Additional resources

* Sending notifications to external systems
* PagerDuty website
* Prometheus Integration Guide (PagerDuty documentation)
* Support version matrix for monitoring components
* Enabling alert routing for user-defined projects

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc

[id="configuring-alert-routing-default-platform-alerts_{context}"]
= Configuring alert routing for default platform alerts

You can configure Alertmanager to send notifications to receive important alerts coming from your cluster. Customize where and how Alertmanager sends notifications about default platform alerts by editing the default configuration in the `alertmanager-main` secret in the `openshift-monitoring` namespace.

[NOTE]
====
All features of a supported version of upstream Alertmanager are also supported in an OpenShift Container Platform Alertmanager configuration. To check all the configuration options of a supported version of upstream Alertmanager, see Alertmanager configuration (Prometheus documentation).
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have installed the {oc-first}.

.Procedure

. Extract the currently active Alertmanager configuration from the `alertmanager-main` secret and save it as a local `alertmanager.yaml` file:
+
[source,terminal]
----
$ oc -n openshift-monitoring get secret alertmanager-main --template='{{ index .data "alertmanager.yaml" }}' | base64 --decode > alertmanager.yaml
----

. Open the `alertmanager.yaml` file.

. Edit the Alertmanager configuration:

.. Optional: Change the default Alertmanager configuration:
+
.Example of the default Alertmanager secret YAML
[source,yaml]
----
global:
  resolve_timeout: 5m
  http_config:
    proxy_from_environment: true # <1>
route:
  group_wait: 30s # <2>
  group_interval: 5m # <3>
  repeat_interval: 12h # <4>
  receiver: default
  routes:
  - matchers:
    - "alertname=Watchdog"
    repeat_interval: 2m
    receiver: watchdog
receivers:
- name: default
- name: watchdog
----
<1> If you configured an HTTP cluster-wide proxy, set the `proxy_from_environment` parameter to `true` to enable proxying for all alert receivers.
<2> Specify how long Alertmanager waits while collecting initial alerts for a group of alerts before sending a notification.
<3> Specify how much time must elapse before Alertmanager sends a notification about new alerts added to a group of alerts for which an initial notification was already sent.
<4> Specify the minimum amount of time that must pass before an alert notification is repeated.
If you want a notification to repeat at each group interval, set the `repeat_interval` value to less than the `group_interval` value.
The repeated notification can still be delayed, for example, when certain Alertmanager pods are restarted or rescheduled.

.. Add your alert receiver configuration:
+
[source,yaml]
----
# ...
receivers:
- name: default
- name: watchdog
- name: <receiver> # <1>
  <receiver_configuration> # <2>
# ...
----
<1> The name of the receiver.
<2> The receiver configuration. The supported receivers are PagerDuty, webhook, email, Slack, and Microsoft Teams.
+
.Example of configuring PagerDuty as an alert receiver
[source,yaml]
----
# ...
receivers:
- name: default
- name: watchdog
- name: team-frontend-page
  pagerduty_configs:
  - routing_key: xxxxxxxxxx # <1>
    http_config: # <2>
      proxy_from_environment: true
      authorization:
        credentials: xxxxxxxxxx
# ...
----
<1> Defines the PagerDuty integration key.
<2> Optional: Add the custom HTTP configuration for a specific receiver. That receiver does not inherit the global HTTP configuration settings.
+
--
.Example of configuring email as an alert receiver
[source,yaml]
----
# ...
receivers:
- name: default
- name: watchdog
- name: team-frontend-page
  email_configs:
    - to: myemail@example.com # <1>
      from: alertmanager@example.com # <2>
      smarthost: 'smtp.example.com:587' # <3>
      auth_username: alertmanager@example.com  # <4>
      auth_password: password
      hello: alertmanager # <5>
# ...
----
<1> Specify an email address to send notifications to.
<2> Specify an email address to send notifications from.
<3> Specify the SMTP server address used for sending emails, including the port number.
<4> Specify the authentication credentials that Alertmanager uses to connect to the SMTP server. This example uses username and password.
<5> Specify the hostname to identify to the SMTP server. If you do not include this parameter, the hostname defaults to `localhost`.
--
+
[IMPORTANT]
====
Alertmanager requires an external SMTP server to send email alerts. To configure email alert receivers, ensure you have the necessary connection details for an external SMTP server.
====

.. Add the routing configuration:
+
[source,yaml]
----
# ...
route:
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 12h
  receiver: default
  routes:
  - matchers:
    - "alertname=Watchdog"
    repeat_interval: 2m
    receiver: watchdog
  - matchers: # <1>
    - "<your_matching_rules>" # <2>
    receiver: <receiver> # <3>
# ...
----
<1> Use the `matchers` key name to specify the matching rules that an alert has to fulfill to match the node.
If you define inhibition rules, use `target_matchers` key name for target matchers and `source_matchers` key name for source matchers.
<2> Specify labels to match your alerts.
<3> Specify the name of the receiver to use for the alerts.
+
[WARNING]
====
Do not use the `match`, `match_re`, `target_match`, `target_match_re`, `source_match`, and `source_match_re` key names, which are deprecated and planned for removal in a future release.
====
+
--
.Example of alert routing
[source,yaml]
----
# ...
route:
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 12h
  receiver: default
  routes:
  - matchers:
    - "alertname=Watchdog"
    repeat_interval: 2m
    receiver: watchdog
  - matchers: # <1>
    - "service=example-app"
    routes: # <2>
    - matchers:
      - "severity=critical"
      receiver: team-frontend-page
# ...
----
<1>  This example matches alerts from the `example-app` service.
<2> You can create routes within other routes for more complex alert routing.
--
+
The previous example routes alerts of `critical` severity that are fired by the `example-app` service to the `team-frontend-page` receiver. Typically, these types of alerts are paged to an individual or a critical response team.

. Apply the new configuration in the file:
+
[source,terminal]
----
$ oc -n openshift-monitoring create secret generic alertmanager-main --from-file=alertmanager.yaml --dry-run=client -o=yaml |  oc -n openshift-monitoring replace secret --filename=-
----

. Verify your routing configuration by visualizing the routing tree:
+
[source,terminal]
----
$ oc exec alertmanager-main-0 -n openshift-monitoring -- amtool config routes show --alertmanager.url http://localhost:9093
----
+
.Example output
[source,terminal]
----
Routing tree:
.
└── default-route  receiver: default
    ├── {alertname="Watchdog"}  receiver: Watchdog
    └── {service="example-app"}  receiver: default
        └── {severity="critical"}  receiver: team-frontend-page
----

[role="_additional-resources"]
.Additional resources

* Send test alerts to Alertmanager in OpenShift 4 (Red{nbsp}Hat Customer Portal)

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc
// * post_installation_configuration/configuring-alert-notifications.adoc

[id="configuring-alert-routing-console_{context}"]
= Configuring alert routing with the OpenShift Container Platform web console

You can configure alert routing through the OpenShift Container Platform web console to ensure that you learn about important issues with your cluster.

[NOTE]
====
The OpenShift Container Platform web console provides fewer settings to configure alert routing than the `alertmanager-main` secret. To configure alert routing with the access to more configuration settings, see "Configuring alert routing for default platform alerts".
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` cluster role.

.Procedure

. In the OpenShift Container Platform web console, go to *Administration* -> *Cluster Settings* -> *Configuration* -> *Alertmanager*.
+
[NOTE]
====
Alternatively, you can go to the same page through the notification drawer. Select the bell icon at the top right of the OpenShift Container Platform web console and choose *Configure* in the *AlertmanagerReceiverNotConfigured* alert.
====

. Click *Create Receiver* in the *Receivers* section of the page.

. In the *Create Receiver* form, add a *Receiver name* and choose a *Receiver type* from the list.

. Edit the receiver configuration:
+
* For PagerDuty receivers:
+
.. Choose an integration type and add a PagerDuty integration key.
+
.. Add the URL of your PagerDuty installation.
+
.. Click *Show advanced configuration* if you want to edit the client and incident details or the severity specification.
+
* For webhook receivers:
+
.. Add the endpoint to send HTTP POST requests to.
+
.. Click *Show advanced configuration* if you want to edit the default option to send resolved alerts to the receiver.
+
* For email receivers:
+
.. Add the email address to send notifications to.
+
.. Add SMTP configuration details, including the address to send notifications from, the smarthost and port number used for sending emails, the hostname of the SMTP server, and authentication details.
+
[IMPORTANT]
====
Alertmanager requires an external SMTP server to send email alerts. To configure email alert receivers, ensure you have the necessary connection details for an external SMTP server.
====
+
.. Select whether TLS is required.
+
.. Click *Show advanced configuration* if you want to edit the default option not to send resolved alerts to the receiver or edit the body of email notifications configuration.
+
* For Slack receivers:
+
.. Add the URL of the Slack webhook.
+
.. Add the Slack channel or user name to send notifications to.
+
.. Select *Show advanced configuration* if you want to edit the default option not to send resolved alerts to the receiver or edit the icon and username configuration. You can also choose whether to find and link channel names and usernames.

. By default, firing alerts with labels that match all of the selectors are sent to the receiver. If you want label values for firing alerts to be matched exactly before they are sent to the receiver, perform the following steps:
.. Add routing label names and values in the *Routing labels* section of the form.

.. Click *Add label* to add further routing labels.

. Click *Create* to create the receiver.

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
