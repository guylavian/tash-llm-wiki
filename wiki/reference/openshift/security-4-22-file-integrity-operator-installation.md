---
title: "Installing the File Integrity Operator"
type: reference
domain: openshift
slug: security-4-22-file-integrity-operator-installation
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/file-integrity-operator-installation
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the File Integrity Operator

[id="installing-file-integrity-operator"]
= Installing the File Integrity Operator

[IMPORTANT]
====
All cluster nodes must have the same release version in order for this Operator to function properly.
As an example, for nodes running {op-system}, all nodes must have the same {op-system} version.
====

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-installation.adoc

[id="installing-file-integrity-operator-using-web-console_{context}"]
= Installing the File Integrity Operator using the web console

.Prerequisites

* You must have `admin` privileges.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Software Catalog*.
. Search for the File Integrity Operator, then click *Install*.
. Keep the default selection of *Installation mode* and *namespace* to ensure that the Operator will be installed to the `openshift-file-integrity` namespace.
. Click *Install*.

.Verification

To confirm that the installation is successful:

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. Check that the Operator is installed in the `openshift-file-integrity` namespace and its status is `Succeeded`.

If the Operator is not installed successfully:

. Navigate to the *Ecosystem* -> *Installed Operators* page and inspect the `Status` column for any errors or failures.
. Navigate to the *Workloads* -> *Pods* page and check the logs in any pods in the `openshift-file-integrity` project that are reporting issues.

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-installation.adoc

[id="installing-file-integrity-operator-using-cli_{context}"]
= Installing the File Integrity Operator using the CLI

.Prerequisites

* You must have `admin` privileges.

.Procedure

. Create a `Namespace` object YAML file by running:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged <1>
  name: openshift-file-integrity
----
<1> In OpenShift Container Platform , the pod security label must be set to `privileged` at the namespace level.

. Create the `OperatorGroup` object YAML file:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: file-integrity-operator
  namespace: openshift-file-integrity
spec:
  targetNamespaces:
  - openshift-file-integrity
----

. Create the `Subscription` object YAML file:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: file-integrity-operator
  namespace: openshift-file-integrity
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: file-integrity-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.Verification

. Verify the installation succeeded by inspecting the CSV file:
+
[source,terminal]
----
$ oc get csv -n openshift-file-integrity
----

. Verify that the File Integrity Operator is up and running:
+
[source,terminal]
----
$ oc get deploy -n openshift-file-integrity
----

[id="additional-resources-installing-the-file-integrity-operator"]
[role="_additional-resources"]
== Additional resources

* Using Operator Lifecycle Manager in disconnected environments
