---
title: "Installation methods"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-nutanix
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-nutanix
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installation methods

[id="preparing-to-install-on-nutanix"]
= Installation methods

You can install an OpenShift Container Platform cluster on Nutanix by using a variety of different installation methods. Each method has qualities that can make the method more suitable for different use cases, such as installing a cluster in a disconnected environment or installing a cluster that requires minimal configuration and provisioning. Before you install OpenShift Container Platform, ensure that your Nutanix environment meets specific requirements.

// Module included in the following assemblies:
//
// * installing/installing_nutanix/preparing-to-install-nutanix.adoc

[id="installation-nutanix-infrastructure_{context}"]
= Nutanix version requirements

You must install the OpenShift Container Platform cluster to a Nutanix environment that meets the following requirements:

.Version requirements for Nutanix virtual environments
[cols=2, options="header"]
|===
|Component |Required version
|Nutanix AOS | 6.5.2.7 or later
|Prism Central | pc.2022.6 or later
|===

[id="preparing-to-install-on-nutanix-agent_{context}"]
== Agent-based Installer

You can install an OpenShift Container Platform cluster on Nutanix by using the Agent-based Installer.
For example, the Agent-based Installer can be used to install a three-node cluster, which is a smaller, more resource efficient cluster for testing, development, and production. See Preparing to install with the Agent-based Installer for additional details.

// Module included in the following assemblies:
//
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc

[id="installation-nutanix-installer-infra-reqs_{context}"]
= Environment requirements

Before you install an OpenShift Container Platform cluster, review the following Nutanix AOS environment requirements.

[id="installation-nutanix-installer-infrastructure-reqs_{context}"]
== Infrastructure requirements

You can install OpenShift Container Platform on on-premise Nutanix clusters, Nutanix Cloud Clusters (NC2) on {aws-first}, or NC2 on {azure-first}.

For more information, see Nutanix Cloud Clusters on AWS and Nutanix Cloud Clusters on Microsoft Azure.

[id="installation-nutanix-installer-infra-reqs-account_{context}"]
== Required account privileges

The installation program requires access to a Nutanix account with the necessary permissions to deploy the cluster and to maintain the daily operation of it. The following options are available to you:

* You can use a local Prism Central user account with administrative privileges. Using a local account is the quickest way to grant access to an account with the required permissions.
* If your organization's security policies require that you use a more restrictive set of permissions, use the permissions that are listed in the following table to create a custom Cloud Native role in Prism Central. You can then assign the role to a user account that is a member of a Prism Central authentication directory.

Consider the following when managing this user account:

* When assigning entities to the role, ensure that the user can access only the Prism Element and subnet that are required to deploy the virtual machines.
* Ensure that the user is a member of the project to which it needs to assign virtual machines.

For more information, see the Nutanix documentation about creating a Custom Cloud Native role, assigning a role, and adding a user to a project.

.Required permissions for creating a Custom Cloud Native role
[%collapsible]
====
[cols="3a,3a,3a,3a",options="header"]
|===
|Nutanix Object
|When required
|Required permissions in Nutanix API
|Description

|Categories
|Always
|
[%hardbreaks]
`Create_Category_Mapping`
`Create_Or_Update_Name_Category`
`Create_Or_Update_Value_Category`
`Delete_Category_Mapping`
`Delete_Name_Category`
`Delete_Value_Category`
`View_Category_Mapping`
`View_Name_Category`
`View_Value_Category`
|Create, read, and delete categories that are assigned to the OpenShift Container Platform machines.

|Images
|Always
|
[%hardbreaks]
`Create_Image`
`Delete_Image`
`View_Image`
|Create, read, and delete the operating system images used for the OpenShift Container Platform machines.

|Virtual Machines
|Always
|
[%hardbreaks]
`Create_Virtual_Machine`
`Delete_Virtual_Machine`
`View_Virtual_Machine`
|Create, read, and delete the OpenShift Container Platform machines.

|Clusters
|Always
|`View_Cluster`
|View the Prism Element clusters that host the OpenShift Container Platform machines.

|Subnets
|Always
|`View_Subnet`
|View the subnets that host the OpenShift Container Platform machines.

|Projects
|If you will associate a project with compute machines, control plane machines, or all machines.
|
[%hardbreaks]
`View_Project`
|View the projects defined in Prism Central and allow a project to be assigned to the OpenShift Container Platform machines.

|Tasks
|Always
|
[%hardbreaks]
`View_Task`
|Fetch and view tasks on the Prism Element that contain OpenShift Container Platform machines and nodes.

|Hosts
|If you use GPUs with compute machines.
|
[%hardbreaks]
`View_Host`
|Fetch and view hosts on the Prism Element that have GPUs attached.
|===
====

[id="installation-nutanix-installer-infra-reqs-limits_{context}"]
== Cluster limits

Available resources vary between clusters. The number of possible clusters within a Nutanix environment is limited primarily by available storage space and any limitations associated with the resources that the cluster creates, and resources that you require to deploy the cluster, such a IP addresses and networks.

[id="installation-nutanix-installer-infra-reqs-resources_{context}"]
== Cluster resources

A minimum of 800 GB of storage is required to use a standard cluster.

When you deploy a OpenShift Container Platform cluster that uses installer-provisioned infrastructure, the installation program must be able to create several resources in your Nutanix instance. Although these resources use 856 GB of storage, the bootstrap node is destroyed as part of the installation process.

A standard OpenShift Container Platform installation creates the following resources:

* 1 label
* Virtual machines:
** 1 disk image
** 1 temporary bootstrap node
** 3 control plane nodes
** 3 compute machines

[id="installation-nutanix-installer-infra-requirements-networking_{context}"]
== Networking requirements

You must use either AHV IP Address Management (IPAM) or Dynamic Host Configuration Protocol (DHCP) for the network and ensure that it is configured to provide persistent IP addresses to the cluster machines. Additionally, create the following networking resources before you install the OpenShift Container Platform cluster:

* IP addresses
* DNS records

Nutanix Flow Virtual Networking is supported for new cluster installations. To use this feature, enable Flow Virtual Networking on your AHV cluster before installing. For more information, see Flow Virtual Networking overview.

[NOTE]
====
It is recommended that each OpenShift Container Platform node in the cluster have access to a Network Time Protocol (NTP) server that is discoverable via DHCP. Installation is possible without an NTP server. However, an NTP server prevents errors typically associated with asynchronous server clocks.
====

[id="installation-nutanix-installer-infra-reqs-_{context}"]
=== Required IP Addresses
An installer-provisioned installation requires two static virtual IP (VIP) addresses:

* A VIP address for the API is required. This address is used to access the cluster API.
* A VIP address for ingress is required. This address is used for cluster ingress traffic.

You specify these IP addresses when you install the OpenShift Container Platform cluster.

[id="installation-nutanix-installer-infra-reqs-dns-records_{context}"]
=== DNS records
You must create DNS records for two static IP addresses in the appropriate DNS server for the Nutanix instance that hosts your OpenShift Container Platform cluster. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the cluster base domain that you specify when you install the cluster.

If you use your own DNS or DHCP server, you must also create records for each node, including the bootstrap, control plane, and compute nodes.

A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

.Required DNS records
[cols="1a,5a,3a",options="header"]
|===

|Component
|Record
|Description

|API VIP
|`api.<cluster_name>.<base_domain>.`
|This DNS A/AAAA or CNAME record must point to the load balancer
for the control plane machines. This record must be resolvable by both clients
external to the cluster and from all the nodes within the cluster.

|Ingress VIP
|`*.apps.<cluster_name>.<base_domain>.`
|A wildcard DNS A/AAAA or CNAME record that points to the load balancer that targets the
machines that run the Ingress router pods, which are the worker nodes by
default. This record must be resolvable by both clients external to the cluster
and from all the nodes within the cluster.
|===

// Module included in the following assemblies:
//
//Postinstall and update content
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
//
//Platforms that must use `ccoctl` and update content
// * installing/installing_ibm_cloud/configuring-iam-ibm-cloud.adoc
// * installing/installing_ibm_powervs/preparing-to-install-on-ibm-power-vs.doc
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Postinstall  and update content

//Platforms that must use `ccoctl`

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-configuring_{context}"]

[role="_abstract"]
//Nutanix-only intro because it needs context in its install procedure.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on {ibm-power-server-name}, you must set the CCO to `manual` mode as part of the installation process.

//The upgrade and postinstall procs also have a different intro, so they are excluded here.
To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

//Intro for the postinstall procs.
To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary.

//Intro for the upgrade procs.
To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

[NOTE]
====
The `ccoctl` utility is a Linux binary that must run in a Linux environment.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the {oc-first}.

//Upgrade prereqs
* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

//Permissions requirements (per platform, for install and key rotation)

.Procedure

. Set a variable for the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
----
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
----

. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
----
+
[NOTE]
====
Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
====

. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
----
+
For `<rhel_version>`, specify the value that corresponds to the version of {op-system-base-full} that the host uses.
If no value is specified, `ccoctl.rhel8` is used by default.
The following values are valid:
+
* `rhel8`: Specify this value for hosts that use {op-system-base} 8.
* `rhel9`: Specify this value for hosts that use {op-system-base} 9.

+
[NOTE]
====
The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
====

. Change the permissions to make `ccoctl` executable by running the following command:
+
[source,terminal]
----
$ chmod 775 ccoctl
----

.Verification

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:
+
[source,terminal]
----
$ ./ccoctl
----
+
.Example output
[source,terminal]
----
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
----

//Postinstall and update content

//Platforms that must use `ccoctl` and update content

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[role="_additional-resources"]
.Additional resources
* Preparing to update a cluster with manually maintained credentials
