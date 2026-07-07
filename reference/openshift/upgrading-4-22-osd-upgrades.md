---
title: "{product-title} cluster upgrades"
type: reference
domain: openshift
slug: upgrading-4-22-osd-upgrades
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/upgrading/osd-upgrades
version: 4.22
family: upgrading
documentKind: "Documentation"
---

# {product-title} cluster upgrades

[id="osd-upgrades"]
= OpenShift Container Platform cluster upgrades

[role="_abstract"]
You can schedule automatic or manual upgrade policies to update the version of your OpenShift Container Platform clusters. Upgrading OpenShift Container Platform clusters can be done through {cluster-manager-first} or {cluster-manager} CLI.

Red Hat Site Reliability Engineers (SREs) monitor upgrade progress and remedy any issues encountered.

// Module included in the following assemblies:
//
// * upgrading/osd-upgrades.adoc

[id="osd-lifecycle-policy_{context}"]
= Life cycle policies and planning

[role="_abstract"]
To plan an upgrade, review the _OpenShift Container Platform update life cycle_ guide in the _Additional resources_ section. The life cycle page includes release definitions, support and upgrade requirements, installation policy information, and life cycle dates.

You can use update channels to decide which OpenShift Container Platform minor version to update your clusters to. OpenShift Container Platform supports updates through the `stable-4.y`, `fast-4.y`, and `eus-4.y` channels. For more information, see the _Channels in OpenShift Container Platform clusters_ section.

// Module included in the following assemblies:
//
// * assemblies/upgrades.adoc

[id="upgrade_{context}"]
= Understanding OpenShift Container Platform cluster upgrades

[role="_abstract"]
When upgrades are made available for your OpenShift Container Platform cluster, you can upgrade to the newest version through {cluster-manager-first} or {cluster-manager} CLI. You can set your upgrade policies on existing clusters or during cluster creation, and upgrades can be scheduled to occur automatically or manually.

[IMPORTANT]
====
Before upgrading a Workload Identity Federation (WIF)-enabled OpenShift Container Platform on {GCP} cluster, you must update the wif-config. For more information, see "Cluster upgrades with Workload Identity Federation (WIF)".
====

Red Hat Site Reliability Engineers (SRE) will provide a curated list of available versions for your OpenShift Container Platform clusters. For each cluster you will be able to review the full list of available releases, as well as the corresponding release notes. {cluster-manager} will enable installation of clusters at the latest supported versions, and upgrades can be canceled at any time.

You can also set a grace period for how long `PodDisruptionBudget` protected workloads are respected during upgrades. After this grace period, any workloads protected by  `PodDisruptionBudget` that have not been successfully drained from a node, will be forcibly deleted.

[NOTE]
====
All Kubernetes objects and Persistent Volumes (PVs) in each OpenShift Container Platform cluster are backed up as part of the OpenShift Container Platform service. Application and application data backups are not a part of the OpenShift Container Platform service. Ensure you have a backup policy in place for your applications and application data before scheduling upgrades.
====

[NOTE]
====
When following a scheduled upgrade policy, there might be a delay of an hour or more before the upgrade process begins, even if it is an immediate upgrade. Additionally, the duration of the upgrade might vary based on your workload configuration.
====

[id="upgrade-automatic_{context}"]
== Recurring upgrades

Upgrades can be scheduled to occur automatically on a day and time specified by the cluster owner or administrator. Upgrades occur on a weekly basis, unless an upgrade is unavailable for that week.

If you select recurring updates for your cluster, you must provide an administrator's acknowledgment. {cluster-manager} does not start scheduled y-stream updates for minor versions without receiving an administrator's acknowledgment.

[NOTE]
====
Recurring upgrade policies are optional and if they are not set, the upgrade policies default to individual.
====

[id="upgrade-manual_upgrades_{context}"]
== Individual upgrades

If you opt for individual upgrades, you are responsible for updating your cluster. If you select an update version that requires approval, you must provide an administrator's acknowledgment.

If your cluster version becomes outdated, it changes to a limited support status.

[id="upgrade-notifications_{context}"]
== Upgrade notifications

From {cluster-manager} console you can view your cluster's history from the *Overview* tab. The Upgrade states can be viewed in the service log under the *Cluster history* heading.

Every change of state also triggers an email notification to the cluster owner and subscribed users. You will receive email notifications for the following events:

* An upgrade has been scheduled.
* An upgrade has started.
* An upgrade has completed.
* An upgrade has been canceled.

[NOTE]
====
For recurring upgrades, you will also receive email notifications before the upgrade occurs based on the following cadence:

* 2 week notice
* 1 week notice
* 1 day notice
====

[id="wif-upgrades_{context}"]
== Cluster upgrades with Workload Identity Federation (WIF)
Before upgrading an OpenShift Container Platform on {GCP} cluster with WIF authentication type to a newer y-stream version, you must update the WIF configuration to that version. Failure to do so before attempting to upgrade the cluster version will result in an error.
For more information on how to update a WIF configuration, see the  _Additional resources_ section.

[NOTE]
====
The update path to a brand new release of OpenShift Container Platform is not available in the stable channel until 45 to 90 days after the initial GA of a newer y-stream version.
====

[id="osd-upgrading-channels_{context}"]
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

When you have set the channel and an update is initiated, the Cluster Version Operator (CVO) retrieves the target release image and begins applying the changes to the cluster.

[NOTE]
====
The *Channel groups* option is now deprecated in OpenShift Container Platform. Channel groups allowed you to upgrade through the available patch/z-stream updates for a particular channel group, such as stabe or eus.
There was the possibility of inadvertently upgrading to the next minor version/Y+1 version if it appeared in the available updates.
====

// Module included in the following assemblies:
//
// * upgrading/osd-upgrades.adoc

[id="osd-upgrading-switch-channels_{context}"]
= Switch channels to view available update options

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
// * assemblies/upgrades.adoc

[id="upgrade-auto_{context}"]

= Scheduling recurring upgrades for your cluster

[role="_abstract"]
You can use {cluster-manager} to schedule recurring, automatic upgrades for z-stream patch versions for your OpenShift Container Platform cluster. Based on upstream changes, there might be times when no updates are released. Therefore, no upgrade occurs for that week.

.Procedure

. From {cluster-manager-url}, select your cluster from the clusters list.

. Click the *Upgrade settings* tab to access the upgrade operator.

. To schedule recurring upgrades, select *Recurring updates*.

. Provide an administrator's acknowledgment and click *Approve and continue*. {cluster-manager} does not start scheduled y-stream updates for minor versions without receiving an administrator's acknowledgment.
+
[IMPORTANT]
====
Before upgrading a Workload Identity Federation (WIF)-enabled OpenShift Container Platform on {GCP} cluster, you must update the wif-config. For more information, see "Cluster upgrades with Workload Identity Federation (WIF)".
====
+
. Specify the day of the week and the time you want your cluster to upgrade.

. Click *Save*.

. Optional: Set a grace period for *Node draining* by selecting a designated amount of time from the drop down list. A *1 hour* grace period is set by default.

. To edit an existing recurring upgrade policy, edit the preferred day or start time from the *Upgrade Settings* tab. Click *Save*.

. To cancel a recurring upgrade policy, switch the upgrade method to individual from the *Upgrade Settings* tab. Click *Save*.

.Verification
* On the *Upgrade settings* tab, the *Upgrade status* box indicates that an upgrade is scheduled. The date and time of the next scheduled update is listed.

// Module included in the following assemblies:
//
// * assemblies/upgrades.adoc

[id="upgrade-manual_{context}"]

= Scheduling individual upgrades for your cluster

[role="_abstract"]
You can use {cluster-manager} to manually upgrade your OpenShift Container Platform cluster one time.

.Procedure

. From {cluster-manager-url}, select your cluster from the clusters list.

. Click the *Upgrade settings* tab to access the upgrade operator. You can also update your cluster from the *Overview* tab by clicking *Update* next to the cluster version under the *Details* heading.

. To schedule an individual upgrade, select *Individual updates*.

. Click *Update* in the *Update Status* box.

. Select the version you want to upgrade your cluster to. Recommended cluster upgrades appear in the UI. To learn more about each available upgrade version, click *View release notes*.

. If you select an update version that requires approval, provide an administrator's acknowledgment and click *Approve and continue*.
+
[IMPORTANT]
====
Before upgrading a Workload Identity Federation (WIF)-enabled OpenShift Container Platform on {GCP} cluster, you must update the wif-config. For more information, see "Cluster upgrades with Workload Identity Federation (WIF)".
====
+
. Click *Next*.

. To schedule your upgrade:
- Click *Upgrade now* to upgrade within the next hour.
- Click *Schedule a different time* and specify the date and time that you want the cluster to upgrade.

. Click *Next*.

. Review the upgrade policy and click *Confirm upgrade*.

. A confirmation appears when the cluster upgrade has been scheduled. Click *Close*.

. Optional: Set a grace period for *Node draining* by selecting a designated amount of time from the drop down list. A *1 hour* grace period is set by default.

.Verification

* From the *Overview* tab, next to the cluster version, the UI notates that the upgrade has been scheduled.
** Click *View details* to view the upgrade details. If you need to cancel the scheduled upgrade, you can click *Cancel this upgrade* from the *View Details* pop-up.
** The same upgrade details are available on the *Upgrade settings* tab under the *Upgrade status* box. If you need to cancel the scheduled upgrade, you can click *Cancel this upgrade* from the *Upgrade status* box.

[WARNING]
====
If a Common Vulnerabilities and Exposures (CVE) or other critical issue to OpenShift Container Platform is found, all clusters are upgraded within 48 hours of the fix being released. You are notified when the fix is available and informed that the cluster will be automatically upgraded at your latest preferred start time before the 48 hour window closes. You can also upgrade manually at any time before the recurring upgrade starts.
====

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform update life cycle

 * Understanding update channels and releases

* Accessing cluster notifications in {hybrid-console}

* Updating a WIF configuration
