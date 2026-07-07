---
title: "Using the Cluster Samples Operator with an alternate registry"
type: reference
domain: openshift
slug: openshift-images-4-22-samples-operator-alt-registry
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/samples-operator-alt-registry
version: 4.22
family: openshift_images
documentKind: "Documentation"
---

# Using the Cluster Samples Operator with an alternate registry

[id="samples-operator-alt-registry"]
= Using the Cluster Samples Operator with an alternate registry

[role="_abstract"]
You can use the Cluster Samples Operator with an alternate registry by preparing a mirror host and creating a mirror registry.

// Module included in the following assemblies:
//
// * installing/disconnected_install/installing-mirroring-installation-images.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * scalability_and_performance/ztp-deploying-disconnected.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc

[id="installation-about-mirror-registry_{context}"]
= About the mirror registry

[role="_abstract"]
You must have access to the internet to obtain the necessary container images. Using an alternative registry means that you place the mirror registry on a mirror host that has access to both your network and the internet.

You can mirror the images that are required for OpenShift Container Platform installation and subsequent product updates to a container mirror registry such as {quay}, JFrog Artifactory, Sonatype Nexus Repository, or Harbor. If you do not have access to a large-scale container registry, you can use the _mirror registry for Red{nbsp}Hat OpenShift_, a small-scale container registry included with OpenShift Container Platform subscriptions.

You can use any container registry that supports Docker v2-2, such as {quay}, the _mirror registry for Red{nbsp}Hat OpenShift_, Artifactory, Sonatype Nexus Repository, or Harbor. Regardless of your chosen registry, the procedure to mirror content from Red Hat hosted sites on the internet to an isolated image registry is the same. After you mirror the content, you configure each cluster to retrieve this content from your mirror registry.
You can mirror the images that are required for OpenShift Container Platform installation and subsequent product updates to a container mirror registry that supports Docker v2-2, such as {quay}. If you do not have access to a large-scale container registry, you can use the _mirror registry for Red{nbsp}Hat OpenShift_, which is a small-scale container registry included with OpenShift Container Platform subscriptions.

Regardless of your chosen registry, the procedure to mirror content from Red Hat hosted sites on the internet to an isolated image registry is the same. After you mirror the content, you configure each cluster to retrieve this content from your mirror registry.

[IMPORTANT]
====
The {product-registry} cannot be used as the target registry because it does not support pushing without a tag, which is required during the mirroring process.
====

If choosing a container registry that is not the _mirror registry for Red{nbsp}Hat OpenShift_, it must be reachable by every machine in the clusters that you provision. If the registry is unreachable, installation, updating, or normal operations such as workload relocation might fail. For that reason, you must run mirror registries in a highly available way, and the mirror registries must at least match the production availability of your OpenShift Container Platform clusters.

When you populate your mirror registry with OpenShift Container Platform images, you can follow two scenarios. If you have a host that can access both the internet and your mirror registry, but not your cluster nodes, you can directly mirror the content from that machine. This process is referred to as _connected mirroring_. If you have no such host, you must mirror the images to a file system and then bring that host or removable media into your restricted environment. This process is referred to as _disconnected mirroring_.

For mirrored registries, to view the source of pulled images, you must review the `Trying to access` log entry in the CRI-O logs. Other methods to view the image pull source, such as using the `crictl images` command on a node, show the non-mirrored image name, even though the image is pulled from the mirrored location.

[NOTE]
====
Red{nbsp}Hat does not test third party registries with OpenShift Container Platform.
====

//Incorrect rendering of ROSA attributes discovered during Pruning HCP task. I believe some of the following content is not correct for managed OpenShift. I have created JIRA issue to investigate further.

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

// Module included in the following assemblies:
//
// * installing/disconnected_install/installing-mirroring-installation-images.adoc
// * installing/disconnected_install/installing-mirroring-disconnected.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc

[id="installation-adding-registry-pull-secret_{context}"]
= Configuring credentials that allow images to be mirrored

[role="_abstract"]
Create a container image registry credentials file so that you can mirror images from Red{nbsp}Hat to your mirror. Complete the following steps on the installation host.

[WARNING]
====
Do not use this image registry credentials file as the pull secret when you install a cluster. If you provide this file when you install cluster, all of the machines in the cluster will have write access to your mirror registry.
====

// removed this warning since the first part is more of a prereq, and the second part seems to just describe what will happen later in the procedure. Can revert/modify as needed.

.Prerequisites
* You configured a mirror registry to use in your disconnected environment.
* You configured a mirror registry to use.
* You identified an image repository location on your mirror registry to mirror images into.
* You provisioned a mirror registry account that allows images to be uploaded to that image repository.
* You have write access to the mirror registry.

.Procedure
. Download your `registry.redhat.io` {cluster-manager-url-pull}.

. Make a copy of your pull secret in JSON format by running the following command:
+
[source,terminal]
----
$ cat ./pull-secret | jq . > <path>/<pull_secret_file_in_json>
----
+
Specify the path to the directory to store the pull secret in and a name for the JSON file that you create.
+
.Example pull secret
[source,json]
----
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
----
+
. Save the file as either `~/.docker/config.json` or `$XDG_RUNTIME_DIR/containers/auth.json`:
+
// An additional step for following this procedure when using oc-mirror as part of the disconnected install process.

.. If the `.docker` or `$XDG_RUNTIME_DIR/containers` directories do not exist, create one by entering the following command:
+
[source,terminal]
----
$ mkdir -p <directory_name>
----
+
Where `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`.

.. Copy the pull secret to the appropriate directory by entering the following command:
+
[source,terminal]
----
$ cp <path>/<pull_secret_file_in_json> <directory_name>/<auth_file>
----
+
The `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`, and `<auth_file>` is either `config.json` or `auth.json`

. Optional: If using the oc-mirror plugin, save the file as either `~/.docker/config.json` or `$XDG_RUNTIME_DIR/containers/auth.json`:
+
// Similar to the additional step above, except it is framed as optional because it is included in a disconnected update page (where users may or may not use oc-mirror for their process)

** If the `.docker` or `$XDG_RUNTIME_DIR/containers` directories do not exist, create one by entering the following command:
+
[source,terminal]
----
$ mkdir -p <directory_name>
----
+
Where `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`.

** Copy the pull secret to the appropriate directory by entering the following command:
+
[source,terminal]
----
$ cp <path>/<pull_secret_file_in_json> <directory_name>/<auth_file>
----
+
Where `<directory_name>` is either `~/.docker` or `$XDG_RUNTIME_DIR/containers`, and `<auth_file>` is either `config.json` or `auth.json`.

. If the `$XDG_RUNTIME_DIR/containers` directory does not exist, create one by entering the following command:
+
[source,terminal]
----
$ mkdir -p $XDG_RUNTIME_DIR/containers
----
+
// Additional step for allowing this procedure for oc-mirror-v2
+
// Should this step below also have the "if you don't have this directory, create it using this command" substeps?

. Save the pull secret file as `$XDG_RUNTIME_DIR/containers/auth.json`.

. Generate the base64-encoded user name and password or token for your mirror registry by running the following command:
+
[source,terminal]
----
$ echo -n '<user_name>:<password>' | base64 -w0
----
For `<user_name>` and `<password>`, specify the user name and password that you configured for your registry.
+
.Example output
[source,terminal]
----
BGVtbYk3ZHAtqXs=
----

. Create a `.json` file and add a section that describes your registry to it:
+
[source,json]
----
{
  "auths": {
    "<mirror_registry>": {
      "auth": "<credentials>",
      "email": "you@example.com"
    }
  }
}
----
+
* For the `<mirror_registry>` value, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:8443`.
+
* For the `<credentials>` value, specify the base64-encoded user name and password for the mirror registry.

. Edit the JSON file and add a section that describes your registry to it:
+
[source,json]
----
  "auths": {
    "<mirror_registry>": {
      "auth": "<credentials>",
      "email": "you@example.com"
    }
  },
----
+
* For the `<mirror_registry>` value, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:8443`.
+
* For the `<credentials>` value, specify the base64-encoded user name and password for the mirror registry.
+
.Example modified pull secret
[source,json]
----
{
  "auths": {
    "registry.example.com": {
      "auth": "BGVtbYk3ZHAtqXs=",
      "email": "you@example.com"
    },
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
----

This is not currently working as intended.
. Log in to your registry by using the following command:
+
[source,terminal]
----
$ oc registry login --to ./pull-secret.json --registry "<registry_host_and_port>" --auth-basic=<username>:<password>
----
+
Provide both the registry details and a valid user name and password for the registry.

// Module included in the following assemblies:
//
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc

[id="installation-mirror-repository_{context}"]
= Mirroring the OpenShift Container Platform image repository

[role="_abstract"]
Mirror the OpenShift Container Platform image repository to your registry to use during cluster installation or upgrade. Complete the following steps on the mirror host.

// Note to CQA assignee: this deprecation notice is in 4.22+ docs, this should not be backported to 4.20 and 4.21 docs while cherry picking CQAs.

.Prerequisites

* Your mirror host has access to the internet.
* You configured a mirror registry to use in your restricted network and
can access the certificate and credentials that you configured.
* You configured a mirror registry to use.
* You downloaded the {cluster-manager-url-pull} and modified it to include authentication to your mirror repository.
* You have created a pull secret for your mirror repository.
* If you use self-signed certificates, you have specified a Subject Alternative Name in the certificates.

.Procedure

. Review the
Download OpenShift Container Platform page to determine the version of OpenShift Container Platform that you want to install and determine the corresponding tag on the Repository Tags page.
OpenShift Container Platform releases page
to determine the version and tag of OpenShift Container Platform that you want to install.

. Set the following required environment variables:

.. Export the release version:
+
[source,terminal]
----
$ OCP_RELEASE=<release_version>
----
+
For `<release_version>`, specify the tag that corresponds to the version of OpenShift Container Platform to install, such as `4.21.1`.

.. Export the local registry name and host port:
+
[source,terminal]
----
$ LOCAL_REGISTRY='<local_registry_host_name>:<local_registry_host_port>'
----
+
For `<local_registry_host_name>`, specify the registry domain name for your mirror repository, and for `<local_registry_host_port>`, specify the port that it serves content on.

.. Export the local repository name:
+
[source,terminal]
----
$ LOCAL_REPOSITORY='<local_repository_name>'
----
+
For `<local_repository_name>`, specify the name of the repository to create in your registry, such as `ocp4/openshift4`.

.. Export the name of the repository to mirror:
+
[source,terminal]
----
$ PRODUCT_REPO='openshift-release-dev'
----
+
For a production release, you must specify `openshift-release-dev`.
[source,terminal]
----
$ PRODUCT_REPO='okd'
----

.. Export the path to your registry pull secret:
+
[source,terminal]
----
$ LOCAL_SECRET_JSON='<path_to_pull_secret>'
----
+
For `<path_to_pull_secret>`, specify the absolute path to and file name of the pull secret for your mirror registry that you created.

.. Export the release mirror:
+
[source,terminal]
----
$ RELEASE_NAME="ocp-release"
----
+
For a production release, you must specify `ocp-release`.
[source,terminal]
----
$ RELEASE_NAME="scos-release"
----

.. Export the type of architecture for your cluster:
+
[source,terminal]
----
$ ARCHITECTURE=<cluster_architecture>
----
+
Specify the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.

.. Export the path to the directory to host the mirrored images:
+
[source,terminal]
----
$ REMOVABLE_MEDIA_PATH=<path>
----
+
Specify the full path, including the initial forward slash (/) character.

. Mirror the version images to the mirror registry:
** If your mirror host does not have internet access, take the following actions:
... Connect the removable media to a system that is connected to the internet.
... Review the images and configuration manifests to mirror:
+
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE} --dry-run
----
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE} --dry-run
----

... Record the entire `imageContentSources` section from the output of the previous
command. The information about your mirrors is unique to your mirrored repository, and you must add the `imageContentSources` section to the `install-config.yaml` file during installation.
... Mirror the images to a directory on the removable media:
+
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON} --to-dir=${REMOVABLE_MEDIA_PATH}/mirror quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}
----
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON} --to-dir=${REMOVABLE_MEDIA_PATH}/mirror quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE}
----

... Take the media to the restricted network environment and upload the images to the local container registry.
+
[source,terminal]
----
$ oc image mirror -a ${LOCAL_SECRET_JSON} --from-dir=${REMOVABLE_MEDIA_PATH}/mirror "file://openshift/release:${OCP_RELEASE}*" ${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}
----
+
For the `REMOVABLE_MEDIA_PATH` variable, you must use the same path that you specified when you mirrored the images.
+
[IMPORTANT]
====
Running the `oc image mirror` command might result in the following error: `error: unable to retrieve source image`. This error occurs when image indexes include references to images that no longer exist on the image registry. Image indexes might retain older references to allow users running those images an upgrade path to newer points on the upgrade graph. As a temporary workaround, you can use the `--skip-missing` option to bypass the error and continue downloading the image index. For more information, see Service Mesh Operator mirroring failed.
====

** If the local container registry is connected to the mirror host, take the following actions:
... Directly push the release images to the local registry by using following command:
+
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}
----
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}
----
+
This command pulls the release information as a digest, and its output includes the `imageContentSources` data that you require when you install your cluster.

... Record the entire `imageContentSources` section from the output of the previous
command. The information about your mirrors is unique to your mirrored repository, and you must add the `imageContentSources` section to the `install-config.yaml` file during installation.
+
[NOTE]
====
The image name gets patched to Quay.io during the mirroring process, and the Podman images will show Quay.io in the registry on the bootstrap virtual machine.
====

. To create the installation program that is based on the content that you
mirrored, extract it and pin it to the release:
** If your mirror host does not have internet access, run the following command:
+
[source,terminal]
----
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --icsp-file=<file> --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}" \
--insecure=true
----
+
Optional: If you do not want to configure trust for the target registry, add the `--insecure=true` flag.

** If the local container registry is connected to the mirror host, run the following command:
+
[source,terminal]
----
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}"
----
[source,terminal]
----
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}"
----
+
[IMPORTANT]
====
To ensure that you use the correct images for the version of OpenShift Container Platform that you selected, you must extract the installation program from the mirrored content.

You must perform this step on a machine with an active internet connection.
====

. For clusters using installer-provisioned infrastructure, run the following command:
+
[source,terminal]
----
$ openshift-install
----

. Mirror the version images to the mirror registry:

.. Directly push the release images to the local registry by using following command:
+
[source,terminal]
----
$ oc adm release mirror -a ${LOCAL_SECRET_JSON}  \
     --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} \
     --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} \
     --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}
----
+
This command pulls the release information as a digest, and its output includes the `imageContentSources` data that you require when you install your cluster.

.. Record the entire `imageContentSources` section from the output of the previous command. The information about your mirrors is unique to your mirrored repository, and you must add the `imageContentSources` section to the `install-config.yaml` file during installation.
+
[NOTE]
====
The image name gets patched to Quay.io during the mirroring process, and the Podman images show `quay.io` in the registry on the bootstrap virtual machine.
====

. To create the installation program that is based on the content that you mirrored, extract it and pin it to the release by running the following command:
+
[source,terminal]
----
$ oc adm release extract -a ${LOCAL_SECRET_JSON} --command=openshift-install "${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}"
----
+
[IMPORTANT]
====
To ensure that you use the correct images for the version of OpenShift Container Platform that you selected, you must extract the installation program from the mirrored content.

You must perform this step on a machine with an active internet connection.
====

. For clusters using installer-provisioned infrastructure, run the following command:
+
[source,terminal]
----
$ openshift-install
----

// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * openshift_images/samples-operator-alt-registry.adoc

[id="installation-restricted-network-samples_{context}"]
= Using Cluster Samples Operator image streams with alternate or mirrored registries

[role="_abstract"]
You can use an alternate or mirror registry to host your images streams instead of using the Red{nbsp}Hat registry.

Most image streams in the `openshift` namespace managed by the Cluster Samples Operator point to images located in the Red{nbsp}Hat registry at registry.redhat.io.
Mirroring does not apply to these image streams.

[NOTE]
====
The `cli`, `installer`, `must-gather`, and `tests` image streams, while part of the install payload, are not managed by the Cluster Samples Operator. These are not addressed in this procedure.
====

[IMPORTANT]
====
The Cluster Samples Operator must be set to `Managed` in a disconnected environment. To install the image streams, you must have a mirrored registry.
====

.Prerequisites
* Access to the cluster as a user with the `cluster-admin` role.
* Access to the cluster as a user with the `dedicated-admin` role.
* Create a pull secret for your mirror registry.

.Procedure

. Access the images of a specific image stream to mirror, for example:
+
[source,terminal]
----
$ oc get is <imagestream> -n openshift -o json | jq .spec.tags[].from.name | grep registry.redhat.io
----
+
. Mirror images from registry.redhat.io associated with any image streams you need
in the restricted network environment into one of the defined mirrors, for example:
into your defined preferred registry, for example:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/rhscl/ruby-25-rhel7:latest ${MIRROR_ADDR}/rhscl/ruby-25-rhel7:latest
----

. Create the image configuration object for the cluster by running the following command:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
----

. Add the required trusted CAs for the mirror in the image configuration object:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
----

. Update the `samplesRegistry` field in the Cluster Samples Operator configuration object to contain the `hostname` portion of the mirror location defined in the mirror configuration:
+
[source,terminal]
----
$ oc edit configs.samples.operator.openshift.io -n openshift-cluster-samples-operator
----
+
[IMPORTANT]
====
This step is required because the image stream import process does not use the mirror or search mechanism at this time.
====

. Add any image streams that are not mirrored into the `skippedImagestreams` field of the Cluster Samples Operator configuration object. Or if you do not want to support any of the sample image streams, set the Cluster Samples Operator to `Removed` in the Cluster Samples Operator configuration object.
+
[NOTE]
====
The Cluster Samples Operator issues alerts if image stream imports are failing but the Cluster Samples Operator is either periodically retrying or does not appear to be retrying them.
====
+
Many of the templates in the `openshift` namespace reference the image streams. You can use `Removed` to purge both the image streams and templates. This eliminates the possibility of attempts to use the templates if they are not functional because of any missing image streams.

// Module included in the following assemblies:
//
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * openshift_images/configuring-samples-operator.adoc

[id="installation-images-samples-disconnected-mirroring-assist_{context}"]
= Cluster Samples Operator assistance for mirroring

[role="_abstract"]
During installation, OpenShift Container Platform creates a config map named `imagestreamtag-to-image` in the `openshift-cluster-samples-operator` namespace.

The `imagestreamtag-to-image` config map contains an entry, the populating image, for each image stream tag.

The format of the key for each entry in the data field in the config map is `<image_stream_name>_<image_stream_tag_name>`.

During a disconnected installation of OpenShift Container Platform, the status of the Cluster Samples Operator is set to `Removed`. If you choose to change it to `Managed`, it installs samples.

[NOTE]
====
The use of samples in a network-restricted or discontinued environment might require access to services external to your network. Some example services include: Github, Maven Central, npm, RubyGems, PyPi and others. There might be additional steps to take that allow the Cluster Samples Operators objects to reach the services they require.
====

Use the following principles to determine which images you need to mirror for your image streams to import:

* While the Cluster Samples Operator is set to `Removed`, you can create your mirrored registry, or determine which existing mirrored registry you want to use.
* Mirror the samples you want to the mirrored registry using the new config map as your guide.
* Add any of the image streams you did not mirror to the `skippedImagestreams` list of the Cluster Samples Operator configuration object.
* Set `samplesRegistry` of the Cluster Samples Operator configuration object to the mirrored registry.
* Then set the Cluster Samples Operator to `Managed` to install the image streams you have mirrored.

[id="additional-resources_samples-operator-alt-registry"]
[role="_additional-resources"]
== Additional resources

* Viewing the image pull source
* Using Cluster Samples Operator image streams with alternate or mirrored registries
