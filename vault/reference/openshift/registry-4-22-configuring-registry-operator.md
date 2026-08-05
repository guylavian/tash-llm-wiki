---
title: "Image Registry Operator in {product-title}"
type: reference
domain: openshift
slug: registry-4-22-configuring-registry-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/configuring-registry-operator
version: 4.22
family: registry
documentKind: "Documentation"
---

# Image Registry Operator in {product-title}

[id="configuring-registry-operator"]
= Image Registry Operator in OpenShift Container Platform

[id="image-registry-on-cloud"]
[role="_abstract"]
== Image Registry on cloud platforms and OpenStack
== Image Registry on OpenShift Container Platform

The Image Registry Operator installs a single instance of the {product-registry} and manages all registry configuration, including setting up registry storage.

[NOTE]
====
Storage is only automatically configured when you install an installer-provisioned infrastructure cluster on {aws-short}, {azure-short}, {gcp-short}, {ibm-name}, or {rh-openstack}.

When you install or upgrade an installer-provisioned infrastructure cluster on {aws-short}, {azure-short}, {gcp-short}, {ibm-name}, or {rh-openstack}, the Image Registry Operator sets the `spec.storage.managementState` parameter to `Managed`. If the `spec.storage.managementState` parameter is set to `Unmanaged`, the Image Registry Operator takes no action related to storage.
====

After the control plane deploys in the management cluster, the Operator creates a default `configs.imageregistry.operator.openshift.io` custom resource (CR) instance based on configuration detected in the cluster.

If insufficient information is available to define a complete `configs.imageregistry.operator.openshift.io` CR, the incomplete resource is defined and the Operator updates the resource status with information about what is missing.

The Image Registry Operator runs in the `CONTROL_PLANE_NAMESPACE` environment variable of the management cluster, and manages the registry instance in the `openshift-image-registry` namespace of the cluster. All configuration and workload resources for the registry reside in that namespace.
The Image Registry Operator runs in the `openshift-image-registry` namespace, and manages the registry instance in that location. All configuration and workload resources for the registry reside in that namespace.

[IMPORTANT]
====
The Image Registry Operator's behavior for managing the pruner is orthogonal to the `managementState` specified on the `ClusterOperator` object for the Image Registry Operator. If the Image Registry Operator is not in the `Managed` state, the image pruner can still be configured and managed by the `Pruning` custom resource.

However, the `managementState` of the Image Registry Operator alters the behavior of the deployed image pruner job:

* `Managed`: the `--prune-registry` flag for the image pruner is set to `true`.
* `Removed`: the `--prune-registry` flag for the image pruner is set to `false`, meaning the image pruner job only prunes image metadata in etcd.
====

[id="image-registry-on-bare-metal-vsphere"]
== Image Registry on bare metal, Nutanix, and vSphere

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * registry/configuring-registry-operator.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-baremetal.adoc
// * registry/configuring_registry_storage/configuring-registry-storage-vsphere.adoc

[id="registry-removed_{context}"]
= Image registry removed during installation

[role="_abstract"]
On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

// Module included in the following assemblies:
//
// * openshift_images/configuring-registry-operator.adoc

[id="registry-operator-distribution-across-availability-zones_{context}"]
= Image Registry Operator distribution across availability zones

[role="_abstract"]
The default configuration of the Image Registry Operator spreads image registry pods across topology zones to prevent delayed recovery times in case of a complete zone failure where all pods are impacted. Reference the example YAML to understand the default parameter values that the Image Registry Operator uses when the Operator deploys with a zone-related topology constraint:

[source,yaml]
----
  topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
----

Reference the following YAML to understand the default parameter value that the Image Registry Operator uses when the Operator deploys with a zone-related topology constraint, which applies to bare metal and vSphere instances:

[source,yaml]
----
 topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
----

As a cluster administrator. you can override the default `topologySpreadConstraints` section values by configuring the `configs.imageregistry.operator.openshift.io/cluster` spec file.

[role="_additional-resources"]
== Additional resources

* Configuring pod topology spread constraints

// Module included in the following assemblies:
//
// * openshift_images/configuring-registry-operator.adoc
// * registry/configuring-registry-operator.adoc

[id="registry-operator-configuration-resource-overview_{context}"]
= Image Registry Operator configuration parameters

[role="_abstract"]
You can configure the Image Registry Operator using the `configs.imageregistry.operator.openshift.io` resource.
The resource provides parameters for managing registry state, storage, logging, routing, and deployment settings.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`managementState`
|`Managed`: The Operator updates the registry as configuration resources
are updated.

`Unmanaged`: The Operator ignores changes to the configuration resources.

`Removed`: The Operator removes the registry instance and tear down any
storage that the Operator provisioned.

|`logLevel`
|Sets `logLevel` of the registry instance. Defaults to  `Normal`.

The following values for `logLevel` are supported:

* `Normal`
* `Debug`
* `Trace`
* `TraceAll`

|`httpSecret`
|Value needed by the registry to secure uploads, generated by default.

| `operatorLogLevel`
| The `operatorLogLevel` configuration parameter provides intent-based logging for the Operator itself and a simple way to manage coarse-grained logging choices that Operators must interpret for themselves. This configuration parameter defaults to `Normal`. It does not provide fine-grained control.

The following values for `operatorLogLevel` are supported:

* `Normal`
* `Debug`
* `Trace`
* `TraceAll`

|`proxy`
|Defines the Proxy to be used when calling master API
and upstream registries.

|`affinity`
|You can use the `affinity` parameter to configure pod scheduling preferences and constraints for Image Registry Operator pods.

Affinity settings can use the `podAffinity` or `podAntiAffinity` spec. Both options can use either `preferredDuringSchedulingIgnoredDuringExecution` rules or `requiredDuringSchedulingIgnoredDuringExecution` rules.

|`storage`
|`Storagetype`: Details for configuring registry storage, for example S3 bucket
coordinates. Normally configured by default.

|`readOnly`
|Indicates whether the registry instance should reject attempts to push new images or delete existing ones.

|`requests`
|API Request Limit details. Controls how many parallel requests a given registry
instance will handle before queuing additional requests.

|`defaultRoute`
|Determines whether or not an external route is defined using the default
hostname. If enabled, the route uses re-encrypt encryption. Defaults to `false`.

|`routes`
|Array of additional routes to create. You provide the hostname and certificate
for the route.

|`rolloutStrategy`
|Defines rollout strategy for the image registry deployment. Defaults to `RollingUpdate`.

|`replicas`
|Replica count for the registry.

|`disableRedirect`
| Controls whether to route all data through the registry, rather than redirecting to the back end. Defaults to `false`.

|`spec.storage.managementState`

a|
The Image Registry Operator sets the `spec.storage.managementState` parameter to `Managed` on new installations or upgrades of clusters using installer-provisioned infrastructure on AWS or Azure.

The Image Registry Operator sets the `spec.storage.managementState` parameter to `Managed` on new installations or upgrades of clusters on AWS.

* `Managed`: Determines that the Image Registry Operator manages underlying storage. If the Image Registry Operator's `managementState` is set to `Removed`, then the storage is deleted.
** If the `managementState` is set to `Managed`, the Image Registry Operator attempts to apply some default configuration on the underlying storage unit. For example, if set to `Managed`, the Operator tries to enable encryption on the S3 bucket before making it available to the registry. If you do not want the default settings to be applied on the storage you are providing, make sure the `managementState` is set to `Unmanaged`.
* `Unmanaged`: Determines that the Image Registry Operator ignores the storage settings. If the Image Registry Operator's `managementState` is set to `Removed`, then the storage is not deleted. If you provided an underlying storage unit configuration, such as a bucket or container name, and the `spec.storage.managementState` is not yet set to any value, then the Image Registry Operator configures it to `Unmanaged`.

|===

// Module included in the following assemblies:
//
// * openshift_images/configuring-registry-operator.adoc

[id="registry-operator-default-crd_{context}"]
= Enabling the Image Registry default route by using a CRD

[role="_abstract"]
In OpenShift Container Platform, the `Registry` Operator controls the {product-registry} feature and you define this Operator in the `configs.imageregistry.operator.openshift.io` Custom Resource Definition (CRD). If you need to automatically enable the Image Registry default route, patch the Image Registry Operator CRD.

.Procedure

* Patch the Image Registry Operator CRD:
+
[source,terminal]
----
$ oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
----

// Module included in the following assemblies:
//
// * registry/configuring-registry-operator.adoc
// * openshift_images/image-configuration.adoc

[id="images-configuration-cas_{context}"]
= Configuring additional trust stores for image registry access

[role="_abstract"]
You can add references to a config map that has additional certificate authorities (CAs) to be trusted during image registry access to the `image.config.openshift.io/cluster` custom resource (CR).

.Prerequisites

* The certificate authorities (CAs) must be PEM-encoded.

.Procedure

. Create a config map in the `openshift-config` namespace, then and use the config map name in the `AdditionalTrustedCA` parameter of the `image.config.openshift.io` CR. This adds CAs that should be trusted when the cluster contacts external image registries.
+
.Image registry CA config map example
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  registry.example.com: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
----
+
where:
+
`data:registry.example.com:`:: An example hostname of a registry for which this CA is to be trusted.
`data:registry-with-port.example.com..5000:`:: An example hostname of a registry with the port for which this CA is to be trusted. If the registry has a port, such as `registry-with-port.example.com:5000`, `:` must be replaced with `..`.
+
The PEM certificate content is the value for each additional registry CA to trust.

. Optional. Configure an additional CA by running the following command:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
----
+
[source,terminal]
----
$ oc edit image.config.openshift.io cluster
----
+
[source,yaml]
----
spec:
  additionalTrustedCA:
    name: registry-config
----

// Module included in the following assemblies:
//
// * registry/configuring-registry-operator.adoc

[id="registry-operator-config-resources-storage-credentials_{context}"]
= Configuring storage credentials for the Image Registry Operator

[role="_abstract"]
In addition to the `configs.imageregistry.operator.openshift.io` Custom Resource (CR) and ConfigMap resources, storage credential configuration is provided to the Operator by a separate secret resource. This resource is located within the `openshift-image-registry` namespace.

You can create an `image-registry-private-configuration-user` secret that in turn creates custom credentials needed for storage access and management. If default credentials exist, the custom credentials override the default credentials used by the Operator.

.Procedure

* Create an OpenShift Container Platform secret that contains the required keys.
+
[source,terminal]
----
$ oc create secret generic image-registry-private-configuration-user --from-literal=KEY1=value1 --from-literal=KEY2=value2 --namespace openshift-image-registry
----

[role="_additional-resources"]
== Additional resources

* Configuring the registry for AWS user-provisioned infrastructure
* Configuring the registry for {gcp-short} user-provisioned infrastructure
* Configuring the registry for Azure user-provisioned infrastructure
* Configuring the registry for bare metal
* Configuring the registry for vSphere
* Configuring the registry for {rh-openstack}
* Configuring the registry for {rh-storage-first}
* Configuring the registry for Nutanix
