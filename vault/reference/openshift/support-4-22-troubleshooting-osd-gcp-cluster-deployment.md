---
title: "Troubleshooting an {product-title} on Google Cloud cluster deployment"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-osd-gcp-cluster-deployment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-osd-gcp-cluster-deployment
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting an {product-title} on Google Cloud cluster deployment

[id="troubleshooting-osd-gcp-cluster-deployment"]
= Troubleshooting an OpenShift Container Platform on Google Cloud cluster deployment

[role="_abstract"]
OpenShift Container Platform on {gcp-first} cluster deployment errors can occur for several reasons, including insufficient quota limits and settings, incorrectly inputted data, incompatible configurations, and so on.

Learn how to resolve common OpenShift Container Platform on {gcp-short} cluster installation errors in the following sections.

// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-osd-gcp-cluster-deployment.adoc

[id="osd-on-gcp-troubleshoot-cluster-install_{context}"]
= Troubleshooting OpenShift Container Platform on {gcp-short} installation error codes

[role="_abstract"]
The following table lists OpenShift Container Platform on {gcp-first} installation error codes and what you can do to resolve these errors.

.OpenShift Container Platform on {gcp-short} installation error codes
[options="header",cols="3"]
|===
| Error code | Description | Resolution

| OCM3022
| Invalid {gcp-short} project ID.
| Verify the project ID in the Google cloud console and retry cluster creation.

| OCM3023
| {gcp-short} instance type not found.
| Verify the instance type and retry cluster creation.

For more information about OpenShift Container Platform on {gcp-short} instance types, see _{gcp-full} instance types_ in the _Additional resources_ section.

| OCM3024
| {gcp-short} precondition failed.
| Verify the organization policy constraints and retry cluster creation.

For more information about organization policy constraints, see Organization policy constraints.

| OCM3025
| {gcp-short} SSD quota limit exceeded.
| Check your available persistent disk SSD quota either in the {gcp-full} console or in the `gcloud` CLI. There must be at least 896 GB of SSD available. Increase the SSD quota limit and retry cluster creation.

For more information about managing persistent disk SSD quota, see Allocation quotas.

| OCM3026
| {gcp-short} compute quota limit exceeded.
| Increase your CPU compute quota and retry cluster installation.

For more information about the CPU compute quota, see Compute Engine quota and limits overview.

| OCM3027
| {gcp-short} service account quota limit exceeded.
| Ensure your quota allows for additional unused service accounts. Check your current usage for quotas in your {gcp-short} account and try again.

For more information about managing your quotas, see Manage your quotas using the console.

|===

[role="_additional-resources"]
== Additional resources

* {gcp-full} instance types
