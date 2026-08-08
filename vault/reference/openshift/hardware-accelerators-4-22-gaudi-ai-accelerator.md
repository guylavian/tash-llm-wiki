---
title: "Intel Gaudi AI accelerators"
type: reference
domain: openshift
slug: hardware-accelerators-4-22-gaudi-ai-accelerator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_accelerators/gaudi-ai-accelerator
version: 4.22
family: hardware_accelerators
documentKind: "Documentation"
---

# Intel Gaudi AI accelerators

[id="gaudi-ai-accelerator"]
= Intel Gaudi AI accelerators

You can use Intel Gaudi AI accelerators for your OpenShift Container Platform generative AI and machine learning (AI/ML) applications. Intel Gaudi AI accelerators offer a cost-efficient, flexible, and scalable solution for optimized deep learning workloads.

Red{nbsp}Hat supports Intel Gaudi 2 and Intel Gaudi 3 devices. Intel Gaudi 3 devices provide significant improvements in training speed and energy efficiency.

// Module included in the following assemblies:
//
// * hardware_accelerators/gaudi-ai-accelerator.adoc

[id="gaudi-ai-accelerators-prerequisites_{context}"]
= Intel Gaudi AI accelerators prerequisites

* You have a working OpenShift Container Platform cluster with at least one GPU worker node.

* You have access to the OpenShift Container Platform cluster as a cluster-admin to perform the required steps.

* You have installed {oc-first}.

* You have installed the Node Feature Discovery (NFD) Operator and created a `NodeFeatureDiscovery` instance.

[role="_additional-resources"]
.Additional resources

* OpenShift Installation (Intel Gaudi documentation)

* Intel Gaudi AI Accelerator integration
