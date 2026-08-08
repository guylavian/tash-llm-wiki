---
title: "Installing tkn"
type: reference
domain: openshift
slug: cli-reference-4-22-installing-tkn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/installing-tkn
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Installing tkn

[id='installing-tkn']
= Installing tkn

Use the CLI tool to manage {pipelines-title} from a terminal. The following section describes how to install the CLI tool on different platforms.

You can also find the URL to the latest binaries from the OpenShift Container Platform web console by clicking the *?* icon in the upper-right corner and selecting *Command Line Tools*.

[NOTE]
====
Both the archives and the RPMs contain the following executables:

* `tkn`
* `tkn-pac`
* `opc`
====

// Install tkn on Linux
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

[id="installing-tkn-on-linux"]

= Installing the {pipelines-title} CLI on Linux

[role="_abstract"]
For Linux distributions, you can download the CLI as a `tar.gz` archive.

.Procedure

. Download the relevant CLI tool.

* Linux (x86_64, amd64)

* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)

* Linux on {ibm-power-name} (ppc64le)

* Linux on ARM (aarch64, arm64)

// Binaries also need to be updated in the following modules:
// op-installing-pipelines-as-code-cli.adoc
// op-installing-tkn-on-windows.adoc
// op-installing-tkn-on-macos.adoc

. Unpack the archive:
+
[source,terminal]
----
$ tar xvzf <file>
----
. Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.

. Add the location of your `tkn` and `tkn-pac` files to your `PATH` environment variable.

. To check your `PATH`, run the following command:
+
[source,terminal]
----
$ echo $PATH
----

// Install tkn on Linux using RPM
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

[id="installing-tkn-on-linux-using-rpm"]

= Installing the {pipelines-title} CLI on Linux using an RPM

[role="_abstract"]
For {op-system-base-full} version 8, you can install the {pipelines-title} CLI as an RPM.

.Prerequisites

* You have an active OpenShift Container Platform subscription on your Red Hat account.
* You have root or sudo privileges on your local system.

.Procedure

. Register with Red Hat Subscription Manager:
+
[source,terminal]
----
# subscription-manager register
----

. Pull the latest subscription data:
+
[source,terminal]
----
# subscription-manager refresh
----

. List the available subscriptions:
+
[source,terminal]
----
# subscription-manager list --available --matches '*pipelines*'
----

. In the output for the previous command, find the pool ID for your OpenShift Container Platform subscription and attach the subscription to the registered system:
+
[source,terminal]
----
# subscription-manager attach --pool=<pool_id>
----

. Enable the repositories required by {pipelines-title}:
+
* Linux (x86_64, amd64)
+
[source,terminal,subs="attributes"]
----
# subscription-manager repos --enable="pipelines-{pipelines-version-number}-for-rhel-8-x86_64-rpms"
----
+
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)
+
[source,terminal,subs="attributes"]
----
# subscription-manager repos --enable="pipelines-{pipelines-version-number}-for-rhel-8-s390x-rpms"
----
+
* Linux on {ibm-power-name} (ppc64le)
+
[source,terminal,subs="attributes"]
----
# subscription-manager repos --enable="pipelines-{pipelines-version-number}-for-rhel-8-ppc64le-rpms"
----
+
* Linux on ARM (aarch64, arm64)
+
[source,terminal,subs="attributes"]
----
# subscription-manager repos --enable="pipelines-{pipelines-version-number}-for-rhel-8-aarch64-rpms"
----
. Install the `openshift-pipelines-client` package:
+
[source,terminal]
----
# yum install openshift-pipelines-client
----

After you install the CLI, it is available using the `tkn` command:

[source,terminal]
----
$ tkn version
----

//Install tkn on Windows
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

[id="installing-tkn-on-windows"]

= Installing the {pipelines-title} CLI on Windows

[role="_abstract"]
For Windows, you can download the CLI as a `zip` archive.

.Procedure

.  Download the CLI tool.

. Extract the archive with a ZIP program.
. Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.
. Add the location of your `tkn` and `tkn-pac` files to your `PATH` environment variable.

. To check your `PATH`, run the following command:
+
[source,terminal]
----
C:\> path
----

//Install tkn on macOS
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/installing-tkn.adoc

[id="installing-tkn-on-macos"]

= Installing the {pipelines-title} CLI on macOS

[role="_abstract"]
For macOS, you can download the CLI as a `tar.gz` archive.

.Procedure

. Download the relevant CLI tool.

* macOS

* macOS on ARM

. Unpack and extract the archive.

. Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.

. Add the location of your `tkn` and `tkn-pac` and files to your `PATH` environment variable.

. To check your `PATH`, run the following command:
+
[source,terminal]
----
$ echo $PATH
----
