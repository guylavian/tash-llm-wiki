---
title: "Logging 6.2"
type: reference
domain: openshift
slug: observability-4-22-log6x-release-notes-6-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log6x-release-notes-6.2
version: 4.22
family: observability
documentKind: "Documentation"
---

# Logging 6.2

[id="log6x-release-notes-6-2"]
= Logging 6.2

// Module included in the following assemblies:
//
// * observability/logging/logging-6.2/log6x-release-notes-6.2.adoc

[id="logging-release-notes-6-2-0_{context}"]
= Logging 6.2.0 Release Notes

TOFIX
This release includes {logging-uc} {for} Bug Fix Release 6.2.0.

[id="openshift-logging-release-notes-6-2-0-enhancements_{context}"]
== New Features and Enhancements

TOFIX:
=== Log Collection

* This enhancement adds the source `iostream` to the attributes sent from collected container logs. The value is set to either `stdout` or `stderr` based on how the collector received it. (LOG-5292)

* With this update, the default memory limit for the collector increases from 1024 Mi to 2048 Mi. Users should adjust resource limits based on their cluster’s specific needs and specifications. (LOG-6072)

* With this update, users can now set the syslog output delivery mode of the `ClusterLogForwarder` CR to either `AtLeastOnce` or `AtMostOnce.` (LOG-6355)

=== Log Storage

* With this update, the new `1x.pico` LokiStack size supports clusters with fewer workloads and lower log volumes (up to 50GB/day). (LOG-5939)

[id="logging-release-notes-6-2-0-technology-preview-features_{context}"]
== Technology Preview

* With this update, a `dataModel` field has been added to the `lokiStack` output specification. Set the `dataModel` to `Otel` to configure log forwarding using the OpenTelemetry data format. The default is set to `Viaq`. For information about data mapping see OTLP Specification.

[id="logging-release-notes-6-2-0-bug-fixes_{context}"]
== Bug Fixes
TOFIX:
None.

[id="logging-release-notes-6-2-0-CVEs_{context}"]
== CVEs
TOFIX:
* CVE-2024-6119
* CVE-2024-6232
