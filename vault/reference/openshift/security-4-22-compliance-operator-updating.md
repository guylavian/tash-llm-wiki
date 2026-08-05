---
title: "Updating the Compliance Operator"
type: reference
domain: openshift
slug: security-4-22-compliance-operator-updating
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/compliance-operator-updating
version: 4.22
family: security
documentKind: "Documentation"
---

# Updating the Compliance Operator

[id="compliance-operator-updating"]
= Updating the Compliance Operator

As a cluster administrator, you can update the Compliance Operator on your OpenShift Container Platform cluster.
//
// This will be un-commented for OCP 4.11-4.14 releases. Commented out in the main branch.
//
// [IMPORTANT]
// ====
// It is recommended to update the Compliance Operator to version 1.3.1 or later before updating your OpenShift Container Platform cluster to version 4.14 or later.
// ====

[IMPORTANT]
====
Updating your OpenShift Container Platform cluster to version 4.14 might cause the Compliance Operator to not work as expected. This is due to an ongoing known issue. For more information, see OCPBUGS-18025.
====
//
// This note will be updated with the release of CO 1.3.1 to state the following in branches 4.11-4.14:
//
// [IMPORTANT]
// ====
// It is recommended to update the Compliance Operator to version 1.3.1 or later before updating your OpenShift Container Platform cluster to version 4.14 or later. For more information, see (OCPBUGS-18025).
// ====

// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc

[id="olm-preparing-upgrade_{context}"]
= Preparing for an Operator update

The subscription of an installed Operator specifies an update channel that tracks and receives updates for the Operator. You can change the update channel to start tracking and receiving updates from a newer channel.

The names of update channels in a subscription can differ between Operators, but the naming scheme typically follows a common convention within a given Operator. For example, channel names might follow a minor release update stream for the application provided by the Operator (`1.2`, `1.3`) or a release frequency (`stable`, `fast`).

[NOTE]
====
You cannot change installed Operators to a channel that is older than the current channel.
====

Red Hat Customer Portal Labs include the following application that helps administrators prepare to update their Operators:

* Red Hat OpenShift Container Platform Operator Update Information Checker

You can use the application to search for Operator Lifecycle Manager-based Operators and verify the available Operator version per update channel across different versions of OpenShift Container Platform. Cluster Version Operator-based Operators are not included.

// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc

[id="olm-changing-update-channel_{context}"]
= Changing the update channel for an Operator

You can change the update channel for an Operator by using the OpenShift Container Platform web console.

[TIP]
====
If the approval strategy in the subscription is set to *Automatic*, the update process initiates as soon as a new Operator version is available in the selected channel. If the approval strategy is set to *Manual*, you must manually approve pending updates.
====

.Prerequisites

* An Operator previously installed using Operator Lifecycle Manager (OLM).

.Procedure

. In web console, navigate to *Ecosystem* -> *Installed Operators*.

. Click the name of the Operator you want to change the update channel for.

. Click the *Subscription* tab.

. Click the name of the update channel under *Update channel*.

. Click the newer update channel that you want to change to, then click *Save*.

. For subscriptions with an *Automatic* approval strategy, the update begins automatically. Navigate back to the *Ecosystem* -> *Installed Operators* page to monitor the progress of the update. When complete, the status changes to *Succeeded* and *Up to date*.
+
For subscriptions with a *Manual* approval strategy, you can manually approve the update from the *Subscription* tab.

// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc
// * virt/updating/upgrading-virt.adoc

[id="olm-approving-pending-upgrade_{context}"]
= Manually approving a pending Operator update

[role="_abstract"]
If an installed Operator has the approval strategy in its subscription set to *Manual*, when new updates are released in its current update channel, the update must be manually approved before installation can begin.

.Prerequisites

* An Operator previously installed using {olm-first}.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators*.

. Operators that have a pending update display a status with *Upgrade available*. Click the name of the Operator you want to update.

. Click the *Subscription* tab. Any updates requiring approval are displayed next to *Upgrade status*. For example, it might display *1 requires approval*.

. Click *1 requires approval*, then click *Preview Install Plan*.

. Review the resources that are listed as available for update. When satisfied, click *Approve*.

. Navigate back to the *Ecosystem* -> *Installed Operators* page to monitor the progress of the update. When complete, the status changes to *Succeeded* and *Up to date*.

// [id="additional-resources-updating-the-compliance-operator"]
// [role="_additional-resources"]
// == Additional resources
//
// * For more information, see xref:../../../operators/admin/
