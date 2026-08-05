---
title: "Installing the opm CLI"
type: reference
domain: openshift
slug: cli-reference-4-22-cli-opm-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/cli-opm-install
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Installing the opm CLI

[id="cli-opm-install"]
= Installing the opm CLI

// Module included in the following assemblies:
//
// * operators/understanding/olm-packaging-format.adoc
// * cli_reference/opm/cli-opm-install.adoc

[id="olm-about-opm_{context}"]
= About the opm CLI

The `opm` CLI tool is provided by the Operator Framework for use with the Operator bundle format. This tool allows you to create and maintain catalogs of Operators from a list of Operator bundles that are similar to software repositories. The result is a container image which can be stored in a container registry and then installed on a cluster.

A catalog contains a database of pointers to Operator manifest content that can be queried through an included API that is served when the container image is run. On OpenShift Container Platform, Operator Lifecycle Manager (OLM) can reference the image in a catalog source, defined by a `CatalogSource` object, which polls the image at regular intervals to enable frequent updates to installed Operators on the cluster.

[role="_additional-resources"]
.Additional resources

* See Operator Framework packaging format for more information about the bundle format.

// Module included in the following assemblies:
//
// * cli_reference/opm/cli-opm-install.adoc

[id="olm-installing-opm_{context}"]
= Installing the opm CLI

You can install the `opm` CLI tool on your Linux, macOS, or Windows workstation.

.Prerequisites

* For {op-system-base-full} 9.0 and later, you must provide the following packages:
** `podman` version 1.9.3+ (version 2.0+ recommended)
** `glibc` version 2.28+

.Procedure

. Navigate to the OpenShift mirror site and download the latest version of the tarball that matches your operating system.

. Navigate to the OpenShift mirror site and download the latest version of the tarball that matches your operating system.

. Unpack the archive.

** For Linux or macOS:
+
[source,terminal,subs="attributes+"]
----
$ tar xvf <file>
----

** For Windows, unzip the archive with a ZIP program.

. Place the file anywhere in your `PATH`.
+
--
* For Linux or macOS:

.. Check your `PATH`:
+
[source,terminal]
----
$ echo $PATH
----

.. Move the file. For example:
+
[source,terminal]
----
$ sudo mv ./opm /usr/local/bin/
----

* For Windows:

.. Check your `PATH`:
+
[source,terminal]
----
C:\> path
----

.. Move the file:
+
[source,terminal]
----
C:\> move opm.exe <directory>
----
--

.Verification

* After you install the `opm` CLI, verify that it is available:
+
[source,terminal]
----
$ opm version
----

[role="_additional-resources"]
[id="opm-addtl-resources"]
== Additional resources

* See Managing custom catalogs for `opm` procedures including creating, updating, and pruning catalogs.
