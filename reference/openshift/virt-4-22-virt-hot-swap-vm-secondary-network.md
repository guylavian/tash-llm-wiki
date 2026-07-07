---
title: "Hot swapping a virtual machine secondary network"
type: reference
domain: openshift
slug: virt-4-22-virt-hot-swap-vm-secondary-network
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-hot-swap-vm-secondary-network
version: 4.22
family: virt
documentKind: "Documentation"
---

# Hot swapping a virtual machine secondary network

[id="virt-hot-swap-vm-secondary-network"]
= Hot swapping a virtual machine secondary network

[role="_abstract"]
You can change the secondary network of a virtual machine (VM) without rebooting your VM. The change is transparent to the guest operating system, preserving properties like the MAC address.

By hot swapping the secondary network, you can move a running VM to a different network segment or VLAN and apply new network policies or reconfigure network topology without interrupting the workload. {VirtProductName} supports hot swapping for VMs that are connected to an OVN-Kubernetes localnet and a Linux bridge secondary network.

To hot swap a VM secondary network, you must edit the network configuration of the running VM to refer to a new `NetworkAttachmentDefinition` or `ClusterUserDefinedNetwork` manifest. This action triggers a live migration, connecting the VM to the new network without a reboot.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-hot-swap-vm-secondary-network.adoc

[id="virt-vm-nw-hot-swap-limitations_{context}"]
= Hot swap limitations

[role="_abstract"]
{VirtProductName} supports hot swapping for VMs that are connected to an OVN-Kubernetes localnet and a Linux bridge secondary network.

Consider the following limitations before hot swapping a VM secondary network:

* Hot swapping only works for VMs that are live migratable.
* Network connectivity might be interrupted during the live migration process.
* If you update network references for multiple VMs, the updates might be queued because only a limited number of live migrations can run in parallel across the cluster.
* You cannot hot swap to a new network binding type or a Container Network Interface (CNI) plugin. For example, you cannot change from bridge binding to SR-IOV binding.
* The target `NetworkAttachmentDefinition` and `ClusterUserDefinedNetwork` objects must be valid and all referenced resources such as bridges, VLANs, and network resources must exist. Migration completes even if the network configuration is invalid, but the VM will lose network connectivity.
* This feature applies only to secondary networks attached by using `NetworkAttachmentDefinition` or `ClusterUserDefinedNetwork` manifests. You cannot hot swap the primary pod network, regardless of whether it uses the default cluster network or a custom primary user-defined network.
* If the new network requires a different IP configuration, such as a different subnet or gateway, you must reconfigure the guest operating system network settings. The hot swap does not automatically update the guest network configuration.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-hot-swap-vm-secondary-network.adoc

[id="virt-live-updating-vm-nad-udn_{context}"]
= Hot swapping a virtual machine secondary network by using the command line

[role="_abstract"]
You can hot swap a virtual machine (VM) secondary network by using the command line.

.Prerequisites
* The VM to which you want to hot swap the network is running and is live migratable.
* You have installed the {oc-first}.
* The target `NetworkAttachmentDefinition` object exists in the same namespace as the VM. If you created a `ClusterUserDefinedNetwork` object, verify that the cluster user-defined network controller has created the corresponding `NetworkAttachmentDefinition` object.
+
Example `NetworkAttachmentDefinition` manifest:
+
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: nad-with-vlan20
spec:
  config: '{
    "cniVersion": "0.3.1",
    "name": "nad-with-vlan20",
    "type": "bridge",
    "bridge": "br2",
    "vlan": 20
  }'
----

.Procedure
. Use your preferred text editor to edit the `VirtualMachine` manifest, as shown in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
...
  template:
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: bridge-net
      networks:
      - name: bridge-net
        multus:
          networkName: nad-with-vlan20
#...
----
** `spec.networks.name` specifies the name of the network. This must be the same as the `name` of the new network interface that you defined in the `template.spec.domain.devices.interfaces` list.
** `spec.networks.multus.networkName` specifies the name of the target `NetworkAttachmentDefinition` object.

. Save your changes and exit the editor.
. For the new configuration to take effect, apply the changes by running the following command. If your OpenShift Container Platform cluster has live migration enabled, applying the changes triggers automatic VM live migration and connects the new network to the running VM.
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
+
where:

`<filename>`:: Specifies the name of your `VirtualMachine` manifest YAML file.

.Verification
. Verify that the VM live migration is progressing successfully by using the following command.
+
[source,terminal]
----
$ oc get vmi vm-fedora -w -o jsonpath='{.status.conditions[?(@.type=="MigrationRequired")]}{"\n"}'
----
+
Example output:
+
[source,terminal]
----
{"type":"MigrationRequired","status":"True","lastProbeTime":null,"lastTransitionTime":"2024-05-27T10:15:30Z","reason":"AutoMigrationDueToLiveUpdate","message":""}
----

. Use the following command to connect to the VM console and to devices on the new network:
+
[source,terminal]
----
$ virtctl console vm-fedora
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* About live migration
* Connecting a virtual machine to a secondary localnet user-defined network
* Creating a Linux bridge network attachment definition
* Creating an SR-IOV network attachment definition
