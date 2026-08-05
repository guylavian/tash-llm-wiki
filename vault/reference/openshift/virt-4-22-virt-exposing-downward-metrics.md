---
title: "Exposing downward metrics for virtual machines"
type: reference
domain: openshift
slug: virt-4-22-virt-exposing-downward-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-exposing-downward-metrics
version: 4.22
family: virt
documentKind: "Documentation"
---

# Exposing downward metrics for virtual machines

[id="virt-exposing-downward-metrics"]
= Exposing downward metrics for virtual machines

[role="_abstract"]
As an administrator, you can expose a set of host and virtual machine (VM) metrics to a guest VM by enabling the `downwardMetrics` feature gate and configuring a downward metrics device. You can view these metrics by using the command line or the `vm-dump-metrics` tool.

[NOTE]
====
On Red Hat Enterprise Linux (RHEL) 9, use the command line to view downward metrics.

The `vm-dump-metrics` tool is not supported on the Red Hat Enterprise Linux (RHEL) 9 platform.
====

// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-downward-metrics.adoc

[id="virt-enabling-disabling-downward-metrics-feature-gate-yaml_{context}"]
= Enabling or disabling the downward metrics feature gate in a YAML file

[role="_abstract"]
To expose downward metrics for a host virtual machine, you can enable the `downwardMetrics` feature gate by editing a YAML file.

.Prerequisites

* You must have administrator privileges to enable the feature gate.
* You have installed the {oc-first}.

.Procedure

. Open the HyperConverged custom resource (CR) in your default editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Choose to enable or disable the downwardMetrics feature gate as follows:

* To enable the `downwardMetrics` feature gate, add and then set `spec.featureGates.downwardMetrics` to `true`. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
    featureGates:
      downwardMetrics: true
# ...
----

* To disable the `downwardMetrics` feature gate, set `spec.featureGates.downwardMetrics` to `false`. For example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: {CNVNamespace}
spec:
    featureGates:
      downwardMetrics: false
# ...
----

// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-downward-metrics.adoc

[id="virt-enabling-disabling-downward-metrics-feature-gate-cli_{context}"]
= Enabling or disabling the downward metrics feature gate from the CLI

[role="_abstract"]
To expose downward metrics for a host virtual machine, you can enable the `downwardMetrics` feature gate by using the command line.

.Prerequisites

* You must have administrator privileges to enable the feature gate.
* You have installed the {oc-first}.

.Procedure

* Choose to enable or disable the `downwardMetrics` feature gate as follows:

** Enable the `downwardMetrics` feature gate by running the command shown in the following example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/featureGates/downwardMetrics", \
  "value": true}]'
----

** Disable the `downwardMetrics` feature gate by running the command shown in the following example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/featureGates/downwardMetrics", \
  "value": false}]'
----

// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-downward-metrics.adoc

[id="virt-configuring-downward-metrics_{context}"]
= Configuring a downward metrics device

[role="_abstract"]
You can enable the capturing of downward metrics for a host VM by creating a configuration file that includes a `downwardMetrics` device. Adding this device establishes that the metrics are exposed through a `virtio-serial` port.

.Prerequisites

* You must first enable the `downwardMetrics` feature gate.

.Procedure

* Edit or create a YAML file that includes a `downwardMetrics` device, as shown in the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: fedora
  namespace: default
spec:
  dataVolumeTemplates:
    - metadata:
        name: fedora-volume
      spec:
        sourceRef:
          kind: DataSource
          name: fedora
          namespace: openshift-virtualization-os-images
        storage:
          resources: {}
  instancetype:
    name: u1.medium
  runStrategy: Always
  template:
    metadata:
      labels:
        app.kubernetes.io/name: headless
    spec:
      domain:
        devices:
          downwardMetrics: {}
      subdomain: headless
      volumes:
        - dataVolume:
            name: fedora-volume
          name: rootdisk
        - cloudInitNoCloud:
            userData: |
              #cloud-config
              chpasswd:
                expire: false
              password: '<password>'
              user: fedora
          name: cloudinitdisk
----
+
* `spec.domain.devices.downwardMetrics` defines the `downwardMetrics` device.
* `spec.volumes.cloudInitNoCloud.userdata.password` defines the password for the `fedora` user.

// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-downward-metrics.adoc

[id="virt-viewing-downward-metrics-cli_{context}"]
= Viewing downward metrics by using the CLI

[role="_abstract"]
You can view downward metrics by entering a command from inside a guest virtual machine (VM).

.Procedure

* Run the following commands:
+
[source,terminal]
----
$ sudo sh -c 'printf "GET /metrics/XML\n\n" > /dev/virtio-ports/org.github.vhostmd.1'
----
+
[source,terminal]
----
$ sudo cat /dev/virtio-ports/org.github.vhostmd.1
----

// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-downward-metrics.adoc

[id="virt-viewing-downward-metrics-tool_{context}"]
= Viewing downward metrics by using the vm-dump-metrics tool

[role="_abstract"]
To view downward metrics, install the `vm-dump-metrics` tool and then use the tool to expose the metrics results.

[NOTE]
====
On Red Hat Enterprise Linux (RHEL) 9, use the command line to view downward metrics. The vm-dump-metrics tool is not supported on the Red Hat Enterprise Linux (RHEL) 9 platform.
====

.Procedure

. Install the `vm-dump-metrics` tool by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y vm-dump-metrics
----

. Retrieve the metrics results by running the following command:
+
[source,terminal]
----
$ sudo vm-dump-metrics
----
+
Example output:
+
[source,xml]
----
<metrics>
  <metric type="string" context="host">
    <name>HostName</name>
    <value>node01</value>
[...]
  <metric type="int64" context="host" unit="s">
    <name>Time</name>
    <value>1619008605</value>
  </metric>
  <metric type="string" context="host">
    <name>VirtualizationVendor</name>
    <value>kubevirt.io</value>
  </metric>
</metrics>
----

[id="additional-resources_virt-exposing-downward-metrics-for-vms"]
[role="_additional-resources"]
== Additional resources

* Viewing downward metrics by using the command line
