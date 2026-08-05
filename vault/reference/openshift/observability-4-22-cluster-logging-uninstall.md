---
title: "Uninstalling Logging"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-uninstall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-uninstall
version: 4.22
family: observability
documentKind: "Documentation"
---

# Uninstalling Logging

[id="cluster-logging-uninstall"]
= Uninstalling Logging

You can remove {logging} from your OpenShift Container Platform cluster by removing installed Operators and related custom resources (CRs).

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-uninstall.adoc

[id="uninstall-cluster-logging-operator_{context}"]
= Uninstalling the {logging}

You can stop aggregating logs by deleting the {clo} and the `ClusterLogging` custom resource (CR).

.Prerequisites

* Have access to the OpenShift Container Platform web console as a user with `cluster-admin` privileges.

.Procedure

. Go to the *Administration* -> *Custom Resource Definitions* page, and click *ClusterLogging*.

. On the *Custom Resource Definition Details* page, click *Instances*.

. Click the Options menu {kebab} next to the instance, and click *Delete ClusterLogging*.

. Go to the *Administration* -> *Custom Resource Definitions* page.

. Click the Options menu {kebab} next to *ClusterLogging*, and select *Delete Custom Resource Definition*.
+
[WARNING]
====
Deleting the `ClusterLogging` CR does not remove the persistent volume claims (PVCs). To delete the remaining PVCs, persistent volumes (PVs), and associated data, you must take further action. Releasing or deleting PVCs can delete PVs and cause data loss.
====

. If you have created a `ClusterLogForwarder` CR, click the Options menu {kebab} next to *ClusterLogForwarder*, and then click *Delete Custom Resource Definition*.

. Go to the *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} next to the {clo}, and then click *Uninstall Operator*.

. Optional: Delete the `openshift-logging` project.
+
[WARNING]
====
Deleting the `openshift-logging` project deletes everything in that namespace, including any persistent volume claims (PVCs). If you want to preserve logging data, do not delete the `openshift-logging` project.
====

.. Go to the *Home* -> *Projects* page.
.. Click the Options menu {kebab} next to the *openshift-logging* project, and then click *Delete Project*.
.. Confirm the deletion by typing `openshift-logging` in the dialog box, and then click *Delete*.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-uninstall.adoc

[id="uninstall-logging-delete-pvcs_{context}"]
= Deleting logging PVCs

To keep persistent volume claims (PVCs) for reuse with other pods, keep the labels or PVC names that you need to reclaim the PVCs.
If you do not want to keep the PVCs, you can delete them. If you want to recover storage space, you can also delete the persistent volumes (PVs).

.Prerequisites

* You have administrator permissions.
* Have access to the OpenShift Container Platform web console as a user with `cluster-admin` privileges.

.Procedure

. Go to the *Storage* -> *Persistent Volume Claims* page.
. Click the Options menu {kebab} next to each PVC, and select *Delete Persistent Volume Claim*.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-uninstall.adoc

[id="uninstall-loki-operator_{context}"]
= Uninstalling Loki

.Prerequisites

* You have administrator permissions.
* You have access to the OpenShift Container Platform web console with `cluster-admin` privleges.
* If you have not already removed the {clo} and related resources, you have removed references to LokiStack from the `ClusterLogging` custom resource.

.Procedure

. Go to the *Administration* -> *Custom Resource Definitions* page, and click *LokiStack*.

. On the *Custom Resource Definition Details* page, click *Instances*.

. Click the Options menu {kebab} next to the instance, and then click *Delete LokiStack*.

. Go to the *Administration* -> *Custom Resource Definitions* page.

. Click the Options menu {kebab} next to *LokiStack*, and select *Delete Custom Resource Definition*.

. Delete the object storage secret.

. Go to the *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} next to the {loki-op}, and then click *Uninstall Operator*.

. Optional: Delete the `openshift-operators-redhat` project.
+
[IMPORTANT]
====
Do not delete the `openshift-operators-redhat` project if other global Operators are installed in this namespace.
====

.. Go to the *Home* -> *Projects* page.
.. Click the Options menu {kebab} next to the *openshift-operators-redhat* project, and then click *Delete Project*.
.. Confirm the deletion by typing `openshift-operators-redhat` in the dialog box, and then click *Delete*.
// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-uninstall.adoc

[id="uninstall-es-operator_{context}"]
= Uninstalling Elasticsearch

.Prerequisites

* You have administrator permissions.
* Have access to the OpenShift Container Platform web console as a user with `cluster-admin` privileges.
* If you have not already removed the {clo} and related resources, you must remove references to Elasticsearch from the `ClusterLogging` custom resource.

.Procedure

. Go to the *Administration* -> *Custom Resource Definitions* page, and click *Elasticsearch*.

. On the *Custom Resource Definition Details* page, click *Instances*.

. Click the Options menu {kebab} next to the instance, and then click *Delete Elasticsearch*.

. Go to the *Administration* -> *Custom Resource Definitions* page.

. Click the Options menu {kebab} next to *Elasticsearch*, and select *Delete Custom Resource Definition*.

. Delete the object storage secret.

. Go to the *Ecosystem* -> *Installed Operators* page.

. Click the Options menu {kebab} next to the {es-op}, and then click *Uninstall Operator*.

. Optional: Delete the `openshift-operators-redhat` project.
+
[IMPORTANT]
====
Do not delete the `openshift-operators-redhat` project if other global Operators are installed in this namespace.
====

.. Go to the *Home* -> *Projects* page.
.. Click the Options menu {kebab} next to the *openshift-operators-redhat* project, and then click *Delete Project*.
.. Confirm the deletion by typing `openshift-operators-redhat` in the dialog box, and then click *Delete*.

//Generic deleting operators from a cluster using CLI
// Module included in the following assemblies:
//
// * operators/admin/olm-deleting-operators-from-a-cluster.adoc
// * serverless/install/removing-openshift-serverless.adoc

[id="olm-deleting-operator-from-a-cluster-using-cli_{context}"]
= Deleting Operators from a cluster using the CLI

Cluster administrators can delete installed Operators from a selected namespace by using the CLI.

.Prerequisites

- You have access to the OpenShift Container Platform cluster using an account with
`cluster-admin` permissions.
`dedicated-admin` permissions.
- The OpenShift CLI (`oc`) is installed on your workstation.

.Procedure

. Ensure the latest version of the subscribed operator (for example, `serverless-operator`) is identified in the `currentCSV` field.
+
[source,terminal]
----
$ oc get subscription.operators.coreos.com serverless-operator -n openshift-serverless -o yaml | grep currentCSV
----
+
.Example output
[source,terminal]
----
  currentCSV: serverless-operator.v1.28.0
----

. Delete the subscription (for example, `serverless-operator`):
+
[source,terminal]
----
$ oc delete subscription.operators.coreos.com serverless-operator -n openshift-serverless
----
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com "serverless-operator" deleted
----

. Delete the CSV for the Operator in the target namespace using the `currentCSV` value from the previous step:
+
[source,terminal]
----
$ oc delete clusterserviceversion serverless-operator.v1.28.0 -n openshift-serverless
----
+
.Example output
[source,terminal]
----
clusterserviceversion.operators.coreos.com "serverless-operator.v1.28.0" deleted
----

[role="_additional-resources"]
.Additional resources
* Reclaiming a persistent volume manually
* Reclaiming a persistent volume manually
