---
title: "Uninstalling the {lws-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-lws-uninstalling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/lws-uninstalling
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Uninstalling the {lws-operator}

[id="lws-uninstalling"]
= Uninstalling the {lws-operator}

[role="_abstract"]
If you no longer need the {lws-operator} in your cluster, you can uninstall the Operator and remove its related resources.

// Uninstalling the {lws-operator}
// Module included in the following assemblies:
//
// * ai_workloads/leader_worker_set/lws-uninstalling.adoc

[id="lws-uninstall_{context}"]
= Uninstalling the {lws-operator}

[role="_abstract"]
You can use the web console to uninstall the {lws-operator} if you no longer need the Operator in your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have installed the {lws-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Operators* -> *Installed Operators*.

. Select `openshift-lws-operator` from the *Project* dropdown list.

. Delete the `LeaderWorkerSetOperator` instance.
.. Click *{lws-operator}* and select the *LeaderWorkerSetOperator* tab.
.. Click the Options menu {kebab} next to the *cluster* entry and select *Delete LeaderWorkerSetOperator*.
.. In the confirmation dialog, click *Delete*.

. Uninstall the {lws-operator}.
.. Navigate to *Operators* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{lws-operator}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

// Removing {lws-operator} resources
// Module included in the following assemblies:
//
// * ai_workloads/leader_worker_set/lws-uninstalling.adoc

[id="lws-remove-resources_{context}"]
= Uninstalling {lws-operator} resources

[role="_abstract"]
Optionally, remove custom resources (CRs) and the associated namespace after the {lws-operator} is uninstalled. This cleans up all remaining Leader Worker Set artifacts.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have uninstalled the {lws-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove CRDs that were created when the {lws-operator} was installed:
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Enter `LeaderWorkerSetOperator` in the *Name* field to filter the CRDs.
.. Click the Options menu {kebab} next to the *LeaderWorkerSetOperator* CRD and select *Delete CustomResourceDefinition*.
.. In the confirmation dialog, click *Delete*.

. Delete the `openshift-lws-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Enter `openshift-lws-operator` into the filter box.
.. Click the Options menu {kebab} next to the *openshift-lws-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-lws-operator` and click *Delete*.
