---
title: "Configuring and viewing IP addresses"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-viewing-ips-for-vms
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-viewing-ips-for-vms
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring and viewing IP addresses

[id="virt-configuring-viewing-ips-for-vms"]
= Configuring and viewing IP addresses

[role="_abstract"]
You can configure an IP address when you create a virtual machine (VM). The IP address is provisioned with cloud-init. View the IP address of a VM by using the OpenShift Container Platform web console or the command line. The network information is collected by the QEMU guest agent.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

[id="virt-configuring-ip-vm-web_{context}"]
= Configuring a static IP address when creating a virtual machine by using the web console

[role="_abstract"]
You can configure a static IP address when you create a virtual machine (VM) by using the web console. The IP address is provisioned with cloud-init.

[NOTE]
====
If the VM is connected to the pod network, the pod network interface is the default route unless you update it.
====

.Prerequisites

* The virtual machine is connected to a secondary network.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click a template tile.
. Click *Customize VirtualMachine*.
. Click *Next*.
. On the *Scripts* tab, click the edit icon beside *Cloud-init*.
. Select the *Add network data* checkbox.
. Enter the ethernet name, one or more IP addresses separated by commas, and the gateway address.
. Click *Apply*.
. Click *Create VirtualMachine*.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

[id="virt-configuring-ip-vm-cli_{context}"]
= Configuring an IP address when creating a virtual machine by using the CLI

[role="_abstract"]
You can configure a static or dynamic IP address when you create a virtual machine (VM). The IP address is provisioned with cloud-init.

[NOTE]
====
If the VM is connected to the pod network, the pod network interface is the default route unless you update it.
====

.Prerequisites

* The virtual machine is connected to a secondary network.
* You have a DHCP server available on the secondary network to configure a dynamic IP for the virtual machine.

.Procedure

* Edit the `spec.template.spec.volumes.cloudInitNoCloud.networkData` stanza of the virtual machine configuration:

** To configure a dynamic IP address, specify the interface name and enable DHCP:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <interface_name>
  kind: VirtualMachine
spec:
# ...
  template:
  # ...
    spec:
      volumes:
      - cloudInitNoCloud:
          networkData: |
            version: 2
            ethernets:
              eth1:
                dhcp4: true
    # ...
----

** To configure a static IP, specify the interface name and the IP address:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <interface_name>
  kind: VirtualMachine
spec:
# ...
  template:
  # ...
    spec:
      volumes:
      - cloudInitNoCloud:
          networkData: |
            version: 2
            ethernets:
              eth1:
                addresses:
                - 10.10.10.14/24
    # ...
----

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

[id="virt-viewing-vmi-ip-web_{context}"]
= Viewing the IP address of a virtual machine by using the web console

[role="_abstract"]
You can view the IP address of a virtual machine (VM) by using the OpenShift Container Platform web console.

[NOTE]
====
You must install the QEMU guest agent on a VM to view the IP address of a secondary network interface. A pod network interface does not require the QEMU guest agent.
====

.Procedure

. In the OpenShift Container Platform console, click *Virtualization* -> *VirtualMachines* from the side menu.
. Select a VM to open the *VirtualMachine details* page.
. Click the *Details* tab to view the IP address.

// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

[id="virt-viewing-vmi-ip-cli_{context}"]
= Viewing the IP address of a virtual machine by using the CLI

[role="_abstract"]
You can view the IP address of a virtual machine (VM) by using the command line.

[NOTE]
====
You must install the QEMU guest agent on a VM to view the IP address of a secondary network interface. A pod network interface does not require the QEMU guest agent.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Obtain the virtual machine instance configuration by running the following command:
+
[source,terminal]
----
$ oc describe vmi <vmi_name>
----
+
Example output:
+
[source,yaml]
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
   Interface Name:  v2
   Ip Address:      1.1.1.7/24
   Ip Addresses:
     1.1.1.7/24
     fe80::f4d9:70ff:fe13:9089/64
   Mac:             f6:d9:70:13:90:89
   Interface Name:  v1
   Ip Address:      1.1.1.1/24
   Ip Addresses:
     1.1.1.1/24
     1.1.1.2/24
     1.1.1.4/24
     2001:de7:0:f101::1/64
     2001:db8:0:f101::1/64
     fe80::1420:84ff:fe10:17aa/64
   Mac:             16:20:84:10:17:aa
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Installing the QEMU guest agent
