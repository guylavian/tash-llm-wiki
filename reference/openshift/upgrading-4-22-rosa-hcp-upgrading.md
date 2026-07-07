---
title: "Updating {product-title} clusters"
type: reference
domain: openshift
slug: upgrading-4-22-rosa-hcp-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/upgrading/rosa-hcp-upgrading
version: 4.22
family: upgrading
documentKind: "Documentation"
---

# Updating {product-title} clusters

[id="rosa-hcp-upgrading"]
= Updating OpenShift Container Platform clusters

[role="_abstract"]
In OpenShift Container Platform, updating provisions a new component with updated software and uses it to replace an existing component that has outdated software.

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

[id="rosa-upgrade-options_{context}"]
= Update options for OpenShift Container Platform clusters configured with {autonode}

[role="_abstract"]
You can control the impact of updates to your workload by controlling which parts of the cluster are updated.

Update only the hosted control plane:: This initiates update of the hosted control plane. When the cluster is not configured with {autonode}, it does not impact your worker nodes. When the cluster is configured with {autonode}, worker nodes that are part of the default `EC2NodeClass` resource managed by Karpenter are updated along with the {hcp}.

Update nodes in a machine pool:: OpenShift Container Platform machine pool updates are designed to fully replace each node in a machine pool during the update process. This provides additional security and stability benefits over performing an in-place update. Updating the nodes in a machine pool initiates a rolling replacement of nodes in the specified machine pool, and temporarily impacts the worker nodes on that machine pool. You can also update multiple machine pools concurrently.

Update nodes in a Karpenter-managed `EC2NodeClass`:: When {autonode} is enabled, `OpenshiftEC2NodeClass` resource created in the cluster can be upgraded.

[IMPORTANT]
====
You cannot update the hosted control plane at the same time as any machine pool update. You must update the hosted control plane first, and then update machine pools.
====

[IMPORTANT]
====
To maintain compatibility between nodes in the cluster, nodes in machine pools cannot use a newer version than the hosted control plane. This means that the hosted control plane should always be updated to a given version before any machine pools are updated to the same version.
====

You can further control the time required for a machine pool update, and the impact of an update to your workload, by editing the `--max-surge` and `--max-unavailable` values for each machine pool. These options control the number of nodes that can be updated simultaneously on a machine pool, and whether an update provisions excess nodes or makes some existing nodes unavailable or both, for example:

* **To prioritize high workload availability**, you can provision excess nodes instead of making existing nodes unavailable by setting a higher value for `--max-surge` and setting `--max-unavailable` to `0`.
* **To prioritize lower infrastructure costs**, you can make some existing nodes unavailable and avoid provisioning excess nodes by setting a higher value for `--max-unavailable` and setting `--max-surge` to `0`.
* **To prioritize update speed by updating multiple nodes simultaneously**, you can provision excess nodes and allow some existing nodes to be made unavailable by configuring moderate values for both `--max-surge` and `--max-unavailable`.

For more information about these parameters and their usage, see the _ROSA CLI reference_ for `rosa edit machinepool`.

//Additional resources included in assembly.

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

[id="rosa-nodes-autonode-upgrading-autonode_{context}"]
= Understanding upgrades for OpenShift Container Platform clusters configured with {autonode}

[role="_abstract"]
You can upgrade clusters that are configured with {autonode}.

[id="rosa-nodes-autonode-upgrading-autonode-openshiftec2nodeclass_{context}"]
*Default `OpenshiftEC2NodeClass`*

When you enable {autonode}, a default `OpenshiftEC2NodeClass` resource is created with the same version as that of the hosted control plane. All node pools that reference the default `EC2NodeClass` are automatically upgraded as part of the hosted control plane upgrade.

[id="rosa-nodes-autonode-upgrading-autonode-secondary-openshiftec2nodeclass_{context}"]
*Optional `OpenshiftEC2NodeClass`*

Upgrade behavior depends on whether or not the `OpenshiftEC2NodeClass` is pinned to a version by using the `spec.version` field.

Unpinned `OpenshiftEC2NodeClass`:: By default, `OpenshiftEC2NodeClass` resources have the same version of the hosted control plane. When the hosted control plane is upgraded, unpinned `OpenshiftEC2NodeClass` resources are automatically upgraded.

Pinned `OpenshiftEC2NodeClass`:: In the `OpenshiftEC2NodeClass` resource, you can specify a valid {ocp-short} version in `spec.version`. Specifying this version pins the cluster's node pools to a specific version. Any pinned `OpenshiftEC2NodeClass` resources are not upgraded as part of the hosted control plane upgrade. You can update the `spec.version` of pinned `OpenshiftEC2NodeClass` resources to a valid version. Updating this `spec.version` field initiates the upgrade of all of the node pools that reference its corresponding `OpenshiftEC2NodeClass` resource.

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

[id="rosa-upgrading-lifecycle-policy_{context}"]
= Life cycle policies and planning

[role="_abstract"]
To plan an upgrade, see the _Red Hat OpenShift Service on AWS update life cycle_ in the "Additional resources" section.
The life cycle page includes release definitions, support and update requirements, installation policy information and life cycle dates.

Updates are manually initiated or automatically scheduled. Red Hat Site Reliability Engineers (SREs) monitor update progress and remedy any issues encountered.

You can use update channels to decide which OpenShift Container Platform minor version to update your clusters to. OpenShift Container Platform supports updates through the `stable-4.y`, `eus-4.y`, and `fast-4.y` channels.

//The following note should be removed when the entire HCP fleet is confirmed multi-arch
[NOTE]
====
If your control plane is not currently multi-architecture enabled, the update process will first migrate the cluster to a multi-architecture image and then apply the version update. Multi-architecture clusters are capable of running both x86-based and Arm-based workloads. Clusters created after 25 July, 2024 are multi-architecture enabled by default.
====

[id="rosa-hcp-upgrading-channels_{context}"]
= Channels in OpenShift Container Platform clusters

[role="_abstract"]
You can use OpenShift Container Platform channels to view available cluster update options and apply patches or z-stream updates in your existing channel. You can also view the update path to newer y-stream versions if available.

== Channel groups and channels
Channel groups in OpenShift Container Platform are similar to channels, but there is no specific version with channel groups. When you select a channel group, your OpenShift Container Platform cluster receives z-stream updates for your current channel group. These channel groups typically include:

* `fast`: cluster receives the latest updates as soon as they are available.
* `stable`: cluster receives updates after they have been thoroughly tested.
* `eus`: Extended Update Support channel, allowing for extended support for even-numbered versions, for example, 4.16, 4.18, or 4.20.

By moving from channel groups to channels, you can have more control over your cluster updates. Instead of receiving patch/z-stream updates only for a particular channel group, by using channels you can view the available updates associated with a minor release version, and determine if there is a path available to that minor/y+1/y+2 version.

[IMPORTANT]
====
The channel group option is being deprecated. If you set a channel group only, OpenShift Container Platform will default to preserving the current channel's target version. For example, a `stable-4.20` cluster moving to the `eus` channel group will use the `eus-4.20` channel by default, if the current cluster version is a member of the `eus-4.20` channel.
====

== Cluster update options
The process for updating your cluster is based on the updates that are available for your current version, and what level of release you are interested in, such as z-stream or y-stream updates.

* *Patch (z-stream) updates*: You do not need to change the channel when performing a patch update within your current minor version. For example, if you have your cluster at version 4.19.12, you can stay within your current `stable-4.19` channel, and decide to update your cluster when there are updates available, such as 4.19.13, 4.19.14, 4.19.17, 4.19.20 until you have the latest updates for that minor version.

* *Minor version (y-stream) updates*: To update to a new minor release, you must change the channel to the next release channel.
+
For example, if you have your cluster at version 4.19.12, you can switch the channel to `stable-4.20` or `stable-4.21` and check if there is an update path available for those versions.
+
If `stable-4.20` has an update path available, it shows you the z-stream updates for your current version, as well as the updates to the y+1 version, such as 4.19.14, 4.19.17, 4.19.20, 4.19.23, 4.19.27, 4.20.0.
+
If you select `stable-4.21`, the available updates might be 4.19.14, 4.19.17, 4.19.20, 4.19.23, 4.19.27, 4.20.0, 4.20.3, 4.20.4, 4.20.6, 4.20.7, with all the z-stream/patch updates displayed right through to the y+2 version of 4.21.0.

You can change your cluster's channel either through the Cluster Overview → Details page in the web console or by using the `rosa edit cluster` command in {rosa-cli}.

When you have set the channel and an update is initiated, the Cluster Version Operator (CVO) retrieves the target release image and begins applying the changes to the cluster.

[NOTE]
====
The *Channel groups* option is now deprecated in OpenShift Container Platform. Channel groups allowed you to upgrade through the available patch/z-stream updates for a particular channel group, such as stabe or eus.
There was the possibility of inadvertently upgrading to the next minor version/Y+1 version if it appeared in the available updates.
====

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

[id="rosa-hcp-upgrading-switch-channels_{context}"]
= Switch channels to view available upgrade options

[role="_abstract"]
You can switch the channel on a OpenShift Container Platform cluster to access update options within a current minor version (y-stream), or the subsequent minor versions (y+1, y+2). The version number in the channel represents the target minor version.

For example, if your cluster is on `stable-4.18`, switching the channel to `stable-4.19` shows update paths from 4.18.z to 4.19.z, if such paths are available. This strategy ensures that administrators must explicitly initiate minor version updates, and they never occur automatically.

.Procedure

. Log in to {cluster-manager-url}.
. Click *Fleet Management* > *Clusters*.
. Select the cluster for which you want to see the update options.
. To view the cluster details, click the *Overview* tab.
  * The *Channel* field displays the current update channel for the cluster.
. Select the new update channel.
.. In the *Channel* field, click the *Edit channel* icon next to the current channel name.
.. On the *Edit channel* dialog, select the required channel version.
.. Click *Save*.
** The *Channel* field updates to display the new update channel.
** The *Version* field displays the *Update* link if updates are available for your selected channel.

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

// NOTE: This module is included several times in the same update assembly.

[id="rosa-hcp-upgrading-cli-control-plane_{context}"]
// HCP-ONLY: Conditions for updating the hosted control plane WITHOUT updating any machine pools
= Updating the hosted control plane with the {rosa-cli}

[role="_abstract"]
You can manually update the hosted control plane of a OpenShift Container Platform cluster by using the {rosa-cli-first}. This method schedules the control plane for an update if a more recent version is available, either immediately, or at a specified future time.

[NOTE]
====
Your control plane only supports machine pools within two minor y-stream versions. For example, a OpenShift Container Platform cluster with a control plane using version 4.17.z supports machine pools with version 4.15.z and 4.16.z, but the control plane does not support machine pools using version 4.14.z.
====

//END HCP-ONLY conditions

// WHOLE CLUSTER: Condition for updating hosted control plane as part of updating the whole cluster in sequence
= Updating the hosted control plane

When you need to update the whole cluster, update the hosted control plane first.

.Prerequisites
* You have installed and configured the latest version of the ROSA CLI.
* No machine pool updates are in progress or scheduled to take place at the same time as the hosted control plane update.

//END WHOLE CLUSTER conditions

.Procedure

. Verify the current version of your cluster by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name_or_id>
----
Replace `<cluster_name_or_id>` with the cluster name or the cluster ID.

. List the versions that you can update your control plane to by running the following command:
+
[source,terminal]
----
$ rosa list upgrade --cluster=<cluster_name_or_id>
----
+
The command returns a list of available updates, including the recommended version.
+
*Example output*
+
[source,terminal]
----
VERSION  NOTES
4.18.18   recommended
4.18.17
4.18.16
----

. Set the update channel. For more information about channels, refer to "Channels in OpenShift Container Platform clusters".
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name_or_id> --channel <channel>
----
For example, to set the channel to `stable-4.19`:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name_or_id> --channel stable-4.19
----

. Update the cluster's hosted control plane by running the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster_name_or_id> [--schedule-date=<yyyy-mm-dd> --schedule-time=<HH:mm>] --version <version_number>
----

** To schedule an immediate update to the specified version, run the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster_name_or_id> --version <version_number>
----
+
Your hosted control plane is scheduled for an immediate update.

** To schedule an update to the specified version at a future date, run the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster_name_or_id> --schedule-date=<yyyy-mm-dd> --schedule-time=<HH:mm> --version=<version_number>
----
+
Your hosted control plane is scheduled for an update at the specified time in Coordinated Universal Time (UTC).

.Troubleshooting
* Sometimes a scheduled update does not initiate. See Upgrade maintenance canceled for more information.

// Module included in the following assemblies:
//
// * upgrading/rosa-hcp-upgrading.adoc

// NOTE: This module is included several times in the same update assembly.

[id="rosa-hcp-upgrading-cli-machinepool_{context}"]
// POOL-ONLY: Conditions for upgrading machine pools WITHOUT upgrading hosted control planes
= Updating machine pools with the {rosa-cli}

[role="_abstract"]
You can manually update one or more machine pools in a OpenShift Container Platform cluster by using the {rosa-cli-first}. This method schedules the specified machine pool for an update if a more recent version is available, either immediately, or at a specified future time.

[NOTE]
====
Your control plane only supports machine pools within two minor y-stream versions. For example, a OpenShift Container Platform cluster with a control plane using version 4.19.z supports machine pools with version 4.17.z and 4.18.z, but the control plane does not support machine pools using version 4.16.z.
====

.Prerequisites
* You have installed and configured the latest version of the {rosa-cli}.
* No updates for the hosted control plane are in progress on the cluster, or scheduled to occur at the same time as the machine pool update.
//END POOL-ONLY condition

// WHOLE CLUSTER: Conditions for upgrading machine pools as part of upgrading the whole cluster in sequence
= Upgrading machine pools

When your hosted control plane update is complete, you can update one or more machine pools.
//END WHOLE CLUSTER condition

[NOTE]
====
Machine pool configurations such as node drain timeout, max-unavailable, and max-surge can affect the timing and success of updates.
====

.Procedure
. Verify the current version of your cluster by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name_or_id>
----
Replace `<cluster_name_or_id>` with the cluster name or the cluster ID.
+

*Example output*
+
[source,terminal]
----
OpenShift Version:     4.17.0
----
*Example output*
+
[source,terminal]
----
OpenShift Version:     4.17.8
----
//WHOLE CLUSTER: updating the version here to show after hcp update in whole cluster section

. List the versions that you can update your machine pools to by running the following command:
+
[source,terminal]
----
$ rosa list upgrade --cluster <cluster-name> --machinepool <machinepool_name>
----
+
The command returns a list of available updates, including the recommended version.
+
*Example output*
+
[source,terminal]
----
VERSION  NOTES
4.17.5   recommended
4.17.4
4.17.3
----
+
[IMPORTANT]
====
Do not update your machine pool to a version higher than your control plane. If you want to move to a higher version, update the control plane to that version first.
====
//Is it even possible to do this? Will a higher version display? Can you specify a higher version even if it doesn't display?

. Verify the update behavior of the machine pools you intend to update by running the following command:
+
[source,terminal]
----
$ rosa describe machinepool --cluster=<cluster_name_or_id> <machinepool_name>
----
+
*Example output*
+
[source,terminal]
----
Replicas: 5
Node drain grace period:   30 minutes

Management update:
- Type: Replace
- Max surge: 20%
- Max unavailable: 20%
----
+
In the example, these settings allow the machine pool to provision one excess node (`max-surge` of 20% of `replicas`) and to have up to one node unavailable (`max-unavailable` of 20% of `replicas`) during an update. This machine pool can therefore update two nodes at a time, by provisioning one new node in excess of the replica count, and by making one node unavailable and replacing it. Node updates may be delayed by up to 30 minutes (`node-drain-grace-period` of 30 minutes) if necessary to protect workloads that have a pod disruption budget.

. Update a machine pool by running the following command:
+
[source,terminal]
----
$ rosa upgrade machinepool -c <cluster_name> <machinepool_name> [--schedule-date=<yyyy-mm-dd> --schedule-time=<HH:mm>] --version <version_number>
----
+
You can update multiple machine pools concurrently by running this command for each machine pool you want to update.

** To schedule the immediate update of a machine pool, run the following command:
+
[source,terminal]
----
$ rosa upgrade machinepool -c <cluster_name> <machinepool_name> --version <version_number>
----
+
The machine pool is scheduled for immediate update, which initiates a rolling replacement of all nodes in the specified machine pool.

** To schedule an update to start at a future time, run the following command:
+
[source,terminal]
----
$ rosa upgrade machinepool -c <cluster_name> <machinepool_name> --schedule-date=<yyyy-mm-dd> --schedule-time=<HH:mm> --version <version_number>
----
+
The machine pool is scheduled to begin an update at the specified time and date in Coordinated Universal Time (UTC). This initiates a rolling replacement of all nodes in the specified machine pool, beginning at the specified time.

[role="_additional-resources"]
.Additional resources
* ROSA CLI reference: `rosa edit machinepool`
* Node lifecycle
* OpenShift Container Platform update life cycle
