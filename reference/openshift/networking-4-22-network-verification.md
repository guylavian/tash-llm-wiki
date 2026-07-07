---
title: "Network verification for {product-title} clusters"
type: reference
domain: openshift
slug: networking-4-22-network-verification
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/network-verification
version: 4.22
family: networking
documentKind: "Documentation"
---

# Network verification for {product-title} clusters

[id="osd-network-verification_{context}"]
= Network verification for OpenShift Container Platform clusters

[role="_abstract"]
Network verification checks run automatically when you deploy
an OpenShift Container Platform
a OpenShift Container Platform
cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster. The checks validate your network configuration and highlight errors, enabling you to resolve configuration issues before cluster deployment. You can also run the network verification checks manually to validate the configuration for an existing cluster.

// Module included in the following assemblies:
//
// * networking/network-verification.adoc

[id="osd-understanding-network-verification_{context}"]
= Understanding network verification for OpenShift Container Platform clusters

[role="_abstract"]
When you deploy
an OpenShift Container Platform
a OpenShift Container Platform
cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster, network verification runs automatically. This helps you identify and resolve configuration issues before cluster deployment.

When you prepare to install your cluster by using {cluster-manager-first}, the automatic checks run after you input a subnet into a subnet ID field on the *Virtual Private Cloud (VPC) subnet settings* page.
When you prepare to install your cluster by using {cluster-manager-first}, the automatic checks run after you input a subnet into a subnet ID field on the *Virtual Private Cloud (VPC) subnet settings* page. If you create your cluster by using the ROSA CLI (`rosa`) with the interactive mode, the checks run after you provide the required VPC network information. If you use the CLI without the interactive mode, the checks begin immediately before cluster creation.

When you add a machine pool with a subnet that is new to your cluster, the automatic network verification checks the subnet to ensure that network connectivity is available before provisioning the machine pool.

After automatic network verification completes, the system sends a record to the service log. The record provides the results of the verification check, including any network configuration errors. You can resolve the identified issues before a deployment and the deployment has a greater chance of success.

You can also run the network verification manually for an existing cluster to verify the network configuration after making configuration changes. For steps to run the network verification checks manually, see _Running the network verification manually_.

// Module included in the following assemblies:
//
// * networking/network_security/network-verification.adoc

[id="scope-of-the-network-verification-checks_{context}"]
= Scope of the network verification checks

[role="_abstract"]
The network verification includes checks for each of the following requirements:

* The parent Virtual Private Cloud (VPC) exists.
* All specified subnets belong to the VPC.
* The VPC has `enableDnsSupport` enabled.
* The VPC has `enableDnsHostnames` enabled.
* Egress is available to the required domain and port combinations.

[role="_additional-resources"]
.Additional resources
* AWS firewall prerequisites
//ifdef::openshift-rosa[]
//Commenting out the following xref because it's breaking the networking and potentially other PRs. Pre- or post-publish HCP pruning task.
//ifdef::openshift-rosa,openshift-rosa-hcp[]
//* Egress is available to the required domain and port combinations that are specified in the AWS firewall prerequisites section.
// This link needs to reamin hidden until the HCP migration is published
// * Egress is available to the required domain and port combinations that are specified in the AWS firewall prerequisites section.
//endif::openshift-rosa,openshift-rosa-hcp[]

// Module included in the following assemblies:
//
// * networking/network-verification.adoc

[id="automatic-network-verification-bypassing_{context}"]
= Automatic network verification bypassing

[role="_abstract"]
You can bypass the automatic network verification if you want to deploy
an OpenShift Container Platform
a OpenShift Container Platform
cluster with known network configuration issues into an existing Virtual Private Cloud (VPC).

If you bypass the network verification when you create a cluster, the cluster has a limited support status. After installation, you can resolve the issues and then manually run the network verification. The verification removes the limited support status after it succeeds.

When you install a cluster into an existing VPC by using {cluster-manager-first}, you can bypass the automatic verification by selecting *Bypass network verification* on the *Virtual Private Cloud (VPC) subnet settings* page.

//Commented out due to updates made in OSDOCS-7033
//ifdef::openshift-rosa[]
//.Bypassing automatic network verification by using the ROSA CLI (`rosa`)

//When you install a cluster into an existing VPC by using the `rosa create cluster` command, you can bypass the automatic verification by including the `--bypass-network-verify --force` arguments. The following example bypasses the network verification before creating a cluster:

//[source,terminal]
//----
//$ rosa create cluster --cluster-name mycluster \
//                      --subnet-ids subnet-03146b9b52b6024cb,subnet-///03146b9b52b2034cc \
//                      --bypass-network-verify --force
//----

//[NOTE]
//====
//Alternatively, you can specify the `--interactive` argument and select the option in the interactive prompts to bypass the network verification checks.
//====
//endif::openshift-rosa[]

// Module included in the following assemblies:
//
// * networking/network-verification.adoc

[id="running-network-verification-manually_{context}"]
= Running the network verification manually

[role="_abstract"]
After installing a OpenShift Container Platform cluster, you can run the network verification checks manually by using {cluster-manager-first} or the ROSA CLI (`rosa`).

// Module included in the following assemblies:
//
// * networking/network-verification.adoc

[id="running-network-verification-manually-ocm_{context}"]
= Running the network verification manually

[id="running-network-verification-manually-ocm_{context}"]
= Running the network verification manually using {cluster-manager}

[role="_abstract"]
You can manually run the network verification checks for an existing OpenShift Container Platform cluster by using {cluster-manager-first}.

.Prerequisites

* You have an existing OpenShift Container Platform cluster.
* You are the cluster owner or you have the cluster editor role.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Select *Verify networking* from the *Actions* drop-down menu.

// Module included in the following assemblies:
//
// * networking/network-verification.adoc

[id="running-network-verification-manually-cli_{context}"]
= Running the network verification manually using the CLI

[role="_abstract"]
You can manually run the network verification checks for an existing OpenShift Container Platform cluster by using the ROSA CLI (`rosa`).

To run the network verification, you can specify either a cluster name or a set of Virtual Private Cloud (VPC) subnet IDs.

.Prerequisites

* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.
* You have an existing OpenShift Container Platform cluster.
* You are the cluster owner or you have the cluster editor role.

.Procedure

* Option 1: Verify the network configuration by specifying the cluster name. The subnet IDs are automatically detected. Replace `<cluster_name>` with the name of your cluster:
+
[source,terminal]
----
$ rosa verify network --cluster <cluster_name>
----
+
.Example output
[source,terminal]
----
I: Verifying the following subnet IDs are configured correctly: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: pending
I: subnet-03146b9b52b2034cc: passed
I: Run the following command to wait for verification to all subnets to complete:
rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
** Ensure that verification to all subnets completes:
+
[source,terminal]
----
$ rosa verify network --watch \
                      --status-only \
                      --region <region_name> \
                      --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
+
*** The `watch` flag causes the command to complete after all the subnets under test are in a failed or passed state.
*** The `status-only` flag does not trigger a run of network verification but returns the current state, for example, `subnet-123 (verification still in-progress)`. By default, without this option, a call to this command always triggers a verification of the specified subnets.
*** Use the `region` flag to provide a specific AWS region that overrides the `_AWS_REGION_` environment variable.
*** Use the `subnet-ids` flag to enter a list of subnet IDs separated by commas to verify. If any of the subnets do not exist, the error message `Network verification for subnet 'subnet-<subnet_number> not found` displays and the system does not check subnets.
+
.Example output
[source,terminal]
----
I: Checking the status of the following subnet IDs: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: passed
I: subnet-03146b9b52b2034cc: passed
----
+
[TIP]
====
To output the full list of verification tests, you can include the `--debug` argument when you run the `rosa verify network` command.
====
+
* Option 2: Verify the network configuration by specifying the VPC subnets IDs. Replace `<region_name>` with your AWS region and `<AWS_account_ID>` with your AWS account ID:
+
[source,terminal]
----
$ rosa verify network --subnet-ids 03146b9b52b6024cb,subnet-03146b9b52b2034cc --region <region_name> --role-arn arn:aws:iam::<AWS_account_ID>:role/my-Installer-Role
----
+
.Example output
[source,terminal]
----
I: Verifying the following subnet IDs are configured correctly: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: pending
I: subnet-03146b9b52b2034cc: passed
I: Run the following command to wait for verification to all subnets to complete:
rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
** Ensure that verification to all subnets completes:
+
[source,terminal]
----
$ rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
+
.Example output
[source,terminal]
----
I: Checking the status of the following subnet IDs: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: passed
I: subnet-03146b9b52b2034cc: passed
----

//OSDOCS-11830 Confirmed verifying via OCM not available for ROSA with HCP
