---
title: "Installing a cluster on {oci-distributed-no-rt} by using the {ai-full}"
type: reference
domain: openshift
slug: installing-4-22-installing-oci-assisted-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-oci-assisted-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {oci-distributed-no-rt} by using the {ai-full}

[id="installing-oci-assisted-installer"]
= Installing a cluster on {oci-distributed-no-rt} by using the {ai-full}

You can use the {ai-full} to install a cluster on {oci-distributed}. This method is recommended for most users, and requires an internet connection.

If you want to set up the cluster manually or using other automation tools, or if you are working in a disconnected environment, you can use the Red Hat Agent-based Installer for the installation. For details, see Installing a cluster on {oci-distributed-no-rt} by using the Agent-based Installer.

// Supported Oracle Distributed Cloud Infrastructures
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-agent-based-installer.adoc
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="installing-oci-distributed-infra-support_{context}"]
= Supported {oci-distributed-no-rt} infrastructures

The following table describes the support status of each {oci-distributed} infrastructure offering:

.{oci-distributed-no-rt} infrastructure support statuses
[cols=".^,.^",options="header"]
|====
|Infrastructure type|Support status

|Commercial Public Cloud
|General Availability

|Dedicated Region
|General Availability

|US Government Cloud
|Technology Preview

|UK Government Cloud
|General Availability

|EU Sovereign Cloud
|Technology Preview

|Isolated Region
|Technology Preview

|Oracle Alloy
|Technology Preview
|====

// The Assisted Installer and Oracle Distributed Cloud overview
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="installing-oci-about-assisted-installer_{context}"]
= About the {ai-full} and {oci-distributed-no-rt} integration

You can run cluster workloads on {oci-distributed} infrastructure that supports dedicated, hybrid, public, and multiple cloud environments. Both Red{nbsp}Hat and Oracle test, validate, and support running an OpenShift Container Platform cluster on {oci-distributed-no-rt}.

This section explains how to use the {ai-full} to install an OpenShift Container Platform cluster on the {oci-first-no-rt} platform. The installation deploys cloud-native components such as {oci-ccm-full} and {oci-csi-full}, and integrates your cluster with {oci} API resources such as instance node, load balancer, and storage.

The installation process uses the OpenShift Container Platform discovery ISO image provided by Red Hat, together with the  scripts and manifests provided and maintained by Oracle.

[id="installing-oci-preinstallation-considerations_{context}"]
== Preinstallation considerations

Before installing OpenShift Container Platform on {oci-distributed-no-rt}, you must consider the following configuration choices.

.Deployment platforms

The integration between OpenShift Container Platform and {oci-distributed-no-rt} is certified on both virtual machines (VMs) and bare-metal (BM) machines. Bare-metal installations using iSCSI boot drives require a secondary vNIC that is automatically created in the Terraform stack provided by Oracle.

Before you create a virtual machine (VM) or bare-metal (BM) machine, you must identify the relevant {oci} shape. For details, see the following resource:

* Cloud instance types (Red{nbsp}Hat Ecosystem Catalog portal).

.VPU sizing recommendations

To ensure the best performance conditions for your cluster workloads that operate on {oci-distributed-no-rt}, ensure that volume performance units (VPUs) for your block volume are sized for your workloads. The following list provides guidance for selecting the VPUs needed for specific performance needs:

* Test or proof of concept environment: 100 GB, and 20 to 30 VPUs.
* Basic environment: 500 GB, and 60 VPUs.
* Heavy production environment: More than 500 GB, and 100 or more VPUs.

Consider reserving additional VPUs to provide sufficient capacity for updates and scaling activities. For more information about VPUs, see Volume Performance Units (Oracle documentation).

.Instance sizing recommendations

Find recommended values for compute instance CPU, memory, VPU, and volume size for OpenShift Container Platform nodes. For details, see Instance Sizing Recommendations for OpenShift Container Platform Nodes (Oracle documentation).

[id="installing-oci-workflow_{context}"]
== Workflow

.High-level workflow for using the Assisted Installer in a connected environment to install a cluster on {oci-distributed-no-rt}
image::569_OpenShift_ai_install_oci_0725.png[High-level workflow for using the Assisted Installer in a connected environment to install a cluster on {oci-distributed-no-rt}]

The procedure for using the {ai-full} in a connected environment to install a cluster on {oci-distributed-no-rt} is outlined below:

. In the {oci-first-no-rt} console, configure an {oci} account to host the cluster:

.. Create a new child compartment under an existing compartment.

.. Create a new object storage bucket or use one provided by {oci-distributed-no-rt}.

.. Download the stack file template stored locally.

. In the {ai-full} console, set up a cluster:

.. Enter the cluster configurations.

.. Generate and download the discovery ISO image.

. In the {oci} console, create the infrastructure:

.. Upload the discovery ISO image to the {oci} bucket.

.. Create a Pre-Authenticated Request (PAR) for the ISO image.

.. Upload the stack file template, and use it to create and apply the stack.

.. Copy the custom manifest YAML file from the stack.

. In the {ai-full} console, complete the cluster installation:

.. Set roles for the cluster nodes.

.. Upload the manifests provided by Oracle.

.. Install the cluster.

[IMPORTANT]
====
The steps for provisioning {oci} resources are provided as an example only. You can also choose to create the required resources through other methods; the scripts are just an example. Installing a cluster with infrastructure that you provide requires knowledge of the cloud provider and the installation process on OpenShift Container Platform. You can access {oci} configurations to complete these steps, or use the configurations to model your own custom script.
====

[role="_additional-resources"]
.Additional resources

* {ai-full} for OpenShift Container Platform
* Installing a Cluster with Red Hat's {ai-full} (Oracle documentation)
* Internet access for OpenShift Container Platform

// Preparing the OCI environment
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="creating-oci-resources-services_{context}"]
= Preparing the {oci-distributed-no-rt} environment

Before installing OpenShift Container Platform using Assisted Installer, create the necessary resources and download the configuration file in the {oci-distributed-no-rt} environment.

.Prerequisites

* You have an {oci-first-no-rt} account to host the cluster.
* If you use a firewall and you plan to use a Telemetry service, you configured your firewall to allow OpenShift Container Platform to access the sites required.

.Procedure

. Log in to your {oci} account with administrator privileges.

. Configure the account by defining the Cloud Accounts and Resources (Oracle documentation). Ensure that you create the following resources:

.. Create a child compartment for organizing, restricting access, and setting usage limits to {oci} resources. For the full procedure, see Creating a Compartment (Oracle documentation).

.. Create a new object storage bucket into which you will upload the discovery ISO image.
For the full procedure, see Creating an Object Storage Bucket (Oracle documentation).

. Download the latest version of the `create-cluster-vX.X.X.zip` configuration file from the `oracle-quickstart/oci-openshift` repository. This file
provides the infrastructure for the cluster and contains configurations for the following:
+
--
** *Terraform Stacks*: The Terraform stack code for provisioning {oci} resources to create and manage OpenShift Container Platform clusters on {oci-distributed-no-rt}.

** *Custom Manifests*: The manifest files needed for the installation of OpenShift Container Platform clusters on {oci-distributed-no-rt}.
--
+
[NOTE]
====
To make any changes to the manifests, you can clone the entire Oracle GitHub repository and access the `custom_manifests` and `terraform-stacks` directories directly.
====
+
For details, see Configuration Files (Oracle documentation).

// Using the Assisted Installer to generate an OCI-compatible discovery ISO image
[id="using-assisted-installer-oci-agent-iso_{context}"]
== Using the {ai-full} to generate a discovery ISO image

Create the cluster configuration and generate the discovery ISO image in the {ai-full} web console.

.Prerequisites

* You created a child compartment and an object storage bucket on {oci-distributed-no-rt}. For details, see _Preparing the {oci-distributed-no-rt} environment_.
* You reviewed details about the OpenShift Container Platform installation and update processes.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="using-assisted-installer-oci-create-cluster_{context}"]
= Creating the cluster

Set the cluster details.

.Procedure

. Log in to the {ai-full} web console with your credentials.

. In the *Red Hat OpenShift* tile, select *OpenShift*.

. In the *Red Hat OpenShift Container Platform* tile, select *Create Cluster*.

. On the *Cluster Type* page, scroll down to the end of the *Cloud* tab, and select *Oracle Cloud Infrastructure (virtual machines)*.

. On the *Create an OpenShift Cluster* page, select the *Interactive* tile.

. On the *Cluster Details* page, complete the following fields:
+
[cols="1,3",options="header",subs="quotes"]
|===
|Field |Action required

|*Cluster name*
|Specify the name of your cluster, such as `oci`. This is the same value as the cluster name in {oci-distributed-no-rt}.

|*Base domain*
|Specify the base domain of the cluster, such as `openshift-demo.devcluster.openshift.com`.

This must be the same value as the zone DNS server in {oci-distributed-no-rt}.

|*OpenShift version*
| * For installations on virtual machines only, specify `OpenShift 4.14` or a later version.

* For installations that include bare metal machines, specify `OpenShift 4.16` or a later version.

|*CPU architecture*
| Specify `x86_64` or `Arm64`.

|*Integrate with external partner platforms*
|Specify `Oracle Cloud Infrastructure`.

After you specify this value, the *Include custom manifests* checkbox is selected by default and the *Custom manifests* page is added to the wizard.
|===

. Leave the default settings for the remaining fields, and click *Next*.

. On the *Operators* page, click *Next*.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="using-assisted-installer-oci-generating-iso_{context}"]
= Generating the Discovery ISO image

Generate and download the Discovery ISO image.

.Procedure

. On the *Host Discovery* page, click *Add hosts* and complete the following steps:

.. For the *Provisioning type* field, select *Minimal image file*.

.. For the *SSH public key* field, add the SSH public key from your local system, by copying the output of the following command:
+
[source,terminal]
----
$ cat ~/.ssh/id_rsa.put
----
+
The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes.

.. Click *Generate Discovery ISO* to generate the discovery ISO image file.

.. Click *Download Discovery ISO* to save the file to your local system.

[role="_additional-resources"]
.Additional resources

* Installation and update
* Configuring your firewall

// Provisioning OCI infrastructure for your cluster
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="provision-oci-infrastructure-ocp-cluster_{context}"]
= Provisioning {oci} infrastructure for your cluster

When using the {ai-full} to create details for your OpenShift Container Platform cluster, you specify these details in a Terraform stack. A stack is an {oci-first-no-rt} feature that automates the provisioning of all necessary {oci} infrastructure resources that are required for installing an OpenShift Container Platform cluster on {oci-distributed-no-rt}.

.Prerequisites

* You downloaded the discovery ISO image to a local directory. For details, see _Using the {ai-full} to generate a discovery ISO image_.
* You downloaded the Terraform stack template to a local directory. For details, see "Preparing the {oci-distributed-no-rt} environment".

.Procedure

. Log in to your {oci-distributed-no-rt} account.

. Upload the discovery ISO image from your local drive to the new object storage bucket you created. For the full procedure, see Uploading an Object Storage Object to a Bucket (Oracle documentation).

. Locate the uploaded discovery ISO, and complete the following steps:
+
--
.. Create a Pre-Authenticated Request (PAR) for the ISO from the adjacent options menu.

.. Copy the generated URL to use as the OpenShift Image Source URI in the next step.
--
+
For the full procedure, see Creating a Pre-Authenticated Requests in Object Storage (Oracle documentation).

. Create and apply the Terraform stack:
+
[IMPORTANT]
====
The Terraform stack includes files for creating cluster resources and custom manifests. The stack also includes a script, and when you apply the stack, the script creates {oci} resources, such as DNS records, an instance, and other resources. For a list of the resources, see the `terraform-stacks` folder in OpenShift on OCI (OSO).
====
+
--
.. Upload the Terraform stacks template terraform-stacks to the new object storage bucket.

.. Complete the stack information and click *Next*.
+
[IMPORTANT]
====
* Make sure that *Cluster Name* matches *Cluster Name* in {ai-full}, and *Zone DNS* matches *Base Domain* in {ai-full}.
* In the *OpenShift Image Source URI* field, paste the Pre-Authenticated Request URL link that you generated in the previous step.
* Ensure that the correct *Compute Shape* field value is defined, depending on whether you are installing on bare metal or a virtual machine. If not, select a different shape from the list. For details, see Compute Shapes (Oracle documentation).
====

.. Click *Apply* to apply the stack.
--
+
For the full procedure, see Creating OpenShift Container Platform Infrastructure Using Resource Manager (Oracle documentation).

. Copy the `dynamic_custom_manifest.yml` file from the *Outputs* page of the Terraform stack.
+
[NOTE]
====
The YAML file contains all the required manifests, concatenated and preformatted with the configuration values. For details, see the Custom Manifests README file.
====
+
For the full procedure, see Getting the OpenShift Container Platform Custom Manifests for Installation (Oracle documentation).

// Completing the remaining Assisted Installer steps

[id="completing-assisted-installer-oci_{context}"]
== Completing the remaining {ai-full} steps

After you provision {oci-distributed} resources and upload OpenShift Container Platform custom manifest configuration files to {oci-distributed-no-rt}, you must complete the remaining cluster installation steps on the {ai-full} before you can create an {oci-distributed-no-rt} instance. These steps include assigning node roles and adding custom manifests.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="assigning-node-roles-oci_{context}"]
= Assigning node roles

Following host discovery, the role of all nodes appears as *Auto-assign* by default. Change each of the node roles to either *Control Plane node* or *Worker*.

.Prerequisites

* You created and applied the Terraform stack in {oci-distributed-no-rt}. For details, see "Provisioning {oci} infrastructure for your cluster".

.Procedure

. From the {ai-full} user interface, go to the *Host discovery* page.

. Under the *Role* column, select either *Control plane node* or *Worker* for each targeted hostname. Then click *Next*.
+
[NOTE]
====
. Before continuing to the next step, wait for each node to reach `Ready` status.
. Expand the node to verify that the hardware type is bare metal.
====

. Accept the default settings for the *Storage* and *Networking* pages. Then click *Next*.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="adding-custom-manifests-oci_{context}"]
= Adding custom manifests

Add the mandatory custom manifests provided by Oracle. For details, see Custom Manifests (Oracle documentation).

.Prerequisites

* You copied the `dynamic_custom_manifest.yml` file from the Terraform stack in {oci-distributed-no-rt}. For details, see "Provisioning {oci} infrastructure for your cluster".

.Procedure

. On the *Custom manifests* page, in the *Folder* field, select `manifests`. This is the {ai-full} folder where you want to save the custom manifest file.

. In the *File name* field, enter a filename, for example, `dynamic_custom_manifest.yml`.

. Paste the contents of the `dynamic_custom_manifest.yml` file that you copied from {oci-distributed-no-rt}:

.. In the *Content* section, click the *Paste content* icon.

.. If you are using Firefox, click *OK* to close the dialog box, and then press *Ctrl+V*. Otherwise, skip this step.

. Click *Next* to save the custom manifest.

. From the *Review and create* page, click *Install cluster* to create your OpenShift Container Platform cluster on {oci-distributed-no-rt}.

After the cluster installation and initialization operations, the {ai-full} indicates the completion of the cluster installation operation. For more information, see "Completing the installation" section in the {ai-full} for OpenShift Container Platform document.

[role="_additional-resources"]
.Additional resources

* {ai-full} for OpenShift Container Platform

// Verifying a successful cluster installation on OCI
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="verifying-cluster-install-ai-oci_{context}"]
= Verifying a successful cluster installation on {oci-distributed-no-rt}

Verify that your cluster was installed and is running effectively on {oci-distributed}.

.Procedure

. From the Red Hat Hybrid Cloud Console, go to *Clusters > Assisted Clusters* and select your cluster's name.

. On the *Installation Progress* page, check that the Installation progress bar is at 100% and a message displays indicating `Installation completed successfully`.

. Under *Host inventory*, confirm that the status of all control plane and compute nodes is `Installed`.
+
[NOTE]
====
OpenShift Container Platform designates one of the control plane nodes as the bootstrap virtual machine, eliminating the need for a separate bootstrap machine.
====

. Click the Web Console URL, to access the OpenShift Container Platform web console.

. From the menu, select *Compute > Nodes*.

. Locate your node from the *Nodes* table.

. From the *Terminal* tab, verify that iSCSI appears next to the serial number.

. From the *Overview* tab, check that your node has a *Ready* status.

. Select the *YAML* tab.

. Check the `labels` parameter, and verify that the listed labels apply to your configuration. For example, the `topology.kubernetes.io/region=us-sanjose-1` label indicates in what {oci-distributed-no-rt} region the node was deployed.

// Adding hosts to the cluster following the installation
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="installing-oci-adding-hosts-day-two_{context}"]
= Adding hosts to the cluster following the installation

After creating a cluster with the {ai-full}, you can use the {hybrid-console} to add new host nodes to the cluster and approve their certificate signing requests (CSRs).

For details, see Adding Nodes to a Cluster (Oracle documentation).

// Troubleshooting the installation of a cluster on OCI
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-oci-assisted-installer.adoc

[id="installing-troubleshooting-assisted-installer-oci_{context}"]
= Troubleshooting the installation of a cluster on {oci-distributed-no-rt}

If you experience issues with using the {ai-full} to install an OpenShift Container Platform cluster on {oci-distributed}, read the following sections to troubleshoot common problems.

[id="installing-troubleshooting-load-balancer_{context}"]
== The Ingress Load Balancer in {oci-distributed-no-rt} is not at a healthy status

This issue is classed as a `Warning` because by using {oci-distributed-no-rt} to create a stack, you created a pool of compute nodes, 3 by default, that are automatically added as backend listeners for the Ingress Load Balancer. By default, the OpenShift Container Platform deploys 2 router pods, which are based on the default values from the OpenShift Container Platform manifest files. The `Warning` is expected because a mismatch exists with the number of router pods available, 2, to run on the 3 compute nodes.

.Example of a `Warning` message that is under the Backend set information tab on {oci-distributed-no-rt}
image::ingress_load_balancer_warning_message.png[Example of an warning message that is under the Backend set information tab on {oci-distributed-no-rt}]

You do not need to modify the Ingress Load Balancer configuration. Instead, you can point the Ingress Load Balancer to specific compute nodes that operate in your cluster on OpenShift Container Platform. To do this, use placement mechanisms, such as annotations, on OpenShift Container Platform to ensure router pods only run on the compute nodes that you originally configured on the Ingress Load Balancer as backend listeners.

[id="installing-troubleshooting-stack-operation_{context}"]
== {oci-distributed-no-rt} create stack operation fails with an Error: 400-InvalidParameter message

On attempting to create a stack on {oci-distributed-no-rt}, you identified that the *Logs* section of the job outputs an error message. For example:

[source,terminal]
----
Error: 400-InvalidParameter, DNS Label oci-demo does not follow Oracle requirements
Suggestion: Please update the parameter(s) in the Terraform config as per error message DNS Label oci-demo does not follow Oracle requirements
Documentation: https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_vcn
----

Go to the https://console.redhat.com/openshift/assisted-installer/clusters/~new[*Install OpenShift with the Assisted Installer*] page on the Hybrid Cloud Console, and check the *Cluster name* field on the *Cluster Details* step. Remove any special characters, such as a hyphen (`-`), from the name, because these special characters are not compatible with the {oci} naming conventions. For example, change `oci-demo` to `ocidemo`.

[role="_additional-resources"]
.Additional resources

* Troubleshooting OpenShift Container Platform on {oci} (Oracle documentation)

* Installing an on-premise cluster using the {ai-full}
