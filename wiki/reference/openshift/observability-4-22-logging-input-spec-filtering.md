---
title: "Filtering logs by metadata"
type: reference
domain: openshift
slug: observability-4-22-logging-input-spec-filtering
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/logging-input-spec-filtering
version: 4.22
family: observability
documentKind: "Documentation"
---

# Filtering logs by metadata

[id="logging-input-spec-filtering"]
= Filtering logs by metadata

You can filter logs in the `ClusterLogForwarder` CR to select or ignore an entire log stream based on the metadata by using the `input` selector. As an administrator or developer, you can include or exclude the log collection to reduce the memory and CPU load on the collector.

[IMPORTANT]
====
You can use this feature only if the Vector collector is set up in your logging deployment.
====

[NOTE]
====
`input` spec filtering is different from content filtering. `input` selectors select or ignore entire log streams based on the source metadata. Content filters edit the log streams to remove and modify the records based on the record content.
====

// Module included in the following assemblies:
//
// * observability/logging/performance_reliability/logging-input-spec-filtering.adoc

[id="logging-input-spec-filter-namespace-container_{context}"]
= Filtering application logs at input by including or excluding the namespace or container name

You can include or exclude the application logs based on the namespace and container name by using the `input` selector.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have created a `ClusterLogForwarder` custom resource (CR).

.Procedure

. Add a configuration to include or exclude the namespace and container names in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to include or exclude namespaces and container names:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: ClusterLogForwarder
# ...
spec:
  inputs:
    - name: mylogs
      application:
        includes:
          - namespace: "my-project" # <1>
            container: "my-container" # <2>
        excludes:
          - container: "other-container*" # <3>
            namespace: "other-namespace" # <4>
# ...
----
<1> Specifies that the logs are only collected from these namespaces.
<2> Specifies that the logs are only collected from these containers.
<3> Specifies the pattern of namespaces to ignore when collecting the logs.
<4> Specifies the set of containers to ignore when collecting the logs.

. Apply the `ClusterLogForwarder` CR by running the following command:

+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
[NOTE]
====
The `excludes` option takes precedence over `includes`.
====
// Module included in the following assemblies:
//
// * observability/logging/performance_reliability/logging-input-spec-filtering.adoc

[id="logging-input-spec-filter-labels-expressions_{context}"]
= Filtering application logs at input by including either the label expressions or matching label key and values

You can include the application logs based on the label expressions or a matching label key and its values by using the `input` selector.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have created a `ClusterLogForwarder` custom resource (CR).

.Procedure

. Add a configuration for a filter to the `input` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to include logs based on label expressions or matched label key/values:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: ClusterLogForwarder
# ...
spec:
  inputs:
    - name: mylogs
      application:
        selector:
          matchExpressions:
          - key: env # <1>
            operator: In # <2>
            values: [“prod”, “qa”] # <3>
          - key: zone
            operator: NotIn
            values: [“east”, “west”]
          matchLabels: # <4>
            app: one
            name: app1
# ...
----
<1> Specifies the label key to match.
<2> Specifies the operator. Valid values include: `In`, `NotIn`, `Exists`, and `DoesNotExist`.
<3> Specifies an array of string values. If the `operator` value is either `Exists` or `DoesNotExist`, the value array must be empty.
<4> Specifies an exact key or value mapping.

. Apply the `ClusterLogForwarder` CR by running the following command:

+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
// Module included in the following assemblies:
//
// * observability/logging/performance_reliability/logging-input-spec-filtering.adoc

[id="logging-input-spec-filter-audit-infrastructure_{context}"]
= Filtering the audit and infrastructure log inputs by source

You can define the list of `audit` and `infrastructure` sources to collect the logs by using the `input` selector.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have created a `ClusterLogForwarder` custom resource (CR).

.Procedure

. Add a configuration to define the `audit` and `infrastructure` sources in the `ClusterLogForwarder` CR.

+
The following example shows how to configure the `ClusterLogForwarder` CR to define `aduit` and `infrastructure` sources:
+
.Example `ClusterLogForwarder` CR
+
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: ClusterLogForwarder
# ...
spec:
  inputs:
    - name: mylogs1
      infrastructure:
        sources: # <1>
          - node
    - name: mylogs2
      audit:
        sources: # <2>
          - kubeAPI
          - openshiftAPI
          - ovn
# ...
----
<1> Specifies the list of infrastructure sources to collect. The valid sources include:
** `node`: Journal log from the node
** `container`: Logs from the workloads deployed in the namespaces
<2> Specifies the list of audit sources to collect. The valid sources include:
** `kubeAPI`: Logs from the Kubernetes API servers
** `openshiftAPI`: Logs from the OpenShift API servers
** `auditd`: Logs from a node auditd service
** `ovn`: Logs from an open virtual network service

. Apply the `ClusterLogForwarder` CR by running the following command:

+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
