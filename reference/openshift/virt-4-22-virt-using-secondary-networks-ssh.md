---
title: "Use a secondary network for SSH access"
type: reference
domain: openshift
slug: virt-4-22-virt-using-secondary-networks-ssh
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-secondary-networks-ssh
version: 4.22
family: virt
documentKind: "Documentation"
---

# Use a secondary network for SSH access

[id="virt-using-secondary-networks-ssh"]
= Use a secondary network for SSH access

[role="_abstract"]
You can configure a secondary network, attach a virtual machine (VM) to the secondary network interface, and connect to the DHCP-allocated IP address by using SSH.

[IMPORTANT]
====
Secondary networks provide excellent performance because the traffic is not handled by the cluster network stack. However, the VMs are exposed directly to the secondary network and are not protected by firewalls. If a VM is compromised, an intruder could gain access to the secondary network. You must configure appropriate security within the operating system of the VM if you use this method.
====

For additional information about networking options, see the Multus and SR-IOV documentation in the "{VirtProductName} Tuning & Scaling Guide".

[NOTE]
====
You can also access a VM attached to a secondary network interface by using the cluster FQDN.
====

[id="prerequisites_{context}"]
== Prerequisites

* You configured a secondary network such as Linux bridge or SR-IOV.
* You created a network attachment definition for a Linux bridge network or the SR-IOV Network Operator created a network attachment definition when you created an `SriovNetwork` object.
* You configured a secondary network.
* You created a network attachment definition.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/managing_vms/ssh/virt-using-secondary-networks-ssh.adoc

[id="virt-vm-creating-nic-web_{context}"]
= Configuring a VM network interface by using the web console

[role="_abstract"]
You can configure a network interface for a virtual machine (VM) by using the OpenShift Container Platform web console.

.Prerequisites

* You created a network attachment definition for the network.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Click a VM to view the *VirtualMachine details* page.
. On the *Configuration* tab, click the *Network interfaces* tab.
. Click *Add network interface*.
. Enter the interface name and select the network attachment definition from the *Network* list.
. Click *Save*.
. Restart or live migrate the VM to apply the changes.

// Module included in the following assemblies:
//
// * virt/managing_vms/ssh/virt-using-secondary-networks-ssh.adoc

[id="virt-connecting-secondary-network-ssh_{context}"]
= Connecting to a VM attached to a secondary network by using SSH

[role="_abstract"]
You can connect to a virtual machine (VM) attached to a secondary network by using SSH.

.Prerequisites

* You attached a VM to a secondary network with a DHCP server.
* You have an SSH client installed.
* You have installed the {oc-first}.

.Procedure

. Obtain the IP address of the VM by running the following command:
+
[source,terminal]
----
$ oc describe vm <vm_name> -n <namespace>
----
+
Example output:
+
[source,terminal]
----
# ...
Interfaces:
  Interface Name:  eth0
  Ip Address:      10.244.0.37/24
  Ip Addresses:
    10.244.0.37/24
    fe80::858:aff:fef4:25/64
  Mac:             0a:58:0a:f4:00:25
  Name:            default
# ...
----

. Connect to the VM by running the following command:
+
[source,terminal]
----
$ ssh <user_name>@<ip_address> -i <ssh_key>
----
+
Example command:
+
[source,terminal]
----
$ ssh cloud-user@10.244.0.37 -i ~/.ssh/id_rsa_cloud-user
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
