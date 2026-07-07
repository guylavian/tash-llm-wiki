---
title: "Customizing the External Secrets Operator for Red Hat OpenShift"
type: reference
domain: openshift
slug: security-4-22-external-secrets-log-levels
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-log-levels
version: 4.22
family: security
documentKind: "Documentation"
---

# Customizing the External Secrets Operator for Red Hat OpenShift

[id="external-secrets-log-levels"]
= Customizing the External Secrets Operator for Red Hat OpenShift

[role="_abstract"]
You can customize the behavior of the {external-secrets-operator} operand components by configuring custom annotations, deployment lifecycle settings, and environment variables through the `ExternalSecretsConfig` custom resource (CR).

These configurations provide administrators with fine-grained control over the external-secrets deployment.

You can customize the {external-secrets-operator} operand by using the `ExternalSecretsConfig` custom resource (CR). The CR supports a set of deployment and runtime options, such as custom annotations, revision history limits, environment variables, resource limits, tolerations, and proxy settings—so you can control how the operand is deployed and run without editing the operand resources directly.

All supported options are defined in the `ExternalSecretsConfig` CR (for example under the `spec.controllerConfig` for controller-related settings). The Operator reconciles the operand from this CR. Changes made directly to operand resources are overwritten. Use the `ExternalSecretsConfig` CR as the only supported way to customize the operand.

For the complete list of fields and allowed values, see the `ExternalSecretsConfig` API reference in the {external-secrets-operator} documentation.

[role="_additional-resources"]
.Additional resources

* External Secrets Operator for Red Hat OpenShift APIs

// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-enable-operator-log-level_{context}"]
= Setting a log level for the {external-secrets-operator}

[role="_abstract"]
You can configure the log verbosity for the lifecycle manager. You must adjust this setting to troubleshoot issues related to the installation, upgrade, or configuration of the operator itself, rather than secret synchronization.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

* Update the subscription object for the {external-secrets-operator} to provide the verbosity level for the operator logs by running the following command:
+
[source,terminal]
----
$ oc -n <external_secrets_operator_namespace> patch subscription openshift-external-secrets-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"OPERATOR_LOG_LEVEL","value":"<log_level>"}]}}}'
----
+
where:

external_secrets_operator_namespace:: Specifies the namespace where the Operator is installed.

log_level:: Specifies the level of log detail. Values range from 1-5. The default is 2.

.Verification

. The External Secrets Operator pod is redeployed. Verify that the log level of the {external-secrets-operator} is updated by running the following command:
+
[source,terminal]
----
$ oc set env deploy/external-secrets-operator-controller-manager -n external-secrets-operator --list | grep -e OPERATOR_LOG_LEVEL -e container
----
+
The following example verifies that the log level of the {external-secrets-operator} is updated.
+
[source,terminal]
----
# deployments/external-secrets-operator-controller-manager, container manager
OPERATOR_LOG_LEVEL=2
----

. Verify that the log level of the {external-secrets-operator} is updated by running the `oc logs` command:
+
[source,terminal]
----
$ oc logs -n external-secrets-operator -f deployments/external-secrets-operator-controller-manager -c manager
----

// enable operand log level
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-enable-operand-log-level_{context}"]
= Setting a log level for the {external-secrets-operator} operand

[role="_abstract"]
You can troubleshoot common issues, such as secret synchronization failures, provider authentication errors, or data formatting problems, by configuring the log verbosity for the core controller.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

. Edit the `ExternalSecretsConfig` CR by running the following command:
+
[source,terminal]
----
$ oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Set the log level value by editing the `spec.appConfig.logLevel` section:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
...
spec:
  appConfig:
    logLevel: <log_level>
----
+
where:

log_level:: Supports the value range of 1-5. The log level gets mapped to the following operand support levels:
 * 1 - warnings
 * 2 - error logs
 * 3 - info logs
 * 4 and 5 - debug logs

. Save your changes and exit the editor.

// configure cert-manager certificate requirements
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-cert-manager-config_{context}"]
= Configuring cert-manager for the external-secrets certificate requirements

[role="_abstract"]
You can optionally configure cert-manager to manage certificates for the {external-secrets-operator} webhook and plugins. If you do not use cert-manager, the Operator automatically generates webhook certificates, but you must manually configure certificates for any plugins.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have created the `ExternalSecretsConfig` custom resource.
* You have installed the {cert-manager-operator}. For more information, see "Installing the {cert-manager-operator}"

.Procedure

. Edit the `ExternalSecretsConfig` custom resource by running the following command:
+
[source,terminal]
----
$  oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Configure `cert-manager` by editing the `spec.controllerConfig.certProvider.certManager` section as follows:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
...
spec:
  controllerConfig:
    certProvider:
      certManager:
        injectAnnotations: "true"
        issuerRef:
          name: <issuer_name>
          kind: <issuer_kind>
          group: <issuer_group>
        mode: Enabled
----
+
where:

injectAnnotation:: Must be set to `true` when enabled.
name:: Specifies the name of the issuer object referenced in `ExternalSecretsConfig`.
kind:: Specifies the API issuer. Can be set to either `Issuer` or `ClusterIssuer`.
group:: Specifies the API issuer group. The group name must be `cert-manager.io`.
mode:: Must be set to `Enabled`. This is an immutable field and cannot be modified once it is configured.

. Save your changes.

. After you update the `cert-manager` configurations in the `externalsecretsconfig.operator.openshift.io` object, you must manually delete `external-secrets-cert-controller` deployment by running the following command. This prevents performance degradation of the `external-secrets` application.
+
[source,terminal]
----
$ oc delete deployments.apps external-secrets-cert-controller -n external-secrets
----

. Optionally, you can delete other resources created for the `cert-controller` by running the following commands:
+
[source,terminal]
----
$ oc delete clusterrolebindings.rbac.authorization.k8s.io external-secrets-cert-controller
----
+
[source,terminal]
----
$ oc delete clusterroles.rbac.authorization.k8s.io external-secrets-cert-controller
----
+
[source,terminal]
----
$ oc delete serviceaccounts external-secrets-cert-controller -n external-secrets
----
+
[source,terminal]
----
$ oc delete secrets external-secrets-webhook -n external-secrets
----

[role="_additional-resources"]
[id="external-secrets-log-levels_additional-resources"]
.Additional resources

* External Secrets Operator for Red Hat OpenShift APIs
* cert-manager Operator for Red Hat Openshift
* Installing the cert-manager-Operator for Red Hat Openshift

// configuring bitwarden
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-bit-warden-config_{context}"]
= Configuring the bitwardenSecretManagerProvider plugin

[role="_abstract"]
You must configure the `bitwardenSecretManagerProvider` plugin to enable communication with the Bitwarden API. This configuration enables the Operator to authenticate and fetch secrets for synchronization.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

. Edit the `ExternalSecretsConfig` custom resource by running the following command:
+
[source,terminal]
----
$  oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Edit the `spec.plugins.bitwardenSecretManagerProvider` section as follows to enable the Bitwarden Secrets Manager:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
...
spec:
  plugins:
    bitwardenSecretManagerProvider:
      mode: Enabled
      secretRef:
        name: <secret_object_name>
----
+
where:

name:: The name of the secret containing the certificate key pair for the plugin. The key name in the secret for the certificate must be `tls.crt`. The key name for the private key must be `tls.key`. The key name for the Certificate Authority (CA) certificate key name must be `ca.crt`. Configuring the secret is optional when the cert-manager certificate provider is configured.

. Save your changes and exit the editor.

. If you disable the plugin the following resources must be deleted manually by running the following commands:
+
[source,terminal]
----
$ oc delete deployments.apps bitwarden-sdk-server -n external-secrets
----
+
[source,terminal]
----
$ oc delete certificates.cert-manager.io bitwarden-tls-certs -n external-secrets
----
+
[source,terminal]
----
$ oc delete service bitwarden-sdk-server -n external-secrets
----
+
[source,terminal]
----
$ oc delete serviceaccounts bitwarden-sdk-server -n external-secrets
----

// add custom annotations
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-enable-operator-adding-custom-annotations_{context}"]
= Adding custom annotations to external-secrets resources

[role="_abstract"]
To customize your resources, you can define up to 20 custom annotations in the custom resource (CR). The Operator merges the annotations with the defaults, prioritizes them, and safely preserves annotations set by external systems.

When an annotation is removed from the CR, the Operator automatically removes it from all managed resources during the next reconciliation. Annotations set by external sources, such as Kubernetes system annotations or annotations added by other controllers, are preserved and are not affected by the Operator.

Annotation keys containing the following reserved domain prefixes are not allowed and are rejected by validation if applied:

* `kubernetes.io/` (including subdomains such as `*.kubernetes.io/`)

* `k8s.io/` (including subdomains such as `*.k8s.io/`)

* `openshift.io/` (including subdomains such as `*.openshift.io/`)

* `cert-manager.io/`

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

. Edit the `ExternalSecretsConfig` CR by running the following command:
+
[source,terminal]
----
$ oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Add the `annotations` field under `spec.controllerConfig` as follows:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  name: cluster
spec:
  controllerConfig:
    annotations:
      prometheus.io/scrape: "true"
      example.com/environment: "production"
----

.Verification

. Verify that annotations are applied to the external-secrets deployment by running the following command:
+
[source,terminal]
----
$ oc get deployment external-secrets -n external-secrets -o jsonpath='{.metadata.annotations}' | jq .
----
+
The output should include the custom annotations you specified.

. Verify that annotations are applied to the pod template by running the following command:
+
[source,terminal]
----
$ oc get deployment external-secrets -n external-secrets -o jsonpath='{.spec.template.metadata.annotations}' | jq .
----
+
The output should include the custom annotations you specified.

. Verify that annotations are applied to other managed resources such as Services by running the following command:
+
[source,terminal]
----
$ oc get service external-secrets-webhook -n external-secrets -o jsonpath='{.metadata.annotations}' | jq .
----
+
The output should include the custom annotations you specified.

// configure history limit
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-enable-operator-configure-history-limit_{context}"]
= Configuring the revisionHistoryLimit for external-secrets components

[role="_abstract"]
Configure the number of old `ReplicaSet` objects retained for rollback by setting the `revisionHistoryLimit` parameter for `external-secrets` components.

The following components can be configured:

[cols="1,1",options="header"]
|===
| Component name
| Description

| `ExternalSecretsCoreController`
| The main `external-secrets` controller.

| `Webhook`
| The `external-secrets` webhook server.

| `CertController`
| The certificate controller for webhook TLS.

| `BitwardenSDKServer`
| The Bitwarden SDK server plugin.
|===

Each component can only have one configuration entry. A maximum of 4 component configuration entries are allowed, one per component.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

. Edit the `ExternalSecretsConfig` CR by running the following command:
+
[source,terminal]
----
$ oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Add the `componentConfigs` field under `spec.controllerConfig` as follows:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  name: cluster
spec:
  controllerConfig:
    componentConfigs:
      - componentName: ExternalSecretsCoreController
        deploymentConfigs:
          revisionHistoryLimit: 5
      - componentName: Webhook
        deploymentConfigs:
          revisionHistoryLimit: 3
----
+
where

`spec.controllerConfig.componentConfigs.componentName.deploymentConfigs.revisionHistoryLimit`:: Specifies the number of old `ReplicaSet` objects to retain for rollback. The value must be at least 1 to ensure rollback capability. The maximum value is 50. If not specified, the default is 10.

.Verification

* Verify that the `revisionHistoryLimit` parameter is applied to the deployment by running the following command:
+
[source,terminal]
----
$ oc get deployment external-secrets -n external-secrets -o jsonpath='{.spec.revisionHistoryLimit}'
----
+
The output should display the value you configured.

// Set custom environment variables
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-log-levels.adoc

[id="external-secrets-operator-set-custom-variables_{context}"]
=  Setting custom environment variables for external-secrets components

[role="_abstract"]
To configure component behavior at runtime or integrate with external services, set custom environment variables for individual `external-secrets` components.

Custom environment variables are merged with the default environment variables set by the Operator. User-specified variables take precedence in case of conflicts with the Operator defaults. A maximum of 50 custom environment variables can be specified per component.

The environment variable names starting with the following prefixes are reserved:

* `HOSTNAME`

* `KUBERNETES_`

* `EXTERNAL_SECRETS_`

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.

* You have created the `ExternalSecretsConfig` custom resource.

.Procedure

. Edit the `ExternalSecretsConfig` CR by running the following command:
+
[source,terminal]
----
$ oc edit externalsecretsconfigs.operator.openshift.io cluster
----

. Add the `overrideEnv` field under the desired component in the `spec.controllerConfig.componentConfigs` stanza as follows:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ExternalSecretsConfig
metadata:
  name: cluster
spec:
  controllerConfig:
    componentConfigs:
      - componentName: ExternalSecretsCoreController
        overrideEnv:
          - name: Example
            value: "4"
----
+
where

`spec.controllerConfig.componentConfigs.overrideEnv.name`:: Specifies the name of the environment variable. Environment variable names starting with `HOSTNAME`, `KUBERNETES_`, or `EXTERNAL_SECRETS_` are reserved and are not allowed.

`spec.controllerConfig.componentConfigs.overrideEnv.value`:: Specifies the value of the environment variable.

.Verification

* Verify that the environment variable is set on the deployment by running the following command:
+
[source,terminal]
----
$ oc set env deployment/external-secrets -n external-secrets --list
----
+
The output should include the custom environment variable you specified.
