---
title: "Red Hat OpenShift Cluster Manager"
type: reference
domain: openshift
slug: architecture-4-22-ocm-overview-ocp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/ocm-overview-ocp
version: 4.22
family: architecture
documentKind: "Documentation"
---

# Red Hat OpenShift Cluster Manager

[id="ocm-overview-ocp"]
= Red Hat OpenShift Cluster Manager

{cluster-manager-first} is a managed service where you can install, modify, operate, and upgrade your Red Hat OpenShift clusters. This service allows you to work with all of your organization´s clusters from a single dashboard.

{cluster-manager} guides you to install {OCP}, {rosa-classic-title}, {hcp-title-first}, and {dedicated} clusters. It is also responsible for managing both {OCP} clusters after self-installation as well as your {rosa-classic-title} and {dedicated} clusters.

You can use {cluster-manager} to do the following actions:

* Create new clusters
* View cluster details and metrics
* Manage your clusters with tasks such as scaling, changing node labels, networking, authentication
* Manage access control
* Monitor clusters
* Schedule upgrades

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

[id="ocm-general-actions-ocp"]
== General actions

On the top right of the cluster page, there are some actions that a user can perform on the entire cluster:

* **Open console** launches a web console so that the cluster owner can issue commands to the cluster.
* **Actions** drop-down menu allows the cluster owner to rename the display name of the cluster, change the amount of load balancers and persistent storage on the cluster, if applicable, manually set the node count, and delete the cluster.
* **Refresh** icon forces a refresh of the cluster.

[id="ocm-cluster-tabs-ocp"]
== Cluster tabs

Selecting an active, installed cluster shows tabs associated with that cluster. The following tabs display after the cluster's installation completes:

* Overview
* Access control
* Add-ons
* Networking
* Machine pools
* {red-hat-lightspeed} Advisor
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

[id="ocm-addons-tab_{context}"]
= Add-ons tab

[role="_abstract"]
The **Add-ons** tab displays all of the optional add-ons that can be added to the cluster. Select the desired add-on, and then select **Install** below the description for the add-on that displays.
The Add-ons tab is not currently supported on hosted control plane clusters.

// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc

[id="ocm-insightsadvisor-tab_{context}"]
= {red-hat-lightspeed} Advisor tab

The **{red-hat-lightspeed} Advisor** tab uses the Remote Health functionality of the OpenShift Container Platform to identify and mitigate risks to security, performance, availability, and stability. See Using {red-hat-lightspeed} to identify issues with your cluster in the {OCP} documentation.

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

[id="ocm-additional-resources-ocp"]
== Additional resources

* For the complete documentation for {cluster-manager}, see {cluster-manager} documentation.
