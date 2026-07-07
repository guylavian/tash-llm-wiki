---
title: "Managing the link state of a virtual machine interface"
type: reference
domain: openshift
slug: virt-4-22-virt-setting-interface-link-state
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-setting-interface-link-state
version: 4.22
family: virt
documentKind: "Documentation"
---

# Managing the link state of a virtual machine interface

[id="virt-setting-interface-link-state"]
= Managing the link state of a virtual machine interface

[role="_abstract"]
You can manage the link state of a primary or secondary virtual machine (VM) interface by using the OpenShift Container Platform web console or the CLI. By specifying the link state, you can logically connect or disconnect the virtual network interface controller (vNIC) from a network.

[NOTE]
====
{VirtProductName} does not support link state management for Single Root I/O Virtualization (SR-IOV) secondary network interfaces and their link states are not reported.
====

You can specify the desired link state when you first create a VM, by editing the configuration of an existing VM that is stopped or running, or when you hot plug a new network interface to a running VM. If you edit a running VM, you do not need to restart or migrate the VM for the changes to be applied. The current link state of a VM interface is reported in the `status.interfaces.linkState` field of the `VirtualMachineInstance` manifest.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-setting-interface-link-state.adoc

[id="virt-configuring-interface-link-state-web_{context}"]
= Setting the VM interface link state by using the web console

[role="_abstract"]
You can set the link state of a primary or secondary virtual machine (VM) network interface by using the web console.

.Prerequisites
* You are logged into the OpenShift Container Platform web console.

.Procedure
. Navigate to *Virtualization* -> *VirtualMachines*.

. Select a VM to view the *VirtualMachine details* page.

. On the *Configuration* tab, click *Network*. A list of network interfaces is displayed.

. Click the Options menu {kebab} of the interface that you want to edit.

. Choose the appropriate option to set the interface link state:
** If the current interface link state is `up`, select *Set link down*.
** If the current interface link state is `down`, select *Set link up*.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-setting-interface-link-state.adoc

[id="virt-configuring-interface-link-state_{context}"]
= Setting the VM interface link state by using the CLI

[role="_abstract"]
You can set the link state of a primary or secondary virtual machine (VM) network interface by using the CLI.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).

.Procedure
. Edit the VM configuration to set the interface link state, as in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: my-vm
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
            - name: default
              state: down
              masquerade: { }
      networks:
        - name: default
          pod: { }
# ...
----
+
* `spec.template.spec.domain.devices.interfaces.name` defines the name of the interface.
* `spec.template.spec.domain.devices.interfaces.state` defines the state of the interface. The possible values are:
+
** `up`: Represents an active network connection. This is the default if no value is specified.
** `down`: Represents a network interface link that is switched off.
** `absent`: Represents a network interface that is hot unplugged.
+
[IMPORTANT]
====
If you have defined readiness or liveness probes to run VM health checks, setting the primary interface's link state to `down` causes the probes to fail. If a liveness probe fails, the VM is deleted and a new VM is created to restore responsiveness.
====

. Apply the `VirtualMachine` manifest:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Verification
* Verify that the desired link state is set by checking the `status.interfaces.linkState` field of the `VirtualMachineInstance` manifest.
+
[source,terminal]
----
$ oc get vmi <vmi-name>
----
+
Example output:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  name: my-vm
spec:
  domain:
    devices:
      interfaces:
      - name: default
        state: down
        masquerade: { }
  networks:
  - name: default
    pod: { }
status:
  interfaces:
    - name: default
      linkState: down
# ...
----
