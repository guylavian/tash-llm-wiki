---
title: "Migrating from the community External Secrets Operator to the External Secrets Operator for Red Hat OpenShift"
type: reference
domain: openshift
slug: security-4-22-external-secrets-operator-migrate-downstream-upstream
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-operator-migrate-downstream-upstream
version: 4.22
family: security
documentKind: "Documentation"
---

# Migrating from the community External Secrets Operator to the External Secrets Operator for Red Hat OpenShift

[id="external-secrets-operator-migrate-downstream-upstream"]
= Migrating from the community External Secrets Operator to the External Secrets Operator for Red Hat OpenShift

[role="_abstract"]
You can migrate from the community version of the {external-secrets-operator-short}. Migrating to {external-secrets-operator} provides you with an officially supported product giving you access to enterprise-grade support. It also provides you with seamless integration from installation to upgrades.

The following migration versions have been fully tested.

[cols="1,1,1",options="header"]
|===
| Upstream version
| Installation method
| Downstream version

| 0.11.0
| OLM
| v1.0.0 GA

| 0.19.0
| Helm
| v1.0.0 GA
|===

[NOTE]
====
The migration does not support rollbacks.
====

[NOTE]
====
{external-secrets-operator} is based on the upstream version 0.19.0. Do not try to migrate from a higher version of the {external-secrets-operator-short}.
====

// Deleting the operatorconfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-delete-upstream-operatorconfig_{context}"]
= Deleting the community {external-secrets-operator-short}

[role="_abstract"]
Delete the configuration resource for the community Operator so that the legacy application is fully removed. This action prevents conflicts before installing the {external-secrets-operator}.

.Prerequisites

* You must be logged in as a user with the `cluster-admin` role.

* You must have the `oc` command-line tool installed and configured.

.Procedure

. Find your community Operator's `namespace` by running the following command:
+
[source,terminal]
----
$ oc get operatorconfigs.operator.external-secrets.io -A
----
+
The following is an example of finding the `namespace`:
+
[source,terminal]
----
NAMESPACE             NAME        AGE
external-secrets      cluster     9m18s
----

. Delete the `operatorconfig` custom resrouce (CR) by running the following command:
+
[source,terminal]
----
$ oc delete operatorconfig <config_name> -n <operator_namespace>
----

.Verification

. To verify that the `operatorconfig` CR is deleted, run the following command:
+
[source,terminal]
----
$ oc get operatorconfig -n <operator_namespace>
----
+
The command must return `no resource found`.

. To verify that the old webhooks are deleted, run the following commands:
+
[source,terminal]
----
$ oc get validatingwebhookconfigurations | grep external-secrets
----
+
[source,terminal]
----
$ oc get mutatingwebhookconfigurations | grep external-secrets
----
+
The commands must return no results.

// Uninstalling the upstream {external-secrets-operator}
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-uninstall-upstream-eso_{context}"]
= Uninstalling the community {external-secrets-operator-short}

[role="_abstract"]
Uninstall the community {external-secrets-operator-short} to prevent conflicts or accidental recreation after you migrate to {external-secrets-operator}.

You must uninstall the community {external-secrets-operator-short} to prevent it from being recreated or conflicting with the new one. The steps to uninstall are different based on how the community {external-secrets-operator-short} was installed but the prerequisites are the same for each.

// Uninstalling the upstream {external-secrets-operator} installed by helm
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-uninstall-helm_{context}"]
= Uninstalling a helm installed community {external-secrets-operator-short}

[role="_abstract"]
Remove the community {external-secrets-operator-short} that was installed using Helm. This helps you free up resources and maintain a clean environment for your cluster.

.Prerequisites

* You must be logged in as a user with the `cluster-admin` role.

* You must have deleted the `operatorconfig` custom resource (CR).

.Procedure

. Install the {external-secrets-operator}. The `external-secrets-operator` namespace must be null.

. Delete the {external-secrets-operator-short} by running the following command:
+
[source,terminal]
----
$ oc helm delete <release_name> -n <operator_namespace>
----
+
[NOTE]
====
Using `helm delete` might delete all Custom Resource Definitions (CRDs) and CRs. It is recommended to install the downstream Operator first if the namespace `external-secrets-operator` is empty.
====

// Uninstalling the upstream {external-secrets-operator} installed by OLM
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-uninstall-olm_{context}"]
= Uninstalling an Operator Lifecylce Manager installed community {external-secrets-operator-short}

[role="_abstract"]
Remove the community {external-secrets-operator-short} that was installed by an Operator Lifecycle Manager (OLM) subscription. This helps you free up resources and maintain a clean environment for your cluster.

.Prerequisites

* You must be logged in as a user with the `cluster-admin` role.

* You must have deleted the `operatorconfig` CR.

.Procedure

. Find the subscription name by running the following command:
+
[source,terminal]
----
$ oc get subscription -n <operator_namespace> | grep external-secrets
----

. Delete the subscription by running the following command:
+
[source,terminal]
----
$ oc delete subscription <subscription_name> -n <operator_namespace>
----

. Delete the `ClusterServiceVersion` by running the following command:
+
[source,terminal]
----
$ oc delete csv <csv_name> -n <operator_namespace>
----

// Uninstalling the upstream {external-secrets-operator} installed by raw manifests
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-uninstall-raw-manifests_{context}"]
= Uninstalling a raw manifest installed community {external-secrets-operator-short}

[role="_abstract"]
Remove the community {external-secrets-operator-short} that was installed by raw manifests. This helps you free up resources and maintain a clean environment for your cluster.

.Prerequisites

* You must be logged in as a user with the `cluster-admin` role.

* You must have deleted the `operatorconfig` CR.

.Procedure

* To remove the communiity {external-secrets-operator-short} that was installed by raw manifests, run the following command:
+
[source,terminal]
----
$ oc delete -f /path/to/your/old/manifests.yaml -n <operator_namespace>
----

// Removing {external-secrets-operator-short} using CLI
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-eso-install_{context}"]
= Installing the {external-secrets-operator}

[role="_abstract"]
Install the {external-secrets-operator} after cleaning up the community version. This establishes the officially supported service for managing secrets in your cluster.

// Create externalsecretsconfig and verify everything is running
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-migrate-downstream-upstream.adoc

[id="external-secrets-operator-create-externalsecretsconfig_{context}"]
= Creating the ExternalSecretsConfig Operator

[role="_abstract"]
Create the `ExternalSecretsConfig` resource to install and configure the core `external-secrets` component. This setup helps ensure that features like Bitwarden and cert-manager support are correctly enabled.

.Prerequisites

* {external-secrets-operator} is installed.

* {cert-manager-operator} is installed.

* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create an `externalsecretsconfig` file by defining a YAML file with the following content:
+
[source,yml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  labels:
    app.kubernetes.io/name: cluster
  name: cluster
spec:
  appConfig:
    logLevel: 1
  controllerConfig:
    networkPolicies:
      - componentName: ExternalSecretsCoreController
        egress:
          - {}
        name: allow-external-secrets-egress
  plugins: {}
----

. Create the `ExternalSecretsConfig` object by running the following command:
+
[source,terminal]
----
$ oc create -f externalsecretsconfig.yaml
----

.Verification

Verify that all custom resources (CRs) are present and that the APIs are using `v1` instead of `v1beta1`. There CRs are retained and automatically converted by the new Operator.

. To verify that the `external-secrets` pods are in a `running` state, run the following command:
+
[source,terminal]
----
$ oc get pods -n external-secret
----
+
The following is example output that the `external-secrets` pods are in a `running` state.
+
[source,terminal]
----
NAME                                          READY        STATUS        RESTARTS     AGE
bitwarden-sdk-server-5b4cf48766-w7zp7         1/1          Running       0            5m
external-secrets-5854b85dd5-m6zf9             1/1          Running       0            5m
external-secrets-webhook-5cb85b8fdb-6jtqb     1/1          Running       0            5m
----

. To verify that the `SecretStore` CR is present, run the following command:
+
[source,terminal]
----
$ oc get secretstores.external-secrets.io -A
----
+
The following is example output from validating that the `SecretStore` is present:
+
[source,terminal]
----
NAMESPACE               NAME                         AGE         STATUS      CAPABILITIES    READY
external-secrets-1      gcp-store                    18min       Valid       ReadWrite       True
external-secrets-2      aws-secretstore              11min       Valid       ReadWrite       True
external-secrets        bitwarden-secretsmanager     20min       Valid       Readwrite       True
----

. To verify that the `ExternalSecret` CR is present, run the following command:
+
[source,terminal]
----
$ oc get externalsecrets.external-secrets.io -A
----
+
The following is example output from validating that the `SecretStore` is present:
+
[source,terminal]
----
NAMESPACE             NAME                    STORE                      REFRESH INTERVAL    STATUS          READY
external-secrets-1    gcp-externalsecret      gcp-store                  1hr                 SecretSynced    True
external-secrets-2    aws-external-secret     aws-secret-store           1hr                 SecretSynced    True
external-secrets      bitwarden               bitwarden-secretsmanager   1hr                 SecretSynced    True
----

. To verify that the `SecretStore` is `apiVersion: external-secrets.io/v1`, run the following command:
+
[source,terminal]
----
$ oc get secretstores.external-secrets.io -n external-secrets-1 gcp-store -o yaml
----
+
The following is example output that the `SecretStore` is `apiVersion: external-secrets.io/v1`.
+
[source,yml]
----
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
  creationTimestamp: "2025-10-27T11:38:19Z"
  generation: 1
  name: gcp-store
  namespace: external-secrets-1
  resourceVersion: "104519"
  uid: 7bccb0cc-2557-4f4a-9caa-1577f0108f4b
spec:
.
.
.
status:
  capabilities: ReadWrite
  conditions:
  - lastTransitionTime: "2025-10-27T11:38:19Z"
    message: store validated
    reason: Valid
    status: "True"
    type: Ready
----

. To verify that the `ExternalSecret` is `apiVersion: external-secrets.io/v1`, run the following command:
+
[source,terminal]
----
$ oc get externalsecrets.external-secrets.io -n external-secrets-1 gcp-externalsecret -o yaml
----
+
The following is example output that the `ExternalSecret` is `apiVersion: external-secrets.io/v1`.
+
[source,yml]
----
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  creationTimestamp: "2025-10-27T11:39:03Z"
  generation: 1
  name: gcp-externalsecret
  namespace: external-secrets-1
  resourceVersion: "104532"
  uid: 93a3295a-a3ad-4304-90e1-1328d951e5fb
spec:
.
.
.
status:
  binding:
    name: k8s-secret-gcp
  conditions:
  - lastTransitionTime: "2025-10-27T11:39:03Z"
    message: secret synced
    reason: SecretSynced
    status: "True"
    type: Ready
  refreshTime: "2025-10-27T12:13:15Z"
  syncedResourceVersion: 1-f47fe3c0b255b6dd8047cdffa772587bb829efe7a1cb70febeda2eb2
----
