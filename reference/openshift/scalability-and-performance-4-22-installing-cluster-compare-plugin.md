---
title: "Installing the cluster-compare plugin"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-installing-cluster-compare-plugin
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/installing-cluster-compare-plugin
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Installing the cluster-compare plugin

[id="installing-cluster-compare-plugin"]
= Installing the cluster-compare plugin

You can extract the `cluster-compare` plugin from a container image in the Red Hat container catalog and use it as a plugin to the `oc` command.

// Module included in the following assemblies:

// *scalability_and_performance/cluster-compare/installing-cluster-compare-plugin.adoc

[id="installing-cluster-compare_{context}"]
= Installing the cluster-compare plugin

Install the `cluster-compare` plugin to compare a reference configuration with a cluster configuration from a live cluster or `must-gather` data.

.Prerequisites

. You have installed the OpenShift CLI (`oc`).

. You installed `podman`.

. You have access to the Red Hat container catalog.

.Procedure

. Log in to the Red Hat container catalog by running the following command:
+
[source,terminal]
----
$ podman login registry.redhat.io
----

. Create a container for the `cluster-compare` image by running the following command:
+
[source,terminal]
----
$ podman create --name cca registry.redhat.io/openshift4/kube-compare-artifacts-rhel9:latest
----

. Copy the `cluster-compare` plugin to a directory that is included in your `PATH` environment variable by running the following command:
+
[source,terminal]
----
$ podman cp cca:/usr/share/openshift/<arch>/kube-compare.<rhel_version> <directory_on_path>/kubectl-cluster_compare
----
+
* `arch` is the architecture for your machine. Valid values are:
** `linux_amd64`
** `linux_arm64`
** `linux_ppc64le`
** `linux_s390x`
* `<rhel_version>` is the version of {op-system-base} on your machine. Valid values are `rhel8` or `rhel9`.
* `<directory_on_path>` is the path to a directory included in your `PATH` environment variable.

.Verification

* View the help for the plugin by running the following command:
+
[source,terminal]
----
$ oc cluster-compare -h
----
+
.Example output
[source,terminal]
----
Compare a known valid reference configuration and a set of specific cluster configuration CRs.

...

Usage:
  compare -r <Reference File>

Examples:
  # Compare a known valid reference configuration with a live cluster:
  kubectl cluster-compare -r ./reference/metadata.yaml

 ...
----

[role="_additional-resources"]
== Additional resources

* Extending the OpenShift CLI with plugins
