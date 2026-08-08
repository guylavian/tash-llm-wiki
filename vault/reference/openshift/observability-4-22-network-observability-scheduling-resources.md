---
title: "Scheduling resources"
type: reference
domain: openshift
slug: observability-4-22-network-observability-scheduling-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-scheduling-resources
version: 4.22
family: observability
documentKind: "Documentation"
---

# Scheduling resources

[id="network-observability-scheduling-resources"]
= Scheduling resources

[role="_abstract"]
Taints and tolerations help you control which nodes host certain pods. Use these tools, along with node selectors, to guide the placement of network observability components.

A node selector specifies a map of key/value pairs that are defined using custom labels on nodes and selectors specified in pods.

For the pod to be eligible to run on a node, the pod must have the same key/value node selector as the label on the node.

// Module included in the following assemblies:
//
// network_observability/network-observability-scheduling-resources.adoc

[id="network-observability-multi-tenancy_{context}"]
= Network observability deployment in specific nodes

[role="_abstract"]
Configure the `FlowCollector` resource using scheduling specifications, including `NodeSelector`, `Tolerations`, and `Affinity`, to control the deployment of network observability components on specific nodes.

The `spec.agent.ebpf.advanced.scheduling`, `spec.processor.advanced.scheduling`, and `spec.consolePlugin.advanced.scheduling` specifications have the following configurable settings:

* `NodeSelector`
* `Tolerations`
* `Affinity`
* `PriorityClassName`

.Sample `FlowCollector` resource for `spec.<component>.advanced.scheduling`
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
# ...
advanced:
  scheduling:
    tolerations:
    - key: "<taint key>"
      operator: "Equal"
      value: "<taint value>"
      effect: "<taint effect>"
      nodeSelector:
        <key>: <value>
      affinity:
        nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: name
              operator: In
              values:
              - app-worker-node
      priorityClassName: """
# ...
----

[role="_additional-resources"]
.Additional resources
* Understanding taints and tolerations
* Assign Pods to Nodes (Kubernetes documentation)
* Pod Priority and Preemption (Kubernetes documentation)
