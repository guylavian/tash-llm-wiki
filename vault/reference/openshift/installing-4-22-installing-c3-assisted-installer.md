---
title: "Installing a cluster on {oci-edge-no-rt} by using the {ai-full}"
type: reference
domain: openshift
slug: installing-4-22-installing-c3-assisted-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-c3-assisted-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {oci-edge-no-rt} by using the {ai-full}

[id="installing-c3-assisted-installer"]
= Installing a cluster on {oci-edge-no-rt} by using the {ai-full}

With {oci-edge}, you can run applications and middleware by using {oci-first} services on high performance cloud infrastructure in your data center.

The following procedures describe a cluster installation on {oci-c3} as an example.

// Supported Oracle Edge Cloud Infrastructures
// Module included in the following assemblies:
//
// * installing/installing_oci_edge/installing-c3-agent-based-installer.adoc
// * installing/installing_oci_edge/installing-c3-assisted-installer.adoc

[id="installing-oci-edge-infra-support_{context}"]
= Supported {oci-edge-no-rt} infrastructures

The following table describes the support status of each {oci-edge} infrastructure offering:

.{oci-edge-no-rt} infrastructure support statuses
[cols=".^,.^",options="header"]
|====
|Infrastructure type|Support status

|Private Cloud Appliance
|General Availability

|Oracle Compute Cloud@Customer
|General Availability

|Roving Edge
|Technology Preview

|====

// Overview
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-overview_{context}"]
= Overview

You can install OpenShift Container Platform on {oci-edge-no-rt} by using the {ai-full}.

For an alternative installation method, see "Installing a cluster on {oci-edge} by using the Agent-based Installer".

.Preinstallation considerations

* Ensure that your installation meets the prerequisites specified for Oracle. For details, see the "Access and Considerations" section in the Oracle documentation.

* Ensure that your infrastructure is certified and uses a compatible cloud instance type. For details, see Oracle Cloud Infrastructure.

* Ensure that you are performing the installation on a virtual machine.

.Installation process

The installation process builds a bastion host within the designated compartment of the OpenShift Container Platform cluster. The bastion host is used to run two Terraform scripts:

* The first script builds IAM Resources in the {oci} Home region of the {oci-edge} system (two Dynamic Groups and one Policy).

* The second script builds the infrastructure resources on the {oci-edge} system to support the OpenShift Container Platform cluster, including the OpenShift Container Platform VCN, public and private subnets, load balancers, Internet GW, NAT GW, and DNS server. The script includes all the resources needed to activate the control plane nodes and compute nodes that form a cluster.

The bastion host is installed in the designated OpenShift Container Platform Compartment and configured to communicate through a designated {oci-edge} DRG Subnet or Internet GW Subnet within the {oci-edge} parent tenancy.

The installation process subsequently provisions three control plane (master) nodes and three compute (worker) nodes, together with the external and internal Load Balancers that form the cluster. This is the standard implementation for {oci-edge-no-rt}.

.Main steps

The main steps of the procedure are as follows:

. Preparing the {oci-edge} bastion server.

. Running the Terraform script via the Home region.

. Preparing the OpenShift Container Platform image for {oci-edge-no-rt}.

. Running the Terraform script via the {oci-edge} region.

. Installing the cluster by using the {ai-full} web console.

// Preparing the Bastian server
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-preparing-bastian-server_{context}"]
= Preparing the {oci} bastion server

By implementing a bastion host, you can securely and efficiently manage access to your {oci-first-no-rt} resources, ensuring that your private instances remain protected and accessible only through a secure, controlled entry point.

.Prerequisites

* See the "Bastion server - prerequisites" section in the Oracle documentation.

.Procedure

. Install the bastion server. For details, see the "Bastion Installation" section in the Oracle documentation.

. Install the Terraform application which is used to run the Terraform script. For details, see the "Terraform Installation" section in the Oracle documentation.

. Install and configure the {oci} command-line interface (CLI). For details, see the "Installing and Configuring the {oci} CLI" section in the Oracle documentation.

.Additional resources

* Quick start - Installing the CLI (Oracle documentation).

// Terraform script execution - part 1
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-running-script-via-home_{context}"]
= Running the Terraform script via the Home region

Copy the Terraform scripts `createInfraResources.tf` and `terraform.tfvars` onto the bastion server. Then run the `createInfraResources.tf` script to create the Dynamic Group Identity resources on your {oci-first-no-rt} Home Region. These resources include dynamic groups, policies, and tags.

.Prerequisites

* You have tenancy privileges to create Dynamic Groups and Policies. If not, you can manually provision them during this procedure.

.Procedure

. Connect to the bastion server via SSH.

. Create `OpenShift\createResourceOnHomeRegion` folders.

. Copy the `createInfraResources.tf` and `terraform.tfvars` files from the C3_PCA GitHub repository into the `createResourceOnHomeRegion` folder.

. Ensure that you have access to the source environment, and that your C3 certificate has been exported.

. Run the `createInfraResources.tf` Terraform script.

For the full procedure, see the "Terraform Script Execution Part-1 (Run Script via Home Region)" section in the Oracle documentation.

// Preparing the OpenShift image
[id="c3-assisted-installer-preparing-image_{context}"]
== Preparing the {oci} image

Generate the OpenShift Container Platform ISO image in the {ai-full} on the Red{nbsp}Hat portal. Then, convert the image to an {oci-edge-no-rt} compatible image and upload it to the *Custom Images* page of your {oci-edge-no-rt} environment.

You can generate, convert and upload the image on your laptop and not on the bastion server or within environments such as Oracle Solution Center.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-assisted-installer-preparing-image-generating_{context}"]
= Generating the image in the {ai-full}

Create a cluster and download the discovery ISO image.

.Procedure

. Log in to {ai-full} web console with your credentials.

. In the *Red Hat OpenShift* tile, select *OpenShift*.

. In the *Red Hat OpenShift Container Platform* tile, select *Create Cluster*.

. On the *Cluster Type* page, scroll to the end of the *Cloud* tab, and select *Oracle Cloud Infrastructure (virtual machines)*.

. On the *Create an OpenShift Cluster* page, select the *Interactive* tile.

. On the *Cluster Details* page, complete the following fields:
+
[cols="1,3",options="header",subs="quotes"]
|===
|Field |Action required

|*Cluster name*
|Specify the name of your OpenShift Container Platform cluster. This name is the same name you used to create the resource via the Terraform scripts. The name must be between 1-54 characters. It can use lowercase alphanumeric characters or hyphen (-), but must start and end with a lowercase letter or a number.

|*Base domain*
|Specify the base domain of the cluster. This is the value used for the `zone_dns` variables in the Terraform scripts that run on {oci-edge}. Make a note of the value.

|*OpenShift version*
| Select *OpenShift 4.16.20*. If it is not immediately visible, scroll to the end of the dropdown menu, select *Show all available versions*, and type the version in the search box.

|*Integrate with external partner platforms*
|Select *Oracle Cloud Infrastructure*.

After you specify this value, the *Include custom manifests* checkbox is selected by default and the *Custom manifests* page is added to the wizard.
|===

. Leave the default settings for the remaining fields, and click *Next*.

. On the *Operators* page, click *Next*.

. On the *Host Discovery* page, click *Add hosts* and complete the following steps:
+
[NOTE]
====
The minimal ISO image is the mandatory *Provisioning type* for the {oci-edge-no-rt}, and cannot be changed.
====

.. In the *SSH public key* field, add the SSH public key by copying the output of the following command:
+
[source,terminal]
----
$ cat ~/.ssh/id_rsa.put
----
+
The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes.

.. Click the *Show proxy settings* checkbox.

.. Add the proxy variables from the `/etc/environment` file of the bastion server that you configured earlier:
+
[source,terminal]
----
http_proxy=http://www-proxy.<your_domain>.com:80
https_proxy=http://www-proxy.<your_domain>.com:80
no_proxy=localhost,127.0.0.1,1,2,3,4,5,6,7,8,9,0,.<your_domain>.com
#(ie.oracle.com,.oraclecorp.com)
----

.. Click *Generate Discovery ISO* to generate the discovery ISO image file.

. Click *Download Discovery ISO* to save the file to your local system. After you download the ISO file, you can rename it as required, for example `discovery_image_<your_cluster_name>.iso`.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-assisted-installer-preparing-image-converting_{context}"]
= Converting and uploading the image to {oci-edge-no-rt}

Convert the ISO image to an {oci-first-no-rt} image and upload it to your {oci-edge-no-rt} system from your OCI Home Region Object
Store.

.Procedure

. Convert the image from ISO to {oci}.
. Upload the {oci} image to an {oci} bucket, and generate a Pre-Authenticated Request (PAR) URL.
. Import the {oci} image to the {oci-edge} portal.
. Copy the Oracle Cloud Identifier (OCID) of the image for use in the next procedure.

For the full procedure, see step 6 - 8 in the "OpenShift Image Preparation" section of the Oracle documentation.

// Terraform script execution - part 2
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-running-script-via-region_{context}"]
= Running the Terraform script via the C3 region

Run the `terraform.tfvars` Terraform script to create all infrastructure resources on {oci-edge}. These resources include the OpenShift Container Platform VCN, public and private subnets, load balancers, internet GW, NAT GW, and DNS server.

This procedure deploys a cluster consisting of three control plane (master) and three compute (worker) nodes. After deployment, you must rename and reboot the nodes. This process temporarily duplicates nodes, requiring manual cleanup in the next procedure.

.Procedure

. Connect to the bastion server via SSH.

. Set the C3 Certificate location and export the certificate.

. Run the `terraform.tfvars` script to create three control plane nodes and three compute nodes.

. Update the labels for the control plane and compute nodes.

. Stop and restart the instances one by one on the {oci-edge} portal.

For the full procedure, see the "Terraform Script Execution - Part 2" section in the Oracle documentation.

// Completing the installation

[id="c3-ai-completing-installation_{context}"]
== Completing the installation by using the {ai-full} web console

After you configure the infrastructure, the instances are now running and are ready to be registered with Red{nbsp}Hat.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-completing-installation-nodes_{context}"]
= Assigning node roles

If the Terraform scripts completed successfully, twelve hosts are now listed for the cluster. Three control plane hosts and three compute hosts have the status "Disconnected". Three control plane hosts and three compute hosts have the status "Insufficient".

Delete the disconnected hosts and assign roles to the remaining hosts.

.Procedure

. From the {ai-full} web console, select the cluster and navigate to the *Host discovery* page.

. Delete the six hosts with a "Disconnected" status, by clicking the option button for each host and selecting *Remove host*. The status of the remaining hosts changes from "Insufficient" to "Ready". This process can take up to three minutes.

. From the *Role* column, assign the *Control plane* role to the three nodes with a boot size of 1.10 TB. Assign the *Worker* role to the three nodes with boot size of 100 GB.

. Rename any hosts with a name shorter than 63 characters, by clicking the option button for the host and selecting *Change hostname*. Otherwise the cluster installation will fail.

. Click *Next*.

. On the *Storage* page, click *Next*.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-completing-installation-networking_{context}"]
= Configuring networking

On the *Networking* page, add the NTP sources for any hosts that display the `Some validations failed` status.

.Procedure

. In the *Host inventory* table, click the *Some validations failed* link for each host displaying this status.

. Click *Add NTP sources*, and then add the IP address `169.254.169.254` for one of the nodes.

. Wait for 2 - 3 minutes until all the *Some validations failed* indicators disappear.

. Select *Next*.

// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-completing-installation-manifests_{context}"]
= Adding custom manifests

Create, modify, and upload the four mandatory custom manifests provided by Oracle.

* In the `C3/custom_manifests_C3/manifests` folder, the following manifests are mandatory:

** `oci-ccm.yml`
** `oci-csi.yml`

* In the `C3/custom_manifests_C3/openshift` folder, the following manifests are mandatory:

** `machineconfig-ccm.yml`
** `machineconfig-csi.yml`

.Prerequisites

* Prepare the custom manifests. For details, see step 8 in the "Install the Cluster using the RH Assisted Installer UI" section of the Oracle documentation.

.Procedure

. Navigate to the *Custom manifests* page.

. Upload and save the `oci-ccm.yml` and `oci-csi.yml` manifest files:

.. In the *Folder* field, select *manifests*.

.. In the *File name* field, enter `oci-ccm.yml`.

.. In the *Content* section, click *Browse*.

.. Select the *oci-ccm.yml* file from the `C3/custom_ manifest_C3/manifests` folder.

.. Click *Add another manifest* and repeat the previous substeps for the `oci-csi.yml` file.

. Upload and save the `machineconfig-ccm.yml` and `machineconfig-csi.yml` manifest files:

.. Click *Add another manifest*.

.. In the *Folder* field, select *openshift*.

.. In the *File name* field, enter `machineconfig-ccm.yml`.

.. In the *Content* section, click *Browse*.

.. Select the *machineconfig-ccm.yml* file from the `C3/custom_ manifest_C3/openshift` folder.

.. Click *Add another manifest* and repeat the previous substeps for the `machineconfig-csi.yml` file.

. Click *Next* to save the custom manifests.

. From the *Review and create* page, click *Install cluster* to create your OpenShift Container Platform cluster. This process takes approximately thirty minutes.

// Opening the cluster
// Module included in the following assemblies:
//
// * installing/installing_oci/installing-c3-assisted-installer.adoc

[id="c3-ai-opening-cluster_{context}"]
= Opening OpenShift Container Platform from the {oci-edge-no-rt} web console

For instructions to access the OpenShift Container Platform console from {oci-edge-no-rt}, see steps 15 - 17 in the "Install the Cluster using the RH Assisted Installer UI" section of the Oracle documentation.
