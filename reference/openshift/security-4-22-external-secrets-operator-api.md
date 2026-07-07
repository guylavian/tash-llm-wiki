---
title: "External Secrets Operator for Red Hat OpenShift APIs"
type: reference
domain: openshift
slug: security-4-22-external-secrets-operator-api
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/external-secrets-operator-api
version: 4.22
family: security
documentKind: "Documentation"
---

# External Secrets Operator for Red Hat OpenShift APIs

[id="external-secrets-operator-api"]
= External Secrets Operator for Red Hat OpenShift APIs

[role="_abstract"]
{external-secrets-operator} uses the following two APIs to configure the `external-secrets` application deployment.

//:FeatureName: The {external-secrets-operator}
//include::snippets/technology-preview.adoc[leveloffset=+1]

[cols="1,1,1",options="header"]
|===
| Group
| Version
| Kind

| `operator.openshift.io`
| `v1alpha1`
| `externalsecretsConfig`

| `operator.openshift.io`
| `v1alpha1`
| `externalsecretsmanager`
|===

The following list contains the {external-secrets-operator} APIs:

* ExternalSecretsConfig
* ExternalSecretsManager

//ExternalSecretsManagerList
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-manager-list_{context}"]
= externalSecretsManagerList

[role="_abstract"]
The `externalSecretsManagerList` object fetches the list of `externalSecretsManager` objects.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `apiVersion`
| _string_
| The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.
|
|

| `kind`
| _string_
| `kind` specifies the type of the object, which is `externalSecretsManagerList` for this API.
|
|

| `metadata`
| _ListMeta_
| Refer to Kubernetes API documentation for details about the `metadata` fields.
|
|

| `items`
| _array_
|
|
|
|===

//ExternalSecretsManager
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-manager_{context}"]
= externalSecretsManager

[role="_abstract"]
The `externalSecretsManager` object defines the configuration and information of deployments managed by the {external-secrets-operator-short}. Set the name to `cluster` as this allows only one instance of `externalSecretsManager` per cluster. You can configure global options by using `externalSecretsManager`. This serves as a centralized configuration for managing multiple controllers of the Operator. The Operator automatically creates the `externalSecretsManager` object during installation.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `apiVersion`
| _string_
| The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.
|
|

| `kind`
| _string_
| `kind` specifies the type of the object, which is `externalSecretsManager` for this Object.
|
|

| `metadata`
| _ObjectMeta_
| Refer to Kubernetes API documentation for details about the `metadata` fields.
|
|

| `spec`
| _object_
| `spec` contains specifications of the desired behavior.
|
|

| `status`
| _object_
| `status` displays the most recently observed state of the controllers in the {external-secrets-operator-short}.
|
|
|===

//ExternalSecretsConfigList
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-list_{context}"]
= externalSecretsConfigList

[role="_abstract"]
The `externalSecretsConfigList` object fetches the list of `externalSecretsConfig` objects.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `apiVersion`
| _string_
| The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`
|
|

| `kind`
| _string_
| `kind` specifies the type of the object, which is `externalSecretsList` for this API.
|
|

| `metadata`
| _ListMeta_
| Refer to Kubernetes API documentation for details about the `metadata` fields.
|
|

| `items`
| _array_
| `Items` contains a list of `externalSecrets` objects.
|
|
|===

//ExternalSecretsConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets_{context}"]
= externalSecretsConfig

[role="_abstract"]
The `externalSecretsConfig` object defines the configuration and information for the managed `external-secrets` operand deployment. Set the name to `cluster` as `externalSecretsConfig` object allows only one instance per cluster.

Creating an `externalSecretsConfig` object triggers the deployment of the `external-secrets` operand and maintains the desired state.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `apiVersion`
| _string_
| The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.
|
|

| `kind`
| _string_
| `kind` specifies the type of the object, which is `externalSecrets` for this object.
|
|

| `metadata`
| _ObjectMeta_
| Refer to Kubernetes API documentation for details about the `metadata` fields.
|
|

| `spec`
| _object_
| `spec` contains the specifications of the desired behavior of the `externalSecrets` object.
|
|

| `status`
| _object_
| `status` displays the most recently observed status of the `externalSecrets` object.
|
|

|===

//ExternalSecretsManagerSpec
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-manager-spec_{context}"]
= externalSecretsManagerSpec

[role="_abstract"]
The `externalSecretsManagerSpec` field defines the desired behavior of the `externalSecretsManager` object.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| type
| Description
| Default
| Validation

| `globalConfig`
| _object_
| `globalConfig` configures the behavior of deployments that {external-secrets-operator-short} manages.
|
| Optional
|===

//externalSecretsManagerStatus
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-manager-status_{context}"]
= externalSecretsManagerStatus

[role="_abstract"]
The `externalSecretsManagerStatus` field shows the most recently observed status of the `externalSecretsManager` object.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `controllerStatuses`
|  _array_
| `controllerStatuses` holds the observed conditions of the controllers used by the Operator.
|
|

| `lastTransitionTime`
| _Time_
| `lastTransitionTime` records the most recent time the status of the condition changed.
|
| Format: date-time

Type: string
|===

//ExternalSecretsConfigSpec
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-spec_{context}"]
= externalSecretsConfigSpec

[role="_abstract"]
The `externalSecretsConfigSpec` field defines the desired behavior of the `externalSecrets` object.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `appConfig`
| _object_
| `appConfig` configures the behavior of the `external-secrets` operand.
|
| Optional

| `plugins`
| _object_
| `plugins` configures the optional provider plugins.
|
| Optional

| `controllerConfig`
| _object_
| `controllerConfig` configures the controller to set up defaults that enable `external-secrets` operand.
|
| Optional
|===

//externalSecretsConfigStatus
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-status_{context}"]
= externalSecretsConfigStatus

[role="_abstract"]
The `externalSecretsConfigStatus` field shows the most recently observed status of the `externalSecretsConfig` Object.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `conditions`
| _Condition_ _array_
| `conditions` contains information about the current state of deployment.
|
|

| `externalSecretsImage`
| _string_
| `externalSecretsImage` specifies the image name and tag used for deploy `external-secrets` operand.
|
|

| `bitwardenSDKServerImage`
| _string_
| `bitwardenSDKServerImage` specifies the name of the image and tag used for deploying the `bitwarden-sdk-server`.
|
|
|===

//GlobalConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-global-config_{context}"]
= globalConfig

[role="_abstract"]
The `globalConfig` field defines the baseline behavior and deployment parameters for the {external-secrets-operator}. Use this section to apply labels to all managed resources and configure the logging verbosity. It also provides infrastructure-level controls to govern where and how the Operator is scheduled, alongside proxy settings for network compatibility.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `labels`
| _integer_
| `labels` applies to all resources created by the Operator. This field can have a maximum of 20 entries
| 1
| The maximum number of properties is 20

The minimum number of properties is 0

Optional

| `logLevel`
| _integer_
| `logLevel` supports a range of values as defined in the kubernetes logging guidelines.
| 1
| The maximum range value is 5

The minimum range value is 1

Optional

| `resources`
| _ResourceRequirements_
| `resources` defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see 
|
| Optional

| `affinity`
| _Affinity_
| `affinity` sets the scheduling affinity rules. For more information, see 
|
| Optional

| `tolerations`
| _Toleration_ _array_
| `tolerations` sets the pod tolerations. For more information, see 
|
| The maximum number of items is 50

The minimum number of items is 0

Optional

| `nodeSelector`
| _object (keys:string, values:string)_
| `nodeSelector` defines the scheduling criteria by using the node labels. For more information, see 
|
| The maximum number of properties is 50

The minimum number of properties is 0

Optional

| `proxy`
| _object_
| `proxy` sets the proxy configurations available in the operand containers managed by the Operator as environment variables.
|
| Optional
|===

//ControllerConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-controller-config_{context}"]
= controllerConfig

[role="_abstract"]
The `controllerConfig` specifies the configurations used by the controller when installing the `external-secrets` operand and the plugins.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `certProvider`
| _string_
| `certProvider` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.
|
| Optional

| `labels`
| _object (keys:string, values:string)_
| `labels` field applies labels to all resources created for the `external-secrets` operand deployment.
|
a| The maximum number of properties is 20.

The minimum number of properties is 0.

Optional

| `annotations`
| _object (keys:string, values:string)_
| `annotations` add custom annotations to all the resources created for the `external-secrets` deployment. The annotations are merged with any default annotations set by the Operator. User-specified annotations take precedence over defaults in case of conflicts. Annotation keys containing the reserved domains `kubernetes.io/`, `openshift.io/`, `k8s.io/`, or `cert-manager.io/` (including subdomains like `*.kubernetes.io/`) are not allowed.
|
a| The maximum number of properties is 20.

The minimum number of properties is 0.

Optional

| `componentConfigs`
| _ComponentConfig array_
| `componentConfigs` allows specifying deployment-level configuration overrides for individual `external-secrets` components. Each component can have only one configuration entry.
a| The maximum number of items is 4.

The minimum number of items is 0.

Optional

|===

//controllerStatus
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-controller-status_{context}"]
= controllerStatus

[role="_abstract"]
The `controllerStatus` field tracks the health and synchronization state of the individual controllers managed by the Operator. It identifies each controller by name, details its current operational conditions, and verifies that the controller is processing the latest configuration version.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `name`
| _string_
| `name` specifies the name of the controller for which the observed condition is recorded.
|
| Required

| `conditions`
| _array_
| `conditions` contains information about the current state of the {external-secrets-operator-short} controllers.
|
|

| `observedGeneration`
| _integer_
| `observedGeneration` represents the `.metadata.generation` on the observed resource.
|
| The minimum number of observed resources is 0.
|===

//ApplicationConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-external-secrets-config_{context}"]
= applicationConfig

[role="_abstract"]
The `applicationConfig` object customizes the runtime behavior and deployment constraints of the operand. Use this section to control observability, define the operational scope, and configure webhook specifics. Additionally, you can tailor the deployment to your infrastructure requirements.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `logLevel`
| _integer_
| `logLevel` supports a range of values as defined in the kubernetes logging guidelines.
| 1
| The maximum range value is 5

The minimum range value is 1

Optional

| `operatingNamespace`
| _string_
| `operatingNamespace` restricts the `external-secrets` operand operations to the provided namespace. Enabling this field disables `ClusterSecretStore` and `ClusterExternalSecret`.
|
| The maximum length is 63

The minimum length is 1

Optional

| `webhookConfig`
| _object_
| `webhookConfig` configures webhook specifics of the `external-secrets` operand.
|
|

| `resources`
| _ResourceRequirements_
| `resources` defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see 
|
| Optional

| `affinity`
| _Affinity_
| `affinity` sets the scheduling affinity rules. For more information, see 
|
| Optional

| `tolerations`
| _Toleration_ _array_
| `tolerations` sets the pod tolerations. For more information, see 
|
| The maximum number of items is 50

The minimum number of items is 0

Optional

| `nodeSelector`
| _object (keys:string, values:string)_
| `nodeSelector` defines the scheduling criteria by using node labels. For more information, see 
|
| The maximum number of properties is 50

The minimum number of properties is 0

Optional

| `proxy`
| _object (keys:string, values:string)_
| `proxy` sets the proxy configurations available in operand containers managed by the Operator as environment variables.
|
| Optional
|===

//bitwardenSecretManagerProvider
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-bitwarden-secret_{context}"]
= bitwardenSecretManagerProvider

[role="_abstract"]
To enable the Bitwarden secrets manager provider and set up the additional service required to connect to the Bitwarden server, you can configure the `bitwardenSecretManagerProvider` field.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `mode`
| _string_
| `mode` field enables the `bitwardenSecretManagerProvider` provider state, which can be set to `Enabled` or `Disabled`. If set to `Enabled`, the Operator ensures the plugin is deployed and synchronized. If set to `Disabled`, the Bitwarden provider plugin reconciliation is disabled. The plugin and resources remain in their current state, and are not managed by the Operator.
| `Disabled`
| enum: [Enabled Disabled]

Optional

| `secretRef`
| _SecretReference_
| `SecretRef` specifies the Kubernetes secret that contains the TLS key pair for the Bitwarden server. If this reference is not provided and the `certManagerConfig` field is configured, the issuer defined in `certManagerConfig` generates the required certificate. The secret must use `tls.crt` for certificate, `tls.key` for the private key, and `ca.crt` for CA certificate.
|
| Optional
|===

//WebhookConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-web-hook-config_{context}"]
= webhookConfig

[role="_abstract"]
The `webhookConfig` field configures the specifics of the `external-secrets` application webhook.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `certificateCheckInterval`
| _Duration_
| `certificateCheckInterval` configures the polling interval to check certificate validity.
| 5m
| Optional
|===

//CertManagerConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-cert-manager-config_{context}"]
= certManagerConfig

[role="_abstract"]
You can integrate the {external-secrets-operator} with cert-manager to secure internal webhooks. Use these settings to replace the default internal certificate management with cert-manager, specify custom issuers, and define certificate lifecycle and renewal policies.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `mode`
| _string_
| `mode` specifies whether to use cert-manager for certificate management instead of the built-in `cert-controller` which can be indicated by setting either `Enabled` or `Disabled`. If set to `Enabled`, uses `cert-manager` for obtaining the certificates for the webhook server and other components. If set to `Disabled`, uses the `cert-controller` for obtaining the certificates for the webhook server. `Disabled` is the default behavior.
| false
| enum: [true false]

Required

| `injectAnnotations`
| _string_
| `injectAnnotations` adds the `cert-manager.io/inject-ca-from` annotation to the webhooks and custom resource definitions (CRDs) to automatically configure the webhook with the `cert-manager` Operator certificate authority (CA). This requires CA Injector to be enabled in `cert-manager` Operator. Set this field to `true` or `false`. When set, this field cannot be changed.
| false
| enum: [true false]

Optional

| `issuerRef`
| _ObjectReference_
| `issuerRef` contains details of the referenced object used for obtaining certificates. The object must exist in the `external-secrets` namespace unless a cluster-scoped `cert-manager` Operator issuer is used.
|
| Required

| `certificateDuration`
| _Duration_
| `certificateDuration` sets the validity period of the webhook certificate.
| 8760h
| Optional

| `certificateRenewBefore`
| _Duration_
| `certificateRenewBefore` sets the ahead time to renew the webhook certificate before expiry.
| 30m
| Optional
|===

//CertProvidersConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-cert-providers-config_{context}"]
= certProvidersConfig

[role="_abstract"]
The `certProvidersConfig` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `certManager`
| _object_
| `certManager` defines the configuration for `cert-manager` provider specifics.
|
| Optional
|===

//ObjectReference
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-object-reference_{context}"]
= objectReference

[role="_abstract"]
The `ObjectReference` object acts as a pointer to a specific Kubernetes resource. It uniquely identifies the target by requiring its name, and optionally, helps scope the reference to a specific resource type and API group.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `name`
| _string_
| `name` specifies the name of the resource being referred to.
|
| The maximum length is 253 characters.

The minimum length is 1 character.

Required

| `kind`
| _string_
| `kind` specifies the kind of the resource being referred to.
|
| The maximum length is 253 characters.

The minimum length is 1 character.

Optional

| `group`
| _string_
| `group` specifies the group of the resource being referred to.
|
| The maximum length is 253 characters.

The minimum length is 1 character.

Optional
|===

//secretReference
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-secret-reference_{context}"]
= secretReference

[role="_abstract"]
The `secretReference` field refers to a secret with the given name in the same namespace where it used.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `name`
| _string_
| `name` specifies the name of the secret resource being referred to.
|
| The maximum length is 253.

The minimum length is 1.

Required
|===

//condition
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-condition_{context}"]
= condition

[role="_abstract"]
The `condition` object reports the current health and operational state of the {external-secrets-operator} deployment. It provides a standardized status check by detailing the specific type of condition, its current status, and a message to verify deployment success or troubleshooting errors.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `type`
| _string_
| `type` contains the condition of the deployment.
|
| Required

| `status`
| _ConditionStatus_
| `status` contains the status of the condition of the deployment
|
|

| `message`
| _string_
| `message` provides details on the state of the deployment
|
|
|===

//conditionalStatus
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-conditional-status_{context}"]
= conditionalStatus

[role="_abstract"]
The `conditionalStatus` field holds information about the current state of the `external-secrets` deployment.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `conditions`
| _array_
| `conditions` contains information on the current state of the deployment.
|
|
|===

//mode
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-mode_{context}"]
= mode

[role="_abstract"]
The `mode` field indicates the operational state of the optional features.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `Enabled`
|
| `Enabled` indicates the optional configuration is enabled.
|
|

| `Disabled`
|
| `Disabled` indicates the optional configuration is disabled.
|
|
|===

//pluginsConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-plugiins-config_{context}"]
= pluginsConfig

[role="_abstract"]
The `pluginsConfig` configures the optional plugins.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `bitwardenSecretManagerProvider`
| _object_
| `bitwardenSecretManagerProvider` enables the `bitwarden-secrets-manager` provider plugin for connecting with the 'bitwarden-secrets-manager'.
|
| Optional
|===

//ProxyConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-proxy-config_{context}"]
= proxyConfig

[role="_abstract"]
The `proxyConfig` object defines the network proxy settings that the Operator injects into managed containers as environment variables. Use this configuration to ensure proper connectivity in restricted network environments, or to bypass the proxy and connect directly.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `httpProxy`
| _string_
| The `httpProxy` field contains the URL of the proxy for HTTP requests. This field can have a maximum of 2048 characters.
|
| The maximum length is 2048 characters.

The minimum length is 0 characters.

Optional

| `httpsProxy`
| _string_
| The `httpsProxy` field contains the URL of the proxy for HTTPS requests. This field can have a maximum of 2048 characters.
|
| The maximum length is 2048 characters.

The minimum length is 0 characters.

Optional

| `noProxy`
| _string_
| The `noProxy` field is a comma-separated list of hostnames, classless inter-domain routings (CIDRs), and IP addresses or a combination of the three for which the proxy should not be used. This field can have a maximum of 4096 characters.
|
| The maximum length is 4096 characters.

The minimum length is 0 characters.

Optional
|===

//componentConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-comoponent-config_{context}"]
= componentConfig

[role="_abstract"]
The `componentConfig` field defines configuration overrides for a specific `external-secrets` component.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `componentName`
| _string_
| `componentName` identifies which `external-secrets` component this configuration applies to. Valid values are `ExternalSecretsCoreController`, `Webhook`, `CertController`, and `BitwardenSDKServer`.
|
a| Enum: [`ExternalSecretsCoreController`, `Webhook`, `CertController`, `BitwardenSDKServer`]

Required

| `deploymentConfigs`
| _object_
| `deploymentConfigs` specifies overrides for the Kubernetes Deployment resource of this component.
|
|Optional

| `overrideEnv`
a| *EnvVar*

_array_
| `overrideEnv` specifies custom environment variables for this component's container. These are merged with operator-managed environment variables, with user-defined values taking precedence. Environment variable names starting with `HOSTNAME`, `KUBERNETES_` or `EXTERNAL_SECRETS_` are reserved and are not allowed.
|
a| The maximum number of items is 50.

Optional
|===

//deploymentConfig
// Module included in the following assemblies:
//
// * security/external_secrets_operator/external-secrets-operator-api.adoc

[id="eso-deployment-config_{context}"]
= deploymentConfig

[role="_abstract"]
The `deploymentConfig` field defines configuration overrides for a Kubernetes Deployment resource.

[cols="1,1,1,1,1",options="header"]
|===
| Field
| Type
| Description
| Default
| Validation

| `revisionHistoryLimit`
| _integer_
| `revisionHistoryLimit` specifies the number of old `ReplicaSets` to retain for rollback purposes. This allows rolling back to previous deployment versions using the command `oc rollout undo`. Must be at least 1 to ensure rollback capability.
| 10
a| The minimum value is 1.

The maximum value is 50.

Optional
|===
