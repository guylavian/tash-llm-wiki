---
title: "Uninstalling the {secondary-scheduler-operator}"
type: reference
domain: openshift
slug: nodes-4-22-nodes-secondary-scheduler-uninstalling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-secondary-scheduler-uninstalling
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Uninstalling the {secondary-scheduler-operator}

[id="secondary-scheduler-uninstalling"]
= Uninstalling the {secondary-scheduler-operator}

[role="_abstract"]
If you no longer need the {secondary-scheduler-operator-full} in your cluster, you can uninstall the Operator and remove its related resources.

// Uninstalling the {secondary-scheduler-operator}
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-uninstalling.adoc

[id="nodes-secondary-scheduler-uninstall-console_{context}"]
= Uninstalling the {secondary-scheduler-operator}

[role="_abstract"]
You can use the web console to uninstall the {secondary-scheduler-operator-full} if you no longer need the Operator in your cluster.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* You have access to the OpenShift Container Platform web console.
* The {secondary-scheduler-operator-full} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Uninstall the {secondary-scheduler-operator-full} Operator.
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{secondary-scheduler-operator}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

// Removing {secondary-scheduler-operator} resources
// Module included in the following assemblies:
//
// * nodes/scheduling/secondary_scheduler/nodes-secondary-scheduler-uninstalling.adoc

[id="nodes-secondary-scheduler-remove-resources-console_{context}"]
= Removing {secondary-scheduler-operator} resources

[role="_abstract"]
Optionally, remove the custom resource definition (CRD) and associated namespace after the {secondary-scheduler-operator-full} is uninstalled. This cleans up all remaining secondary scheduler artifacts.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove the CRD that was installed by the {secondary-scheduler-operator}:
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Enter `SecondaryScheduler` in the *Name* field to filter the CRDs.
.. Click the Options menu {kebab} next to the *SecondaryScheduler* CRD and select *Delete Custom Resource Definition*:

. Remove the `openshift-secondary-scheduler-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Click the Options menu {kebab} next to the *openshift-secondary-scheduler-operator* and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-secondary-scheduler-operator` in the field and click *Delete*.
