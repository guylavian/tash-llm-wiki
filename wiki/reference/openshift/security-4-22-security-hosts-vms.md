---
title: "Understanding host and VM security"
type: reference
domain: openshift
slug: security-4-22-security-hosts-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/security-hosts-vms
version: 4.22
family: security
documentKind: "Documentation"
---

# Understanding host and VM security

[id="security-hosts-vms"]
= Understanding host and VM security

Both containers and virtual machines provide ways of separating
applications running on a host from the operating system itself.
Understanding {op-system}, which is the operating system used by
OpenShift Container Platform, will help you see how the host
systems protect containers and hosts from each other.

// How containers are secured on {op-system}
// Module included in the following assemblies:
//
// * security/container_security/security-hosts-vms.adoc

[id="security-hosts-vms-rhcos_{context}"]
= Securing containers on {op-system-first}

Containers simplify the act of deploying many applications to run on the same host, using the same kernel and container runtime to spin up each container. The applications can be owned by many users and, because they are kept separate, can run different, and even incompatible, versions of those applications at the same time without issue.

In Linux, containers are just a special type of process, so securing containers is similar in many ways to securing any other running process. An environment for running containers starts with an operating system that can secure the host kernel from containers and other processes running on the host, as well as secure containers from each other.

Because OpenShift Container Platform  runs on {op-system} hosts, with the option of using {op-system-base-full} as worker nodes, the following concepts apply by default to any deployed OpenShift Container Platform cluster. These {op-system-base} security features are at the core of what makes running containers in OpenShift Container Platform more secure:

* _Linux namespaces_ enable creating an abstraction of a particular global system resource to make it appear as a separate instance to processes within a namespace. Consequently, several containers can use the same computing resource simultaneously without creating a conflict. Container namespaces that are separate from the host by default include mount table, process table, network interface, user, control group, UTS, and IPC namespaces. Those containers that need direct access to host namespaces need to have elevated permissions to request that access.
See Building, running, and managing containers from the {op-system-base} 9 container documentation for details on the types of namespaces.

* _SELinux_ provides an additional layer of security to keep containers isolated from each other and from the host. SELinux allows administrators to enforce mandatory access controls (MAC) for every user, application, process, and file.

[WARNING]
====
Disabling SELinux on {op-system} is not supported.
====

* _CGroups_ (control groups) limit, account for, and isolate the resource usage (CPU, memory, disk I/O, network, etc.) of a collection of processes. CGroups are used to ensure that containers on the same host are not impacted by each other.

* _Secure computing mode (seccomp)_ profiles can be associated with a container to restrict available system calls. See page 94 of the Red Hat OpenShift security guide for details about seccomp.

* Deploying containers using _{op-system}_ reduces the attack surface by minimizing the host environment and tuning it for containers. The CRI-O container engine further reduces that attack surface by implementing only those features required by Kubernetes and OpenShift Container Platform to run and manage containers, as opposed to other container engines that implement desktop-oriented standalone features.

{op-system} is a version of {op-system-base-full} that is specially configured to work as control plane (master) and worker nodes on OpenShift Container Platform clusters. So {op-system} is tuned to efficiently run container workloads, along with Kubernetes and OpenShift Container Platform services.

[NOTE]
====
To further protect {op-system} systems in OpenShift Container Platform clusters, most containers, except those managing or monitoring the host system itself, should run as a non-root user. Dropping the privilege level or creating containers with the least amount of privileges possible is recommended best practice for protecting your own OpenShift Container Platform clusters.
====

[role="_additional-resources"]
.Additional resources
* How nodes enforce resource constraints
* Managing security context constraints
* Supported platforms for OpenShift clusters
* Choosing how to configure {op-system}
* Ignition
* Kernel arguments
* Kernel modules
* Disk encryption
* Chrony time service
* About the OpenShift Update Service
* FIPS cryptography

// Virtualization versus containers
// Module included in the following assemblies:
//
// * security/container_security/security-hosts-vms.adoc

[id="security-hosts-vms-vs-containers_{context}"]
= Comparing virtualization and containers

Traditional virtualization provides another way to keep application
environments separate on the same physical host. However, virtual machines
work in a different way than containers.
Virtualization relies on a hypervisor spinning up guest
virtual machines (VMs), each of which has its own operating system (OS),
represented by a running kernel, as well as the running application and its dependencies.

With VMs, the hypervisor isolates the guests from each other and from the host
kernel. Fewer individuals and processes have access to the hypervisor, reducing
the attack surface on the physical server. That said, security must still be
monitored: one guest VM might be able to use hypervisor bugs to gain access to
another VM or the host kernel. And, when the OS needs to be patched, it must be
patched on all guest VMs using that OS.

Containers can be run inside guest VMs, and there might be use cases where this is
desirable. For example, you might be deploying a traditional application in a
container, perhaps to lift-and-shift an application to the cloud.

Container separation on a single host, however, provides a more lightweight,
flexible, and easier-to-scale deployment solution. This deployment model is
particularly appropriate for cloud-native applications. Containers are
generally much smaller than VMs and consume less memory and CPU.

See Linux Containers Compared to KVM Virtualization
in the {op-system-base} 7 container documentation to learn about the differences between container and VMs.

// Securing OpenShift
// Module included in the following assemblies:
//
// * security/container_security/security-hosts-vms.adoc

[id="security-hosts-vms-openshift_{context}"]
= Securing OpenShift Container Platform

When you deploy OpenShift Container Platform, you have the choice of an
installer-provisioned infrastructure (there are several available platforms)
or your own user-provisioned infrastructure.
Some low-level security-related configuration, such as enabling FIPS
mode or adding kernel modules required at first boot, might
benefit from a user-provisioned infrastructure.
Some low-level security-related configuration, such as adding kernel modules required at first boot, might
benefit from a user-provisioned infrastructure.
Likewise, user-provisioned infrastructure is appropriate for disconnected OpenShift Container Platform deployments.

Keep in mind that, when it comes to making security enhancements and other
configuration changes to OpenShift Container Platform, the goals should include:

* Keeping the underlying nodes as generic as possible. You want to be able to
easily throw away and spin up similar nodes quickly and in prescriptive ways.
* Managing modifications to nodes through OpenShift Container Platform as much as possible,
rather than making direct, one-off changes to the nodes.

In pursuit of those goals, most node changes should be done during installation through Ignition
or later using MachineConfigs that are applied to sets of nodes by the Machine Config Operator.
Examples of security-related configuration changes you can do in this way include:

* Adding kernel arguments

* Adding kernel modules

* Enabling support for FIPS cryptography

* Configuring disk encryption

* Configuring the chrony time service

Besides the Machine Config Operator, there are several other Operators available to configure OpenShift Container Platform infrastructure that are managed by the Cluster Version Operator (CVO). The CVO is able to automate many aspects of
OpenShift Container Platform cluster updates.

[role="_additional-resources"]
.Additional resources
* FIPS cryptography
