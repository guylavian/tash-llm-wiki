---
title: "Troubleshooting {product-title} installations"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-installations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-installations
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting {product-title} installations

[id="rosa-troubleshooting-installations"]
= Troubleshooting OpenShift Container Platform installations

[role="_abstract"]
Troubleshoot the installation of OpenShift Container Platform clusters by completing the following instructions.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations.adoc

[id="rosa-troubleshooting-installing_{context}"]
= Installation troubleshooting

[role="_abstract"]
This procedure describes how to troubleshoot installation issues for OpenShift Container Platform clusters.

.Procedure

* Inspect install or uninstall logs:
** To display install logs, run the following command, replacing `<cluster_name>` with the name of your cluster:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name>
----
+
** To watch the logs, include the `--watch` flag:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----
+
** To display uninstall logs, run the following command, replacing `<cluster_name>` with the name of your cluster:
+
[source,terminal]
----
$ rosa logs uninstall --cluster=<cluster_name>
----
+
** To watch the logs, include the `--watch` flag:
+
[source,terminal]
----
$ rosa logs uninstall --cluster=<cluster_name> --watch
----

* Verify your AWS account permissions for clusters without STS:
+
Run the following command to verify if your AWS account has the correct permissions. This command verifies permissions only for clusters that do not use the AWS Security Token Service (STS):
+
[source,terminal]
----
$ rosa verify permissions
----
+
If you receive any errors, double check to ensure than an SCP is not applied to your AWS account. If you are required to use an SCP, see Red{nbsp}Hat Requirements for Customer Cloud Subscriptions for details on the minimum required SCP.

* Verify your AWS account and quota:
+
Run the following command to verify you have the available quota on your AWS account:
+
[source,terminal]
----
$ rosa verify quota
----
+
AWS quotas change based on region. Be sure you are verifying your quota for the correct AWS region. If you need to increase your quota, go to your AWS console, and request a quota increase for the service that failed.

* AWS notification emails:
+
When creating a cluster, the OpenShift Container Platform service creates small instances in all supported regions. This check ensures the AWS account being used can deploy to each supported region.
+
For AWS accounts that are not using all supported regions, AWS might send one or more emails confirming that "Your Request For Accessing AWS Resources Has Been Validated." Typically the sender of this email is aws-verification@amazon.com.
+
This is expected behavior as the OpenShift Container Platform service is validating your AWS account configuration.
