---
title: "{oadp-short} recommended network settings"
type: reference
domain: openshift
slug: backup-and-restore-4-22-oadp-recommended-network-settings
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-recommended-network-settings
version: 4.22
family: backup_and_restore
documentKind: "Documentation"
---

# {oadp-short} recommended network settings

[id="oadp-recommended-network-settings"]
= {oadp-short} recommended network settings

[role="_abstract"]
Keep a stable network across your {OCP-short} nodes, {aws-short} Simple Storage Service (S3) storage, and cloud environments. Meeting these recommended network settings helps you ensure successful {oadp-first} backup and restore operations, even when using remote {aws-short} S3 buckets.

// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/oadp-performance/oadp-recommended-network-settings.adoc

[id="oadp-performance-network-requirements_{context}"]
= {oadp-short} network requirements

[role="_abstract"]
For a supported experience with {oadp-first}, you should have a stable and resilient network across {OCP-short} nodes, {aws-short} Simple Storage Service (S3)-compatible object storage, and in supported cloud environments that meet {OCP-short} network requirements.

For deployments that use remote S3 buckets located off-cluster with suboptimal data paths, such as high-latency or geographically distant locations, successful backup and restore operations require specific configurations. Ensure your network settings meet the following minimum requirements:

* Bandwidth (network upload speed to object storage): Greater than 2 Mbps for small backups and 10-100 Mbps depending on the data volume for larger backups.
* Packet loss: 1%
* Packet corruption: 1%
* Latency: 100 ms

Ensure that your OpenShift Container Platform network performs optimally and meets OpenShift Container Platform network requirements.

[IMPORTANT]
====
Although Red Hat provides support for standard backup and restore failures, it does not provide support for failures caused by network settings that do not meet the recommended thresholds.
====

[role="_additional-resources"]
== Additional resources

* Configuring network settings

* About installing {oadp-short}
* Troubleshooting

* About installing {oadp-short}
* Troubleshooting
