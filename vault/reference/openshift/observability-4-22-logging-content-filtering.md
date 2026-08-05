---
title: "Filtering logs by content"
type: reference
domain: openshift
slug: observability-4-22-logging-content-filtering
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-content-filtering
version: 4.22
family: observability
documentKind: "Documentation"
---

# Filtering logs by content

[id="logging-content-filtering"]
= Filtering logs by content

Collecting all logs from a cluster might produce a large amount of data, which can be expensive to transport and store.

You can reduce the volume of your log data by filtering out low priority data that does not need to be stored. {logging-uc} provides content filters that you can use to reduce the volume of log data.

[NOTE]
====
Content filters are distinct from `input` selectors. `input` selectors select or ignore entire log streams based on source metadata. Content filters edit log streams to remove and modify records based on the record content.
====

Log data volume can be reduced by using one of the following methods:

* Configuring content filters to drop unwanted log records
* Configuring content filters to prune log records

// Module included in the following assemblies:
//
// * observability/logging/performance_reliability/logging-content-filtering.adoc

[id="logging-content-filter-drop-records_{context}"]
= Configuring content filters to drop unwanted log records

When the `drop` filter is configured, the log collector evaluates log streams according to the filters before forwarding. The collector drops unwanted log records that match the specified configuration.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have created a `ClusterLogForwarder` custom resource (CR).

.Procedure

. Add a configuration for a filter to the `filters` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to drop log records based on regular expressions:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  filters:
  - name: <filter_name>
    type: drop # <1>
    drop: # <2>
    - test: # <3>
      - field: .kubernetes.labels."foo-bar/baz" # <4>
        matches: .+ # <5>
      - field: .kubernetes.pod_name
        notMatches: "my-pod" # <6>
  pipelines:
  - name: <pipeline_name> # <7>
    filterRefs: ["<filter_name>"]
# ...
----
<1> Specifies the type of filter. The `drop` filter drops log records that match the filter configuration.
<2> Specifies configuration options for applying the `drop` filter.
<3> Specifies the configuration for tests that are used to evaluate whether a log record is dropped.
** If all the conditions specified for a test are true, the test passes and the log record is dropped.
** When multiple tests are specified for the `drop` filter configuration, if any of the tests pass, the record is dropped.
** If there is an error evaluating a condition, for example, the field is missing from the log record being evaluated, that condition evaluates to false.
<4> Specifies a dot-delimited field path, which is a path to a field in the log record. The path can contain alpha-numeric characters and underscores (`a-zA-Z0-9_`), for example, `.kubernetes.namespace_name`. If segments contain characters outside of this range, the segment must be in quotes, for example, `.kubernetes.labels."foo.bar-bar/baz"`. You can include multiple field paths in a single `test` configuration, but they must all evaluate to true for the test to pass and the `drop` filter to be applied.
<5> Specifies a regular expression. If log records match this regular expression, they are dropped. You can set either the `matches` or `notMatches` condition for a single `field` path, but not both.
<6> Specifies a regular expression. If log records do not match this regular expression, they are dropped. You can set either the `matches` or `notMatches` condition for a single `field` path, but not both.
<7> Specifies the pipeline that the `drop` filter is applied to.

. Apply the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Additional examples

The following additional example shows how you can configure the `drop` filter to only keep higher priority log records:

[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  filters:
  - name: important
    type: drop
    drop:
      test:
      - field: .message
        notMatches: "(?i)critical|error"
      - field: .level
        matches: "info|warning"
# ...
----

In addition to including multiple field paths in a single `test` configuration, you can also include additional tests that are treated as _OR_ checks. In the following example, records are dropped if either `test` configuration evaluates to true. However, for the second `test` configuration, both field specs must be true for it to be evaluated to true:

[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  filters:
  - name: important
    type: drop
    drop:
      test:
      - field: .kubernetes.namespace_name
        matches: "^open"
      test:
      - field: .log_type
        matches: "application"
      - field: .kubernetes.pod_name
        notMatches: "my-pod"
# ...
----
// Module included in the following assemblies:
//
// * observability/logging/performance_reliability/logging-content-filtering.adoc

[id="logging-content-filter-prune-records_{context}"]
= Configuring content filters to prune log records

When the `prune` filter is configured, the log collector evaluates log streams according to the filters before forwarding. The collector prunes log records by removing low value fields such as pod annotations.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have created a `ClusterLogForwarder` custom resource (CR).

.Procedure

. Add a configuration for a filter to the `prune` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to prune log records based on field paths:
+
[IMPORTANT]
====
If both are specified, records are pruned based on the `notIn` array first, which takes precedence over the `in` array. After records have been pruned by using the `notIn` array, they are then pruned by using the `in` array.
====
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  filters:
  - name: <filter_name>
    type: prune # <1>
    prune: # <2>
      in: [.kubernetes.annotations, .kubernetes.namespace_id] # <3>
      notIn: [.kubernetes,.log_type,.message,."@timestamp"] # <4>
  pipelines:
  - name: <pipeline_name> # <5>
    filterRefs: ["<filter_name>"]
# ...
----
<1> Specify the type of filter. The `prune` filter prunes log records by configured fields.
<2> Specify configuration options for applying the `prune` filter. The `in` and `notIn` fields are specified as arrays of dot-delimited field paths, which are paths to fields in log records. These paths can contain alpha-numeric characters and underscores (`a-zA-Z0-9_`), for example, `.kubernetes.namespace_name`. If segments contain characters outside of this range, the segment must be in quotes, for example, `.kubernetes.labels."foo.bar-bar/baz"`.
<3> Optional: Any fields that are specified in this array are removed from the log record.
<4> Optional: Any fields that are not specified in this array are removed from the log record.
<5> Specify the pipeline that the `prune` filter is applied to.

. Apply the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

[role="_additional-resources"]
[id="additional-resources_logging-content-filtering"]
== Additional resources
* About forwarding logs to third-party systems
