---
title: "Troubleshooting {product-title} cluster installations"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-installations-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-installations-hcp
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting {product-title} cluster installations

[id="rosa-troubleshooting-installations-hcp"]
= Troubleshooting OpenShift Container Platform cluster installations

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

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations-hcp .adoc
[id="rosa-verify-hcp-install_{context}"]
= Verifying installation of OpenShift Container Platform clusters

[role="_abstract"]
If the OpenShift Container Platform cluster is in the installing state for over 30 minutes and has not become ready, ensure the AWS account environment is prepared for the required cluster configurations. If the AWS account environment is prepared for the required cluster configurations correctly, try to delete and re-create the cluster. If the problem persists, contact support.

.Procedure

* Verify the AWS account environment is prepared for the required cluster configurations.
* If the AWS account environment is prepared correctly, try to delete and re-create the cluster.
* If the problem persists, contact support.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations-hcp.adoc

[id="rosa-troubleshoot-hcp-install_{context}"]
= Troubleshooting OpenShift Container Platform installation error codes

[role="_abstract"]
The following table lists OpenShift Container Platform installation error codes and what you can do to troubleshoot these errors.

.OpenShift Container Platform installation error codes
[options="header",cols="3"]
|===
| Error code | Description | Resolution

| OCM3999
| Unknown error.
| Check the cluster installation logs for more details, or delete this cluster and retry cluster installation. If this issue persists, contact Red{nbsp}Hat support. See _Additional resources_ for more information.

| OCM5001
| OpenShift Container Platform cluster provision has failed.
| Check the cluster installation logs for more details, or delete this cluster and retry cluster installation. If this issue persists, contact Red{nbsp}Hat support. See _Additional resources_ for more information.

| OCM5002
| The maximum resource tag size of 25 has been exceeded.
| Check the cluster information to determine if you can remove any unnecessary tags you have specified and retry cluster installation.

| OCM5003
| Unable to establish an AWS client to provision the cluster.
| You must create several role resources on your AWS account to create and manage a OpenShift Container Platform cluster. Ensure that your provided AWS credentials are correct and retry cluster installation.

For more information about OpenShift Container Platform IAM role resources, see _ROSA IAM role resources_ in the _Additional resources_ section.

| OCM5004
| Unable to establish a cross-account AWS client to provision the cluster.
| You must create several role resources on your AWS account to create and manage a OpenShift Container Platform cluster. Ensure that your provided AWS credentials are correct and retry cluster installation.

For more information about OpenShift Container Platform IAM role resources, see _ROSA IAM role resources_ in the _Additional resources_ section.

| OCM5005
| Failed to retrieve AWS subnets defined for the cluster.
| Review the provided subnet IDs and retry cluster installation.

| OCM5006
| You must configure at least one private AWS subnet for the cluster.
| Review the provided subnet IDs and retry cluster installation.

| OCM5007
| Unable to create AWS STS prerequisites for the cluster.
| Verify that account and operator roles have been created and are correct. For more information, see _AWS STS and ROSA with HCP explained_ in the _Additional resources_ section.

| OCM5008
| The provided cluster flavour is incorrect.
| Verify that the provided name or ID is correct when you are using the flavour parameter and retry cluster creation.

| OCM5009
| The cluster version could not be found.
| Ensure that the configured version ID matches a valid OpenShift Container Platform version.

| OCM5010
| Failed to tag subnets for the cluster.
| Confirm that the AWS permissions and the subnet configurations are correct. You must tag at least one private subnet and, if applicable, one public subnet.

| OCM5011
| Cluster installation has failed due to unavailable capacity in the selected region.
| Try your cluster installation in another region or retry cluster installation.

|===

[role="_additional-resources"]
.Additional resources
* Red Hat Customer Support

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations-hcp .adoc
[id="rosa-hcp-no-console-access_{context}"]
= Troubleshooting access to {hybrid-console}

[role="_abstract"]
In OpenShift Container Platform clusters, the OpenShift Container Platform OAuth server is hosted in the Red Hat service's AWS account while the web console service is published by using the cluster's default ingress controller in the cluster's AWS account. If you can log in to your cluster by using the OpenShift CLI (oc) but cannot access the OpenShift Container Platform web console, verify the following criteria are met:

.Procedure

* Verify the console workloads are running.
* Verify the default ingress controller's load balancer is active.
* Verify you are accessing the console from a machine that has network connectivity to the cluster's VPC network.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations-hcp .adoc
[id="rosa-hcp-ready-no-console-access_{context}"]
= Verifying access to OpenShift Container Platform web console for OpenShift Container Platform cluster in ready state

[role="_abstract"]
OpenShift Container Platform clusters return a `ready` status when the control plane hosted in the OpenShift Container Platform service account becomes ready. Cluster console workloads are deployed on the cluster's worker nodes. The OpenShift Container Platform web console will not be available and accessible until the worker nodes have joined the cluster and console workloads are running.

.Procedure

* If your OpenShift Container Platform cluster is ready but you are unable to access the OpenShift Container Platform web console for the cluster, wait for the worker nodes to join the cluster and retry accessing the console.
+
You can either log in to the OpenShift Container Platform cluster or use the `rosa describe machinepool` command in the `rosa` CLI watch the nodes.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-installations-hcp .adoc
[id="rosa-hcp-private-ready-no-console-access_{context}"]
= Verifying access to {hybrid-console} for private OpenShift Container Platform clusters

[role="_abstract"]
The console of the private cluster is private by default. During cluster installation, the default Ingress Controller managed by OpenShift's Ingress Operator is configured with an internal AWS Network Load Balancer (NLB).

.Procedure

* If your private OpenShift Container Platform cluster shows a `ready` status but you cannot access the OpenShift Container Platform web console for the cluster, try accessing the cluster console from either within the cluster VPC or from a network that is connected to the VPC.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Installation troubleshooting
* Verifying installation of OpenShift Container Platform clusters
* Troubleshooting OpenShift Container Platform installation error codes
* Troubleshooting access to {hybrid-console}
* Verifying access to OpenShift Container Platform web console for OpenShift Container Platform cluster in ready state
* Verifying access to {hybrid-console} for private OpenShift Container Platform clusters
* AWS prerequisites for OpenShift Container Platform
// * For information about the required IAM, see ROSA IAM role resources.
* AWS STS and OpenShift Container Platform explained
* OpenShift Container Platform OAuth server
//Commented out until Networking book has been fully migrated.
//* For more information about the OpenShift Container Platform ingress operator, Configuring the Ingress Controller.
* Web Console Overview
* `rosa describe machinepool`
* AWS Virtual Private Cloud (VPC) Documentation
