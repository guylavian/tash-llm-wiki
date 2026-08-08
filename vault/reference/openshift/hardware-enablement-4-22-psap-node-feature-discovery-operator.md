---
title: "Node Feature Discovery Operator"
type: reference
domain: openshift
slug: hardware-enablement-4-22-psap-node-feature-discovery-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_enablement/psap-node-feature-discovery-operator
version: 4.22
family: hardware_enablement
documentKind: "Documentation"
---

# Node Feature Discovery Operator

[id="psap-node-feature-discovery-operator"]
= Node Feature Discovery Operator

Learn about the Node Feature Discovery (NFD) Operator and how you can use it to expose node-level information by orchestrating Node Feature Discovery, a Kubernetes add-on for detecting hardware features and system configuration.

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="about-node-feature-discovery-operator_{context}"]
= Node Feature Discovery Operator

= About the Node Feature Discovery Operator

The Node Feature Discovery Operator (NFD) manages the detection of hardware features and configuration in an OpenShift Container Platform cluster by labeling the nodes with hardware-specific information. NFD labels the host with node-specific attributes, such as PCI cards, kernel, operating system version, and so on.

The NFD Operator can be found on the Operator Hub by searching for “Node Feature Discovery”.

== Project

cluster-nfd-operator

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="installing-the-node-feature-discovery-operator_{context}"]
= Installing the Node Feature Discovery Operator

The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the NFD daemon set. As a cluster administrator, you can install the NFD Operator by using the OpenShift Container Platform CLI or the web console.

[id="install-operator-cli_{context}"]
== Installing the NFD Operator using the CLI

As a cluster administrator, you can install the NFD Operator using the CLI.

.Prerequisites

* An OpenShift Container Platform cluster
* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a namespace for the NFD Operator.

.. Create the following `Namespace` custom resource (CR) that defines the `openshift-nfd` namespace, and then save the YAML in the `nfd-namespace.yaml` file. Set `cluster-monitoring` to `"true"`.
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nfd
  labels:
    name: openshift-nfd
    openshift.io/cluster-monitoring: "true"
----

.. Create the namespace by running the following command:
+
[source,terminal]
----
$ oc create -f nfd-namespace.yaml
----

. Install the NFD Operator in the namespace you created in the previous step by creating the following objects:

.. Create the following `OperatorGroup` CR and save the YAML in the `nfd-operatorgroup.yaml` file:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  generateName: openshift-nfd-
  name: openshift-nfd
  namespace: openshift-nfd
spec:
  targetNamespaces:
  - openshift-nfd
----

.. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nfd-operatorgroup.yaml
----

.. Create the following `Subscription` CR and save the YAML in the `nfd-sub.yaml` file:
+
.Example Subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nfd
  namespace: openshift-nfd
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: nfd
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.. Create the subscription object by running the following command:
+
[source,terminal]
----
$ oc create -f nfd-sub.yaml
----

.. Change to the `openshift-nfd` project:
+
[source,terminal]
----
$ oc project openshift-nfd
----

.Verification

* To verify that the Operator deployment is successful, run:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          10m
----
+
A successful deployment shows a `Running` status.

[id="install-operator-web-console_{context}"]
== Installing the NFD Operator using the web console

As a cluster administrator, you can install the NFD Operator using the web console.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Software Catalog*.

. Choose *Node Feature Discovery* from the list of available Operators, and then click *Install*.

. On the *Install Operator* page, select *A specific namespace on the cluster*, and then click *Install*. You do not need to create a namespace because it is created for you.

.Verification

To verify that the NFD Operator installed successfully:

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. Ensure that *Node Feature Discovery* is listed in the *openshift-nfd* project with a *Status* of *InstallSucceeded*.
+
[NOTE]
====
During installation an Operator might display a *Failed* status. If the installation later succeeds with an *InstallSucceeded* message, you can ignore the *Failed* message.
====

.Troubleshooting

If the Operator does not appear as installed, troubleshoot further:

. Navigate to the *Ecosystem* -> *Installed Operators* page and inspect the *Operator Subscriptions* and *Install Plans* tabs for any failure or errors under *Status*.
. Navigate to the *Workloads* -> *Pods* page and check the logs for pods in the `openshift-nfd` project.

[id="psap-node-feature-discovery-operator-using-the-operator"]
== Using the Node Feature Discovery Operator

The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the Node-Feature-Discovery daemon set by watching for a `NodeFeatureDiscovery` custom resource (CR). Based on the `NodeFeatureDiscovery` CR, the Operator creates the operand (NFD) components in the selected namespace. You can edit the CR to use another namespace, image, image pull policy, and `nfd-worker-conf` config map, among other options.

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR by using the {oc-first} or the web console.

[NOTE]
====
Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using {olm-first}, OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly.
====

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="creating-nfd-cr-cli_{context}"]
= Creating a NodeFeatureDiscovery CR by using the CLI

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR instance by using the {oc-first}.

[NOTE]
====
The `spec.operand.image` setting requires a `-rhel9` image to be defined for use with OpenShift Container Platform releases 4.13 and later.
====

The following example shows the use of `-rhel9` to acquire the correct image.

.Prerequisites

* You have access to an OpenShift Container Platform cluster
* You installed the {oc-first}.
* You logged in as a user with `cluster-admin` privileges.
* You installed the NFD Operator.

.Procedure

. Create a `NodeFeatureDiscovery` CR:
+
.Example `NodeFeatureDiscovery` CR
[source,yaml,subs="attributes+"]
----
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
  namespace: openshift-nfd
spec:
  instance: "" # instance is empty by default
  topologyupdater: false # False by default
  operand:
    image: registry.redhat.io/openshift4/ose-node-feature-discovery-rhel9:v <1>
    imagePullPolicy: Always
  workerConfig:
    configData: |
      core:
      #  labelWhiteList:
      #  noPublish: false
        sleepInterval: 60s
      #  sources: [all]
      #  klog:
      #    addDirHeader: false
      #    alsologtostderr: false
      #    logBacktraceAt:
      #    logtostderr: true
      #    skipHeaders: false
      #    stderrthreshold: 2
      #    v: 0
      #    vmodule:
      ##   NOTE: the following options are not dynamically run-time configurable
      ##         and require a nfd-worker restart to take effect after being changed
      #    logDir:
      #    logFile:
      #    logFileMaxSize: 1800
      #    skipLogHeaders: false
      sources:
        cpu:
          cpuid:
      #     NOTE: whitelist has priority over blacklist
            attributeBlacklist:
              - "BMI1"
              - "BMI2"
              - "CLMUL"
              - "CMOV"
              - "CX16"
              - "ERMS"
              - "F16C"
              - "HTT"
              - "LZCNT"
              - "MMX"
              - "MMXEXT"
              - "NX"
              - "POPCNT"
              - "RDRAND"
              - "RDSEED"
              - "RDTSCP"
              - "SGX"
              - "SSE"
              - "SSE2"
              - "SSE3"
              - "SSE4.1"
              - "SSE4.2"
              - "SSSE3"
            attributeWhitelist:
        kernel:
          kconfigFile: "/path/to/kconfig"
          configOpts:
            - "NO_HZ"
            - "X86"
            - "DMI"
        pci:
          deviceClassWhitelist:
            - "0200"
            - "03"
            - "12"
          deviceLabelFields:
            - "class"
  customConfig:
    configData: |
          - name: "more.kernel.features"
            matchOn:
            - loadedKMod: ["example_kmod3"]
----
<1> The `operand.image` field is mandatory.

. Create the `NodeFeatureDiscovery` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----

.Verification

. Check that the `NodeFeatureDiscovery` CR was created by running the following command:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          11m
nfd-master-hcn64                          1/1     Running   0          60s
nfd-master-lnnxx                          1/1     Running   0          60s
nfd-master-mp6hr                          1/1     Running   0          60s
nfd-worker-vgcz9                          1/1     Running   0          60s
nfd-worker-xqbws                          1/1     Running   0          60s
----
+
A successful deployment shows a `Running` status.

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="creating-nfd-cr-cli-disconnected_{context}"]
= Creating a NodeFeatureDiscovery CR by using the CLI in a disconnected environment

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR instance by using the {oc-first}.

.Prerequisites

* You have access to an OpenShift Container Platform cluster
* You installed the {oc-first}.
* You logged in as a user with `cluster-admin` privileges.
* You installed the NFD Operator.
* You have access to a mirror registry with the required images.
* You installed the `skopeo` CLI tool.

.Procedure

. Determine the digest of the registry image:

.. Run the following command:
+
[source,terminal]
----
$ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:<openshift_version>
----
+
.Example command
[source,terminal]
----
$ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:v4.12
----

.. Inspect the output to identify the image digest:
+
.Example output
[source,terminal]
----
{
  ...
  "Digest": "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
  ...
}
----

. Use the `skopeo` CLI tool to copy the image from `registry.redhat.io` to your mirror registry, by running the following command:
+
[source,terminal]
----
skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@<image_digest> docker://<mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest>
----
+
.Example command
[source,terminal]
----
skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef docker://<your-mirror-registry>/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
----

. Create a `NodeFeatureDiscovery` CR:
+
.Example `NodeFeatureDiscovery` CR
[source,yaml,subs="attributes+"]
----
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
spec:
  operand:
    image: <mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest> <1>
    imagePullPolicy: Always
  workerConfig:
    configData: |
      core:
      #  labelWhiteList:
      #  noPublish: false
        sleepInterval: 60s
      #  sources: [all]
      #  klog:
      #    addDirHeader: false
      #    alsologtostderr: false
      #    logBacktraceAt:
      #    logtostderr: true
      #    skipHeaders: false
      #    stderrthreshold: 2
      #    v: 0
      #    vmodule:
      ##   NOTE: the following options are not dynamically run-time configurable
      ##         and require a nfd-worker restart to take effect after being changed
      #    logDir:
      #    logFile:
      #    logFileMaxSize: 1800
      #    skipLogHeaders: false
      sources:
        cpu:
          cpuid:
      #     NOTE: whitelist has priority over blacklist
            attributeBlacklist:
              - "BMI1"
              - "BMI2"
              - "CLMUL"
              - "CMOV"
              - "CX16"
              - "ERMS"
              - "F16C"
              - "HTT"
              - "LZCNT"
              - "MMX"
              - "MMXEXT"
              - "NX"
              - "POPCNT"
              - "RDRAND"
              - "RDSEED"
              - "RDTSCP"
              - "SGX"
              - "SSE"
              - "SSE2"
              - "SSE3"
              - "SSE4.1"
              - "SSE4.2"
              - "SSSE3"
            attributeWhitelist:
        kernel:
          kconfigFile: "/path/to/kconfig"
          configOpts:
            - "NO_HZ"
            - "X86"
            - "DMI"
        pci:
          deviceClassWhitelist:
            - "0200"
            - "03"
            - "12"
          deviceLabelFields:
            - "class"
  customConfig:
    configData: |
          - name: "more.kernel.features"
            matchOn:
            - loadedKMod: ["example_kmod3"]
----
<1> The `operand.image` field is mandatory.

. Create the `NodeFeatureDiscovery` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----

.Verification

. Check the status of the `NodeFeatureDiscovery` CR by running the following command:
+
[source,terminal]
----
$ oc get nodefeaturediscovery nfd-instance -o yaml
----

. Check that the pods are running without `ImagePullBackOff` errors by running the following command:
+
[source,terminal]
----
$ oc get pods -n <nfd_namespace>
----

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="creating-nfd-cr-web-console_{context}"]
= Creating a NodeFeatureDiscovery CR by using the web console

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR by using the OpenShift Container Platform web console.

.Prerequisites

* You have access to an OpenShift Container Platform cluster
* You logged in as a user with `cluster-admin` privileges.
* You installed the NFD Operator.

.Procedure

. Navigate to the *Ecosystem* -> *Installed Operators* page.
. In the *Node Feature Discovery* section, under *Provided APIs*, click *Create instance*.
. Edit the values of the `NodeFeatureDiscovery` CR.
. Click *Create*.

[NOTE]
====
Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using {olm-first}, OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/psap-node-feature-discovery-operator.adoc

[id="configuring-the-node-feature-discovery_{context}"]
= Configuring the Node Feature Discovery Operator

[id="configuring-node-feature-discovery-operator-core_{context}"]
== core

The `core` section contains common configuration settings that are not specific to any particular feature source.

[id="configuring-node-feature-discovery-operator-core-sleepInterval_{context}"]
=== core.sleepInterval

`core.sleepInterval` specifies the interval between consecutive passes of feature detection or re-detection, and thus also the interval between node re-labeling. A non-positive value implies infinite sleep interval; no re-detection or re-labeling is done.

This value is overridden by the deprecated `--sleep-interval` command-line flag, if specified.

.Example usage
[source,yaml]
----
core:
  sleepInterval: 60s <1>
----
The default value is `60s`.

[id="configuring-node-feature-discovery-operator-core-sources_{context}"]
=== core.sources

`core.sources` specifies the list of enabled feature sources. A special value `all` enables all feature sources.

This value is overridden by the deprecated `--sources` command-line flag, if specified.

Default: `[all]`

.Example usage
[source,yaml]
----
core:
  sources:
    - system
    - custom
----

[id="configuring-node-feature-discovery-operator-core-label-whitelist_{context}"]
=== core.labelWhiteList

`core.labelWhiteList` specifies a regular expression for filtering feature labels based on the label name. Non-matching labels are not published.

The regular expression is only matched against the basename part of the label, the part of the name after '/'. The label prefix,  or namespace, is omitted.

This value is overridden by the deprecated `--label-whitelist` command-line flag, if specified.

Default: `null`

.Example usage
[source,yaml]
----
core:
  labelWhiteList: '^cpu-cpuid'
----

[id="configuring-node-feature-discovery-operator-core-no-publish_{context}"]
=== core.noPublish

Setting `core.noPublish` to `true` disables all communication with the `nfd-master`. It is effectively a dry run flag; `nfd-worker` runs feature detection normally, but no labeling requests are sent to `nfd-master`.

This value is overridden by the `--no-publish` command-line flag, if specified.

Example:

.Example usage
[source,yaml]
----
core:
  noPublish: true <1>
----
The default value is `false`.

[id="configuring-node-feature-discovery-operator-core-klog_{context}"]
== core.klog

The following options specify the logger configuration, most of which can be dynamically adjusted at run-time.

The logger options can also be specified using command-line flags, which take precedence over any corresponding config file options.

[id="configuring-node-feature-discovery-operator-core-klog-adddirheader_{context}"]
=== core.klog.addDirHeader

If set to `true`, `core.klog.addDirHeader` adds the file directory to the header of the log messages.

Default: `false`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-alsologtostderr_{context}"]
=== core.klog.alsologtostderr

Log to standard error as well as files.

Default: `false`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-BacktraceAt_{context}"]
=== core.klog.logBacktraceAt

When logging hits line file:N, emit a stack trace.

Default: *empty*

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-logdir_{context}"]
=== core.klog.logDir

If non-empty, write log files in this directory.

Default: *empty*

Run-time configurable: no

[id="configuring-node-feature-discovery-operator-core-klog-logfile_{context}"]
=== core.klog.logFile

If not empty, use this log file.

Default: *empty*

Run-time configurable: no

[id="configuring-node-feature-discovery-operator-core-klog-logFileMaxSize_{context}"]
=== core.klog.logFileMaxSize

`core.klog.logFileMaxSize` defines the maximum size a log file can grow to. Unit is megabytes. If the value is `0`, the maximum file size is unlimited.

Default: `1800`

Run-time configurable: no

[id="configuring-node-feature-discovery-operator-core-klog-logtostderr_{context}"]
=== core.klog.logtostderr

Log to standard error instead of files

Default: `true`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-skipHeaders_{context}"]
=== core.klog.skipHeaders

If `core.klog.skipHeaders` is set to `true`, avoid header prefixes in the log messages.

Default: `false`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-skipLogHeaders_{context}"]
=== core.klog.skipLogHeaders

If `core.klog.skipLogHeaders` is set to `true`, avoid headers when opening log files.

Default: `false`

Run-time configurable: no

[id="configuring-node-feature-discovery-operator-core-klog-stderrthreshold_{context}"]
=== core.klog.stderrthreshold

Logs at or above this threshold go to stderr.

Default: `2`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-v_{context}"]
=== core.klog.v

`core.klog.v` is the number for the log level verbosity.

Default: `0`

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-core-klog-vmodule_{context}"]
=== core.klog.vmodule

`core.klog.vmodule` is a comma-separated list of `pattern=N` settings for file-filtered logging.

Default: *empty*

Run-time configurable: yes

[id="configuring-node-feature-discovery-operator-sources_{context}"]
== sources

The `sources` section contains feature source specific configuration parameters.

[id="configuring-node-feature-discovery-operator-sources-cpu-cpuid-attributeBlacklist_{context}"]
=== sources.cpu.cpuid.attributeBlacklist

Prevent publishing `cpuid` features listed in this option.

This value is overridden by `sources.cpu.cpuid.attributeWhitelist`, if specified.

Default: `[BMI1, BMI2, CLMUL, CMOV, CX16, ERMS, F16C, HTT, LZCNT, MMX, MMXEXT, NX, POPCNT, RDRAND, RDSEED, RDTSCP, SGX, SGXLC, SSE, SSE2, SSE3, SSE4.1, SSE4.2, SSSE3]`

.Example usage
[source,yaml]
----
sources:
  cpu:
    cpuid:
      attributeBlacklist: [MMX, MMXEXT]
----

[id="configuring-node-feature-discovery-operator-sources-cpu-cpuid-attributeWhitelist_{context}"]
=== sources.cpu.cpuid.attributeWhitelist

Only publish the `cpuid` features listed in this option.

`sources.cpu.cpuid.attributeWhitelist` takes precedence over `sources.cpu.cpuid.attributeBlacklist`.

Default: *empty*

.Example usage
[source,yaml]
----
sources:
  cpu:
    cpuid:
      attributeWhitelist: [AVX512BW, AVX512CD, AVX512DQ, AVX512F, AVX512VL]
----

[id="configuring-node-feature-discovery-operator-sources-kernel-kconfigFilet_{context}"]
=== sources.kernel.kconfigFile

`sources.kernel.kconfigFile` is the path of the kernel config file. If empty, NFD runs a search in the well-known standard locations.

Default: *empty*

.Example usage
[source,yaml]
----
sources:
  kernel:
    kconfigFile: "/path/to/kconfig"
----

[id="configuring-node-feature-discovery-operator-sources-kernel-configOpts_{context}"]
=== sources.kernel.configOpts

`sources.kernel.configOpts` represents kernel configuration options to publish as feature labels.

Default: `[NO_HZ, NO_HZ_IDLE, NO_HZ_FULL, PREEMPT]`

.Example usage
[source,yaml]
----
sources:
  kernel:
    configOpts: [NO_HZ, X86, DMI]
----

[id="configuring-node-feature-discovery-operator-sources-pci-deviceClassWhitelist_{context}"]
=== sources.pci.deviceClassWhitelist

`sources.pci.deviceClassWhitelist` is a list of PCI device class IDs for which to publish a label. It can be specified as a main class only (for example, `03`) or full class-subclass combination (for example `0300`). The former implies that all
subclasses are accepted.  The format of the labels can be further configured with `deviceLabelFields`.

Default: `["03", "0b40", "12"]`

.Example usage
[source,yaml]
----
sources:
  pci:
    deviceClassWhitelist: ["0200", "03"]
----

[id="configuring-node-feature-discovery-operator-sources-pci-deviceLabelFields_{context}"]
=== sources.pci.deviceLabelFields

`sources.pci.deviceLabelFields` is the set of PCI ID fields to use when constructing the name of the feature label. Valid fields are `class`, `vendor`, `device`, `subsystem_vendor` and `subsystem_device`.

Default: `[class, vendor]`

.Example usage
[source,yaml]
----
sources:
  pci:
    deviceLabelFields: [class, vendor, device]
----

With the example config above, NFD would publish labels such as `feature.node.kubernetes.io/pci-<class-id>_<vendor-id>_<device-id>.present=true`

[id="configuring-node-feature-discovery-operator-sources-usb-deviceClassWhitelist_{context}"]
=== sources.usb.deviceClassWhitelist

`sources.usb.deviceClassWhitelist` is a list of USB device class IDs for
which to publish a feature label. The format of the labels can be further
configured with `deviceLabelFields`.

Default: `["0e", "ef", "fe", "ff"]`

.Example usage
[source,yaml]
----
sources:
  usb:
    deviceClassWhitelist: ["ef", "ff"]
----

[id="configuring-node-feature-discovery-operator-sources-usb-deviceLabelFields_{context}"]
=== sources.usb.deviceLabelFields

`sources.usb.deviceLabelFields` is the set of USB ID fields from which to compose the name of the feature label. Valid fields are `class`, `vendor`, and `device`.

Default: `[class, vendor, device]`

.Example usage
[source,yaml]
----
sources:
  pci:
    deviceLabelFields: [class, vendor]
----

With the example config above, NFD would publish labels like: `feature.node.kubernetes.io/usb-<class-id>_<vendor-id>.present=true`.

[id="configuring-node-feature-discovery-operator-sources-custom_{context}"]
=== sources.custom

`sources.custom` is the list of rules to process in the custom feature source to create user-specific labels.

Default: *empty*

.Example usage
[source,yaml]
----
source:
  custom:
  - name: "my.custom.feature"
    matchOn:
    - loadedKMod: ["e1000e"]
    - pciId:
        class: ["0200"]
        vendor: ["8086"]
----

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="nfd-rules-about_{context}"]
= About the NodeFeatureRule custom resource

`NodeFeatureRule` objects are a `NodeFeatureDiscovery` custom resource designed for rule-based custom labeling of nodes. Some use cases include application-specific labeling or distribution by hardware vendors to create specific labels for their devices.

`NodeFeatureRule` objects provide a method to create vendor- or application-specific labels and taints. It uses a flexible rule-based mechanism for creating labels and optionally taints based on node features.

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="nfd-rules-using_{context}"]
= Using the NodeFeatureRule custom resource

Create a `NodeFeatureRule` object to label nodes if a set of rules match the conditions.

.Procedure

. Create a custom resource file named `nodefeaturerule.yaml` that contains the following text:
+
[source,yaml]
----
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureRule
metadata:
  name: example-rule
spec:
  rules:
    - name: "example rule"
      labels:
        "example-custom-feature": "true"
      # Label is created if all of the rules below match
      matchFeatures:
        # Match if "veth" kernel module is loaded
        - feature: kernel.loadedmodule
          matchExpressions:
            veth: {op: Exists}
        # Match if any PCI device with vendor 8086 exists in the system
        - feature: pci.device
          matchExpressions:
            vendor: {op: In, value: ["8086"]}
----
+
This custom resource specifies that labelling occurs when the `veth` module is loaded and any PCI device with vendor code `8086` exists in the cluster.

. Apply the `nodefeaturerule.yaml` file to your cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f https://raw.githubusercontent.com/kubernetes-sigs/node-feature-discovery/v0.13.6/examples/nodefeaturerule.yaml
----
The example applies the feature label on nodes with the `veth` module loaded and any PCI device with vendor code `8086` exists.
+
[NOTE]
====
A relabeling delay of up to 1 minute might occur.
====

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="using-the-nfd-topology-updater_{context}"]
= Using the NFD Topology Updater

The Node Feature Discovery (NFD) Topology Updater is a daemon responsible for examining allocated resources on a worker node. It accounts for resources that are available to be allocated to new pod on a per-zone basis, where a zone can be a Non-Uniform Memory Access (NUMA) node. The NFD Topology Updater communicates the information to nfd-master, which creates a `NodeResourceTopology` custom resource (CR) corresponding to all of the worker nodes in the cluster. One instance of the NFD Topology Updater runs on each node of the cluster.

To enable the Topology Updater workers in NFD, set the `topologyupdater` variable to `true` in the `NodeFeatureDiscovery` CR, as described in the section *Using the Node Feature Discovery Operator*.

== NodeResourceTopology CR

When run with NFD Topology Updater, NFD creates custom resource instances corresponding to the node resource hardware topology, such as:

[source,yaml]
----
apiVersion: topology.node.k8s.io/v1alpha1
kind: NodeResourceTopology
metadata:
  name: node1
topologyPolicies: ["SingleNUMANodeContainerLevel"]
zones:
  - name: node-0
    type: Node
    resources:
      - name: cpu
        capacity: 20
        allocatable: 16
        available: 10
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
  - name: node-1
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic2
        capacity: 6
        allocatable: 6
        available: 6
  - name: node-2
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
----

// Module included in the following assemblies:
//
// * hardware_enablement/psap-node-feature-discovery-operator.adoc

[id="nfd-topology-updater-command-line-flags_{context}"]
= NFD Topology Updater command-line flags

To view available command-line flags, run the `nfd-topology-updater -help` command. For example, in a podman container, run the following command:

[source,terminal]
----
$ podman run gcr.io/k8s-staging-nfd/node-feature-discovery:master nfd-topology-updater -help
----

[id="nfd-topology-updater-ca-file_{context}"]
== -ca-file

The `-ca-file` flag is one of the three flags, together with the `-cert-file` and `-key-file`flags, that controls the mutual TLS authentication on the NFD Topology Updater. This flag specifies the TLS root certificate that is used for verifying the authenticity of nfd-master.

Default: empty

[IMPORTANT]
====
The `-ca-file` flag must be specified together with the `-cert-file` and `-key-file` flags.
====

.Example
[source,terminal]
----
$ nfd-topology-updater -ca-file=/opt/nfd/ca.crt -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key
----

[id="nfd-topology-updater-cert-file_{context}"]
== -cert-file

The `-cert-file` flag is one of the three flags, together with the `-ca-file` and `-key-file flags`, that controls mutual TLS authentication on the NFD Topology Updater. This flag specifies the TLS certificate presented for authenticating outgoing requests.

Default: empty

[IMPORTANT]
====
The `-cert-file` flag must be specified together with the `-ca-file` and `-key-file` flags.
====

.Example
[source,terminal]
----
$ nfd-topology-updater -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key -ca-file=/opt/nfd/ca.crt
----

[id="nfd-topology-updater-help_{context}"]
== -h, -help

Print usage and exit.

[id="nfd-topology-updater-key-file_{context}"]
== -key-file

The `-key-file` flag is one of the three flags, together with the `-ca-file` and `-cert-file` flags, that controls the mutual TLS authentication on the NFD Topology Updater. This flag specifies the private key corresponding the given certificate file, or `-cert-file`, that is used for authenticating outgoing requests.

Default: empty

[IMPORTANT]
====
The `-key-file` flag must be specified together with the `-ca-file` and `-cert-file` flags.
====

.Example
[source,terminal]
----
$ nfd-topology-updater -key-file=/opt/nfd/updater.key -cert-file=/opt/nfd/updater.crt -ca-file=/opt/nfd/ca.crt
----

[id="nfd-topology-updater-kubelet-config-file_{context}"]
== -kubelet-config-file

The `-kubelet-config-file` specifies the path to the Kubelet's configuration
file.

Default: `/host-var/lib/kubelet/config.yaml`

.Example
[source,terminal]
----
$ nfd-topology-updater -kubelet-config-file=/var/lib/kubelet/config.yaml
----

[id="nfd-topology-updater-no-publish_{context}"]
== -no-publish

The `-no-publish` flag disables all communication with the nfd-master, making it a dry run flag for nfd-topology-updater. NFD Topology Updater runs resource hardware topology detection normally, but no CR requests are sent to nfd-master.

Default: `false`

.Example
[source,terminal]
----
$ nfd-topology-updater -no-publish
----

[id="nfd-topology-updater-oneshot_{context}"]
== -oneshot

The `-oneshot` flag causes the NFD Topology Updater to exit after one pass of resource hardware topology detection.

Default: `false`

.Example
[source,terminal]
----
$ nfd-topology-updater -oneshot -no-publish
----

[id="nfd-topology-updater-podresources-socket_{context}"]
== -podresources-socket

The `-podresources-socket` flag specifies the path to the Unix socket where kubelet exports a gRPC service to enable discovery of in-use CPUs and devices, and to provide metadata for them.

Default: `/host-var/liblib/kubelet/pod-resources/kubelet.sock`

.Example
[source,terminal]
----
$ nfd-topology-updater -podresources-socket=/var/lib/kubelet/pod-resources/kubelet.sock
----

[id="nfd-topology-updater-server_{context}"]
== -server

The `-server` flag specifies the address of the nfd-master endpoint to connect to.

Default: `localhost:8080`

.Example
[source,terminal]
----
$ nfd-topology-updater -server=nfd-master.nfd.svc.cluster.local:443
----

[id="nfd-topology-updater-server-name-override_{context}"]
== -server-name-override

The `-server-name-override` flag specifies the common name (CN) which to expect from the nfd-master TLS certificate. This flag is mostly intended for development and debugging purposes.

Default: empty

.Example
[source,terminal]
----
$ nfd-topology-updater -server-name-override=localhost
----

[id="nfd-topology-updater-sleep-interval_{context}"]
== -sleep-interval

The `-sleep-interval` flag specifies the interval between resource hardware topology re-examination and custom resource updates. A non-positive value implies infinite sleep interval and no re-detection is done.

Default: `60s`

.Example
[source,terminal]
----
$ nfd-topology-updater -sleep-interval=1h
----

[id="nfd-topology-updater-version_{context}"]
== -version

Print version and exit.

[id="nfd-topology-updater-watch-namespace_{context}"]
== -watch-namespace

The `-watch-namespace` flag specifies the namespace to ensure that resource hardware topology examination only happens for the pods running in the
specified namespace. Pods that are not running in the specified namespace are not considered during resource accounting. This is particularly useful for testing and debugging purposes. A `*` value means that all of the pods across all namespaces are considered during the accounting process.

Default: `*`

.Example
[source,terminal]
----
$ nfd-topology-updater -watch-namespace=rte
----
