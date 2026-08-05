---
title: "Connecting a virtual machine to a primary user-defined network"
type: reference
domain: openshift
slug: virt-4-22-virt-connecting-vm-to-primary-udn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-connecting-vm-to-primary-udn
version: 4.22
family: virt
documentKind: "Documentation"
---

# Connecting a virtual machine to a primary user-defined network

[id="virt-connecting-vm-to-primary-udn"]
= Connecting a virtual machine to a primary user-defined network

[role="_abstract"]
You can connect a virtual machine (VM) to a user-defined network (UDN) on the VM's primary interface by using the OpenShift Container Platform web console or the CLI. The primary user-defined network replaces the default pod network in your specified namespace. Unlike the pod network, you can define the primary UDN per project, where each project can use its specific subnet and topology.

{VirtProductName} supports the namespace-scoped `UserDefinedNetwork` and the cluster-scoped `ClusterUserDefinedNetwork` custom resource definitions (CRD).

Cluster administrators can configure a primary `UserDefinedNetwork` CRD to create a tenant network that isolates the tenant namespace from other namespaces without requiring network policies. Additionally, cluster administrators can use the `ClusterUserDefinedNetwork` CRD to create a shared OVN network across multiple namespaces.

[NOTE]
====
You must add the `k8s.ovn.org/primary-user-defined-network` label when you create a namespace that is to be used with user-defined networks.
====

With the layer 2 topology, OVN-Kubernetes creates an overlay network between nodes. You can use this overlay network to connect VMs on different nodes without having to configure any additional physical networking infrastructure.

The layer 2 topology enables seamless migration of VMs without the need for Network Address Translation (NAT) because persistent IP addresses are preserved across cluster nodes during live migration.

You must consider the following limitations before implementing a primary UDN:

* You cannot use the `virtctl ssh` command to configure SSH access to a VM.
* You cannot use the `oc port-forward` command to forward ports to a VM.
* You cannot use headless services to access a VM.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-primary-udn-web-intro_{context}"]
= Create a primary user-defined network by using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to create a primary namespace-scoped `UserDefinedNetwork` or a cluster-scoped `ClusterUserDefinedNetwork` custom resource definition (CRD). The UDN serves as the default primary network for pods and VMs that you create in namespaces associated with the network.

After you define the custom primary overlay network, you can create namespaces that are associated with the cluster-scoped UDN.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-udn-namespace-web_{context}"]
= Creating a namespace for user-defined networks by using the web console

[role="_abstract"]
You can create a namespace to be used with primary user-defined networks (UDNs) by using the OpenShift Container Platform web console.

.Prerequisites
* Log in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure
. From the *Administrator* perspective, click *Administration* -> *Namespaces*.

. Click *Create Namespace*.

. In the *Name* field, specify a name for the namespace. The name must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character.

. In the *Labels* field, add the `k8s.ovn.org/primary-user-defined-network` label.

. Optional: If the namespace is to be used with an existing cluster-scoped UDN, add the appropriate labels as defined in the `spec.namespaceSelector` field in the `ClusterUserDefinedNetwork` custom resource.

. Optional: Specify a default network policy.

. Click *Create* to create the namespace.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-primary-udn-web_{context}"]
= Creating a primary namespace-scoped user-defined network by using the web console

[role="_abstract"]
You can create an isolated primary network in your project namespace by creating a `UserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

.Prerequisites
* You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.
* You have created a namespace and applied the `k8s.ovn.org/primary-user-defined-network` label. For more information, see "Creating a namespace for user-defined networks by using the web console".

.Procedure
. From the *Administrator* perspective, click *Networking* -> *UserDefinedNetworks*.

. Click *Create UserDefinedNetwork*.

. From the *Project name* list, select the namespace that you previously created.

. Specify a value in the *Subnet* field.

. Click *Create*. The user-defined network serves as the default primary network for pods and virtual machines that you create in this namespace.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc
[id="virt-creating-a-localnet-cudn-web_{context}"]
= Creating a cluster-scoped network to connect pods directly to an external network

[role="_abstract"]
You can connect one or more projects to a physical network for direct layer 2 access to data center resources through a `ClusterUserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

.Prerequisites
* You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure

. In the OpenShift Container Platform web console, go to *Virtualization* -> *Networking*.
. Click *Virtual machine networks* in the navigation pane.
. Click *Create*. The *Create virtual machine network* wizard is displayed.
. Give details about the network on the *Network definition* page:
.. Enter a name for the network in the *Name* field.
.. Select a physical network through an `OpenvSwitch` bridge from the *Select physical network* list.
.. Enter the maximum transmission unit (MTU).
+
[NOTE]
====
An MTU, measured in bytes, is the largest allowable size of a data packet. Ensure that all underlying physical network equipment supports this MTU, or higher.
====
.. Optional: Select the *VLAN ID* checkbox to enter VLAN tagging information. If you tag traffic with a VLAN ID, you must configure your physical switch with a VLAN trunk that includes the VLAN ID that you choose.
. Click *Next*.
. Select the projects that the network should be made available to on the *Project mapping* page. By default, all projects have access to the network.
. Click *Create*.

.Verification

. Navigate to the *Virtualization* -> *Virtual machine networks* page.
. Click the *OVN localnet* tab.
. Verify that your new network is displayed in the list.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-primary-cluster-udn-web_{context}"]
= Creating a primary cluster-scoped user-defined network by using the web console

[role="_abstract"]
You can connect multiple namespaces to the same primary user-defined network (UDN) by creating a `ClusterUserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

.Prerequisites
* You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

.Procedure
. From the *Administrator* perspective, click *Networking* -> *UserDefinedNetworks*.

. From the *Create* list, select *ClusterUserDefinedNetwork*.

. In the *Name* field, specify a name for the cluster-scoped UDN.

. Specify a value in the *Subnet* field.

. In the *Project(s) Match Labels* field, add the appropriate labels to select namespaces that the cluster UDN applies to.

. Click *Create*. The cluster-scoped UDN serves as the default primary network for pods and virtual machines located in namespaces that contain the labels that you specified in step 5.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-primary-udn-cli-intro_{context}"]
= Create a primary user-defined network by using the CLI

[role="_abstract"]
You can create a primary `UserDefinedNetwork` or `ClusterUserDefinedNetwork` custom resource definition (CRD) by using the {oc-first}. After you define the custom primary overlay network, you can create namespaces that are associated with the cluster-scoped UDN.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-udn-namespace-cli_{context}"]
= Creating a namespace for user-defined networks by using the CLI

[role="_abstract"]
You can create a namespace to be used with primary user-defined networks (UDNs) by using the {oc-first}.

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` permissions.
* You have installed the {oc-first}.

.Procedure

. Create a `Namespace` object as a YAML file similar to the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: my-namespace
  labels:
    k8s.ovn.org/primary-user-defined-network: ""
# ...
----
+
The `k8s.ovn.org/primary-user-defined-network` label is required for the namespace to be associated with a UDN. If the namespace is to be used with an existing cluster UDN, you must also add the appropriate labels that are defined in the `spec.namespaceSelector` field of the `ClusterUserDefinedNetwork` custom resource.

. Apply the `Namespace` manifest by running the following command:
+
[source, terminal]
----
$ oc apply -f <filename>.yaml
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-a-primary-udn_{context}"]
= Creating a primary namespace-scoped user-defined network by using the CLI

[role="_abstract"]
You can create an isolated primary network in your project namespace by using the CLI. You must use the OVN-Kubernetes layer 2 topology and enable persistent IP address allocation in the user-defined network (UDN) configuration to ensure VM live migration support.

.Prerequisites

* You have installed the {oc-first}.
* You have created a namespace and applied the `k8s.ovn.org/primary-user-defined-network` label.

.Procedure

. Create a `UserDefinedNetwork` object to specify the custom network configuration.
+
Example `UserDefinedNetwork` manifest:
+
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: UserDefinedNetwork
metadata:
  name: udn-l2-net
  namespace: my-namespace
spec:
  topology: Layer2
  layer2:
    role: Primary
    subnets:
      - "10.0.0.0/24"
      - "2001:db8::/60"
    ipam:
      lifecycle: Persistent
----
** `metadata.name` specifies the name of the `UserDefinedNetwork` custom resource.
** `metadata.namespace` specifies the namespace in which the VM is located. The namespace must have the `k8s.ovn.org/primary-user-defined-network` label. The namespace must not be `default`, an `openshift-*` namespace, or match any global namespaces that are defined by the Cluster Network Operator (CNO).
** `spec.topology` specifies the topological configuration of the network. The required value is `Layer2`. A `Layer2` topology creates a logical switch that is shared by all nodes.
** `spec.layer2.role` specifies whether the UDN is primary or secondary. The `Primary` role means that the UDN acts as the primary network for the VM and all default traffic passes through this network.
** `spec.layer2.ipam.lifecycle` specifies that virtual workloads have consistent IP addresses across reboots and migration. The `spec.layer2.subnets` field is required when `ipam.lifecycle: Persistent` is specified.

. Apply the `UserDefinedNetwork` manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f --validate=true <filename>.yaml
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-creating-a-primary-cluster-udn_{context}"]
= Creating a primary cluster-scoped user-defined network by using the CLI

[role="_abstract"]
You can connect multiple namespaces to the same primary user-defined network (UDN) to achieve native tenant isolation by using the CLI.

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` privileges.
* You have installed the {oc-first}.

.Procedure

. Create a `ClusterUserDefinedNetwork` object to specify the custom network configuration.
+
Example `ClusterUserDefinedNetwork` manifest:
+
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: ClusterUserDefinedNetwork
metadata:
  name: cudn-l2-net
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: In
      values: ["red-namespace", "blue-namespace"]
  network:
    topology: Layer2
    layer2:
      role: Primary
      ipam:
        lifecycle: Persistent
      subnets:
        - 203.203.0.0/16
----
** `metadata.name` specifies the name of the `ClusterUserDefinedNetwork` custom resource.
** `spec.namespaceSelector` specifies the set of namespaces that the cluster UDN applies to. The namespace selector must not point to `default`, an `openshift-*` namespace, or any global namespaces that are defined by the Cluster Network Operator (CNO).
** `spec.namespaceSelector.matchExpressions` specifies the type of selector. In this example, the `matchExpressions` selector selects objects that have the label `kubernetes.io/metadata.name` with the value `red-namespace` or `blue-namespace`.
** `spec.namespaceSelector.matchExpressions.operator` specifies the type of operator. Possible values are `In`, `NotIn`, and `Exists`.
** `spec.network.topology` specifies the topological configuration of the network. The required value is `Layer2`. A `Layer2` topology creates a logical switch that is shared by all nodes.
** `spec.network.layer2.role` specifies whether the UDN is primary or secondary. The `Primary` role means that the UDN acts as the primary network for the VM and all default traffic passes through this network.

. Apply the `ClusterUserDefinedNetwork` manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f --validate=true <filename>.yaml
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-attaching-vm-to-primary-udn-intro_{context}"]
= Attach a virtual machine to the primary user-defined network

[role="_abstract"]
You can connect a virtual machine (VM) to the primary user-defined network (UDN) by requesting the pod network attachment and configuring the interface binding.

{VirtProductName} supports the following network binding plugins to connect the network interface to the VM:

Layer 2 bridge:: The Layer 2 bridge binding creates a direct Layer 2 connection between the VM's virtual interface and the virtual switch of the UDN.

Passt:: The Plug a Simple Socket Transport (passt) binding provides a user-space networking solution that integrates seamlessly with the pod network, providing better integration with the OpenShift Container Platform networking ecosystem.
+
Passt binding has the following benefits:

* You can define readiness and liveness HTTP probes to configure VM health checks.
* You can use Red Hat Advanced Cluster Security to monitor TCP traffic within the cluster with detailed insights.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-attaching-vm-to-primary-udn-web_{context}"]
= Attaching a virtual machine to the primary user-defined network by using the web console

[role="_abstract"]
You can connect a virtual machine (VM) to the primary user-defined network (UDN) by using the OpenShift Container Platform web console. VMs that are created in a namespace where the primary UDN is configured are automatically attached to the UDN with the Layer 2 bridge network binding plugin.

To attach a VM to the primary UDN by using the Plug a Simple Socket Transport (passt) binding, enable the plugin and configure the VM network interface in the web console.

.Prerequisites
* You are logged in to the OpenShift Container Platform web console.

.Procedure
. Enable the passt network binding plugin Technology Preview feature:

.. Click *Virtualization* -> *Settings*.

.. Click *Preview features* and set *Enable Passt binding for primary user-defined networks* to on.

. Click *Virtualization* -> *VirtualMachines*.

. Click the *Virtual machines* tab.

. Select a VM to open the *VirtualMachine details* page.

. Click the *Configuration* tab.

. Click *Network*.

. Click the Options menu {kebab} on the *Network interfaces* page and select *Edit*.

. In the *Edit network interface* dialog, select the default pod network attachment from the *Network* list.

. Expand *Advanced* and then select the *Passt* binding.

. Click *Save*.

. If your VM is running, restart it for the changes to take effect.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-primary-udn.adoc

[id="virt-attaching-vm-to-primary-udn_{context}"]
= Attaching a virtual machine to the primary user-defined network by using the CLI

[role="_abstract"]
You can connect a virtual machine (VM) to the primary user-defined network (UDN) by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Edit the `VirtualMachine` manifest to add the UDN interface details, as in the following example:
+
Example `VirtualMachine` manifest:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
  namespace: my-namespace
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - name: udn-l2-net
              binding:
                name: l2bridge
# ...
      networks:
      - name: udn-l2-net
        pod: {}
# ...
----
** `metadata.namespace` specifies the namespace in which the VM is located. This value must match the namespace in which the UDN is defined.
** `spec.template.spec.domain.devices.interfaces.name` specifies the name of the user-defined network interface.
** `spec.template.spec.domain.devices.interfaces.binding.name` specifies the name of the binding plugin that is used to connect the interface to the VM. The possible values are `l2bridge` and `passt`. The default value is `l2bridge`.
** `spec.template.spec.networks.name` specifies the name of the network. This must match the value of the `spec.template.spec.domain.devices.interfaces.name` field.

. Optional: If you are using the Plug a Simple Socket Transport (passt) network binding plugin, set the `hco.kubevirt.io/deployPasstNetworkBinding` annotation to `true` in the `HyperConverged` custom resource (CR) by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc annotate {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} hco.kubevirt.io/deployPasstNetworkBinding=true --overwrite
----

. Apply the `VirtualMachine` manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

//Excluding from ROSA because the Networking -> Multiple networks -> Primary networks section is not part of ROSA docs
[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* About user-defined networks
