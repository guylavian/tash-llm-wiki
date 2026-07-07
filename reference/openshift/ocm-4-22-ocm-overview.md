---
title: "Red Hat OpenShift Cluster Manager"
type: reference
domain: openshift
slug: ocm-4-22-ocm-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ocm/ocm-overview
version: 4.22
family: ocm
documentKind: "Documentation"
---

# Red Hat OpenShift Cluster Manager

[id="ocm-overview"]
= Red Hat OpenShift Cluster Manager

[role="_abstract"]
{cluster-manager-first} is a managed service where you can install, modify, operate, and upgrade your Red Hat OpenShift clusters. As a cluster administrator, this service allows you to work with all of your organization's clusters from a single dashboard.

{cluster-manager} guides you to install {OCP}, {rosa-classic-title}, {hcp-title-first}, and {dedicated} clusters. It is also responsible for both {OCP} clusters after self-installation as well as your {rosa-classic-title}, {hcp-title-first}, and {dedicated} clusters.

You can use {cluster-manager} to do the following actions:

* Create clusters
* View cluster details and metrics
* Manage your clusters with tasks such as scaling, changing node labels, networking, authentication
* Manage access control
* Monitor clusters
* Schedule upgrades
* Update billing accounts
* Transferring cluster ownership

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="accessing-ocm_{context}"]
= Accessing {cluster-manager-first}

[role="_abstract"]
You can access {cluster-manager} with your configured OpenShift account.

.Prerequisites

* You have an account that is part of an OpenShift organization.
* If you are creating a cluster, your organization has a specified quota.

.Procedure

* Log in to {cluster-manager-url} using your login credentials.

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-general-actions_{context}"]
= General actions

[role="_abstract"]
On the top right of the cluster page, there are some actions that a user can perform on the entire cluster:

* **Open console** launches a web console so that the cluster owner can issue commands to the cluster.
* **Actions** drop-down menu allows the cluster owner to rename the display name of the cluster, edit the machine pools, and delete the cluster.
You may also transfer the cluster's ownership to another user.
* **Refresh** icon forces a refresh of the cluster.

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-cluster-tabs_{context}"]
= Cluster tabs

[role="_abstract"]
Selecting an active, installed cluster shows tabs associated with that cluster. The following tabs display after the cluster's installation completes:

* Overview
* Access control
* Add-ons
* Cluster history
* Networking
* Machine pools
* Support
* Settings

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-overview-tab_{context}"]
= Overview tab

[role="_abstract"]
The **Overview** tab provides information about how the cluster was configured:

* **Cluster ID** is the unique identification for the created cluster. This ID can be used when issuing commands to the cluster from the command line.
* **Domain prefix** is the prefix that is used throughout the cluster. The default value is the cluster's name.
* **Type** shows the type of cluster, for example {rosa-classic-title}, {rosa-title}, or {dedicated}.
* **Control plane type** is the architecture type of the cluster. The field only displays if the cluster uses a hosted control plane architecture.
* **Region** is the server region.
* **Availability** shows which type of availability zone that the cluster uses, either single or multizone.
* **Availability** shows multizone for {rosa-title} clusters.
*  **Channel group** shows the update channel for the cluster, such as stable or eus. Support for channel groups varies by cluster version. If support channel editing is available, this field can be changed by clicking the pencil icon.
* **Version** is the OpenShift version that is installed on the cluster. If there is an update available, you can update from this field.
* **Created at** shows the date and time that the cluster was created.
* **Owner** identifies who created the cluster and has owner rights.
* **Delete Protection: <status>** shows whether or not the cluster's delete protection is enabled.
* **Status** displays the current status of the control plane and machine pools of the cluster.
* **Status** displays the current status of the cluster.
* **Total vCPU** shows the total available virtual CPU for this cluster.
* **Total memory** shows the total available memory for this cluster.
* **Infrastructure AWS account** displays the AWS account that is responsible for cluster creation and maintenance.
* **Billing marketplace account** displays the AWS account that is used for billing purposes. Click on the pencil icon to edit this field.
* **Additional encryption** field shows any applicable additional encryption options.
* **Nodes** shows the actual and desired nodes on the cluster. These numbers might not match due to cluster scaling.
* **Cluster autoscaling** field shows whether or not you have enabled autoscaling on the cluster.
* **Instance Metadata Service (IMDS)** field shows your selected instance metadata service for the cluster.
* **Network** field shows the address and prefixes for network connectivity.
* **OIDC configuration** field shows the Open ID Connect configuration for the cluster.
* **Resource usage** section of the tab displays the resources in use with a graph.
* **Advisor recommendations** section gives insight in relation to security, performance, availability, and stability. This section requires the use of remote health functionality. See _Using {red-hat-lightspeed} to identify issues with the cluster_ in the _Additional resources_ section.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-accesscontrol-tab_{context}"]
= Access control tab

[role="_abstract"]
The **Access control** tab allows the cluster owner to set up an identity provider, grant elevated permissions, and grant roles to other users.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-accesscontrol-tab-identity-providers_{context}"]
= Identity providers

[role="_abstract"]
You can create your cluster's identity provider in this section. See the _Additional resources_ for more information.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-accesscontrol-tab-cluster-roles-access_{context}"]
= Cluster roles and access

[role="_abstract"]
You can create a `dedicated-admins` role for {dedicated} clusters or `cluster-admins` role for {rosa-title} or {rosa-classic-title} clusters.

.Procedure
. Click the **Add user** button.
. Enter the ID of the user you want to grant cluster admin access.
. Select the appropriate group for your user. Either `dedicated-admins` for {dedicated} clusters, or `cluster-admins` for
OpenShift Container Platform
clusters.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-accesscontrol-tab-ocm-roles-access_{context}"]
= OCM roles and access

[role="_abstract"]
Use the following procedure to grant roles on the cluster.

.Prerequisites

* You must be the cluster owner or have the correct permissions to grant roles.

.Procedure

. Click the **Grant role** button.
. Enter the Red Hat account login for the user that you want to grant a role on the cluster.
. Select the role from following options:
** **Cluster editor** allows users or groups to manage or configure the cluster.
** **Cluster viewer** allows users or groups to view cluster details only.
** **Cluster autoscaler editor** allows users or groups to manage and configure the cluster autoscaler settings.
** **Identity provider editor** allows users or groups to manage and configure the identity providers.
** **Machine pool editor** allows users or groups to manage and configure the machine pools.
. Click the **Grant role** button on the dialog box.

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-accesscontrol-tab-transfer-ownership_{context}"]
= Transfer ownership

[role="_abstract"]
You can transfer your cluster to another user.

[NOTE]
====
Once you transfer cluster ownership, you lose access to the cluster.
====

.Procedure

. Select **Initiate transfer**.
. Enter the user name, account ID, and organization ID of the user that you are transferring the cluster to.
. Select **Initiate transfer**.

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-addons-tab_{context}"]
= Add-ons tab

[role="_abstract"]
The **Add-ons** tab displays all of the optional add-ons that can be added to the cluster. Select the desired add-on, and then select **Install** below the description for the add-on that displays.
The Add-ons tab is not currently supported on hosted control plane clusters.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-cluster-history-tab_{context}"]
= Cluster history tab

[role="_abstract"]
The **Cluster history** tab shows every change to the cluster from creation onward for each version. You can specify date ranges for your cluster history and use filters to search based on the description of the notification, the severity of the notification, the type of notification, and which role logged it. You may download your cluster history as a JSON or CSV file.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc
[id="ocm-networking-tab_{context}"]
= Networking tab

[role="_abstract"]
The **Networking** tab provides a control plane API endpoint as well as the default application router. Both the control plane API endpoint and the default application router can be made private by selecting the respective box below label. If applicable, you can also find your virtual private cloud (VPC) details on this tab.

You can change your application ingress to private or public by selecting the **Edit application ingress** button then checking or unchecking the "Make router private" checkbox.
Select the **Edit application ingress** button to edit the existing application ingress. You can change your application ingress to private or public by checking or unchecking the "Make router private" checkbox.

[IMPORTANT]
====
For Security Token Service (STS) installations, these options cannot be changed. STS installations also do not allow you to change privacy nor allow you to add an additional router.
====
[IMPORTANT]
====
{cluster-manager-first} does not support the networking tab for a {gcp-first}, non-CCS cluster running in a Red Hat {gcp-short} project.
====
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc
[id="ocm-networking-tab-adding-ingress_{context}"]
= Adding a network Ingress to your OpenShift Container Platform cluster

[role="_abstract"]
You can add a network Ingress to your cluster from the {cluster-manager-url} web UI.

.Prerequisites

* You have a Red Hat account.
* You have the required permissions to make changes to your cluster in {cluster-manager}.

.Procedure

. From the **Networking** tab in {cluster-manager}, click the **Additional application router** toggle to enable the Ingress. There are two options you can add to the additional router:
.. **Make router private**: This checkbox allows you to control cluster privacy. By default, your Ingress router is publicly exposed and allows anyone access. You can limit access to applications or websites you run on your cluster by selecting this checkbox. For example, if you only want internal employees to access this cluster, then using this option requires a private connection, such as a virtual private network (VPN) or virtual private cloud (VPC) peering connection.
.. **Label match for additional router**: This field provides a way to target the specific route you want exposed in this additional Ingress router. By default, the router exposes all routes. If you leave this field blank, these routes stay exposed.
+
A commonly used setup has a private default router, which means any applications deployed require a VPN or VPC peering to access. You can create an additional public router with a label match of  `route=external`. Then, if you add the `route=external` label to additional routes, the additional router matches this label and exposes it for public use.
. Click **Change settings** to confirm that you want to add the network Ingress.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-machinepools-tab_{context}"]
= Machine pools tab

[role="_abstract"]
The **Machine pools** tab allows the cluster owner to create new machine pools if there is enough available quota, or edit an existing machine pool.

Selecting the image:kebab.png[title=Other options] > **Edit** option opens the "Edit machine pool" dialog. In this dialog, you can change the node count per availability zone, edit node labels and taints, and view any associated AWS security groups.

Select the **Edit cluster autoscaling** button to specify your autoscaling strategy.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-support-tab_{context}"]
= Support tab

[role="_abstract"]
In the *Support* tab, you can add notification contacts for individuals that should receive cluster notifications. The username or email address that you provide must relate to a user account in the Red Hat organization where the cluster is deployed.
For the steps to add a notification contact, see _Adding cluster notification contacts_.

Also from this tab, you can open a support case to request technical support for your cluster.
// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-settings-tab_{context}"]
= Settings tab

[role="_abstract"]
The **Settings** tab provides a few options for the cluster owner:

* **Monitoring**, which is enabled by default, allows for reporting done on user-defined actions.
* **Update strategy** allows you to determine if the cluster automatically updates on a certain day of the week at a specified time or if all updates are scheduled manually.
* **Node draining** sets the duration that protected workloads are respected during updates. When this duration has passed, the node is forcibly removed.
* **Update status** shows the current version and if there are any updates available.

[id="ocm-additional-resources"]
== Additional resources
* {cluster-manager}
* Adding cluster notification contacts
* Configuring identity providers
* Understanding the monitoring stack
* Using {red-hat-lightspeed} to identify issues with your cluster
* Adding cluster notification contacts
