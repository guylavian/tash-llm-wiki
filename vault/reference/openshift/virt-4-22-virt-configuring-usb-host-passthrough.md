---
title: "Configuring USB host passthrough"
type: reference
domain: openshift
slug: virt-4-22-virt-configuring-usb-host-passthrough
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-configuring-usb-host-passthrough
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring USB host passthrough

[id="virt-configuring-usb-host-passthrough"]
= Configuring USB host passthrough

[role="_abstract"]
As a cluster administrator, you can expose USB devices in a cluster, which makes the devices available for virtual machine (VM) owners to assign to VMs. Enabling this passthrough of USB devices allows a VM to connect to USB hardware that is attached to an OpenShift Container Platform node, as if the hardware and the VM are physically connected.

To expose a USB device, first enable host passthrough and then configure the VM to use the USB device.

// Module included in the following assemblies:
//
// * virt/advanced_vm_management/virt-configuring-usb-host-passthrough.adoc

[id="virt-enabling-usb-host-passthrough_{context}"]
= Enabling USB host passthrough

[role="_abstract"]
To attach a USB device to a virtual machine (VM), you must first enable USB host passthrough at the cluster level.

To do this, specify a resource name and USB device name for each device you want first to add and then assign to a VM. You can allocate more than one device, each of which is known as a `selector` in the `HyperConverged` custom resource (CR), to a single resource name. If you have multiple identical USB devices on the cluster, you can choose to allocate a VM to a specific device.

.Prerequisites

* You have access to an OpenShift Container Platform cluster as a user who has the `cluster-admin` role.
* You have installed the {oc-first}.

.Procedure

. Identify the USB device vendor and product:
+
[source,terminal]
----
$ lsusb
----
+
*Example output*
+
[source,terminal]
----
Bus 003 Device 007: ID 1b1c:0a60 example_manufacturer example_product_name
----

** If you cannot use the `lsusb` command, inspect the USB device configurations in the host's `/sys/bus/usb/devices/` directory:
+
[source,terminal]
----
for dev in *; do
    if [[ -f "$dev/idVendor" && -f "$dev/idProduct" ]]; then
        echo "Device: $dev"
        echo -n "  Manufacturer : "; cat "$dev/manufacturer"
        echo -n "  Product: "; cat "$dev/product"
        echo -n "  Vendor ID : "; cat "$dev/idVendor"
        echo -n "  Product ID: "; cat "$dev/idProduct"
        echo
    fi
done
----
+
*Example output*
+
[source,terminal]
----
Device: 3-7
  Manufacturer : example_manufacturer
  Product: example_product_name
  Vendor ID : 1b1c
  Product ID: 0a60
----

. Open the `HyperConverged` CR in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Add the required USB device to the `permittedHostDevices` stanza of the `HyperConvered` CR. The following example adds a device with vendor ID `045e` and product ID `07a5`:
+
[source,yaml,highlight=11..12,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
  permittedHostDevices:
    usbHostDevices:
    - resourceName: kubevirt.io/peripherals
      selectors:
      - vendor: "045e"
        product: "07a5"
      - vendor: "062a"
        product: "4102"
      - vendor: "072f"
        product: "b100"
----
+
* `spec.permittedHostDevices` defines the host devices that have permission to be used in the cluster.
* `spec.permittedHostDevices.usbHostDevices` defines a list of available USB devices.
* `spec.permittedHostDevices.usbHostDevices.resourceName` defines the USB device that you want to add and assign to the
  VM. In this example, the resource is bound to three devices, each of which is identified by `vendor` and `product` and
  is known as a `selector`.
// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-configuring-usb-host-passthrough.adoc

[id="virt-configuring-vm-use-usb-device_{context}"]
= Connecting a USB device to a virtual machine

[role="_abstract"]
You can configure virtual machine (VM) access to a USB device. This configuration enables the VM to connect to USB hardware that is attached to an OpenShift Container Platform node, as if the hardware and the VM are physically connected.

.Prerequisites

* You have installed the {oc-first}.
* You have attached the required USB device as a resource at the cluster level.

.Procedure

. In the `HyperConverged` custom resource (CR), find the assigned resource name of the USB device:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----
+
Example output:
+
[source, yaml]
----
# ...
  spec:
    permittedHostDevices:
      usbHostDevices:
        - resourceName: kubevirt.io/peripherals
          selectors:
            - vendor: "045e"
              product: "07a5"
            - vendor: "062a"
              product: "4102"
            - vendor: "072f"
              product: "b100"
----

. Open the VM CR:
+
[source,terminal]
----
$ oc edit vm <vm_name>
----
+
where:
+
`<vm_name>`:: Specifies the name of the `VirtualMachine` CR.

. Edit the CR by adding the USB device, as shown in the following example:
+
Example configuration:
+
[source, yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      architecture: amd64
      domain:
        devices:
          hostDevices:
          - deviceName: kubevirt.io/peripherals
            name: local-peripherals
# ...
----
+
* `spec.template.spec.domain.devices.hostDevices.deviceName` specifies the resource name from the `HyperConverged` CR.
* `spec.template.spec.domain.devices.hostDevices.name` defines the name of the USB device.

. Save and apply your changes:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
+
where:
+
`<filename>`:: Specifies the name of the `VirtualMachine` manifest YAML file.
