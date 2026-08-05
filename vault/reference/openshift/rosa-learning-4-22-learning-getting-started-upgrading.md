---
title: "Upgrading your cluster"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-getting-started-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-getting-started-upgrading
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Upgrading your cluster

[id="learning-getting-started-upgrading"]
= Upgrading your cluster

[role="_abstract"]
You can schedule cluster upgrades for OpenShift Container Platform as part of the managed service. Relying on this managed service completely automates the update process without requiring you to run manual commands or make configuration changes.

Ways to schedule a cluster upgrade include:

* *Manually using the command line interface (CLI)*: Start a one-time immediate upgrade or schedule a one-time upgrade for a future date and time.
* *Manually using the Red{nbsp}Hat OpenShift Cluster Manager user interface (UI)*: Start a one-time immediate upgrade or schedule a one-time upgrade for a future date and time.
* *Automated upgrades*: Set an upgrade window for recurring y-stream upgrades whenever a new version is available without needing to manually schedule it. Minor versions have to be manually scheduled.

For more details about cluster upgrades, run the following command:

[source,terminal]
----
$ rosa upgrade cluster --help
----

// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-upgrading-cli_{context}"]
= Manually upgrading your cluster using the CLI

[role="_abstract"]
You can upgrade your cluster by using {rosa-cli}.

.Procedure

. Check if there is an upgrade available by running the following command:
+
[source,terminal]
----
$ rosa list upgrade -c <cluster-name>
----
+
*For example*:
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
$ rosa upgrade cluster -c --control-plane <cluster-name> --version <desired-version>
----

. *Optional:* Schedule the cluster to upgrade at a later date and time by running the following command:
+
[source,terminal]
----
$ rosa upgrade cluster -c <cluster-name> --version <desired-version> --schedule-date <future-date-for-update> --schedule-time <future-time-for-update>
----
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-upgrading-web-ui_{context}"]
= Manually upgrading your cluster using the UI

[role="_abstract"]
You can upgrade your cluster using {cluster-manager-url}.

.Procedure
. Log in to the {cluster-manager}, and select the cluster you want to upgrade.
. Click the *Settings* tab.
. If an upgrade is available, click *Update*.
+
image::cloud-experts-getting-started-cluster-upgrade.png[]

. Select the version to which you want to upgrade in the new window.
. Schedule a time for the upgrade or begin it immediately.
// Module included in the following assemblies:
//
// * rosa_learning/creating_cluster_workshop/learning-getting-started-support.adoc
[id="learning-getting-started-upgrading-recurring-updates_{context}"]
= Setting up automatic recurring upgrades

[role="_abstract"]
To schedule your cluster to automatically receive new patch (z-stream) updates, you can set your cluster to upgrade on a recurring basis within {cluster-manager-url}.

.Procedure
. Log in to the {cluster-manager}, and select the cluster you want to upgrade.
. Click the *Settings* tab.
. Under *Update Strategy*, click *Recurring updates*.
. Set the day and time for the upgrade to occur.
. Click *Save*.
