---
title: "Using the Generic Device Plugin"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-gdp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-gdp
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Using the Generic Device Plugin

[id="microshift-gdp"]
= Using the Generic Device Plugin

[role="_abstract"]
The Generic Device Plugin (GDP) for {microshift-short} enables your containerized applications to securely access physical host devices, such as serial ports, video cameras, or sound cards directly from within Kubernetes pods. By using GDP, you can extend capabilities of {microshift-short} to support applications that require direct hardware interaction, such as Internet of Things (IoT) applications.

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-understanding-generic-device-plugin-con_{context}"]
= Understanding the Generic Device Plugin

[role="_abstract"]
The Generic Device Plugin in OpenShift Container Platform is a Kubernetes device plugin that enables pods to access host devices such as serial ports, cameras, and sound cards securely. You can use it for edge and IoT workloads that require direct hardware access without elevated container privileges.

The GDP integrates with the kubelet to advertise available devices to the node and facilitate their allocation to pods without requiring elevated privileges within the container itself. It is designed to handle devices that are initialized and managed by the operating system and do not require any special initialization procedures or drivers for a pod to use them.

Here are examples of generic devices that are suitable for the GDP:

* Serial ports, for example, `/dev/ttyUSB*`, `/dev/ttyACM*`.
* Video cameras, for example, `/dev/video0`.
* Sound devices, for example, `/dev/snd`, `/dev/snd/controlC0`.
* USB devices specified by Vendor ID and Product ID, or, optionally, by the device serial number.

The following specialized devices are not suitable for the GDP:

* Devices that require specific initialization procedures beyond standard operating system management.
* Specialized hardware that needs additional drivers or kernel modules. Examples of this specialized hardware include GPUs and FPGAs. These types of devices typically require their own specialized device plugins.

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-limitations-of-generic-device-plugin_{context}"]
= Limitations and considerations for the Generic Device Plugin

[role="_abstract"]
The Generic Device Plugin in OpenShift Container Platform has limitations and considerations for exposing host devices. You can use this information to choose suitable devices, configure stable identifiers, and plan for performance.

[id="microshift-devices-not-suited-generic-device-plugin_{context}"]
== Devices not suited for the Generic Device Plugin

The GDP is designed for devices that are managed directly by the operating system and do not require special setup procedures. Devices that are not well-suited for the Generic Device Plugin include:

* Complex hardware requiring specialized drivers such as GPUs (graphics processing units) or FPGAs (field-programmable gate arrays). These types of hardware typically require dedicated device plugins that can perform unique initialization procedures, memory management, or queue resets before a pod can use them.
* Devices with specific vendor-supplied software stacks. Devices that require a complex software stack or proprietary APIs beyond direct file system access might require a specialized plugin.

[id="microshift-device-id-logging-generic-device-plugin_{context}"]
== Device identification and logging

When you use glob paths, for example, `/dev/ttyUSB*`, to expose multiple similar devices, the GDP allocates devices based on availability. However, if your application needs to connect to an exactly specified physical device, for example, `serial device 3` out of 10, using broad glob paths might be insufficient. In such cases, configure individual device entries in the `config.yaml` file using more stable and unique identifiers such as:

* Specific device paths, for example, `/dev/video0`.
* Symbolic links provided by the operating system, for example, `/dev/serial/by-id/` or `/dev/serial/by-path/`.
* USB vendor ID, product ID, and serial number combinations for precise USB device targeting.

[id="microshift-performance-considerations-generic-device-plugin_{context}"]
== Performance considerations

The `count` parameter in the `config.yaml` file enables a device group to be scheduled multiple times concurrently. While there are no explicit limits set within the GDP for the count (for example, `1000` for `/dev/fuse`), the actual performance depends on the host system's capabilities and the nature of the device itself. Running a very high number of concurrent processes that access the same device might affect performance.

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-configuring-generic-device-plugin_{context}"]
= Configuring the Generic Device Plugin

[role="_abstract"]
The Generic Device Plugin (GDP) is disabled by default in {microshift-short}. To expose host devices such as serial ports and cameras to pods in OpenShift Container Platform, you can enable the Generic Device Plugin and define devices in the `config.yaml` file or create a configuration snippet file such as `/etc/microshift/config.d/10-gdp.yaml`.

.Prerequisites

* You installed {microshift-short}.
* You created a custom `config.yaml` file in the `/etc/microshift` directory.
* You installed the {oc-first}.
* You have `sudo` privileges on the {microshift-short} host.
* You have identified the specific host devices that you want to expose to your {microshift-short} node. For example, `/dev/video0`, `/dev/ttyUSB*`, or USB Vendor/Product IDs.

.Procedure

. From your CLI using `sudo` privileges, open `/etc/microshift/config.yaml` in a text editor.
+
. Locate the `genericDevicePlugin` section. If it is not present, add it.
+
. Set the `status` parameter to `Enabled` and define the `devices` that should be exposed. Each device definition needs a `name` and one or more `groups`. Each group can specify devices using `paths`, for file-based devices, including glob patterns, or `usbs`, for USB devices using Vendor/Product IDs. You cannot mix `paths` and `usbs` within the same device group.
+
.GDP fields with default values
[source,yaml]
----
apiServer:
# ...
genericDevicePlugin:
  devices:
  - groups:
    - paths:
      - path: /dev/ttyUSB*
      - path: /dev/ttyACM*
    name: serial
  - groups:
    - paths:
      - path: /dev/fuse
    name: fuse
  - groups:
    - usbs:
      - product: "0x7523"
        serial: ""
        vendor: "0x1a86"
    name: converter
  domain: device.microshift.io
  status: Enabled
----
+
where:
+
--
`/dev/ttyUSB*`:: Specifies the file path for all the USB serial devices that are matched by this glob.

`/dev/ttyACM*`:: Specifies the file path for all the ACM serial devices that are matched by this glob.

`/dev/fuse`:: Specifies the file path for a fuse device.

`fuse`:: Specifies the name of the device.

`0x7523`:: Specifies the Product ID for a CH340 serial converter.

`0x1a86`:: Specifies the Vendor ID for a CH340 serial converter.

`device.microshift.io`:: Specifies the default domain for the GDP.
--
+
[IMPORTANT]
====
* The output of the `microshift show-config` parameter might include pre-configured default paths for serial devices even if you have not explicitly configured them in `config.yaml`. These paths represent the default discovery settings if the Generic Device Plugin is enabled without specific user configuration.

* For consistency and precise device targeting, especially when dealing with multiple similar devices, consider using stable device paths like `/dev/serial/by-id/` or specific USB Vendor, Product, or Serial IDs instead of broad glob patterns like `/dev/ttyUSB*`.

* The `count` parameter in a device group allows a single device, or a set of devices matched by a glob, to be allocated multiple times concurrently to different pods. If omitted, `count` defaults to `1`.
====
+
. Save the `config.yaml` file.

. Restart the {microshift-short} service to apply the changes:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----
+
Allow some time for {microshift-short} to restart and for the GDP to register its devices with the Kubelet.

.Verification

* You can check the available devices in your node by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc describe node _<microshift_node_name>_ | grep "device.microshift.io"
----
+
* Depending on your configuration, expect output that indicates that the devices are now discoverable and schedulable within your {microshift-short} node.
+
.Example output
[source,terminal]
----
Capacity:
 cpu:                                2
 device.microshift.io/audio:         0
 device.microshift.io/capture:       0
 device.microshift.io/custom-device: 1
 device.microshift.io/dummy-video:   0
 device.microshift.io/fuse:          0
 device.microshift.io/serial:        5
 device.microshift.io/video:         0
Allocatable:
 cpu:                                2
 device.microshift.io/audio:         0
 device.microshift.io/capture:       0
 device.microshift.io/custom-device: 1
 device.microshift.io/dummy-video:   0
 device.microshift.io/fuse:          0
 device.microshift.io/serial:        5
 device.microshift.io/video:         0
Allocated resources:
 (Total limits may be over 100 percent, i.e., overcommitted.)
 Resource                           Requests     Limits
 --------                           --------     ------
 cpu                                450m (22%)   500m (25%)
 memory                             1550Mi (42%) 500Mi (13%)
 ephemeral-storage                  0 (0%)       0 (0%)
 hugepages-1Gi                      0 (0%)       0 (0%)
 hugepages-2Mi                      0 (0%)       0 (0%)
 device.microshift.io/audio         0            0
 device.microshift.io/capture       0            0
 device.microshift.io/custom-device 1            1
 device.microshift.io/dummy-video   1            1
 device.microshift.io/fuse          0            0
 device.microshift.io/serial        0            0
 device.microshift.io/video         0            0
----

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-deploying-applications-with-generic-devices_{context}"]
= Deploying applications that use generic devices

[role="_abstract"]
After the Generic Device Plugin (GDP) is configured and enabled in {microshift-short}, you can deploy Kubernetes workloads, such as pods, deployments, or `StatefulSets`, that request access to the host devices that you have exposed. Devices are made available inside the container without requiring the pod to run with elevated privileges.

.Prerequisites

* You installed {microshift-short}.
* You enabled and configured GDP.
* You installed {oc-first}.

.Procedure

. Define the device request in your `Pod` specification:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: device-app
spec:
  containers:
  - name: container
    image: <your_application_image>
    command: ["/path/to/your/app"]
    args: ["--device_path=/dev/video0"]
    resources:
      limits:
        device.microshift.io/video: 1
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
      runAsNonRoot: true
      seccompProfile:
        type: "RuntimeDefault"
----
+
where:
+
--
`spec.containers.image`:: Specifies the container image.
`spec.containers.command`:: Specifies the command for your application.
`spec.containers.args`:: Specifies the arguments for your application. For example, how your application might use the device.
`spec.containers.resources.limits`:: Specifies the resource limit for the device. The resource name must follow the pattern `device.microshift.io/<device_name>`, where `<device_name>` matches the `name` that you specified in your configuration file. This example requests one instance of the `video` device.
`spec.containers.securityContext`:: Specifies the privilege escalation. Define and configure with the least privilege value to ensure that the container has only required permissions, such as access to the device file, and to restrict other capabilities for the container.
--
+
. Deploy the Kubernetes workload by applying the manifest to the {microshift-short} node by running the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<your_workload_manifest.yaml>_
----
+
After the pod is running, the specified host device is available at its original path, or `mountPath` if specified, inside the container. Your application can then interact with it as if it were a local device.
+
For example, if you requested `device.microshift.io/serial`, which maps to `/dev/ttyUSB*`, your application might find the device at `/dev/ttyUSB0` or a similar path inside the container.

.Verification

* Verify device access by running the following command inside the running pod:
+
[source,terminal,subs="+quotes"]
----
$ oc exec -it _<pod_name>_ -- ls -l /dev/video0
----

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-generic-device-plugin-configuration-parameters_{context}"]
= Generic Device Plugin configuration reference

[role="_abstract"]
The Generic Device Plugin configuration reference lists and describes the parameters in the `genericDevicePlugin` section of the` config.yaml` file in OpenShift Container Platform. You can use this reference when you enable the GDP and define which host devices to expose.

.GDP configuration fields definitions table
[cols="1,2"]
|===
|Parameter|Description

|`genericDevicePlugin`
|The `genericDevicePlugin` section of the {microshift-short} configuration file defines the configurable parameters for the implementation of the {microshift-short} `GenericDevicePlugin` API. All of the following parameters in this table are subsections in the `genericDevicePlugin` section of the {microshift-short} configuration.

|`devices`
|Is a subgroup that lists the device definitions to be exposed by the plugin. Each `Device` entry contains a 'name' and a list of `groups`.

|`devices.groups`
|Lists device groups. Devices within a group comprise a pool of devices under a common name. When you request a device from that pool, you can receive a device from different defined paths.

|`devices.groups.count`
|Specifies how many times this group of devices can be mounted concurrently. If unspecified, `Count` defaults to `1`. Setting a high count, for example, `1000` for `/dev/fuse`, is possible because are no inherent limits, but performance might be impacted depending on the host's capabilities and the nature of the device.

|`devices.groups.paths`
|Lists the host device file paths. Paths can be glob patterns, for example, `/dev/ttyUSB*`, in which case each matched device is schedulable `Count` times. This field is exclusive with `usbs`; you cannot define both in the same device group.

|`devices.groups.paths.limit`
|Specifies up to how many times this device can be used in the group concurrently when other devices in the group yield more matches. For example, if one path in the group matches 5 devices and another matches 1 device but has a limit of 10, then the group provides 5 pairs of devices. When unspecified, the limit defaults to `1`.

|`devices.groups.paths.mountPath`
|The file path at which the host device should be mounted within the container. When unspecified, `mountPath` defaults to `path`.

|`devices.groups.paths.path`
|The file path of a device on the host, for example, `/dev/video0`, `/dev/ttyUSB*`.

|`devices.groups.paths.permissions`
|The file-system permissions given to the mounted device. Applies only to mounts of type `Device`. Can be one or more of:

* `r` - allows the container to read from the specified device.

* `w` - allows the container to write to the specified device.

* `m` - allows the container to create device files that do not yet exist.

When unspecified, `Permissions` defaults to `mrw`.

|`devices.groups.paths.readOnly`
|Specifies whether the path should be mounted read-only. The values are `true` or `false`. Applies only to mounts of type `Mount`.

|`devices.groups.path.type`
|Describes what type of file-system node this `path` represents and thus how it should be mounted. The type can be `Device` or `Mount`. When unspecified, `type` defaults to `Device`.

|`devices.groups.usbs`
|Lists the USB specifications that this device group consists of. The vendor and product IDs must always match. The serial ID must match if provided, or skipped if the ID is empty, The `usbs` field is exclusive with `paths`.

|`devices.groups.usbs.product`
|The USB Product ID of the device to match on, for example, `0x7523`.

|`devices.groups.usbs.serial`
|The serial number of the device to match on. A USB device must match exactly on all the given attributes to pass.

|`devices.groups.usbs.vendor`
|The USB Vendor ID of the device to match on, for example, `0x1a86`

|`devices.name`
|A unique string representing the kind of device this specification describes, for example, `serial`, `video`, or `fuse`. This name is used in pod resource requests, for example, `device.microshift.io/serial`.

|`domain`
|`domain` is a subgroup that specifies the domain prefix with which devices are advertised and present in the node. For example, `device.microshift.io/serial`. The default value is `device.microshift.io`.

|`status`
|`status` is a subgroup that specifies the default GDP status. `Enabled` or `Disabled` are valid values.

|===

// Module included in the following assemblies:
//
// microshift_configuring/microshift-gdp.adoc

[id="microshift-generic-device-plugin-troubleshooting_{context}"]
= Troubleshooting configuration issues

[role="_abstract"]
The following entries explain common Generic Device Plugin configuration issues and how to resolve them.

`Invalid configuration: failed to parse device`:: Occurs when you have incorrectly mixed `paths` and `usbs` fields within the same `groups` entry for a device. Each `group` must exclusively use either `paths` or `usbs` to define its devices.

`Cannot define both path and usbs at the same time`:: Occurs when you have incorrectly mixed `paths` and `usbs` fields within the same `groups` entry for a device. Each `group` must exclusively use either `paths` or `usbs` to define its devices.

[id="_additional-resources_microshift-gdp_{context}"]
== Additional resources

* Understanding networking settings
* About using multiple networks
* About network policies
