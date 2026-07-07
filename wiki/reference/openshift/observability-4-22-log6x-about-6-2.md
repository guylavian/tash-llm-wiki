---
title: "Logging 6.2"
type: reference
domain: openshift
slug: observability-4-22-log6x-about-6-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log6x-about-6.2
version: 4.22
family: observability
documentKind: "Documentation"
---

# Logging 6.2

[id="log6x-about-6-2"]
= Logging 6.2

The `ClusterLogForwarder` custom resource (CR) is the central configuration point for log collection and forwarding.

[id="inputs-and-outputs_6-2_{context}"]
== Inputs and outputs

Inputs specify the sources of logs to be forwarded. Logging provides the following built-in input types that select logs from different parts of your cluster:

* `application`
* `receiver`
* `infrastructure`
* `audit`

You can also define custom inputs based on namespaces or pod labels to fine-tune log selection.

Outputs define the destinations where logs are sent. Each output type has its own set of configuration options, allowing you to customize the behavior and authentication settings.

[id="receiver-input-type_6-2_{context}"]
== Receiver input type
The receiver input type enables the Logging system to accept logs from external sources. It supports two formats for receiving logs: `http` and `syslog`.

The `ReceiverSpec` field defines the configuration for a receiver input.

[id="pipelines-and-filters_6-2_{context}"]
== Pipelines and filters

Pipelines determine the flow of logs from inputs to outputs. A pipeline consists of one or more input refs, output refs, and optional filter refs. You can use filters to transform or drop log messages within a pipeline. The order of filters matters, as they are applied sequentially, and earlier filters can prevent log messages from reaching later stages.

[id="operator-behavior_6-2_{context}"]
== Operator behavior

The Cluster Logging Operator manages the deployment and configuration of the collector based on the `managementState` field of the `ClusterLogForwarder` resource:

- When set to `Managed` (default), the Operator actively manages the logging resources to match the configuration defined in the spec.
- When set to `Unmanaged`, the Operator does not take any action, allowing you to manually manage the logging components.

[id="validation_6-2_{context}"]
== Validation
Logging includes extensive validation rules and default values to ensure a smooth and error-free configuration experience. The `ClusterLogForwarder` resource enforces validation checks on required fields, dependencies between fields, and the format of input values. Default values are provided for certain fields, reducing the need for explicit configuration in common scenarios.

[id="quick-start_6-2_{context}"]
== Quick start

OpenShift Logging supports two data models:

* ViaQ (General Availability)
* OpenTelemetry (Technology Preview)

You can select either of these data models based on your requirement by configuring the `lokiStack.dataModel` field in the `ClusterLogForwarder`. ViaQ is the default data model when forwarding logs to LokiStack.

[NOTE]
====
In future releases of OpenShift Logging, the default data model will change from ViaQ to OpenTelemetry.
====

// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-about.adoc

[id="quick-start-viaq_{context}"]
= Quick start with ViaQ

To use the default ViaQ data model, follow these steps:

.Prerequisites
* You have access to an OpenShift Container Platform cluster with `cluster-admin` permissions.
* You installed the {oc-first}.
* You have access to a supported object store. For example, AWS S3, {gcp-full} Storage, {azure-short}, Swift, Minio, or {rh-storage}.

.Procedure

. Install the `{clo}`, `{loki-op}`, and `{coo-first}` from the software catalog.

. Create a `LokiStack` custom resource (CR) in the `openshift-logging` namespace:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  managementState: Managed
  size: 1x.extra-small
  storage:
    schemas:
    - effectiveDate: '2024-10-01'
      version: v13
    secret:
      name: logging-loki-s3
      type: s3
  storageClassName: gp3-csi
  tenants:
    mode: openshift-logging
----
+
[NOTE]
====
Ensure that the `logging-loki-s3` secret is created beforehand. The contents of this secret vary depending on the object storage in use. For more information, see Secrets and TLS Configuration.
====

. Create a service account for the collector:
+
[source,terminal]
----
$ oc create sa collector -n openshift-logging
----

. Allow the collector's service account to write data to the `LokiStack` CR:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user logging-collector-logs-writer -z collector -n openshift-logging
----
+
[NOTE]
====
The `ClusterRole` resource is created automatically during the Cluster Logging Operator installation and does not need to be created manually.
====

. To collect logs, use the service account of the collector by running the following commands:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-application-logs -z collector -n openshift-logging
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-audit-logs -z collector -n openshift-logging
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-infrastructure-logs -z collector -n openshift-logging
----
+
[NOTE]
====
The example binds the collector to all three roles (application, infrastructure, and audit), but by default, only application and infrastructure logs are collected. To collect audit logs, update your `ClusterLogForwarder` configuration to include them. Assign roles based on the specific log types required for your environment.
====

. Create a `UIPlugin` CR to enable the *Log* section in the *Observe* tab:
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1alpha1
kind: UIPlugin
metadata:
  name: logging
spec:
  type: Logging
  logging:
    lokiStack:
      name: logging-loki
----

. Create a `ClusterLogForwarder` CR to configure log forwarding:
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: collector
  namespace: openshift-logging
spec:
  serviceAccount:
    name: collector
  outputs:
  - name: default-lokistack
    type: lokiStack
    lokiStack:
      authentication:
        token:
          from: serviceAccount
      target:
        name: logging-loki
        namespace: openshift-logging
    tls:
      ca:
        key: service-ca.crt
        configMapName: openshift-service-ca.crt
  pipelines:
  - name: default-logstore
    inputRefs:
    - application
    - infrastructure
    outputRefs:
    - default-lokistack
----
+
[NOTE]
====
The `dataModel` field is optional and left unset (`dataModel: ""`) by default. This allows the Cluster Logging Operator (CLO) to automatically select a data model. Currently, the CLO defaults to the ViaQ model when the field is unset, but this will change in future releases. Specifying `dataModel: ViaQ` ensures the configuration remains compatible if the default changes.
====

.Verification
* Verify that logs are visible in the *Log* section of the *Observe* tab in the OpenShift Container Platform web console.

// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-about.adoc

[id="quick-start-opentelemetry_{context}"]
= Quick start with OpenTelemetry

To configure OTLP ingestion and enable the OpenTelemetry data model, follow these steps:

.Prerequisites
* You have access to an OpenShift Container Platform cluster with `cluster-admin` permissions.
* You have installed the {oc-first}.
* You have access to a supported object store. For example, AWS S3, {gcp-full} Storage, {azure-short}, Swift, Minio, or {rh-storage}.

.Procedure

. Install the `{clo}`, `{loki-op}`, and `{coo-first}` from the software catalog.

. Create a `LokiStack` custom resource (CR) in the `openshift-logging` namespace:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  managementState: Managed
  size: 1x.extra-small
  storage:
    schemas:
    - effectiveDate: '2024-10-01'
      version: v13
    secret:
      name: logging-loki-s3
      type: s3
  storageClassName: gp3-csi
  tenants:
    mode: openshift-logging
----
+
[NOTE]
====
Ensure that the `logging-loki-s3` secret is created beforehand. The contents of this secret vary depending on the object storage in use. For more information, see "Secrets and TLS Configuration".
====

. Create a service account for the collector:
+
[source,terminal]
----
$ oc create sa collector -n openshift-logging
----

. Allow the collector's service account to write data to the `LokiStack` CR:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user logging-collector-logs-writer -z collector -n openshift-logging
----
+
[NOTE]
====
The `ClusterRole` resource is created automatically during the Cluster Logging Operator installation and does not need to be created manually.
====

. To collect logs, use the service account of the collector by running the following commands:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-application-logs -z collector -n openshift-logging
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-audit-logs -z collector -n openshift-logging
----
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-infrastructure-logs -z collector -n openshift-logging
----
+
[NOTE]
====
The example binds the collector to all three roles (application, infrastructure, and audit). By default, only application and infrastructure logs are collected. To collect audit logs, update your `ClusterLogForwarder` configuration to include them. Assign roles based on the specific log types required for your environment.
====

. Create a `UIPlugin` CR to enable the *Log* section in the *Observe* tab:
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1alpha1
kind: UIPlugin
metadata:
  name: logging
spec:
  type: Logging
  logging:
    lokiStack:
      name: logging-loki
----

. Create a `ClusterLogForwarder` CR to configure log forwarding:
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: collector
  namespace: openshift-logging
  annotations:
    observability.openshift.io/tech-preview-otlp-output: "enabled" # <1>
spec:
  serviceAccount:
    name: collector
  outputs:
  - name: loki-otlp
    type: lokiStack # <2>
    lokiStack:
      target:
        name: logging-loki
        namespace: openshift-logging
      dataModel: Otel # <3>
      authentication:
        token:
          from: serviceAccount
    tls:
      ca:
        key: service-ca.crt
        configMapName: openshift-service-ca.crt
  pipelines:
  - name: my-pipeline
    inputRefs:
    - application
    - infrastructure
    outputRefs:
    - loki-otlp
----
<1> Use the annotation to enable the `Otel` data model, which is a Technology Preview feature.
<2> Define the output type as `lokiStack`.
<3> Specifies the OpenTelemetry data model.
+
[NOTE]
====
You cannot use `lokiStack.labelKeys` when `dataModel` is `Otel`. To achieve similar functionality when `dataModel` is `Otel`, refer to "Configuring LokiStack for OTLP data ingestion".
====

.Verification
* To verify that OTLP is functioning correctly, complete the following steps:
.. In the OpenShift web console, click *Observe* -> *OpenShift Logging* -> *LokiStack* -> *Writes*.
.. Check the *Distributor - Structured Metadata* section.
