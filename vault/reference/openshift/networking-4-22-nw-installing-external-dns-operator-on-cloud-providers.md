---
title: "Installing the External DNS Operator"
type: reference
domain: openshift
slug: networking-4-22-nw-installing-external-dns-operator-on-cloud-providers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/nw-installing-external-dns-operator-on-cloud-providers
version: 4.22
family: networking
documentKind: "Documentation"
---

# Installing the External DNS Operator

[id="installing-external-dns-on-cloud-providers"]
= Installing the External DNS Operator

[role="_abstract"]
To manage DNS records on your cloud infrastructure, install the External DNS Operator. This Operator supports deployment on major cloud providers, including {aws-first}, {azure-first}, and {gcp-first}.

// Installing the External DNS Operator with OperatorHub
// Module included in the following assemblies:
//
// * networking/external_dns_operator/nw-installing-external-dns-operator-on-cloud-providers.adoc

[id="nw-installing-external-dns-operator_{context}"]
= Installing the External DNS Operator with the Software Catalog

[role="_abstract"]
You can install the External DNS Operator by using the OpenShift Container Platform Software Catalog. You can then manage the Operator lifecycle directly from the web console.

.Procedure

. Click *Ecosystem* -> *Software Catalog* in the OpenShift Container Platform web console.

. Click *External DNS Operator*. You can use the *Filter by keyword* text box or the filter list to search for External DNS Operator from the list of Operators.

. Select the `external-dns-operator` namespace.

. On the *External DNS Operator* page, click *Install*.

. On the *Install Operator* page, ensure that you selected the following options:
+
.. Update the channel as *stable-v1*.
+
.. Installation mode as *A specific name on the cluster*.
+
.. Installed namespace as `external-dns-operator`. If namespace `external-dns-operator` does not exist, the Operator gets created during the Operator installation.
+
.. Select *Approval Strategy* as *Automatic* or *Manual*. The Approval Strategy defaults to *Automatic*.
+
.. Click *Install*.
+
If you select *Automatic* updates, the Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without any intervention.
+
If you select *Manual* updates, the OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the Operator updated to the new version.

.Verification

* Verify that the External DNS Operator shows the *Status* as *Succeeded* on the *Installed Operators* dashboard.

// Installing the External DNS Operator by using the CLI
// Module included in the following assemblies:
//
// * networking/external_dns_operator/nw-installing-external-dns-operator-on-cloud-providers.adoc

[id="nw-installing-external-dns-operator-cli_{context}"]
= Installing the External DNS Operator by using the CLI

[role="_abstract"]
You can use the {oc-first} to install the External DNS Operator. The Operator manages the installation process directly from your terminal without you having to use the web console.

.Prerequisites

* You are logged in to the {oc-first}.

.Procedure

. Create a `Namespace` object:
+
.. Create a YAML file that defines the `Namespace` object:
+
.Example `namespace.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: external-dns-operator
# ...
----
+
.. Create the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f namespace.yaml
----

. Create an `OperatorGroup` object:
+
.. Create a YAML file that defines the `OperatorGroup` object:
+
.Example `operatorgroup.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: external-dns-operator
  namespace: external-dns-operator
spec:
  upgradeStrategy: Default
  targetNamespaces:
  - external-dns-operator
# ...
----
+
.. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f operatorgroup.yaml
----

. Create a `Subscription` object:
+
.. Create a YAML file that defines the `Subscription` object:
+
.Example `subscription.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: external-dns-operator
  namespace: external-dns-operator
spec:
  channel: stable-v1
  installPlanApproval: Automatic
  name: external-dns-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
# ...
----
+
.. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f subscription.yaml
----

.Verification

. Get the name of the install plan from the subscription by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator \
  get subscription external-dns-operator \
  --template='{{.status.installplan.name}}{{"\n"}}'
----

. Verify that the status of the install plan is `Complete` by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator \
  get ip <install_plan_name> \
  --template='{{.status.phase}}{{"\n"}}'
----

. Verify that the status of the `external-dns-operator` pod is `Running` by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator get pod
----

+
.Example output
[source,terminal]
----
NAME                                     READY   STATUS    RESTARTS   AGE
external-dns-operator-5584585fd7-5lwqm   2/2     Running   0          11m
----

. Verify that the catalog source of the subscription is `redhat-operators` by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator get subscription
----

. Check the `external-dns-operator` version by running the following command:
+
[source,terminal]
----
$ oc -n external-dns-operator get csv
----
