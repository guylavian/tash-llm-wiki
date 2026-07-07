---
title: "Boot image skew enforcement"
type: reference
domain: openshift
slug: machine-configuration-4-22-mco-update-boot-skew-mgmt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/mco-update-boot-skew-mgmt
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Boot image skew enforcement

[id="mco-update-boot-skew-mgmt"]
= Boot image skew enforcement

[role="_abstract"]
You can use boot image skew enforcement to help ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and {op-system} version being used in the cluster. Using an older boot image could cause issues when scaling new nodes. If the images are older than a predetermined version, the MCO disables cluster upgrades until it deems the boot images to be compliant.

[NOTE]
====
Boot image skew enforcement is not supported for {sno} clusters.
====

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-skew-mgmt.adoc

[id="mco-update-boot-skew-mgmt-about_{context}"]
= About boot image skew enforcement

[role="_abstract"]
Using boot image skew enforcement, you can ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and {op-system} version being used in the cluster. Making sure that your boot images are current can help you avoid the problems associated with running older images.

When boot image skew enforcement is active in a cluster, the Machine Config Operator (MCO) examines the boot image version reported in the `MachineConfiguration` object to determine if that boot image is appropriate for the cluster. If the boot image version is too old, the Operator reports that _boot image version skew_ is detected and blocks cluster updates until you manually update the boot image or disable boot image skew enforcement by setting the `None` mode, as described in this section.

The limit for boot image version skew is set within the MCO and cannot be modified.

For information on manually configuring the boot image in your cluster, see "Manually updating the boot image".

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-skew-mgmt-modes.adoc

[id="mco-update-boot-skew-mgmt-about-modes_{context}"]
= About boot image skew enforcement modes

[role="_abstract"]
Review the following information to learn about the boot image skew enforcement modes. Use the information to determine the best method for your cluster.

Boot image skew enforcement operates in one of the following modes:

Automatic::
When set to `Automatic`, with boot image management also enabled, if the cluster is updated from one OpenShift Container Platform version to the next, the MCO automatically updates the boot image version in the `MachineConfiguration` object and tests the boot image version for skew.
+
[NOTE]
====
In OpenShift Container Platform 4.22, the automatic mode is available only for {aws-short}, {gcp-short}, {azure-short}, and {vmw-short} clusters and is the default for these platforms.
====
+
The MCO automatically configures this mode when the following conditions are met:
+
--
* Boot image management is available for the platform that your cluster uses. Currently boot image management is available for only {aws-short}, {gcp-short}, {azure-short}, and {vmw-short} clusters.
* You have enabled boot image management for compute machine sets.
* You have not set skew enforcement to the manual or none mode.
--
+
For information on boot image management, see "Boot image management".
+
.Example `MachineConfiguration` object with automatic skew enforcement
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
status:
# ...
  bootImageSkewEnforcementStatus:
    automatic:
      ocpVersion: 4.22.0
    mode: Automatic
----
+
The MCO examines the boot image reported in the `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits.

Manual::
When set to `Manual`, if the boot image version is updated, a cluster administrator is responsible for manually updating the `MachineConfiguration` object with the {op-system} version of the new boot image or the OpenShift Container Platform version associated with the new boot image. The MCO then tests the boot image version for skew.
+
.Example `MachineConfiguration` object with skew enforcement based on an {op-system} version
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: Manual
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.2.20251023-0
# ...
status:
  bootImageSkewEnforcementStatus:
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.2.20251023-0
    mode: Manual
----
+
.Example `MachineConfiguration` object with skew enforcement based on an OpenShift Container Platform version
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    manual:
      mode: OCPVersion
      ocpVersion: 4.22.0
    mode: Manual
# ...
status:
  bootImageSkewEnforcementStatus:
    manual:
      mode: OCPVersion
      ocpVersion: 4.22.0
    mode: Manual
----
+
The MCO examines the boot image reported in the `rhcosVersion` or `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits.

None::
When set to `None`, boot image skew enforcement is disabled. When disabled, the MCO does not monitor for boot image skew and does not report if new nodes are provisioned with older boot images, which could introduce issues when scaling new nodes.
+
.Example `MachineConfiguration` object with skew enforcement disabled
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: None
# ...
status:
  bootImageSkewEnforcementStatus:
    mode: None
----
+
When in the none mode, the MCO reports a Prometheus alert that skew enforcement is disabled and that scale-up might run into issues due to old boot images. The alert does not cause any functional issues for the cluster.
+
{sno-caps} clusters default to the none mode regardless of platform, because they do not scale. The skew enforcement Prometheus alert is not reported for {sno} clusters.
+
Bare-metal clusters running OpenShift Container Platform version 4.10 and later do not use the MCO to keep their boot images up-to-date. Skew enforcement defaults to the none mode and the skew enforcement Prometheus alert mentioned is not reported. For bare-metal clusters running OpenShift Container Platform version 4.9 and earlier, you need to perform a one-time action to migrate to the 4.10 system, this is explained further in the bare metal boot image update docs. For information, see "Manually updating the boot image".

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-skew-mgmt.adoc

[id="mco-update-boot-skew-mgmt-configuring_{context}"]
= Configuring boot image skew enforcement

[role="_abstract"]
You can configure the current boot image skew enforcement mode that the Machine Config Operator (MCO) uses. By configuring the boot image skew enforcement mode, you can determine if the boot image version in the `MachineConfiguration` object is updated automatically or manually.

Alternatively, you can disable boot image skew enforcement by setting the `mode` to `None`. When disabled, the MCO does not monitor for boot image skew, and older boot images could be used, possibly introducing issues when scaling new nodes.

In OpenShift Container Platform 4.22, the automatic mode is available only for {aws-short}, {gcp-short}, {azure-short}, and {vmw-short} clusters and is the default for these platforms. If you modify a cluster from the automatic mode to the manual or none mode, you can revert a cluster back to automatic mode only by removing the `bootImageSkewEnforcement` stanza from the `MachineConfiguration` object.

All other platforms default to manual mode with the OpenShift Container Platform version set as the boot image version in the `MachineConfiguration` object. In manual mode, you are expected to manually update the `MachineConfiguration` object with new boot image version whenever you update the boot image.

.Procedure

. For manual mode, you can obtain the current boot image on a node by using the following command:
+
[source,terminal]
----
$ oc debug node/<new-node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
.Example output
[source,terminal]
----
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251023-0-ostree.x86_64.ociarchive",
    "version": "9.6.20251023-0"
----
+
You should use the newest node on the cluster, because the boot image might have been updated after the older nodes were created. Ideally, test the newest node from each machine set and use the oldest boot image among them.

. Specify the boot image skew enforcement mode and set the boot image version as needed:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  bootImageSkewEnforcement:
    mode: Manual
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.6.20251023-0
# ...
----
where:

`spec.bootImageSkewEnforcement.mode`:: Specifies the boot image enforcement mode, one of the following values:
+
--
* `Manual`. Specifies that boot image skew management is in manual mode. You must specify the `spec.bootImageSkewEnforcement.manual` parameters.
* `None`. Specifies that boot image skew management is disabled. You do not need to specify the `spec.bootImageSkewEnforcement.manual` parameters.
--

`spec.bootImageSkewEnforcement.manual.mode`:: Specifies the version you want to represent the current boot image, either `OCPVersion` or `RHCOSVersion`. You must include one of the following parameters:
+
--
** For `RHCOSVersion`, use `spec.bootImageSkewEnforcement.manual.rhcosVersion` to specify the {op-system} version that is being used as a boot image in the `[major].[minor].[datestamp(YYYYMMDD)]-[buildnumber]` or `[major].[minor].[timestamp(YYYYMMDDHHmm)]-[buildnumber]` format. This field must be between 14 and 21 characters.
** For `OCPVersion`, use `spec.bootImageSkewEnforcement.manual.ocpVersion` to specify the OpenShift Container Platform version associated with the boot image that is being used in the `x.y.z` format. This field must be between 5 and 10 characters.
--

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-skew-mgmt.adoc

[id="mco-update-boot-skew-mgmt-updating.adoc_{context}"]
= Updating the boot image skew enforcement version

[role="_abstract"]
If you are running boot image skew enforcement in the manual mode, you must manually update the boot image version in the `MachineConfiguration` object each time you update the boot image in your cluster. With the boot image updated in the `MachineConfiguration` object, the Machine Config Operator (MCO) can properly perform boot image skew enforcement to ensure that your nodes are up-to-date.

.Procedure

. If necessary, obtain the {op-system} or OpenShift Container Platform version of the current boot image on an updated node by using one of the following commands:

* Obtain the {op-system} version by running the following command:
+
[source,terminal]
----
$ oc debug node/<new-node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
----
+
.Example output
[source,terminal]
----
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251023-0-ostree.x86_64.ociarchive",
    "version": "9.6.20251023-0"
----

* Obtain the OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
$ openshift-install version
----
+
Ensure that you use the same `openshift-install` binary that you used when updating the boot image.
+
.Example output
[source,terminal]
----
openshift-install 4.22.0
----

. Specify the boot image version in the `MachineConfiguration` object with either the {op-system} or OpenShift Container Platform version:
+
* Update the `MachineConfiguration` object with the {op-system} version:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: Manual
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.2.20251023-0
# ...
----
+
If the `spec.bootImageSkewEnforcement.manual.mode` is `RHCOSVersion`, specify the {op-system} version of the boot image with the `rhcosVersion` parameter, as shown in the example.

* Update the `MachineConfiguration` object with the OpenShift Container Platform version
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: Manual
    manual:
      mode: OCPVersion
      ocpVersion: 4.22.0
# ...
----
+
If the `spec.bootImageSkewEnforcement.manual.mode` is `OCPVersion`, specify the OpenShift Container Platform version of the boot image with the `ocpVersion` parameter, as shown in the example.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Boot image management
* Manually updating the boot image
