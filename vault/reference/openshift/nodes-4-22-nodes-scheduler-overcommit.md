---
title: "Placing pods onto overcommited nodes"
type: reference
domain: openshift
slug: nodes-4-22-nodes-scheduler-overcommit
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-scheduler-overcommit
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Placing pods onto overcommited nodes

[id="nodes-scheduler-overcommit"]
= Placing pods onto overcommited nodes

[role="_abstract"]
OpenShift Container Platform administrators can use container compute resource requests and limits to allow and manage the overcommitment of resources on a node, which enables pods to use additional resources when available, without guaranteeing those resources.

In an _overcommited_ state, the sum of the container compute resource requests and limits exceeds the resources available on the system.
Overcommitment might be desirable in development environments where a trade-off of guaranteed performance for capacity is acceptable.

Requests and limits enable administrators to allow and manage the overcommitment of resources on a node.
The scheduler uses requests for scheduling your container and providing a minimum service guarantee.
Limits constrain the amount of compute resource that may be consumed on your node.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc

[id="nodes-cluster-overcommit-about_{context}"]
= Understanding overcommitment

[role="_abstract"]
OpenShift Container Platform administrators can control the level of overcommit and manage container density on nodes by configuring masters to override the ratio between the container compute resource requests and limits set on developer containers.

Requests and limits enable administrators to allow and manage the overcommitment of resources on a node. The scheduler uses requests for scheduling your container and providing a minimum service guarantee. Limits constrain the amount of compute resource that may be consumed on your node. In conjunction with a per-project `LimitRange` object specifying limits and defaults, this adjusts the container limit and request to achieve the desired level of overcommit.

[NOTE]
====
That these overrides have no effect if no limits have been set on containers. Create a `LimitRange` object with default limits, per individual project, or in the project template, to ensure that the overrides apply.
====

After these overrides, the container limits and requests must still be validated by any `LimitRange` object in the project. It is possible, for example, for developers to specify a limit close to the minimum limit, and have the request then be overridden below the minimum limit, causing the pod to be forbidden. This unfortunate user experience should be addressed with future work, but for now, configure this capability and `LimitRange` objects with caution.

// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

[id="nodes-cluster-overcommit-configure-nodes_{context}"]
= Understanding nodes overcommitment

[role="_abstract"]
To maintain optimal system performance and stability in an overcommitted environment in OpenShift Container Platform, configure your nodes to manage resource contention effectively.

When the node starts, it ensures that the kernel tunable flags for memory management are set properly. The kernel should never fail memory allocations unless it runs out of physical memory.

To ensure this behavior, OpenShift Container Platform configures the kernel to always overcommit memory by setting the `vm.overcommit_memory` parameter to `1`, overriding the default operating system setting.

OpenShift Container Platform also configures the kernel to not panic when it runs out of memory by setting the `vm.panic_on_oom` parameter to `0`. A setting of 0 instructs the kernel to call the OOM killer in an Out of Memory (OOM) condition, which kills processes based on priority.

You can view the current setting by running the following commands on your nodes:

[source,terminal]
----
$ sysctl -a |grep commit
----

.Example output
[source,terminal]
----
#...
vm.overcommit_memory = 0
#...
----

[source,terminal]
----
$ sysctl -a |grep panic
----

.Example output
[source,terminal]
----
#...
vm.panic_on_oom = 0
#...
----

[NOTE]
====
The previous commands should already be set on nodes, so no further action is required.
====

You can also perform the following configurations for each node:

* Disable or enforce CPU limits using CPU CFS quotas

* Reserve resources for system processes

* Reserve memory across quality of service tiers
