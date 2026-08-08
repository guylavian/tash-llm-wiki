---
title: "Creating primary networks using a NetworkAttachmentDefinition"
type: reference
domain: openshift
slug: networking-4-22-about-primary-nwt-nad
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/about-primary-nwt-nad
version: 4.22
family: networking
documentKind: "Documentation"
---

# Creating primary networks using a NetworkAttachmentDefinition

[id="about-primary-nwt-nad"]
= Creating primary networks using a NetworkAttachmentDefinition

[role="_abstract"]
Use the `NetworkAttachmentDefinition` (NAD) resource to create primary networks when you need to use CNI plugins other than OVN-Kubernetes, such as IPVLAN or MACVLAN, or when you require direct control over the Container Network Interface (CNI) configuration for advanced networking scenarios.

// Module included in the following assemblies:
//
// * networking/multiple_networks/creating-primary-nad.adoc

[id="approaches-managing-additional-network_{context}"]
= Approaches to managing a primary network

[role="_abstract"]
You can manage the life cycle of a primary network created by a NAD CR through the Cluster Network Operator (CNO) or a YAML manifest. Using the CNO provides automated management of the network resource, while applying a YAML manifest allows for direct control over the network configuration.

Modifying the Cluster Network Operator (CNO) configuration:: With this method, the CNO automatically creates and manages the `NetworkAttachmentDefinition` object. In addition to managing the object lifecycle, the CNO ensures that a DHCP is available for a primary network that uses a DHCP assigned IP address.

Applying a YAML manifest:: With this method, you can manage the primary network directly by creating an `NetworkAttachmentDefinition` object. This approach allows for the invocation of multiple CNI plugins in order to attach primary network interfaces in a pod.

Each approach is mutually exclusive and you can only use one approach for managing a primary network at a time. For either approach, the primary network is managed by a Container Network Interface (CNI) plugin that you configure.

[NOTE]
====
When deploying OpenShift Container Platform nodes with multiple network interfaces on {rh-openstack-first} with OVN SDN, DNS configuration of the secondary interface might take precedence over the DNS configuration of the primary interface. In this case, remove the DNS nameservers for the subnet ID that is attached to the secondary interface by running the following command:

[source,terminal]
----
$ openstack subnet set --dns-nameserver 0.0.0.0 <subnet_id>
----
====

// Module included in the following assemblies:
//
// * networking/multiple_networks/primary_networks/about-primary-nwt-nad.adoc

[id="nw-multus-create-network_{context}"]
= Creating a primary network attachment with the Cluster Network Operator

[role="_abstract"]
When you specify a primary network to create by using the Cluster Network Operator (CNO), the (CNO) creates the `NetworkAttachmentDefinition` custom resource definition (CRD) automatically and manages it.

[IMPORTANT]
====
Do not edit the `NetworkAttachmentDefinition` CRDs that the Cluster Network Operator manages. Doing so might disrupt network traffic on your primary network.
====

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Optional: Create the namespace for the primary networks:
+
[source,terminal]
----
$ oc create namespace <namespace_name>
----

. To edit the CNO configuration, enter the following command:
+
[source,terminal]
----
$ oc edit networks.operator.openshift.io cluster
----

. Modify the CR that you are creating by adding the configuration for the primary network that you are creating, as in the following example CR.
+
[source,yaml,subs="attributes+"]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  # ...
  additionalNetworks:
  - name: tertiary-net
    namespace: namespace2
    type: Raw
    rawCNIConfig: |-
      {
        "cniVersion": "0.3.1",
        "name": "tertiary-net",
        "type": "ipvlan",
        "master": "eth1",
        "mode": "l2",
        "ipam": {
          "type": "static",
          "addresses": [
            {
              "address": "192.168.1.23/24"
            }
          ]
        }
      }
----

. Save your changes and quit the text editor to commit your changes.

.Verification

* Confirm that the CNO created the `NetworkAttachmentDefinition` CRD by running the following command. A delay might exist before the CNO creates the CRD. The expected output shows the name of the NAD CRD and the creation age in minutes.
+
[source,terminal]
----
$ oc get network-attachment-definitions -n <namespace>
----
+
--
where:

`<namespace>`:: Specifies the namespace for the network attachment that you added to the CNO configuration.
--

// Module included in the following assemblies:
//
// * networking/multiple_networks/creating-primary-nad.adoc

[id="nw-nad-cr_{context}"]
= Configuration for a primary network attachment

[role="_abstract"]
You configure a primary network by using the `NetworkAttachmentDefinition` API in the `k8s.cni.cncf.io` API group.

The configuration for the API is described in the following table:

.`NetworkAttachmentDefinition` API fields
[cols=".^3,.^2,.^5",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name for the primary network.

|`metadata.namespace`
|`string`
|The namespace that the object is associated with.

|`spec.config`
|`string`
|The CNI plugin configuration in JSON format.

|====

// Module included in the following assemblies:
//
// * networking/multiple_networks/primary_networks/about-primary-nwt-nad.adoc

[id="nw-multus-create-network-apply_{context}"]
= Creating a primary network attachment by applying a YAML manifest

[role="_abstract"]
Create a primary network attachment by directly applying a `NetworkAttachmentDefinition` YAML manifest. This gives you full control over the network configuration without relying on the Cluster Network Operator to manage the resource automatically.

.Prerequisites

* You have installed the {oc-first}.
* You have logged in as a user with `cluster-admin` privileges.
* You are working in the namespace where the NAD is to be deployed.

.Procedure

. Create a YAML file with your primary network configuration, such as in the following example:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: next-net
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "name": "work-network",
      "namespace": "namespace2",
      "type": "host-device",
      "device": "eth1",
      "ipam": {
        "type": "dhcp"
      }
    }
----
+
.. Optional: You can specify a namespace to which the NAD is applied. If you are working in the namespace where the NAD is to be deployed, the `namespace` specification is not necessary.

. To create the primary network, enter the following command:
+
[source,terminal]
----
$ oc apply -f <file>.yaml
----
+
--
where:

`<file>`:: Specifies the name of the file contained the YAML manifest.
--
