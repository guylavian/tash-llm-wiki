---
title: "Managing MAC address pools for network interfaces"
type: reference
domain: openshift
slug: virt-4-22-virt-using-mac-address-pool-for-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-using-mac-address-pool-for-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing MAC address pools for network interfaces

[id="virt-using-mac-address-pool-for-vms"]
= Managing MAC address pools for network interfaces

[role="_abstract"]
KubeMacPool allocates MAC addresses for virtual machine (VM) network interfaces from a shared MAC address pool. This ensures that each network interface is assigned a unique MAC address.

A virtual machine instance created from that VM retains the assigned MAC address across reboots.

[NOTE]
====
KubeMacPool does not handle virtual machine instances created independently from a virtual machine.
====

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-mac-address-pool-for-vms.adoc

[id="virt-managing-kubemacpool-cli_{context}"]
= Managing KubeMacPool by using the CLI

[role="_abstract"]
You can disable and re-enable KubeMacPool by using the command line.

KubeMacPool is enabled by default.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* To disable KubeMacPool in two namespaces, run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace1> <namespace2> mutatevirtualmachines.kubemacpool.io=ignore
----

* To re-enable KubeMacPool in two namespaces, run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace1> <namespace2> mutatevirtualmachines.kubemacpool.io-
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-mac-address-pool-for-vms.adoc

[id="virt-custom-kubemacpool-range_{context}"]
= Customizing the MAC pool range

[role="_abstract"]
KubeMacPool works by allocating MAC addresses to VMs from a range. The `rangeStart` and `rangeEnd` parameters in the `HyperConverged` custom resource (CR) define the MAC pool range.

As a cluster administrator, you can configure this range to ensure that MAC addresses for VMs hosted on {VirtProductName} do not conflict with other virtualization solutions on the same network.

.Prerequisites

* You have cluster administrator access on an OpenShift Container Platform cluster.
* You have installed the {oc-first}.

.Procedure

. Edit the `HyperConverged` CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Update the `HyperConverged` CR to configure the `rangeStart` and `rangeEnd` parameters that define your required MAC address range:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  kubeMacPoolConfiguration:
    rangeStart: "AA:00:00:00:00:00"
    rangeEnd: "FD:FF:FF:FF:FF:FF"
# ...
----

.Verification

. Run the following command and observe the output:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} -o=jsonpath='{.spec.kubeMacPoolConfiguration}'
----
+
If you have successfully applied the configuration changes, the output shows the new MAC pool range you have configured:
+
Example output:
+
[source,terminal]
----
{
  "rangeStart": "AA:00:00:00:00:00",
  "rangeEnd": "FD:FF:FF:FF:FF:FF"
}
----

. Optional. Create a new VM and run the following command to check the MAC address of the VM's network interface:
+
[source,terminal]
----
$ oc get vmi <vm-name> -o=jsonpath='{.status.interfaces[0].macAddress}'
----
+
Example output:
+
[source,yaml]
----
macAddress: AA:00:00:00:00:04
----
+
If you have successfully applied the configuration changes, the `macAddress` field in the VM interface is within the range you specified in your `kubeMacPoolConfiguration`, between the value of `rangeStart` and `rangeEnd`.
