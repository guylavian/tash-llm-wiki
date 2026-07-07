---
title: "Uninstalling the {run-once-operator}"
type: reference
domain: openshift
slug: nodes-4-22-run-once-duration-override-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/run-once-duration-override-uninstall
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Uninstalling the {run-once-operator}

[id="run-once-duration-override-uninstall"]
= Uninstalling the {run-once-operator}

You can remove the {run-once-operator} from OpenShift Container Platform by uninstalling the Operator and removing its related resources.

// Uninstalling the {run-once-operator}
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-uninstall.adoc

[id="rodoo-uninstall-operator_{context}"]
= Uninstalling the {run-once-operator}

You can use the web console to uninstall the {run-once-operator}. Uninstalling the {run-once-operator} does not unset the `activeDeadlineSeconds` field for run-once pods, but it will no longer apply the override value to future run-once pods.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have installed the {run-once-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Select `openshift-run-once-duration-override-operator` from the *Project* dropdown list.

. Delete the `RunOnceDurationOverride` instance.
.. Click *{run-once-operator}* and select the *Run Once Duration Override* tab.
.. Click the Options menu {kebab} next to the *cluster* entry and select *Delete RunOnceDurationOverride*.
.. In the confirmation dialog, click *Delete*.

. Uninstall the {run-once-operator}.
.. Navigate to *Ecosystem* -> *Installed Operators*.
.. Click the Options menu {kebab} next to the *{run-once-operator}* entry and click *Uninstall Operator*.
.. In the confirmation dialog, click *Uninstall*.

// Removing {run-once-operator} resources
// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-uninstall.adoc

[id="rodoo-uninstall-resources_{context}"]
= Uninstalling {run-once-operator} resources

Optionally, after uninstalling the {run-once-operator}, you can remove its related resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have uninstalled the {run-once-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Remove CRDs that were created when the {run-once-operator} was installed:
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Enter `RunOnceDurationOverride` in the *Name* field to filter the CRDs.
.. Click the Options menu {kebab} next to the *RunOnceDurationOverride* CRD and select *Delete CustomResourceDefinition*.
.. In the confirmation dialog, click *Delete*.

. Delete the `openshift-run-once-duration-override-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Enter `openshift-run-once-duration-override-operator` into the filter box.
.. Click the Options menu {kebab} next to the *openshift-run-once-duration-override-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-run-once-duration-override-operator` and click *Delete*.

. Remove the run-once duration override label from the namespaces that it was enabled on.

.. Navigate to *Administration* -> *Namespaces*.
.. Select your namespace.
.. Click *Edit* next to the *Labels* field.
.. Remove the *runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true* label and click *Save*.
