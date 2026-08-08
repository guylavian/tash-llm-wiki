---
title: "Log Record Fields"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-exported-fields
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-exported-fields
version: 4.22
family: observability
documentKind: "Documentation"
---

# Log Record Fields

[id="cluster-logging-exported-fields"]
= Log Record Fields

The following fields can be present in log records exported by the {logging}. Although log records are typically formatted as JSON objects, the same data model can be applied to other encodings.

To search these fields from Elasticsearch and Kibana, use the full dotted field name when searching. For example, with an Elasticsearch */_search URL*, to look for a Kubernetes pod name, use `/_search/q=kubernetes.pod_name:name-of-my-pod`.

// The logging system can parse JSON-formatted log entries to external systems. These log entries are formatted as a fluentd message with extra fields such as `kubernetes`. The fields exported by the logging system and available for searching from Elasticsearch and Kibana are documented at the end of this document.

[id="cluster-logging-exported-fields-top-level-fields_{context}"]

// Normally, the following title would be an H1 prefixed with an `=`. However, because the following content is auto-generated at https://github.com/ViaQ/documentation/blob/main/src/data_model/public/top-level.part.adoc and pasted here, it is more efficient to use it as-is with no modifications. Therefore, to "realign" the content, I am going to prefix the title with `==` and use `include::modules/cluster-logging-exported-fields-top-level-fields.adoc[leveloffset=0]` in the assembly file.

// DO NOT MODIFY THE FOLLOWING CONTENT. Instead, update https://github.com/ViaQ/documentation/blob/main/src/data_model/model/top-level.yaml and run `make` as instructed here: https://github.com/ViaQ/documentation

//The top-level fields can be present in every record. The descriptions for fields that are optional begin with "Optional:"

The top level fields may be present in every record.

[discrete]
== message

The original log entry text, UTF-8 encoded. This field may be absent or empty if a non-empty `structured` field is present. See the description of `structured` for more.

[horizontal]
Data type:: text
Example value:: `HAPPY`

[discrete]
== structured

Original log entry as a structured object. This field may be present if the forwarder was configured to parse structured JSON logs. If the original log entry was a valid structured log, this field will contain an equivalent JSON structure. Otherwise this field will be empty or absent, and the `message` field will contain the original log message. The `structured` field can have any subfields that are included in the log message, there are no restrictions defined here.

[horizontal]
Data type:: group
Example value:: map[message:starting fluentd worker pid=21631 ppid=21618 worker=0 pid:21631 ppid:21618 worker:0]

[discrete]
== @timestamp

A UTC value that marks when the log payload was created or, if the creation time is not known, when the log payload was first collected. The “@” prefix denotes a field that is reserved for a particular use. By default, most tools look for “@timestamp” with ElasticSearch.

[horizontal]
Data type:: date
Example value:: `2015-01-24 14:06:05.071000000 Z`

[discrete]
== hostname

The name of the host where this log message originated. In a Kubernetes cluster, this is the same as `kubernetes.host`.

[horizontal]
Data type:: keyword

[discrete]
== ipaddr4

The IPv4 address of the source server. Can be an array.

[horizontal]
Data type:: ip

[discrete]
== ipaddr6

The IPv6 address of the source server, if available. Can be an array.

[horizontal]
Data type:: ip

[discrete]
== level

The logging level from various sources, including `rsyslog(severitytext property)`, a Python logging module, and others.

The following values come from `syslog.h`, and are preceded by their http://sourceware.org/git/?p=glibc.git;a=blob;f=misc/sys/syslog.h;h=ee01478c4b19a954426a96448577c5a76e6647c0;hb=HEAD#l51[numeric equivalents]:

* `0` = `emerg`, system is unusable.
* `1` = `alert`, action must be taken immediately.
* `2` = `crit`, critical conditions.
* `3` = `err`, error conditions.
* `4` = `warn`, warning conditions.
* `5` = `notice`, normal but significant condition.
* `6` = `info`, informational.
* `7` = `debug`, debug-level messages.

The two following values are not part of `syslog.h` but are widely used:

* `8` = `trace`, trace-level messages, which are more verbose than `debug` messages.
* `9` = `unknown`, when the logging system gets a value it does not recognize.

Map the log levels or priorities of other logging systems to their nearest match in the preceding list. For example, from python logging, you can match `CRITICAL` with `crit`, `ERROR` with `err`, and so on.

[horizontal]
Data type:: keyword
Example value:: `info`

[discrete]
== pid

The process ID of the logging entity, if available.

[horizontal]
Data type:: keyword

[discrete]
== service

The name of the service associated with the logging entity, if available. For example, syslog's `APP-NAME` and rsyslog's `programname` properties are mapped to the service field.

[horizontal]
Data type:: keyword

== tags

Optional. An operator-defined list of tags placed on each log by the collector or normalizer. The payload can be a string with whitespace-delimited string tokens or a JSON list of string tokens.

[horizontal]
Data type:: text

[discrete]
== file

The path to the log file from which the collector reads this log entry. Normally, this is a path in the `/var/log` file system of a cluster node.

[horizontal]
Data type:: text

[discrete]
== offset

The offset value. Can represent bytes to the start of the log line in the file (zero- or one-based), or log line numbers (zero- or one-based), so long as the values are strictly monotonically increasing in the context of a single log file. The values are allowed to wrap, representing a new version of the log file (rotation).

[horizontal]
Data type:: long

[id="cluster-logging-exported-fields-kubernetes_{context}"]

// Normally, the following title would be an H1 prefixed with an `=`. However, because the following content is auto-generated at https://github.com/ViaQ/documentation/blob/main/src/data_model/public/kubernetes.part.adoc and pasted here, it is more efficient to use it as-is with no modifications. Therefore, to "realign" the content, I am going to prefix the title with `==` and use `include::modules/cluster-logging-exported-fields-kubernetes.adoc[leveloffset=0]` in the assembly file.

// DO NOT MODIFY THE FOLLOWING CONTENT. Instead, update https://github.com/ViaQ/documentation/blob/main/src/data_model/model/kubernetes.yaml and run `make` as instructed here: https://github.com/ViaQ/documentation

== kubernetes

The namespace for Kubernetes-specific metadata

[horizontal]
Data type:: group

=== kubernetes.pod_name

The name of the pod

[horizontal]
Data type:: keyword

=== kubernetes.pod_id

The Kubernetes ID of the pod

[horizontal]
Data type:: keyword

=== kubernetes.namespace_name

The name of the namespace in Kubernetes

[horizontal]
Data type:: keyword

=== kubernetes.namespace_id

The ID of the namespace in Kubernetes

[horizontal]
Data type:: keyword

=== kubernetes.host

The Kubernetes node name

[horizontal]
Data type:: keyword

=== kubernetes.container_name

The name of the container in Kubernetes

[horizontal]
Data type:: keyword

=== kubernetes.annotations

Annotations associated with the Kubernetes object

[horizontal]
Data type:: group

=== kubernetes.labels

Labels present on the original Kubernetes Pod

[horizontal]
Data type:: group

=== kubernetes.event

The Kubernetes event obtained from the Kubernetes master API. This event description loosely follows `type Event` in Event v1 core.

[horizontal]
Data type:: group

==== kubernetes.event.verb

The type of event, `ADDED`, `MODIFIED`, or `DELETED`

[horizontal]
Data type:: keyword
Example value:: `ADDED`

==== kubernetes.event.metadata

Information related to the location and time of the event creation

[horizontal]
Data type:: group

===== kubernetes.event.metadata.name

The name of the object that triggered the event creation

[horizontal]
Data type:: keyword
Example value:: `java-mainclass-1.14d888a4cfc24890`

===== kubernetes.event.metadata.namespace

The name of the namespace where the event originally occurred. Note that it differs from `kubernetes.namespace_name`, which is the namespace where the `eventrouter` application is deployed.

[horizontal]
Data type:: keyword
Example value:: `default`

===== kubernetes.event.metadata.selfLink

A link to the event

[horizontal]
Data type:: keyword
Example value:: `/api/v1/namespaces/javaj/events/java-mainclass-1.14d888a4cfc24890`

===== kubernetes.event.metadata.uid

The unique ID of the event

[horizontal]
Data type:: keyword
Example value:: `d828ac69-7b58-11e7-9cf5-5254002f560c`

===== kubernetes.event.metadata.resourceVersion

A string that identifies the server's internal version of the event. Clients can use this string to determine when objects have changed.

[horizontal]
Data type:: integer
Example value:: `311987`

==== kubernetes.event.involvedObject

The object that the event is about.

[horizontal]
Data type:: group

===== kubernetes.event.involvedObject.kind

The type of object

[horizontal]
Data type:: keyword
Example value:: `ReplicationController`

===== kubernetes.event.involvedObject.namespace

The namespace name of the involved object. Note that it may differ from `kubernetes.namespace_name`, which is the namespace where the `eventrouter` application is deployed.

[horizontal]
Data type:: keyword
Example value:: `default`

===== kubernetes.event.involvedObject.name

The name of the object that triggered the event

[horizontal]
Data type:: keyword
Example value:: `java-mainclass-1`

===== kubernetes.event.involvedObject.uid

The unique ID of the object

[horizontal]
Data type:: keyword
Example value:: `e6bff941-76a8-11e7-8193-5254002f560c`

===== kubernetes.event.involvedObject.apiVersion

The version of kubernetes master API

[horizontal]
Data type:: keyword
Example value:: `v1`

===== kubernetes.event.involvedObject.resourceVersion

A string that identifies the server's internal version of the pod that triggered the event. Clients can use this string to determine when objects have changed.

[horizontal]
Data type:: keyword
Example value:: `308882`

==== kubernetes.event.reason

A short machine-understandable string that gives the reason for generating this event

[horizontal]
Data type:: keyword
Example value:: `SuccessfulCreate`

==== kubernetes.event.source_component

The component that reported this event

[horizontal]
Data type:: keyword
Example value:: `replication-controller`

==== kubernetes.event.firstTimestamp

The time at which the event was first recorded

[horizontal]
Data type:: date
Example value:: `2017-08-07 10:11:57.000000000 Z`

==== kubernetes.event.count

The number of times this event has occurred

[horizontal]
Data type:: integer
Example value:: `1`

==== kubernetes.event.type

The type of event, `Normal` or `Warning`. New types could be added in the future.

[horizontal]
Data type:: keyword
Example value:: `Normal`

== OpenShift

The namespace for openshift-logging specific metadata

[horizontal]
Data type:: group

=== openshift.labels

Labels added by the Cluster Log Forwarder configuration

[horizontal]
Data type:: group

// add modules/cluster-logging-exported-fields-openshift when available
