---
title: "Adding services to a cluster using {cluster-manager-first} console"
type: reference
domain: openshift
slug: adding-service-cluster-4-22-adding-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/adding_service_cluster/adding-service
version: 4.22
family: adding_service_cluster
documentKind: "Documentation"
---

# Adding services to a cluster using {cluster-manager-first} console

[id="adding-service"]
= Adding services to a cluster using {cluster-manager-first} console

You can add, access, and remove add-on services for your OpenShift Container Platform
(ROSA)
cluster by using {cluster-manager-first}.

== Prerequisites
* For the Amazon CloudWatch service, you must first install the `cluster-logging-operator` using the ROSA CLI (`rosa`).

// Module included in the following assemblies:
//
// * assemblies/adding-service.adoc

[id="adding-service-existing_{context}"]

= Adding an add-on service to a cluster

You can add an add-on service to an existing OpenShift Container Platform
(ROSA)
cluster by using {cluster-manager-first}.

.Prerequisites

* You have created and provisioned a cluster for OpenShift Container Platform.
* Your cluster meets all of the prerequisites for the service that you want to add on to your cluster.
* For paid add-on services, note the following considerations:
** If the organization has sufficient quota, and if the service is compatible with the cluster, the service appears in {cluster-manager}.
** If the organization has never had quota, or if the cluster is not compatible, then the service does not display.
** If the organization had quota in the past, but the quota is currently `0`, the service is still visible but disabled in {cluster-manager} until you get more quota.

// TODO: Could this just be one of the above prereqs instead of its own NOTE?
[NOTE]
====
To add a service to a cluster, you must be the cluster owner.
====

.Procedure

. Navigate to the *Cluster List* page in  {cluster-manager-url}.

. Select the cluster you want to add a service to.

. Click the *Add-ons* tab.

. Click the service option you want to add, click *Install*. An installing icon appears, indicating that the service has begun installing.
+
A green check mark appears in the service option when the installation is complete. You might have to refresh your browser to see the installation status.

. When the service is *Installed*, click *View in console* to access the service.
// Module included in the following assemblies:
//
// * assemblies/adding-service.adoc

[id="access-service_{context}"]

= Accessing installed add-on services on your cluster

After you successfully install an add-on service on your OpenShift Container Platform
(ROSA)
cluster, you can access the service by using the OpenShift web console.

.Prerequisites

* You have successfully installed a service on your OpenShift Container Platform cluster.

.Procedure

. Navigate to the *Cluster List* page in {cluster-manager-url}.

. Select the cluster with an installed service you want to access.

. Navigate to the *Add-ons* tab, and locate the installed service that you want to access.

. Click *View on console* from the service option to open the OpenShift web console.

. Enter your credentials to log in to the OpenShift web console.

. Click the *Red Hat Applications* menu by clicking the three-by-three matrix icon in the upper right corner of the main screen.

. Select the service you want to open from the drop-down menu. A new browser tab opens and you are required to authenticate through Red Hat Single Sign-On.

You have now accessed your service and can begin using it.
// Module included in the following assemblies:
//
// * assemblies/adding-service.adoc

[id="deleting-service_{context}"]
= Deleting an add-on service using {cluster-manager-first}

You can delete an add-on service from your OpenShift Container Platform
(ROSA)
cluster by using {cluster-manager-first}.

.Procedure

. Navigate to the *Cluster List* page in {cluster-manager-url}.

. Click the cluster with the installed service that you want to delete.

. Navigate to the *Add-ons* tab, and locate the installed service that you want to delete.

. From the installed service option, click the menu and select *Uninstall add-on* from the drop-down menu.

. You must type the name of the service that you want to delete in the confirmation message that appears.

. Click *Uninstall*. You are returned to the *Add-ons* tab and an uninstalling state icon is present on the service option you deleted.
//include::modules/deleting-service-cli.adoc[leveloffset=+1]
