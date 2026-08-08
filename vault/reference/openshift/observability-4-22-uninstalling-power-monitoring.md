---
title: "Uninstalling {PM-shortname}"
type: reference
domain: openshift
slug: observability-4-22-uninstalling-power-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/uninstalling-power-monitoring
version: 4.22
family: observability
documentKind: "Documentation"
---

# Uninstalling {PM-shortname}

[id="uninstalling-power-monitoring"]
= Uninstalling {PM-shortname}

You can uninstall {PM-shortname} by deleting the {PM-kepler} instance and then the {PM-operator} in the OpenShift Container Platform web console.

// Removing kepler
// Module included in the following assemblies:

// * power_monitoring/uninstalling-power-monitoring.adoc

[id="power-monitoring-deleting-kepler_{context}"]
= Deleting {PM-kepler}

You can delete {PM-kepler} by removing the {PM-kepler} instance of the `{PM-kepler}` custom resource definition (CRD) from the OpenShift Container Platform web console.

[IMPORTANT]
====
Starting with {PM-title} 0.5 (Technology Preview), use the `PowerMonitor` CRD, and remove all instances of the `Kepler` CRD.
====

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.

.Procedure

. In the web console, go to *Ecosystem* -> *Installed Operators*.

. Click *{PM-title-c}* from the *Installed Operators* list and go to the *{PM-kepler}* tab.

. Locate the {PM-kepler} instance entry in the list.

. Click {kebab} for this entry and select *Delete {PM-kepler}*.

. In the *Delete {PM-kepler}?* dialog, click *Delete* to delete the {PM-kepler} instance.

//might need Additional resource section to add link to configuring PowerMonitor CRD content when that content is ready

// Removing PowerMonitor CRD
// Module included in the following assemblies:

// * power_monitoring/uninstalling-power-monitoring.adoc

[id="power-monitoring-deleting-power-monitoring-custom-resource_{context}"]
= Deleting the PowerMonitor custom resource

You can delete the `PowerMonitor` custom resource (CR) by removing the `power-monitor` instance of the `PowerMonitor` CR from the OpenShift Container Platform web console.

.Prerequisites

* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.

.Procedure

. In the web console, go to *Ecosystem* -> *Installed Operators*.

. Click *{PM-title-c}* from the *Installed Operators* list and go to the *PowerMonitor* tab.

. Locate the *PowerMonitor* instance entry in the list.

. Click the {kebab} for this entry and select *Delete PowerMonitor*.

. In the *Delete PowerMonitor?* dialog, click *Delete* to delete the `PowerMonitor` instance.

// Uninstalling power monitoring operator
// Module included in the following assemblies:

// * power_monitoring/uninstalling-power-monitoring.adoc

[id="power-monitoring-uninstalling-pmo_{context}"]
= Uninstalling the {PM-operator}

If you installed the {PM-operator} by using the software catalog, you can uninstall it from the OpenShift Container Platform web console.

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.

.Procedure

. Delete the {PM-kepler} instance.
+
[WARNING]
====
Ensure that you have deleted the {PM-kepler} instance before uninstalling the {PM-operator}.
====

. Go to *Ecosystem* -> *Installed Operators*.

. Locate the *{PM-title-c}* entry in the list.

. Click {kebab} for this entry and select *Uninstall Operator*.

. In the *Uninstall Operator?* dialog, click *Uninstall* to uninstall the {PM-operator}.
