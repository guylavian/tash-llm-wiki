---
title: "Using Kickstart files for installing {microshift-short} in {op-system-base}"
type: reference
domain: openshift
slug: microshift-install-kickstarts-4-22-microshift-rhel-kickstarts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_kickstarts/microshift-rhel-kickstarts
version: 4.22
family: microshift_install_kickstarts
documentKind: "Documentation"
---

# Using Kickstart files for installing {microshift-short} in {op-system-base}

[id="microshift-rhel-kickstarts"]
= Using Kickstart files for installing {microshift-short} in {op-system-base}

[role="_abstract"]
Use a Kickstart file that automates the installation of an {op-system-base} image with {microshift-short}.

// Module included in the following assemblies:
//
// microshift/microshift-install-kickstarts.adoc

[id="microshift-rhel-kickstart_{context}"]
= Kickstart files for embedding {microshift-short} with a {op-system-base} installation

By using a Kickstart file, you automate a typical {op-system-base-full} installation by creating a single file containing all of the information required for success.

* You can also automate your {microshift-short} installation by including {microshift-short} in the Kickstart file for the {op-system-base} type that you choose.
* You can use a Kickstart file to provision virtual machines (VMs) or to complete a regular {op-system-base} installation for deployment on edge devices.

For {microshift-short}, your Kickstart file must include information to provision the {op-system-base} system to meet the following requirements:

* A {op-system-base} system you provision must meet the requirements for installing {microshift-short}.
* The {op-system-base} file system must have a logical volume manager (LVM) volume group (VG) with sufficient capacity for the persistent volumes (PVs) of your workload.
* A pull secret from the https://console.redhat.com/openshift/install/pull-secret[Red Hat Hybrid Cloud Console] must be present as `/etc/crio/openshift-pull-secret` and have root user-only read/write permissions.

// Module included in the following assemblies:
//
// microshift/microshift-kickstart-prep.adoc

[id="microshift-kickstart-prep_{context}"]
= Setting up the {microshift-short} Kickstart file

You can use the Kickstart file provided with {microshift-short} to provision a host by following the instructions for your install type. The ISO you created in the previous steps then runs on the host that you provision with your Kickstart file. To get started with the {microshift-short} Kickstart file, begin with the following procedure.

.Prerequisites

* The host you are provisioning must meet the system requirements for installing {microshift-short}.
* A pull secret from `~/.pull-secret.json` must be present and have read permissions for the current user.

.Procedure

. Install the `microshift-release-info` RPM package containing the sample Kickstart files that are in the `/usr/share/microshift/kickstart` directory by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y microshift-release-info
----

. Install the utilities used during the Kickstart file creation by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y openssl gettext
----

. Set the variables pointing to secrets included in `kickstart.ks`.

* The `PULL_SECRET` file contents are copied to the `/etc/crio/openshift-pull-secret` directory at the post-installation stage to authenticate {ocp} container registry access.
+
.Example command setting the `PULL_SECRET` variable:
[source,terminal]
----
$ export PULL_SECRET="$(cat ~/.pull-secret.json)"
----

* Set a password in the `PASSWD_TEXT` variable to use in the`USER_PASSWD` setting by running the following command:
+
.Example command setting the `PASSWD_TEXT` variable.
[source,terminal,subs="+quotes"]
----
$ PASSWD_TEXT=_<redhat_user_plain_text_password>_ <1>
----
<1> Replace _<redhat_user_plain_text_password>_ with the password you want to use.

* The `USER_PASSWD` setting is used as an encrypted password for the `redhat` user for logging into the host. Encrypt your password string using the SHA-512 encryption standard.
+
.Example command setting the `USER_PASSWD` variable.
[source,terminal]
----
$ export USER_PASSWD="$(openssl passwd -6 "${PASSWD_TEXT}")"  # <1>
----
<1> Only the encrypted password is included in the Kickstart file. The plain text password is not.

.Next steps

* Follow the instructions for your installation type to create a working Kickstart file from the provided template. Instructions for RPM-based, {op-system-ostree}, and {op-system-image} installations follow this procedure.

* Optional. Create a virtual machine (VM) using the Kickstart file. Creating a VM allows you to test and validate the values in your Kickstart file.

// Module included in the following assemblies:
//
// microshift/microshift-kickstart-prep.adoc

[id="microshift-kickstart-rpm-install_{context}"]
= Creating a Kickstart file for a {microshift-short} RPM installation

Use the Kickstart file provided with {microshift-short} to provision an RPM-based virtual machine.

.Prerequisites

* You set up the {microshift-short} Kickstart file.
* You know the Activation Keys and organization ID to activate your Red{nbsp}Hat subscription.
* You have the information needed to set the `BOOTC_IMAGE_URL`, `AUTH_CONFIG`, and `REGISTRY_CONFIG` required variables.

[IMPORTANT]
====
The subscription must include access to the `rhocp-4.x-for-rhel-{op-system-version-major}-$(uname -m)-rpms` and `fast-datapath-for-rhel-{op-system-version-major}-$(uname -m)-rpms` RPM repositories.
====

.Procedure

. Add the following variables to create an RPM Kickstart file:
+
.Example commands setting the Kickstart file variables.
+
* The `RHSM_ORG` variable contains a Red{nbsp}Hat Subscription Manager organization ID for the subscription registration command in the Kickstart file.
+
[source,terminal]
----
$ export RHSM_ORG="$(cat ~/.rhsm-activation-org)"
----
+
* The `RHSM_KEY` variable contains a Red{nbsp}Hat Subscription Manager activation key for the subscription registration command in the Kickstart file.
+
[source,terminal]
----
$ export RHSM_KEY="$(cat ~/.rhsm-activation-key)"
----
+
* The `MICROSHIFT_VER` variable references the {microshift-short} version to install using the `4.y` format. The latest available `.z` version of the `4.y` version set in this variable is automatically installed.
+
[source,terminal]
----
$ export MICROSHIFT_VER= # <1>
----
<1> The latest `.z` of the minor version that you set is installed.

. Run the following command to create the `kickstart.ks` file to be used during the virtual machine installation:
+
[source,terminal]
----
envsubst < \
    /usr/share/microshift/kickstart/kickstart-rpm.ks.template > \
    "${HOME}/kickstart.ks"
----

// Module included in the following assemblies:
//
// microshift/microshift-.adoc

[id="microshift-kickstart-ostree-install_{context}"]
= Creating a Kickstart file for a {microshift-short} {op-system-ostree} installation

Use the Kickstart file provided with {microshift-short} to provision a {op-system-ostree}-based virtual machine.

.Prerequisites

* You set up the {microshift-short} Kickstart file.
* You have the information needed to set required and optional variables.

.Procedure

. Add the following required variables to create an {op-system-ostree} Kickstart file:
+
.Example commands setting required variables.
+
* The `OSTREE_SERVER_URL` variable contains an `rpm-ostree` server URL that is passed to the `ostreesetup` Kickstart command.
+
[source,terminal,subs="+quotes"]
----
$ export OSTREE_SERVER_URL="_<http://my_ostree_server_url>_" # <1>
----
<1> Replace _<http://my_ostree_server_url>_ with your server URL.
+
* The `OSTREE_COMMIT_REF` variable contains an `rpm-ostree` commit reference that is installed from the server.
+
[source,terminal,subs="+quotes"]
----
$ export OSTREE_COMMIT_REF="_<myostree_commit_reference>_" # <1>
----
<1> Replace _<myostree_commit_reference>_ with the `rpm-ostree` commit reference.

. Optional. Add the following variable for server authentication:
+
* The `AUTH_CONFIG` contents are copied to `/etc/ostree/auth.json` at the pre-install stage to authenticate access to the `OSTREE_SERVER_URL` server. If no server authentication is required, skip this setting.
+
[source,terminal]
----
$ export AUTH_CONFIG="$(cat ~/.ostree-auth.json)"
----

. Run the following command to create the `kickstart.ks` file to be used during the installation:
+
[source,terminal]
----
envsubst < \
    /usr/share/microshift/kickstart/kickstart-ostree.ks.template > \
    "${HOME}/kickstart.ks"
----

[NOTE]
====
The {microshift-short} version specified in the `rpm-ostree` commit is installed. To change the version of {microshift-short}, you must create a new commit.
====

// Module included in the following assemblies:
//
// microshift/microshift-.adoc

[id="microshift-kickstart-bootc-install_{context}"]
= Creating a Kickstart file for installing {microshift-short} on image mode for RHEL

You can use the Kickstart file provided with {microshift-short} for an image mode for RHEL installation.

.Prerequisites

* You set up the {microshift-short} Kickstart file.
* You have the information needed to set required and optional variables.

.Procedure

. Set the required `BOOTC_IMAGE_URL` variable value to point to an image used in the RHEL Kickstart file installation process by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ export BOOTC_IMAGE_URL=_<myregistry>/<myorg>/<mypath>_/microshift-image:tag # <1>
----
<1> Replace _<myregistry>_,_<myorg>_, and _<mypath>_ with your information.

* The `BOOTC_IMAGE_URL` variable contains a reference to the image that is installed with the `ostreecontainer` command. You can specify a z-stream release other than the latest by using the tag if required.

. Optional. Add variables and values for registry authentication and configuration by using the following commands:
+
.Example commands setting optional variables
+
* Set the `AUTH_CONFIG` variable to authenticate access to the `BOOTC_IMAGE_URL` image by running the following command:
+
[source,terminal]
----
$ export AUTH_CONFIG="$(cat ~/.quay-auth.json)" # <1>
----
<1> See the `containers-auth.json(5)` manual page for more information about this file format.
+
* Set the `REGISTRY_CONFIG` variable to configure access to the registry containing the `BOOTC_IMAGE_URL` image by running the following command:
+
[source,terminal]
----
$ export REGISTRY_CONFIG="$(cat ~/.quay-config.conf)" # <1>
----
<1> See the `containers-registries.conf(5)` manual page for more information about this file format.

. Create the `kickstart.ks` file to be used during the installation by running the following command:
+
[source,terminal]
----
envsubst < \
    /usr/share/microshift/kickstart/kickstart-bootc.ks.template > \
    "${HOME}/kickstart.ks"
----
