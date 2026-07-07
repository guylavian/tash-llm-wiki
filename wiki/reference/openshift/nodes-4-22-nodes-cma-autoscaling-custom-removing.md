---
title: "Removing the Custom Metrics Autoscaler Operator"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-removing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-removing
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Removing the Custom Metrics Autoscaler Operator

[id="nodes-cma-autoscaling-custom-removing"]
= Removing the Custom Metrics Autoscaler Operator

You can remove the custom metrics autoscaler from your OpenShift Container Platform cluster. After removing the Custom Metrics Autoscaler Operator, remove other components associated with the Operator to avoid potential issues.

[NOTE]
====
Delete the `KedaController` custom resource (CR) first. If you do not delete the `KedaController` CR, OpenShift Container Platform can hang when you delete the `openshift-keda` project. If you delete the Custom Metrics Autoscaler Operator before deleting the CR, you are not able to delete the CR.
====
[NOTE]
====
Delete the `KedaController` custom resource (CR) first. If you do not delete the `KedaController` CR, OpenShift Container Platform can hang when you delete the `keda` project. If you delete the Custom Metrics Autoscaler Operator before deleting the CR, you are not able to delete the CR.
====

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-uninstall.adoc

[id="nodes-cma-autoscaling-custom-uninstalling_{context}"]
= Uninstalling the Custom Metrics Autoscaler Operator

Use the following procedure to remove the custom metrics autoscaler from your OpenShift Container Platform cluster.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Installed Operators*.

. Switch to the *openshift-keda* project.
. Switch to the *keda* project.

. Remove the `KedaController` custom resource.

.. Find the *CustomMetricsAutoscaler*  Operator and click the *KedaController* tab.

.. Find the custom resource, and then click *Delete KedaController*.

.. Click *Uninstall*.

. Remove the Custom Metrics Autoscaler Operator:

.. Click *Ecosystem* -> *Installed Operators*.

.. Find the *CustomMetricsAutoscaler*  Operator and click the Options menu {kebab} and select *Uninstall Operator*.

.. Click *Uninstall*.

. Optional: Use the OpenShift CLI to remove the custom metrics autoscaler components:

.. Delete the custom metrics autoscaler CRDs:
+
--
* `clustertriggerauthentications.keda.sh`
* `kedacontrollers.keda.sh`
* `scaledjobs.keda.sh`
* `scaledobjects.keda.sh`
* `triggerauthentications.keda.sh`
--
+
[source,terminal]
----
$ oc delete crd clustertriggerauthentications.keda.sh kedacontrollers.keda.sh scaledjobs.keda.sh scaledobjects.keda.sh triggerauthentications.keda.sh
----
+
Deleting the CRDs removes the associated roles, cluster roles, and role bindings. However, there might be a few cluster roles that must be manually deleted.

.. List any custom metrics autoscaler cluster roles:
+
[source,terminal]
----
$ oc get clusterrole | grep keda.sh
----

.. Delete the listed custom metrics autoscaler cluster roles. For example:
+
[source,terminal]
----
$ oc delete clusterrole.keda.sh-v1alpha1-admin
----

.. List any custom metrics autoscaler cluster role bindings:
+
[source,terminal]
----
$ oc get clusterrolebinding | grep keda.sh
----

.. Delete the listed custom metrics autoscaler cluster role bindings. For example:
+
[source,terminal]
----
$ oc delete clusterrolebinding.keda.sh-v1alpha1-admin
----

. Delete the custom metrics autoscaler project:
+
[source,terminal]
----
$ oc delete project openshift-keda
----
[source,terminal]
----
$ oc delete project keda
----

. Delete the Cluster Metric Autoscaler Operator:
+
[source,terminal]
----
$ oc delete operator/openshift-custom-metrics-autoscaler-operator.openshift-keda
----
[source,terminal]
----
$ oc delete operator/openshift-custom-metrics-autoscaler-operator.keda
----
