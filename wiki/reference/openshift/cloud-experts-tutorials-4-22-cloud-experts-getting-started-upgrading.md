---
title: "Tutorial: Upgrading your cluster"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-upgrading
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Upgrading your cluster

[id="cloud-experts-getting-started-upgrading"]
= Tutorial: Upgrading your cluster

[role="_abstract"]
OpenShift Container Platform executes all cluster upgrades as part of the managed service. You do not need to run any commands or make changes to the cluster. You can schedule the upgrades at a convenient time.

Ways to schedule a cluster upgrade include:

* *Manually using the command-line interface (CLI)*: Start a one-time immediate upgrade or schedule a one-time upgrade for a future date and time.
* *Manually using the Red{nbsp}Hat OpenShift Cluster Manager user interface (UI)*: Start a one-time immediate upgrade or schedule a one-time upgrade for a future date and time.
* *Automated upgrades*: Set an upgrade window for recurring y-stream upgrades whenever a new version is available without needing to manually schedule it. Minor versions have to be manually scheduled.

For more details about cluster upgrades, run the following command:

[source,terminal]
----
$ rosa upgrade cluster --help
----

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-upgrading.adoc

[id="cloud-experts-getting-started-upgrading-manual-cli_{context}"]
= Manually upgrading your cluster using the CLI

[role="_abstract"]
You can upgrade your cluster by using the {rosa-cli-first}.

.Procedure
. Check if there is an upgrade available by running the following command:
+
[source,terminal]
----
$ rosa list upgrade -c <cluster-name>
----
+
**Example output**
+
[source,terminal]
----
$ rosa list upgrade -c <cluster-name>
VERSION  NOTES
4.14.7   recommended
4.14.6
...
----
+
In the above example, versions 4.14.7 and 4.14.6 are both available.

. Schedule the cluster to upgrade within the hour by running the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster-name> --version <desired-version>
----

. *Optional:* Schedule the cluster to upgrade at a later date and time by running the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster-name> --version <desired-version> --schedule-date <future-date-for-update> --schedule-time <future-time-for-update>
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-upgrading.adoc

[id="cloud-experts-getting-started-upgrading-manual-ui_{context}"]
= Manually upgrading your cluster using the UI

[role="_abstract"]
You can upgrade your clusters using the {cluster-manager}.

.Procedure
. Log in to the {cluster-manager-url}, and select the cluster you want to upgrade.
. Click *Settings*.
. If an upgrade is available, click *Update*.
+
image::cloud-experts-getting-started-cluster-upgrade.png[]

. Select the version to which you want to upgrade in the new window.
. Schedule a time for the upgrade or begin it immediately.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-upgrading.adoc

[id="cloud-experts-getting-started-upgrading-recurring_{context}"]
= Setting up automatic recurring upgrades

[role="_abstract"]
You can set up automatic recurring upgrades within {cluster-manager} for your clusters.

.Procedure
. Log in to the {cluster-manager-url}, and select the cluster you want to upgrade.
. Click *Settings*.
. Under *Update Strategy*, click *Recurring updates*.
. Set the day and time for the upgrade to occur.
. Under *Node draining*, select a grace period to allow the nodes to drain before pod eviction.
. Click *Save*.
