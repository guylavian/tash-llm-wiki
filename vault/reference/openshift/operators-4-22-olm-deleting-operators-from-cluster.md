---
title: "Deleting Operators from a cluster"
type: reference
domain: openshift
slug: operators-4-22-olm-deleting-operators-from-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-deleting-operators-from-cluster
version: 4.22
family: operators
documentKind: "Documentation"
---

# Deleting Operators from a cluster

[id="olm-deleting-operators-from-a-cluster"]
= Deleting Operators from a cluster

The following describes how to delete, or uninstall, Operators that were previously installed using Operator Lifecycle Manager (OLM) on your OpenShift Container Platform cluster.

[IMPORTANT]
====
You must successfully and completely uninstall an Operator prior to attempting to reinstall the same Operator. Failure to fully uninstall the Operator properly can leave resources, such as a project or namespace, stuck in a "Terminating" state and cause "error resolving resource" messages to be observed when trying to reinstall the Operator.

For more information, see Reinstalling Operators after failed uninstallation.
====

// Module included in the following assemblies:
//
// * operators/admin/olm-deleting-operators-from-a-cluster.adoc
// * backup_and_restore/application_backup_and_restore/installing/uninstalling-oadp.adoc
// * serverless/install/removing-openshift-serverless.adoc
// * virt/install/uninstalling-virt.adoc

[id="olm-deleting-operators-from-a-cluster-using-web-console_{context}"]
= Deleting Operators from a cluster using the web console

[role="_abstract"]
Cluster administrators can delete installed Operators from a selected namespace by using the web console.

.Prerequisites

- You have access to the OpenShift Container Platform cluster web console using an account with
`cluster-admin` permissions.
`dedicated-admin` permissions.

.Procedure

. Navigate to the *Ecosystem* -> *Installed Operators* page.

. Scroll or enter a keyword into the *Filter by name* field to find the Operator that you want to remove. Then, click on it.

. On the right side of the *Operator Details* page, select *Uninstall Operator* from the *Actions* list.
+
An *Uninstall Operator?* dialog box is displayed.

. Select *Uninstall* to remove the Operator, Operator deployments, and pods. Following this action, the Operator stops running and no longer receives updates.
+
[NOTE]
====
This action does not remove resources managed by the Operator, including custom resource definitions (CRDs) and custom resources (CRs). Dashboards and navigation items enabled by the web console and off-cluster resources that continue to run might need manual clean up. To remove these after uninstalling the Operator, you might need to manually delete the Operator CRDs.
====

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

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc
// * serverless/install/removing-openshift-serverless.adoc

[id="olm-refresh-subs_{context}"]
= Refreshing failing subscriptions

[role="_abstract"]
In Operator Lifecycle Manager (OLM), if you subscribe to an Operator that references images that are not accessible on your network, you can find jobs in the `openshift-marketplace` namespace that are failing with the following errors:

.Example output
[source,terminal]
----
ImagePullBackOff for
Back-off pulling image "example.com/openshift4/ose-elasticsearch-operator-bundle@sha256:6d2587129c846ec28d384540322b40b05833e7e00b25cca584e004af9a1d292e"
----

.Example output
[source,terminal]
----
rpc error: code = Unknown desc = error pinging docker registry example.com: Get "https://example.com/v2/": dial tcp: lookup example.com on 10.0.0.1:53: no such host
----

As a result, the subscription is stuck in this failing state and the Operator is unable to install or upgrade.

You can refresh a failing subscription by deleting the subscription, cluster service version (CSV), and other related objects. After recreating the subscription, OLM then reinstalls the correct version of the Operator.

.Prerequisites

* You have a failing subscription that is unable to pull an inaccessible bundle image.
* You have confirmed that the correct bundle image is accessible.

.Procedure

. Get the names of the `Subscription` and `ClusterServiceVersion` objects from the namespace where the Operator is installed:
+
[source,terminal]
----
$ oc get sub,csv -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                                                       PACKAGE                  SOURCE             CHANNEL
subscription.operators.coreos.com/elasticsearch-operator   elasticsearch-operator   redhat-operators   5.0

NAME                                                                         DISPLAY                            VERSION    REPLACES   PHASE
clusterserviceversion.operators.coreos.com/elasticsearch-operator.5.0.0-65   OpenShift Elasticsearch Operator   5.0.0-65              Succeeded
----

. Delete the subscription:
+
[source,terminal]
----
$ oc delete subscription <subscription_name> -n <namespace>
----

. Delete the cluster service version:
+
[source,terminal]
----
$ oc delete csv <csv_name> -n <namespace>
----

. Get the names of any failing jobs and related config maps in the `openshift-marketplace` namespace:
+
[source,terminal]
----
$ oc get job,configmap -n openshift-marketplace
----
+
.Example output
[source,terminal]
----
NAME                                                                        COMPLETIONS   DURATION   AGE
job.batch/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   1/1           26s        9m30s

NAME                                                                        DATA   AGE
configmap/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   3      9m30s
----

. Delete the job:
+
[source,terminal]
----
$ oc delete job <job_name> -n openshift-marketplace
----
+
This ensures pods that try to pull the inaccessible image are not recreated.

. Delete the config map:
+
[source,terminal]
----
$ oc delete configmap <configmap_name> -n openshift-marketplace
----

. Reinstall the Operator using the software catalog in the web console.

.Verification

* Check that the Operator has been reinstalled successfully:
+
[source,terminal]
----
$ oc get sub,csv,installplan -n <namespace>
----
