---
title: "About high availability for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-high-availability-for-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-high-availability-for-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# About high availability for virtual machines

[id="virt-high-availability-for-vms"]
= About high availability for virtual machines

// Hiding manual delete item as not supported
[role="_abstract"]
You can enable high availability for virtual machines (VMs) by manually deleting a failed node to trigger VM failover or by configuring remediating nodes.

Manually deleting a failed node:: If a node fails and machine health checks are not deployed on your cluster, virtual machines with `runStrategy: Always` configured are not automatically relocated to healthy nodes. To trigger VM failover, you must manually delete the `Node` object.

Configuring remediating nodes::
You can enable high availability for virtual machines (VMs) by configuring remediating nodes.

You can configure remediating nodes by installing the Self Node Remediation Operator or the Fence Agents Remediation Operator from the software catalog and enabling machine health checks or node remediation checks.

For more information on remediation, fencing, and maintaining nodes, see the "Workload Availability for Red Hat OpenShift" documentation.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Workload Availability for Red Hat OpenShift
* Delete a failed node to trigger virtual machine failover
