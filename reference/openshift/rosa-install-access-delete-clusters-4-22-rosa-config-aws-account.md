---
title: "Configuring your AWS account"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-config-aws-account
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-config-aws-account
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Configuring your AWS account

[id="rosa-config-aws-account"]
= Configuring your AWS account

[role="_abstract"]
After you complete the AWS prerequisites, configure your AWS account and enable the OpenShift Container Platform service.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-config-aws-account.adoc

[id="rosa-configuring-aws-account_{context}"]
= Configuring your AWS account

[role="_abstract"]
To configure your AWS account to use the OpenShift Container Platform service, complete the following steps.

.Prerequisites

* Review and complete the deployment prerequisites and policies.
* Create a Red{nbsp}Hat account, if you do not already have one. Then, check your email for a verification link. You will need these credentials to install ROSA.

.Procedure

. Log in to the Amazon Web Services (AWS) account that you want to use.
+
A dedicated AWS account is recommended to run production clusters. If you are using AWS Organizations, you can use an AWS account within your organization or create a new one.
+
If you are using AWS Organizations and you need to have a service control policy (SCP) applied to the AWS account you plan to use, see AWS Prerequisites for details on the minimum required SCP.
+
As part of the cluster creation process, `rosa` establishes an `osdCcsAdmin` IAM user. This user uses the IAM credentials you provide when configuring the AWS CLI.
+
[NOTE]
====
This user has `Programmatic` access enabled and the `AdministratorAccess` policy attached to it.
====
+
. Enable the ROSA service in the AWS Console.
.. Sign in to your AWS account.
.. To enable ROSA, go to the ROSA service and select *Enable OpenShift*.

. Install and configure the AWS CLI.
.. Follow the AWS command-line interface documentation to install and configure the AWS CLI for your operating system.
+
Specify the correct `aws_access_key_id` and `aws_secret_access_key` in the `.aws/credentials` file. See AWS Configuration basics in the AWS documentation.

.. Set a default AWS region.
+
[NOTE]
====
It is recommended to set the default AWS region by using the environment variable.
====
+
The OpenShift Container Platform service evaluates regions in the following priority order:
+
... The region specified when running the `rosa` command with the `--region` flag.
... The region set in the `AWS_DEFAULT_REGION` environment variable. See Environment variables to configure the AWS CLI in the AWS documentation.
... The default region set in your AWS configuration file. See Quick configuration with aws configure in the AWS documentation.
.. Optional: Configure your AWS CLI settings and credentials by using an AWS named profile. `rosa` evaluates AWS named profiles in the following priority order:
... The profile specified when running the `rosa` command with the `--profile` flag.
... The profile set in the `AWS_PROFILE` environment variable. See Named profiles in the AWS documentation.
.. Verify the AWS CLI is installed and configured correctly by running the following command to query the AWS API:
+
[source,terminal]
----
$ aws sts get-caller-identity --output text
----
+
.Example output
[source,terminal]
----
<aws_account_id>    arn:aws:iam::<aws_account_id>:user/<username>  <aws_user_id>
----
+
After completing these steps, install OpenShift Container Platform.

[id="additional-resources_rosa-config-aws-account"]
[role="_additional-resources"]
== Additional resources

* AWS prerequisites
* Required AWS service quotas and requesting increases
* Understanding the ROSA deployment workflow
