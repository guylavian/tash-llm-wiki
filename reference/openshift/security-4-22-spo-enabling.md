---
title: "Enabling the Security Profiles Operator"
type: reference
domain: openshift
slug: security-4-22-spo-enabling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/spo-enabling
version: 4.22
family: security
documentKind: "Documentation"
---

# Enabling the Security Profiles Operator

[id="spo-enabling"]
= Enabling the Security Profiles Operator

[role="_abstract"]
Before you can use the Security Profiles Operator, you must ensure the Operator is deployed in the cluster.

[IMPORTANT]
====
All cluster nodes must have the same release version in order for this Operator to function properly.
As an example, for nodes running {op-system}, all nodes must have the same {op-system} version.
====

[IMPORTANT]
====
The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.
====

[IMPORTANT]
====
The Security Profiles Operator supports `x86_64` and `ppc64le` architecture.
====

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-enabling.adoc

[id="spo-installing_{context}"]
= Installing the Security Profiles Operator

[role="_abstract"]
You can use the OpenShift Container Platform web console to install the Security Profiles Operator. This installs the Security Profiles Operator into the `openshift-security-profiles` namespace by default. You can also verify correct installation by using the OpenShift Container Platform web console.

.Prerequisites

* You must have access to the web console as a user with `cluster-admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the Security Profiles Operator, then click *Install*.
. Keep the default selection of *Installation mode* and *namespace* to ensure that the Operator will be installed to the `openshift-security-profiles` namespace.
. Click *Install*.

.Verification

To confirm that the installation is successful:

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. Check that the Security Profiles Operator is installed in the `openshift-security-profiles` namespace and its status is `Succeeded`.

If the Operator is not installed successfully:

. Navigate to the *Ecosystem* -> *Installed Operators* page and inspect the `Status` column for any errors or failures.
. Navigate to the *Workloads* -> *Pods* page and check the logs in any pods in the `openshift-security-profiles` project that are reporting issues.

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-enabling.adoc

[id="spo-installing-cli_{context}"]
= Installing the Security Profiles Operator using the CLI

[role="_abstract"]
You can install the OpenShift Container Platform Security Profiles Operator by using the command line interface.

.Prerequisites

* You must have `cluster-admin` privileges.

.Procedure

. Define a `Namespace` object:
+
.Example `namespace-object.yaml`
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
    name: openshift-security-profiles
labels:
  openshift.io/cluster-monitoring: "true"
----

. Create the `Namespace` object:
+
[source,terminal]
----
$ oc create -f namespace-object.yaml
----

. Define an `OperatorGroup` object:
+
.Example `operator-group-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: security-profiles-operator
  namespace: openshift-security-profiles
----

. Create the `OperatorGroup` object:
+
[source,terminal]
----
$ oc create -f operator-group-object.yaml
----

. Define a `Subscription` object:
+
.Example `subscription-object.yaml`
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: security-profiles-operator-sub
  namespace: openshift-security-profiles
spec:
  channel: release-alpha-rhel-8
  installPlanApproval: Automatic
  name: security-profiles-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

. Create the `Subscription` object:
+
[source,terminal]
----
$ oc create -f subscription-object.yaml
----
+
[NOTE]
====
If you are setting the global scheduler feature and enable `defaultNodeSelector`, you must create the namespace manually and update the annotations of the `openshift-security-profiles` namespace, or the namespace where the Security Profiles Operator was installed, with `openshift.io/node-selector: “”`. This removes the default node selector and prevents deployment failures.
====

.Verification

. Verify the installation succeeded by inspecting the following CSV file:
+
[source,terminal]
----
$ oc get csv -n openshift-security-profiles
----

. Verify that the Security Profiles Operator is operational by running the following command:
+
[source,terminal]
----
$ oc get deploy -n openshift-security-profiles
----

// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-enabling.adoc

[id="logging-verbosity_{context}"]
= Configuring logging verbosity

[role="_abstract"]
The Security Profiles Operator supports the default logging verbosity of `0` and an enhanced verbosity of `1`.

.Procedure

* To enable enhanced logging verbosity, patch the `spod` configuration and adjust the value by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod \
    spod --type=merge -p '{"spec":{"verbosity":1}}'
----
+
.Example output
[source,terminal]
----
securityprofilesoperatordaemon.security-profiles-operator.x-k8s.io/spod patched
----
