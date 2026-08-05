---
title: "Troubleshooting cluster comparisons"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-troubleshooting-cluster-comparisons
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/troubleshooting-cluster-comparisons
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Troubleshooting cluster comparisons

[id="troubleshooting-cluster-comparisons"]
= Troubleshooting cluster comparisons

[role="_abstract"]
When using the `cluster-compare` plugin, you might see unexpected results, such as false positives or conflicts when multiple cluster custom resources (CRs) exist.

// Module included in the following assembly:
//
// * scalability_and_performance/cluster-compare/troubleshooting-cluster-comparisons.adoc

[id="troubleshooting-cc-false-positives_{context}"]
= Troubleshooting false positives for missing resources

[role="_abstract"]
The plugin might report a missing resource even though the cluster custom resource (CR) is present in the cluster.

.Procedure

. Ensure you are using the latest version of the `cluster-compare` plugin. For more information, see "Installing the cluster-compare plugin".

. Ensure you are using the most up-to-date version of the reference configuration.

. Ensure that template has the same `apiVersion`, `kind`, `name`, and `namespace` fields as the cluster CR.

// Module included in the following assembly:
//
// * scalability_and_performance/cluster-compare/troubleshooting-cluster-comparisons.adoc

[id="troubleshooting-cc-multiple-matches_{context}"]
= Troubleshooting multiple template matches for the same CR

[role="_abstract"]
In some cases, more than one cluster CR can match a template because they feature the same `apiVersion`, `namespace`, and `kind`. The plugin's default matching compares the CR that features the least differences.

You can optionally configure your reference configuration to avoid this situation.

.Procedure

. Ensure the templates feature distinct `apiVersion`, `namespace`, and `kind` values to ensure no duplicate template matching.

. Use a user configuration file to manually match a template to a CR. For more information, see "Configuring manual matching between CRs and templates".

[role="_additional-resources"]
== Additional resources

* Installing the cluster-compare plugin

* Configuring manual matching between CRs and templates
