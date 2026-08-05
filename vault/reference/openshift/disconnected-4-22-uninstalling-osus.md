---
title: "Uninstalling the OpenShift Update Service from a cluster"
type: reference
domain: openshift
slug: disconnected-4-22-uninstalling-osus
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected/uninstalling-osus
version: 4.22
family: disconnected
documentKind: "Documentation"
---

# Uninstalling the OpenShift Update Service from a cluster

[id="uninstalling-osus"]
= Uninstalling the OpenShift Update Service from a cluster

To remove a local copy of the OpenShift Update Service (OSUS) from your cluster, you must first delete the OSUS application and then uninstall the OSUS Operator.

[id="update-service-delete-service_{context}"]
== Deleting an OpenShift Update Service application

You can delete an OpenShift Update Service application by using the OpenShift Container Platform web console or CLI.

// Deleting an OpenShift Update Service application by using the web console
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/uninstalling-osus.adoc

[id="update-service-delete-service-web-console_{context}"]
= Deleting an OpenShift Update Service application by using the web console

You can use the OpenShift Container Platform web console to delete an OpenShift Update Service application by using the OpenShift Update Service Operator.

.Prerequisites

* The OpenShift Update Service Operator has been installed.

.Procedure

. In the web console, click *Ecosystem* -> *Installed Operators*.

. Choose *OpenShift Update Service* from the list of installed Operators.

. Click the *Update Service* tab.

. From the list of installed OpenShift Update Service applications, select the application to be deleted and then click *Delete UpdateService*.

. From the *Delete UpdateService?* confirmation dialog, click *Delete* to confirm the deletion.

// Deleting an OpenShift Update Service application by using the CLI
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/uninstalling-osus.adoc

[id="update-service-delete-service-cli_{context}"]
= Deleting an OpenShift Update Service application by using the CLI

You can use the OpenShift CLI (`oc`) to delete an OpenShift Update Service application.

.Procedure

. Get the OpenShift Update Service application name using the namespace the OpenShift Update Service application was created in, for example, `openshift-update-service`:
+
[source,terminal]
----
$ oc get updateservice -n openshift-update-service
----
+
.Example output
[source,terminal]
----
NAME      AGE
service   6s
----

. Delete the OpenShift Update Service application using the `NAME` value from the previous step and the namespace the OpenShift Update Service application was created in, for example, `openshift-update-service`:
+
[source,terminal]
----
$ oc delete updateservice service -n openshift-update-service
----
+
.Example output
[source,terminal]
----
updateservice.updateservice.operator.openshift.io "service" deleted
----

[id="update-service-uninstall_{context}"]
== Uninstalling the OpenShift Update Service Operator

You can uninstall the OpenShift Update Service Operator by using the OpenShift Container Platform web console or CLI.

// Uninstalling the OpenShift Update Service Operator by using the web console
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/uninstalling-osus.adoc

[id="update-service-uninstall-web-console_{context}"]
= Uninstalling the OpenShift Update Service Operator by using the web console

You can use the OpenShift Container Platform web console to uninstall the OpenShift Update Service Operator.

.Prerequisites

* All OpenShift Update Service applications have been deleted.

.Procedure

. In the web console, click *Ecosystem* -> *Installed Operators*.

. Select *OpenShift Update Service* from the list of installed Operators and click *Uninstall Operator*.

. From the *Uninstall Operator?* confirmation dialog, click *Uninstall* to confirm the uninstallation.

// Uninstalling the OpenShift Update Service Operator by using the CLI
// Module included in the following assemblies:
// * updating/updating_a_cluster/updating_disconnected_cluster/uninstalling-osus.adoc

[id="update-service-uninstall-cli_{context}"]
= Uninstalling the OpenShift Update Service Operator by using the CLI

You can use the OpenShift CLI (`oc`) to uninstall the OpenShift Update Service Operator.

.Prerequisites

* All OpenShift Update Service applications have been deleted.

.Procedure

. Change to the project containing the OpenShift Update Service Operator, for example, `openshift-update-service`:
+
[source,terminal]
----
$ oc project openshift-update-service
----
+
.Example output
[source,terminal]
----
Now using project "openshift-update-service" on server "https://example.com:6443".
----

. Get the name of the OpenShift Update Service Operator operator group:
+
[source,terminal]
----
$ oc get operatorgroup
----
+
.Example output
[source,terminal]
----
NAME                             AGE
openshift-update-service-fprx2   4m41s
----

. Delete the operator group, for example, `openshift-update-service-fprx2`:
+
[source,terminal]
----
$ oc delete operatorgroup openshift-update-service-fprx2
----
+
.Example output
[source,terminal]
----
operatorgroup.operators.coreos.com "openshift-update-service-fprx2" deleted
----

. Get the name of the OpenShift Update Service Operator subscription:
+
[source,terminal]
----
$ oc get subscription
----
+
.Example output
[source,terminal]
----
NAME                      PACKAGE                   SOURCE                        CHANNEL
update-service-operator   update-service-operator   updateservice-index-catalog   v1
----

. Using the `Name` value from the previous step, check the current version of the subscribed OpenShift Update Service Operator in the `currentCSV` field:
+
[source,terminal]
----
$ oc get subscription update-service-operator -o yaml | grep " currentCSV"
----
+
.Example output
[source,terminal]
----
  currentCSV: update-service-operator.v0.0.1
----

. Delete the subscription, for example, `update-service-operator`:
+
[source,terminal]
----
$ oc delete subscription update-service-operator
----
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com "update-service-operator" deleted
----

. Delete the CSV for the OpenShift Update Service Operator using the `currentCSV` value from the previous step:
+
[source,terminal]
----
$ oc delete clusterserviceversion update-service-operator.v0.0.1
----
+
.Example output
[source,terminal]
----
clusterserviceversion.operators.coreos.com "update-service-operator.v0.0.1" deleted
----
