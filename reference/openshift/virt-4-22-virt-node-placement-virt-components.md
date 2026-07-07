---
title: "Specifying nodes for {VirtProductName} components"
type: reference
domain: openshift
slug: virt-4-22-virt-node-placement-virt-components
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-node-placement-virt-components
version: 4.22
family: virt
documentKind: "Documentation"
---

# Specifying nodes for {VirtProductName} components

[id="virt-node-placement-virt-components"]
= Specifying nodes for {VirtProductName} components

[role="_abstract"]
You can configure node placement rules to specify where {VirtProductName} Operators, workloads, and controllers are deployed. While default scheduling is sufficient for standard environments, custom placement rules allow you to isolate virtual machine (VM) traffic or dedicate specialized compute resources to critical workloads.

[IMPORTANT]
====
You can configure node placement rules for some components after installing {VirtProductName}, but virtual machines cannot be present if you want to configure node placement rules for workloads.
====

// Module included in the following assemblies:
//
// * vvirt/post_installation_configuration/virt-node-placement-virt-components.adoc

[id="virt-about-node-placement-virt-components_{context}"]
= About node placement rules for {VirtProductName} components

[role="_abstract"]
You can use node placement rules to deploy virtual machines only on nodes intended for virtualization workloads, to deploy Operators only on infrastructure nodes, or to maintain separation between workloads.

Depending on the object, you can use one or more of the following rule types:

`nodeSelector`:: Allows pods to be scheduled on nodes that are labeled with the key-value pair or pairs that you specify in this field. The node must have labels that exactly match all listed pairs.
`affinity`:: Enables you to use more expressive syntax to set rules that match nodes with pods. Affinity also allows for more nuance in how the rules are applied. For example, you can specify that a rule is a preference, not a requirement. If a rule is a preference, pods are still scheduled when the rule is not satisfied.
`tolerations`:: Allows pods to be scheduled on nodes that have matching taints. If a taint is applied to a node, that node only accepts pods that tolerate the taint.

If you are running an {ibm-z-title} or {ibm-linuxone-title} (`s390x`) cluster with mixed hypervisors, refer to the following table for the supported nodes to run the virtual machines.

.{ibm-z-name} node options
[cols="1,1,1,1,1",options="header"]
|===
|Node architecture |Hypervisor |VM deployment |Node selection |VM architecture

|s390x
|LPAR
|Supported
|set node selector for LPAR node
|s390x

|s390x
|z/VM
|Unsupported
|set anti-affinity for z/VM node
|Not applicable

|s390x
|KVM
|Unsupported
|set anti-affinity for KVM node
|Not applicable
|===

[NOTE]
====
The scheduler does not select LPAR over z/VM or KVM nodes on `s390x` by default. To have a supported `s390x` virtual machine, you must set at least one `s390x` LPAR node as a schedulable compute node and you must set the node selector before deploying the virtual machine.
====

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-node-placement-virt-components.adoc

[id="virt-applying-node-place-rules_{context}"]
= Applying node placement rules

[role="_abstract"]
To ensure that virtualization components run on the most suitable nodes for your workload requirements, you can apply node placement rules by editing the `Subscription`, `HyperConverged`, or `HostPathProvisioner` objects.
[role="_abstract"]
To ensure that virtualization components run on the most suitable nodes for your workload requirements, you can apply node placement rules by editing the `HyperConverged` or `HostPathProvisioner` objects.

.Prerequisites

* You have installed the {oc-first}.
* You are logged in with cluster administrator permissions.

.Procedure

. Edit the object in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit <resource_type> <resource_name> -n {CNVNamespace}
----

. Save the file to apply the changes.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-node-placement-virt-components.adoc

[id="virt-node-placement-rule-examples_{context}"]
= Node placement rule examples

[role="_abstract"]
You can specify node placement rules for a {VirtProductName} component by editing a `Subscription`, `HyperConverged`, or `HostPathProvisioner` object.
[role="_abstract"]
You can specify node placement rules for a {VirtProductName} component by editing a `HyperConverged` or `HostPathProvisioner` object.

[id="subscription-object-node-placement-rules_{context}"]
== Subscription object node placement rule examples

To specify the nodes where OLM deploys the {VirtProductName} Operators, edit the `Subscription` object during {VirtProductName} installation.

Currently, you cannot configure node placement rules for the `Subscription` object by using the web console.

The `Subscription` object does not support the `affinity` node placement rule.

Example `Subscription` object with `nodeSelector` rule:

[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source: {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable"
  config:
    nodeSelector:
      example.io/example-infra-key: example-infra-value
----

OLM deploys the {VirtProductName} Operators on nodes labeled `example.io/example-infra-key = example-infra-value`.

Example `Subscription` object with `tolerations` rule:

[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source:  {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable"
  config:
    tolerations:
    - key: "key"
      operator: "Equal"
      value: "virtualization"
      effect: "NoSchedule"
----

OLM deploys {VirtProductName} Operators on nodes labeled `key = virtualization:NoSchedule` taint. Only pods with the matching tolerations are scheduled on these nodes.

[id="hyperconverged-object-node-placement-rules_{context}"]
== HyperConverged object node placement rule example

To specify the nodes where {VirtProductName} deploys its components, you can edit the `nodePlacement` object in the `HyperConverged` custom resource (CR) file that you create during {VirtProductName} installation.

Example `HyperConverged` object with `nodeSelector` rule:

[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  infra:
    nodePlacement:
      nodeSelector:
        example.io/example-infra-key: example-infra-value
  workloads:
    nodePlacement:
      nodeSelector:
        example.io/example-workloads-key: example-workloads-value
----

* Infrastructure resources are placed on nodes labeled `example.io/example-infra-key = example-infra-value`.
* Workloads are placed on nodes labeled `example.io/example-workloads-key = example-workloads-value`.

Example `HyperConverged` object with `affinity` rule:

[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  infra:
    nodePlacement:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: example.io/example-infra-key
                operator: In
                values:
                - example-infra-value
  workloads:
    nodePlacement:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: example.io/example-workloads-key
                operator: In
                values:
                - example-workloads-value
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: example.io/num-cpus
                operator: Gt
                values:
                - 8
----

* Infrastructure resources are placed on nodes labeled `example.io/example-infra-key = example-value`.
* Workloads are placed on nodes labeled `example.io/example-workloads-key = example-workloads-value`.
* Nodes that have more than eight CPUs are preferred for workloads, but if they are not available, pods are still scheduled.

Example `HyperConverged` object with `tolerations` rule:

[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  workloads:
    nodePlacement:
      tolerations:
      - key: "key"
        operator: "Equal"
        value: "virtualization"
        effect: "NoSchedule"
----

Nodes reserved for {VirtProductName} components are labeled with the `key = virtualization:NoSchedule` taint. Only pods with matching tolerations are scheduled on reserved nodes.

[id="hostpathprovisioner-object-node-placement-rules_{context}"]
== HostPathProvisioner object node placement rule example

You can edit the `HostPathProvisioner` object directly or by using the web console.

[WARNING]
====
You must schedule the hostpath provisioner (HPP) and the {VirtProductName} components on the same nodes. Otherwise, virtualization pods that use the hostpath provisioner cannot run. You cannot run virtual machines.
====

After you deploy a virtual machine (VM) with the HPP storage class, you can remove the hostpath provisioner pod from the same node by using the node selector. However, you must first revert that change, at least for that specific node, and wait for the pod to run before trying to delete the VM.

You can configure node placement rules by specifying `nodeSelector`, `affinity`, or `tolerations` for the `spec.workload` field of the `HostPathProvisioner` object that you create when you install the hostpath provisioner.

Example `HostPathProvisioner` object with `nodeSelector` rule:

[source,yaml]
----
apiVersion: hostpathprovisioner.kubevirt.io/v1beta1
kind: HostPathProvisioner
metadata:
  name: hostpath-provisioner
spec:
  imagePullPolicy: IfNotPresent
  pathConfig:
    path: "</path/to/backing/directory>"
    useNamingPrefix: false
  workload:
    nodeSelector:
      example.io/example-workloads-key: example-workloads-value
----

Workloads are placed on nodes labeled `example.io/example-workloads-key = example-workloads-value`.

[id="additional-resources_virt-node-placement-virt-components"]
[role="_additional-resources"]
== Additional resources
* Specifying nodes for virtual machines
* Placing pods on specific nodes using node selectors
* Controlling pod placement on nodes using node affinity rules
* Controlling pod placement using node taints
