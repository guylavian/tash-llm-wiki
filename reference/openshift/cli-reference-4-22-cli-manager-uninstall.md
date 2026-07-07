---
title: "Uninstalling the {cli-manager}"
type: reference
domain: openshift
slug: cli-reference-4-22-cli-manager-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/cli-manager-uninstall
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Uninstalling the {cli-manager}

[id="cli-manager-uninstall"]
= Uninstalling the {cli-manager}

You can remove the {cli-manager} from OpenShift Container Platform by uninstalling the {cli-manager} and removing its related resources.

// Uninstalling the {cli-manager}
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-uninstall.adoc

[id="cli-manager-uninstalling_{context}"]
= Uninstalling the {cli-manager}

You can uninstall the {cli-manager} by using the web console.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.
* The {cli-manager} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Uninstall the {cli-manager} by completing the following steps:
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{cli-manager}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

// Uninstalling the related resources
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-uninstall.adoc

[id="cli-manager-remove-resources_{context}"]
= Removing {cli-manager} resources

Optionally, after you uninstall the {cli-manager}, you can remove its related resources from your cluster.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove the `openshift-cli-manager-operator` namespace:
.. Navigate to *Administration* -> *Namespaces*.
.. Click the Options menu {kebab} next to the *openshift-cli-manager-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-cli-manager-operator` in the field and click *Delete*.
