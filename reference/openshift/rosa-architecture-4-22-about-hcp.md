---
title: "{product-title} overview"
type: reference
domain: openshift
slug: rosa-architecture-4-22-about-hcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/about-hcp
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# {product-title} overview

[id="about-hcp"]
= OpenShift Container Platform overview

//IMPORTANT!!!
//This page includes information from "Understanding ROSA" (rosa-architecture-rosa-understanding) and "What is ROSA" (cloud-experts-getting-started-what-is-rosa). I have intentionally deleted those two modules from the HCP topic map in an effort to condense our introductory materials.

[role="_abstract"]
OpenShift Container Platform is a fully-managed turnkey application platform that allows you to focus on what matters most, delivering value to your customers by building and deploying applications. Red{nbsp}Hat and AWS SRE experts manage the underlying platform so you do not have to worry about infrastructure management. OpenShift Container Platform provides seamless integration with a wide range of AWS compute, database, analytics, machine learning, networking, mobile, AI and other services to further accelerate the building and delivering of differentiating experiences to your customers.

OpenShift Container Platform offers a reduced-cost solution to create a managed OpenShift Container Platform cluster with a focus on efficiency and security. You can quickly create a new cluster and deploy applications in minutes.

You subscribe to the service directly from your AWS account. After you create clusters, you can operate your clusters with the OpenShift web console, the `rosa` CLI, or through {cluster-manager-first}.

You receive OpenShift updates with new feature releases and a shared, common source for alignment with OpenShift Container Platform. OpenShift Container Platform supports the same versions of OpenShift as Red{nbsp}Hat OpenShift Container Platform to achieve version consistency.

image::291_OpenShift_on_AWS_Intro_1122_docs.png[OpenShift Container Platform]

OpenShift Container Platform uses AWS Security Token Service (STS) with AWS IAM to obtain credentials to manage infrastructure in your AWS account. AWS STS is a global web service that creates temporary credentials for IAM users/roles or federated users/roles. OpenShift Container Platform uses this to assign short-term, limited-privilege, security credentials. These credentials are associated with IAM roles that are specific to each component that makes AWS API calls. This method aligns with the principals of least privilege and secure practices in cloud service resource management. The ROSA command-line interface (CLI) tool manages the STS credentials that are assigned for unique tasks and takes action on AWS resources as part of OpenShift functionality. For a more detailed explanation, see AWS STS and OpenShift Container Platform explained.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-key-features_{context}"]
= Key features of OpenShift Container Platform

* *Cluster node scaling:* OpenShift Container Platform requires a minimum of only two nodes, making it ideal for smaller projects while still being able to scale to support larger projects and enterprises. Easily add or remove compute nodes to match resource demand. Autoscaling allows you to automatically adjust the size of the cluster based on the current workload. See About autoscaling nodes on a cluster for more details.

* *Fully managed underlying control plane infrastructure:* Control plane components, such as the API server and etcd database, are hosted in a Red{nbsp}Hat-owned AWS account.
* *Rapid provisioning time:* Provisioning time is approximately 10 minutes.
* *Continued cluster operation during upgrades:* Customers can upgrade the control plane and machine pools separately, ensuring the cluster remains operational during the upgrade process.
* *Native AWS service:* Access and use Red{nbsp}Hat OpenShift on-demand with a self-service onboarding experience through the AWS management console.
* *Flexible, consumption-based pricing:* Scale to your business needs and pay as you go with flexible pricing and an on-demand hourly or annual billing model.
* *Single bill for Red{nbsp}Hat OpenShift and AWS usage:* Customers will receive a single bill from AWS for both Red{nbsp}Hat OpenShift and AWS consumption.
* *Fully integrated support experience:* Management, maintenance, and upgrades are performed by Red{nbsp}Hat site reliability engineers (SREs) with joint Red{nbsp}Hat and Amazon support and a 99.95% service-level agreement (SLA). See the OpenShift Container Platform support documentation for more details.
* *AWS service integration:* AWS has a robust portfolio of cloud services, such as compute, storage, networking, database, analytics, Virtualization and AI. All of these services are directly accessible through OpenShift Container Platform. This makes it easier to build, operate, and scale globally and on-demand through a familiar management interface.
* *Maximum availability:* Deploy clusters across multiple availability zones in supported regions to maximize availability and maintain high availability for your most demanding mission-critical applications and data.
* *Optimized clusters:* Choose from memory-optimized, compute-optimized, general purpose, or accelerated EC2 instance types with clusters to meet your needs.
* *Global availability:* Refer to the product regional availability page to see where OpenShift Container Platform is available globally.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-sdpolicy-billing_{context}"]
= Billing and pricing

OpenShift Container Platform is billed directly to your {AWS} account. ROSA pricing is consumption based, with annual commitments or three-year commitments for greater discounting. The total cost of ROSA consists of two components:

* ROSA service fees
* AWS infrastructure fees

Visit the OpenShift Container Platform Pricing page on the AWS website for more details.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-getting-started-learn_{context}"]
= Getting started with OpenShift Container Platform

[role="_abstract"]
Use the following sections to find content to help you learn about and use OpenShift Container Platform.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="architect_{context}"]
= Architect
[options="header",cols="3*"]
|===
| Learn about OpenShift Container Platform |Plan OpenShift Container Platform deployment |Additional resources

|
OpenShift Container Platform architecture
|
Back up and restore
|
OpenShift Container Platform life cycle

|
|
Understanding process and security

OpenShift Container Platform service definition

Lifecycle updates
|
Getting support

ROSA roadmap
|===

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="cluster-administrator_{context}"]
= Cluster Administrator
[options="header",cols="4*"]
|===
|Learn about OpenShift Container Platform |Deploy OpenShift Container Platform |Manage OpenShift Container Platform |Additional resources
//Row 1
|OpenShift Container Platform architecture
|Installing OpenShift Container Platform
|Logging
|Getting support
//Row 2
|OpenShift Interactive Learning Portal
|Storage
|About OpenShift Container Platform monitoring

OpenShift Container Platform life cycle

OpenShift Container Platform responsibility matrix

|Back up and restore

//Row 3
|About IAM resources
|OpenShift Container Platform roadmap
|About availability

|Upgrading
|
|

|===

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-developer-topics_{context}"]
= Developer

[options="header",cols="3*"]
|===
|Learn about application development in OpenShift Container Platform |Deploy applications |Additional resources

|Red{nbsp}Hat Developers site
|Building applications overview
|Getting support

|{openshift-dev-spaces-productname} (formerly Red{nbsp}Hat CodeReady Workspaces)
|Operators overview
|OpenShift Container Platform roadmap
|

|Images
|

|
|Developer-focused CLI
|

|===

// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
[id="rosa-next-steps-cluster_{context}"]
= Before creating your first OpenShift Container Platform cluster

For additional information about ROSA installation, see a quick introduction to the process in Installing OpenShift Container Platform interactive walkthrough.

[role="_additional-resources"]
== Additional resources

* OpenShift Container Platform product page
* AWS product page
* Red{nbsp}Hat Customer Portal
* Learn about OpenShift
