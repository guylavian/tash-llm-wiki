---
title: "Cluster capabilities"
type: reference
domain: openshift
slug: installing-4-22-cluster-capabilities
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/cluster-capabilities
version: 4.22
family: installing
documentKind: "Documentation"
---

# Cluster capabilities

[id="cluster-capabilities"]
= Cluster capabilities

[role="_abstract"]
As a cluster administrator, you can use cluster capabilities to enable or disable optional components before installation. Additionally, you can enable cluster capabilities at anytime after installation.

[NOTE]
====
You cannot disable a cluster capability after it is enabled.
====

// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="enabling-cluster-capabilities_{context}"]
= Enabling cluster capabilities

[role="_abstract"]
If you are using an installation method that includes customizing your cluster by creating an `install-config.yaml` file, you can select which cluster capabilities you want to make available on the cluster.

[NOTE]
====
If you customize your cluster by enabling or disabling specific cluster capabilities, you must manually maintain your `install-config.yaml` file. New OpenShift Container Platform updates might declare new capability handles for existing components, or introduce new components altogether. Users who customize their `install-config.yaml` file should consider periodically updating their `install-config.yaml` file as OpenShift Container Platform is updated.
====

You can use the following configuration parameters to select cluster capabilities:

[source,yaml]
----
capabilities:
  baselineCapabilitySet: v4.11
  additionalEnabledCapabilities:
  - CSISnapshot
  - Console
  - Storage
----

`capabilities.baselineCapabilitySet`:: Specifies a baseline set of capabilities to install. Valid values are `None`, `vCurrent` and `v4.x`. If you select `None`, all optional capabilities are disabled. The default value is `vCurrent`, which enables all optional capabilities.

[NOTE]
====
`v4.x` refers to any value up to and including the current cluster version.
For example, valid values for a OpenShift Container Platform 4.12 cluster are `v4.11` and `v4.12`.
====

`capabilities.additionalEnabledCapabilities`:: Specifies a list of capabilities to explicitly enable. These capabilities are enabled in addition to the capabilities specified in `baselineCapabilitySet`.

[NOTE]
====
In this example, the default capability is set to `v4.11`. The `additionalEnabledCapabilities` field enables additional capabilities over the default `v4.11` capability set.
====

[role="_additional-resources"]
.Additional resources

* Installing a cluster on AWS with customizations
* Installing a cluster on {gcp-short} with customizations

// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="explanation_of_capabilities_{context}"]
= Optional cluster capabilities in OpenShift Container Platform 

[role="_abstract"]
Currently, cluster Operators provide the features for these optional capabilities.

The following sections summarize the features provided by each capability and what functionality you lose if you disable a functionality.

[role="_additional-resources"]
.Additional resources

* Cluster Operators reference

// Bare-metal capability
// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc
// *  installing/overview/cluster-capabilities.adoc

[id="cluster-bare-metal-operator_{context}"]

[role="_abstract"]
The Cluster Baremetal Operator is an optional cluster capability that can be disabled by cluster administrators during installation.

For more information about optional cluster capabilities, see "Cluster capabilities".
The Cluster Baremetal Operator provides the features for the `baremetal` capability.

The Cluster Baremetal Operator (CBO) deploys all the components necessary to take a bare-metal server to a fully functioning worker node ready to run OpenShift Container Platform compute nodes. The CBO ensures that the metal3 deployment, which consists of the Bare Metal Operator (BMO) and Ironic containers, runs on one of the control plane nodes within the OpenShift Container Platform cluster. The CBO also listens for OpenShift Container Platform updates to resources that it watches and takes appropriate action.

The bare-metal capability is required for deployments using installer-provisioned infrastructure. Disabling the bare-metal capability can result in unexpected problems with these deployments.

[IMPORTANT]
====
If the bare-metal capability is disabled, the cluster cannot provision or manage bare-metal nodes. Only disable the capability if there are no `BareMetalHost` resources in your deployment. The `baremetal` capability depends on the `MachineAPI` capability. If you enable the `baremetal` capability, you must also enable `MachineAPI`.
====

[NOTE]
====
Red{nbsp}Hat recommends that cluster administrators only disable the bare-metal capability during installations with user-provisioned infrastructure that do not have any `BareMetalHost` resources in the cluster.
====

Project::

cluster-baremetal-operator

[role="_additional-resources"]
.Additional resources

* Deploying installer-provisioned clusters on bare metal
* Preparing for bare metal cluster installation
* Configuration using the Bare Metal Operator

// Build capability
// Module included in the following assemblies:
//
// *  installing/overview/cluster-capabilities.adoc

[id="build-config-capability_{context}"]
= Build capability

[role="_abstract"]
The `Build` capability enables the `Build` API. The `Build` API manages the lifecycle of `Build` and `BuildConfig` objects.

[IMPORTANT]
====
If you disable the `Build` capability, the following resources will not be available in the cluster:

* `Build` and `BuildConfig` resources
* The `builder` service account

Disable the `Build` capability only if you do not require `Build` and `BuildConfig` resources or the `builder` service account in the cluster.
====

// Cloud controller manager capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-cloud-controller-manager-operator_{context}"]

[role="_abstract"]
The Cloud Controller Manager Operator provides features for the `CloudControllerManager` capability.

[NOTE]
====
Currently, disabling the `CloudControllerManager` capability is not supported on all platforms.
====

You can determine if your cluster supports disabling the `CloudControllerManager` capability by checking values in the installation configuration (`install-config.yaml`) file for your cluster.

In the `install-config.yaml` file, locate the `platform` parameter.

* If the value of the `platform` parameter is `Baremetal` or `None`, you can disable the `CloudControllerManager` capability on your cluster.

* If the value of the `platform` parameter is `External`, locate the `platform.external.cloudControllerManager` parameter.
If the value of the `platform.external.cloudControllerManager` parameter is `None`, you can disable the `CloudControllerManager` capability on your cluster.

[IMPORTANT]
====
If these parameters contain any other values than those listed, you cannot disable the `CloudControllerManager` capability on your cluster.
====

[NOTE]
====
The status of this Operator is General Availability for {aws-first}, {gcp-first}, {ibm-cloud-name}, global {azure-full}, Microsoft Azure Stack Hub, Nutanix, {rh-openstack-first}, and {vmw-full}.

The Operator is available as a Technology Preview for {ibm-power-server-name}.
====

The Cloud Controller Manager Operator manages and updates the cloud controller managers deployed on top of OpenShift Container Platform. The Operator is based on the Kubebuilder framework and `controller-runtime` libraries. You can install the Cloud Controller Manager Operator by using the Cluster Version Operator (CVO).

The Cloud Controller Manager Operator includes the following components:

* Operator
* Cloud configuration observer

By default, the Operator exposes Prometheus metrics through the `metrics` service.

Project::

See "cluster-cloud-controller-manager-operator" in the _Additional resources_ section.

[role="_additional-resources"]
.Additional resources

* Technology Preview

* `cluster-cloud-controller-manager-operator`

// Cloud credential capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/modules/node-tuning-operator.adoc

[id="cloud-credential-operator_{context}"]

[role="_abstract"]
The Cloud Credential Operator provides features for the `CloudCredential` capability.

[NOTE]
====
Currently, disabling the `CloudCredential` capability is only supported for bare-metal clusters.
====

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

Project::

See "openshift-cloud-credential-operator" in the _Additional resources_ section.

CRDs::

* `credentialsrequests.cloudcredential.openshift.io`
** Scope: Namespaced
** CR: `CredentialsRequest`
** Validation: Yes

Configuration objects::

No configuration required.

[role="_additional-resources"]
.Additional resources

* About the Cloud Credential Operator
* `openshift-cloud-credential-operator`

// Cluster Image Registry capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

// operators/operator-reference.adoc

// installing/overview/cluster-capabilities.adoc

[id="cluster-image-registry-operator_{context}"]

The Cluster Image Registry Operator provides features for the `ImageRegistry` capability.

The Cluster Image Registry Operator manages a singleton instance of the {product-registry}. It manages all configuration of the registry, including creating storage.

On initial start up, the Operator creates a default `image-registry` resource instance based on the configuration detected in the cluster. This indicates what cloud storage type to use based on the cloud provider.

If insufficient information is available to define a complete `image-registry` resource, then an incomplete resource is defined and the Operator updates the resource status with information about what is missing.

The Cluster Image Registry Operator runs in the `openshift-image-registry` namespace and it also manages the registry instance in that location. All configuration and workload resources for the registry reside in that namespace.

In order to integrate the image registry into the cluster's user authentication and authorization system, an image pull secret is generated for each service account in the cluster.

[IMPORTANT]
====
If you disable the `ImageRegistry` capability or if you disable the integrated {product-registry} in the Cluster Image Registry Operator's configuration, the image pull secret is not generated for each service account.
====

If you disable the `ImageRegistry` capability, you can reduce the overall resource footprint of OpenShift Container Platform in Telco environments. Depending on your deployment, you can disable this component if you do not need it.

== Project

cluster-image-registry-operator

[role="_additional-resources"]
.Additional resources

* Image Registry Operator in OpenShift Container Platform
* Automatically generated secrets
* cluster-image-registry-operator

// Cluster storage capability
// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc
// *  installing/overview/cluster-capabilities.adoc

[id="cluster-storage-operator_{context}"]

[NOTE]
====
The Cluster Storage Operator is an optional cluster capability that can be disabled by cluster administrators during installation. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.
====

The Cluster Storage Operator provides the features for the `Storage` capability.

The Cluster Storage Operator sets OpenShift Container Platform cluster-wide storage defaults. It ensures a default `storageclass` exists for OpenShift Container Platform clusters. It also installs Container Storage Interface (CSI) drivers which enable your cluster to use various storage backends.

[IMPORTANT]
====
If the cluster storage capability is disabled, the cluster will not have a default `storageclass` or any CSI drivers. Users with administrator privileges can create a default `storageclass` and manually install CSI drivers if the cluster storage capability is disabled.
====

== Project

cluster-storage-operator

== Configuration

No configuration is required.

== Notes

* The storage class that the Operator creates can be made non-default by editing its annotation, but this storage class cannot be deleted as long as the Operator runs.

[role="_additional-resources"]
.Additional resources

* cluster-storage-operator

// Console capability
// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc
// *  installing/overview/cluster-capabilities.adoc

// operators/operator-reference.adoc

[id="console-operator_{context}"]

[NOTE]
====
The Console Operator is an optional cluster capability that can be disabled by cluster administrators during installation. If you disable the Console Operator at installation, your cluster is still supported and upgradable. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.
====

The Console Operator provides the features for the `Console` capability.

The Console Operator installs and maintains the OpenShift Container Platform web console on a cluster. The Console Operator is installed by default and automatically maintains a console.

== Project

console-operator

[role="_additional-resources"]
.Additional resources

* Web console overview
* console-operator

// CSI snapshot controller capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

[id="cluster-csi-snapshot-controller-operator_{context}"]

[role="_abstract"]
The Cluster CSI Snapshot Controller Operator is an optional cluster capability that can be disabled by cluster administrators during installation. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.

The Cluster CSI Snapshot Controller Operator provides the features for the `CSISnapshot` capability.

The Cluster CSI Snapshot Controller Operator installs and maintains the CSI Snapshot Controller. The CSI Snapshot Controller is responsible for watching the `VolumeSnapshot` CRD objects and manages the creation and deletion lifecycle of volume snapshots.

Project::
+
`cluster-csi-snapshot-controller-operator`

[role="_additional-resources"]
.Additional resources

* CSI volume snapshots
* cluster-csi-snapshot-controller-operator

// DeploymentConfig capability
// Module included in the following assemblies:
//
// *  installing/overview/cluster-capabilities.adoc

[id="deployment-config-capability_{context}"]
= DeploymentConfig capability

[role="_abstract"]
The `DeploymentConfig` capability enables and manages the `DeploymentConfig` API.

[IMPORTANT]
====
If you disable the `DeploymentConfig` capability, the following resources will not be available in the cluster:

* `DeploymentConfig` resources
* The `deployer` service account

Disable the `DeploymentConfig` capability only if you do not require `DeploymentConfig` resources and the `deployer` service account in the cluster.
====

// Ingress capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

[id="ingress-operator_{context}"]

[role="_abstract"]

The Ingress Operator provides the features for the `Ingress` capability.

The Ingress Operator configures and manages the OpenShift Container Platform router.

Project::
+
`openshift-ingress-operator`

CRDs::
+
* `clusteringresses.ingress.openshift.io`
** Scope: Namespaced
** CR: `clusteringresses`
** Validation: No

Configuration objects::
+
* Cluster config
** Type Name: `clusteringresses.ingress.openshift.io`
** Instance Name: `default`
** View Command:
+
[source,terminal]
----
$ oc get clusteringresses.ingress.openshift.io -n openshift-ingress-operator default -o yaml
----

Notes::
+
The Ingress Operator sets up the router in the `openshift-ingress` project and creates the deployment for the router:
+
[source,terminal]
----
$ oc get deployment -n openshift-ingress
----
+
The Ingress Operator uses the `clusterNetwork[].cidr` from the `network/cluster` status to determine what mode (IPv4, IPv6, or dual stack) the managed Ingress Controller (router) should operate in. For example, if `clusterNetwork` contains only a v6 `cidr`, then the Ingress Controller operates in IPv6-only mode.
+
In the following example, Ingress Controllers managed by the Ingress Operator will run in IPv4-only mode because only one cluster network exists and the network is an IPv4 `cidr`:
+
[source,terminal]
----
$ oc get network/cluster -o jsonpath='{.status.clusterNetwork[*]}'
----
+
.Example output
[source,terminal]
----
map[cidr:10.128.0.0/14 hostPrefix:23]
----

[role="_additional-resources"]
.Additional resources

* openshift-ingress-operator

// Insights capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

[id="insights-operator_{context}"]

[role="_abstract"]
The {insights-operator} is an optional cluster capability that can be disabled by cluster administrators during installation. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.

The {insights-operator} provides the features for the `Insights` capability.

The {insights-operator} gathers OpenShift Container Platform configuration data and sends it to Red{nbsp}Hat. The data is used to produce proactive insights recommendations about potential issues that a cluster might be exposed to. These insights are communicated to cluster administrators through the {red-hat-lightspeed} advisor service on console.redhat.com.

Project::
+
`insights-operator`

Configuration::
+
No configuration is required.

Notes::
+
{insights-operator} complements OpenShift Container Platform Telemetry.

[role="_additional-resources"]
.Additional resources

* Using {insights-operator}
* {hybrid-console}
* insights-operator

// Machine API capability
// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="machine-api-capability_{context}"]
= Machine API capability

[role="_abstract"]
The `machine-api-operator`, `cluster-autoscaler-operator`, and `cluster-control-plane-machine-set-operator` Operators provide the features for the `MachineAPI` capability. You can disable this capability only if you install a cluster with user-provisioned infrastructure.

The Machine API capability is responsible for all machine configuration and management in the cluster. If you disable the Machine API capability during installation, you need to manage all machine-related tasks manually.

[role="_additional-resources"]
.Additional resources

* Overview of machine management
* Machine API Operator
* Cluster Autoscaler Operator
* Control Plane Machine Set Operator

// Marketplace capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

// operators/operator-reference.adoc

// installing/overview/cluster-capabilities.adoc

[id="marketplace-operator_{context}"]

[role="_abstract"]
The Marketplace Operator is an optional cluster capability that can be disabled by cluster administrators if it is not needed. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.

The Marketplace Operator provides the features for the `marketplace` capability.

The Marketplace Operator simplifies the process for bringing off-cluster Operators to your cluster by using a set of default Operator Lifecycle Manager (OLM) catalogs on the cluster. When the Marketplace Operator is installed, it creates the `openshift-marketplace` namespace. OLM ensures catalog sources installed in the `openshift-marketplace` namespace are available for all namespaces on the cluster.

If you disable the `marketplace` capability, the Marketplace Operator does not create the `openshift-marketplace` namespace. Catalog sources can still be configured and managed on the cluster manually, but OLM depends on the `openshift-marketplace` namespace in order to make catalogs available to all namespaces on the cluster. Users with elevated permissions to create namespaces prefixed with `openshift-`, such as system or cluster administrators, can manually create the `openshift-marketplace` namespace.

If you enable the `marketplace` capability, you can enable and disable individual catalogs by configuring the Marketplace Operator.

Project::
+
`operator-marketplace`

[role="_additional-resources"]
.Additional resources

* Red Hat-provided Operator catalogs
* operator-marketplace

// Node Tuning capability
// Module included in the following assemblies:
//
// * scalability_and_performance/using-node-tuning-operator.adoc
// * operators/operator-reference.adoc
// * post_installation_configuration/node-tasks.adoc
// * nodes/nodes/nodes-node-tuning-operator.adoc

[id="about-node-tuning-operator_{context}"]
= Node Tuning Operator

= About the Node Tuning Operator

[role="_abstract"]
The Node Tuning Operator provides features for the `NodeTuning` capability.

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs.

If you disable the NodeTuning capability, some default tuning settings will not be applied to the control-plane nodes. This might limit the scalability and performance of large clusters with over 900 nodes or 900 routes.

The Operator manages the containerized TuneD daemon for OpenShift Container Platform as a Kubernetes daemon set. It ensures the custom tuning specification is passed to all containerized TuneD daemons running in the cluster in the format that the daemons understand. The daemons run on all nodes in the cluster, one per node.

Node-level settings applied by the containerized TuneD daemon are rolled back on an event that triggers a profile change or when the containerized TuneD daemon is terminated gracefully by receiving and handling a termination signal.

The Node Tuning Operator uses the Performance Profile controller to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications.

The cluster administrator configures a performance profile to define node-level settings such as the following:

* Updating the kernel to kernel-rt.
* Choosing CPUs for housekeeping.
* Choosing CPUs for running workloads.

The Node Tuning Operator is part of a standard OpenShift Container Platform installation in version 4.1 and later.

[NOTE]
====
In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.
====

Project::
+
`cluster-node-tuning-operator`

[role="_additional-resources"]
.Additional resources

* Using the Node Tuning Operator
* cluster-node-tuning-operator

// OpenShift samples capability
// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc
// *  installing/overview/cluster-capabilities.adoc

// operators/operator-reference.adoc

// installing/overview/cluster-capabilities.adoc

[id="cluster-samples-operator_{context}"]

[role="_abstract"]
The Cluster Samples Operator is an optional cluster capability that can be disabled by cluster administrators during installation. For more information about optional cluster capabilities, see "Cluster capabilities" in _Installing_.

The Cluster Samples Operator provides the features for the `openshift-samples` capability.

The Cluster Samples Operator manages the sample image streams and templates stored in the `openshift` namespace.

On initial start up, the Operator creates the default samples configuration resource to initiate the creation of the image streams and templates. The configuration object is a cluster scoped object with the key `cluster` and type `configs.samples`.

The image streams are the {op-system-first}-based OpenShift Container Platform image streams pointing to images on `registry.redhat.io`. Similarly, the templates are those categorized as OpenShift Container Platform templates.

If you disable the samples capability, users cannot access the image streams, samples, and templates it provides. Depending on your deployment, you might want to disable this component if you do not need it.

The Cluster Samples Operator deployment is contained within the `openshift-cluster-samples-operator` namespace. On start up, the install pull secret is used by the image stream import logic in the {product-registry} and API server to authenticate with `registry.redhat.io`. An administrator can create any additional secrets in the `openshift` namespace if they change the registry used for the sample image streams. If created, those secrets contain the content of a `config.json` for `docker` needed to facilitate image import.

The image for the Cluster Samples Operator contains image stream and template definitions for the associated OpenShift Container Platform release. After the Cluster Samples Operator creates a sample, it adds an annotation that denotes the OpenShift Container Platform version that it is compatible with. The Operator uses this annotation to ensure that each sample matches the compatible release version. Samples outside of its inventory are ignored, as are skipped samples.

Modifications to any samples that are managed by the Operator are allowed as long as the version annotation is not modified or deleted. However, on an upgrade, as the version annotation will change, those modifications can get replaced as the sample will be updated with the newer version. The Jenkins images are part of the image payload from the installation and are tagged into the image streams directly.

The samples resource includes a finalizer, which cleans up the following upon its deletion:

* Operator-managed image streams
* Operator-managed templates
* Operator-generated configuration resources
* Cluster status resources

Upon deletion of the samples resource, the Cluster Samples Operator recreates the resource using the default configuration.

Project::
+
`cluster-samples-operator`

[role="_additional-resources"]
.Additional resources

* Configuring the Cluster Samples Operator
* cluster-samples-operator

// OperatorLifecycleManager capability
// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/operator-reference.adoc

[id="olm-overview_{context}"]
= What is {olmv0-first}?

= {olmv0-first} capability

{olmv0} provides the features for the `OperatorLifecycleManager` capability.

{olmv0-first} helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. It is part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way.

.{olmv0} workflow
image::olm-workflow.png[]

OLM runs by default in OpenShift Container Platform , which aids cluster administrators
OLM runs by default in OpenShift Container Platform, which aids administrators with the `dedicated-admin` role
in installing, upgrading, and granting access to Operators running on their cluster. The OpenShift Container Platform web console provides management screens for
cluster administrators
`dedicated-admin` administrators
to install Operators, as well as grant specific projects access to use the catalog of Operators available on the cluster.

For developers, a self-service experience allows provisioning and configuring instances of databases, monitoring, and big data services without having to be subject matter experts, because the Operator has that knowledge baked into it.

If an Operator requires any of the following APIs, then you must enable the `OperatorLifecycleManager` capability:

* `ClusterServiceVersion`
* `CatalogSource`
* `Subscription`
* `InstallPlan`
* `OperatorGroup`

[IMPORTANT]
====
The `marketplace` capability depends on the `OperatorLifecycleManager` capability. You cannot disable the `OperatorLifecycleManager` capability and enable the `marketplace` capability.
====

[role="_additional-resources"]
.Additional resources

* Operator Lifecycle Manager concepts and resources

// Operator Lifecycle Manager v1 capability
// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
// * installing/overview/cluster-capabilities.adoc

[id="cluster-operators-ref-olmv1_{context}"]
= {olmv1-first} Operator

= {olmv1-first} capability

{olmv1} provides the features for the `OperatorLifecycleManagerV1` capability.

Starting in OpenShift Container Platform 4.18, {olmv1} is enabled by default alongside {olmv0}. This next-generation iteration provides an updated framework that evolves many of {olmv0} concepts that enable cluster administrators to extend capabilities for their users.

{olmv1} manages the lifecycle of the new `ClusterExtension` object, which includes Operators via the `registry+v1` bundle format, and controls installation, upgrade, and role-based access control (RBAC) of extensions within a cluster.

In OpenShift Container Platform, {olmv1} is provided by the `olm` cluster Operator.

[NOTE]
====
The `olm` cluster Operator informs cluster administrators if there are any installed extensions blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Compatibility with OpenShift Container Platform versions".
====

== Components

{olmv1-first} comprises the following component projects:

Operator Controller:: The central component of {olmv1} that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from catalogd.

Catalogd:: A Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the {olmv1} microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content.

== CRDs

* `clusterextension.olm.operatorframework.io`
** Scope: Cluster
** CR: `ClusterExtension`

* `clustercatalog.olm.operatorframework.io`
** Scope: Cluster
** CR: `ClusterCatalog`

== Project

* operator-framework/operator-controller
* operator-framework/catalogd

[role="_additional-resources"]
.Additional resources

* Extensions overview

// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="viewing-cluster-capabilities_{context}"]
= Viewing the cluster capabilities

As a cluster administrator, you can view the capabilities by using the `clusterversion` resource status.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* To view the status of the cluster capabilities, run the following command:
+
[source,terminal]
----
$ oc get clusterversion version -o jsonpath='{.spec.capabilities}{"\n"}{.status.capabilities}{"\n"}'
----
+
.Example output
[source,terminal]
----
{"additionalEnabledCapabilities":["openshift-samples"],"baselineCapabilitySet":"None"}
{"enabledCapabilities":["openshift-samples"],"knownCapabilities":["CSISnapshot","Console","Insights","Storage","baremetal","marketplace","openshift-samples"]}
----

// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="enabling-baseline-capability-set_{context}"]
= Enabling the cluster capabilities by setting baseline capability set

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `baselineCapabilitySet` configuration parameter.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* To set the `baselineCapabilitySet` configuration parameter, run the following command:
+
[source,terminal]
----
$ oc patch clusterversion version --type merge -p '{"spec":{"capabilities":{"baselineCapabilitySet":"vCurrent"}}}' <1>
----
<1> For `baselineCapabilitySet` you can specify `vCurrent`, `v`, or `None`.

// Module included in the following assemblies:
//
// * installing/overview/cluster-capabilities.adoc

[id="enabling-additional-enabled-capabilities_{context}"]
= Enabling the cluster capabilities by setting additional enabled capabilities

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `additionalEnabledCapabilities` configuration parameter.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. View the additional enabled capabilities by running the following command:
+
[source,terminal]
----
$ oc get clusterversion version -o jsonpath='{.spec.capabilities.additionalEnabledCapabilities}{"\n"}'
----
+
.Example output
[source,terminal]
----
["openshift-samples"]
----

. To set the `additionalEnabledCapabilities` configuration parameter, run the following command:
+
[source,terminal]
----
$ oc patch clusterversion/version --type merge -p '{"spec":{"capabilities":{"additionalEnabledCapabilities":["openshift-samples", "marketplace"]}}}'
----

[IMPORTANT]
====
It is not possible to disable a capability which is already enabled in a cluster. The cluster version Operator (CVO) continues to reconcile the capability which is already enabled in the cluster.
====

If you try to disable a capability, then CVO shows the divergent spec:
[source,terminal]
----
$ oc get clusterversion version -o jsonpath='{.status.conditions[?(@.type=="ImplicitlyEnabledCapabilities")]}{"\n"}'
----

.Example output
[source,terminal]
----
{"lastTransitionTime":"2022-07-22T03:14:35Z","message":"The following capabilities could not be disabled: openshift-samples","reason":"CapabilitiesImplicitlyEnabled","status":"True","type":"ImplicitlyEnabledCapabilities"}
----

[NOTE]
====
During the cluster upgrades, it is possible that a given capability could be implicitly enabled. If a resource was already running on the cluster before the upgrade, then any capabilities that is part of the resource will be enabled. For example, during a cluster upgrade, a resource that is already running on the cluster has been changed to be part of the `marketplace` capability by the system. Even if a cluster administrator does not explicitly enabled the `marketplace` capability, it is implicitly enabled by the system.
====
