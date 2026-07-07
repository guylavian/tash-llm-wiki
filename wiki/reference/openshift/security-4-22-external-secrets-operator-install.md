---
title: "Installing the External Secrets Operator for Red Hat OpenShift"
type: reference
domain: openshift
slug: security-4-22-external-secrets-operator-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-operator-install
version: 4.22
family: security
documentKind: "Documentation"
---

# Installing the External Secrets Operator for Red Hat OpenShift

[id="external-secrets-operator-install"]
= Installing the External Secrets Operator for Red Hat OpenShift

[role="_abstract"]
The {external-secrets-operator} is not installed on the OpenShift Container Platform by default. Install the {external-secrets-operator-short} by using either the web console or the command-line interface (CLI).

//Limitations of application installation and uninstallation
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-limitations_{context}"]
= Limitations of {external-secrets-operator}

[role="_abstract"]
There are specific operational constraints to consider when deploying or removing the {external-secrets-operator}, that might require manual intervention or strict dependency ordering.

The following are the limitations of {external-secrets-operator} during the installation and uninstallation of the `external-secrets` application.

* Uninstalling the {external-secrets-operator} does not delete the resources created for `external-secrets` application. you must clean up the resources manually.
* When you add `cert-manager` Operator configurations in `externalsecrets.operator.openshift.io` object after creation, delete the `external-secrets-cert-controller` deployment resource manually to prevent degradation of the `external-secrets` application.
* Enable the `BitwardenSecretManagerProvider` field in `externalsecrets.operator.openshift.io` object only when installed on OpenShift Cluster running on x86_64 and arm64 architectures .
* Ensure `cert-manager` Operator is installed and operational before deploying the {external-secrets-operator} for seamless functioning. If you install the `cert-manager` Operator later, manually restart the `external-secrets-operator` pod to apply cert-manager configurations in `externalsecrets.operator.openshift.io` object.

//Installing the {external-secrets-operator} using the web console
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-install-console_{context}"]
= Installing the {external-secrets-operator} by using the web console

[role="_abstract"]
You can install the {external-secrets-operator} by using the OpenShift Container Platform web console. You can select the desired update channel and approval strategy, and deploy the Operator into the recommended namespace without manually defining YAML resources.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Software Catalog*.

. Enter *{external-secrets-operator-short}* in the search box.

. Select the *{external-secrets-operator}* from the generated list and click *Install*.

. On the *Install Operator* page:

.. Update the *Update channel*, if necessary. The channel defaults to *stable-v1*, which installs the latest stable release of the {external-secrets-operator-short}.

.. Select the version from *Version* drop-down list.

.. Choose the *Installed Namespace* for the Operator.
+
* To use the default Operator namespace, select the *Operator recommended Namespace* option.
+
* To use the namespace that you created, select the *Select a Namespace* option, and then select the namespace from the drop-down list.
+
* If the default `external-secrets-operator` namespace does not exist, it is created for you by the {olm-first}.
+
.. Select an *Update approval* strategy.
+
* The *Automatic* strategy enables {olm} to automatically update the Operator when a new version is available.
+
* The *Manual* strategy requires a user with appropriate credentials to approve the Operator update.

.. Click *Install*.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.

. Verify that *{external-secrets-operator-short}* is listed with a *Status* of *Succeeded* in the `external-secrets-operator` namespace.

//Installing using CLI
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-install-cli_{context}"]
= Installing the {external-secrets-operator} by using the CLI

[role="_abstract"]
You can install the {external-secrets-operator} by manually configuring the Operator Lifecycle Manager (OLM) resources using the OpenShift CLI. You can create a dedicated namespace, define the Operator's scope, and install the Operator from the catalog.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a new project named `external-secrets-operator` by running the following command:
+
[source,terminal]
----
$ oc new-project external-secrets-operator
----

. Create an `OperatorGroup` object by defining a YAML file with the following content:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-external-secrets-operator
  namespace: external-secrets-operator
spec:
  targetNamespaces: []
----

. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc create -f operatorGroup.yaml
----

. Create a `Subscription` object by defining a YAML file with the following content:
+
The following is an example of a `subscription.yaml` file.
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-external-secrets-operator
  namespace: external-secrets-operator
spec:
  channel: stable-v1
  name: openshift-external-secrets-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Automatic
  startingCSV: external-secrets-operator.v1.0.0
----

. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc create -f subscription.yaml
----

.Verification

. Verify that the {olm} subscription is created by running the following command:
+
[source,terminal]
----
$ oc get subscription -n external-secrets-operator
----
+
The following is example output verifying the {olm} subscription is created.
+
[source,terminal]
----
NAME                                  PACKAGE                               SOURCE             CHANNEL
openshift-external-secrets-operator   openshift-external-secrets-operator   redhat-operators   stable-v1
----

. Verify whether the Operator is successfully installed by running the following command:
+
[source,terminal]
----
$ oc get csv -n external-secrets-operator
----
+
The following is example output verifying that the Operator is installed.
+
[source,terminal]
----
NAME                               DISPLAY                                           VERSION   REPLACES   PHASE
external-secrets-operator.v1.0.0   External Secrets Operator for Red Hat OpenShift   1.0.0                Succeeded
----

. Verify that the status of the {external-secrets-operator-short} is `Running` by entering the following command:
+
[source,terminal]
----
$ oc get pods -n external-secrets-operator
----
+
The following is example output verifying the {external-secrets-operator-short} is `Running`.
+
[source,terminal]
----
NAME                                                            READY   STATUS    RESTARTS   AGE
external-secrets-operator-controller-manager-5699f4bc54-kbsmn   1/1     Running   0          25h
----

[role="_additional-resources"]
[id="external-secrets-operator-install_additional-resources"]
== Additional resources

* Adding Operators to a cluster

//== Installing the external secrets operand using CLI
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operand-install-cli_{context}"]
= Installing the External Secrets operand by using the CLI

[role="_abstract"]
To install the External Secrets operand, create an instance of the `ExternalSecrets` custom resource by using the command-line interface (CLI) which deploys necessary operand components such as the core controller, webhook, and certificate controller into the `external-secrets` namespace.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create an `externalsecretsconfig.openshift.operator.io` object by defining a YAML file with the following content:
+
.Example `externalsecretsconfig.yaml` file.
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  labels:
    app: external-secrets-operator
    app.kubernetes.io/name: cluster
  name: cluster
spec:
  controllerConfig:
    networkPolicies:
    - componentName: ExternalSecretsCoreController
      egress:
      - {}
      name: allow-external-secrets-egress
----
+
For more information on spec configuration, see "External Secrets Operator for Red Hat OpenShift APIs".

. Create the `externalsecretsconfigs.openshift.operator.io` object by running the following command:
+
[source,terminal]
----
$ oc create -f externalsecretsconfig.yaml
----

.Verification

. Verify that the `external-secrets` pods are running by entering the following command:
+
[source,terminal]
----
$ oc get pods -n external-secrets
----
+
.Example output
+
[source,terminal]
----
NAME                                                READY   STATUS    RESTARTS   AGE
external-secrets-75d47cb9c8-6p4n2                   1/1     Running   0          4h5m
external-secrets-cert-controller-676444b897-qb6ft   1/1     Running   0          4h5m
external-secrets-webhook-b566658ff-7m4d5            1/1     Running   0          4h5m
----

. Verify that the `external-secrets-operator` deployment object reports a successful status by running the following command:
+
[source,terminal]
----
$ oc get externalsecretsconfig.operator.openshift.io cluster -n external-secrets-operator -o jsonpath='{.status.conditions}' | jq .
----
+
.Example output
+
[source,terminal]
----
[
  {
    "lastTransitionTime": "2025-06-17T14:57:04Z",
    "message": "",
    "observedGeneration": 2,
    "reason": "Ready",
    "status": "False",
    "type": "Degraded"
  },
  {
    "lastTransitionTime": "2025-11-27T05:58:38Z,
    "message": "reconciliation successful",
    "observedGeneration": 2,
    "reason": "Ready",
    "status": "True",
    "type": "Ready"
  }
]
----

.Next step

* Configure the network policies of the operand as described in "Configuring network policy for the operand".

//== updating external secrets channels
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-update-channels_{context}"]
= Understanding update channels of the {external-secrets-operator}

[role="_abstract"]
Control the version of the {external-secrets-operator} in your cluster by selecting an update channel. By using this mechanism, you can declare a specific version track, ensuring your environment receives only the updates you require for stability.

The {external-secrets-operator} offers the following update channels:

* `stable-v1`
* `stable-v1.y`

//== updating external secrets stable v1 channels
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-stablev1-channel_{context}"]
= About the {external-secrets-operator} stable-v1 channel

[role="_abstract"]
Select the `stable-v1` channel to install and update the latest release of the {external-secrets-operator}. By selecting this channel, you can use the most recent stable release for your Operator.

[NOTE]
====
The `stable-v1` channel is the default and suggested channel while installing the {external-secrets-operator}.
====

The `stable-v1` channel offers the following update approval strategies:

Automatic:: If you choose automatic updates for an installed {external-secrets-operator}, a new version of the {external-secrets-operator} is available in the `stable-v1` channel. The Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without human intervention.

Manual:: If you select manual updates, when a newer version of the {external-secrets-operator} is available, OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the {cert-manager-operator} updated to the new version.

//== updating external secrets stable v1.y channels
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-install.adoc

[id="external-secrets-operator-stablev1-y-channel_{context}"]
= About the {external-secrets-operator} stable-v1.y channel

[role="_abstract"]
Select the stable-v1 channel to install and update the latest release of the {external-secrets-operator}. By selecting this channel, you can use the latest stable release and allows you to choose between automatic and manual updates.

The y-stream version of the {external-secrets-operator} installs updates from the `stable-v1.y` channels such as `stable-v1.0`, `stable-v1.1`, and `stable-v1.2`. Select the `stable-v1.y` channel if you want to use the y-stream version and stay updated to the z-stream version of the {external-secrets-operator}.

The `stable-v1.y` channel offers the following update approval strategies:

Automatic:: If you choose automatic updates for an installed {external-secrets-operator}, a new z-stream version of the {external-secrets-operator} is available in the `stable-v1.y` channel. OLM automatically upgrades the running instance of your Operator without human intervention.

Manual:: If you select manual updates, when a newer version of the {external-secrets-operator} is available, OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the {external-secrets-operator} updated to the new version of the z-stream releases.

[role="_additional-resources"]
[id="external-secrets-operator-update-channels_additional-resources"]
== Additional resources

* Adding Operators to a cluster
* Updating installed Operators
