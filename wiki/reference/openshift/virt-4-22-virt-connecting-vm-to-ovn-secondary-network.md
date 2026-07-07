---
title: "Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network"
type: reference
domain: openshift
slug: virt-4-22-virt-connecting-vm-to-ovn-secondary-network
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-connecting-vm-to-ovn-secondary-network
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network

[id="virt-connecting-vm-to-ovn-secondary-network"]
= Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network

[role="_abstract"]
You can connect a VM to an OVN-Kubernetes custom secondary overlay network. A layer 2 topology connects workloads by a cluster-wide logical switch. The OVN-Kubernetes Container Network Interface (CNI) plugin uses the Geneve (Generic Network Virtualization Encapsulation) protocol to create an overlay network between nodes. You can use this overlay network to connect VMs on different nodes, without configuring any additional physical networking infrastructure.

[NOTE]
====
An OVN-Kubernetes secondary network is compatible with the multi-network policy API which provides the `MultiNetworkPolicy` custom resource definition (CRD) to control traffic flow to and from VMs. You must use the `ipBlock` attribute to define network policy ingress and egress rules for specific CIDR blocks. You cannot use pod or namespace selectors for virtualization workloads.
====

To configure an OVN-Kubernetes layer 2 secondary network and attach a VM to that network, perform the following steps:

. Define the secondary network

. Attach the VM to the secondary network

[NOTE]
====
Configuring IP address management (IPAM) by specifying the `spec.config.ipam.subnet` attribute in a network attachment definition for virtual machines is not supported.
====

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-ovn-secondary-network.adoc

[id="virt-creating-layer2-nad-cli_{context}"]
= Creating a NAD for layer 2 topology by using the CLI

[role="_abstract"]
You can create a network attachment definition (NAD) which describes how to attach a pod to the layer 2 overlay network.

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` privileges.
* You have installed the {oc-first}.

.Procedure

. Create a `NetworkAttachmentDefinition` object:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: l2-network
  namespace: my-namespace
spec:
  config: |-
    {
            "cniVersion": "0.3.1",
            "name": "my-namespace-l2-network",
            "type": "ovn-k8s-cni-overlay",
            "topology":"layer2",
            "mtu": 1400,
            "netAttachDefName": "my-namespace/l2-network"
    }
----
+
* `spec.config.cniVersion` defines the Container Network Interface (CNI) specification version. The required value is `0.3.1`.
* `spec.config.name` defines the name of the network. This attribute is not namespaced. For example, you can have a network named `l2-network` referenced from two different `NetworkAttachmentDefinition` objects that exist in two different namespaces. This feature is useful to connect VMs in different namespaces.
* `spec.config.type` defines the name of the CNI plugin. The required value is `ovn-k8s-cni-overlay`.
* `spec.config.topology` defines the topological configuration for the network. The required value is `layer2`.
* `spec.config.mtu` is optional and defines the maximum transmission unit (MTU) value. If you do not set a value, the Cluster Network Operator (CNO) sets a default MTU value by calculating the difference among the underlay MTU of the primary network interface, the overlay MTU of the pod network, such as the Geneve (Generic Network Virtualization Encapsulation), and byte capacity of any enabled features, such as IPsec.
* `spec.config.netAttachDefName` defines the value of the `namespace` and `name` fields in the `metadata` stanza of the `NetworkAttachmentDefinition` object.
+
[NOTE]
====
The previous example configures a cluster-wide overlay without a subnet defined. This means that the logical switch implementing the network only provides layer 2 communication. You must configure an IP address when you create the virtual machine by either setting a static IP address or by deploying a DHCP server on the network for a dynamic IP address.
====

. Apply the manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-ovn-secondary-network.adoc

[id="virt-creating-nad-l2-overlay-console_{context}"]
= Creating a NAD for layer 2 topology by using the web console

[role="_abstract"]
You can create a network attachment definition (NAD) that describes how to attach a pod to the layer 2 overlay network.

.Prerequisites
* You have access to the cluster as a user with `cluster-admin` privileges.

.Procedure

. Go to *Networking* -> *NetworkAttachmentDefinitions* in the web console.

. Click *Create Network Attachment Definition*. The network attachment definition must be in the same namespace as the pod or virtual machine using it.

. Enter a unique *Name* and optional *Description*.

. Select *OVN Kubernetes L2 overlay network* from the *Network Type* list.

. Click *Create*.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-ovn-secondary-network.adoc

[id="virt-attaching-vm-to-ovn-secondary-nw-cli_{context}"]
= Attaching a virtual machine to an OVN-Kubernetes secondary network using the CLI

[role="_abstract"]
You can connect a virtual machine (VM) to the OVN-Kubernetes secondary network by including the network details in the VM configuration.

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` privileges.
* You have installed the {oc-first}.

.Procedure

. Edit the `VirtualMachine` manifest to add the OVN-Kubernetes secondary network interface details, as in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-server
spec:
  runStrategy: Always
  template:
    spec:
      domain:
        devices:
          interfaces:
          - name: secondary
            bridge: {}
        resources:
          requests:
            memory: 1024Mi
      networks:
      - name: secondary
        multus:
          networkName: <nad_name>
      nodeSelector:
        node-role.kubernetes.io/worker: ''
# ...
----
** `spec.template.spec.domain.devices.interfaces.name` specifies the name of the OVN-Kubernetes secondary interface.
** `spec.template.spec.networks.name` specifies the name of the network. This must match the value of the `spec.template.spec.domain.devices.interfaces.name` field.
** `spec.template.spec.networks.multus.networkName` specifies the name of the `NetworkAttachmentDefinition` object.
** `spec.template.spec.nodeSelector` specifies the nodes on which the VM can be scheduled. The recommended node selector value is `node-role.kubernetes.io/worker: ''`.

. Apply the `VirtualMachine` manifest:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. Optional: If you edited a running virtual machine, you must restart it for the changes to take effect.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Creating secondary networks on OVN-Kubernetes
* About the Kubernetes NMState Operator
* Multi-network policy API
* Creating primary networks by using a network attachment definition
