---
title: "Uninstalling the {js-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-jobset-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/jobset-uninstall
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Uninstalling the {js-operator}

[id="js-uninstall"]
= Uninstalling the {js-operator}

[role="_abstract"]
Uninstall the {js-operator} by using the OpenShift Container Platform web console to remove the Operator instance and its resources from your cluster.

//Uninstalling the {js-operator}
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/jobset-uninstall.adoc

[id="js-uninstall_{context}"]
= Uninstalling the {js-operator}

[role="_abstract"]
Uninstall the {js-operator} by using the OpenShift Container Platform web console to remove the Operator instance.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have installed the {js-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Operators* -> *Installed Operators*.

. Select `openshift-js-operator` from the *Project* dropdown list.

. Delete the `JobSetOperator` instance.
.. Click *{js-operator}* and select the *JobSetOperator* tab.
.. Click the Options menu {kebab} next to the *cluster* entry and select *Delete JobSetOperator*.
.. In the confirmation dialog, click *Delete*.

. Uninstall the {js-operator}.
.. Navigate to *Operators* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{js-operator}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

//Removing jobset resources
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/jobset-uninstall.adoc

[id="js-remove-resources_{context}"]
= Uninstalling {js-operator} resources

[role="_abstract"]
Optionally, after uninstalling the {js-operator}, you can remove its related resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have uninstalled the {js-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove CRDs that were created when the {js-operator} was installed:
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Enter `JobSetOperator` in the *Name* field to filter the CRDs.
.. Click the Options menu {kebab} next to the *JobSetOperator* CRD and select *Delete CustomResourceDefinition*.
.. In the confirmation dialog, click *Delete*.

. Delete the `openshift-jobset-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Fine `openshift-jobset-operator` in the list of namespaces.
.. Click the Options menu {kebab} next to the *openshift-jobset-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-jobset-operator` and click *Delete*.
