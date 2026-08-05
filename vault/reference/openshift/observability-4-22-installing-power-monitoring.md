---
title: "Installing {PM-title}"
type: reference
domain: openshift
slug: observability-4-22-installing-power-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/installing-power-monitoring
version: 4.22
family: observability
documentKind: "Documentation"
---

# Installing {PM-title}

[id="installing-power-monitoring"]
= Installing {PM-title}

You can install {PM-title} by deploying the {PM-operator} in the OpenShift Container Platform web console.

//Installing power monitoring operator
// Module included in the following assemblies:

// * power_monitoring/installing-power-monitoring.adoc

[id="power-monitoring-installing-pmo_{context}"]
= Installing the {PM-operator}

As a cluster administrator, you can install the {PM-operator} from the software catalog by using the OpenShift Container Platform web console.

[WARNING]
====
You must remove any previously installed versions of the {PM-operator} before installation.
====

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.

.Procedure

. In the web console, go to *Ecosystem* -> *Software Catalog*.

. Search for `{PM-shortname}`, click the *{PM-title-c}* tile, and then click *Install*.
//. On the *Install Operator* page:
//.. Select an *Update channel*.
//.. Select a {PM-shortname} *Version* to install.
// This can be included once the user has options there to choose. Not needed for now.

. Click *Install* again to install the {PM-operator}.
+
{PM-title-c} is now available in all namespaces of the OpenShift Container Platform cluster.

.Verification

. Verify that the {PM-operator} is listed in *Ecosystem* -> *Installed Operators*. The *Status* should resolve to *Succeeded*.

// Deploying Kepler
// Module included in the following assemblies:

// * power_monitoring/installing-power-monitoring.adoc

[id="power-monitoring-deploying-power-monitor-custom-resource_{context}"]
= Deploying PowerMonitor custom resource

You can deploy {PM-kepler} by creating an instance of the `PowerMonitor` custom resource (CR) using the {PM-operator}.

[IMPORTANT]
====
The `Kepler` custom resource definition (CRD) has been deprecated and will be removed in a future release. Use the `PowerMonitor` custom resource instead.
====

.Prerequisites
* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.
* You have installed the {PM-operator}.

.Procedure

. In the web console, go to *Ecosystem* -> *Installed Operators*.

. Click *{PM-title-c}* from the *Installed Operators* list and go to the *PowerMonitor* tab.

. Click *Create PowerMonitor*.

. On the *Create PowerMonitor* page, ensure the *Name* is set to `power-monitor`.
+
[IMPORTANT]
====
The name of your `PowerMonitor` instance must be set to `power-monitor`. All other instances are ignored by the {PM-operator}.
====

. Click *Create* to deploy the PowerMonitor and {PM-shortname} dashboards.

//formerly Deploying Kepler.
//Kepler CRDs are being removed from TP 0.5 and being replaced with PowerMonitor CRDs.
