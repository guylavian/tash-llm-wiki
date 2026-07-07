---
title: "Monitoring cluster events and logs"
type: reference
domain: openshift
slug: security-4-22-security-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/security-monitoring
version: 4.22
family: security
documentKind: "Documentation"
---

# Monitoring cluster events and logs

[id="security-monitoring"]
= Monitoring cluster events and logs

The ability to monitor and audit an OpenShift Container Platform cluster is an
important part of safeguarding the cluster and its users against
inappropriate usage.

There are two main sources of cluster-level information that
are useful for this purpose: events and logging.

// Cluster events
// Module included in the following assemblies:
//
// * security/container_security/security-monitoring.adoc

[id="security-monitoring-events_{context}"]
= Watching cluster events

Cluster administrators are encouraged to familiarize themselves with the `Event` resource
type and review the list of system events to
determine which events are of interest.
Events are associated with a namespace, either the namespace of the
resource they are related to or, for cluster events, the `default`
namespace. The default namespace holds relevant events for monitoring or auditing a cluster,
such as node events and resource events related to infrastructure components.

The master API and `oc` command do not provide parameters to scope a listing of events to only those
related to nodes. A simple approach would be to use `grep`:

[source,terminal]
----
$ oc get event -n default | grep Node
----

.Example output
[source,terminal]
----
1h         20h         3         origin-node-1.example.local   Node      Normal    NodeHasDiskPressure   ...
----

A more flexible approach is to output the events in a form that other
tools can process. For example, the following example uses the `jq`
tool against JSON output to extract only `NodeHasDiskPressure` events:

[source,terminal]
----
$ oc get events -n default -o json \
  | jq '.items[] | select(.involvedObject.kind == "Node" and .reason == "NodeHasDiskPressure")'
----

.Example output
[source,terminal]
----
{
  "apiVersion": "v1",
  "count": 3,
  "involvedObject": {
    "kind": "Node",
    "name": "origin-node-1.example.local",
    "uid": "origin-node-1.example.local"
  },
  "kind": "Event",
  "reason": "NodeHasDiskPressure",
  ...
}
----

Events related to resource creation, modification, or deletion can also be
good candidates for detecting misuse of the cluster. The following query,
for example, can be used to look for excessive pulling of images:

[source,terminal]
----
$ oc get events --all-namespaces -o json \
  | jq '[.items[] | select(.involvedObject.kind == "Pod" and .reason == "Pulling")] | length'
----

.Example output
[source,terminal]
----
4
----

[NOTE]
====
When a namespace is deleted, its events are deleted as well. Events can also expire and are deleted to prevent
filling up etcd storage. Events are
not stored as a permanent record and frequent polling is necessary to capture statistics over time.
====

// Logging
// Module included in the following assemblies:
//
// * security/container_security/security-monitoring.adoc

[id="security-monitoring-cluster-logging_{context}"]
= Logging

Using the `oc log` command, you can view container logs, build configs and deployments in real time. Different can users have access different access to logs:

* Users who have access to a project are able to see the logs for that project by default.
* Users with admin roles can access all container logs.

To save your logs for further audit and analysis, you can enable the `cluster-logging` add-on feature to collect, manage, and view system, container, and audit logs. You can deploy, manage, and upgrade OpenShift Logging through the {es-op} and {clo}.

// Audit logging
// Module included in the following assemblies:
//
// * security/container_security/security-monitoring.adoc

[id="security-monitoring-audit-logs_{context}"]
= Audit logs

With _audit logs_, you can follow a sequence of activities associated with how a
user, administrator, or other OpenShift Container Platform component is behaving.
API audit logging is done on each server.

[role="_additional-resources"]
.Additional resources
* List of system events
//* xref :../../observability/logging/cluster-logging.adoc#cluster-logging[Understanding OpenShift Logging]
* Viewing audit logs
