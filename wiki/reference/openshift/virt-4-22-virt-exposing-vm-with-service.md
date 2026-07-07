---
title: "Exposing a virtual machine by using a service"
type: reference
domain: openshift
slug: virt-4-22-virt-exposing-vm-with-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-exposing-vm-with-service
version: 4.22
family: virt
documentKind: "Documentation"
---

# Exposing a virtual machine by using a service

[id="virt-exposing-vm-with-service"]
= Exposing a virtual machine by using a service

[role="_abstract"]
You can expose a virtual machine (VM) within the cluster or outside the cluster by creating a `Service` object. By exposing a VM as a Kubernetes service, you can leverage native load balancing and observability tools that provide unified traffic management, consistent SSL termination, and centralized security policies across hybrid workloads.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-services.adoc
// * virt/vm_networking/virt-exposing-vm-with-service.adoc

[id="virt-about-services_{context}"]
= About services

[role="_abstract"]
A Kubernetes service exposes network access for clients to an application running on a set of pods. Services offer abstraction, load balancing, and, in the case of the `NodePort` and `LoadBalancer` types, exposure to the outside world.

`ClusterIP`:: Exposes the service on an internal IP address and as a DNS name to other applications within the cluster. A single service can map to multiple virtual machines. When a client tries to connect to the service, the client's request is load balanced among available backends. `ClusterIP` is the default service type.

`NodePort`:: Exposes the service on the same port of each selected node in the cluster. `NodePort` makes a port accessible from outside the cluster, provided that the node itself is externally accessible to the client.

`LoadBalancer`:: Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP address to the service.

[NOTE]
====
For on-premise clusters, you can configure a load balancing service by deploying the MetalLB Operator.
====

[NOTE]
====
For {product-rosa}, you must use `externalTrafficPolicy: Cluster` when configuring a load balancing service, to minimize the network downtime during live migration.
====

// Dual-stack (IPv4/IPv6) service configuration is not documented for OpenShift Dedicated
// Module included in the following assemblies:
//
// * virt/vm_networking/virt-exposing-vm-with-service.adoc

[id="virt-dual-stack-support-services_{context}"]
= Dual-stack support

[role="_abstract"]
If IPv4 and IPv6 dual-stack networking is enabled for your cluster, you can create a service that uses IPv4, IPv6, or both, by defining the `spec.ipFamilyPolicy` and the `spec.ipFamilies` fields in the `Service` object.

The `spec.ipFamilyPolicy` field can be set to one of the following values:

SingleStack:: The control plane assigns a cluster IP address for the service based on the first configured service cluster IP range.

PreferDualStack:: The control plane assigns both IPv4 and IPv6 cluster IP addresses for the service on clusters that have dual-stack configured.

RequireDualStack:: This option fails for clusters that do not have dual-stack networking enabled. For clusters that have dual-stack configured, the behavior is the same as when the value is set to `PreferDualStack`. The control plane allocates cluster IP addresses from both IPv4 and IPv6 address ranges.

You can define which IP family to use for single-stack or define the order of IP families for dual-stack by setting the `spec.ipFamilies` field to one of the following array values:

* `[IPv4]`
* `[IPv6]`
* `[IPv4, IPv6]`
* `[IPv6, IPv4]`

[NOTE]
====
IPv6 single stack and the `[IPv6, IPv4]` array are not supported in {ibm-z-name} and {ibm-linuxone-name}.
====

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-services.adoc
// * virt/vm_networking/virt-exposing-vm-with-service.adoc

[id="virt-creating-service-cli_{context}"]
= Creating a service by using the CLI

[role="_abstract"]
You can create a service and associate it with a virtual machine (VM) by using the command line.

.Prerequisites

* You configured the cluster network to support the service.
* You have installed the {oc-first}.

.Procedure

. Edit the `VirtualMachine` manifest to add the label for service creation. Add `special: key` to the `spec.template.metadata.labels` stanza:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: example-namespace
spec:
  runStrategy: Halted
  template:
    metadata:
      labels:
        special: key
# ...
----
+
[NOTE]
====
Labels on a virtual machine pass through to the pod. The `special: key` label must match the label in the `spec.selector` attribute of the `Service` manifest.
====

. Save the `VirtualMachine` manifest file to apply your changes.

. Create a `Service` manifest to expose the VM:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: example-service
  namespace: example-namespace
spec:
# ...
  selector:
    special: key
  type: NodePort
  ports:
    protocol: TCP
    port: 80
    targetPort: 9376
    nodePort: 30000
----
+
* `spec.selector` defines the label that you added to the `spec.template.metadata.labels` stanza of the `VirtualMachine` manifest.
* `spec.type` defines the type of service by the way it is exposed. Choose one of `ClusterIP`, `NodePort`, or `LoadBalancer`.
* `spec.ports` defines a collection of network ports and protocols to expose from the virtual machine.

. Save the `Service` manifest file.
. Create the service by running the following command:
+
[source,terminal]
----
$ oc create -f example-service.yaml
----

. Restart the VM to apply the changes.

.Verification

* Query the `Service` object to verify that it is available:
+
[source,terminal]
----
$ oc get service -n example-namespace
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Configuring ingress cluster traffic by using a `NodePort`
* Configuring ingress cluster traffic by using a load balancer
* Installing the MetalLB Operator
* Configuring services to use MetalLB
