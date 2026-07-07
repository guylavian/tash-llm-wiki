---
title: "Managing billing accounts for {product-title} clusters"
type: reference
domain: openshift
slug: cli-reference-4-22-rosa-updating-billing-account-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/rosa-updating-billing-account-cli
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Managing billing accounts for {product-title} clusters

[id="rosa-updating-account-cli"]
= Managing billing accounts for OpenShift Container Platform clusters

[role="_abstract"]
You can use the {rosa-cli-first} to point an existing cluster at a different AWS billing account after deployment. This process lets you correct a billing account linked at install time or change the account at a later date.

[NOTE]
====
You also have the option to update your billing account through the {cluster-manager}.
====

// Module included in the following assemblies:
//
// * rosa_cli/rosa-updating-billing-account-cli.adoc
[id="rosa-update-billing_{context}"]
= Update billing accounts for OpenShift Container Platform clusters

[role="_abstract"]
Change which AWS billing account a deployed cluster uses by running `rosa edit cluster` in interactive mode.

.Prerequisites

* You must have more than one AWS billing account.
* The AWS billing account you want your cluster to link to must already be linked to the Red{nbsp}Hat organization where the cluster is deployed.

.Procedure
. Run the following command in your terminal window. Replace `<cluster_ID>` with the ID of the cluster whose billing account you want to update.
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_ID>
----
+
[NOTE]
====
To locate the IDs of your active clusters, run the `$ rosa list clusters` command in your terminal window.
====
+
. Skip to the `Billing Account` parameter within the interactive mode.
. Select the desired AWS billing account from the list of available options and press "Enter".
+
The AWS billing account for your cluster is now updated.

[role="_additional-resources"]
.Additional resources

* Updating billing accounts for OpenShift Container Platform clusters
