---
title: "{hcp-capital} overview"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/index
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# {hcp-capital} overview

[id="hcp-overview"]
= {hcp-capital} overview

You can deploy OpenShift Container Platform clusters by using two different control plane configurations: standalone or {hcp}. The standalone configuration uses dedicated virtual machines or physical machines to host the control plane. With {hcp} for OpenShift Container Platform, you create control planes as pods on a management cluster without the need for dedicated virtual or physical machines for each control plane.

// Module included in the following assemblies:
//
// * architecture/control-plane.adoc
// * hosted-control-planes/index.adoc

[id="hosted-control-planes-overview_{context}"]
= Introduction to {hcp}

{hcp-capital} is available by using a supported version of {mce} on the following platforms:

* Bare metal by using the Agent provider
* Non-bare-metal Agent machines, as a Technology Preview feature
* {VirtProductName}
* {aws-first}
* {ibm-z-title}
* {ibm-power-title}
* {rh-openstack-first} 17.1, as a Technology Preview feature

The {hcp} feature is enabled by default.

[NOTE]
====
The {mce-short} is an integral part of {rh-rhacm-first} and is enabled by default with {rh-rhacm}. However, you do not need {rh-rhacm} in order to use {hcp}.
====

[id="hosted-control-planes-architecture_{context}"]
== Architecture of {hcp}

OpenShift Container Platform is often deployed in a coupled, or standalone, model, where a cluster consists of a control plane and a data plane. The control plane includes an API endpoint, a storage endpoint, a workload scheduler, and an actuator that ensures state. The data plane includes compute, storage, and networking where workloads and applications run.

The standalone control plane is hosted by a dedicated group of nodes, which can be physical or virtual, with a minimum number to ensure quorum. The network stack is shared. Administrator access to a cluster offers visibility into the cluster's control plane, machine management APIs, and other components that contribute to the state of a cluster.

Although the standalone model works well, some situations require an architecture where the control plane and data plane are decoupled. In those cases, the data plane is on a separate network domain with a dedicated physical hosting environment. The control plane is hosted by using high-level primitives such as deployments and stateful sets that are native to Kubernetes. The control plane is treated as any other workload.

image::hosted-control-planes-diagram.png[Diagram that compares the hosted control plane model against OpenShift with a coupled control plane and workers]

[id="hosted-control-planes-benefits_{context}"]
== Benefits of {hcp}

With {hcp}, you can pave the way for a true hybrid-cloud approach and enjoy several other benefits.

* The security boundaries between management and workloads are stronger because the control plane is decoupled and hosted on a dedicated hosting service cluster. As a result, you are less likely to leak credentials for clusters to other users. Because infrastructure secret account management is also decoupled, cluster infrastructure administrators cannot accidentally delete control plane infrastructure.

* With {hcp}, you can run many control planes on fewer nodes. As a result, clusters are more affordable.

* Because the control planes consist of pods that are launched on OpenShift Container Platform, control planes start quickly. The same principles apply to control planes and workloads, such as monitoring, logging, and auto-scaling.

* From an infrastructure perspective, you can push registries, HAProxy, cluster monitoring, storage nodes, and other infrastructure components to the tenant's cloud provider account, isolating usage to the tenant.

* From an operational perspective, multicluster management is more centralized, which results in fewer external factors that affect the cluster status and consistency. Site reliability engineers have a central place to debug issues and navigate to the cluster data plane, which can lead to shorter Time to Resolution (TTR) and greater productivity.

// Module included in the following assemblies:
//
// * hosted_control_planes/index.adoc

[id="hcp-ocp-differences_{context}"]
= Differences between {hcp} and OpenShift Container Platform

{hcp-capital} is a form factor of OpenShift Container Platform. Hosted clusters and the stand-alone OpenShift Container Platform clusters are configured and managed differently. See the following tables to understand the differences between OpenShift Container Platform and {hcp}:

[id="cluster-creation_{context}"]
== Cluster creation and lifecycle

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|You install a standalone OpenShift Container Platform cluster by using the `openshift-install` binary or the Assisted Installer.
|You install a hosted cluster by using the `hypershift.openshift.io` API resources such as `HostedCluster` and `NodePool`, on an existing OpenShift Container Platform cluster.

|===

[id="cluster-configuration_{context}"]
== Cluster configuration

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|You configure cluster-scoped resources such as authentication, API server, and proxy by using the `config.openshift.io` API group.
|You configure resources that impact the control plane in the `HostedCluster` resource.

|===

[id="etcd-encryption_{context}"]
== etcd encryption

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|You configure etcd encryption by using the `APIServer` resource with AES-GCM or AES-CBC. For more information, see "Enabling etcd encryption".
|You configure etcd encryption by using the `HostedCluster` resource in the `SecretEncryption` field with AES-CBC or KMS for {aws-full}.

|===

[id="operators-and-control-plane_{context}"]
== Operators and control plane

[cols="2a,4a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|A standalone OpenShift Container Platform cluster contains separate Operators for each control plane component.
|A hosted cluster contains a single Operator named Control Plane Operator that runs in the hosted control plane namespace on the management cluster.

|etcd uses storage that is mounted on the control plane nodes. The etcd cluster Operator manages etcd.
|etcd uses a persistent volume claim for storage and is managed by the Control Plane Operator.

|The Ingress Operator, network related Operators, and {olm-first} run on the cluster.
|The Ingress Operator, network related Operators, and {olm-first} run in the hosted control plane namespace on the management cluster.

|The OAuth server runs inside the cluster and is exposed through a route in the cluster.
|The OAuth server runs inside the control plane and is exposed through a route, node port, or load balancer on the management cluster.

|===

[id="upgrades_{context}"]
== Updates

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|The Cluster Version Operator (CVO) orchestrates the update process and monitors the `ClusterVersion` resource. Administrators and OpenShift components can interact with the CVO through the `ClusterVersion` resource. The `oc adm upgrade` command results in a change to the `ClusterVersion.Spec.DesiredUpdate` field in the `ClusterVersion` resource.
|The {hcp} update results in a change to the `.spec.release.image` field in the `HostedCluster` and `NodePool` resources. Any changes to the `ClusterVersion` resource are ignored.

|After you update an OpenShift Container Platform cluster, both the control plane and compute machines are updated.
|After you update the hosted cluster, only the control plane is updated. You perform node pool updates separately.

|===

[id="machine-config-manage_{context}"]
== Machine configuration and management

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|The `MachineSets` resource manages machines in the `openshift-machine-api` namespace.
|The `NodePool` resource manages machines on the management cluster.

|A set of control plane machines are available.
|A set of control plane machines do not exist.

|You enable a machine health check by using the `MachineHealthCheck` resource.
|You enable a machine health check through the `.spec.management.autoRepair` field in the `NodePool` resource.

|You enable autoscaling by using the `ClusterAutoscaler` and `MachineAutoscaler` resources.
|You enable autoscaling through the `spec.autoScaling` field in the `NodePool` resource.

|Machines and machine sets are exposed in the cluster.
|Machines, machine sets, and machine deployments from upstream {cluster-capi-operator} are used to manage machines but are not exposed to the user.

|All machine sets are upgraded automatically when you update the cluster.
|You update your node pools independently from the hosted cluster updates.

|Only an in-place upgrade is supported in the cluster.
|Both replace and in-place upgrades are supported in the hosted cluster.

|The Machine Config Operator manages configurations for machines.
|The Machine Config Operator does not exist in {hcp}.

|You configure machine Ignition by using the `MachineConfig`, `KubeletConfig`, and `ContainerRuntimeConfig` resources that are selected from a `MachineConfigPool` selector.
|You configure the `MachineConfig`, `KubeletConfig`, and `ContainerRuntimeConfig` resources through the config map referenced in the `spec.config` field of the `NodePool` resource.

|The Machine Config Daemon (MCD) manages configuration changes and updates on each of the nodes.
|For an in-place upgrade, the node pool controller creates a run-once pod that updates a machine based on your configuration.

|You can modify the machine configuration resources such as the SR-IOV Operator.
|You cannot modify the machine configuration resources.

|===

[id="netowrking_{context}"]
== Networking

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|The Kube API server communicates with nodes directly, because the Kube API server and nodes exist in the same Virtual Private Cloud (VPC).
|The Kube API server communicates with nodes through Konnectivity. The Kube API server and nodes exist in a different Virtual Private Cloud (VPC).

|Nodes communicate with the Kube API server through the internal load balancer.
|Nodes communicate with the Kube API server through an external load balancer or a node port.

|===

[id="web-console_{context}"]
== Web console

[cols="2a,2a",options="header"]
|===

|OpenShift Container Platform |{hcp-capital}

|The web console shows the status of a control plane.
|The web console does not show the status of a control plane.

|You can update your cluster by using the web console.
|You cannot update the hosted cluster by using the web console.

|The web console displays the infrastructure resources such as machines.
|The web console does not display the infrastructure resources.

|You can configure machines through the `MachineConfig` resource by using the web console.
|You cannot configure machines by using the web console.

|===

[role="_additional-resources"]
.Additional resources
* Enabling etcd encryption

// Module included in the following assemblies:
//
// * hosted_control_planes/index.adoc

[id="hcp-mce-acm-relationship-intro_{context}"]
= Relationship between {hcp}, {mce-short}, and {rh-rhacm}

You can configure {hcp} by using the {mce}. The {mce-short} cluster lifecycle defines the process of creating, importing, managing, and destroying Kubernetes clusters across various infrastructure cloud providers, private clouds, and on-premises data centers.

[NOTE]
====
The {mce-short} is an integral part of {rh-rhacm-first} and is enabled by default with {rh-rhacm}. However, you do not need {rh-rhacm} in order to use {hcp}.
====

The {mce-short} is the cluster lifecycle Operator that provides cluster management capabilities for OpenShift Container Platform and {rh-rhacm} hub clusters. The {mce-short} enhances cluster fleet management and supports OpenShift Container Platform cluster lifecycle management across clouds and data centers.

.Cluster life cycle and foundation
image::acm-mce-intro-diagram.png[Cluster life cycle and foundation]

You can use the {mce-short} with OpenShift Container Platform as a standalone cluster manager or as part of a {rh-rhacm} hub cluster.

[TIP]
====
A management cluster is also known as the hosting cluster.
====

You can deploy OpenShift Container Platform clusters by using two different control plane configurations: standalone or {hcp}. The standalone configuration uses dedicated virtual machines or physical machines to host the control plane. With {hcp} for OpenShift Container Platform, you create control planes as pods on a management cluster without the need for dedicated virtual or physical machines for each control plane.

.{rh-rhacm} and the {mce-short} introduction diagram
image::rhacm-flow.png[{rh-rhacm} and the {mce-short} introduction diagram]

// Module included in the following assemblies:
//
// * hosted_control_planes/index.adoc

[id="hcp-acm-discover_{context}"]
= Discovering {mce-short} hosted clusters in {rh-rhacm}

If you want to bring hosted clusters to a {rh-rhacm-first} hub cluster to manage them with {rh-rhacm} management components, see the instructions in the {rh-rhacm-title} official documentation.

// Module included in the following assemblies:
//
// * architecture/control-plane.adoc
// * hosted-control-planes/index.adoc

[id="hosted-control-planes-version-support_{context}"]
= Versioning for {hcp}

The {hcp} feature includes the following components, which might require independent versioning and support levels:

* Management cluster
* HyperShift Operator
* {hcp-capital} (`hcp`) command-line interface (CLI)
* `hypershift.openshift.io` API
* Control Plane Operator

[id="hcp-versioning-mgmt_{context}"]
== Management cluster

In management clusters for production use, you need {mce}, which is available through the software catalog. The {mce-short} bundles a supported build of the HyperShift Operator. For your management clusters to remain supported, you must use the version of OpenShift Container Platform that {mce-short} runs on. In general, a new release of {mce-short} runs on the following versions of OpenShift Container Platform:

* The latest General Availability version of OpenShift Container Platform
* Two versions before the latest General Availability version of OpenShift Container Platform

The full list of OpenShift Container Platform versions that you can install through the HyperShift Operator on a management cluster depends on the version of your HyperShift Operator. However, the list always includes at least the same OpenShift Container Platform version as the management cluster and two previous minor versions relative to the management cluster. For example, if the management cluster is running 4.17 and a supported version of {mce-short}, the HyperShift Operator can install 4.17, 4.16, 4.15, and 4.14 hosted clusters.

With each major, minor, or patch version release of OpenShift Container Platform, two components of {hcp} are released:

* The HyperShift Operator
* The `hcp` command-line interface (CLI)

[id="hcp-versioning-ho_{context}"]
== HyperShift Operator

The HyperShift Operator manages the lifecycle of hosted clusters that are represented by the `HostedCluster` API resources. The HyperShift Operator is released with each OpenShift Container Platform release. The HyperShift Operator creates the `supported-versions` config map in the `hypershift` namespace. The config map contains the supported hosted cluster versions.

You can host different versions of control planes on the same management cluster.

.Example `supported-versions` config map object
[source,yaml]
----
    apiVersion: v1
    data:
      supported-versions: '{"versions":["4.22"]}'
    kind: ConfigMap
    metadata:
      labels:
        hypershift.openshift.io/supported-versions: "true"
      name: supported-versions
      namespace: hypershift
----

[id="hcp-versioning-cli_{context}"]
== {hcp} CLI

You can use the `hcp` CLI to create hosted clusters. You can download the CLI from {mce-short}. When you run the `hcp version` command, the output shows the latest OpenShift Container Platform that the CLI supports against your `kubeconfig` file.

[id="hcp-versioning-api_{context}"]
== hypershift.openshift.io API

You can use the `hypershift.openshift.io` API resources, such as, `HostedCluster` and `NodePool`, to create and manage OpenShift Container Platform clusters at scale. A `HostedCluster` resource contains the control plane and common data plane configuration. When you create a `HostedCluster` resource, you have a fully functional control plane with no attached nodes. A `NodePool` resource is a scalable set of worker nodes that is attached to a `HostedCluster` resource.

The API version policy generally aligns with the policy for Kubernetes API versioning.

Updates for {hcp} involve updating the hosted cluster and the node pools. For more information, see "Updates for {hcp}".

[id="hcp-versioning-cpo_{context}"]
== Control Plane Operator

The Control Plane Operator is released as part of each OpenShift Container Platform payload release image for the following architectures:

* amd64
* arm64
* multi-arch

[role="_additional-resources"]
.Additional resources
* AMD64 release images
* ARM64 release images
* Multi-arch release images

// Module included in the following assemblies:
//
// * architecture/control-plane.adoc
// * hosted-control-planes/index.adoc

[id="hosted-control-planes-concepts-personas_{context}"]
= Glossary of common concepts and personas for {hcp}

When you use {hcp} for OpenShift Container Platform, it is important to understand its key concepts and the personas that are involved.

[id="hosted-control-planes-concepts_{context}"]
== Concepts

data plane:: The part of the cluster that includes the compute, storage, and networking where workloads and applications run.

hosted cluster:: An OpenShift Container Platform cluster with its control plane and API endpoint hosted on a management cluster. The hosted cluster includes the control plane and its corresponding data plane.

hosted cluster infrastructure:: Network, compute, and storage resources that exist in the tenant or end-user cloud account.

hosted control plane:: An OpenShift Container Platform control plane that runs on the management cluster, which is exposed by the API endpoint of a hosted cluster. The components of a control plane include etcd, the Kubernetes API server, the Kubernetes controller manager, and a VPN.

hosting cluster:: See _management cluster_.

managed cluster:: A cluster that the hub cluster manages. This term is specific to the cluster lifecycle that the {mce} manages in Red Hat Advanced Cluster Management. A managed cluster is not the same thing as a _management cluster_. For more information, see Managed cluster.

management cluster:: An OpenShift Container Platform cluster where the HyperShift Operator is deployed and where the control planes for hosted clusters are hosted. The management cluster is synonymous with the _hosting cluster_.

management cluster infrastructure:: Network, compute, and storage resources of the management cluster.

node pool:: A resource that manages a set of compute nodes that are associated with a hosted cluster. The compute nodes run applications and workloads within the hosted cluster.

[id="hosted-control-planes-personas_{context}"]
== Personas

cluster instance administrator:: Users who assume this role are the equivalent of administrators in standalone OpenShift Container Platform. This user has the `cluster-admin` role in the provisioned cluster, but might not have power over when or how the cluster is updated or configured. This user might have read-only access to see some configuration projected into the cluster.

cluster instance user:: Users who assume this role are the equivalent of developers in standalone OpenShift Container Platform. This user does not have a view into the software catalog or machines.

cluster service consumer:: Users who assume this role can request control planes and worker nodes, drive updates, or modify externalized configurations. Typically, this user does not manage or access cloud credentials or infrastructure encryption keys. The cluster service consumer persona can request hosted clusters and interact with node pools. Users who assume this role have RBAC to create, read, update, or delete hosted clusters and node pools within a logical boundary.

cluster service provider:: Users who assume this role typically have the `cluster-admin` role on the management cluster and have RBAC to monitor and own the availability of the HyperShift Operator as well as the control planes for the tenant's hosted clusters. The cluster service provider persona is responsible for several activities, including the following examples:
** Owning service-level objects for control plane availability, uptime, and stability
** Configuring the cloud account for the management cluster to host control planes
** Configuring the user-provisioned infrastructure, which includes the host awareness of available compute resources
