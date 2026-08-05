---
title: "Understanding image-based installation and deployment for {sno}"
type: reference
domain: openshift
slug: edge-computing-4-22-ibi-understanding-image-based-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ibi-understanding-image-based-install
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Understanding image-based installation and deployment for {sno}

[id="ibi-understanding-image-based-install"]
= Understanding image-based installation and deployment for {sno}

[role="_abstract"]
Image-based installations significantly reduce the deployment time of {sno} clusters by streamlining the installation process.

This approach enables the preinstallation of configured and validated instances of {sno} on target hosts. These preinstalled hosts can be rapidly reconfigured and deployed at the far edge of the network, including in disconnected environments, with minimal intervention.

[NOTE]
====
To deploy a managed cluster using an imaged-based approach in combination with {ztp-first}, you can use the SiteConfig operator.
====

[id="ibi-installation-deployment-overview_{context}"]
== Overview of image-based installation and deployment for {sno} clusters

Deploying infrastructure at the far edge of the network presents challenges for service providers with low bandwidth, high latency, and disconnected environments.
It is also costly and time-consuming to install and deploy {sno} clusters.

An image-based approach to installing and deploying {sno} clusters at the far edge of the network overcomes these challenges by separating the installation and deployment stages.

.Overview of an image-based installation and deployment for managed {sno} clusters
image::../images/711_OpenShift_IBI_Installation_high-level_0624.png[Overview of an image-based installation and deployment]

Imaged-based installation::
Preinstall multiple hosts with {sno} at a central site, such as a service depot or a factory.
Then, validate the base configuration for these hosts and leverage the image-based approach to perform reproducible factory installs at scale by using a single live installation ISO.

Image-based deployment::
Ship the preinstalled and validated hosts to a remote site and rapidly reconfigure and deploy the clusters in a matter of minutes by using a configuration ISO.

You can choose from two methods to preinstall and configure your SNO clusters.

Using the `openshift-install` program::
For a {sno} cluster, use the `openshift-install` program only to manually create the live installation ISO that is common to all hosts. Then, use the program again to create the configuration ISO which ensures that the host is unique. For more information, see “Deploying managed {sno} using the openshift-install program”.

Using the IBI Operator::
For managed {sno} clusters, you can use the `openshift-install` with the Image Based Install (IBI) Operator to scale up the operations. The program creates the live installation ISO and then the IBI Operator creates one configuration ISO for each host. For more information, see "Deploying {sno} using the IBI Operator".

// Module included in the following assemblies:
// * edge_computing/image_base_install/ibi-understanding-image-based-install.adoc

[id="ibi-image-based-installation-overview_{context}"]
= Image-based installation for {sno} clusters

[role="_abstract"]
Using the {lcao}, you can generate an OCI container image that encapsulates an instance of a {sno} cluster.

This image is derived from a dedicated cluster that you can configure with the target OpenShift Container Platform version.

You can reference this image in a live installation ISO to consistently preinstall configured and validated instances of {sno} to multiple hosts. This approach enables the preparation of hosts at a central location, for example in a factory or service depot, before shipping the preinstalled hosts to a remote site for rapid reconfiguration and deployment. The instructions for preinstalling a host are the same whether you deploy the host by using only the `openshift-install` program or using the program with the IBI Operator.

The following is a high-level overview of the image-based installation process:

. Generate an image from a {sno} cluster.
. Use the `openshift-install` program to embed the seed image URL, and other installation artifacts, in a live installation ISO.
. Start the host using the live installation ISO to preinstall the host.
+
During this process, the `openshift-install` program installs {op-system-first} to the disk, pulls the image you generated, and precaches release container images to the disk.

. When the installation completes, the host is ready to ship to the remote site for rapid reconfiguration and deployment.

// Module included in the following assemblies:
// * edge_computing/image_base_install/ibi-understanding-image-based-install.adoc

[id="ibi-image-based-deployment-overview_{context}"]
= Image-based deployment for {sno} clusters

[role="_abstract"]
You can use the `openshift-install` program or the IBI Operator to configure and deploy a host that you preinstalled with an image-based installation.

{sno-caps} cluster deployment::

To configure the target host with site-specific details by using the `openshift-install` program, you must create the following resources:
+
--
* The `install-config.yaml` installation manifest

* The `image-based-config.yaml` manifest
--
+
The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment.

Managed {sno} cluster deployment::

{rh-rhacm-first} and the {mce} (MCE) use a hub-and-spoke architecture to manage and deploy {sno} clusters across multiple sites. Using this approach, the hub cluster serves as a central control plane that manages the spoke clusters, which are often remote {sno} clusters deployed at the far edge of the network.
+
You can define the site-specific configuration resources for an image-based deployment in the hub cluster. The IBI Operator uses these configuration resources to reconfigure the preinstalled host at the remote site and deploy the host as a managed {sno} cluster. This approach is especially beneficial for telecommunications providers and other service providers with extensive, distributed infrastructures, where an end-to-end installation at the remote site would be time-consuming and costly.
+
The following is a high-level overview of the image-based deployment process for hosts preinstalled with an imaged-based installation:
+
--
* Define the site-specific configuration resources for the preinstalled host in the hub cluster.
* Apply these resources in the hub cluster. This initiates the deployment process.
* The IBI Operator creates a configuration ISO.
* The IBI Operator boots the target preinstalled host with the configuration ISO attached.
* The host mounts the configuration ISO and begins the reconfiguration process.
* When the reconfiguration completes, the {sno} cluster is ready.
--
+
As the host is already preinstalled using an image-based installation, a technician can reconfigure and deploy the host in a matter of minutes.

// Module included in the following assemblies:
// * edge_computing/image_base_install/ibi-understanding-image-based-install.adoc

[id="ibi-installation-deployment-components_{context}"]
= Image-based installation and deployment components

[role="_abstract"]
The following content describes the components in an image-based installation and deployment.

Seed image:: OCI container image generated from a dedicated cluster with the target OpenShift Container Platform version.

Seed cluster:: Dedicated {sno} cluster that you use to create a seed image and is deployed with the target OpenShift Container Platform version.

{lcao}:: Generates the seed image.

Image Based Install (IBI) Operator:: When you deploy managed clusters, the IBI Operator creates a configuration ISO from the site-specific resources you define in the hub cluster, and attaches the configuration ISO to the preinstalled host by using a bare-metal provisioning service.

`openshift-install` program:: Creates the installation and configuration ISO, and embeds the seed image URL in the live installation ISO. If the IBI Operator is not used, you must manually attach the configuration ISO to a preinstalled host to complete the deployment.

[role="_additional-resources"]
.Additional resources

* Deploying a {sno} cluster using the `openshift-install` program

// Module included in the following assemblies:
// * edge_computing/image-based-install/ibi-understanding-image-based-install.adoc

[id="ibi-image-based-install-cluster-guide_{context}"]
= Cluster guidelines for image-based installation and deployment

[role="_abstract"]
For a successful image-based installation and deployment, see the following guidelines.

[id="ibi-cluster-guidelines_{context}"]
== Cluster guidelines

* If you are using {rh-rhacm-first}, to avoid including any {rh-rhacm} resources in your seed image, you need to disable all optional {rh-rhacm} add-ons before generating the seed image.

* In a deployed cluster, the `clusterversion` resource shows a `creationTimestamp` that reflects the creation date of the seed cluster, not the deployment date of the new cluster.
To determine the deployment date of a new cluster, check the `creationTimestamp` field for the `Node` resource instead.

[id="ibi-seed-cluster-guidelines_{context}"]
== Seed cluster guidelines

* If your cluster deployment at the edge of the network requires a proxy configuration, you must create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.

* The `clusterNetwork` and `serviceNetwork` network configurations in the seed cluster persist to the deployed cluster. The Lifecycle Agent embeds these settings in the seed image. You cannot change these settings later in the image-based installation and deployment process.

* If you set a maximum transmission unit (MTU) in the seed cluster, you must set the same MTU value in the static network configuration for the image-based configuration ISO.

* Your {sno} seed cluster must have a shared `/var/lib/containers` directory for precaching images during an image-based installation. For more information see "Configuring a shared container partition between ostree stateroots".

* Create a seed image from a {sno} cluster that uses the same hardware as your target bare-metal host. The seed cluster must reflect your target cluster configuration for the following items:

** CPU topology
*** CPU architecture
*** Number of CPU cores
*** Tuned performance configuration, such as number of reserved CPUs

** IP version configuration, either IPv4, IPv6, or dual-stack networking

** Disconnected registry
+
[NOTE]
====
If the target cluster uses a disconnected registry, your seed cluster must use a disconnected registry. The registries do not have to be the same.
====

** FIPS configuration

[role="_additional-resources"]
.Additional resources

* Configuring a shared container partition between ostree stateroots

// Module included in the following assemblies:
// * scalability_and_performance/ztp-image-based-upgrade.adoc

[id="ztp-image-based-upgrade-prereqs_{context}"]
= Software prerequisites for an image-based installation and deployment

[role="_abstract"]
An image-based installation and deployment requires the following minimum software versions for these required components.

.Minimum software requirements
[cols=2*, width="80%", options="header"]
|====
|Component
|Software version

|Managed cluster version
|4.17

|Hub cluster version
|4.16

|{rh-rhacm-first}
|2.12

|{lcao}
|4.16 or later

|Image Based Install Operator
|4.17

|`openshift-install` program
|4.17

|====

[role="_additional-resources"]
.Additional resources

* Multicluster architecture

* Understanding the image-based upgrade for {sno} clusters

* SiteConfig operator
