---
title: "Installing the NBDE Tang Server Operator"
type: reference
domain: openshift
slug: security-4-22-nbde-tang-server-operator-installing
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/nbde-tang-server-operator-installing
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the NBDE Tang Server Operator

[id="installing-nbde-tang-server-operator"]
= Installing the NBDE Tang Server Operator

You can install the NBDE Tang Operator either by using the web console or through the `oc` command from CLI.

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-installing.adoc

[id="installing-nbde-tang-server-operator-using-web-console_{context}"]
= Installing the NBDE Tang Server Operator using the web console

You can install the NBDE Tang Server Operator from the software catalog using the web console.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the NBDE Tang Server Operator:
+
image::nbde-tang-server-operator-01-operatorhub.png[NBDE Tang Server Operator in the software catalog]
. Click *Install*.
. On the *Operator Installation* screen, keep the *Update channel*, *Version*, *Installation mode*, *Installed Namespace*, and *Update approval* fields on the default values.
. After you confirm the installation options by clicking *Install*, the console displays the installation confirmation.
+
image::nbde-tang-server-operator-03-confirmation.png[Confirmation of a NBDE Tang Server Operator installation]

.Verification

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. Check that the NBDE Tang Server Operator is installed and its status is `Succeeded`.
+
image::nbde-tang-server-operator-05-succeeded.png[NBDE Tang Server Operator status]

// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-installing.adoc

[id="installing-nbde-tang-server-operator-using-cli_{context}"]
= Installing the NBDE Tang Server Operator using CLI

You can install the NBDE Tang Server Operator from the software catalog using the CLI.

.Prerequisites

* You must have `cluster-admin` privileges on an OpenShift Container Platform cluster.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Use the following command to list available Operators in the software catalog, and limit the output to Tang-related results:
+
[source,terminal]
----
$ oc get packagemanifests -n openshift-marketplace | grep tang
----
+
.Example output
[source,terminal]
----
tang-operator           Red Hat
----
+
In this case, the corresponding packagemanifest name is `tang-operator`.

. Create a `Subscription` object YAML file to subscribe a namespace to the NBDE Tang Server Operator, for example, `tang-operator.yaml`:
+
.Example subscription YAML for tang-operator
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: tang-operator
  namespace: openshift-operators
spec:
  channel: stable <1>
  installPlanApproval: Automatic
  name: tang-operator <2>
  source: redhat-operators <3>
  sourceNamespace: openshift-marketplace <4>
----
<1> Specify the channel name from where you want to subscribe the Operator.
<2> Specify the name of the Operator to subscribe to.
<3> Specify the name of the CatalogSource that provides the Operator.
<4> The namespace of the CatalogSource. Use `openshift-marketplace` for the default software catalog sources.

. Apply the `Subscription` to the cluster:
+
[source,terminal]
----
$ oc apply -f tang-operator.yaml
----

.Verification

* Check that the NBDE Tang Server Operator controller runs in the `openshift-operators` namespace:
+
[source,terminal]
----
$ oc -n openshift-operators get pods
----
+
.Example output
[source,terminal]
----
NAME                                                READY   STATUS    RESTARTS   AGE
tang-operator-controller-manager-694b754bd6-4zk7x   2/2     Running   0          12s
----
