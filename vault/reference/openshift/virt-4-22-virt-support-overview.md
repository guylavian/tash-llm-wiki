---
title: "Support overview"
type: reference
domain: openshift
slug: virt-4-22-virt-support-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-support-overview
version: 4.22
family: virt
documentKind: "Documentation"
---

# Support overview

[id="virt-support-overview"]
= Support overview

[role="_abstract"]
Accelerate the resolution of cluster and virtual machine (VM) issues by using the integrated diagnostic tools and support provided by {VirtProductName}.

To gather debugging information, configure Prometheus and Alertmanager and collect `must-gather` data for OpenShift Container Platform and {VirtProductName}.

// Module included in the following assemblies:
//
// * virt/support/virt-support-overview.adoc

[id="virt-support-opening-case_{context}"]
= Opening a support case

[role="_abstract"]
Open a support case with Red{nbsp}Hat Support when you encounter an issue that requires immediate assistance.

// Module included in the following assemblies:
//
// * virt/support/virt-support-overview.adoc

[id="virt-support-collect-data_{context}"]
= Collecting data for Red{nbsp}Hat Support

[role="_abstract"]
Gather information about the issue affecting your environment to submit with your support case. This aids Red{nbsp}Hat Support in effectively diagnosing your issue.

Gather troubleshooting information by using the following tools:

* Configure Prometheus and Alertmanager.

// must-gather not supported for ROSA/OSD, per Dustin Row
* Configure and use the `must-gather` tool.
* Collect `must-gather` data and memory dumps from VMs.
* Collect `must-gather` data for OpenShift Container Platform and {VirtProductName}

// Module included in the following assemblies:
//
// * virt/support/virt-support-overview.adoc

[id="virt-support-submit-support-case_{context}"]
= Submitting a support case

[role="_abstract"]
Submit a support case to resolve a cluster issue that is affecting the ability of {VirtProductName} to function properly in your environment.

You can submit a support case to Red{nbsp}Hat Support by using the Customer Support page. Include data that you collected about your issue with your support request.

// Module included in the following assemblies:
//
// * virt/support/virt-support-overview.adoc

[id="virt-creating-jira-issue_{context}"]
= Creating a Jira issue

[role="_abstract"]
To report a bug, use the Red Hat Issue Router (RHIR), which is available in the Customer Portal Labs.

.Procedure

. Access the RHIR.

. In the list of all {VirtProductName} components, find the component for which you want to report an issue.

. Click the *Report a bug* link of the component.

. On the *Create issue* page, fill out the form:

.. Complete the *Summary* and *Description* fields. In the *Description* field, include a detailed description of the issue.

.. Submit any collected troubleshooting information:

... Add any textual troubleshooting information, such as command outputs, in the *Description* field.
... Add troubleshooting files using the *Attachment* field.

. Click *Create* at the bottom of the page.

. Review the details of the bug you created.

// Module included in the following assemblies:
//
// * virt/support/virt-support-overview.adoc

[id="virt-support-web-console-monitoring_{context}"]
= Web console monitoring

[role="_abstract"]
Monitor cluster and virtual machine (VM) health with the OpenShift Container Platform web console.

The OpenShift Container Platform web console displays resource usage, alerts, events, and trends for your cluster and for {VirtProductName} components and resources.

.Web console pages for monitoring and troubleshooting
[options="header"]
|====
|Page |Description

|*Virtualization* -> *VirtualMachines* -> *Overview* page
|Cluster details, status, alerts, inventory, and resource usage

|*Virtualization* -> *VirtualMachines* -> *Overview* -> *Overview* tab
|{VirtProductName} resources, usage, alerts, and status

|*Virtualization* -> *Migrations* page
|Progress of live migrations

|*Virtualization* -> *VirtualMachines* -> *Virtual machines* tab
|CPU, memory, and storage usage summary

|*Virtualization* -> *VirtualMachines* -> *Virtual machines* -> *VirtualMachine details* -> *Metrics* tab
|VM resource usage, storage, network, and migration

|*Virtualization* -> *VirtualMachines* -> *Virtual machines* -> *VirtualMachine details* -> *Events* tab
|List of VM events

|*Virtualization* -> *VirtualMachines* -> *Virtual machines* -> *VirtualMachine details* -> *Diagnostics* tab
|VM status conditions and volume snapshot status
|====

[role="_additional-resources"]
== Additional resources
* Submitting a support case
* Collecting data about your environment
* Using the `must-gather` tool for {VirtProductName}
* Red{nbsp}Hat Issue Router
* Red{nbsp}Hat Jira account
* Create issue
