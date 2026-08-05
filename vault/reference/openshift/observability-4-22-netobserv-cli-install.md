---
title: "Installing the Network Observability CLI"
type: reference
domain: openshift
slug: observability-4-22-netobserv-cli-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/netobserv-cli-install
version: 4.22
family: observability
documentKind: "Documentation"
---

# Installing the Network Observability CLI

[id="netobserv-cli-install"]
= Installing the Network Observability CLI

[role="_abstract"]
The Network Observability CLI (oc netobserv) is a standalone {oc-first} plugin used to debug and troubleshoot cluster network traffic. It operates independently of the Network Observability Operator to gather immediate network performance diagnostics.

//Module included in the following assemblies:
//
// observability/network_observability/network-observability-cli/netobserv-cli-overview.adoc

[id="network-observability-netoberv-cli-about_{context}"]
= About the Network Observability CLI

[role="_abstract"]
Use the Network Observability CLI (`oc netobserv`) to quickly debug and troubleshoot networking issues. This tool provides instant, live insight into flows and packets without installing the Network Observability Operator.

The Network Observability CLI is a flow and packet visualization tool that relies on eBPF agents to stream collected data to an ephemeral collector pod. It requires no persistent storage during the capture. After the run, the output is transferred to your local machine.

[IMPORTANT]
====
CLI capture is meant to run only for short durations, such as 8-10 minutes. If it runs for too long, it can be difficult to delete the running process.
====
// Module included in the following assemblies:
//
// * observability/network_observability/netobserv_cli/netobserv-cli-install.adoc

[id="network-observability-cli-install_{context}"]
= Installing the Network Observability CLI

[role="_abstract"]
The Network Observability CLI gives you a lightweight way to quickly debug and troubleshoot network observability. It must be installed separately.

Installing the Network Observability CLI (`oc netobserv`) is a separate procedure from the Network Observability Operator installation. This means that, even if the Operator is installed from the software catalog, the `CLI` must be installed separately.

[NOTE]
====
Users can optionally use Krew to install the `netobserv` CLI plugin. For more information, see "Installing a CLI plugin with Krew".
====

.Prerequisites
* You must install the {oc-first}.
* You must have a macOS or Linux operating system.
* You must install either `docker` or `podman`.

[NOTE]
====
You can use `podman` or `docker` to run the installation commands. This procedure uses `podman`.
====

.Procedure

. Log in to the *Red Hat registry* by running the following command:
+
[source,terminal]
----
$ podman login registry.redhat.io
----

. Extract the `oc-netobserv` file from the image by running the following commands:
+
[source,terminal]
----
$ podman create --name netobserv-cli registry.redhat.io/network-observability/network-observability-cli-rhel9:1.11
$ podman cp netobserv-cli:/oc-netobserv .
$ podman rm netobserv-cli
----

. Move the extracted file to a directory that is on the system's `PATH`, such as `/usr/local/bin/`, by running the following command:
+
[source,terminal]
----
$ sudo mv oc-netobserv /usr/local/bin/
----

.Verification

. Verify that `oc netobserv` is available:
+
[source,terminal]
----
$ oc netobserv version
----
+
This command should produce an outcome similar to the following example:
[source,terminal]
----
Netobserv CLI version <version>
----

[role="_additional-resources"]
.Additional resources
* Installing and using CLI plugins
* Installing the {cli-manager}
