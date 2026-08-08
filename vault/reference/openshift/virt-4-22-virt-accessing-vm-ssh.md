---
title: "SSH access for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-accessing-vm-ssh
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-accessing-vm-ssh
version: 4.22
family: virt
documentKind: "Documentation"
---

# SSH access for virtual machines

[id="virt-accessing-vm-ssh"]
= SSH access for virtual machines

[role="_abstract"]
You can use SSH to securely access your virtual machines (VMs) from the command line. To set up your SSH configuration, use one of the following methods:

* `virtctl ssh` command
* `virtctl port-forward` command
* Service
* Secondary network

// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

[id="virt-access-configuration-considerations_{context}"]
= Access configuration considerations

[role="_abstract"]
Each method for configuring access to a virtual machine (VM) has advantages and limitations, depending on the traffic load and client requirements.

[NOTE]
====
Services provide excellent performance and are recommended for applications that are accessed from outside the cluster.
====

If the internal cluster network cannot handle the traffic load, you can configure a secondary network.

`virtctl ssh` and `virtctl port-forwarding` commands::
* Simple to configure.
* Recommended for troubleshooting VMs.
* `virtctl port-forwarding` recommended for automated configuration of VMs with Ansible.
* Dynamic public SSH keys can be used to provision VMs with Ansible.
* Not recommended for high-traffic applications like Rsync or Remote Desktop Protocol because of the burden on the API server.
* The API server must be able to handle the traffic load.
* The clients must be able to access the API server.
* The clients must have access credentials for the cluster.

Cluster IP service::
* The internal cluster network must be able to handle the traffic load.
* The clients must be able to access an internal cluster IP address.

Node port service::
* The internal cluster network must be able to handle the traffic load.
* The clients must be able to access at least one node.

Load balancer service::
* A load balancer must be configured.
* Each node must be able to handle the traffic load of one or more load balancer services.

Secondary network::
* Excellent performance because traffic does not go through the internal cluster network.
* Allows a flexible approach to network topology.
* Guest operating system must be configured with appropriate security because the VM is exposed directly to the secondary network. If a VM is compromised, an intruder could gain access to the secondary network.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* {VirtProductName} Tuning & Scaling Guide
* Connecting a virtual machine to a Linux bridge network
* Connecting a virtual machine to an SR-IOV network
* Creating a Linux bridge NAD by using the web console
* Configuring SR-IOV additional network
* Accessing a virtual machine by using its external FQDN
* Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network
