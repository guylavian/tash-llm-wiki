---
title: "Installing the {hcp} command-line interface"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-cli
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Installing the {hcp} command-line interface

[id="hcp-cli"]
= Installing the {hcp} command-line interface

[role="_abstract"]
The {hcp} command-line interface, `hcp`, is a tool that you can use to get started with {hcp}. For Day 2 operations, such as management and configuration, use GitOps or your own automation tool.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-cli.adoc

[id="hcp-cli-terminal_{context}"]
= Installing the {hcp} command-line interface from the terminal

[role="_abstract"]
You can install the {hcp} command-line interface (CLI), `hcp`, from the terminal.

.Prerequisites

* On an OpenShift Container Platform cluster, you have installed {mce} 2.5 or later. The {mce-short} is automatically installed when you install Red{nbsp}Hat Advanced Cluster Management. You can also install {mce-short} without Red{nbsp}Hat Advanced Management as an Operator from the OpenShift Container Platform software catalog.

.Procedure

. Get the URL to download the `hcp` binary by running the following command:
+
[source,terminal]
----
$ oc get ConsoleCLIDownload hcp-cli-download -o json | jq -r ".spec"
----

. Download the `hcp` binary by running the following command:
+
[source,terminal]
----
$ wget <hcp_cli_download_url>
----
+
Replace `hcp_cli_download_url` with the URL that you obtained from the previous step.

. Unpack the downloaded archive by running the following command:
+
[source,terminal]
----
$ tar xvzf hcp.tar.gz
----

. Make the `hcp` binary file executable by running the following command:
+
[source,terminal]
----
$ chmod +x hcp
----

. Move the `hcp` binary file to a directory in your path by running the following command:
+
[source,terminal]
----
$ sudo mv hcp /usr/local/bin/.
----
+
[NOTE]
====
If you download the CLI on a Mac computer, you might see a warning about the `hcp` binary file. You need to adjust your security settings to allow the binary file to be run.
====

.Verification

* Verify that you see the list of available parameters by running the following command:
+
[source,terminal]
----
$ hcp create cluster <platform> --help
----
+
You can use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `aws`, `agent`, and `kubevirt`.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-cli.adoc

[id="hcp-cli-console_{context}"]
= Installing the {hcp} command-line interface by using the web console

[role="_abstract"]
You can install the {hcp} command-line interface (CLI), `hcp`, by using the OpenShift Container Platform web console.

.Prerequisites

* On an OpenShift Container Platform cluster, you have installed {mce} 2.5 or later. The {mce-short} is automatically installed when you install Red{nbsp}Hat Advanced Cluster Management. You can also install {mce-short} without Red{nbsp}Hat Advanced Management as an Operator from the OpenShift Container Platform software catalog.

.Procedure

. From the OpenShift Container Platform web console, click the *Help icon* -> *Command Line Tools*.

. Click *Download hcp CLI* for your platform.

. Unpack the downloaded archive by running the following command:
+
[source,terminal]
----
$ tar xvzf hcp.tar.gz
----

. Run the following command to make the binary file executable:
+
[source,terminal]
----
$ chmod +x hcp
----

. Run the following command to move the binary file to a directory in your path:
+
[source,terminal]
----
$ sudo mv hcp /usr/local/bin/.
----
+
[NOTE]
====
If you download the CLI on a Mac computer, you might see a warning about the `hcp` binary file. You need to adjust your security settings to allow the binary file to be run.
====

.Verification

* Verify that you see the list of available parameters by running the following command:
+
[source,terminal]
----
$ hcp create cluster <platform> --help
----
+
You can use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `aws`, `agent`, and `kubevirt`.

// Module included in the following assemblies:
// * hosted-control-planes/hcp-prepare/hcp-cli.adoc

[id="hcp-cli-gateway_{context}"]
= Installing the {hcp} command-line interface by using the content gateway

[role="_abstract"]
You can install the {hcp} command-line interface (CLI), `hcp`, by using the content gateway.

.Prerequisites

* On an OpenShift Container Platform cluster, you have installed {mce} 2.7 or later. The {mce-short} is automatically installed when you install Red{nbsp}Hat Advanced Cluster Management. You can also install {mce-short} without Red{nbsp}Hat Advanced Management as an Operator from OpenShift Container Platform OperatorHub.

.Procedure

. Navigate to the content gateway and download the `hcp` binary.

. Unpack the downloaded archive by running the following command:
+
[source,terminal]
----
$ tar xvzf hcp.tar.gz
----

. Make the `hcp` binary file executable by running the following command:
+
[source,terminal]
----
$ chmod +x hcp
----

. Move the `hcp` binary file to a directory in your path by running the following command:
+
[source,terminal]
----
$ sudo mv hcp /usr/local/bin/.
----
+
[NOTE]
====
If you download the CLI on a Mac computer, you might see a warning about the `hcp` binary file. You need to adjust your security settings to allow the binary file to be run.
====

.Verification

* Verify that you see the list of available parameters by running the following command:
+
[source,terminal]
----
$ hcp create cluster <platform> --help
----
+
You can use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `aws`, `agent`, and `kubevirt`.
