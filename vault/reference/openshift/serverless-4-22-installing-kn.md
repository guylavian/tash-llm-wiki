---
title: "Installing the Knative CLI"
type: reference
domain: openshift
slug: serverless-4-22-installing-kn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/installing-kn
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Installing the Knative CLI

[id="installing-kn"]
= Installing the Knative CLI

The Knative (`kn`) CLI does not have its own login mechanism. To log in to the cluster, you must install the OpenShift CLI (`oc`) and use the `oc login` command. Installation options for the CLIs may vary depending on your operating system.

For more information on installing the OpenShift CLI (`oc`) for your operating system and logging in with `oc`, see the OpenShift CLI getting started documentation.
// need to wait til CLI docs are added to OSD and ROSA for this link to work
// TODO: remove this conditional once this is available

{ServerlessProductName} cannot be installed using the Knative (`kn`) CLI. A cluster administrator must install the {ServerlessOperatorName} and set up the Knative components, as described in the Installing the {ServerlessOperatorName} documentation.

[IMPORTANT]
====
If you try to use an older version of the Knative (`kn`) CLI with a newer {ServerlessProductName} release, the API is not found and an error occurs.

For example, if you use the 1.23.0 release of the Knative (`kn`) CLI, which uses version 1.2, with the 1.24.0 {ServerlessProductName} release, which uses the 1.3 versions of the Knative Serving and Knative Eventing APIs, the CLI does not work because it continues to look for the outdated 1.2 API versions.

Ensure that you are using the latest Knative (`kn`) CLI version for your {ServerlessProductName} release to avoid issues.
====

// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

[id="installing-cli-web-console_{context}"]
= Installing the Knative CLI using the OpenShift Container Platform web console

Using the OpenShift Container Platform web console provides a streamlined and intuitive user interface to install the Knative (`kn`) CLI. After the {ServerlessOperatorName} is installed, you will see a link to download the Knative (`kn`) CLI for Linux (amd64, s390x, ppc64le), macOS, or Windows from the *Command Line Tools* page in the OpenShift Container Platform web console.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* The {ServerlessOperatorName} and Knative Serving are installed on your OpenShift Container Platform cluster.
+
[IMPORTANT]
====
If *libc* is not available, you might see the following error when you run CLI commands:

[source,terminal]
----
$ kn: No such file or directory
----
====

* If you want to use the verification steps for this procedure, you must install the OpenShift (`oc`) CLI.

.Procedure

. Download the Knative (`kn`) CLI from the *Command Line Tools* page. You can access the *Command Line Tools* page by clicking the image:../images/question-circle.png[title="Help"] icon in the top right corner of the web console and selecting *Command Line Tools* in the list.

. Unpack the archive:
+
[source,terminal]
----
$ tar -xf <file>
----

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, run:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* Run the following commands to check that the correct Knative CLI resources and route have been created:
+
[source,terminal]
----
$ oc get ConsoleCLIDownload
----
+
.Example output
[source,terminal]
----
NAME                  DISPLAY NAME                                             AGE
kn                    kn - OpenShift Serverless Command Line Interface (CLI)   2022-09-20T08:41:18Z
oc-cli-downloads      oc - OpenShift Command Line Interface (CLI)              2022-09-20T08:00:20Z
----
+
[source,terminal]
----
$ oc get route -n openshift-serverless
----
+
.Example output
[source,terminal]
----
NAME   HOST/PORT                                  PATH   SERVICES                      PORT       TERMINATION     WILDCARD
kn     kn-openshift-serverless.apps.example.com          knative-openshift-metrics-3   http-cli   edge/Redirect   None
----
// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

[id="serverless-installing-cli-linux-rpm-package-manager_{context}"]
= Installing the Knative CLI for Linux by using an RPM package manager

For {op-system-base-full}, you can install the Knative (`kn`) CLI as an RPM by using a package manager, such as `yum` or `dnf`. This allows the Knative CLI version to be automatically managed by the system. For example, using a command like `dnf upgrade` upgrades all packages, including `kn`, if a new version is available.

.Prerequisites

* You have an active OpenShift Container Platform subscription on your Red Hat account.

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

. Attach the subscription to the registered system:
+
[source,terminal]
----
# subscription-manager attach --pool=<pool_id> <1>
----
+
<1> Pool ID for an active OpenShift Container Platform subscription

. Enable the repositories required by the Knative (`kn`) CLI:
+
* Linux (x86_64, amd64)
+
[source,terminal]
----
# subscription-manager repos --enable="openshift-serverless-1-for-rhel-8-x86_64-rpms"
----
+
* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)
+
[source,terminal]
----
# subscription-manager repos --enable="openshift-serverless-1-for-rhel-8-s390x-rpms"
----
+
* Linux on {ibm-power-name} (ppc64le)
+
[source,terminal]
----
# subscription-manager repos --enable="openshift-serverless-1-for-rhel-8-ppc64le-rpms"
----

. Install the Knative (`kn`) CLI as an RPM by using a package manager:
+
.Example `yum` command
[source,terminal]
----
# yum install openshift-serverless-clients
----
// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

[id="installing-cli-linux_{context}"]
= Installing the Knative CLI for Linux

If you are using a Linux distribution that does not have RPM or another package manager installed, you can install the Knative (`kn`) CLI as a binary file. To do this, you must download and unpack a `tar.gz` archive and add the binary to a directory on your `PATH`.

.Prerequisites

* If you are not using RHEL or Fedora, ensure that *libc* is installed in a directory on your library path.
+
[IMPORTANT]
====
If *libc* is not available, you might see the following error when you run CLI commands:

[source,terminal]
----
$ kn: No such file or directory
----
====

.Procedure

. Download the relevant Knative (`kn`) CLI `tar.gz` archive:
+
--
* Linux (x86_64, amd64)

* Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)

* Linux on {ibm-power-name} (ppc64le)
--
+
You can also download any version of `kn` by navigating to that version's corresponding directory in the Serverless client download mirror.

. Unpack the archive:
+
[source,terminal]
----
$ tar -xf <filename>
----

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, run:
+
[source,terminal]
----
$ echo $PATH
----
// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

[id="serverless-installing-cli-macos_{context}"]
= Installing the Knative CLI for macOS

If you are using macOS, you can install the Knative (`kn`) CLI as a binary file. To do this, you must download and unpack a `tar.gz` archive and add the binary to a directory on your `PATH`.

// no prereqs?

.Procedure

. Download the Knative (`kn`) CLI `tar.gz` archive.
+
You can also download any version of `kn` by navigating to that version's corresponding directory in the Serverless client download mirror.

. Unpack and extract the archive.

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, open a terminal window and run:
+
[source,terminal]
----
$ echo $PATH
----
// Module included in the following assemblies:
//
// * serverless/cli_tools/installing-kn.adoc

[id="installing-cli-windows_{context}"]
= Installing the Knative CLI for Windows

If you are using Windows, you can install the Knative (`kn`) CLI as a binary file. To do this, you must download and unpack a ZIP archive and add the binary to a directory on your `PATH`.

// no prereqs?

.Procedure

. Download the Knative (`kn`) CLI ZIP archive.
+
You can also download any version of `kn` by navigating to that version's corresponding directory in the Serverless client download mirror.

. Extract the archive with a ZIP program.

. Move the `kn` binary to a directory on your `PATH`.

. To check your `PATH`, open the command prompt and run the command:
+
[source,terminal]
----
C:\> path
----
