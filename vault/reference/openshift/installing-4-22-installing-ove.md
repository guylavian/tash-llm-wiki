---
title: "Installing a cluster without an external registry"
type: reference
domain: openshift
slug: installing-4-22-installing-ove
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-ove
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster without an external registry

[id="installing-ove"]
= Installing a cluster without an external registry

[role="_abstract"]
You can deploy an OpenShift Container Platform cluster without the need for an external image registry, either in a connected or disconnected environment. This installation method uses a simplified user interface and self-contained media to facilitate the installation.

Although the method supports general clusters, the downloaded media contains an Operator bundle that is curated specifically for {ove-first}, meaning additional Operators must be retrieved separately if required for other use cases.

// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/installing-ove.adoc

[id="virt-installing-ove-advantages_{context}"]
= Installation method advantages

[role="_abstract"]
This method has several advantages for users who want to install a cluster primarily to run virtualized workloads using {VirtProductName}.

Simplified web interface:: The cluster installation is performed through a graphical user interface.
In addition to providing reasonable default configurations, this interface guides you through the installation by providing hints and warnings about configuring your cluster, without limiting the configurations that are available at installation time.
This reduces the need for in-depth knowledge of OpenShift Container Platform while still allowing for complex configurations to be made.

No external registry needed:: If you are installing your cluster in a disconnected environment, you do not need to configure an external image registry in your environment when using this method.
All other disconnected installation methods require this additional environment setup.

Included Operator bundle:: You can install the Virtualization bundle, which includes all of the additional {olm-first} Operators needed to run virtual machines on your cluster, at the same time as the cluster installation.

[NOTE]
====
This installation method does not come with any storage Operators as part of the Operator bundle.
You must configure your own storage solution separately.
====

// Downloading the installation ISO
// Module included in the following assemblies:
//
// * virt/install/installing-ove.adoc

[id="virt-installing-ove-iso_{context}"]
= Downloading the installation ISO

[role="_abstract"]
You must first download the ISO image that will be used to run the installation on your bare-metal machines.
This image includes all of the necessary OpenShift Container Platform release images, as well as the {olm-first} Operators needed to install Virtualization on the cluster.

[NOTE]
====
The size of the ISO image can vary depending on the release you select.
====

.Procedure

. Log in to the {hybrid-console-url}.

. On the *Red Hat OpenShift* tile, click *OpenShift*.

. On the *Red Hat OpenShift Container Platform* tile, click *Create cluster*.

. Click the *Datacenter* tab.

. Under *Assisted Installer*, click *Create cluster*.

. In the *Cluster details* page, select the toggle for "I'm installing on a disconnected/air-gapped/secured environment".

. Click *Next*.

. Click *Download ISO*.

// Mounting the ISO and booting the rendezvous node
// Module included in the following assemblies:
//
// * virt/install/installing-booting.adoc

[id="virt-installing-ove-booting_{context}"]
= Mounting the ISO and booting the rendezvous node

[role="_abstract"]
To initiate the cluster installation, attach the downloaded ISO to the machine that will serve as your rendezvous host and boot the machine from the ISO.

The rendezvous node runs as the bootstrap host during the installation, which hosts the configuration web console and runs an Assisted Service that facilitates the cluster deployment.

.Prerequisites

* You have downloaded the installation ISO.

.Procedure

. On the machine that you have designated to be the rendezvous node, attach the ISO image to the machine and boot the machine from this image.
You can also boot from a USB drive containing the ISO image.
+
[NOTE]
====
If you mount the ISO via a virtual drive, the cluster installation might take several hours to complete.
Mount the ISO with physical media such as a USB drive to reduce the overall installation time.
====

. Wait for the machine to boot from the image and display the *Rendezvous node setup* menu.

. Select *This is the rendezvous node* in the *Rendezvous node setup* menu.
+
[IMPORTANT]
====
You must select only one machine to act as the rendezvous node.
Selecting two or more machines as a rendezvous node is not supported.
====

. In the *Rendezvous node IP selection* menu, select an IP address from the list to use as the rendezvous node IP address and select *Continue*.
Make note of this address for later use.

. Wait for the rendezvous node to provide a URL for finishing the installation and save the URL for later use, as shown in the following image.
+
image::installing-ove-console.png[The rendezvous host providing the URL of the installation console]

// Configuring cluster details and choosing Operators to install
// Module included in the following assemblies:
//
// * virt/install/installing-booting.adoc

[id="virt-installing-ove-console-initial_{context}"]
= Configuring cluster details and choosing Operators to install

[role="_abstract"]
Once the rendezvous node has been booted from the ISO image, configure details about your cluster and choose Virtualization Operators to install from the web console.

.Prerequisites

* You have the URL of the installation web console that was provided by the rendezvous node.

.Procedure

. In a web browser, go to the URL provided by the rendezvous node.

. Configure your cluster in the *Cluster details* page:

.. Enter a name for the cluster in the *Cluster name* field.

.. Enter a base domain for the cluster in the *Base domain* field.
All subdomains for the cluster will use this base domain.
+
[NOTE]
====
The base domain must be a valid DNS name.
You must not have a wildcard domain set up for the base domain.
====

.. Enter your pull secret in the *Pull secret* field.
You can obtain a copy of your pull secret from the {hybrid-console}.

.. Optional: In the *Number of control plane nodes* field, select the number of control plane nodes for your installation from the dropdown menu.
The default value is `3`.

.. Optional: Select the *Include custom manifests* checkbox if you want to upload custom manifests to further configure your cluster.
This option adds an additional page for custom manifests that you use later in the configuration process.
+
[IMPORTANT]
====
If you have already added custom manifests, clearing the *Include custom manifests* checkbox automatically deletes them all.
You must confirm the deletion.
====

.. Optional: Under *Encryption of installation disks*, select the toggle switch for each disk you want to encrypt.

.. If you are encrypting disks, select either *TPM v2* or *Tang* as your encryption method.

.. If you are encrypting disks using a Tang server, enter the **Server URL** and **Server Thumbprint** in the **Tang servers** section of the page. You can select **Add another Tang server** to configure details for additional Tang server.

.. Click *Next* to continue.
Once you proceed to the next page, you cannot go back to change any of these cluster details.

. Choose additional Operators to install in the *Operators* page:

.. If you want to install all of the Operators recommended for running Virtualization on your cluster, select *Virtualization* in the *Bundles* section.

.. If you want to install only some Operators, select the individual Operators from the Single Operators section.
+
[NOTE]
====
Some of the listed Operators are available only as part of the Virtualization Operator bundle.
====

.. Click *Next* to continue.

// Booting the remaining cluster hosts
// Module included in the following assemblies:
//
// * virt/install/installing-booting.adoc

[id="virt-installing-ove-hosts_{context}"]
= Booting the remaining cluster hosts

[role="_abstract"]
After you have configured initial cluster details in the installation web console and have a defined cluster topology, you must boot the remaining machines that will make up your cluster from the ISO image.

[NOTE]
====
You can boot non-rendezvous node machines earlier in the installation process, even before you designate a machine as the rendezvous node. However, you must know the valid IP address that you will select for the rendezvous node.

When you boot your non-rendezvous node machines, the machines will perform a check to see if an Assisted Service is running at the specified rendezvous IP address.
If the service is not yet running, a warning appears to confirm whether you would still like to proceed booting the machine from the ISO image.
====

.Prerequisites

* You have downloaded the installation ISO.

.Procedure

. Attach the ISO image to a machine and boot the machine from this image.
You can also boot from a USB drive containing the ISO image.

. Wait for a machine to boot from the image and display the *Rendezvous node setup* menu.

. Enter the rendezvous node IP address in the *Rendezvous node setup* menu and select *Save rendezvous IP*.

. Select *Save and Continue*.

. Repeat this process for each remaining machine that will comprise the hosts in your cluster.

// Completing cluster configuration and initiating the installation
// Module included in the following assemblies:
//
// * virt/install/installing-ove.adoc

[id="virt-installing-ove-console-final_{context}"]
= Completing cluster configuration and initiating the installation

[role="_abstract"]
Before you can finally initiate the cluster installation, you must verify host details, configure cluster networking details, and download the default cluster credentials.

.Prerequisites

* You have booted all of the hosts that will comprise your cluster and configured them with the correct rendezvous node IP address.
+
[IMPORTANT]
====
You can add as many hosts as you want to your cluster.
However, at this stage, you must at least have enough available hosts to match the value you specified in the *Number of control plane nodes* field of the installation console's *Cluster details* page.
====

.Procedure

. On the installation console hosted by the rendezvous node, configure the hosts in the *Host discovery* page:

.. Verify that every machine you booted from the ISO image appears in the *Host Inventory* section and has a *Status* value of *Ready*.

.. For each host, click the expand icon and verify that all of the specification fields are correct.

.. Optional: For each host except the rendezvous node, configure the role by selecting an option from the dropdown menu of the *Role* column.
The default value for every host except the rendezvous node is `Auto-assign`.

.. Click *Next* to continue.

. On the *Storage* page, click the expand icon for each host and verify that all of the specification fields are correct.

. Click *Next* to continue.

. If you want to manage your own networking, select the *User-Managed Networking* option on the *Networking* page.

. If you want the cluster to manage networking, select the *Cluster-Managed Networking* option on the *Networking* page and configure cluster networking:

.. Select a *Networking stack type*.

.. Optional: Select a machine network from the dropdown menu of the *Machine network* field.
Otherwise, a default value is selected.

.. Enter an IP address in the *API IP* field.
An API IP provides an endpoint for all users to interact with and configure the platform.

.. Enter an IP address in the *Ingress IP* field.
An ingress IP provides an endpoint for application traffic flowing from outside the cluster.

. Optional: Select the *Use advanced networking* checkbox and configure other parameters such as the *Cluster network CIDR*, the *Cluster network host prefix*, or *the Service network CIDR*.
+
This option is available for both cluster-managed and user-managed networking.

. Optional: Enter a key in the *Host SSH Public Key for troubleshooting after installation* field, which you can use to connect to hosts using a public SSH key for troubleshooting after installation.
+
This option is available for both cluster-managed and user-managed networking.

. Click *Next* to continue.

. On the *Download credentials* page, select the checkbox to acknowledge that you must download credential files prior to cluster installation.

. Click *Download credentials* and save the cluster credentials file in a secure location.
+
[IMPORTANT]
====
You must download the credentials at this stage.
Once you initiate the cluster installation, the rendezvous node reboots and you can no longer retrieve the credentials.
====

. On the *Review and create* page, review all of the cluster details and click *Install cluster* to initiate the cluster installation.
+
During the installation process, the rendezvous node reboots and the console you used to configure the installation is no longer accessible.
At that point, the URL of the deployed cluster's web console is provided, although this console is not accessible until the cluster installation is completed.
+
Once the cluster is installed, you can visit this URL and sign in to the web console with your downloaded credentials.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* Installing virtctl
* Creating virtual machines from instance types
* Creating virtual machines from templates
* Migrating virtual machines from VMware vSphere (Migration Toolkit for Virtualization documentation)
* Migrating virtual machines from Red{nbsp}Hat Virtualization (Migration Toolkit for Virtualization documentation)
