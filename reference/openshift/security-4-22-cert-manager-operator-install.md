---
title: "Installing the {cert-manager-operator}"
type: reference
domain: openshift
slug: security-4-22-cert-manager-operator-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-operator-install
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the {cert-manager-operator}

[id="cert-manager-operator-install"]
= Installing the {cert-manager-operator}

[role="_abstract"]
The {cert-manager-operator} is not installed in OpenShift Container Platform by default. You can install the {cert-manager-operator} by using the web console.

[NOTE]
====
The {cert-manager-operator} sets the `features.operators.openshift.io/token-auth-aws`, `features.operators.openshift.io/token-auth-azure`, and `features.operators.openshift.io/token-auth-gcp` annotations in the `ClusterServiceVersion` custom resource of the Operator. The OpenShift Container Platform web console requires the credential details when these annotations are set. Currently, the Operator does not use the values collected by the OpenShift web console and you can provide any value when asked for the input. For example, when installing on the managed OpenShift Container Platform cluster, the `identity-provider-arn` is asked and any value can be provided to proceed.
====

[IMPORTANT]
====
The {cert-manager-operator} version 1.15 or later supports the `AllNamespaces`, `SingleNamespace`, and `OwnNamespace` installation modes. Earlier versions, such as 1.14, support only the `SingleNamespace` and `OwnNamespace` installation modes.
====

== Installing the {cert-manager-operator}
// Installing the {cert-manager-operator} using the web console
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-operator-install.adoc

[id="cert-manager-install-console_{context}"]
= Installing the {cert-manager-operator} by using the web console

[role="_abstract"]
You can use the web console to install the {cert-manager-operator}.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Software Catalog*.

. Enter *{cert-manager-operator}* into the filter box.

. Select the *{cert-manager-operator}*

. Select the {cert-manager-operator} version from *Version* drop-down list, and click *Install*.
+
[NOTE]
====
See supported {cert-manager-operator} versions in the following "Additional resources" section.
====

. On the *Install Operator* page:
.. Update the *Update channel*, if necessary. The channel defaults to *stable-v1*, which installs the latest stable release of the {cert-manager-operator}.
.. Choose the *Installed Namespace* for the Operator. The default Operator namespace is `cert-manager-operator`.
+
If the `cert-manager-operator` namespace does not exist, it is created for you.
+
[NOTE]
====
During the installation, the OpenShift Container Platform  web console allows you to select between `AllNamespaces` and `SingleNamespace` installation modes. For installations with {cert-manager-operator} version 1.15.0 or later, it is recommended to choose the `AllNamespaces` installation mode. `SingleNamespace` and `OwnNamespace` support will remain for earlier versions but will be deprecated in future versions.
====

.. Select an *Update approval* strategy.
+
* The *Automatic* strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.
. Verify that *{cert-manager-operator}* is listed with a *Status* of *Succeeded* in the `cert-manager-operator` namespace.
. Verify that cert-manager pods are up and running by entering the following command:
+
[source,terminal]
----
$ oc get pods -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt               1/1     Running   0          3m39s
cert-manager-cainjector-56cc5f9868-7g9z7   1/1     Running   0          4m5s
cert-manager-webhook-d4f79d7f7-9dg9w       1/1     Running   0          4m9s
----
+
You can use the {cert-manager-operator} only after cert-manager pods are up and running.

//Installing using CLI
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-operator-install.adoc

[id="cert-manager-install-cli_{context}"]
= Installing the {cert-manager-operator} by using the CLI

[role="_abstract"]
You can install the {cert-manager-operator} by using the command-line interface(CLI).

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a new project named `cert-manager-operator` by running the following command:
+
[source, terminal]
----
$ oc new-project cert-manager-operator
----

. Create an `OperatorGroup` object:

.. Create a YAML file, for example, `operatorGroup.yaml`, with the following content:
+
[source, yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-cert-manager-operator
  namespace: cert-manager-operator
spec:
  targetNamespaces:
  - "cert-manager-operator"
----

.. For {cert-manager-operator} v1.15.0 or later, create a YAML file with the following content:
+
[source, yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-cert-manager-operator
  namespace: cert-manager-operator
spec:
  targetNamespaces: []
  spec: {}
----
+
[NOTE]
====
Starting from {cert-manager-operator} version 1.15.0, it is recommended to install the Operator using the `AllNamespaces` OLM `installMode`. Older versions can continue using the `SingleNamespace` or `OwnNamespace` OLM `installMode`. Support for `SingleNamespace` and `OwnNamespace` will be deprecated in future versions.
====

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
  name: openshift-cert-manager-operator
  namespace: cert-manager-operator
spec:
  channel: stable-v1
  name: openshift-cert-manager-operator
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

. Verify that the OLM subscription is created by running the following command:
+
[source, terminal]
----
$ oc get subscription -n cert-manager-operator
----
+
.Example output
[source, terminal]
----
NAME                              PACKAGE                           SOURCE             CHANNEL
openshift-cert-manager-operator   openshift-cert-manager-operator   redhat-operators   stable-v1
----

. Verify whether the Operator is successfully installed by running the following command:
+
[source, terminal]
----
$ oc get csv -n cert-manager-operator
----
+
.Example output
[source, terminal]
----
NAME                            DISPLAY                                       VERSION   REPLACES                        PHASE
cert-manager-operator.v1.13.0   cert-manager Operator for Red Hat OpenShift   1.13.0    cert-manager-operator.v1.12.1   Succeeded
----

. Verify that the status {cert-manager-operator} is `Running` by running the following command:
+
[source, terminal]
----
$ oc get pods -n cert-manager-operator
----
+
.Example output
[source, terminal]
----
NAME                                                        READY   STATUS    RESTARTS   AGE
cert-manager-operator-controller-manager-695b4d46cb-r4hld   2/2     Running   0          7m4s
----

. Verify that the status of cert-manager pods is `Running` by running the following command:
+
[source, terminal]
----
$ oc get pods -n cert-manager
----
+
.Example output
[source, terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-58b7f649c4-dp6l4              1/1     Running   0          7m1s
cert-manager-cainjector-5565b8f897-gx25h   1/1     Running   0          7m37s
cert-manager-webhook-9bc98cbdd-f972x       1/1     Running   0          7m40s
----

[role="_additional-resources"]
.Additional resources
* Supported {cert-manager-operator} versions

// Updating paths for the {cert-manager-operator}
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-operator-install.adoc

[id="cert-manager-operator-update-channels_{context}"]
= Understanding update channels of the {cert-manager-operator}

[role="_abstract"]
Update channels are the mechanism by which you can declare the version of your {cert-manager-operator} in your cluster. The {cert-manager-operator} offers the following update channels:

* `stable-v1`
* `stable-v1.y`

[id="stable-v1-channel_{context}"]
== stable-v1 channel
The `stable-v1` channel installs and updates the latest release version of the {cert-manager-operator}. Select the `stable-v1` channel if you want to use the latest stable release of the {cert-manager-operator}.

[NOTE]
====
The `stable-v1` channel is the default and suggested channel while installing the {cert-manager-operator}.
====

The `stable-v1` channel offers the following update approval strategies:

Automatic:: If you choose automatic updates for an installed {cert-manager-operator}, a new version of the {cert-manager-operator} is available in the `stable-v1` channel. The Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without human intervention.

Manual:: If you select manual updates, when a newer version of the {cert-manager-operator} is available, OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the {cert-manager-operator} updated to the new version.

[id="stable-v1-y-channel_{context}"]
== stable-v1.y channel

The y-stream version of the {cert-manager-operator} installs updates from the `stable-v1.y` channels such as `stable-v1.10`, `stable-v1.11`, and `stable-v1.12`. Select the `stable-v1.y` channel if you want to use the y-stream version and stay updated to the z-stream version of the {cert-manager-operator}.

The `stable-v1.y` channel offers the following update approval strategies:

Automatic:: If you choose automatic updates for an installed {cert-manager-operator}, a new z-stream version of the {cert-manager-operator} is available in the `stable-v1.y` channel. OLM automatically upgrades the running instance of your Operator without human intervention.

Manual:: If you select manual updates, when a newer version of the {cert-manager-operator} is available, OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the {cert-manager-operator} updated to the new version of the z-stream releases.

[role="_additional-resources"]
[id="cert-manager-operator-install_additional-resources"]
== Additional resources

* Adding Operators to a cluster
* Updating installed Operators
