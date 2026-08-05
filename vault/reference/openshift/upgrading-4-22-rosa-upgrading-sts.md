---
title: "Upgrading {product-title} clusters"
type: reference
domain: openshift
slug: upgrading-4-22-rosa-upgrading-sts
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/upgrading/rosa-upgrading-sts
version: 4.22
family: upgrading
documentKind: "Documentation"
---

# Upgrading {product-title} clusters

[id="rosa-upgrading-sts"]
= Upgrading OpenShift Container Platform clusters

[role="_abstract"]
Use one of the following methods to upgrade OpenShift Container Platform clusters:

* Manually through the {rosa-cli-first} - Start a one-time immediate upgrade or schedule a one-time upgrade for a future date or time.
* Manually through the {cluster-manager} UI - Start a one-time immediate upgrade or schedule a one-time upgrade for a future date or time; or schedule an upgrade window for automatic recurring upgrades whenever a new z-version is available.

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

[id="rosa-upgrading-channels_{context}"]
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
// * upgrading/rosa-upgrading-sts.adoc

[id="rosa-sts-upgrading-a-cluster-with-sts_{context}"]
= Upgrading a OpenShift Container Platform cluster

[role="_abstract"]
Upgrade your OpenShift Container Platform clusters using either the {rosa-cli-first} or the {cluster-manager} console. While both methods verify compatibility, the {rosa-cli} can automatically align {AWS} {sts-first} policies to the target version, ensuring your IAM roles meet all security requirements for the new release.

[NOTE]
====
The actual start time of the cluster upgrade will be within one hour of the upgrade schedule time. Additionally, the duration of the upgrade might vary based on your workload configuration.
====

When a OpenShift Container Platform cluster that uses AWS Security Token Services (STS) is upgraded, the {rosa-cli} verifies the account and Operator role policies for the chosen cluster are compatible with the target version of the upgrade. If the policies are compatible, the CLI automatically upgrades the cluster. If the policies are not compatible with the chosen upgrade version, the CLI automatically upgrades IAM policies before upgrading the cluster. When scheduling the upgrade, you give administrative acknowledgment to confirm you have reviewed the changes involved with the upgrade, if required.

// Module included in the following assemblies:
//
// upgrading/rosa-upgrading-sts.adoc

[id="rosa-how-upgrades-work_{context}"]
= How OpenShift Container Platform cluster upgrades work

[role="_abstract"]
Upgrades are manually initiated (one-time) or automatically scheduled (recurring). Red{nbsp}Hat Site Reliability Engineers (SREs) monitor upgrade progress and either proactively notify you to take corrective actions or remedy issues encountered.

The Cluster Version Operator (CVO) is the primary component that orchestrates and facilitates the OpenShift Container Platform update process.

The Managed Upgrade Operator (MUO) handles the scheduling, monitoring, and notifications of OpenShift Container Platform cluster upgrades. The MUO orchestrates the automated in-place cluster upgrades by ensuring the operating conditions are met before and after the upgrade of a managed cluster.

[id="rosa-upgrade-scheduled-time_{context}"]
== Cluster upgrade scheduled time

You can schedule cluster upgrades by setting the scheduled time. This is when the preparation for the cluster upgrade begins with pre-upgrade health checks and additional compute capacity creation. The actual cluster upgrade starts within one hour from the scheduled time. You receive an email notification when the cluster upgrade starts.

The Pre-Health Check (PHC) provides extra protection to ensure the scheduled update proceeds as expected and runs in the following two scenarios:

* If an upgrade is scheduled for more than 2 hours from the current time, the PHC runs and the user is notified if there are any failures. This PHC is in the _New_ phase of the upgrade.
* When the upgrade is immediate or within 2 hours, the PHC runs just before the upgrade begins. This PHC is in the _Upgrading_ phase of the upgrade.
This means that PHC is always run at least one time during the upgrading phase but can also be run additionally in advance if the upgrade is scheduled for more than 2 hours from the current time.

You can observe the status of the cluster upgrade by running the `rosa describe upgrade --cluster=<cluster name_or_id>` command in the ROSA CLI (`rosa`).

[id="rosa-cluster-upgrade-overview_{context}"]
== OpenShift Container Platform upgrade overview

The following are the high-level steps that occur during the OpenShift Container Platform cluster update:

. Scheduling the upgrade in advance triggers the `PreHealthCheck` and notifies users of any failures that they can then address before the upgrade begins.
. Before the cluster upgrade begins, a cluster health check is performed by the MUO. If the MUO identifies an issue that requires corrective action, you will be notified. Some examples of the cluster health checks that MUO performs include:
** Identifying any Pod Disruption Budgets (PDBs) that can potentially block or delay the update of the nodes.
** Ensuring cluster Operators are available and healthy.
** Ensuring cluster critical alerts are not firing.
. A temporary compute node is created in each availability zone (AZ) in the cluster to allow for the scheduling of drained pods during the update.
+
[NOTE]
====
The temporary compute node creation does not always happen. For example, if there is no `worker` machine pool, the temporary compute node will not be created. This might happen when a cluster admin deletes the existing `worker` machine pool and creates another `worker` machine pool with a different name or instance type.
====
. The cluster version is set to the target version.
+
[NOTE]
====
In certain situations, an upgrade path can become unavailable since the time the cluster update was requested but before it was completed. In such cases, the upgrade is automatically canceled and a notification is sent. You must pick another target version to request the upgrade.
====
+
. During the upgrade, the control plane components are updated to the new version.
. Next, individual cluster Operators perform update tasks on their domain of the cluster.
. Finally, the MCO updates the system configuration and operating system of every node. During this step, each node is rebooted after successfully draining the workloads running on the node.
.. During the update of each node, workloads are drained, honoring the PDBs. Workloads with PDBs that do not allow disruptions essentially block the draining of the node, increasing the elapsed time for the cluster update.
.. During the update of every node in the cluster, the cluster update waits until the time specified by the _node drain grace period_ to allow for safely draining the workloads. Upon reaching the node drain grace period, the node is forcibly drained to allow for cluster upgrade to progress. You can only configure the node drain grace period before initiating the upgrade and you cannot change it after the cluster upgrade begins.
.. When cluster nodes are updated, the MCO selects one node at a time per machine config pool according to their age, starting with the oldest.

// Module included in the following assemblies:
//
// * upgrading/rosa-upgrading-sts.adoc

[id="rosa-upgrading-cli_{context}"]
= Updating with the {rosa-cli}

[role="_abstract"]
You can use the {rosa-cli-first} to update a OpenShift Container Platform cluster either immediately within one hour or at a future time.

.Prerequisites

* You have installed and configured the latest {rosa-cli} on your installation host.
* Your OpenShift Container Platform cluster is in a `Ready` state.

.Procedure

. To verify the current version of your cluster, enter the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name_or_id>
----
Replace `<cluster_name_or_id>` with the cluster name or the ID of the cluster.

. To verify that an upgrade is available, enter the following command:
+
[source,terminal]
----
$ rosa list upgrade --cluster=<cluster_name_or_id>
----
+
The command returns a list of versions to which the cluster can be upgraded, including a recommended version. The recommendation is based on the conditional update risks. Each known risk might apply to all clusters or only clusters matching certain conditions. Refer to the OpenShift release notes to evaluate, validate and determine the appropriate version to upgrade to.

. Set the update channel. For more information about channels, refer to "Understanding update channels and releases" listed in the _Additional resources_.
+
[source,terminal]
----
$ rosa edit -c <cluster_name_or_id> --channel <channel>
----
+
For example, to set the channel to `stable-4.19`:
+
[source,terminal]
----
$ rosa edit -c <cluster_name_or_id> --channel <stable-4.19>
----

. To upgrade the cluster to a specified version immediately within the next hour, enter the following command:
+
[source,terminal]
----
$ rosa upgrade cluster --cluster=<cluster_name_or_id> --version <version-id>
----
[source,terminal]
[source,terminal]
----
$ rosa upgrade cluster --cluster=<cluster_name_or_id> --control-plane
----
+
[NOTE]
====
If you are upgrading an AWS Security Token Service (STS) cluster, this command starts an interactive IAM Roles/policies upgrade mode process that verifies the account and operator role policies for the chosen cluster are compatible with the target version of the upgrade. If the policies are not compatible with the chosen upgrade version, the CLI automatically upgrades them in auto mode.
====
+
The cluster is scheduled for an immediate upgrade as denoted by the _Scheduled Time_. The upgrade will begin within one hour from the scheduled time.
+
. Alternatively, to upgrade the cluster at a future time in UTC, enter the following command:
+
[source,terminal]
----
$ rosa upgrade cluster --cluster=<cluster_name|cluster_id>   \
          --version <version-id>   \
          --schedule-date yyyy-mm-dd \
          --schedule-time HH:mm
----
+
. To customize the grace period for every node to be drained during the cluster upgrade, enter the following command:
+
[source,terminal]
----
$ rosa upgrade cluster --cluster=<cluster_name_or_id>   \
          --version <version-id>   \
          --node-drain-grace-period 15 minutes
----
+

.Verification

. You can view the status of the upgrade by entering the following command, which shows both the status (scheduled or started) and the scheduled time.
+
[source,terminal]
----
$ rosa list upgrade --cluster=<cluster_name_or_id>
----
+
.Example output
[source,terminal]
----
VERSION  NOTES
4.19.14  recommended - scheduled for 2026-04-02 15:00 UTC
4.19.13
----

You will receive email notifications confirming the scheduling, beginning, and completion of the cluster upgrade.

.Troubleshooting
* Sometimes a scheduled upgrade does not trigger. See Upgrade maintenance cancelled for more information.

// Module included in the following assemblies:
//
// * upgrading/rosa-upgrading-sts.adoc

[id="rosa-deleting-cluster-upgrade-cli_{context}"]
= Deleting a OpenShift Container Platform cluster upgrade with the ROSA CLI

[role="_abstract"]
You can use either the {rosa-cli-first} or {cluster-manager} console to delete a scheduled upgrade. This procedure uses the {rosa-cli}.

.Procedure

. Verify the cluster update has not started using the following command:
+
[source,terminal]
----
$ rosa list upgrades --cluster=<cluster_name_or_id>
----
+
.Example output
[source,terminal]
----
VERSION  NOTES
4.19.14  recommended - scheduled for 2026-06-02 15:00 UTC
4.19.13
----

. Delete a scheduled update by running the following command:
+
[source,terminal]
----
$ rosa delete upgrade --cluster=<cluster_name_or_id>
----
+
. Confirm the deletion by entering `Yes` at the confirmation prompt.
+
.Example output
[source,terminal]
----
I: Successfully canceled scheduled upgrade on cluster 'my-cluster'
----

You will receive an email notification confirming that the scheduled upgrade has been canceled.

// Module included in the following assemblies:
//
// * upgrading/rosa-upgrading-sts.adoc

//  adding this ifeval hcp-in-rosa when a hcp procedure appears in the rosa distro as well as the  hcp distro

[id="rosa-upgrade-ocm_{context}"]
= Upgrading with the {cluster-manager} console

[role="_abstract"]
You can schedule upgrades for a OpenShift Container Platform cluster manually either one time or on a recurring schedule by using {cluster-manager} console.

.Procedure

. Log in to {cluster-manager-url}.
. Select a cluster to upgrade.
. Click the *Settings* tab.
. For production clusters, ensure that the *Channel* is set to the correct channel for the version that you want to update to, such as `stable-4.19`.
. In the *Update strategy* pane, select which type of update you want:
** For individual updates, you can request the upgrade either immediately (to start within an hour) or at a future time.
** For recurring updates, select a recurring date and time to start the upgrade automatically to the latest x.y.Z (z-stream) version available.
+
[IMPORTANT]
====
Recurring updates are applicable only for z-stream updates. Minor version or y-stream updates need to be done manually. You will be notified when a new y-stream update is available.
====
. Optional: In the *Node draining* pane, select a grace period interval from the list. The grace period enables the nodes to gracefully drain before forcing the pod eviction. The default is *1 hour*.
+
[IMPORTANT]
====
You cannot change the node drain grace period after you start the upgrade process.
====
. In the *Update strategy* pane, click *Save* to apply your update strategy.
. In the *Update status* pane, review the *Update available* information and click *Update*.
+
[NOTE]
====
The *Update* button is enabled only when an upgrade is available.
====
+
. The *Update cluster* dialog opens. Recommended cluster upgrades appear in the *Select version* pane. Select the version you want to upgrade your cluster to, and click *Next*.
. Optional: For OpenShift Container Platform clusters that use AWS Security Token Service (STS), the account-level and cluster-specific Operator roles might need to be updated, depending on the selected target version.
.. In the {rosa-cli}, run the `rosa list account-roles` command to list and verify that the account roles are compatible with the target minor version chosen for the upgrade. If the roles are not compatible, run the `rosa upgrade account-roles` command to upgrade the account roles to the latest OpenShift version.
.. In the {rosa-cli}, run the `rosa list operator-roles` command to list and verify that Operator roles associated with the cluster are compatible with the target minor version chosen for the upgrade. If not, run the `rosa upgrade operators-roles` command to upgrade the cluster's Operator roles to the latest OpenShift version.
.. If you select an update version that requires approval, provide an administrator's acknowledgment by typing *Acknowledge* into the field provided, and click *Next*.
. In the *Schedule update* dialog, schedule your cluster upgrade.
+
* To upgrade within an hour, select *Update now* and click *Next*.
* To upgrade at a later time, select *Schedule a different time* and set a time and date for your upgrade. Click *Next* to proceed to the confirmation dialog.
+
. After reviewing the version and schedule summary, select *Confirm update*.
. Click *Close* to exit out of the *Update cluster* dialog.
+
The cluster is scheduled for an upgrade to the target version. This action can take up to an hour, depending on the selected upgrade schedule and your workload configuration, such as pod disruption budgets.
+
The status is displayed in the *Update status* pane.

. After the update completes and the Cluster Version Operator refreshes the available updates, check if more updates are available in your current channel.
+
--
** If updates are available, continue to perform updates in the current channel until you can no longer update.
** If no updates are available, change the *Channel* to the `stable-\*`, `fast-\*`, or `eus-*` channel for the next minor version, and update to the version that you want in that channel.
+
You might need to perform several intermediate updates until you reach the version that you want.
--

.Troubleshooting
* Sometimes a scheduled upgrade does not trigger. See Upgrade maintenance cancelled for more information.

// Module included in the following assemblies:
//
// * upgrading/rosa-upgrading-sts.adoc

[id="rosa-deleting-cluster-upgrade-ocm_{context}"]
= Deleting an upgrade with the {cluster-manager} console

[role="_abstract"]
You can use the {cluster-manager} console to delete a scheduled upgrade.

.Procedure

. Log in to {cluster-manager-url}.
. Select the cluster with the scheduled upgrade.
. Click the *Settings* tab.
. In the *Update status* pane, click *Cancel this update*.
. Review the update details in the *Cancel update* dialog and click *Cancel this update*.

You will receive an email notification confirming that the scheduled upgrade has been canceled.

[role="_additional-resources"]
.Additional resources

* Understanding update channels and releases
* Red Hat OpenShift Service on AWS update life cycle
