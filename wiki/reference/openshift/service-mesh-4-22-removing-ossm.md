---
title: "Uninstalling Service Mesh"
type: reference
domain: openshift
slug: service-mesh-4-22-removing-ossm
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/removing-ossm
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Uninstalling Service Mesh

[id="removing-ossm-v1x"]
= Removing Service Mesh

To remove {SMProductName} from an existing OpenShift Container Platform instance, remove the control plane before removing the operators.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-control-plane-remove_{context}"]
= Removing the {SMProductName} control plane

To uninstall {SMProductShortName} from an existing OpenShift Container Platform instance, first you delete the {SMProductShortName} control plane and the Operators. Then, you run commands to remove residual resources.

[id="ossm-control-plane-remove-operatorhub_{context}"]
== Removing the {SMProductShortName} control plane using the web console

You can remove the {SMProductName} control plane by using the web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Click the *Project* menu and select the project where you installed the {SMProductShortName} control plane, for example *istio-system*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click *Service Mesh Control Plane* under *Provided APIs*.

. Click the `ServiceMeshControlPlane` menu {kebab}.

. Click *Delete Service Mesh Control Plane*.

. Click *Delete* on the confirmation dialog window to remove the `ServiceMeshControlPlane`.

[id="ossm-control-plane-remove-cli_{context}"]
== Removing the {SMProductShortName} control plane using the CLI

You can remove the {SMProductName} control plane by using the CLI.  In this example, `istio-system` is the name of the control plane project.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Run the following command to delete the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc delete smmr -n istio-system default
----

. Run this command to retrieve the name of the installed `ServiceMeshControlPlane`:
+
[source,terminal]
----
$ oc get smcp -n istio-system
----

. Replace `<name_of_custom_resource>` with the output from the previous command, and run this command to remove the custom resource:
+
[source,terminal]
----
$ oc delete smcp -n istio-system <name_of_custom_resource>
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-operatorhub-remove-operators_{context}"]
= Removing the installed Operators

You must remove the Operators to successfully remove {SMProductName}. After you remove the {SMProductName} Operator, you must remove the Kiali Operator, the {JaegerName} Operator, and the OpenShift Elasticsearch Operator.

[id="ossm-remove-operator-servicemesh_{context}"]
== Removing the Operators

Follow this procedure to remove the Operators that make up {SMProductName}. Repeat the steps for each of the following Operators.

* {SMProductName}
* Kiali
* {JaegerName}
* OpenShift Elasticsearch

.Procedure

. Log in to the OpenShift Container Platform web console.

. From the *Ecosystem* -> *Installed Operators* page, scroll or type a keyword into the *Filter by name* to find each Operator. Then, click the Operator name.

. On the *Operator Details* page, select *Uninstall Operator* from the *Actions* menu. Follow the prompts to uninstall each Operator.

// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc

[id="ossm-remove-cleanup-1x_{context}"]
= Clean up Operator resources

Follow this procedure to manually remove resources left behind after removing the {SMProductName} Operator using the OpenShift Container Platform web console.

.Prerequisites

* An account with cluster administration access.
* Access to the OpenShift CLI (`oc`).

.Procedure

. Log in to the OpenShift Container Platform CLI as a cluster administrator.

. Run the following commands to clean up resources after uninstalling the Operators. If you intend to keep using Jaeger as a stand alone service without service mesh, do not delete the Jaeger resources.
+
[NOTE]
====
The Operators are installed in the `openshift-operators` namespace by default.  If you installed the Operators in another namespace, replace `openshift-operators` with the name of the project where the {SMProductName} Operator was installed.
====
+
[source,terminal]
----
$ oc delete validatingwebhookconfiguration/openshift-operators.servicemesh-resources.maistra.io
----
+
[source,terminal]
----
$ oc delete mutatingwebhookconfiguration/openshift-operators.servicemesh-resources.maistra.io
----
+
[source,terminal]
----
$ oc delete -n openshift-operators daemonset/istio-node
----
+
[source,terminal]
----
$ oc delete clusterrole/istio-admin clusterrole/istio-cni clusterrolebinding/istio-cni
----
// needs a slash?  What is the format here?
+
[source,terminal]
----
$ oc delete clusterrole istio-view istio-edit
----
+
[source,terminal]
----
$ oc delete clusterrole jaegers.jaegertracing.io-v1-admin jaegers.jaegertracing.io-v1-crdview jaegers.jaegertracing.io-v1-edit jaegers.jaegertracing.io-v1-view
----
+
[source,terminal]
----
$ oc get crds -o name | grep '.*\.istio\.io' | xargs -r -n 1 oc delete
----
+
[source,terminal]
----
$ oc get crds -o name | grep '.*\.maistra\.io' | xargs -r -n 1 oc delete
----
+
[source,terminal]
----
$ oc get crds -o name | grep '.*\.kiali\.io' | xargs -r -n 1 oc delete
----
+
[source,terminal]
----
$ oc delete crds jaegers.jaegertracing.io
----
+
[source,terminal]
----
$ oc delete svc admission-controller -n <operator-project>
----
+
[source,terminal]
----
$ oc delete project <istio-system-project>
----
