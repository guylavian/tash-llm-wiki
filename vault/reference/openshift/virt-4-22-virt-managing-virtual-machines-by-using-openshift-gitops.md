---
title: "Managing virtual machines by using OpenShift GitOps"
type: reference
domain: openshift
slug: virt-4-22-virt-managing-virtual-machines-by-using-openshift-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-managing-virtual-machines-by-using-openshift-gitops
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing virtual machines by using OpenShift GitOps

// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management

[id="virt-managing-virtual-machines-by-using-openshift-gitops_{context}"]
= Managing virtual machines by using OpenShift GitOps

[role="_abstract"]
To automate and optimize virtual machine (VM) management in {VirtProductName}, you can use Red{nbsp}Hat OpenShift GitOps.

With GitOps, you can set up VM deployments based on configuration files stored in a Git repository. This also makes it easier to automate, update, or replicate these configurations, as well to use version control for tracking their changes.

.Prerequisites

* You have a GitHub account. For instructions to set up an account, see Creating an account on GitHub.

* OpenShift Virtualuzation has been installed on your OpenShift cluster. For instructions, see OpenShift Virtualization installation.

* The OpenShift GitOps operator has been installed on your OpenShift cluster. For instructions, see Installing GitOps.

.Procedure

Follow the _Manage OpenShift virtual machines with GitOps_ learning path in performing these steps:

. Connect an external Git repository to your Argo CD instance.

. Create the required VM configuration in the Git repository.

. Use the VM configuration to create VMs on your cluster.

[role="_additional-resources"]
.Additional resources
* OpenShift GitOps documentation
