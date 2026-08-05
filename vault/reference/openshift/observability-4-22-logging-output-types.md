---
title: "Log output types"
type: reference
domain: openshift
slug: observability-4-22-logging-output-types
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-output-types
version: 4.22
family: observability
documentKind: "Documentation"
---

# Log output types

[id="logging-output-types"]
= Log output types

Outputs define the destination where logs are sent to from a log forwarder. You can configure multiple types of outputs in the `ClusterLogForwarder` custom resource (CR) to send logs to servers that support different protocols.

// Module included in the following assemblies:
//
// * observability/logging/log_collection_forwarding/logging-output-types.adoc

[id="supported-log-outputs_{context}"]
= Supported log forwarding outputs

Outputs can be any of the following types:

.Supported log output types
[cols="5",options="header"]
|===
|Output type
|Protocol
|Tested with
|Logging versions
|Supported collector type

|Elasticsearch v6
|HTTP 1.1
|6.8.1, 6.8.23
|5.6+
|Fluentd, Vector

|Elasticsearch v7
|HTTP 1.1
|7.12.2, 7.17.7, 7.10.1
|5.6+
|Fluentd, Vector

|Elasticsearch v8
|HTTP 1.1
|8.4.3, 8.6.1
|5.6+
|Fluentd ^[1]^, Vector

|Fluent Forward
|Fluentd forward v1
|Fluentd 1.14.6, Logstash 7.10.1, Fluentd 1.14.5
|5.4+
|Fluentd

|{gcp-full} Logging
|REST over HTTPS
|Latest
|5.7+
|Vector

|HTTP
|HTTP 1.1
|Fluentd 1.14.6, Vector 0.21
|5.7+
|Fluentd, Vector

|Kafka
|Kafka 0.11
|Kafka 2.4.1, 2.7.0, 3.3.1
|5.4+
|Fluentd, Vector

|Loki
|REST over HTTP and HTTPS
|2.3.0, 2.5.0, 2.7, 2.2.1
|5.4+
|Fluentd, Vector

|Splunk
|HEC
|8.2.9, 9.0.0
|5.7+
|Vector

|Syslog
|RFC3164, RFC5424
|Rsyslog 8.37.0-9.el7, rsyslog-8.39.0
|5.4+
|Fluentd, Vector ^[2]^

|Amazon CloudWatch
|REST over HTTPS
|Latest
|5.4+
|Fluentd, Vector
|===
[.small]
--
1. Fluentd does not support Elasticsearch 8 in the {logging} version 5.6.2.
2. Vector supports Syslog in the {logging} version 5.7 and higher.
--

[id="logging-output-types-descriptions"]
== Output type descriptions

`default`:: The on-cluster, Red{nbsp}Hat managed log store. You are not required to configure the default output.
+
[NOTE]
====
If you configure a `default` output, you receive an error message, because the `default` output name is reserved for referencing the on-cluster, Red{nbsp}Hat managed log store.
====
`loki`:: Loki, a horizontally scalable, highly available, multi-tenant log aggregation system.
`kafka`:: A Kafka broker. The `kafka` output can use a TCP or TLS connection.
`elasticsearch`:: An external Elasticsearch instance. The `elasticsearch` output can use a TLS connection.
`fluentdForward`:: An external log aggregation solution that supports Fluentd. This option uses the Fluentd `forward` protocols. The `fluentForward` output can use a TCP or TLS connection and supports shared-key authentication by providing a `shared_key` field in a secret. Shared-key authentication can be used with or without TLS.
+
[IMPORTANT]
====
The `fluentdForward` output is only supported if you are using the Fluentd collector. It is not supported if you are using the Vector collector. If you are using the Vector collector, you can forward logs to Fluentd by using the `http` output.
====
`syslog`:: An external log aggregation solution that supports the syslog RFC3164 or RFC5424 protocols. The `syslog` output can use a UDP, TCP, or TLS connection.
`cloudwatch`:: Amazon CloudWatch, a monitoring and log storage service hosted by Amazon Web Services (AWS).
`cloudlogging`:: {gcp-full} Logging, a monitoring and log storage service hosted by {gcp-first}.
