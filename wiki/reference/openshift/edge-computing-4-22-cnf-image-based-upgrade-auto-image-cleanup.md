---
title: "Configuring the automatic image cleanup of the container storage disk"
type: reference
domain: openshift
slug: edge-computing-4-22-cnf-image-based-upgrade-auto-image-cleanup
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/cnf-image-based-upgrade-auto-image-cleanup
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# Configuring the automatic image cleanup of the container storage disk

[id="cnf-image-based-upgrade-configure-auto-image-cleanup"]
= Configuring the automatic image cleanup of the container storage disk

Configure when the {lcao} cleans up unpinned images in the `Prep` stage by setting a minimum threshold for available storage space through annotations.
The default container storage disk usage threshold is 50%.

The {lcao} does not delete images that are pinned in CRI-O or are currently used.
The Operator selects the images for deletion by starting with dangling images and then sorting the images from oldest to newest that is determined by the image `Created` timestamp.

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-image-based-upgrade-shared-container-partition

[id="ztp-image-based-upgrade-configure-threshold_{context}"]
= Configuring the automatic image cleanup of the container storage disk

Configure the minimum threshold for available storage space through annotations.

.Prerequisites

* You have created an `ImageBasedUpgrade` CR.

.Procedure

. Increase the threshold to 65% by running the following command:
+
[source,terminal]
----
$ oc -n openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/disk-usage-threshold-percent='65'
----

. (Optional) Remove the threshold override by running the following command:
+
[source,terminal]
----
$ oc -n  openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/disk-usage-threshold-percent-
----

// Module included in the following assemblies:
// * edge_computing/image-based-upgrade/cnf-image-based-upgrade-shared-container-partition

[id="ztp-image-based-upgrade-disable-container-storage-image-cleanup_{context}"]
= Disable the automatic image cleanup of the container storage disk

Disable the automatic image cleanup threshold.

.Procedure

. Disable the automatic image cleanup by running the following command:
+
[source,terminal]
----
$ oc -n openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/on-prep='Disabled'
----

. (Optional) Enable automatic image cleanup again by running the following command:
+
[source,terminal]
----
$ oc -n  openshift-lifecycle-agent annotate ibu upgrade image-cleanup.lca.openshift.io/on-prep-
----
