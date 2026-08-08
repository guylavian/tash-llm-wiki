---
title: "Uninstalling the {descheduler-operator}"
type: reference
domain: openshift
slug: nodes-4-22-nodes-descheduler-uninstalling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-descheduler-uninstalling
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Uninstalling the {descheduler-operator}

[id="nodes-descheduler-uninstalling"]
= Uninstalling the {descheduler-operator}

[role="_abstract"]
If you no longer need the {descheduler-operator} in your cluster, you can uninstall the Operator and remove its related resources.

// Uninstalling the descheduler
// Module included in the following assemblies:
//
// * nodes/scheduling/descheduler/nodes-descheduler-uninstalling.adoc

[id="nodes-descheduler-uninstalling_{context}"]
= Uninstalling the descheduler

[role="_abstract"]
If you no longer need the descheduler in your cluster, you can remove it by deleting the descheduler instance and uninstalling the {descheduler-operator}. You can also delete the `KubeDescheduler` CRD and `openshift-kube-descheduler-operator` namespace.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.
* Access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.
. Delete the descheduler instance.
.. From the *Ecosystem* -> *Installed Operators* page, click *{descheduler-operator}*.
.. Select the *Kube Descheduler* tab.
.. Click the Options menu {kebab} next to the *cluster* entry and select *Delete KubeDescheduler*.
.. In the confirmation dialog, click *Delete*.
. Uninstall the {descheduler-operator}.
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{descheduler-operator}* entry and select *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.
. Delete the `openshift-kube-descheduler-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Enter `openshift-kube-descheduler-operator` into the filter box.
.. Click the Options menu {kebab} next to the *openshift-kube-descheduler-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-kube-descheduler-operator` and click *Delete*.
. Delete the `KubeDescheduler` CRD.
.. Navigate to *Administration* -> *Custom Resource Definitions*.
.. Enter `KubeDescheduler` into the filter box.
.. Click the Options menu {kebab} next to the *KubeDescheduler* entry and select *Delete CustomResourceDefinition*.
.. In the confirmation dialog, click *Delete*.
