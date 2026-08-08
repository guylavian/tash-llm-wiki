---
title: "Boot image management"
type: reference
domain: openshift
slug: nodes-4-22-nodes-update-boot-images
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-update-boot-images
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Boot image management

[id="nodes-update-boot-images"]
= Boot image management

[role="_abstract"]

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-update-boot-images.adoc
// * machine_configuration/mco-update-boot-images.adoc

[id="mco-update-boot-images_{context}"]
= About boot image management

[role="_abstract"]
With boot image management enabled, the Machine Config Operator (MCO) manages and updates the {op-system-first} version of the boot image in the machine sets for your control plane or worker nodes. This means that the MCO updates the boot image whenever you update your cluster. Without boot image management enabled, if your cluster was originally created with an older OpenShift Container Platform version, the boot image that the MCO would use to create new nodes is an older {op-system-first} version, even if your cluster is at a later OpenShift Container Platform version.

New nodes created after enabling the feature use the updated boot image. This feature has no effect on existing nodes.

[NOTE]
====
====

For example, with the feature disabled, if your cluster was originally created with OpenShift Container Platform 4.16, the boot image that the MCO would use to create new nodes is the same {op-system} version that was installed for the cluster, even if your cluster is currently at a later OpenShift Container Platform version.

Using an older boot image could cause the following issues:

* Extra time to start nodes
* Certificate expiration issues
* Version skew issues

You can disable the boot image management feature, if needed. When the feature is disabled, the boot image version no longer updates with the cluster. For example, you could disable the boot image management feature in order to use a custom boot image that you do not want changed. For information on how to disable this feature, see "Disabling boot image management". If you disable this feature, you can re-enable the feature at any time. For information, see "Enabling boot image management".

How the cluster behaves after disabling or re-enabling the feature, depends upon when you made the change, including the following scenarios:

* If you disable the feature before updating to a new OpenShift Container Platform version:
** The boot image version used by the machine sets remains the same OpenShift Container Platform version as when the feature was disabled.
** When you scale up nodes, the new nodes use that same OpenShift Container Platform version.

* If you disable the feature after updating to a new OpenShift Container Platform version:
** The boot image version used by the machine sets is updated to match the updated OpenShift Container Platform version.
** When you scale up nodes, the new nodes use the updated OpenShift Container Platform version.
** If you update to a later OpenShift Container Platform version, the boot image version in the machine sets remains at the current version and is not updated with the cluster.

* If you enable the feature after disabling:
** The boot image version used by the machine sets is updated to the current OpenShift Container Platform version, if different.
** When you scale up nodes, the new nodes use the current OpenShift Container Platform version in the cluster.

[NOTE]
====
Because a boot image is used only when a node is scaled up, this feature has no effect on existing nodes.
====

To view the current {op-system-first} boot image version used in your cluster, you can view the `/sysroot/.coreos-aleph-version.json` file on that node.

.Example coreos-aleph-version.json file with an older boot image
[source,yaml]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-418.94.202511191518-0-ostree.x86_64.ociarchive",
    "version": "418.94.202511191518-0"
}
----
where:

`<version>`:: Specifies the {op-system-first} boot image version. In this example, the boot image is from the originally-installed OpenShift Container Platform 4.18 version, regardless of the current version of the cluster.

// The following admonition is intended to address https://issues.redhat.com/browse//OSDOCS-14592
[IMPORTANT]
====
If any of the machine sets for which you want to enable boot image management use a `*-user-data` secret that is based on Ignition version 2.2.0, the Machine Config Operator converts the Ignition version to 3.4.0 when you enable the feature. OpenShift Container Platform versions 4.5 and lower use Ignition version 2.2.0. If this conversion fails, the MCO or your cluster could degrade. An error message that includes _err: converting ignition stub failed: failed to parse Ignition config_ is added to the output of the `oc get ClusterOperator machine-config` command. You can use the following general steps to correct the problem:

. Disable the boot image management feature. For information, see "Disabling boot image management".
. Manually update the `*-user-data` secret to use Ignition version to 3.2.0.
. Enable the boot image management feature. For information, see "Enabling boot image management".
====

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-images.adoc
// * nodes/nodes/nodes-update-boot-images.adoc

[id="mco-update-boot-images-disable_{context}"]
= Disabling boot image management

[role="_abstract"]
You can disable the boot image management feature so that the Machine Config Operator (MCO) no longer manages or updates the boot image in the affected machine sets. For example, you could disable this feature for the worker nodes in order to use a custom boot image that you do not want changed.

[NOTE]
====
If you are updating an {azure-first} or {vmw-first} cluster from OpenShift Container Platform 4.21 to 4.22, and you have not configured the `managedBootImages` parameter, the update is blocked with the message: `This cluster is Azure or vSphere but lacks a boot image configuration`. The update is intentionally blocked on {azure-short} or {vmw-short} clusters in order to alert you that the default boot image management behavior is changing between version 4.21 and 4.22 in order to enable boot images management by default on those platforms.

To allow the update, perform one of the following tasks:

* If you want to allow the feature to be enabled, acknowledge that you are aware of the change in the default behavior by patching the `admin-acks` config map by running the following command:
+
[source,terminal]
----
$ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.21-boot-image-opt-out-in-4.22":"true"}}' --type=merge
----

* If you do not want the boot image management feature enabled, explicitly disable the feature for worker machine sets by using the following procedure.
====

You disable the boot image management feature for the control plane or worker machine sets in your cluster by editing the `MachineConfiguration` object.

[NOTE]
====
====

Disabling this feature does not rollback the nodes or machine sets to the originally-installed boot image. The machine sets retain the boot image version that was present when the feature was disabled and is not updated if the cluster is upgraded to a new OpenShift Container Platform version in the future. This feature has no effect on existing nodes.

If boot image management is disabled, you must update the boot image version that is used by the boot image skew enforcement feature to ensure that the boot image is current for your cluster. For more information, see "Boot image skew enforcement".

After disabling the feature, you can re-enable the feature at any time. For more information, see "Enabling updated boot images".

.Procedure

. Edit the `MachineConfiguration` object, named `cluster`, by using the following command::
+
[source,terminal]
----
$ oc edit MachineConfiguration cluster
----

. Disable the feature for some or all of your machine sets by making one or both of the following changes:

* Disable the feature for nodes in the worker machine sets by adding the following parameters:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: None
----
+
--
where:

`spec.managedBootImages`:: Specifies the parameters for the boot image management feature.

`spec.managedBootImages.machineManagers.apiGroup`:: Specifies the API group. This must be `machine.openshift.io`.

`spec.managedBootImages.machineManagers.resource`:: Specifies that the `selection.mode` parameter applies to worker nodes when a value of `machinesets` is set.

`spec.managedBootImages.machineManagers.selection.mode`:: When `None`, specifies that the feature is disabled for the specified machine sets.
--

* Disable the feature for nodes in the control plane machine sets by adding the following parameters:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: None
----
+
--
where:

`spec.managedBootImages`:: Specifies the parameters for the boot image management feature.

`spec.managedBootImages.machineManagers.apiGroup`:: Specifies the API group. This must be `machine.openshift.io`.

`spec.managedBootImages.machineManagers.resource`:: Specifies that the `selection.mode` parameter applies to control plane nodes when a value of `controlplanemachinesets` is set.

`spec.managedBootImages.machineManagers.selection.mode`:: When `None`, specifies that the feature is disabled for the specified machine sets.
--

Hiding per djoshy https://github.com/openshift/openshift-docs/pull/93065#pullrequestreview-2844549815
* Optional: Disable the default behavior for specific machine sets:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: Partial
        partial:
          machineResourceSelector:
            matchLabels:
              region: "east"
----
where:

`spec.managedBootImages`:: Specifies the configuration of the boot image management feature.
`spec.managedBootImages.machineManagers.apiGroup`:: Specifies an API group. This must be `machine.openshift.io`.
`spec.managedBootImages.machineManagers.resource`:: Specifies the resource within the specified API group to apply the change. This must be `machinesets`.
`spec.managedBootImages.machineManagers.selection.mode`:: Specifies that the feature is disabled for specific machine sets.
`spec.managedBootImages.machineManagers.selection.partial.machineResourceSelector`:: Specifies that the feature is enabled only for machine sets with these labels. The feature is disabled for any machine set that does not contain the listed labels.

.Verification

* View the current state of the boot image management feature by using the following command to view the machine configuration object:
+
[source,terminal]
----
$ oc get machineconfiguration cluster -o yaml
----
+
.Example machine set with the boot image reference
[source,yaml]
----
kind: MachineConfiguration
metadata:
  name: cluster
# ...
status:
  conditions:
  - lastTransitionTime: "2025-05-01T20:11:49Z"
    message: Reconciled 2 of 4 MAPI MachineSets | Reconciled 0 of 0 CAPI MachineSets
      | Reconciled 0 of 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "True"
    type: BootImageUpdateProgressing
  - lastTransitionTime: "2025-05-01T19:30:13Z"
    message: 0 Degraded MAPI MachineSets | 0 Degraded CAPI MachineSets | 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "False"
    type: BootImageUpdateDegraded
  managedBootImagesStatus:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: None
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
----
+
--
where:

`status.managedBootImagesStatus.machineManagers.selection.mode`:: Specifies that the boot image management feature is disabled when set to `None`. In this example, the boot image management feature is disabled for control plane machine sets and enabled for worker machine sets.
--

// Module included in the following assemblies:
//
// * machine-configuration/mco-update-boot-images.adoc
// * nodes/nodes/nodes-update-boot-images.adoc

[id="mco-update-boot-images-configuring_{context}"]
= Enabling boot image management

[role="_abstract"]

[NOTE]
====
====

To enable the boot image management feature for control plane machine sets or to re-enable the boot image management feature for worker machine sets where it was disabled, edit the `MachineConfiguration` object. You can enable the feature for all of the machine sets in the cluster or specific machine sets.

[NOTE]
====
Because the boot image management feature for worker nodes is default for the {gcp-short} and {aws-short} platforms, the `managedBootImages` configuration does not appear in the machine configuration object. To enable the feature for control plane machine sets without disabling the feature for worker machine sets, you must expressly add the configuration for both the control plane and worker machine sets, as shown in the following procedure. If you add only the configuration for control plane machine sets, due to default behavior, the Machine Config Operator (MCO) overwrites the configuration for the worker machine sets.
====

Enabling the feature updates the boot image to the {op-system-first} boot image version appropriate for your cluster. If the cluster is again updated to a new OpenShift Container Platform version in the future, the boot image is updated again. New nodes created after enabling the feature use the updated boot image. This feature has no effect on existing nodes.

When boot image management is enabled, the MCO automatically enables boot image skew enforcement to ensure that the boot image version is compliant for your cluster. For more information, see "Boot image skew enforcement".

.Procedure

. Edit the `MachineConfiguration` object, named `cluster`, by using the following command:
+
[source,terminal]
----
$ oc edit MachineConfiguration cluster
----

. Enable the boot image management feature for some or all of your machine sets:

* Enable the boot image management feature for all machine sets:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: All
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
----
+
--
where:

`spec.managedBootImages`:: Configures the boot image management feature.

`spec.managedBootImages.machineManagers.apiGroup`:: Specifies the API group. This must be `machine.openshift.io`.

`spec.managedBootImages.machineManagers.resource`:: Specifies the resource within the specified API group to apply the change. Use one or both of the following parameters. You must add the full stanza, as shown, if you want to enable the feature for control plane and worker machine sets.

* `controlplanemachinesets`: Enables boot image management for control plane machine sets.
* `machinesets`: Enables boot image management for worker machine sets.

`spec.managedBootImages.machineManagers.selection.mode`:: Specifies that the feature is enabled for all machine sets in the cluster.
--

* Enable the boot image management feature for specific worker machine sets:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: Partial
        partial:
          machineResourceSelector:
            matchLabels:
              region: "east"
----
+
--
where:

`spec.managedBootImages`:: Configures the boot image management feature.

`spec.managedBootImages.machineManagers.apiGroup`:: Specifies the API group. This must be `machine.openshift.io`.

`spec.managedBootImages.machineManagers.resource`:: Specifies the resource within the specified API group to apply the change. This must be `machinesets`. Partial boot image management for control plane machine sets is not supported.

`spec.managedBootImages.machineManagers.selection.mode`:: Specifies that the feature is enabled for specific machine sets in the cluster. This must be `Partial`.

`spec.managedBootImages.machineManagers.selection.partial`:: Specifies that the feature is enabled for machine sets with the specified label in their `MachineSet` object.
--

.Verification

. View the current state of the boot image management feature by using the following command to view the machine configuration object:
+
[source,terminal]
----
$ oc get machineconfiguration cluster -o yaml
----
+
.Example machine set with the boot image reference
[source,yaml]
----
kind: MachineConfiguration
metadata:
  name: cluster
# ...
status:
  conditions:
  - lastTransitionTime: "2025-05-01T20:11:49Z"
    message: Reconciled 2 of 4 MAPI MachineSets | Reconciled 0 of 0 CAPI MachineSets
      | Reconciled 0 of 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "True"
    type: BootImageUpdateProgressing
  - lastTransitionTime: "2025-05-01T19:30:13Z"
    message: 0 Degraded MAPI MachineSets | 0 Degraded CAPI MachineSets | 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "False"
    type: BootImageUpdateDegraded
  managedBootImagesStatus:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: All
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
----
+
--
where:

`status.managedBootImagesStatus.machineManagers.selection.mode`:: Specifies that the boot image management feature is enabled when set to `All`.
--

. Scale a machine set to create a new node by using a command similar to the following. The boot image is updated only for new nodes.
+
[source,terminal]
----
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
----

. If your cluster was using an older boot image version, you can see the new boot image version when the new node reaches the `READY` state. View the {op-system-first} version on a nodes:

.. Log in to the node by using a command similar to the following:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

.. Set `/host` as the root directory within the debug shell by using the following command:
+
[source,terminal]
----
sh-5.1# chroot /host
----

.. View the `/sysroot/.coreos-aleph-version.json` file by using a command similar to the following:
+
[source,terminal]
----
sh-5.1# cat /sysroot/.coreos-aleph-version.json
----
+
.Example output
[source,yaml]
----
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251015-1"
}
----
where:

`<version>`:: Specifies the boot image version.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Disabling boot image management
* Enabling boot image management
* Manually updating the boot image
