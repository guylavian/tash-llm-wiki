---
title: "{product-title} scalability and performance overview"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/index
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# {product-title} scalability and performance overview

[id="scalability-and-performance-overview"]
= OpenShift Container Platform scalability and performance overview

// ifndef::openshift-dedicated,openshift-rosa[]
OpenShift Container Platform provides best practices and tools to help you optimize the performance and scale of your clusters. The following documentation provides information on recommended performance and scalability practices, reference design specifications, optimization, and low latency tuning.

To contact Red Hat support, see Getting support.

// endif::openshift-dedicated,openshift-rosa[]

[NOTE]
====
Some performance and scalability Operators have release cycles that are independent from OpenShift Container Platform release cycles. For more information, see OpenShift Operators.
====

== Recommended performance and scalability practices

Recommended control plane practices

Recommended infrastructure practices

== Telco reference design specifications

Telco RAN DU reference design specification for OpenShift Container Platform 

Telco core reference design specification

== Planning, optimization, and measurement
Planning your environment according to object maximums

Recommended practices for {ibm-z-title} and {ibm-linuxone-title}

Using the Node Tuning Operator

Using CPU Manager and Topology Manager

Scheduling NUMA-aware workloads

Optimizing storage, routing, networking and CPU usage

Managing bare metal hosts and events

What are huge pages and how are they used by apps

Low latency tuning for improving cluster stability and partitioning workload

Improving cluster stability in high latency environments using worker latency profiles

Workload partitioning

Using the Node Observability Operator

// endif::[]
