---
title: "Chapter 2. Scaling - Red Hat build of Keycloak 26.6 Getting Started Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-getting-started-scaling-and-tuning
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/getting_started_guide/getting-started-scaling-and-tuning-
guide: getting_started_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Scale and tune your Red Hat build of Keycloak installation. After starting Red Hat build of Keycloak, consider adapting your instance to the required load using these scaling and tuning guidelines: minimize resource utilization achieve target response times minimize database pool contention resolve out of memory errors, or excessive garbage collection overhead provide higher availability via horiz…"
---

# Chapter 2. Scaling - Red Hat build of Keycloak 26.6 Getting Started Guide

Chapter 2. Scaling
Scale and tune your Red Hat build of Keycloak installation.
After starting Red Hat build of Keycloak, consider adapting your instance to the required load using these scaling and tuning guidelines:
- minimize resource utilization
- achieve target response times
- minimize database pool contention
- resolve out of memory errors, or excessive garbage collection overhead
- provide higher availability via horizontal scaling
2.1. Vertical Scaling
As you monitor your Red Hat build of Keycloak workload, check to see if the CPU or memory is under or over utilized. Consult Concepts for sizing CPU and memory resources to better tune the resources available to the Java Virtual Machine (JVM).
Before increasing the amount of memory available to the JVM, in particular when experiencing an out of memory error, it is best to determine what is contributing to the increased footprint using a heap dump. Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory. See the following section.
2.1.1. Common Tuning Options
Red Hat build of Keycloak automatically adjusts the number of used threads based upon how many cores you make available. Manually changing the thread count can improve overall throughput. For more details, see Concepts for configuring thread pools. However, changing the thread count must be done in conjunction with other JVM resources, such as database connections; otherwise, you may be moving a bottleneck somewhere else. For more details, see Concepts for database connection pools.
To limit memory utilization of queued work and to provide for load shedding, see Concepts for configuring thread pools.
If you are experiencing timeouts in obtaining database connections, you should consider increasing the number of connections available. For more details, see Concepts for database connection pools.
2.1.2. Vertical Autoscaling
Some platforms, such as Kubernetes, provide mechanisms to vertically autoscale. Vertical autoscaling is not recommended for Red Hat build of Keycloak if it requires restarting the server instance, which is currently the case for Java on Kubernetes. You can consider instead providing higher CPU and/or memory limits to allow your JVM to adapt within those limits as needed.
2.2. Horizontal Scaling
A single Red Hat build of Keycloak instance is susceptible to availability issues. If the instance goes down, you experience a full outage until another instance comes up. By running two or more cluster members on different machines, you greatly increase the availability of Red Hat build of Keycloak.
A single JVM has a limit on how many concurrent requests it can handle. Additional server instances can provide roughly linear scaling of throughput until associated resources, such as the database or distributed caching, limit that scaling.
In general, consider allowing the Red Hat build of Keycloak Operator to handle horizontal scaling concerns. When using the Operator, set the Keycloak custom resource spec.instances
as desired to horizontally scale. For more details, see Deploying Red Hat build of Keycloak across multiple availability-zones with the Operator.
If you are not using the Operator, please review the following:
- Higher availability is possible if your instances are on separate machines. On Kubernetes, use Pod anti-affinity to enforce this.
Use distributed caching; for multi-cluster deployments, use external caching for cluster members to share the same state. For details on the relevant configuration, see Configuring distributed caches. The embedded Infinispan cache has horizontal scaling considerations including:
- Your instances need a way to discover each other. For more information, see discovery in Configuring distributed caches.
- This cache does not gracefully handle multiple members joining or leaving concurrently. In particular, members leaving at the same time can lead to data loss. On Kubernetes, use a StatefulSet with the default serial handling to ensure Pods are started and stopped sequentially, using a deployment is not supported or recommended.
To avoid losing service availability when a whole cluster is unavailable, see the high availability guide for more information on a multi-cluster deployments. See High availability overview.
2.2.1. Horizontal Autoscaling
Horizontal autoscaling allows for adding or removing Red Hat build of Keycloak instances on demand. Keep in mind that startup times will not be instantaneous and that optimized images should be used to minimize the start time.
On Kubernetes, the Keycloak custom resource is scalable meaning that it can be targeted by the built-in autoscaler. For example to scale on average CPU utilization:
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
name: keycloak-hpa
namespace: keycloak-cluster
spec:
scaleTargetRef:
apiVersion: k8s.keycloak.org/v2beta1
kind: Keycloak
name: keycloak
minReplicas: 2
maxReplicas: 10
metrics:
- type: Resource
resource:
name: cpu
target:
type: Utilization
averageUtilization: 80
Scaling on memory is generally not needed with persistent sessions enabled, and should not be needed at all when using remote Data Grid. If you are using persistent sessions or remote Data Grid and you experience memory issues, it is best to fully diagnose the problem and revisit the Concepts for sizing CPU and memory resources guide. Adjusting the memory request and limit is preferable to horizontal scaling.
Consult the Kubernetes docs for additional information, including the usage of custom metrics.
