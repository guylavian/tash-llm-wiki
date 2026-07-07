---
title: "Getting started with the OpenShift CLI"
type: reference
domain: openshift
slug: cli-reference-4-22-getting-started-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/getting-started-cli
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Getting started with the OpenShift CLI

[id="cli-getting-started"]
= Getting started with the OpenShift CLI

// About the CLI
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-about-cli_{context}"]
= About the OpenShift CLI

With the {oc-first}, you can create applications and manage OpenShift Container Platform projects from a terminal. The OpenShift CLI is ideal in the following situations:

* Working directly with project source code.
* Scripting OpenShift Container Platform operations
* Managing projects while restricted by bandwidth resources and the web console is unavailable.
* Managing projects while restricted by bandwidth resources.

[id="installing-openshift-cli"]
== Installing the OpenShift CLI

You can install the OpenShift CLI (`oc`) either by downloading the binary or by using an RPM.

// Installing the OpenShift CLI on Linux
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-linux_{context}"]
= Installing the OpenShift CLI on Linux

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on Linux.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.

. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Navigate to the Download {OCP} page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Linux Clients* entry and save the file.
. Unpack the archive:
+
[source,terminal]
----
$ tar xvf <file>
----

. Place the `oc` binary in a directory that is on your `PATH`.
+
To check your `PATH`, execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Installing the OpenShift CLI on Windows
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-windows_{context}"]
= Installing the OpenShift CLI on Windows

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install {oc-first} binary on Windows.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.zip`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Navigate to the Download {OCP} page on the Red Hat Customer Portal.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v Windows Client* entry and save the file.
. Extract the archive with a ZIP program.

. Move the `oc` binary to a directory that is on your `PATH` variable.
+
To check your `PATH` variable, open the command prompt and execute the following command:
+
[source,terminal]
----
C:\> path
----

.Verification

* After you install the OpenShift CLI, it is available using the `oc` command:
+
[source,terminal]
----
C:\> oc <command>
----

// Installing the OpenShift CLI on macOS
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installaing_aws/installing-aws-wavelength-zone.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adocs
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * updating/updating-restricted-network-cluster/mirroring-image-repository.adoc
// * microshift_cli_ref/microshift-oc-cli-install.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc
// * installing/installing-nutanix-installer-provisioned.adoc
// * installing/installing-restricted-networks-nutanix-installer-provisioned.adoc
// * installing/installing_ibm_powervc/installing-ibm-powervc-installer-custom.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * installing/installing_vsphere/ipi/ipi-vsphere-preparing-to-install.adoc
// * installing/installing_vsphere/upi/upi-vsphere-preparing-to-install.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc
// AMQ docs link to this; do not change anchor

[id="cli-installing-cli-macos_{context}"]
= Installing the OpenShift CLI on macOS

[role="_abstract"]
To manage your cluster and deploy applications from the command line, install the {oc-first} binary on macOS.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.
If you are updating a cluster in a disconnected environment, install the `oc` version that you plan to update to.
====

[NOTE]
====
OpenShift Container Platform version numbering matches {OCP} version numbering. Use the `oc` binary that matches your {microshift-short} version and has the appropriate RHEL compatibility.
====

.Procedure

. Navigate to https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/ and choose the folder for your operating system and architecture.
. Download `oc.tar.gz`.
. Navigate to the Download OpenShift Container Platform page on the Red{nbsp}Hat Customer Portal.

. Select the architecture from the *Product Variant* list.

. Select the appropriate version from the *Version* list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.
+
[NOTE]
====
For macOS arm64, choose the *OpenShift v macOS arm64 Client* entry.
====
. Navigate to the Download {OCP} on the Red{nbsp}Hat Customer Portal.
. Select the appropriate version from the *Version* drop-down list.

. Click *Download Now* next to the *OpenShift v macOS Clients* entry and save the file.

. Unpack and unzip the archive.

. Move the `oc` binary to a directory on your `PATH` variable.
+
To check your `PATH` variable, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

.Verification

* Verify your installation by using an `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Installing the CLI by using the web console

[id="cli-installing-cli-web-console_{context}"]
= Installing the OpenShift CLI by using the web console

You can install the {oc-first} to interact with OpenShift Container Platform clusters from a web console. You can install `oc` on Linux, Windows, or macOS.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all
of the commands in
OpenShift Container Platform .
OpenShift Container Platform.
Download and
install the new version of `oc`.
If you are upgrading a cluster in a restricted network, install the `oc` version that you plan to upgrade to.
====

// Installing the CLI on Linux by using the web console

[id="cli-installing-cli-web-console-macos-linux_{context}"]
= Installing the OpenShift CLI on Linux using the web console

You can install the OpenShift CLI (`oc`) binary on Linux by using the following procedure.

.Procedure
. From the web console, click *?*.
+
image::click-question-mark.png[]
. Click *Command Line Tools*.
+
image::CLI-list.png[]
. Select appropriate `oc` binary for your Linux platform, and then click *Download oc for Linux*.

. Save the file.
. Unpack the archive.

. Download the latest version of the `oc` CLI for your operating system from the *Downloads* page on {cluster-manager}.

. Extract the `oc` binary file from the downloaded archive.
+
[source,terminal]
----
$ tar xvf <file>
----
. Move the `oc` binary to a directory that is on your `PATH`.
+
To check your `PATH`, execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

After you install the OpenShift CLI, it is available using the `oc` command:

[source,terminal]
----
$ oc <command>
----

// Installing the CLI on Windows by using the web console

[id="cli-installing-cli-web-console-macos-windows_{context}"]
= Installing the OpenShift CLI on Windows using the web console

You can install the OpenShift CLI (`oc`) binary on Windows by using the following procedure.

.Procedure
. From the web console, click *?*.
+
image::click-question-mark.png[]
. Click *Command Line Tools*.
+
image::CLI-list.png[]
. Select the `oc` binary for Windows platform, and then click *Download oc for Windows for x86_64*.
. Save the file.
. Unzip the archive with a ZIP program.
. Download the latest version of the `oc` CLI for your operating system from the *Downloads* page on {cluster-manager}.

. Extract the `oc` binary file from the downloaded archive.

. Move the `oc` binary to a directory that is on your `PATH`.
+
To check your `PATH`, open the command prompt and execute the following command:
+
[source,terminal]
----
C:\> path
----

After you install the OpenShift CLI, it is available using the `oc` command:

[source,terminal]
----
C:\> oc <command>
----

// Installing the CLI on macOS by using the web console
[id="cli-installing-cli-web-console-macos_{context}"]
= Installing the OpenShift CLI on macOS using the web console

You can install the OpenShift CLI (`oc`) binary on macOS by using the following procedure.

.Procedure
. From the web console, click *?*.
+
image::click-question-mark.png[]
. Click *Command Line Tools*.
+
image::CLI-list.png[]
. Select the `oc` binary for macOS platform, and then click *Download oc for Mac for x86_64*.
+
[NOTE]
====
For macOS arm64, click *Download oc for Mac for ARM 64*.
====

. Save the file.
. Unpack and unzip the archive.
. Download the latest version of the `oc` CLI for your operating system from the *Downloads* page on {cluster-manager}.

. Extract the `oc` binary file from the downloaded archive.
. Move the `oc` binary to a directory on your PATH.
+
To check your `PATH`, open a terminal and execute the following command:
+
[source,terminal]
----
$ echo $PATH
----

After you install the OpenShift CLI, it is available using the `oc` command:

[source,terminal]
----
$ oc <command>
----

// Installing the CLI by using an RPM
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * microshift_cli_ref/microshift_oc_cli_install.adoc

[id="cli-installing-cli-rpm_{context}"]
= Installing the OpenShift CLI by using an RPM

[role="_abstract"]
For {op-system-base-full}, you can install the {oc-first} as an RPM if you have an active OpenShift Container Platform subscription on your Red Hat account.

[IMPORTANT]
====
You must install `oc` for {op-system-base} 9 by downloading the binary. Installing `oc` by using an RPM package is not supported on {op-system-base-full} 9.
====

.Prerequisites

* You must have root or sudo privileges.

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
# subscription-manager list --available --matches '*OpenShift*'
----

. In the output for the previous command, find the pool ID for
an OpenShift Container Platform
a ROSA
subscription and attach the subscription to the registered system:
+
[source,terminal]
----
# subscription-manager attach --pool=<pool_id>
----

. Enable the repositories required by
OpenShift Container Platform .
ROSA.
+
[source,terminal,subs="attributes+"]
----
# subscription-manager repos --enable="rhocp--for-rhel-8-x86_64-rpms"
----

. Install the `openshift-clients` package:
+
[source,terminal]
----
# yum install openshift-clients
----

.Verification

* Verify your installation by using an `oc` command:
+
[source,terminal]
----
$ oc <command>
----

// Installing the CLI by using Homebrew
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * microshift_cli_ref/microshift_oc_cli_install.adoc

[id="cli-installing-cli-brew_{context}"]
= Installing the OpenShift CLI by using Homebrew

[role="_abstract"]
For macOS, you can install the OpenShift CLI (`oc`) by using the Homebrew package manager.

.Prerequisites

* You must have Homebrew (`brew`) installed.

.Procedure

* Install the openshift-cli package by running the following command:
+
[source,terminal]
----
$ brew install openshift-cli
----

.Verification

* Verify your installation by using an `oc` command:

[source,terminal]
----
$ oc <command>
----

// Logging in to the CLI
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-logging-in_{context}"]
= Logging in to the OpenShift CLI

You can log in to the OpenShift CLI (`oc`) to access and manage your cluster.

.Prerequisites

* You must have access to a OpenShift Container Platform cluster.
* The {oc-first} is installed.

[NOTE]
====
To access a cluster that is accessible only over an HTTP proxy server, you can set the `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` variables.
These environment variables are respected by the `oc` CLI so that all communication with the cluster goes through the HTTP proxy.

Authentication headers are sent only when using HTTPS transport.
====

.Procedure

. Enter the `oc login` command and pass in a user name:
+
[source,terminal]
----
$ oc login -u user1
----

. When prompted, enter the required information:
+
.Example output
[source,terminal]
----
Server [https://localhost:8443]: https://openshift.example.com:6443 <1>
The server uses a certificate signed by an unknown authority.
You can bypass the certificate check, but any data you send to the server could be intercepted by others.
Use insecure connections? (y/n): y <2>

Authentication required for https://openshift.example.com:6443 (openshift)
Username: user1
Password: <3>
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>

Welcome! See 'oc help' to get started.
----
<1> Enter the OpenShift Container Platform server URL.
<2> Enter whether to use insecure connections.
<3> Enter the user's password.

[NOTE]
====
If you are logged in to the web console, you can generate an `oc login` command that includes your token and server information. You can use the command to log in to the
OpenShift CLI (`oc`) without the interactive prompts. To generate the command, select *Copy login command* from the username drop-down menu at the top right of the web console.
====

You can now create a project or issue other commands for managing your cluster.

// Logging in to the CLI by using the web
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-logging-in-web_{context}"]
= Logging in to the OpenShift CLI using a web browser

You can log in to the OpenShift CLI (`oc`) with the help of a web browser to access and manage your cluster. This allows users to avoid inserting their access token into the command line.

[WARNING]
====
Logging in to the CLI through the web browser runs a server on localhost with HTTP, not HTTPS; use with caution on multi-user workstations.
====

.Prerequisites

* You must have access to an OpenShift Container Platform cluster.
* You must have installed the OpenShift CLI (`oc`).
* You must have a browser installed.

.Procedure

. Enter the `oc login` command with the `--web` flag:
+
[source,terminal]
----
$ oc login <cluster_url> --web <1>
----
<1> Optionally, you can specify the server URL and callback port. For example, `oc login <cluster_url> --web --callback-port 8280 localhost:8443`.

. The web browser opens automatically. If it does not, click the link in the command output. If you do not specify the OpenShift Container Platform server `oc` tries to open the web console of the cluster specified in the current `oc` configuration file. If no `oc` configuration exists, `oc` prompts interactively for the server URL.
+
.Example output

[source,terminal]
----
Opening login URL in the default browser: https://openshift.example.com
Opening in existing browser session.
----

. If more than one identity provider is available, select your choice from the options provided.

. Enter your username and password into the corresponding browser fields. After you are logged in, the browser displays the text `access token received successfully; please return to your terminal`.

. Check the CLI for a login confirmation.
+
.Example output

[source,terminal]
----
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>

----

[NOTE]
====
The web console defaults to the profile used in the previous session. To switch between Administrator and Developer profiles, log out of the OpenShift Container Platform web console and clear the cache.
====

You can now create a project or issue other commands for managing your cluster.

// Using the CLI
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-using-cli_{context}"]
= Using the OpenShift CLI

Review the following sections to learn how to complete common tasks using the CLI.

== Creating a project

Use the `oc new-project` command to create a new project.

[source,terminal]
----
$ oc new-project my-project
----

.Example output
[source,terminal]
----
Now using project "my-project" on server "https://openshift.example.com:6443".
----

== Creating a new app

Use the `oc new-app` command to create a new application.

[source,terminal]
----
$ oc new-app https://github.com/sclorg/cakephp-ex
----

.Example output
[source,terminal]
----
--> Found image 40de956 (9 days old) in imagestream "openshift/php" under tag "7.2" for "php"

...

    Run 'oc status' to view your app.
----

== Viewing pods

Use the `oc get pods` command to view the pods for the current project.

[NOTE]
====
When you run `oc` inside a pod and do not specify a namespace, the namespace of the pod is used by default.
====

[source,terminal]
----
$ oc get pods -o wide
----

.Example output
[source,terminal]
----
NAME                  READY   STATUS      RESTARTS   AGE     IP            NODE                           NOMINATED NODE
cakephp-ex-1-build    0/1     Completed   0          5m45s   10.131.0.10   ip-10-0-141-74.ec2.internal    <none>
cakephp-ex-1-deploy   0/1     Completed   0          3m44s   10.129.2.9    ip-10-0-147-65.ec2.internal    <none>
cakephp-ex-1-ktz97    1/1     Running     0          3m33s   10.128.2.11   ip-10-0-168-105.ec2.internal   <none>
----

== Viewing pod logs

Use the `oc logs` command to view logs for a particular pod.

[source,terminal]
----
$ oc logs cakephp-ex-1-deploy
----

.Example output
[source,terminal]
----
--> Scaling cakephp-ex-1 to 1
--> Success
----

== Viewing the current project

Use the `oc project` command to view the current project.

[source,terminal]
----
$ oc project
----

.Example output
[source,terminal]
----
Using project "my-project" on server "https://openshift.example.com:6443".
----

== Viewing the status for the current project

Use the `oc status` command to view information about the current project, such
as services, deployments, and build configs.

[source,terminal]
----
$ oc status
----

.Example output
[source,terminal]
----
In project my-project on server https://openshift.example.com:6443

svc/cakephp-ex - 172.30.236.80 ports 8080, 8443
  dc/cakephp-ex deploys istag/cakephp-ex:latest <-
    bc/cakephp-ex source builds https://github.com/sclorg/cakephp-ex on openshift/php:7.2
    deployment #1 deployed 2 minutes ago - 1 pod

3 infos identified, use 'oc status --suggest' to see details.
----

== Listing supported API resources

Use the `oc api-resources` command to view the list of supported API resources
on the server.

[source,terminal]
----
$ oc api-resources
----

.Example output
[source,terminal]
----
NAME                                  SHORTNAMES       APIGROUP                              NAMESPACED   KIND
bindings                                                                                     true         Binding
componentstatuses                     cs                                                     false        ComponentStatus
configmaps                            cm                                                     true         ConfigMap
...
----

// Getting help
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-getting-help_{context}"]
= Getting help

You can get help with CLI commands and OpenShift Container Platform
resources in the following ways:

* Use `oc help` to get a list and description of all available CLI commands:
+
.Example: Get general help for the CLI
[source,terminal]
----
$ oc help
----
+
.Example output
[source,terminal]
----
OpenShift Client

This client helps you develop, build, deploy, and run your applications on any OpenShift or Kubernetes compatible
platform. It also includes the administrative commands for managing a cluster under the 'adm' subcommand.

Usage:
  oc [flags]

Basic Commands:
  login           Log in to a server
  new-project     Request a new project
  new-app         Create a new application

...
----

* Use the `--help` flag to get help about a specific CLI command:
+
.Example: Get help for the `oc create` command
[source,terminal]
----
$ oc create --help
----
+
.Example output
[source,terminal]
----
Create a resource by filename or stdin

JSON and YAML formats are accepted.

Usage:
  oc create -f FILENAME [flags]

...
----

* Use the `oc explain` command to view the description and fields for a
particular resource:
+
.Example: View documentation for the `Pod` resource
[source,terminal]
----
$ oc explain pods
----
+
.Example output
[source,terminal]
----
KIND:     Pod
VERSION:  v1

DESCRIPTION:
     Pod is a collection of containers that can run on a host. This resource is
     created by clients and scheduled onto hosts.

FIELDS:
   apiVersion	<string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

...
----

// Logging out of the CLI
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-logging-out_{context}"]
= Logging out of the OpenShift CLI

You can log out the OpenShift CLI to end your current session.

* Use the `oc logout` command.
+
[source,terminal]
----
$ oc logout
----
+
.Example output
[source,terminal]
----
Logged "user1" out on "https://openshift.example.com"
----

This deletes the saved authentication token from the server and removes it from
your configuration file.
