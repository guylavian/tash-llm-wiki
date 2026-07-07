---
title: "Tutorial: Deploying an application"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-prerequisites
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-prerequisites
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Deploying an application

[id="cloud-experts-deploying-application-prerequisites"]
= Tutorial: Deploying an application

[role="_abstract"]
This tutorial requires a provisioned OpenShift Container Platform cluster, the OpenShift CLI, and a GitHub account to complete the prerequisites for deploying an application.

== Prerequisites

. A provisioned OpenShift Container Platform cluster
+
This lab assumes you have access to a successfully provisioned a OpenShift Container Platform cluster. If you have not yet created a OpenShift Container Platform cluster, see OpenShift Container Platform quick start guide for more information.
This lab assumes you have access to a successfully provisioned a OpenShift Container Platform cluster. If you have not yet created a OpenShift Container Platform cluster, see OpenShift Container Platform quick start guide for more information.

. The OpenShift Command Line Interface (CLI)
+
For more information, see
Getting started with the OpenShift CLI.
Getting started with the OpenShift CLI.

. A GitHub Account
+
Use your existing GitHub account or register at https://github.com/signup.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-sts-understanding-aws-account-association_{context}"]
= AWS account association

[role="_abstract"]
Before you can use {cluster-manager-first} on the {hybrid-console-url} to create
{hcp-title}
OpenShift Container Platform (ROSA)
clusters that use the AWS Security Token Service (STS), you must associate your AWS account with your Red{nbsp}Hat organization. You can associate your account by creating and linking the following IAM roles.

{cluster-manager} role:: Create an {cluster-manager} IAM role and link it to your Red{nbsp}Hat organization.
+
You can apply basic or administrative permissions to the {cluster-manager} role. The basic permissions enable cluster maintenance using {cluster-manager}. The administrative permissions enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider using {cluster-manager}.
+
You can use the administrative permissions with the {cluster-manager} role to deploy a cluster quickly.

User role:: Create a user IAM role and link it to your Red{nbsp}Hat user account. The Red{nbsp}Hat user account must exist in the Red{nbsp}Hat organization that is linked to your {cluster-manager} role.
+
The user role is used by Red{nbsp}Hat to verify your AWS identity when you use the {cluster-manager} {hybrid-console-second} to install a cluster and the required STS resources.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adocs

[id="rosa-sts-associating-your-aws-account_{context}"]
= Associate your AWS account with your Red{nbsp}Hat organization

[role="_abstract"]
Before using {cluster-manager-first} on the {hybrid-console-url} to create
{rosa-classic-short}
{rosa-short}
clusters that use the AWS Security Token Service (STS), create an {cluster-manager} IAM role and link it to your Red{nbsp}Hat organization. Then, create a user IAM role and link it to your Red{nbsp}Hat user account in the same Red{nbsp}Hat organization.

.Prerequisites

* You have completed the AWS prerequisites for {rosa-short}.
* You have completed the AWS prerequisites for OpenShift Container Platform with STS.
* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform service in the AWS Console.
* You have installed and configured the latest {rosa-cli} (`rosa`) on your installation host.
+
[NOTE]
====
To successfully install
{rosa-short}
ROSA
clusters, use the latest version of the ROSA CLI.
====
* You have logged in to your Red{nbsp}Hat account by using the ROSA CLI.
* You have organization administrator privileges in your Red{nbsp}Hat organization.

.Procedure

. Create an {cluster-manager} role and link it to your Red{nbsp}Hat organization:
+
[NOTE]
====
To enable automatic deployment of the cluster-specific Operator roles and the OpenID Connect (OIDC) provider using the {cluster-manager} {hybrid-console-second}, you must apply the administrative privileges to the role by choosing the _Admin OCM role_ command in the *Accounts and roles* step of creating a
{rosa-short}
ROSA
cluster. For more information about the basic and administrative privileges for the {cluster-manager} role, see _Understanding AWS account association_.
====
+
[NOTE]
====
If you choose the _Basic OCM role_ command in the *Accounts and roles* step of creating a
{rosa-short}
ROSA
cluster in the {cluster-manager} {hybrid-console-second}, you must deploy a
{rosa-short}
ROSA
cluster using manual mode. You will be prompted to configure the cluster-specific Operator roles and the OpenID Connect (OIDC) provider in a later step.
====
+
[source,terminal]
----
$ rosa create ocm-role
----
+
Select the default values at the prompts to quickly create and link the role.
+
. Create a user role and link it to your Red{nbsp}Hat user account:
+
[source,terminal]
----
$ rosa create user-role
----
+
Select the default values at the prompts to quickly create and link the role.
+
[NOTE]
====
The Red{nbsp}Hat user account must exist in the Red{nbsp}Hat organization that is linked to your {cluster-manager} role.
====

.Verification

* Verify that the OCM role and user role were created:
+
[source,terminal]
----
$ rosa list ocm-role
$ rosa list user-role
----

[role="_additional-resources"]
.Additional resources

* AWS prerequisites for ROSA with STS
* Understanding ROSA
* IAM roles in AWS
