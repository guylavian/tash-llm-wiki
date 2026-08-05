---
title: "{product-title} architecture"
type: reference
domain: openshift
slug: architecture-4-22-architecture
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/architecture
version: 4.22
family: architecture
documentKind: "Documentation"
---

# {product-title} architecture

[id="architecture"]
= OpenShift Container Platform architecture
[id="architecture"]
= OpenShift Container Platform

// Module included in the following assemblies:
// * architecture/architecture.adoc

[id="architecture-platform-introduction_{context}"]
= Introduction to OpenShift Container Platform

OpenShift Container Platform is a platform for developing and running containerized applications. It is designed to allow applications and the data centers that support them to expand from just a few machines and applications to thousands of machines that serve millions of clients.

With its foundation in Kubernetes, OpenShift Container Platform incorporates the same technology that serves as the engine for massive telecommunications, streaming video, gaming, banking, and other applications. Its implementation in open
Red{nbsp}Hat technologies lets you extend your containerized applications beyond a single cloud to on-premise and multi-cloud environments.

image::525-OpenShift-arch-012025.png[Red Hat {oke}]

// The architecture presented here is meant to give you insights into how OpenShift Container Platform works. It does this by stepping you through the process of installing an OpenShift Container Platform cluster, managing the cluster, and developing and deploying applications on it. Along the way, this architecture describes:

// * Major components of  OpenShift Container Platform
// * Ways of exploring different aspects of OpenShift Container Platform yourself
// * Available frontdoors (and backdoors) to modify the installation and management of your OpenShift Container Platform cluster
// * Different types of container application types

// Module included in the following assemblies:
//
// * architecture/architecture.adoc

[id="architecture-kubernetes-introduction_{context}"]
= About Kubernetes

Although container images and the containers that run from them are the
primary building blocks for modern application development, to run them at scale
requires a reliable and flexible distribution system. Kubernetes is the
defacto standard for orchestrating containers.

Kubernetes is an open source container orchestration engine for automating
deployment, scaling, and management of containerized applications. The general
concept of Kubernetes is fairly simple:

* Start with one or more worker nodes to run the container workloads.
* Manage the deployment of those workloads from one or more control plane nodes.
* Wrap containers in a deployment unit called a pod. Using pods provides extra
metadata with the container and offers the ability to group several containers
in a single deployment entity.
* Create special kinds of assets. For example, services are represented by a
set of pods and a policy that defines how they are accessed. This policy
allows containers to connect to the services that they need even if they do not
have the specific IP addresses for the services. Replication controllers are
another special asset that indicates how many pod replicas are required to run
at a time. You can use this capability to automatically scale your application
to adapt to its current demand.

In only a few years, Kubernetes has seen massive cloud and on-premise adoption.
The open source development model allows many people to extend Kubernetes
by implementing different technologies for components such as networking,
storage, and authentication.

// Module included in the following assemblies:
//
// * architecture/architecture.adoc

[id="architecture-container-application-benefits_{context}"]
= The benefits of containerized applications

Using containerized applications offers many advantages over using traditional deployment methods. Where applications were once expected to be installed on operating systems that included all their dependencies, containers let an application carry their dependencies with them. Creating containerized applications offers many benefits.

[id="operating-system-benefits_{context}"]
== Operating system benefits

Containers use small, dedicated Linux operating systems without a kernel. Their file system, networking, cgroups, process tables, and namespaces are separate from the host Linux system, but the containers can integrate with the hosts seamlessly when necessary. Being based on Linux allows containers to use all the advantages that come with the open source development model of rapid innovation.

Because each container uses a dedicated operating system, you can deploy applications that require conflicting software dependencies on the same host. Each container carries its own dependent software and manages its own interfaces, such as networking and file systems, so applications never need to compete for those assets.

[id="deployment-scaling-benefits_{context}"]
== Deployment and scaling benefits

If you employ rolling upgrades between major releases of your application, you can continuously improve your applications without downtime and still maintain compatibility with the current release.

You can also deploy and test a new version of an application alongside the existing version. If the container passes your tests, simply deploy more new containers and remove the old ones.

Since all the software dependencies for an application are resolved within the container itself, you can use a standardized operating system on each host in your data center. You do not need to configure a specific operating system for each application host. When your data center needs more capacity, you can deploy another generic host system.

Similarly, scaling containerized applications is simple. OpenShift Container Platform offers a simple, standard way of scaling any containerized service. For example, if you build applications as a set of microservices rather than large, monolithic applications, you can scale the individual microservices individually to meet demand. This capability allows you to scale only the required services instead of the entire application, which can allow you to meet application demands while using minimal resources.

// Module included in the following assemblies:
//
// * architecture/architecture.adoc

[id="architecture-platform-benefits_{context}"]
= OpenShift Container Platform overview

Red Hat was one of the early contributors of Kubernetes and quickly integrated
it as the centerpiece of its OpenShift Container Platform product line. Today, Red Hat
continues as one of the largest contributors to Kubernetes across a wide range
of technology areas.

OpenShift Container Platform provides enterprise-ready enhancements to Kubernetes, including the following enhancements:

* Hybrid cloud deployments. You can deploy OpenShift Container Platform clusters to a variety of public cloud platforms or in your data center.
* Integrated Red Hat technology. Major components in OpenShift Container Platform come from {op-system-base-full} and related Red Hat technologies. OpenShift Container Platform benefits from the intense testing and certification initiatives for Red Hat's enterprise quality software.
* Open source development model. Development is completed in the open, and the source code is available from public software repositories. This open collaboration fosters rapid innovation and development.

Although Kubernetes excels at managing your applications, it does not specify
or manage platform-level requirements or deployment processes. Powerful and
flexible platform management tools and processes are important benefits that
OpenShift Container Platform  offers. The following sections describe some
unique features and benefits of OpenShift Container Platform.

[id="architecture-custom-os_{context}"]
== Custom operating system

OpenShift Container Platform uses {op-system-first}, a container-oriented operating system that is specifically designed for running containerized applications from OpenShift Container Platform and works with new tools to provide fast installation, Operator-based management, and simplified upgrades.

OpenShift Container Platform uses {op-system-first} as the operating system for all control plane and worker nodes.

{op-system} includes:

* Ignition, which OpenShift Container Platform uses as a firstboot system configuration for initially bringing up and configuring machines.
* CRI-O, a Kubernetes native container runtime implementation that integrates closely with the operating system to deliver an efficient and optimized Kubernetes experience. CRI-O provides facilities for running, stopping, and restarting containers. It fully replaces the Docker Container Engine, which was used in OpenShift Container Platform 3.
* Kubelet, the primary node agent for Kubernetes that is responsible for
launching and monitoring containers.

In OpenShift Container Platform , you must use {op-system} for all control
plane machines, but you can use Red Hat Enterprise Linux (RHEL) as the operating
system for compute machines, which are also known as worker machines. If you choose to use RHEL workers, you
must perform more system maintenance than if you use {op-system} for all of the
cluster machines.

[id="architecture-platform-management_{context}"]
== Simplified installation and update process
== Simplified update process

With OpenShift Container Platform , if you have an account with the right
permissions, you can deploy a production cluster in supported clouds by running
a single command and providing a few values. You can also customize your cloud
installation or install your cluster in your data center if you use a supported
platform.

For clusters that use {op-system} for all machines, updating, or
upgrading, OpenShift Container Platform is a simple, highly-automated process. Because
OpenShift Container Platform completely controls the systems and services that run on each
machine, including the operating system itself, from a central control plane,
upgrades are designed to become automatic events. If your cluster contains
RHEL worker machines, the control plane benefits from the streamlined update
process, but you must perform more tasks to upgrade the RHEL machines.

Updating, or upgrading, OpenShift Container Platform is a simple, highly-automated process. Because OpenShift Container Platform completely controls the systems and services that run on each machine, including the operating system itself, from a central control plane, upgrades are designed to become automatic events.

[id="architecture-key-features_{context}"]
== Other key features

Operators are both the fundamental unit of the OpenShift Container Platform 
code base and a convenient way to deploy applications and software components
for your applications to use. In OpenShift Container Platform, Operators serve as the platform foundation and remove the need for manual upgrades of operating systems and control plane applications. OpenShift Container Platform Operators such as the
Cluster Version Operator and Machine Config Operator allow simplified,
cluster-wide management of those critical components.

Operator Lifecycle Manager (OLM) and the software catalog provide facilities for
storing and distributing Operators to people developing and deploying applications.

The {quay} Container Registry is a Quay.io container registry that serves
most of the container images and Operators to OpenShift Container Platform clusters.
Quay.io is a public registry version of {quay} that stores millions of images
and tags.

Other enhancements to Kubernetes in OpenShift Container Platform include improvements in
software defined networking (SDN), authentication, log aggregation, monitoring,
and routing. OpenShift Container Platform also offers a comprehensive web console and the
custom OpenShift CLI (`oc`) interface.

OpenShift Container Platform includes the following infrastructure components:

* OpenShift API server
* Kubernetes API server
* Kubernetes controller manager
* Kubernetes nodes/kubelet
* CRI-O
* {op-system}
* Infrastructure Operators
* Networking (SDN/Router/DNS)
* Storage
* Monitoring
* Telemetry
* Security
* Authorization/Authentication/Oauth
* Logging

It also offers the following user interfaces:
* Web Console
* OpenShift CLI (`oc`)
* Rest API

[id="architecture-overview-image_{context}"]
== OpenShift Container Platform lifecycle

The following figure illustrates the basic OpenShift Container Platform lifecycle:

* Creating an OpenShift Container Platform cluster
* Managing the cluster
* Developing and deploying applications
* Scaling up applications

.High level OpenShift Container Platform overview
image::ocp_arch_lifecycle.png[High-level OpenShift Container Platform flow]

== User facing components
* Workloads (Deployments, Jobs, ReplicaSets, etc)
* Operator Lifecycle Manager
* Builds - The build component
provides an API and infrastructure for producing new container images using a
variety of techniques including industry standard Dockerfiles and publishing
them to either the cluster image registry, or an external registry. It also
provides integration with Jenkins based pipeline continuous integration
workflows.
* Image Registry -
The image registry provides a scalable repository for storing and retrieving
container images that are produced by and run on the cluster. Image access is
integrated with the cluster's role-based access controls and user authentication
system.
* Image
streams - The imagestream API provides an abstraction over container images
that exist in registries. It allows workloads to reference an image indirectly,
retains a history of the images that have been referenced, and allows
notification when an image is updated with a new version.

// Module included in the following assemblies:
//
// * installing/installing_bare_metal/upi/installing-bare-metal-network-customizations.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-installer-provisioned-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-installer-provisioned.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_platform_agnostic/installing-platform-agnostic.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-network-customizations.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-vpc.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-private.adoc
// * installing/installing_ibm_cloud/installing-ibm-cloud-restricted.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc
// * installing/installing_azure/installing-azure-default.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-default.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china-region.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
// * installing/installing_aws/installing-aws-localzone.adoc
// * installing/installing-aws-wavelength-zone
// * installing/installing_openstack/installing-openstack-installer-restricted.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-sr-iov.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-sr-iov.adoc
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-default.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_ibm_power/installing-ibm-power.adoc
// * installing/installing_ibm_power/installing-restricted-networks-ibm-power.adoc
// * installing/installing_ibm_powervs/installing-ibm-power-vs-private-cluster.adoc
// * installing/installing_ibm_powervs/installing-restricted-networks-ibm-power-vs.adoc
// * installing/installing_ibm_powervs/installing-ibm-powervs-vpc.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-network-customizations.adoc
// * architecture/architecture.adoc
// * installing/installing_nutanix/installing-nutanix-installer-provisioned.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc
// * installing/installing_ibm_z/upi-ibm-z-preparing-to-install.adoc

[id="cluster-entitlements_{context}"]
= Internet access for OpenShift Container Platform

[role="_abstract"]
In OpenShift Container Platform , you require access to the internet to
install
obtain the images that are necessary to install
your cluster.

You must have internet access to perform the following actions:

* Access {cluster-manager-url} to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

[IMPORTANT]
====
If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.
====
