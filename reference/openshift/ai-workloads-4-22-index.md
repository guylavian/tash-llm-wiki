---
title: "Overview of AI workloads on {product-title}"
type: reference
domain: openshift
slug: ai-workloads-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/index
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Overview of AI workloads on {product-title}

[id="lws-about"]
= {lws-operator} overview

[role="_abstract"]
Use the {lws-operator} to manage multi-node AI/ML inference deployments efficiently. The {lws-operator} treats groups of pods as one unit to simplify scaling, recovery, and updates for large workloads.

Using large language models (LLMs) for AI/ML inference often requires significant compute resources, and workloads typically must be sharded across multiple nodes. This can make deployments complex, creating challenges around scaling, recovery from failures, and efficient pod placement.

The {lws-operator} simplifies these multi-node deployments by treating a group of pods as a single, coordinated unit. It manages the lifecycle of each pod in the group, scales the entire group together, and performs updates and failure recovery at the group level to ensure consistency.

// About the {lws-operator}
// Module included in the following assemblies:
//
// * ai_workloads/leader_worker_set/index.adoc

[id="lws-about_{context}"]
= About the {lws-operator}

[role="_abstract"]
Use the {lws-operator} to deploy groups of pods as a single, manageable unit. This helps you to deploy large AI/ML inference workloads, such as sharded large language models (LLMs).

The {lws-operator} is based on the LeaderWorkerSet open source project. `LeaderWorkerSet` is a custom Kubernetes API that can be used to deploy a group of pods as a unit. This is useful for artificial intelligence (AI) and machine learning (ML) inference workloads, where large language models (LLMs) are sharded across multiple nodes.

With the `LeaderWorkerSet` API, pods are grouped into units consisting of one leader and multiple workers, all managed together as a single entity. Each pod in a group has a unique pod identity. Pods within a group are created in parallel and share identical lifecycle stages. Rollouts, rolling updates, and pod failure restarts are performed as a group.

In the `LeaderWorkerSet` configuration, you define the size of the groups and the number of group replicas. If necessary, you can define separate templates for leader and worker pods, allowing for role-specific customization. You can also configure topology-aware placement, so that pods in the same group are co-located in the same topology.

[IMPORTANT]
====
Before you install the {lws-operator}, you must install the {cert-manager-operator} because it is required to configure services and manage metrics collection.
====

Monitoring for the {lws-operator} is provided by default with OpenShift Container Platform through Prometheus.

[role="_additional-resources"]
.Additional resources

* LeaderWorkerSet project

// LeaderWorkerSet architecture
// Module included in the following assemblies:
//
// * ai_workloads/leader_worker_set/index.adoc

[id="lws-arch_{context}"]
= LeaderWorkerSet architecture

[role="_abstract"]
Review the LeaderWorkerSet architecture to learn how the `LeaderWorkerSet` API organizes groups of pods into a single unit, with one pod as the leader and the rest as the workers, to coordinate distributed workloads.

The following diagram describes the LeaderWorkerSet architecture:

.Leader worker set architecture
image::587_OpenShift_lws_0925.png[Leader worker set architecture]

The `LeaderWorkerSet` API uses a leader stateful set to manage the deployment and lifecycle of the groups of pods. For each replica defined, a leader-worker group is created.

Each leader-worker group contains a leader pod and a worker stateful set. The worker stateful set is owned by the leader pod and manages the set of worker pods associated with that leader pod. The specified size defines the total number of pods in each leader-worker group, with the leader pod included in that number.

[role="_additional-resources"]
[id="lws-about_additional-resources"]
== Additional resources

* LeaderWorkerSet documentation (Kubernetes)
