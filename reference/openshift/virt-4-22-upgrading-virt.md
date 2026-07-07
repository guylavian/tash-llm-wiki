---
title: "Updating {VirtProductName}"
type: reference
domain: openshift
slug: virt-4-22-upgrading-virt
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/upgrading-virt
version: 4.22
family: virt
documentKind: "Documentation"
---

# Updating {VirtProductName}

[id="upgrading-virt"]
= Updating {VirtProductName}

[role="_abstract"]
Learn how to keep {VirtProductName} updated and compatible with OpenShift Container Platform.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-about-upgrading-virt_{context}"]
= About updating {VirtProductName}

[role="_abstract"]
When you install {VirtProductName}, you select an update channel and an approval strategy. The update channel determines the version of {VirtProductName} that you use. The approval strategy determines whether updates occur automatically or require manual approval. Both settings affect supportability.

[id="recommended-settings_{context}"]
== Recommended settings

To keep a supportable environment, use the following settings:

* Update channel: *stable*
* Approval strategy: *Automatic*

Most {VirtProductName} installations use the *stable* release channel and the *Automatic* approval strategy. Use other settings only if you understand the risks.

With these settings, the update process starts automatically when a new Operator version is available in the *stable* channel. This keeps {VirtProductName} and OpenShift Container Platform versions compatible and ensures that {VirtProductName} is suitable for production environments.

[NOTE]
====
Each minor version of {VirtProductName} is supported only with the corresponding OpenShift Container Platform version. For example, you must run {VirtProductName} {VirtVersion} on OpenShift Container Platform {VirtVersion}.
====

[id="what-to-expect_{context}"]
== What to expect

You can expect consistent update behavior in {VirtProductName}, including duration, automation, and data preservation.

* The time required to complete an update depends on your network connection. Most automatic updates complete within fifteen minutes.

* Updating {VirtProductName} does not interrupt network connections.

* An update preserves data volumes and their associated persistent volume claims.

[IMPORTANT]
====
If virtual machines use hostpath provisioner storage, they cannot be live migrated and might block an OpenShift Container Platform cluster update.

As a workaround, reconfigure the virtual machines so they can power off automatically during a cluster update. Set the `evictionStrategy` field to `None` and the `runStrategy` field to `Always`.
====
[IMPORTANT]
====
If virtual machines use AWS Elastic Block Store (EBS) storage, they cannot be live migrated and might block an OpenShift Container Platform cluster update.

As a workaround, reconfigure the virtual machines so they can power off automatically during a cluster update. Set the `evictionStrategy` field to `None` and the `runStrategy` field to `Always`.
====

[id="how-updates-work_{context}"]
== How updates work

Learn how Operator Lifecycle Manager (OLM) updates the {VirtProductName} Operator and how update channels and approval strategies affect upgrade behavior.

* Operator Lifecycle Manager (OLM) manages the lifecycle of the {VirtProductName} Operator. The Marketplace Operator, deployed during OpenShift Container Platform installation, makes external Operators available to your cluster.

* OLM provides z-stream and minor version updates for {VirtProductName}. Minor version updates become available when you update OpenShift Container Platform to the next minor version. You cannot update {VirtProductName} to the next minor version without first updating OpenShift Container Platform.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-changing-update-settings_{context}"]
= Changing update settings

[role="_abstract"]
You can control how and when updates are installed by changing the update channel and approval strategy for the {CNVOperatorDisplayName} subscription.

.Prerequisites

* You have installed the {CNVOperatorDisplayName}.
* You have logged in to the OpenShift Container Platform web console as a cluster administrator.

.Procedure

. Click *Ecosystem* -> *Installed Operators*.

. Select *{VirtProductName}* from the list.

. Click the *Subscription* tab.

. In the *Subscription details* section, click the setting that you want to change. For example, to change the approval strategy from *Manual* to *Automatic*, click *Manual*.

. In the window that opens, select the new update channel or approval strategy.

. Click *Save*.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-manual-approval-strategy_{context}"]
= Manual approval strategy

[role="_abstract"]
If you use the *Manual* approval strategy, you must approve every pending update. If OpenShift Container Platform and {VirtProductName} updates are out of sync, your cluster becomes unsupported.

To avoid risk to cluster supportability and functionality, use the *Automatic* approval strategy. If you must use the *Manual* approval strategy, approve pending Operator updates as soon as they become available.

// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc
// * virt/updating/upgrading-virt.adoc

[id="olm-approving-pending-upgrade_{context}"]
= Manually approving a pending Operator update

[role="_abstract"]
If an installed Operator has the approval strategy in its subscription set to *Manual*, when new updates are released in its current update channel, the update must be manually approved before installation can begin.

.Prerequisites

* An Operator previously installed using {olm-first}.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators*.

. Operators that have a pending update display a status with *Upgrade available*. Click the name of the Operator you want to update.

. Click the *Subscription* tab. Any updates requiring approval are displayed next to *Upgrade status*. For example, it might display *1 requires approval*.

. Click *1 requires approval*, then click *Preview Install Plan*.

. Review the resources that are listed as available for update. When satisfied, click *Approve*.

. Navigate back to the *Ecosystem* -> *Installed Operators* page to monitor the progress of the update. When complete, the status changes to *Succeeded* and *Up to date*.

// cleaning up unused Operators and resources

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-update-removing-unused_{context}"]
= Remove unused Operators and resources

[role="_abstract"]
When updating {VirtProductName} to version {VirtVersion}, you can remove certain Operators and resources that are no longer required. This helps reclaim space and resources on your cluster.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-rhel-9_{context}"]
= {op-system-base} 9 compatibility

[role="_abstract"]
{VirtProductName} {VirtVersion} is based on {op-system-base-full} 9.

[id="rhel-9-machine-type_{context}"]
== {op-system-base} 9 machine type

All VM templates that are included with {VirtProductName} now use the {op-system-base} 9 machine type by default: `machineType: pc-q35-rhel9.<y>.0`, where `<y>` is a single digit corresponding to the latest minor version of {op-system-base} 9. For example, the value `pc-q35-rhel9.2.0` is used for {op-system-base} 9.2.

Updating {VirtProductName} does not change the `machineType` value of any existing VMs. These VMs continue to function as they did before the update. You can optionally change a VM's machine type so that it can benefit from {op-system-base} 9 improvements.

[IMPORTANT]
====
Before you change a VM's `machineType` value, you must shut down the VM.
====

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-monitoring-upgrade-status_{context}"]
= Monitoring update status

[role="_abstract"]
To monitor the status of a {CNVOperatorDisplayName} update, watch the cluster service version (CSV) `PHASE`. You can also monitor the CSV conditions in the web console or by using the CLI.

[NOTE]
====
The `PHASE` and conditions values are approximations that are based on available information.
====

.Prerequisites

* You have logged in to the OpenShift Container Platform cluster as a cluster administrator.
* You have installed the {oc-first}.

.Procedure

. Run the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get csv -n {CNVNamespace}
----

. Review the output, checking the `PHASE` field. For example:
+
[source,terminal,subs="attributes+"]
----
VERSION  REPLACES                                        PHASE
4.9.0    kubevirt-hyperconverged-operator.v4.8.2         Installing
4.9.0    kubevirt-hyperconverged-operator.v4.9.0         Replacing
----

. Optional: Monitor the aggregated status of all {VirtProductName} component
conditions by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  -o=jsonpath='{range .status.conditions[*]}{.type}{"\t"}{.status}{"\t"}{.message}{"\n"}{end}'
----
+
A successful upgrade results in the following output:
+
[source,terminal]
----
ReconcileComplete  True  Reconcile completed successfully
Available          True  Reconcile completed successfully
Progressing        False Reconcile completed successfully
Degraded           False Reconcile completed successfully
Upgradeable        True  Reconcile completed successfully
----

// workload updates

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-about-workload-updates_{context}"]
= VM workload updates

[role="_abstract"]
When you update {VirtProductName}, virtual machine workloads, including `libvirt`, `virt-launcher`, and `qemu`, update automatically if they support live migration.

[NOTE]
====
Each virtual machine has a `virt-launcher` pod that runs the virtual machine instance (VMI). The `virt-launcher` pod runs an instance of `libvirt`, which is used to manage the virtual machine (VM) process.
====

You can configure how workloads are updated by editing the `spec.workloadUpdateStrategy` stanza of the `HyperConverged` custom resource (CR). There are two available workload update methods: `LiveMigrate` and `Evict`.

Because the `Evict` method shuts down VMI pods, only the `LiveMigrate` update strategy is enabled by default.

When `LiveMigrate` is the only update strategy enabled:

* VMIs that support live migration are migrated during the update process. The VM guest moves into a new pod with the updated components enabled.

* VMIs that do not support live migration are not disrupted or updated.

** If a VMI has the `LiveMigrate` eviction strategy but does not support live migration, it is not updated.

If you enable both `LiveMigrate` and `Evict`:

* VMIs that support live migration use the `LiveMigrate` update strategy.

* VMIs that do not support live migration use the `Evict` update strategy. If a VMI is controlled by a `VirtualMachine` object that has `runStrategy: Always` set, a new VMI is created in a new pod with updated components.

[id="migration-attempts-timeouts_{context}"]
== Migration attempts and timeouts

When updating workloads, live migration fails if a pod is in the `Pending` state for the following periods:

5 minutes:: If the pod is pending because it is `Unschedulable`.

15 minutes:: If the pod is stuck in the pending state for any reason.

When a VMI fails to migrate, the `virt-controller` tries to migrate it again. It repeats this process until all migratable VMIs are running on new `virt-launcher` pods. If a VMI is improperly configured, however, these attempts can repeat indefinitely.

[NOTE]
====
Each attempt corresponds to a migration object. Only the five most recent attempts are held in a buffer. This prevents migration objects from accumulating on the system while retaining information for debugging.
====

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-configuring-workload-update-methods_{context}"]
= Configuring workload update methods

[role="_abstract"]
You can configure how virtual machine workloads are updated during cluster upgrades by editing the `HyperConverged` custom resource (CR).

.Prerequisites

* You have enabled live migration in the cluster.
+
[NOTE]
====
If a `VirtualMachineInstance` CR contains `evictionStrategy: LiveMigrate` and the virtual machine instance (VMI) does not support live migration, the VMI will not update.
====

* You have installed the {oc-first}.

.Procedure

. To open the `HyperConverged` CR in your default editor, run the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace}
----

. Edit the `workloadUpdateStrategy` stanza of the `HyperConverged` CR. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  workloadUpdateStrategy:
    workloadUpdateMethods:
    - LiveMigrate
    - Evict
    batchEvictionSize: 10
    batchEvictionInterval: "1m0s"
# ...
----
** `spec.workloadUpdateStrategy.workloadUpdateMethods` defines the methods that can be used to perform automated workload updates. The available values are `LiveMigrate` and `Evict`. If you enable both options as shown in this example, updates use `LiveMigrate` for VMIs that support live migration and `Evict` for any VMIs that do not support live migration. To disable automatic workload updates, you can either remove the `workloadUpdateStrategy` stanza or set `workloadUpdateMethods: []` to leave the array empty.
*** `LiveMigrate` is the least disruptive update method. VMIs that support live migration are updated by migrating the virtual machine (VM) guest into a new pod with the updated components enabled. If `LiveMigrate` is the only workload update method listed, VMIs that do not support live migration are not disrupted or updated.
*** `Evict` is a disruptive method that shuts down VMI pods during upgrade. `Evict` is the only update method available if live migration is not enabled in the cluster. If a VMI is controlled by a `VirtualMachine` object that has `runStrategy: Always` configured, a new VMI is created in a new pod with updated components.
** `spec.workloadUpdateStrategy.batchEvictionSize` defines the number of VMIs that can be forced to be updated at a time by using the `Evict` method. This does not apply to the `LiveMigrate` method.
** `spec.workloadUpdateStrategy.batchEvictionInterval` defines the interval to wait before evicting the next batch of workloads. This does not apply to the `LiveMigrate` method.
+
[NOTE]
====
You can configure live migration limits and timeouts by editing the `spec.liveMigrationConfig` stanza of the `HyperConverged` CR.
====

. To apply your changes, save and exit the editor.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-viewing-outdated-workloads_{context}"]
= Viewing outdated VM workloads

[role="_abstract"]
You can view a list of outdated virtual machine (VM) workloads by using the CLI.

[NOTE]
====
If there are outdated virtualization pods in your cluster, the `OutdatedVirtualMachineInstanceWorkloads` alert fires.
====

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* To view a list of outdated virtual machine instances (VMIs), run the following command:
+
[source,terminal]
----
$ oc get vmi -l kubevirt.io/outdatedLauncherImage --all-namespaces
----

// control plane updates

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-about-control-plane-only-updates_{context}"]
= Control Plane Only updates

[role="_abstract"]
You can use a Control Plane Only update to move between Extended Update Support (EUS) versions of OpenShift Container Platform. This prevents virtual machine workloads from updating during the intermediate upgrade.

Every even-numbered minor version of OpenShift Container Platform is an Extended Update Support (EUS) version. Kubernetes requires minor version updates to occur in sequence. You cannot update directly from one EUS version to the next.

To move between EUS versions, first update {VirtProductName} to the latest z-stream release of the next odd-numbered minor version. Then update the cluster to the target EUS version of OpenShift Container Platform. After the cluster update, update {VirtProductName} to the target EUS version.

[NOTE]
====
You can update {VirtProductName} directly to the latest z-stream release of your current minor version without applying each intermediate z-stream update.
====

For more information about EUS versions, see the "OpenShift Container Platform Life Cycle Policy".

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-preventing-workload-updates-during-control-plane-only-update_{context}"]
= Preventing workload updates during a Control Plane Only update

[role="_abstract"]
When updating between Extended Update Support (EUS) versions, temporarily disable automatic workload updates. This prevents {VirtProductName} from migrating or evicting virtual machines during the upgrade.

[IMPORTANT]
====
In OpenShift Container Platform 4.16, the underlying {op-system-first} upgraded to version 9.4 of {op-system-base-full}. All `virt-launcher` pods in the cluster must use the same {op-system-base} version.

After upgrading to OpenShift Container Platform 4.16, re-enable workload updates in {VirtProductName}. This allows `virt-launcher` pods to update. Before upgrading to the next OpenShift Container Platform version, verify that all VMIs use up-to-date workloads:

[source,terminal]
----
$ oc get kv kubevirt-kubevirt-hyperconverged -o json -n openshift-cnv | jq .status.outdatedVirtualMachineInstanceWorkloads
----

If the command returns a value greater than `0`, list VMIs with outdated `virt-launcher` pods and start live migration:

[source,terminal]
----
$ oc get vmi -l kubevirt.io/outdatedLauncherImage --all-namespaces
----

For supported OpenShift Container Platform releases and their {op-system-base} versions, see {op-system-base} Versions Utilized by {op-system} and OpenShift Container Platform.
====

.Prerequisites

* You have installed the {oc-first}.
* You are running an EUS version of OpenShift Container Platform and plan to update to the next EUS version.
* You have not yet updated to the intermediate odd-numbered minor version.
* You paused the worker nodes' machine config pools as described in the OpenShift Container Platform documentation.
* Use the default *Automatic* approval strategy. If you use the *Manual* approval strategy, you must approve all pending updates in the web console. For more details, see "Manually approving a pending Operator update".

.Procedure

. Run the following command and record the `workloadUpdateMethods` value:
+
[source,terminal,subs="attributes+"]
----
$ oc get kv kubevirt-kubevirt-hyperconverged \
  -n {CNVNamespace} -o jsonpath='{.spec.workloadUpdateStrategy.workloadUpdateMethods}'
----

. Disable workload update methods by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op":"replace","path":"/spec/workloadUpdateStrategy/workloadUpdateMethods", "value":[]}]'
----

. Ensure that the `HyperConverged` Operator is `Upgradeable`:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} -o json | jq ".status.conditions"
----

. Update your cluster from the source EUS version to the next minor version of OpenShift Container Platform:
+
[source,terminal]
----
$ oc adm upgrade
----

. Verify the current cluster version:
+
[source,terminal]
----
$ oc get clusterversion
----
+
[NOTE]
====
Updating OpenShift Container Platform to the next version is a prerequisite for updating {VirtProductName}. For more details, see the "Updating clusters" section of the OpenShift Container Platform documentation.
====

. Update {VirtProductName}.
+
* With the default *Automatic* approval strategy, {VirtProductName} automatically updates after the OpenShift Container Platform update completes.
* If you use the *Manual* approval strategy, approve the pending update in the web console.

. Monitor the {VirtProductName} update:
+
[source,terminal,subs="attributes+"]
----
$ oc get csv -n {CNVNamespace}
----

. Confirm that {VirtProductName} updated to the latest z-stream release of the intermediate version:
+
[source,terminal,subs="attributes+"]
----
$ oc get {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} -o json | jq ".status.versions"
----

. Wait until the `HyperConverged` Operator again reports the `Upgradeable` condition.

. Update OpenShift Container Platform to the target EUS version.

. Verify the cluster version:
+
[source,terminal]
----
$ oc get clusterversion
----
+
. Update {VirtProductName} to the target EUS version.
+
* With the default *Automatic* approval strategy, {VirtProductName} updates automatically.
* If you use the *Manual* approval strategy, approve the pending update in the web console.

. Monitor the update:
+
[source,terminal,subs="attributes+"]
----
$ oc get csv -n {CNVNamespace}
----
+
The update completes when the `VERSION` field matches the target EUS version and the `PHASE` field reads `Succeeded`.

. Restore the `workloadUpdateMethods` configuration recorded in step 1:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {HCOCliKind} kubevirt-hyperconverged -n {CNVNamespace} --type json -p \
"[{\"op\":\"add\",\"path\":\"/spec/workloadUpdateStrategy/workloadUpdateMethods\", \"value\":{WorkloadUpdateMethodConfig}}]"
----

.Verification

* Check the status of VM migrations:
+
[source,terminal]
----
$ oc get vmim -A
----

.Next steps

* Unpause the machine config pools for each compute node.

// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

[id="virt-early-access-releases_{context}"]
= Early access releases

[role="_abstract"]
You can access development builds by subscribing to the *candidate* update channel for your version of {VirtProductName}.

These releases are not fully tested by Red{nbsp}Hat and are not supported. Use them only on non-production clusters to test new capabilities and bug fixes.

The *stable* channel matches the underlying OpenShift Container Platform version and is fully tested. It is suitable for production systems. You can switch between the *stable* and *candidate* channels in OperatorHub. Updating from a *candidate* release to a *stable* release is not tested by Red{nbsp}Hat.

Red{nbsp}Hat promotes some candidate releases to the *stable* channel. Other candidate releases might not include all GA features. Red{nbsp}Hat might remove some features from candidate builds before GA. Candidate releases might not offer update paths to later GA releases.

[IMPORTANT]
====
Use the candidate channel only for testing where you can delete and re-create the cluster.
====

[id="additional-resources_upgrading-virt"]
[role="_additional-resources"]
== Additional resources
* OpenShift Container Platform Life Cycle Policy
* Performing a Control Plane Only update
* What are Operators?
* Operator Lifecycle Manager concepts and resources
* Cluster service versions (CSVs)
* About live migration
* Configure eviction and run strategies
* Configuring live migration limits and timeouts
