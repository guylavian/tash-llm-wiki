---
title: "Installing the {zero-trust-full}"
type: reference
domain: openshift
slug: security-4-22-zero-trust-manager-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/zero-trust-manager-install
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the {zero-trust-full}

[id="zero-trust-manager-install"]
= Installing the {zero-trust-full}

[role="_abstract"]
Install {zero-trust-full} to help ensure secure communication between your workloads. You can install the {zero-trust-full} by using either the web console or CLI.

If you install the Operator into a custom namespace (for example, `my-custom-namespace`), all managed operand resources are deployed within that same namespace. All secrets and ConfigMaps referenced by the Custom Resources (CRs) must also exist in that custom namespace.

[IMPORTANT]
====
The Operator installation is not supported in the `openshift-*` namespaces and the `default` namespace.
====

// Installing the {zero-trust-full} using the web console
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manager/zer-trust-manager-install.adoc

[id="zero-trust-manager-install-console_{context}"]
= Installing the {zero-trust-full} by using the web console

[role="_abstract"]
Use the Software Catalog in the OpenShift Container Platform web console to install the {zero-trust-full}. This process streamlines deployment and helps ensure the Operator is installed in the correct namespace with the appropriate installation mode.

[NOTE]
====
A minimum of 1Gi persistent volume is required to install the SPIRE Server.
====

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Go to *Ecosystem* -> *Software Catalog*.

. Search for *{zero-trust-full}*.

. On the *Install Operator* page:

.. Update the *Update channel*, if necessary. The channel defaults to `stable-v1`, which installs the latest `stable-v1` release of the {zero-trust-full}.

.. Choose the *Installed Namespace* for the Operator. The default Operator namespace is `zero-trust-workload-identity-manager`.
+
If the `zero-trust-workload-identity-manager` namespace does not exist, it is created for you.
+
[NOTE]
====
The Operator and operands are deployed in the same namespace.
====

.. Select an *Update Approval* strategy

* The *Automatic strategy* allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.

* The *Manual strategy* requires a user with appropriate credentials to approve the Operator update.

. Click *Install*.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.

.. Verify that *Zero Trust Workload Identity Manager* is listed with a *Status* of *Succeeded* in the `zero-trust-workload-identity-manager` namespace.

.. Verify that Zero Trust Workload Identity Manager controller manager deployment is ready and available by running the following command:
+
[source,terminal]
----
$ oc get deployment -l name=zero-trust-workload-identity-manager -n zero-trust-workload-identity-manager
----
+
.Example output
[source,terminal]
----
NAME                                                           READY UP-TO-DATE AVAILABLE AGE
zero-trust-workload-identity-manager-controller-manager-6c4djb 1/1   1          1         43m
----

. To check the Operator logs, run the following command:
+
[source,terminal]
----
$ oc logs -f deployment/zero-trust-workload-identity-manager -n zero-trust-workload-identity-manager
----

// Installing the {zero-trust-full} using CLI
// Module included in the following assemblies:
//
// * security/zero_trust_workload_identity_manageer/zero-trust-manager-install.adoc

[id="zero-trust-manager-install-cli_{context}"]
= Installing the {zero-trust-full} by using the CLI

[role="_abstract"]
Install the {zero-trust-full} by using the command-line interface (CLI) to create the required project, `OperatorGroup`, and `Subscription` objects. You can then deploy the Operator components necessary for managing workload identities on your OpenShift Container Platform cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

[NOTE]
====
A minimum of 1Gi persistent volume is required to install the SPIRE Server.
====

.Procedure

. Create a new project named `zero-trust-workload-identity-manager` by running the following command:
+
[source, terminal]
----
$ oc new-project zero-trust-workload-identity-manager
----

. Create an `OperatorGroup` object:

.. Create a YAML file, for example, `operatorGroup.yaml`, with the following content:
+
[source, yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-zero-trust-workload-identity-manager
  namespace: zero-trust-workload-identity-manager
spec:
  upgradeStrategy: Default
----

.. Create the `OperatorGroup` object by running the following command:
+
[source, terminal]
----
$ oc create -f operatorGroup.yaml
----

. Create a `Subscription` object:

.. Create a YAML file, for example, `subscription.yaml`, that defines the `Subscription` object:
+
[source, yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-zero-trust-workload-identity-manager
  namespace: zero-trust-workload-identity-manager
spec:
  channel: stable-v1
  name: openshift-zero-trust-workload-identity-manager
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Automatic
----

.. Create the `Subscription` object by running the following command:
+
[source, terminal]
----
$ oc create -f subscription.yaml
----

.Verification

* Verify that the OLM subscription is created by running the following command:
+
[source, terminal]
----
$ oc get subscription -n zero-trust-workload-identity-manager
----
+
.Example output
[source, terminal]
----
NAME                                             PACKAGE                                SOURCE             CHANNEL
openshift-zero-trust-workload-identity-manager   zero-trust-workload-identity-manager   redhat-operators   stable-v1
----

* Verify whether the Operator is successfully installed by running the following command:
+
[source, terminal]
----
$ oc get csv -n zero-trust-workload-identity-manager
----
+
.Example output
[source, terminal]
----
NAME                                         DISPLAY                                VERSION  PHASE
zero-trust-workload-identity-manager.v1.0.0   Zero Trust Workload Identity Manager   1.0.0    Succeeded
----

* Verify that the {zero-trust-full} controller manager is ready by running the following command:
+
[source, terminal]
----
$ oc get deployment -l name=zero-trust-workload-identity-manager -n zero-trust-workload-identity-manager
----
+
.Example output
[source, terminal]
----
NAME                                                      READY   UP-TO-DATE   AVAILABLE   AGE
zero-trust-workload-identity-manager-controller-manager   1/1     1            1           43m
----
