---
title: "Working with quotas"
type: reference
domain: openshift
slug: applications-4-22-working-with-quotas
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/working-with-quotas
version: 4.22
family: applications
documentKind: "Documentation"
---

# Working with quotas

[id="working-with-quotas"]
= Working with quotas

A _resource quota_, defined by a ResourceQuota object, provides constraints that
limit aggregate resource consumption per project. It can limit the quantity of
objects that can be created in a project by type, as well as the total amount of
compute resources and storage that may be consumed by resources in that project.

An _object quota count_ places a defined quota on all standard namespaced resource
types. When using a resource quota, an object is charged against the quota if it
exists in server storage. These types of quotas are useful to protect against
exhaustion of storage resources.

This guide describes how resource quotas work and how developers can work with
and view them.

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quota-viewing-quotas_{context}"]
= Viewing a quota

You can view usage statistics related to any hard limits defined in a quota for a project by navigating in the web console to the project's *Quota* page.

You can also use the CLI to view quota details.

.Procedure

. Get the list of quotas defined in the project. For example, for a project called
`demoproject`:
+
[source,terminal]
----
$ oc get quota -n demoproject
----
+
.Example output
[source,terminal]
----
NAME                           AGE    REQUEST                                                                                                      LIMIT
besteffort                     4s     pods: 1/2
compute-resources-time-bound   10m    pods: 0/2                                                                                                    limits.cpu: 0/1, limits.memory: 0/1Gi
core-object-counts             109s   configmaps: 2/10, persistentvolumeclaims: 1/4, replicationcontrollers: 1/20, secrets: 9/10, services: 2/10
----

. Describe the quota you are interested in, for example the `core-object-counts`
quota:
+
[source,terminal]
----
$ oc describe quota core-object-counts -n demoproject
----
+
.Example output
[source,terminal]
----
Name:			core-object-counts
Namespace:		demoproject
Resource		Used	Hard
--------		----	----
configmaps		3	10
persistentvolumeclaims	0	4
replicationcontrollers	3	20
secrets			9	10
services		2	10
----

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-resources-managed_{context}"]
= Resources managed by quotas

The following describes the set of compute resources and object types that can be managed by a quota.

[NOTE]
====
A pod is in a terminal state if `status.phase in (Failed, Succeeded)` is true.
====

.Compute resources managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`cpu`
|The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.

|`memory`
|The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.

|`requests.cpu`
|The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.

|`requests.memory`
|The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.

|`limits.cpu`
|The sum of CPU limits across all pods in a non-terminal state cannot exceed this value.

|`limits.memory`
|The sum of memory limits across all pods in a non-terminal state cannot exceed this value.

|===

.Storage resources managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`requests.storage`
|The sum of storage requests across all persistent volume claims in any state cannot exceed this value.

|`persistentvolumeclaims`
|The total number of persistent volume claims that can exist in the project.

|`<storage-class-name>.storageclass.storage.k8s.io/requests.storage`
|The sum of storage requests across all persistent volume claims in any state that have a matching storage class, cannot exceed this value.

|`<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims`
|The total number of persistent volume claims with a matching storage class that can exist in the project.

|`ephemeral-storage`
|The sum of local ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably.

|`requests.ephemeral-storage`
|The sum of ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably.

|`limits.ephemeral-storage`
|The sum of ephemeral storage limits across all pods in a non-terminal state cannot exceed this value.
|===

[id="quotas-object-counts-managed_{context}"]
.Object counts managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`pods`
|The total number of pods in a non-terminal state that can exist in the project.

|`replicationcontrollers`
|The total number of ReplicationControllers that can exist in the project.

|`resourcequotas`
|The total number of resource quotas that can exist in the project.

|`services`
|The total number of services that can exist in the project.

|`services.loadbalancers`
|The total number of services of type `LoadBalancer` that can exist in the project.

|`services.nodeports`
|The total number of services of type `NodePort` that can exist in the project.

|`secrets`
|The total number of secrets that can exist in the project.

|`configmaps`
|The total number of `ConfigMap` objects that can exist in the project.

|`persistentvolumeclaims`
|The total number of persistent volume claims that can exist in the project.

|`openshift.io/imagestreams`
|The total number of imagestreams that can exist in the project.
|===

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-scopes_{context}"]
= Quota scopes

Each quota can have an associated set of _scopes_. A quota only measures usage for a resource if it matches the intersection of enumerated scopes.

Adding a scope to a quota restricts the set of resources to which that quota can apply. Specifying a resource outside of the allowed set results in a validation error.

|===

|Scope |Description

|`BestEffort`
|Match pods that have best effort quality of service for either `cpu` or
`memory`.

|`NotBestEffort`
|Match pods that do not have best effort quality of service for `cpu` and
`memory`.
|===

A `BestEffort` scope restricts a quota to limiting the following resources:

- `pods`

A `NotBestEffort` scope restricts a quota to tracking the following resources:

- `pods`
- `memory`
- `requests.memory`
- `limits.memory`
- `cpu`
- `requests.cpu`
- `limits.cpu`

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quota-enforcement_{context}"]
= Quota enforcement

After a resource quota for a project is first created, the project restricts the ability to create any new resources that may violate a quota constraint until it has calculated updated usage statistics.

After a quota is created and usage statistics are updated, the project accepts the creation of new content. When you create or modify resources, your quota usage is incremented immediately upon the request to create or modify the resource.

When you delete a resource, your quota use is decremented during the next full recalculation of quota statistics for the project. A configurable amount of time determines how long it takes to reduce quota usage statistics to their current observed system value.

If project modifications exceed a quota usage limit, the server denies the action, and an appropriate error message is returned to the user explaining the quota constraint violated, and what their currently observed usage statistics are in the system.

// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-requests-vs-limits_{context}"]
= Requests versus limits

When allocating compute resources, each container might specify a request and a limit value each for CPU, memory, and ephemeral storage. Quotas can restrict any of these values.

If the quota has a value specified for `requests.cpu` or `requests.memory`, then it requires that every incoming container make an explicit request for those resources. If the quota has a value specified for `limits.cpu` or `limits.memory`, then it requires that every incoming container specify an explicit limit for those resources.
