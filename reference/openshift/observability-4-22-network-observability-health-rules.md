---
title: "Network observability health rules"
type: reference
domain: openshift
slug: observability-4-22-network-observability-health-rules
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-health-rules
version: 4.22
family: observability
documentKind: "Documentation"
---

# Network observability health rules

[id="network-observability-health-rules"]
= Network observability health rules

[role="_abstract"]
The Network Observability Operator provides alerts by using built-in metrics and the OpenShift Container Platform monitoring stack to report cluster network health.

[IMPORTANT]
====
Network observability health alerts require OpenShift Container Platform 4.16 or later.
====

// Module included in the following assemblies:
//
// * network_observability/network-observability-health-rules.adoc

[id="network-observability-health-rules-and-performance_{context}"]
= Identifying network issues with automated health rules

[role="_abstract"]
Network observability identifies network issues by using automated health rules to monitor metrics. These rules trigger alerts when anomalies occur, which assists in maintaining connectivity and responding to network degradation.

The Network Observability Operator manages a system of Prometheus-based rules that detect network problems, and converts these rules into `PrometheusRule` resources. It supports the following rule types:

Alerting rules:: Trigger notifications through the Prometheus `Alertmanager` when network anomalies or infrastructure failures are detected.

Recording rules:: Pre-compute complex Prometheus Query Language (PromQL) expressions into new time series to improve dashboard performance.

[id="importance-of-network-health-monitoring_{context}"]
== Importance of network health monitoring

Maintaining reliable and secure network connectivity is critical for cluster administrators and security teams. Unresolved network issues can result in the following consequences:

* Application downtime caused by packet drops or DNS failures.
* Security risks from undetected network policy violations.
* Performance degradation caused by latency spikes or bandwidth saturation.
* Compliance issues from unmonitored network traffic.

Early detection of these issues allows for resolution before service level objectives (SLOs) are affected.

[id="detection-of-network-issues_{context}"]
== Automated health monitoring

The Network Observability Operator provides automated health monitoring through the following features:

* Pre-configured health rules: Detect common network problems by using default thresholds.
* Automated alerting: Integrates with the OpenShift Container Platform monitoring stack.
* Health dashboards: Displays health status for clusters, nodes, namespaces, and workloads.
* Custom rules: Supports the creation of organization-specific monitoring rules.

Health rules monitor network flow metrics and trigger alerts when defined thresholds are exceeded. For example, the `PacketDropsByKernel` rule reports an alert when kernel packet drop rates exceed defined levels.

[id="network-health-monitoring-workflow_{context}"]
== Network health monitoring workflow

Monitoring network health involves the following phases:

* Configuring the Network Observability Operator to collect required network health data for monitoring, such as packet drops or DNS tracking.
* Reviewing and customizing default health rules and thresholds in the `FlowCollector` custom resource.
* Monitoring alerts in the OpenShift Container Platform web console in the *Observe* → *Alerting* and *Observe* → *Network Health* views.
* Creating custom health rules for specific requirements.
* Configuring recording rules to optimize performance for large-scale deployments.

The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command:

[source,terminal]
----
$ oc get prometheusrules -n netobserv -o yaml
----

// Module included in the following assemblies:
//
// * network_observability/network-observability-health-rules.adoc

[id="network-observability-health-rules-monitoring-and-alerting_{context}"]
= Detecting network issues with automated health rules

[role="_abstract"]
The Network Observability Operator includes a rule-based system to detect network anomalies and infrastructure failures. By converting configurations into alerting rules, the Operator provides automated monitoring and troubleshooting through the OpenShift Container Platform web console.

[id="network-observability-health-outcomes_{context}"]
== Monitoring outcomes
The Network Observability Operator displays network status in the following views:

*Alerting* UI:: Specific alerts appear in *Observe* → *Alerting*. Notifications are managed through the Prometheus `Alertmanager`.
*Network Health* dashboard:: A specialized dashboard in *Observe* → *Network Health* provides a summary of cluster network status.

The *Network Health* dashboard categorizes violations into tabs to isolate the scope of an issue:

* *Global*: Aggregate health of the cluster.
* *Nodes*: Violations specific to infrastructure nodes.
* *Namespaces*: Violations specific to individual namespaces.
* *Workloads*: Violations specific to resources, such as `Deployments` or `DaemonSets`.

[id="network-observability-default-rules_{context}"]
== Predefined health rules
The Network Observability Operator provides default rules for common networking scenarios. These rules are active only if the corresponding feature is enabled in the `FlowCollector` custom resource (CR).

The following list contains a subset of available default rules:

`PacketDropsByDevice`:: Reports a high percentage of packet drops from network devices. This rule is based on node-exporter metrics and does not require the `PacketDrop` agent feature.
`PacketDropsByKernel`:: Reports a high percentage of packet drops by the kernel. This rule requires the `PacketDrop` agent feature.
`IPsecErrors`:: Reports IPsec encryption errors. This rule requires the `IPSec` agent feature.
`NetpolDenied`:: Reports traffic denied by network policies. This rule requires the `NetworkEvents` agent feature.
`LatencyHighTrend`:: Reports a significant increase in TCP latency. This rule requires the `FlowRTT` agent feature.
`DNSErrors`:: Reports DNS errors. This rule requires the `DNSTracking` agent feature.

The following operational alerts apply to the Network Observability Operator:

`NetObservNoFlows`:: Reports when the pipeline is active but no flows are observed.
`NetObservLokiError`:: Reports when flows are dropped because of Loki errors.

For a complete list of rules and runbooks, see the Network Observability Operator runbooks.

[id="network-observability-enabling-features-for-health-monitoring_{context}"]
== Enabling features for health monitoring
The Network Observability Operator creates rules based on the features enabled in the `FlowCollector` CR.

For example, packet drop rules are created only if the `PacketDrop` agent feature is enabled. Rules depend on metrics; if the required metrics are unavailable, configuration warnings might appear. Configure metrics in the `spec.processor.metrics.includeList` field of the `FlowCollector` resource.

// Module included in the following assemblies:
//
// network_observability/network-observability-alerts.adoc

[id="network-observability-health-rule-customization_{context}"]
= Health rule threshold and grouping customization

[role="_abstract"]
Health rules in the Network Observability Operator are defined by using rule templates and variants in the `spec.processor.metrics.healthRules` field of the `FlowCollector` custom resource (CR). Customizing these templates allows for flexible, fine-grained alerting tailored to specific environment needs.

For each template, a list of variants can be defined, each with distinct thresholds and grouping configurations.

The following example shows a `FlowCollector` configuration with custom health rules:

[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta1
kind: FlowCollector
metadata:
  name: flow-collector
spec:
  processor:
    metrics:
      healthRules:
      - template: PacketDropsByKernel
        mode: Alert # or Recording
        variants:
        # Triggered when aggregate cluster traffic reaches 10% drops
        - thresholds:
            critical: "10"
        # Triggered per-node with increasing severity levels
        - thresholds:
            critical: "15"
            warning: "10"
            info: "5"
          groupBy: Node
----

`spec.processor.metrics.healthRules.template`:: Specifies the name of the predefined rule template.
`spec.processor.metrics.healthRules.mode`:: Specifies whether the rule functions as an `Alert` or a `Recording` rule.
`spec.processor.metrics.healthRules.variants.thresholds`:: Specifies the numerical values that trigger the rule. Multiple severity levels, such as `critical`, `warning`, or `info`, can be defined within a single variant.
`spec.processor.metrics.healthRules.variants.groupBy`:: Specifies the dimension used to aggregate the metric, such as `Node` or `Namespace`.

[NOTE]
====
Customizing a rule replaces the default configuration for that template. To retain default configurations, the default settings must be manually included in the custom resource.
====

// Module included in the following assemblies:
//
// * network_observability/network-observability-alerts.adoc

[id="network-observability-health-rules-promql-expressions-metadata_{context}"]
= Health rule query and metadata reference

[role="_abstract"]
The `FlowCollector` health rule API maps to the Prometheus Operator to generate `PrometheusRule` objects. Use these base Prometheus Query Language (PromQL) patterns and metadata configurations to create custom health rules for network observability.

The `PrometheusRule` resource in the `netobserv` namespace can be viewed by running the following command:

[source,terminal]
----
$ oc get prometheusrules -n netobserv -o yaml
----

[id="example-query-surge-incoming-traffic_{context}"]
== Customizing alert logic with PromQL: Incoming traffic surge

The following PromQL query calculates the byte rate from the `openshift-ingress` namespace to any workload namespace over a 30-minute interval:

[source,promql]
----
sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace)
----

Queries can be customized to filter low-bandwidth data, compare time periods, and establish thresholds.

Data filtering:: Appending `> 1000` to the query removes rates lower than `1 KB/s` to filter low-bandwidth traffic.
+
`(sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)`
+
[NOTE]
====
The byte rate is relative to the sampling interval in the `FlowCollector` CR. Normalizing byte rates with the `netobserv_agent_sampling_rate` metric decouples the PromQL expression from the sampling configuration.
====

Time comparison:: The `offset` modifier compares data across different time periods. For example, `offset 1d` retrieves data from the previous day.
+
`sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace))`

Threshold application:: A final threshold filters increases below a specific percentage. For example, `> 100` removes increases lower than 100%.

The following example shows a complete PromQL expression for a `PrometheusRule`:

[source,promql]
----
expr: |-
  (100 *
    (
      (sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m])) by (DstK8S_Namespace) > 1000)
      - sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace)
    )
    / sum(rate(netobserv_workload_ingress_bytes_total{SrcK8S_Namespace="openshift-ingress"}[30m] offset 1d)) by (DstK8S_Namespace))
  > 100
----

[id="alert-metadata-fields_{context}"]
== Alert metadata fields

Rule definitions require specific metadata for the Prometheus `Alertmanager` service and the *Network Health* dashboard. The following example shows an `AlertingRule` resource with configured metadata:

[source,yaml]
----
apiVersion: monitoring.openshift.io/v1
kind: AlertingRule
metadata:
  name: netobserv-alerts
  namespace: openshift-monitoring
spec:
  groups:
  - name: NetObservAlerts
    rules:
    - alert: NetObservIncomingBandwidth
      annotations:
        netobserv_io_network_health: '{"namespaceLabels":["DstK8S_Namespace"],"threshold":"100","unit":"%","upperBound":"500"}'
        message: |-
          Surge of incoming traffic detected: current traffic to {{ $labels.DstK8S_Namespace }} increased by more than 100% since yesterday.
        summary: "Surge in incoming traffic"
      expr: |-
        # ... (PromQL expression)
      for: 1m
      labels:
        app: netobserv
        netobserv: "true"
        severity: warning
----

`spec.groups.rules.alert.labels.netobserv`::
Specifies that the *Network Health* dashboard must detect the alert when set to `true`.
`spec.groups.rules.alert.labels.severity`::
Specifies the alert severity. Valid values are `critical`, `warning`, or `info`.

[id="netobserv-io-network-health-annotation_{context}"]
== netobserv_io_network_health annotation fields

The optional `netobserv_io_network_health` annotation is a JSON string that controls how the alert renders on the *Network Health* page.

.Fields for the `netobserv_io_network_health` annotation
[cols="2,2,6",options="header"]
|===
| Field
| Type
| Description

| `namespaceLabels`
| List of strings
| One or more labels containing namespaces. Alerts appear under the *Namespaces* tab.

| `nodeLabels`
| List of strings
| One or more labels containing node names. Alerts appear under the *Nodes* tab.

| `workloadLabels`
| List of strings
| One or more labels containing owner or workload names. Alerts appear under the *Owners* tab when `kindLabels` is also provided.

| `threshold`
| String
| The alert threshold. This value should match the threshold in the PromQL expression.

| `unit`
| String
| The data unit for display purposes.

| `upperBound`
| String
| An upper bound value used to calculate scores on a closed scale. Metric values exceeding this bound are clamped.
|===

[NOTE]
====
The `namespaceLabels` and `nodeLabels` fields are mutually exclusive. If neither is provided, the alert appears under the *Global* tab.
====

// Module included in the following assemblies:
//
// * network_observability/network-observability-alerts.adoc

[id="network-observability-configuring-custom-health-rules_{context}"]
= Configuring custom health rules

[role="_abstract"]
Create custom health rules by using Prometheus Query Language (PromQL) to define an `AlertingRule` resource. These rules trigger alerts based on specific network metrics, such as traffic surges.

.Prerequisites

* Access to the cluster with `cluster-admin` privileges.
* The Network Observability Operator is installed.
* OpenShift Container Platform 4.16 or later is installed.
* Familiarity with PromQL.

[IMPORTANT]
====
Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control.
====

.Procedure

. Define an `AlertingRule` resource in a YAML file, for example, `custom-alert.yaml`.
. Apply the custom alert rule by running the following command:
+
[source,terminal]
----
$ oc apply -f custom-alert.yaml
----

.Verification

. Confirm the `PrometheusRule` resource was created in the target namespace by running the following command:
+
[source,terminal]
----
$ oc get prometheusrules -n <namespace> -o yaml
----

. Confirm the rule is active in the OpenShift Container Platform web console:
.. Navigate to *Observe* → *Alerting* to see the firing status.
.. Navigate to *Observe* → *Network Health* to view the dashboard integration.

// Module included in the following assemblies:
//
// * network_observability/network-observability-health-rules.adoc

[id="network-observability-recording-rules-performance-optimization_{context}"]
= Performance optimization with recording rules

[role="_abstract"]
In large-scale clusters, recording rules optimize how Prometheus handles network data. Recording rules improve dashboard responsiveness and reduce the computational overhead of complex queries.

[id="network-observability-recording-rules-benefits_{context}"]
== Optimization benefits
Recording rules pre-compute complex Prometheus Query Language (PromQL) expressions and save the results as new time series. Unlike alerting rules, recording rules do not monitor thresholds.

Using recording rules provides the following advantages:

Improved performance:: Pre-computing Prometheus queries allows dashboards to load faster by avoiding on-demand calculations for long-term trends.
Resource efficiency:: Calculating data at fixed intervals reduces CPU load on the Prometheus server compared to recalculating data on every dashboard refresh.
Simplified queries:: Using short metric names, such as `cluster:network_traffic:rate_5m`, simplifies complex aggregate calculations in custom dashboards.

[id="network-observability-alert-vs-recording-comparison_{context}"]
== Comparison of rule modes
The following table compares rule modes based on the expected outcome:

[cols="1,2,2",options="header"]
|===
| Feature
| Alerting rules
| Recording rules

| Primary goal
| Issue notification.
| Persistent metric history.

| Data output
| Alerting state.
| New time series metric.

| UI visibility
| *Alerting* and *Network Health* views.
| *Metrics Explorer* and *Network Health* views.

| Notifications
| Triggers `Alertmanager` notifications.
| Does not trigger notifications.
|===

[id="network-observability-integrating-recording-rules-with-health-dashboard_{context}"]
== Integrating recording rules with the health dashboard

Custom recording rules that contribute to the *Network Health* dashboard must meet specific metadata requirements.

Label requirements::
Include the `netobserv: "true"` label in the `labels` field of the rule and the `PrometheusRule` metadata. The Network Observability Operator identifies `PrometheusRule` resources cluster-wide by using this label.

Annotation requirements::
Include the `netobserv.io/network-health` annotation in the `PrometheusRule` metadata. This annotation is required for recording rules to appear in the *Network Health* dashboard. The value is a JSON object where keys are the metric names (the `record` field of each rule). Each value consists of the following fields:
+
* `summary`: An optional short title. This field supports Prometheus template syntax, such as `{{ $labels.namespace }}`.
* `description`: An optional description. This field supports Prometheus template syntax.
* `netobserv_io_network_health`: A required JSON string. For recording rules, use the `recordingThresholds` field instead of `threshold`. This field determines the health score and UI coloring, such as `{"info":"10","warning":"25","critical":"50"}`.

// Module included in the following assemblies:
//
// * network_observability/network-observability-health-rules.adoc

[id="network-observability-configuring-custom-recording-rules_{context}"]
= Optimizing dashboard metrics with recording rules

[role="_abstract"]
Create custom recording rules to pre-compute metrics for the *Network Health* dashboard. Recording rules require specific annotations and labels to integrate with the Network Observability Operator.

.Prerequisites

* Access to the cluster with `cluster-admin` privileges.
* The Network Observability Operator is installed.
* OpenShift Container Platform 4.16 or later is installed.
* Familiarity with PromQL.

[IMPORTANT]
====
Custom `PrometheusRule` resources are not owned by the `FlowCollector` resource. Custom rules created in the `netobserv` namespace might be deleted if the Network Observability Operator is uninstalled. To prevent data loss, create custom rules in a different namespace, such as `openshift-monitoring`, and maintain a backup in version control.
====

.Procedure

. Define a `PrometheusRule` resource in a YAML file, such as `custom-recording-rule.yaml`, ensuring the `netobserv: "true"` label and `netobserv.io/network-health` annotation are included:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: my-recording-rules
  namespace: openshift-monitoring
  labels:
    netobserv: "true"
  annotations:
    netobserv.io/network-health: |
      {
        "my_metric_per_namespace": {
          "summary": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
          "description": "Custom metric is {{ $value }} in the namespace {{ $labels.namespace }}",
          "netobserv_io_network_health": "{\"unit\":\"%\",\"upperBound\":\"100\",\"namespaceLabels\":[\"namespace\"],\"recordingThresholds\":{\"info\":\"10\",\"warning\":\"25\",\"critical\":\"50\"}}"
        }
      }
spec:
  groups:
    - name: MyRecordingRules
      interval: 30s
      rules:
        - record: my_metric_per_namespace
          expr: (count by (namespace) (kube_pod_info) * 0 + 20)
          labels:
            netobserv: "true"
----

. Apply the custom recording rule by running the following command:
+
[source,terminal]
----
$ oc apply -f custom-recording-rule.yaml
----

.Verification

. Confirm the `PrometheusRule` resource exists by running the following command:
+
[source,terminal]
----
$ oc get prometheusrules my-recording-rules -n openshift-monitoring -o yaml
----

. Confirm the recording rule appears in the OpenShift Container Platform web console by navigating to *Observe* → *Network Health*.

// Module included in the following assemblies:
//
// * network_observability/network-observability-alerts.adoc

[id="network-observability-disable-predefined-rules_{context}"]
= Disabling default rules

[role="_abstract"]
Rule templates can be disabled in the `spec.processor.metrics.disableAlerts` field of the `FlowCollector` custom resource (CR). This setting accepts a list of rule template names. For a list of alert template names, see "List of default rules".

If a rule template is included in the `disableAlerts` list, it is not created, even if a custom override exists in the `spec.processor.metrics.healthRules` field. The `disableAlerts` configuration takes precedence over all other health rule settings.

For a list of alert template names, see "List of default rules".

[role="_additional-resources"]
== Additional resources
* List of default rules
* Viewing network observability metrics dashboards
* Creating alerts
* Monitoring stack architecture
* Network Observability Operator runbooks

//file name for Creating alerts: network-observability-includelist-example.adoc
//URL for Creating alerts: https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/network_observability/metrics-dashboards-alerts#network-observability-netobserv-dashboard-high-traffic-alert_metrics-dashboards-alerts
