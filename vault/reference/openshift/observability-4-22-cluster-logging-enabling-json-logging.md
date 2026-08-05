---
title: "Enabling JSON log forwarding"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-enabling-json-logging
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-enabling-json-logging
version: 4.22
family: observability
documentKind: "Documentation"
---

# Enabling JSON log forwarding

[id="cluster-logging-enabling-json-logging"]
= Enabling JSON log forwarding

You can configure the Log Forwarding API to parse JSON strings into a structured object.

[id="cluster-logging-json-log-forwarding_{context}"]
= Parsing JSON logs

You can use a `ClusterLogForwarder` object to parse JSON logs into a structured object and forward them to a supported output.

To illustrate how this works, suppose that you have the following structured JSON log entry:

.Example structured JSON log entry
[source,yaml]
----
{"level":"info","name":"fred","home":"bedrock"}
----

To enable parsing JSON log, you add `parse: json` to a pipeline in the `ClusterLogForwarder` CR, as shown in the following example:

.Example snippet showing `parse: json`
[source,yaml]
----
pipelines:
- inputRefs: [ application ]
  outputRefs: myFluentd
  parse: json
----

When you enable parsing JSON logs by using `parse: json`, the CR copies the JSON-structured log entry in a `structured` field, as shown in the following example:

.Example `structured` output containing the structured JSON log entry
[source,yaml]
----
{"structured": { "level": "info", "name": "fred", "home": "bedrock" },
 "more fields..."}
----

[IMPORTANT]
====
If the log entry does not contain valid structured JSON, the `structured` field is absent.
====
[id="cluster-logging-configuration-of-json-log-data-for-default-elasticsearch_{context}"]
= Configuring JSON log data for Elasticsearch

If your JSON logs follow more than one schema, storing them in a single index might cause type conflicts and cardinality problems. To avoid that, you must configure the `ClusterLogForwarder` custom resource (CR) to group each schema into a single output definition. This way, each schema is forwarded to a separate index.

[IMPORTANT]
====
If you forward JSON logs to the default Elasticsearch instance managed by OpenShift Logging, it generates new indices based on your configuration. To avoid performance issues associated with having too many indices, consider keeping the number of possible schemas low by standardizing to common schemas.
====

.Structure types

You can use the following structure types in the `ClusterLogForwarder` CR to construct index names for the Elasticsearch log store:

* `structuredTypeKey` is the name of a message field. The value of that field is used to construct the index name.
** `kubernetes.labels.<key>` is the Kubernetes pod label whose value is used to construct the index name.
** `openshift.labels.<key>` is the `pipeline.label.<key>` element in the `ClusterLogForwarder` CR whose value is used to construct the index name.
** `kubernetes.container_name` uses the container name to construct the index name.
* `structuredTypeName`: If the `structuredTypeKey` field is not set or its key is not present, the `structuredTypeName` value is used as the structured type. When you use both the `structuredTypeKey` field and the `structuredTypeName` field together, the `structuredTypeName` value provides a fallback index name if the key in the `structuredTypeKey` field is missing from the JSON log data.

[NOTE]
====
Although you can set the value of `structuredTypeKey` to any field shown in the "Log Record Fields" topic, the most useful fields are shown in the preceding list of structure types.
====

.A structuredTypeKey: kubernetes.labels.<key> example

Suppose the following:

* Your cluster is running application pods that produce JSON logs in two different formats, "apache" and "google".
* The user labels these application pods with `logFormat=apache` and `logFormat=google`.
* You use the following snippet in your `ClusterLogForwarder` CR YAML file.

[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
# ...
  outputDefaults:
    elasticsearch:
      structuredTypeKey: kubernetes.labels.logFormat <1>
      structuredTypeName: nologformat
  pipelines:
  - inputRefs:
    - application
    outputRefs:
    - default
    parse: json <2>
----
<1> Uses the value of the key-value pair that is formed by the Kubernetes `logFormat` label.
<2> Enables parsing JSON logs.

In that case, the following structured log record goes to the `app-apache-write` index:

[source]
----
{
  "structured":{"name":"fred","home":"bedrock"},
  "kubernetes":{"labels":{"logFormat": "apache", ...}}
}
----

And the following structured log record goes to the `app-google-write` index:

[source]
----
{
  "structured":{"name":"wilma","home":"bedrock"},
  "kubernetes":{"labels":{"logFormat": "google", ...}}
}
----

.A structuredTypeKey: openshift.labels.<key> example

Suppose that you use the following snippet in your `ClusterLogForwarder` CR YAML file.

[source,yaml]
----
outputDefaults:
 elasticsearch:
    structuredTypeKey: openshift.labels.myLabel <1>
    structuredTypeName: nologformat
pipelines:
 - name: application-logs
   inputRefs:
   - application
   - audit
   outputRefs:
   - elasticsearch-secure
   - default
   parse: json
   labels:
     myLabel: myValue <2>
----
<1> Uses the value of the key-value pair that is formed by the OpenShift `myLabel` label.
<2> The `myLabel` element gives its string value, `myValue`, to the structured log record.

In that case, the following structured log record goes to the `app-myValue-write` index:

[source]
----
{
  "structured":{"name":"fred","home":"bedrock"},
  "openshift":{"labels":{"myLabel": "myValue", ...}}
}
----

.Additional considerations

* The Elasticsearch _index_ for structured records is formed by prepending "app-" to the structured type and appending "-write".
* Unstructured records are not sent to the structured index. They are indexed as usual in the application, infrastructure, or audit indices.
* If there is no non-empty structured type, forward an _unstructured_ record with no `structured` field.

It is important not to overload Elasticsearch with too many indices. Only use distinct structured types for distinct log _formats_, *not* for each application or namespace. For example, most Apache applications use the same JSON log format and structured type, such as `LogApache`.
[id="cluster-logging-forwarding-json-logs-to-the-default-elasticsearch_{context}"]
= Forwarding JSON logs to the Elasticsearch log store

For an Elasticsearch log store, if your JSON log entries _follow different schemas_, configure the `ClusterLogForwarder` custom resource (CR) to group each JSON schema into a single output definition. This way, Elasticsearch uses a separate index for each schema.

[IMPORTANT]
====
Because forwarding different schemas to the same index can cause type conflicts and cardinality problems, you must perform this configuration before you forward data to the Elasticsearch store.

To avoid performance issues associated with having too many indices, consider keeping the number of possible schemas low by standardizing to common schemas.
====

.Procedure

. Add the following snippet to your `ClusterLogForwarder` CR YAML file.
+
[source,yaml]
----
outputDefaults:
 elasticsearch:
    structuredTypeKey: <log record field>
    structuredTypeName: <name>
pipelines:
- inputRefs:
  - application
  outputRefs: default
  parse: json
----

. Use `structuredTypeKey` field to specify one of the log record fields.

. Use `structuredTypeName` field to specify a name.
+
[IMPORTANT]
====
To parse JSON logs, you must set both the `structuredTypeKey` and `structuredTypeName` fields.
====

. For `inputRefs`, specify which log types to forward by using that pipeline, such as `application,` `infrastructure`, or `audit`.

. Add the `parse: json` element to pipelines.

. Create the CR object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----
+
The Red Hat OpenShift Logging Operator redeploys the collector pods. However, if they do not redeploy, delete the collector pods to force them to redeploy.
+
[source,terminal]
----
$ oc delete pod --selector logging-infra=collector
----
// Module is included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/log-forwarding

[id="cluster-logging-forwarding-separate-indices_{context}"]
= Forwarding JSON logs from containers in the same pod to separate indices

You can forward structured logs from different containers within the same pod to different indices. To use this feature, you must configure the pipeline with multi-container support and annotate the pods. Logs are written to indices with a prefix of `app-`. It is recommended that Elasticsearch be configured with aliases to accommodate this.

[IMPORTANT]
====
JSON formatting of logs varies by application. Because creating too many indices impacts performance, limit your use of this feature to creating indices for logs that have incompatible JSON formats. Use queries to separate logs from different namespaces, or applications with compatible JSON formats.
====

.Prerequisites

* {logging-title-uc}: 5.5

.Procedure
. Create or edit a YAML file that defines the `ClusterLogForwarder` CR object:
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  outputDefaults:
    elasticsearch:
      structuredTypeKey: kubernetes.labels.logFormat <1>
      structuredTypeName: nologformat
      enableStructuredContainerLogs: true <2>
  pipelines:
  - inputRefs:
    - application
    name: application-logs
    outputRefs:
    - default
    parse: json
----
<1> Uses the value of the key-value pair that is formed by the Kubernetes `logFormat` label.
<2> Enables multi-container outputs.

. Create or edit a YAML file that defines the `Pod` CR object:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    containerType.logging.openshift.io/heavy: heavy <1>
    containerType.logging.openshift.io/low: low
spec:
  containers:
  - name: heavy <2>
    image: heavyimage
  - name: low
    image: lowimage
----
<1> Format: `containerType.logging.openshift.io/<container-name>: <index>`
<2> Annotation names must match container names

[WARNING]
====
This configuration might significantly increase the number of shards on the cluster.
====

.Additional resources
* Kubernetes Annotations

[role="_additional-resources"]
.Additional resources

* About log forwarding
