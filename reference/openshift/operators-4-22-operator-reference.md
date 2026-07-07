---
title: "Cluster Operators reference"
type: reference
domain: openshift
slug: operators-4-22-operator-reference
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/operator-reference
version: 4.22
family: operators
documentKind: "Documentation"
---

# Cluster Operators reference

[id="operator-reference"]
= Cluster Operators reference

This reference guide indexes the _cluster Operators_ shipped by Red Hat that serve as the architectural foundation for OpenShift Container Platform. Cluster Operators are installed by default, unless otherwise noted, and are managed by the Cluster Version Operator (CVO). For more details on the control plane architecture, see Operators in OpenShift Container Platform.

Cluster administrators can view cluster Operators in the OpenShift Container Platform web console from the *Administration* -> *Cluster Settings* page.

[NOTE]
====
Cluster Operators are not managed by Operator Lifecycle Manager (OLM) and the software catalog. OLM and the software catalog are part of the Operator Framework used in OpenShift Container Platform for installing and running optional add-on Operators.
====

Some of the following cluster Operators can be disabled prior to installation. For more information see cluster capabilities.

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
* Bare-metal capability

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

[id="additional-resources_cluster-op-ref-cco"]
=== Additional resources
* About the Cloud Credential Operator
* `CredentialsRequest` custom resource

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-authentication-operator_{context}"]
= Cluster Authentication Operator

The Cluster Authentication Operator installs and maintains the `Authentication` custom resource in a cluster and can be viewed with:

[source,terminal]
----
$ oc get clusteroperator authentication -o yaml
----

== Project

cluster-authentication-operator

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-autoscaler-operator_{context}"]
= Cluster Autoscaler Operator

The Cluster Autoscaler Operator manages deployments of the OpenShift Cluster Autoscaler using the `cluster-api` provider.

== Project

cluster-autoscaler-operator

== CRDs

* `ClusterAutoscaler`: This is a singleton resource, which controls the configuration autoscaler instance for the cluster. The Operator only responds to the `ClusterAutoscaler` resource named `default` in the managed namespace, the value of the `WATCH_NAMESPACE` environment variable.
* `MachineAutoscaler`: This resource targets a node group and manages the annotations to enable and configure autoscaling for that group, the `min` and `max` size. Currently only `MachineSet` objects can be targeted.

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

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-capi-operator_{context}"]
= {cluster-capi-operator}

The {cluster-capi-operator} maintains the lifecycle of Cluster API resources. This Operator is responsible for all administrative tasks related to deploying the Cluster API project within an OpenShift Container Platform cluster.

[NOTE]
====
This Operator is available as a Technology Preview for {aws-first}, {gcp-first}, {azure-first}, {rh-openstack-first}, and {vmw-first} clusters.
====

== Project

cluster-capi-operator

== CRDs

* `awsmachines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `awsmachine`

*  `gcpmachines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `gcpmachine`

*  `azuremachines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `azuremachine`

*  `openstackmachines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `openstackmachine`

*  `vspheremachines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `vspheremachine`

*  `metal3machines.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `metal3machine`

* `awsmachinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `awsmachinetemplate`

*  `gcpmachinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `gcpmachinetemplate`

*  `azuremachinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `azuremachinetemplate`

*  `openstackmachinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `openstackmachinetemplate`

*  `vspheremachinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `vspheremachinetemplate`

*  `metal3machinetemplates.infrastructure.cluster.x-k8s.io`
** Scope: Namespaced
** CR: `metal3machinetemplate`

// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

[id="cluster-config-operator_{context}"]
= Cluster Config Operator

The Cluster Config Operator performs the following tasks related to `config.openshift.io`:

* Creates CRDs.
* Renders the initial custom resources.
* Handles migrations.

== Project

cluster-config-operator

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
* CSI snapshot controller capability

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

// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

[id="cluster-machine-approver-operator_{context}"]
= Cluster Machine Approver Operator

The Cluster Machine Approver Operator automatically approves the CSRs requested for a new worker node after cluster installation.

[NOTE]
====
For the control plane node, the `approve-csr` service on the bootstrap node automatically approves all CSRs during the cluster bootstrapping phase.
====

== Project

cluster-machine-approver-operator

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-monitoring-operator_{context}"]
= {cmo-full}

The {cmo-first} manages and updates the Prometheus-based cluster monitoring stack deployed on top of OpenShift Container Platform.

[discrete]
== Project

openshift-monitoring

[discrete]
== CRDs

* `alertmanagers.monitoring.coreos.com`
** Scope: Namespaced
** CR: `alertmanager`
** Validation: Yes
* `prometheuses.monitoring.coreos.com`
** Scope: Namespaced
** CR: `prometheus`
** Validation: Yes
* `prometheusrules.monitoring.coreos.com`
** Scope: Namespaced
** CR: `prometheusrule`
** Validation: Yes
* `servicemonitors.monitoring.coreos.com`
** Scope: Namespaced
** CR: `servicemonitor`
** Validation: Yes

[discrete]
== Configuration objects

[source,terminal]
----
$ oc -n openshift-monitoring edit cm cluster-monitoring-config
----

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-network-operator_{context}"]
= Cluster Network Operator

The Cluster Network Operator installs and upgrades the networking components on an OpenShift Container Platform cluster.

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

* OpenShift samples capability

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
* Storage capability

// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

[id="cluster-version-operator_{context}"]
= Cluster Version Operator

Cluster Operators manage specific areas of cluster functionality. The Cluster Version Operator (CVO) manages the lifecycle of cluster Operators, many of which are installed in OpenShift Container Platform by default.

The CVO also checks with the OpenShift Update Service to see the valid updates and update paths based on current component versions and information in the graph by collecting the status of both the cluster version and its cluster Operators. This status includes the condition type, which informs you of the health and current state of the OpenShift Container Platform cluster.

For more information regarding cluster version condition types, see "Understanding cluster version condition types".

== Project

cluster-version-operator

[role="_additional-resources"]
.Additional resources
* Understanding cluster version condition types

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
* Web console capability

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="control-plane-machine-set-operator_{context}"]
= Control Plane Machine Set Operator

The Control Plane Machine Set Operator automates the management of control plane machine resources within an OpenShift Container Platform cluster.

[NOTE]
====
This Operator is available for Amazon Web Services (AWS), {gcp-first}, Microsoft Azure, Nutanix, and VMware vSphere.
====

== Project

cluster-control-plane-machine-set-operator

== CRDs

* `controlplanemachineset.machine.openshift.io`
** Scope: Namespaced
** CR: `ControlPlaneMachineSet`
** Validation: Yes

[role="_additional-resources"]

[id="additional-resources_cluster-op-ref-cpmso"]
=== Additional resources

* About control plane machine sets
* `ControlPlaneMachineSet` custom resource

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="dns-operator_{context}"]
= DNS Operator

The DNS Operator deploys and manages CoreDNS to provide a name resolution service to pods that enables DNS-based Kubernetes Service discovery in OpenShift Container Platform.

The Operator creates a working default deployment based on the cluster's configuration.

* The default cluster domain is `cluster.local`.
* Configuration of the CoreDNS Corefile or Kubernetes plugin is not yet supported.

The DNS Operator manages CoreDNS as a Kubernetes daemon set exposed as a service with a static IP. CoreDNS runs on all nodes in the cluster.

== Project

cluster-dns-operator

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="etcd-cluster-operator_{context}"]
= etcd cluster Operator

The etcd cluster Operator automates etcd cluster scaling, enables etcd monitoring and metrics, and simplifies disaster recovery procedures.

== Project

cluster-etcd-operator

== CRDs

* `etcds.operator.openshift.io`
** Scope: Cluster
** CR: `etcd`
** Validation: Yes

== Configuration objects

[source,terminal]
----
$ oc edit etcd cluster
----

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
* Insights capability
* About remote health monitoring

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="kube-apiserver-operator_{context}"]
= Kubernetes API Server Operator

The Kubernetes API Server Operator manages and updates the Kubernetes API server deployed on top of OpenShift Container Platform. The Operator is based on the OpenShift Container Platform `library-go` framework and it is installed using the Cluster Version Operator (CVO).

== Project

openshift-kube-apiserver-operator

== CRDs

* `kubeapiservers.operator.openshift.io`
** Scope: Cluster
** CR: `kubeapiserver`
** Validation: Yes

== Configuration objects

[source,terminal]
----
$ oc edit kubeapiserver
----

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="kube-controller-manager-operator_{context}"]
= Kubernetes Controller Manager Operator

The Kubernetes Controller Manager Operator manages and updates the Kubernetes Controller Manager deployed on top of OpenShift Container Platform. The Operator is based on OpenShift Container Platform `library-go` framework and it is installed via the Cluster Version Operator (CVO).

It contains the following components:

* Operator
* Bootstrap manifest renderer
* Installer based on static pods
* Configuration observer

By default, the Operator exposes Prometheus metrics through the `metrics` service.

== Project

cluster-kube-controller-manager-operator

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-kube-scheduler-operator_{context}"]
= Kubernetes Scheduler Operator

The Kubernetes Scheduler Operator manages and updates the Kubernetes Scheduler deployed on top of OpenShift Container Platform. The Operator is based on the OpenShift Container Platform `library-go` framework and it is installed with the Cluster Version Operator (CVO).

The Kubernetes Scheduler Operator contains the following components:

* Operator
* Bootstrap manifest renderer
* Installer based on static pods
* Configuration observer

By default, the Operator exposes Prometheus metrics through the metrics service.

== Project

cluster-kube-scheduler-operator

== Configuration

The configuration for the Kubernetes Scheduler is the result of merging:

* a default configuration.
* an observed configuration from the spec `schedulers.config.openshift.io`.

All of these are sparse configurations, invalidated JSON snippets which are merged to form a valid configuration at the end.

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-kube-storage-version-migrator-operator_{context}"]
= Kubernetes Storage Version Migrator Operator

The Kubernetes Storage Version Migrator Operator detects changes of the default storage version, creates migration requests for resource types when the storage version changes, and processes migration requests.

== Project

cluster-kube-storage-version-migrator-operator

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="machine-api-operator_{context}"]
= Machine API Operator

The Machine API Operator manages the lifecycle of specific purpose custom resource definitions (CRD), controllers, and RBAC objects that extend the Kubernetes API. This declares the desired state of machines in a cluster.

== Project

machine-api-operator

== CRDs

* `MachineSet`
* `Machine`
* `MachineHealthCheck`

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="machine-config-operator_{context}"]
= Machine Config Operator

The Machine Config Operator manages and applies configuration and updates of the base operating system and container runtime, including everything between the kernel and kubelet.

There are four components:

* `machine-config-server`: Provides Ignition configuration to new machines joining the cluster.
* `machine-config-controller`: Coordinates the upgrade of machines to the desired configurations defined by a `MachineConfig` object. Options are provided to control the upgrade for sets of machines individually.
* `machine-config-daemon`: Applies new machine configuration during update. Validates and verifies the state of the machine to the requested machine configuration.
* `machine-config`: Provides a complete source of machine configuration at installation, first start up, and updates for a machine.

== Project

openshift-machine-config-operator

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
* Marketplace capability

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
[id="cluster-operators-ref-nto-addtl-resources"]
=== Additional resources
* About low latency

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="openshift-apiserver-operator_{context}"]
= OpenShift API Server Operator

The OpenShift API Server Operator installs and maintains the `openshift-apiserver` on a cluster.

== Project

openshift-apiserver-operator

== CRDs

* `openshiftapiservers.operator.openshift.io`
** Scope: Cluster
** CR: `openshiftapiserver`
** Validation: Yes

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cluster-openshift-controller-manager-operator_{context}"]
= OpenShift Controller Manager Operator

The OpenShift Controller Manager Operator installs and maintains the `OpenShiftControllerManager` custom resource in a cluster and can be viewed with:

[source,terminal]
----
$ oc get clusteroperator openshift-controller-manager -o yaml
----

The custom resource definition (CRD) `openshiftcontrollermanagers.operator.openshift.io` can be viewed in a cluster with:

[source,terminal]
----
$ oc get crd openshiftcontrollermanagers.operator.openshift.io -o yaml
----

== Project

cluster-openshift-controller-manager-operator

[id="cluster-operators-ref-olm"]
== {olmv0-first} Operators

[NOTE]
====
The following sections pertain to {olmv0-first} that has been included with OpenShift Container Platform 4 since its initial release. For {olmv1}, see {olmv1-first} Operators.
====

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

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-olm-operator_{context}"]
= OLM Operator

The OLM Operator is responsible for deploying applications defined by CSV resources after the required resources specified in the CSV are present in the cluster.

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application.

The OLM Operator uses the following workflow:

. Watch for cluster service versions (CSVs) in a namespace and check that requirements are met.
. If requirements are met, run the install strategy for the CSV.
+
[NOTE]
====
A CSV must be an active member of an Operator group for the install strategy to run.
====

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-operator_{context}"]
= Catalog Operator

The Catalog Operator is responsible for resolving and installing cluster service versions (CSVs) and the required resources they specify. It is also responsible for watching catalog sources for updates to packages in channels and upgrading them, automatically if desired, to the latest available versions.

To track a package in a channel, you can create a `Subscription` object configuring the desired package, channel, and the `CatalogSource` object you want to use for pulling updates. When updates are found, an appropriate `InstallPlan` object is written into the namespace on behalf of the user.

The Catalog Operator uses the following workflow:

. Connect to each catalog source in the cluster.
. Watch for unresolved install plans created by a user, and if found:
.. Find the CSV matching the name requested and add the CSV as a resolved resource.
.. For each managed or required CRD, add the CRD as a resolved resource.
.. For each required CRD, find the CSV that manages it.
. Watch for resolved install plans and create all of the discovered resources for it, if approved by a user or automatically.
. Watch for catalog sources and subscriptions and create install plans based on them.

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-arch.adoc
// * operators/operator-reference.adoc

[id="olm-arch-catalog-registry_{context}"]
= Catalog Registry

The Catalog Registry stores CSVs and CRDs for creation in a cluster and stores metadata about packages and channels.

A _package manifest_ is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version.

// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/operator-reference.adoc

[id="olm-architecture_{context}"]
= Component responsibilities

= CRDs

Operator Lifecycle Manager (OLM) is composed of two Operators: the OLM Operator and the Catalog Operator.

The OLM and Catalog Operators are responsible for managing the custom resource definitions (CRDs) that are the basis for the OLM framework:

.CRDs managed by OLM and Catalog Operators
[cols="2a,1a,1a,8a",options="header"]
|===
|Resource |Short name |Owner |Description

|`ClusterServiceVersion` (CSV)
|`csv`
|OLM
|Application metadata: name, version, icon, required resources, installation, and so on.

|`InstallPlan`
|`ip`
|Catalog
|Calculated list of resources to be created to automatically install or upgrade a CSV.

|`CatalogSource`
|`catsrc`
|Catalog
|A repository of CSVs, CRDs, and packages that define an application.

|`Subscription`
|`sub`
|Catalog
|Used to keep CSVs up to date by tracking a channel in a package.

|`OperatorGroup`
|`og`
|OLM
|Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.
|===

Each of these Operators is also responsible for creating the following resources:

.Resources created by OLM and Catalog Operators
[options="header"]
|===
|Resource |Owner

|`Deployments`
.4+.^|OLM

|`ServiceAccounts`
|`(Cluster)Roles`
|`(Cluster)RoleBindings`

|`CustomResourceDefinitions` (CRDs)
.2+.^|Catalog
|`ClusterServiceVersions`
|===

=== Cluster Operators

In OpenShift Container Platform, OLM functionality is provided across a set of cluster Operators:

`operator-lifecycle-manager`:: Provides the OLM Operator. Also informs cluster administrators if there are any installed Operators blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Controlling Operator compatibility with OpenShift Container Platform versions".
`operator-lifecycle-manager-catalog`:: Provides the Catalog Operator.
`operator-lifecycle-manager-packageserver`:: Represents an API extension server responsible for collecting metadata from all catalogs on the cluster and serves the user-facing `PackageManifest` API.

[role="_additional-resources"]

[id="cluster-operators-ref-olm-addtl-resources"]
=== Additional resources
* Understanding Operator Lifecycle Manager (OLM)

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

[id="cluster-operators-ref-olmv1-addtl-resources"]
=== Additional resources
* Extensions overview
* Compatibility with OpenShift Container Platform versions

// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="openshift-service-ca-operator_{context}"]
= OpenShift Service CA Operator

The OpenShift Service CA Operator mints and manages serving certificates for Kubernetes services.

== Project

openshift-service-ca-operator

// Module included in the following assemblies:
//
// *  operators/operator-reference.adoc

[id="vsphere-problem-detector-operator_{context}"]
= {operator-name}

The {operator-name} checks clusters that are deployed on vSphere for common installation and misconfiguration issues that are related to storage.

[NOTE]
====
The {operator-name} is only started by the Cluster Storage Operator when the Cluster Storage Operator detects that the cluster is deployed on vSphere.
====

== Configuration

No configuration is required.

== Notes

* The Operator supports OpenShift Container Platform installations on vSphere.
* The Operator uses the `vsphere-cloud-credentials` to communicate with vSphere.
* The Operator performs checks that are related to storage.

// Clear temporary attributes

[role="_additional-resources"]
.Additional resources
* Using the vSphere Problem Detector Operator
