---
title: "Configuring cluster extensions"
type: reference
domain: openshift
slug: extensions-4-22-olmv1-configuring-extensions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/olmv1-configuring-extensions
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Configuring cluster extensions

[id="olmv1-configuring-extensions"]
= Configuring cluster extensions

[role="_abstract"]
You can customize Operator installations to control namespace scope and manage deployment behavior including resource allocation, node placement, and pod scheduling.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-config-api_{context}"]
= Extension configuration

[role="_abstract"]
Configure the namespace an extension watches by using the `.spec.config` field in the `ClusterExtension` resource.

Extensions watch all namespaces by default. Some Operators support only namespace-scoped watching based on {olmv0} install modes. Configure the `.spec.config.inline.watchNamespace` field to install these Operators.

Whether you must configure this field depends on the install modes supported by the bundle.

[id="olmv1-config-api-structure_{context}"]
== Configuration API structure

The configuration API uses an opaque structure. The bundle validates the configuration values, not {olmv1}. Operator authors can define their own configuration requirements.

Currently, the `Inline` configuration type is the only supported type:

.Example inline configuration
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
...
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <watch_namespace>
----
where:

`<installation_namespace>`:: Specifies the namespace where the extension components run.
`config.configType`:: Specifies the configuration type. Currently, `Inline` is the only supported type.
`<watch_namespace>`:: Specifies the namespace where the extension watches for custom resources. The watch namespace can match or differ from the installation namespace, depending on the install modes supported by the bundle.

[role="_additional-resources"]
.Additional resources

* Operator groups

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-config-api-watch-namespace-requirements_{context}"]
= Watch namespace configuration requirements

[role="_abstract"]
Avoid installation failures by using the correct `watchNamespace` value for the install modes supported by your bundle. Requirements vary based on whether the bundle supports `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

{olmv0} `registry+v1` bundles declare the install modes they support. These install modes control whether `watchNamespace` configuration is required or optional, and what values are valid.

[NOTE]
====
{olmv1} does not support multi-tenancy. You cannot install the same extension more than once on a cluster. As a result, the `MultiNamespace` install mode is not supported.
====

`AllNamespaces`:: Watches resources across all namespaces in the cluster.
`OwnNamespace`:: Watches resources only in the installation namespace.
`SingleNamespace`:: Watches resources in a single namespace that differs from the installation namespace.

Whether the `.spec.config.inline.watchNamespace` field is required depends on the install modes that the bundle supports.

.Watch namespace requirements by bundle capability
[cols="2,1,3",options="header"]
|===
| Bundle install mode support | watchNamespace field | Valid values

| `AllNamespaces` mode only
| Not applicable
| The `watchNamespace` field is not supported. Extensions watch all namespaces.

| `OwnNamespace` mode only
| Required
| Must match `.spec.namespace` field

| `SingleNamespace` mode only
| Required
| Must differ from `.spec.namespace` field

| Both `OwnNamespace` and `SingleNamespace` install modes
| Required
| Can match or differ from `.spec.namespace` field

| `AllNamespaces` install mode with one or both of the `OwnNamespace` and `SingleNamespace` install modes
| Optional
| Omit to watch all namespaces, or specify a namespace to watch only that namespace

|===

[IMPORTANT]
====
{olmv1} validates the `watchNamespace` value based on the install mode support that is declared by the bundle. The installation fails with a validation error if you specify an invalid value or omit a required field.
====

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc
// * extensions/ce/olmv1-supported-extensions.adoc

[id="olmv1-discovering-bundle-install-modes_{context}"]
= Discovering bundle install modes

[role="_abstract"]
You can render the bundle metadata to find which install modes a bundle supports.

.Prerequisites

* You have installed the `jq` CLI tool.
* You have installed the `opm` CLI tool.

.Procedure

. Render the bundle metadata by running the following command:
+
[source,terminal]
----
$ opm render <bundle_image> -o json | \
  jq 'select(.schema == "olm.bundle") | .properties[] | select(.type == "olm.bundle.object")'
----
+
.Example output
[source,json]
----
{
  "type": "olm.bundle.object",
  "value": {
    "data": "...",
    "ref": "olm.csv"
  }
}
----

. Decode the base64-encoded CSV data to view install mode declarations:
+
[source,terminal]
----
$ echo "<base64_data>" | base64 -d | jq '.spec.installModes'
----
+
.Example output
[source,json]
----
[
  {
    "type": "OwnNamespace",
    "supported": true
  },
  {
    "type": "SingleNamespace",
    "supported": true
  },
  {
    "type": "MultiNamespace",
    "supported": false
  },
  {
    "type": "AllNamespaces",
    "supported": false
  }
]
----
+
In this example, the bundle supports both `OwnNamespace` and `SingleNamespace` modes. The `.spec.config.inline.watchNamespace` field is required and can match or differ from the `.spec.namespace` field.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc
// * extensions/ce/olmv1-installing-an-operator-from-a-catalog.adoc

[id="olmv1-deploying-a-ce-in-a-specific-namespace_{context}"]
= Configuring a watch namespace for a cluster extension (Technology Preview)

[role="_abstract"]
You can configure the watch namespace for extensions that support namespace-scoped resource watching.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".
* You have verified the supported install modes for the extension and determined the required `watchNamespace` configuration.

.Procedure

. Create a custom resource (CR) based on where you want the extension to watch for resources:
+
** To configure the extension to watch its own installation namespace:
+
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <installation_namespace>
  serviceAccount:
    name: <service_account>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
      version: <version>
      upgradeConstraintPolicy: CatalogProvided
----
where:

`config.inline.watchNamespace`::  Specifies the namespace to watch for resources. For requirements and valid values, see "Extension configuration".

** To configure the extension to watch a different namespace:
+
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <watched_namespace>
  serviceAccount:
    name: <service_account>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
      version: <version>
      upgradeConstraintPolicy: CatalogProvided
----

. Apply the CR to the cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f <cluster_extension_cr>.yaml
----

.Verification

* Verify that the extension installed successfully by running the following command:
+
[source,terminal]
----
$ oc get clusterextension <extension_name> -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <installation_namespace>
  config:
    configType: Inline
    inline:
      watchNamespace: <installation_namespace>
status:
  conditions:
  - type: Installed
    status: "True"
    reason: Succeeded
----

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-config-api-watch-namespace-examples_{context}"]
= Watch namespace configuration examples

[role="_abstract"]
To configure the `watchNamespace` field correctly for your bundle's install mode, see the following examples. These show valid configurations for Operators that support the `AllNamespaces`, `OwnNamespace`, and `SingleNamespace` install modes.

.Example `AllNamespaces` install mode
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: openshift-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
----

* The `config` field is omitted. The extension watches all namespaces by default.

.Example `OwnNamespace` install mode
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: example-operators
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
----

* You must set the `watchNamespace` field to use the `OwnNamespace` install mode.
* The `watchNamespace` value must match the `spec.namespace` field value.

.Example `SingleNamespace` install mode
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: example-extension
spec:
  namespace: example-operators
  config:
    configType: Inline
    inline:
      watchNamespace: production
  serviceAccount:
    name: example-sa
  source:
    sourceType: Catalog
    catalog:
      packageName: example-operator
----

* You must set the `watchNamespace` field to use the `SingleNamespace` install mode.
* The `watchNamespace` value must differ from the `spec.namespace` field value.
* In this example, the extension runs in the `example-operators` namespace but watches resources in the `production` namespace.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-clusterextension-watchnamespace-validation-errors_{context}"]
= Watch namespace validation errors

[role="_abstract"]
Validation errors occur when the `watchNamespace` field is omitted or contains an invalid value for the install modes supported by the bundle.

.Common `watchNamespace` field validation errors
[cols="2,3,3",options="header"]
|===
| Error | Cause | Resolution

| Required field missing
| The bundle requires the `watchNamespace` field but it is omitted.
| Add the `watchNamespace` field with a value that matches the install modes supported by the bundle.

| `OwnNamespace` validation error
| The bundle only supports `OwnNamespace` mode but the `watchNamespace` value does not match the `.spec.namespace` field.
| Set the `watchNamespace` field to the same value as the `.spec.namespace` field.

| `SingleNamespace` validation error
| The bundle only supports `SingleNamespace` mode but the `watchNamespace` value matches the `.spec.namespace` field.
| Set the `watchNamespace` field to a different namespace than the `.spec.namespace` field.

| Invalid configuration
| The `.spec.config` structure is malformed or has unsupported fields.
| Verify the configuration follows the correct API structure with `configType: Inline` and valid `inline` fields.

|===

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-deployment-config-api_{context}"]
= deploymentConfig API

[role="_abstract"]
The `deploymentConfig` API controls Operator pod runtime settings such as resources, node placement, and environment variables, providing feature parity with {olmv0} Subscription configuration.

Provides feature parity with the `Subscription.spec.config` configuration of the {olmv0}. Configure resources, node placement, storage, environment variables, and other deployment settings.

[id="olmv1-deployment-config-structure_{context}"]
== deploymentConfig structure

Configure how the Operator deploys in the `spec.config.inline.deploymentConfig` field as a JSON object.

.Example `deploymentConfig` object
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: <extension_name>
spec:
  namespace: <installation_namespace>
  serviceAccount:
    name: <service_account_name>
  source:
    sourceType: Catalog
    catalog:
      packageName: <package_name>
  config:
    configType: Inline
    inline:
      deploymentConfig:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
----
where:
--
`serviceAccount:`:: Specifies the service account name for the Operator.
`source:`:: Specifies the package source configuration.
`deploymentConfig:`:: Specifies the object for customizing the deployment.
`resources:`:: Specifies the CPU and memory requests and limits.
`nodeSelector:`:: Specifies the node placement selector.
`tolerations:`:: Specifies the node taint tolerations.
--

[id="olmv1-deployment-config-fields_{context}"]
== Supported configuration fields

Environment variables:: Add or override environment variables with `env`. Values are merged with existing container environment variables, with `deploymentConfig` values taking precedence.

Environment variable sources:: Add environment variable sources with `envFrom`. Sources are appended to existing sources; duplicates are skipped.

Resource requirements:: Specify CPU and memory requests and limits with `resources`. Replaces existing resource requirements.

Node selector:: Control pod node placement with `nodeSelector`. Replaces existing node selector.

Tolerations:: Schedule pods on nodes with taints by using `tolerations`. Appended to existing tolerations.

Affinity rules:: Define pod affinity and anti-affinity rules with `affinity`. Non-nil fields replace corresponding bundle fields.

Volumes and volume mounts:: Add volumes and volume mounts. Volumes with the same name as existing bundle volumes are overridden; new volumes are appended.

Annotations:: Add custom pod annotations. Merged with existing annotations. Annotations already set by the bundle cannot be overridden.

[id="olmv1-deployment-config-validation_{context}"]
== Configuration validation

{olmv1} validates configuration against a JSON schema generated from Kubernetes API definitions. The schema derives from the `SubscriptionConfig` type used in {olmv0}, providing consistent validation across versions.

Invalid configurations prevent installation and report errors in the `ClusterExtension` resource's `Progressing` condition. Common validation errors include:

* Unknown field errors when using unsupported configuration options
* Type mismatch errors when field values do not match the expected type
* Required field errors when mandatory nested fields are missing

[NOTE]
====
{olmv1} applies configurations during the `ClusterObjectSet` deployment process, modifying Operator manifests before organizing them into phases.
====

[id="olmv1-deployment-config-migration_{context}"]
== Converting from {olmv0}

Transfer existing `Subscription.spec.config` settings to the `deploymentConfig` object. The YAML structure is the same, but some merge behaviors differ from {olmv0}.

[NOTE]
====
`volumes` and `volumeMounts` with the same name override existing entries in {olmv1} rather than appending as in {olmv0}.
====

.Example {olmv0} subscription configuration
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: my-operator
spec:
  name: my-operator
  channel: stable
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
    tolerations:
    - key: node-role.kubernetes.io/infra
      operator: Exists
      effect: NoSchedule
----

.Equivalent {olmv1} cluster extension configuration
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
----

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-clusterobjectsets-deployment-mechanism_{context}"]
= ClusterObjectSets deployment mechanism

[role="_abstract"]
`ClusterObjectSets` deploy cluster extensions through ordered phases, enabling safe upgrades by maintaining both old and new revisions until the new version succeeds.

`ClusterObjectSets` are cluster-scoped APIs representing versioned resource sets organized into ordered phases. {olmv1} uses `ClusterObjectSets` to deploy Operator resources sequentially.

[id="olmv1-clusterobjectsets-benefits_{context}"]
== Benefits

Phased rollouts:: Resources deploy in a defined order by kind. For example, Custom Resource Definitions (CRDs) are created before deployments that use them.

Safe upgrades:: Both old and new revisions remain active until the new version succeeds, mitigating service disruption.

Immutable revision records:: Immutable revisions provide a clear deployment record.

Large bundle support:: References externalized secrets to bypass the etcd 1.5 MiB size limit, enabling large bundle deployments.

[id="olmv1-clusterobjectsets-relationship_{context}"]
== Relationship to the deploymentConfig API

{olmv1} applies `deploymentConfig` settings during the `ClusterObjectSet` process, modifying Operator manifests before organizing them into phases.

[id="olmv1-clusterobjectsets-phases_{context}"]
== Deployment phases

Phases are system-determined groups that organize resources into ordered deployment stages based on their API group and kind. Objects are automatically assigned to well-known phases.

[NOTE]
====
All objects within a phase are applied in no particular order. The next phase begins only after all objects in the current phase pass their readiness probes.
====

The system assigns resources to the following phases in order:

`namespaces`:: `Namespace` objects.

`policies`:: `NetworkPolicy`, `PodDisruptionBudget`, and `PriorityClass` objects.

`identity`:: `ServiceAccount` objects.

`configuration`:: `Secret` and `ConfigMap` objects.

`storage`:: `PersistentVolume`, `PersistentVolumeClaim`, and `StorageClass` objects.

`crds`:: `CustomResourceDefinition` objects.

`roles`:: `ClusterRole` and `Role` objects.

`bindings`:: `ClusterRoleBinding` and `RoleBinding` objects.

`infrastructure`:: `Service`, `Issuer`, and `Certificate` objects.

`deploy`:: `Deployment` objects.

`scaling`:: `VerticalPodAutoscaler` objects.

`publish`:: `PrometheusRule`, `ServiceMonitor`, `PodMonitor`, `Ingress`, `Route`, and console resources.

`admission`:: `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` objects.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-inspecting-clusterobjectsets_{context}"]
= Inspecting ClusterObjectSets

[role="_abstract"]
Monitor and troubleshoot cluster extension deployments by viewing ClusterObjectSet phases, resource status, and revision history.

.Procedure

. List all `ClusterObjectSets` in the cluster by entering the following command:
+
[source,terminal]
----
$ oc get clusterobjectsets
----

. List `ClusterObjectSets` for a specific extension by running the following command:
+
[source,terminal]
----
$ oc get clusterobjectsets -l olm.operatorframework.io/owner-name=<extension_name>
----
+
Replace `<extension_name>` with your `ClusterExtension` name.

. View the details of a specific `ClusterObjectSet` by running the following command:
+
[source,terminal]
----
$ oc get clusterobjectset <clusterobjectset_name> -o yaml
----
+
Shows deployment phases, resource status, and conditions.

. Check the `ClusterExtension` status to see active revisions by running the following command:
+
[source,terminal]
----
$ oc get clusterextension <extension_name> -o jsonpath='{.status.activeRevisions}{"\n"}'
----
+
Shows the active revisions currently deployed.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-customizing-operator-deployments_{context}"]
= Customize operator deployments

[role="_abstract"]
Customize Operator pod deployments to meet production requirements by configuring resource allocation, node placement, and pod tolerations through the `ClusterExtension` resource.

.Prerequisites

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have enabled the `TechPreviewNoUpgrade` feature set on the cluster.
* You have created a service account and assigned enough role-based access controls (RBAC) to install, update, and manage the extension. For more information, see "Cluster extension permissions".
* You have installed the {oc-first}.
* You have identified the operator you want to install and customize.

.Procedure

. Create a `ClusterExtension` resource with `deploymentConfig` customizations:
+
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-installer
  config:
    configType: Inline
    inline:
      deploymentConfig:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
      version: 1.0.0
----
+
where:
+
--
`resources:`:: Specifies CPU and memory resource requests and limits for the Operator pod.
`nodeSelector:`:: Specifies pod scheduling restrictions to infrastructure nodes.
`tolerations:`:: Specifies pod tolerations that allow scheduling on nodes with the specified taint.
--

. Apply the `ClusterExtension` resource:
+
[source,terminal]
----
$ oc apply -f my-operator.yaml
----

. Verify the installation:
+
[source,terminal]
----
$ oc get clusterextension my-operator -o yaml
----

.Verification

* Verify that the `deploymentConfig` settings were applied:
+
[source,terminal]
----
$ oc get deployment -n my-operator-ns -l olm.operatorframework.io/owner-name=my-operator -o yaml
----
+
Check the deployment specification for your configured settings such as resource limits, node selectors, tolerations, and volumes.

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-deployment-config-examples_{context}"]
= `deploymentConfig` examples

[role="_abstract"]
Customize Operator deployments using resource limits, node placement, custom volumes, environment variables, and combined configurations.

[id="olmv1-deployment-config-env-vars_{context}"]
== Environment variables

Add environment variables for runtime configuration.

.Adding environment variables
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: kmm-operator
spec:
  namespace: openshift-kmm
  serviceAccount:
    name: kmm-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        env:
        - name: KMM_MANAGED
          value: "1"
  source:
    sourceType: Catalog
    catalog:
      packageName: kernel-module-management
----
where:
--
`KMM_MANAGED`:: Specifies the environment variable used when deploying the Kernel Module Management Operator in a hub-and-spoke configuration.
--

[id="olmv1-deployment-config-volumes_{context}"]
== Custom volumes

Mount a custom CA certificate for HTTPS communication through a proxy.

.Mounting a custom CA certificate
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        volumes:
        - name: trusted-ca
          configMap:
            name: trusted-ca
            items:
            - key: ca-bundle.crt
              path: tls-ca-bundle.pem
        volumeMounts:
        - name: trusted-ca
          mountPath: /etc/pki/ca-trust/extracted/pem
          readOnly: true
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
----
where:
--
`volumes:`:: Specifies a volume created from the `trusted-ca` config map.
`volumeMounts:`:: Specifies the volume mount to the Operator container at the specified path.
`mountPath:`:: Specifies the path where the certificate bundle is available inside the container.
--

[id="olmv1-deployment-config-affinity_{context}"]
== Pod anti-affinity

Spread Operator pods across nodes for high availability.

.Pod anti-affinity for high availability
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: my-operator
spec:
  namespace: my-operator-ns
  serviceAccount:
    name: my-operator-sa
  config:
    configType: Inline
    inline:
      deploymentConfig:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: app.kubernetes.io/name
                    operator: In
                    values:
                    - my-operator
                topologyKey: kubernetes.io/hostname
  source:
    sourceType: Catalog
    catalog:
      packageName: my-operator
----
where:
--
`podAntiAffinity:`:: Specifies anti-affinity rules for the Operator pod.
`preferredDuringSchedulingIgnoredDuringExecution:`:: Specifies soft constraints that the scheduler tries to enforce but does not guarantee.
`topologyKey`:: Specifies the topology key that groups nodes by hostname to ensure pods are spread across different nodes.
--

[id="olmv1-deployment-config-combined_{context}"]
== Multiple customizations

Combine multiple deployment customizations.

.Production Operator with combined customizations
[source,yaml]
----
apiVersion: olm.operatorframework.io/v1
kind: ClusterExtension
metadata:
  name: production-operator
spec:
  namespace: production-operators
  serviceAccount:
    name: production-operator-installer
  config:
    configType: Inline
    inline:
      deploymentConfig:
        resources:
          requests:
            cpu: 200m
            memory: 256Mi
          limits:
            cpu: 1000m
            memory: 1Gi
        env:
        - name: LOG_LEVEL
          value: info
        - name: ENABLE_METRICS
          value: "true"
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
        annotations:
          monitoring.openshift.io/scrape: "true"
          monitoring.openshift.io/port: "8080"
  source:
    sourceType: Catalog
    catalog:
      packageName: production-operator
      version: 2.1.0
----
where:
--
`resources:`:: Specifies memory and CPU requests and limits for the Operator pod.
`env:`:: Specifies environment variables for the Operator.
`nodeSelector:`:: Specifies that the pod runs on infrastructure nodes.
`tolerations:`:: Specifies pod tolerations that allow scheduling on nodes with the specified taint.
`annotations:`:: Specifies Prometheus monitoring annotations for the pod.
--

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-deployment-config-reference_{context}"]
= `deploymentConfig` field reference

[role="_abstract"]
Field reference for the `deploymentConfig` API including {olmv0} to {olmv1} field mappings and merge behavior for each configuration option.

[id="olmv1-deployment-config-field-mapping_{context}"]
== Field mapping from {olmv0} to {olmv1}

Field conversion from {olmv0} to {olmv1}:

.{olmv0} to {olmv1} configuration field mapping
[cols="1,1,2",options="header"]
|===
|{olmv0} field path
|{olmv1} field path
|Notes

|`spec.config.env`
|`spec.config.inline.deploymentConfig.env`
|Environment variables are merged. {olmv1} values take precedence over bundle values.

|`spec.config.envFrom`
|`spec.config.inline.deploymentConfig.envFrom`
|Environment variable sources are appended to bundle sources. Duplicates are skipped.

|`spec.config.resources`
|`spec.config.inline.deploymentConfig.resources`
|Resource specifications completely replace bundle resource requirements.

|`spec.config.nodeSelector`
|`spec.config.inline.deploymentConfig.nodeSelector`
|Node selectors completely replace bundle node selectors.

|`spec.config.tolerations`
|`spec.config.inline.deploymentConfig.tolerations`
|Tolerations are appended to bundle tolerations.

|`spec.config.affinity`
|`spec.config.inline.deploymentConfig.affinity`
|Affinity rules selectively override bundle affinity. Non-nil fields replace corresponding bundle fields.

|`spec.config.volumes`
|`spec.config.inline.deploymentConfig.volumes`
|Volumes override existing bundle volumes with the same name; new volumes are appended.

|`spec.config.volumeMounts`
|`spec.config.inline.deploymentConfig.volumeMounts`
|Volume mounts override existing bundle volume mounts with the same name; new mounts are appended.

|`spec.config.annotations`
|`spec.config.inline.deploymentConfig.annotations`
|Annotations are merged with bundle annotations. Bundle annotations take precedence on conflicts.

|`spec.config.selector`
|Not supported
|The `selector` field from {olmv0} is not supported in {olmv1}. This field was never used in {olmv0}.

|===

[id="olmv1-deployment-config-merge-behavior_{context}"]
== Merge and override behavior

Configuration fields have different merge behaviors:

Replace:: Completely replaces bundle values. Applies to: `resources`, `nodeSelector`

Append:: Adds to existing bundle values. Applies to: `tolerations`, `envFrom`

Override and append:: Overrides existing values with the same name; new values are appended. Applies to: `volumes`, `volumeMounts`

Merge with precedence:: Merges with bundle values. `deploymentConfig` values take precedence on conflicts. Applies to: `env`

Merge with bundle precedence:: Merges with bundle values. Bundle takes precedence on conflicts. Applies to: `annotations`

Selective override:: Non-nil fields replace corresponding bundle fields. Applies to: `affinity`

[id="olmv1-deployment-config-env-reference_{context}"]
== Environment variable fields

`env`:: Specifies an array of environment variable objects. Merged with existing container environment variables, with `deploymentConfig` values taking precedence. Each object has:
+
* `name`: Environment variable name (string, required).
* `value`: Environment variable value (string, optional).
* `valueFrom`: Reference to a secret or config map key (object, optional).

`envFrom`:: Specifies an array of environment variable source objects merged with existing sources. Each object can reference:
+
* `configMapRef`: Config map containing environment variables.
* `secretRef`: Secret containing environment variables.

[id="olmv1-deployment-config-resources-reference_{context}"]
== Resource requirements fields

`resources`:: Specifies compute resource requirements that completely replace existing bundle resource requirements. Contains:
+
* `requests`: Minimum resources required.
** `cpu`: CPU request (string, for example, `"100m"`, `"0.5"`).
** `memory`: Memory request (string, for example, `"128Mi"`, `"1Gi"`).
* `limits`: Maximum resources allowed.
** `cpu`: CPU limit (string).
** `memory`: Memory limit (string).

[id="olmv1-deployment-config-node-placement-reference_{context}"]
== Node placement fields

`nodeSelector`:: Specifies a map of key-value pairs for node selection. Completely replaces any existing node selector. Pods schedule only on nodes with all specified labels.
+
.Example node selector
[source,yaml]
----
nodeSelector:
  node-role.kubernetes.io/infra: ""
  disktype: ssd
----

`tolerations`:: Specifies an array of toleration objects appended to existing bundle tolerations. Each toleration has:
+
* `key`: Taint key (string).
* `operator`: Operator (string: `Exists`, `Equal`).
* `value`: Taint value (string, required if `operator` is `Equal`).
* `effect`: Taint effect (string: `NoSchedule`, `PreferNoSchedule`, `NoExecute`).
* `tolerationSeconds`: Time before pod eviction for `NoExecute` effect (integer).

`affinity`:: Specifies an affinity rules object. Non-nil fields replace corresponding bundle fields. Contains:
+
* `nodeAffinity`: Node label-based scheduling rules.
* `podAffinity`: Pod label-based scheduling rules.
* `podAntiAffinity`: Pod spreading rules across nodes.

[id="olmv1-deployment-config-storage-reference_{context}"]
== Storage fields

`volumes`:: Specifies an array of volume objects. Volumes with the same name as existing bundle volumes are overridden; new volumes are appended. All Kubernetes volume types are supported. Each volume requires a `name` field (string).

`volumeMounts`:: Specifies an array of volume mount objects. Volume mounts with the same name as existing bundle volume mounts are overridden; new mounts are appended. Each mount has:
+
* `name`: Volume name to mount (string, required).
* `mountPath`: The path within the container (string, required).
* `readOnly`: Whether the volume is read-only (boolean, optional).
* `subPath`: A path within the volume (string, optional).

[id="olmv1-deployment-config-metadata-reference_{context}"]
== Metadata fields

`annotations`:: Specifies a map of key-value pairs for deployment and pod annotations. Annotations are applied to both the deployment metadata and the pod template metadata. Annotations from `deploymentConfig` are merged with bundle annotations. When keys conflict, bundle annotations take precedence.
+
.Example annotations
[source,yaml]
----
annotations:
  monitoring.openshift.io/scrape: "true"
  monitoring.openshift.io/port: "8080"
----

// Module included in the following assemblies:
//
// * extensions/ce/olmv1-configuring-extensions.adoc

[id="olmv1-deployment-config-troubleshooting_{context}"]
= Troubleshooting `deploymentConfig`

[role="_abstract"]
Common `deploymentConfig` issues include validation errors, configuration verification problems, and annotation conflicts that can prevent successful Operator installation.

[id="olmv1-deployment-config-troubleshooting-validation_{context}"]
== Validation errors

Check the `Progressing` condition for validation errors when installation fails:

[source,terminal]
----
$ oc get clusterextension <extension_name> -o jsonpath='{.status.conditions[?(@.type=="Progressing")].message}'
----

Common validation errors and resolutions:

Unknown field:: Configuration includes an unsupported field. Remove unsupported fields.

Type mismatch:: Field value does not match the expected type. Verify field types match Kubernetes specifications.

Required field missing:: Mandatory nested field is missing. Complete all required fields in nested structures.

[id="olmv1-deployment-config-troubleshooting-applied_{context}"]
== Verifying applied configuration

Inspect the Operator deployment to verify applied configurations:

[source,terminal]
----
$ oc get deployment -n <namespace> -l olm.operatorframework.io/owner-name=<extension_name> -o yaml
----

Configuration locations in the deployment specification:

* **Environment variables**: `spec.template.spec.containers[].env` and `spec.template.spec.containers[].envFrom`
* **Resources**: `spec.template.spec.containers[].resources`
* **Node selector**: `spec.template.spec.nodeSelector`
* **Tolerations**: `spec.template.spec.tolerations`
* **Affinity**: `spec.template.spec.affinity`
* **Volumes**: `spec.template.spec.volumes` and `spec.template.spec.containers[].volumeMounts`
* **Annotations**: `metadata.annotations` and `spec.template.metadata.annotations`

[id="olmv1-deployment-config-troubleshooting-conflicts_{context}"]
== Annotation conflicts

Bundle annotations take precedence over `deploymentConfig` annotations when keys conflict. View the installed bundle information:

[source,terminal]
----
$ oc get clusterextension <extension_name> -o jsonpath='{.status.install.bundle}'
----

This returns the bundle name and version. To see the annotations applied to the Operator pod template:

[source,terminal]
----
$ oc get deployment -n <namespace> -l olm.operatorframework.io/owner-name=<extension_name> -o jsonpath='{.items[0].spec.template.metadata.annotations}'
----

To override a bundle annotation, modify the bundle or accept the bundle value.

[id="olmv1-configuring-extensions_additional-resources"]
[role="_additional-resources"]
== Additional resources

* Installing a cluster extension in all namespaces
* Assigning Pods to Nodes (Kubernetes)
* Taints and Tolerations (Kubernetes)
