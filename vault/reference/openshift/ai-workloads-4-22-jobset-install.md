---
title: "Installing the {js-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-jobset-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/jobset-install
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Installing the {js-operator}

[id="js-install"]
= Installing the {js-operator}

[role="_abstract"]
Install the {js-operator} on OpenShift Container Platform to enable management of large-scale, coordinated computing workloads, giving your applications a unified API and failure recovery.

// Installing the {js-operator}
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/jobset-install.adoc

[id="js-install_{context}"]
= Installing the {js-operator}

[role="_abstract"]
Install the {js-operator} on OpenShift Container Platform using the web console to begin managing large-scale, coordinated computing workloads.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* You have installed the {cert-manager-operator}.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Verify that the {cert-manager-operator} is installed.

. Install the {js-operator}.
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. Search for and select the *`openshift-operators`* project.
.. Enter *{js-operator}* into the filter box.
.. Select the *{js-operator}* and click *Install*.
.. On the *Install Operator* page:
... The *Update channel* is set to *stable-v1.0*, which installs the latest stable release of {js-operator}.
... Under *Installation mode*, select *A specific namespace on the cluster*.
... Under *Installed Namespace*, select *Operator recommended Namespace: openshift-jobset-operator*.
... Under *Update approval*, select one of the following update strategies:
+
* The *Automatic* strategy allows {olm-first} to automatically update the Operator when a new version is available.
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.
... Click *Install*.

. Create the custom resource (CR) for the {js-operator}:
.. Navigate to *Installed Operators* -> *{js-operator}*.
.. Under *Provided APIs*, click *Create instance* in the *JobSetOperator* pane.
.. Set the name to *cluster*.
.. Set the *managementState* to *Managed*.
.. Click *Create*.

.Verification

* Check that the {js-operator} and operand pods are running by entering the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-jobset-operator
----
+
.Example output
[source,terminal]
----
NAME                                        READY   STATUS    RESTARTS   AGE
jobset-controller-manager-5595547fb-b4g2x   1/1     Running   0          48s
jobset-operator-596cb848c6-q2dmp            1/1     Running   0          2m33s
----
