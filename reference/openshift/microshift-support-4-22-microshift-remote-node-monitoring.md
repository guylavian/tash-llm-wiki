---
title: "Remote health monitoring with a connected node"
type: reference
domain: openshift
slug: microshift-support-4-22-microshift-remote-node-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_support/microshift-remote-node-monitoring
version: 4.22
family: microshift_support
documentKind: "Documentation"
---

# Remote health monitoring with a connected node

[id="microshift-remote-node-monitoring"]
= Remote health monitoring with a connected node

[role="_abstract"]
{product-title-first} includes a remote health monitoring service that uses the Telemetry API to collect data about your node's performance, configuration, and usage. By analyzing lightweight telemetry data, such as, system version, resource capacity, and usage metrics, Red{nbsp}Hat can proactively identify issues and prioritize new features.

// Module included in the following assemblies:
//
// microshift_support/microshift-remote-node-monitoring.adoc

[id="microshift-about-remote-health-monitoring_{context}"]
= About remote health monitoring with {microshift-short}

[role="_abstract"]
Remote health monitoring is conducted in {microshift-short} by the collection of telemetry and configuration data about your node that is reported to Red{nbsp}Hat with the Telemeter API. A node that reports Telemetry to Red{nbsp}Hat is considered a _connected node_.

*Telemetry* is the term that Red{nbsp}Hat uses to describe the information being sent to Red{nbsp}Hat by the {microshift-short} Telemeter API. Lightweight attributes are sent from a connected node to Red{nbsp}Hat to monitor the health of a node.

Telemetry provides the following benefits:

* *Enhanced identification and resolution of issues*. Events that might seem normal to an end-user can be observed by Red{nbsp}Hat from a broader perspective. Some issues can be more rapidly identified from this point of view and resolved without an end-user needing to open a support case or file a Jira issue.

* *Targeted prioritization of new features and functionality*. The data collected provides information about system capabilities and usage characteristics. With this information, Red{nbsp}Hat can focus on developing the new features and functionality that have the greatest impact for our customers.

Telemetry sends a carefully chosen subset of the node monitoring metrics to Red{nbsp}Hat. The Telemeter API fetches the metrics values every hour and uploads the data to Red{nbsp}Hat. This stream of data is used by Red{nbsp}Hat to monitor nodes over time.

This debugging information is available to Red{nbsp}Hat Support and Engineering teams with the same restrictions as accessing data reported through support cases. All _connected node_ information is used by Red{nbsp}Hat to help make {microshift-short} better.

[NOTE]
====
{microshift-short} does not support Prometheus. To view the Telemetry gathered from your node, you must contact Red{nbsp}Hat Support.
====

// Module included in the following assemblies:
//
// * microshift_support/microshift-remote-node-monitoring.adoc

[id="microshift-info-collected-by-telemetry_{context}"]
= Information collected by the {microshift-short} Telemetry API

[role="_abstract"]
The {microshift-short} Telemetry API collects a lightweight set of metrics to assist with remote health monitoring and product improvement. The data payload is minimal, generally under 2KB, and is designed to have very minimal impact on node resources. The collected information is categorized into system configuration, node capacity, and usage metrics.

The following information is collected by Telemetry:

System information::

The system information describes the basic configuration of your {microshift-short} node and where it is running, for example:

* Version information, including the {microshift-short} node version.
* The {op-system-base-full} version.
* The {op-system-base} deployment type.

Sizing information::

Sizing information details the node capacity, for example:

* The CPU cores {microshift-short} can use.
* Architecture information.
* The usable bytes of memory.

Usage information::

Usage information outlines what is happening in the node, for example:

* The CPU usage in percentage.
* The memory usage in percentage.
* The number of Kubernetes objects by resource type (CRDs).
* The number of running containers, namespaces, and running pods.
* The number of routes, ingress, services.

[NOTE]
====
Telemetry does not collect identifying information such as usernames or passwords. Red{nbsp}Hat does not intend to collect personal information. If Red{nbsp}Hat discovers that personal information has been inadvertently received, Red{nbsp}Hat deletes such information. To the extent that any Telemetry constitutes personal data, refer to the Red{nbsp}Hat Privacy Statement for more information about Red{nbsp}Hat's privacy practices.
====

Additional details about how remote health monitoring data is used::

Red{nbsp}Hat collects data about your use of the Red{nbsp}Hat product(s) for purposes such as providing support and troubleshooting, improving the offerings and user experience, responding to issues, and for billing purposes if applicable.

* Collection safeguards: Red{nbsp}Hat employs technical and organizational measures designed to protect Telemetry data.

* Sharing: Red{nbsp}Hat might share the data collected through the Telemetry API internally within Red{nbsp}Hat to improve your user experience. Red{nbsp}Hat might share Telemetry data with its business partners in an aggregated form that does not identify customers to help the partners better understand their markets and their customers' use of Red{nbsp}Hat offerings, or to ensure the successful integration of products jointly supported by those partners.

* Third parties: Red{nbsp}Hat might engage certain third parties to assist in the collection, analysis, and storage of Telemetry data.

* Disabling Telemetry data collection: You can disable {microshift-short} Telemetry by following the instructions in the "Opting out of remote health reporting for {microshift-short}" section.

// Module included in the following assemblies:
//
// microshift_support/microshift-remote-node-monitoring.adoc

[id="microshift-opt-out-telemetry_{context}"]
= Opting out of Telemetry for {microshift-short}

[role="_abstract"]
By default, {microshift-short} enables the Telemetry service to collect health and usage data. You can disable this service if your node is operating in a disconnected environment or if you want to opt out of data collection.

.Prerequisites

* You installed {oc-first}.
* You have root access to the node.

.Procedure

. If you have not done so, make a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, renaming it `config.yaml`.

. Keep the new {microshift-short} `config.yaml` in the `/etc/microshift/` directory. Your `config.yaml` file is read every time the {microshift-short} service starts.
+
[NOTE]
====
After you create it, the `config.yaml` file takes precedence over built-in settings.
====

. Optional: Use a configuration snippet if you are using an existing {microshift-short} YAML. See "Using configuration snippets" in the _Additional resources_ section for more information.

. Set the `telemetry.status` section of the {microshift-short} YAML with the `Disabled` value.
+
.Example disabled Telemetry configuration
[source,yaml]
----
apiServer:
# ...
telemetry:
    endpoint: https://infogw.api.openshift.com
    status: Disabled
# ...
----

[role="_additional-resources"]
[id="additional-resources_microshift-remote-node-monitoring_{context}"]
== Additional resources

* Using configuration snippets
