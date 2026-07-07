---
title: "Update VirtIO drivers"
type: reference
domain: openshift
slug: virt-4-22-virt-update-virtio-drivers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-update-virtio-drivers
version: 4.22
family: virt
documentKind: "Documentation"
---

# Update VirtIO drivers

[id="virt-update-virtio-drivers"]
= Update VirtIO drivers

[role="_abstract"]
Update VirtIO drivers in guest operating systems. Using the latest VirtIO drivers increases performance and stability.

// Module included in the following assemblies:
//
// * virt/managing_vms/virt-update-virtio-drivers.adoc

[id="virt-updating-red-hat-virtio-drivers-windows_{context}"]
= Enable automatic updates for Red{nbsp}Hat virtio-win drivers

[role="_abstract"]
If the Windows Update service (WUS) is restricted to allow only drivers explicitly signed and published by Microsoft, automatic Red{nbsp}Hat `virtio-win` driver updates are disabled. You must manually complete the required configuration steps to enable automatic updates for Red{nbsp}Hat `virtio-win` drivers on a Windows virtual machine (VM).

.Prerequisites

* The cluster must have internet connectivity. Disconnected clusters cannot reach the WUS.

.Procedure

. Import the Red Hat Release Certificate into the Trusted Publishers store.
+
Example command:
+
[source,powershell]
----
Import-Certificate -FilePath "redhat-driver-cert.cer" -CertStoreLocation Cert:\LocalMachine\TrustedPublisher
----

. In the Group Policy Management Console (GPMC):

.. Set the `Allow signed updates from an intranet Microsoft update service location` policy to `Enabled`.
+
If a driver is signed by a certificate in the Trusted Publishers store, it is now accepted, even if it didn't come from Microsoft directly.

.. Set the `Do not include drivers with Windows Updates` policy to `Disabled`.
// Module included in the following assemblies:
//
// * virt/managing_vms/virt-update-virtio-drivers.adoc

[id="virt-updating-virtio-drivers-windows_{context}"]
= Update VirtIO drivers on a Windows VM

[role="_abstract"]
You can update the VirtIO drivers on a Windows virtual machine (VM) by using the Windows Update service (WUS).

[IMPORTANT]
====
If you restrict the WUS to only allow drivers explicitly signed and published by Microsoft, automatic Red{nbsp}Hat `virtio-win` driver updates are disabled. For information about enabling automatic Red{nbsp}Hat VirtIO driver updates, see "Enable automatic updates for Red{nbsp}Hat virtio-win drivers".
====

.Prerequisites

* The cluster must have internet connectivity. Disconnected clusters cannot reach the WUS.

.Procedure

. In the Windows Guest operating system, click the *Windows* key and select *Settings*.
. Navigate to *Windows Update* -> *Advanced Options* -> *Optional Updates*.
. Install all updates from *Red Hat, Inc.*.
. Reboot the VM.

.Verification

. On the Windows VM, navigate to the *Device Manager*.
. Select a device.
. Select the *Driver* tab.
. Click *Driver Details* and confirm that the `virtio` driver details displays the correct version.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Allow signed updates from an intranet Microsoft update service location
* Do not include drivers with Windows Updates
