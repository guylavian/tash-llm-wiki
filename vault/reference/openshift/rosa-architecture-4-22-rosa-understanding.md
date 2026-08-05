---
title: "Understanding ROSA"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-understanding
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-understanding
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# Understanding ROSA

[id="rosa-understanding"]
= Understanding ROSA

[role="_abstract"]
Learn about OpenShift Container Platform (ROSA), interacting with ROSA by using {cluster-manager-first} and command-line interface (CLI) tools, consumption experience, and integration with Amazon Web Services (AWS) services.

[id="rosa-understanding-about_{context}"]
== About ROSA

ROSA is a fully-managed, turnkey application platform that allows you to focus on delivering value to your customers by building and deploying applications. Red{nbsp}Hat site reliability engineering (SRE) experts manage the underlying platform so you do not have to worry about the complexity of infrastructure management. ROSA provides seamless integration with Amazon CloudWatch, AWS Identity and Access Management (IAM), Amazon Virtual Private Cloud (VPC), and a wide range of additional AWS services to further accelerate the building and delivering of differentiating experiences to your customers.

You subscribe to the service directly from your AWS account. After you create clusters, you can operate your clusters with the OpenShift web console, the ROSA CLI, or through {cluster-manager-first}.

You receive OpenShift updates with new feature releases and a shared, common source for alignment with OpenShift Container Platform. ROSA supports the same versions of OpenShift as Red{nbsp}Hat OpenShift Dedicated and OpenShift Container Platform to achieve version consistency.

image::291_OpenShift_on_AWS_Intro_1122_docs.png[OpenShift Container Platform]
For additional information about ROSA installation, see Installing Red{nbsp}Hat OpenShift Service on AWS (ROSA) interactive walkthrough.

//[id="rosa-understanding-credential-modes_{context}"]
//== Credential modes

//include::snippets/rosa-sts.adoc[]

//There are two supported credential modes for ROSA clusters. One uses the AWS Security Token Service (STS), which is recommended, and the other uses Identity Access Management (IAM) roles.

//[id="rosa-understanding-aws-sts_{context}"]
//=== ROSA with STS

//AWS STS is a global web service that provides short-term credentials for IAM or federated users. ROSA with STS is the recommended credential mode for ROSA clusters. You can use AWS STS with ROSA to allocate temporary, limited-privilege credentials for component-specific IAM roles. The service enables cluster components to make AWS API calls using secure cloud resource management practices.

//You can use the ROSA CLI (`rosa`) to create the IAM role, policy, and identity provider resources that are required for ROSA clusters that use STS.

//AWS STS aligns with principles of least privilege and secure practices in cloud service resource management. The ROSA CLI manages the STS credentials that are assigned for unique tasks and takes action upon AWS resources as part of OpenShift functionality. One limitation of using STS is that roles must be created for each ROSA cluster.

//The STS credential mode is more secure because:

//- It supports an explicit and limited set of roles and policies that you create ahead of time, and tracks every permission asked for and every role used.
//- The service is limited to the set permissions.
//- When the service is run, it obtains credentials that expire in one hour, so there is no need to rotate or revoke credentials. The expiration also reduces the risks of credentials leaking and being reused.

//A listing of the account-wide and per-cluster roles is provided in ../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-about-iam-resources[About IAM resources for ROSA clusters that use STS].

//[id="rosa-understanding-aws-without-sts_{context}"]
//=== ROSA without STS

//This mode makes use of a pre-created IAM user with `AdministratorAccess` within the account that has proper permissions to create other roles and resources as needed. Using this account the service creates all the necessary resources that are needed for the cluster.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-billing_{context}"]
= Billing and pricing

OpenShift Container Platform is billed directly to your {AWS} account. ROSA pricing is consumption based, with annual commitments or three-year commitments for greater discounting. The total cost of ROSA consists of two components:

* ROSA service fees
* AWS infrastructure fees

Visit the OpenShift Container Platform Pricing page on the AWS website for more details.

[id="rosa-understanding-getting-started_{context}"]
== Getting started

To get started with deploying your cluster, ensure your AWS account has met the prerequisites, you have a Red{nbsp}Hat account ready, and follow the procedures outlined in Getting started with OpenShift Container Platform.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* OpenShift Cluster Manager
//* xref ../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-about-iam-resources[About IAM resources]
* Getting started with OpenShift Container Platform
* AWS pricing page
