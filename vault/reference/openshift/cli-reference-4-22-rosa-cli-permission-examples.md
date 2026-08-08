---
title: "Least privilege permissions for {rosa-cli} commands"
type: reference
domain: openshift
slug: cli-reference-4-22-rosa-cli-permission-examples
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/rosa-cli-permission-examples
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Least privilege permissions for {rosa-cli} commands

[id="rosa-cli-permission-examples"]
= Least privilege permissions for {rosa-cli} commands

[role="_abstract"]
Create IAM roles that grant only the rights each user needs for {rosa-cli-first} tasks. The examples here use least privilege with the {rosa-cli}.
[IMPORTANT]
====
Although the policies and commands presented in this topic will work in conjunction with one another, you might have other restrictions within your AWS environment that make the policies for these commands insufficient for your specific needs. Red{nbsp}Hat provides these examples as a baseline, assuming no other AWS Identity and Access Management (IAM) restrictions are present.
====

// Omitting from HCP build until BM gets to review
// [NOTE]
// ====
// The examples listed cover several of the most common {rosa-cli} commands. For more information regarding {rosa-cli} commands, see Common commands and arguments.
// ====

// include::modules/rosa-cli-hcp-classic-examples.adoc[leveloffset=+1]
// Module included in the following assemblies:
//
// * rosa_cli/rosa-cli-permission-examples.adoc

[id="rosa-cli-hcp-examples_{context}"]
= Least privilege permissions for common {rosa-cli} commands

[role="_abstract"]
These examples list the least privilege IAM permissions for common {rosa-cli-first} commands when you build OpenShift Container Platform clusters.

[id="rosa-create-OIDC-providers-hcp-classic_{context}"]
== Create a managed OpenID Connect (OIDC) provider
Run the following command with the specified permissions to create your managed OIDC provider by using `auto` mode.

.Input
[source,terminal]
----
$ rosa create oidc-config --mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateOidcConfig",
            "Effect": "Allow",
            "Action": [
                "iam:TagOpenIDConnectProvider",
                "iam:CreateOpenIDConnectProvider"
            ],
            "Resource": "*"
        }
    ]
}
----
[id="rosa-create-unmanaged-OIDC-providers-hcp-classic_{context}"]
== Create an unmanaged OpenID Connect provider
Run the following command with the specified permissions to create your unmanaged OIDC provider by using `auto` mode.

.Input
[source,terminal]
----
$ rosa create oidc-config --mode auto --managed=false
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:TagOpenIDConnectProvider",
                "iam:ListRoleTags",
                "iam:ListRoles",
                "iam:CreateOpenIDConnectProvider",
                "s3:CreateBucket",
                "s3:PutObject",
                "s3:PutBucketTagging",
                "s3:PutBucketPolicy",
                "s3:PutObjectTagging",
                "s3:PutBucketPublicAccessBlock",
                "secretsmanager:CreateSecret",
                "secretsmanager:TagResource"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-account-roles-hcp-classic_{context}"]
== List your account roles
Run the following command with the specified permissions to list your account roles.

.Input
[source,terminal]
----
$ rosa list account-roles
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListAccountRoles",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:ListRoles"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-operator-roles-hcp-classic_{context}"]
== List your Operator roles
Run the following command with the specified permissions to list your Operator roles.

.Input
[source,terminal]
----
$ rosa list operator-roles
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListOperatorRoles",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:ListPolicyTags"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-OIDC-providers-hcp-classic_{context}"]
== List your OIDC providers

Run the following command with the specified permissions to list your OIDC providers.

.Input
[source,terminal]
----
$ rosa list oidc-providers
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListOidcProviders",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:ListOpenIDConnectProviderTags"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-verify-quota-hcp-classic_{context}"]
== Verify your quota

Run the following command with the specified permissions to verify your quota.

.Input
[source,terminal]
----
$ rosa verify quota
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VerifyQuota",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeAccountLimits",
                "servicequotas:ListServiceQuotas"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-delete-oidc-config-hcp-classic_{context}"]
== Delete your managed OIDC configuration

Run the following command with the specified permissions to delete your managed OIDC configuration by using `auto` mode.

.Input
[source,terminal]
----
$ rosa delete oidc-config -–mode auto
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeleteOidcConfig",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:DeleteOpenIDConnectProvider"
            ],
            "Resource": "*"
        }
    ]
}

----
[id="rosa-delete-unmanaged-oidc-config-hcp-classic_{context}"]
== Delete your unmanaged OIDC configuration

Run the following command with the specified permissions to delete your unmanaged OIDC configuration by using `auto` mode.

.Input
[source,terminal]
----
$ rosa delete oidc-config -–mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:DeleteOpenIDConnectProvider",
                "secretsmanager:DeleteSecret",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:DeleteBucket"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-create-hcp-cluster_{context}"]
== Create a cluster

Run the following command with the specified permissions to create OpenShift Container Platform clusters.

.Input
[source,terminal]
----
$ rosa create cluster --hosted-cp
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateCluster",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeAvailabilityZones"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-create-account-operator-roles-hcp_{context}"]
== Create your account roles and Operator roles

Run the following command with the specified permissions to create account and Operator roles by using `auto` mode.

.Input
[source,terminal]
----
$ rosa create account-roles --mode auto --hosted-cp
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateAccountRoles",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:UpdateAssumeRolePolicy",
                "iam:ListRoleTags",
                "iam:GetPolicy",
                "iam:TagRole",
                "iam:ListRoles",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:ListPolicyTags"
            ],
            "Resource": "*"
        }
    ]
}

----
[id="rosa-delete-account-roles-hcp_{context}"]
== Delete your account roles

Run the following command with the specified permissions to delete the account roles in `auto` mode.

.Input
[source,terminal]
----
$ rosa delete account-roles -–mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeleteAccountRoles",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListInstanceProfilesForRole",
                "iam:DetachRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:DeleteRole",
                "iam:ListRolePolicies"
            ],
            "Resource": "*"
        }
    ]
}

----
[id="rosa-delete-operator-roles-hcp_{context}"]
== Delete your Operator roles

Run the following command with the specified permissions to delete your Operator roles in `auto` mode.

.Input
[source,terminal]
----
$ rosa delete operator-roles -–mode auto
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeleteOperatorRoles",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:DetachRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:DeleteRole"
            ],
            "Resource": "*"
        }
    ]
}

----
// Module included in the following assemblies:
//
// * rosa_cli/rosa-cli-permission-examples.adoc

[id="rosa-cli-classic-examples_{context}"]
= Least privilege permissions for common {rosa-cli} commands

[role="_abstract"]
These examples list the least privilege IAM permissions for common {rosa-cli} commands when you build OpenShift Container Platform clusters.

[id="rosa-create-OIDC-providers-hcp-classic_{context}"]
== Create a managed OpenID Connect (OIDC) provider
Run the following command with the specified permissions to create your managed OIDC provider by using `auto` mode.

.Input
[source,terminal]
----
$ rosa create oidc-config --mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateOidcConfig",
            "Effect": "Allow",
            "Action": [
                "iam:TagOpenIDConnectProvider",
                "iam:CreateOpenIDConnectProvider"
            ],
            "Resource": "*"
        }
    ]
}
----
[id="rosa-create-unmanaged-OIDC-providers-hcp-classic_{context}"]
== Create an unmanaged OpenID Connect provider
Run the following command with the specified permissions to create your unmanaged OIDC provider by using `auto` mode.

.Input
[source,terminal]
----
$ rosa create oidc-config --mode auto --managed=false
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:TagOpenIDConnectProvider",
                "iam:ListRoleTags",
                "iam:ListRoles",
                "iam:CreateOpenIDConnectProvider",
                "s3:CreateBucket",
                "s3:PutObject",
                "s3:PutBucketTagging",
                "s3:PutBucketPolicy",
                "s3:PutObjectTagging",
                "s3:PutBucketPublicAccessBlock",
                "secretsmanager:CreateSecret",
                "secretsmanager:TagResource"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-account-roles-hcp-classic_{context}"]
== List your account roles
Run the following command with the specified permissions to list your account roles.

.Input
[source,terminal]
----
$ rosa list account-roles
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListAccountRoles",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:ListRoles"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-operator-roles-hcp-classic_{context}"]
== List your Operator roles
Run the following command with the specified permissions to list your Operator roles.

.Input
[source,terminal]
----
$ rosa list operator-roles
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListOperatorRoles",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:ListPolicyTags"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-list-OIDC-providers-hcp-classic_{context}"]
== List your OIDC providers

Run the following command with the specified permissions to list your OIDC providers.

.Input
[source,terminal]
----
$ rosa list oidc-providers
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListOidcProviders",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:ListOpenIDConnectProviderTags"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-verify-quota-hcp-classic_{context}"]
== Verify your quota

Run the following command with the specified permissions to verify your quota.

.Input
[source,terminal]
----
$ rosa verify quota
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VerifyQuota",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeAccountLimits",
                "servicequotas:ListServiceQuotas"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-delete-oidc-config-hcp-classic_{context}"]
== Delete your managed OIDC configuration

Run the following command with the specified permissions to delete your managed OIDC configuration by using `auto` mode.

.Input
[source,terminal]
----
$ rosa delete oidc-config -–mode auto
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeleteOidcConfig",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:DeleteOpenIDConnectProvider"
            ],
            "Resource": "*"
        }
    ]
}

----
[id="rosa-delete-unmanaged-oidc-config-hcp-classic_{context}"]
== Delete your unmanaged OIDC configuration

Run the following command with the specified permissions to delete your unmanaged OIDC configuration by using `auto` mode.

.Input
[source,terminal]
----
$ rosa delete oidc-config -–mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:ListOpenIDConnectProviders",
                "iam:DeleteOpenIDConnectProvider",
                "secretsmanager:DeleteSecret",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:DeleteBucket"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-min-permissions-required-classic_{context}"]
== Create a cluster

Run the following command with the specified permissions to create a OpenShift Container Platform cluster with least privilege permissions.

.Input
[source,terminal]
----
$ rosa create cluster
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateCluster",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListRoleTags",
                "iam:ListRoles"
            ],
            "Resource": "*"
        }
    ]
}

----

[id="rosa-create-account-operator-roles-classic_{context}"]
== Create account roles and Operator roles

Run the following command with the specified permissions to create account and Operator roles in `auto' mode.

.Input
[source,terminal]
----
$ rosa create account-roles --mode auto --classic
----
.Policy
[source,json]
----

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateAccountOperatorRoles",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:UpdateAssumeRolePolicy",
                "iam:ListRoleTags",
                "iam:GetPolicy",
                "iam:TagRole",
                "iam:ListRoles",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:TagPolicy",
                "iam:CreatePolicy",
                "iam:ListPolicyTags"
            ],
            "Resource": "*"
        }
    ]
}

----
[id="rosa-delete-account-roles-classic_{context}"]
== Delete your account roles

Run the following command with the specified permissions to delete the account roles in `auto` mode.

.Input
[source,terminal]
----
$ rosa delete account-roles -–mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListInstanceProfilesForRole",
                "iam:DetachRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:DeleteRole",
                "iam:ListRolePolicies",
                "iam:GetPolicy",
                "iam:ListPolicyVersions",
                "iam:DeletePolicy"
            ],
            "Resource": "*"
        }
    ]
}
----

[id="rosa-delete-operator-roles-classic_{context}"]
== Delete your Operator roles

Run the following command with the specified permissions to delete the Operator roles in `auto` mode.

.Input
[source,terminal]
----
$ rosa delete operator-roles -–mode auto
----
.Policy
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:ListInstanceProfilesForRole",
                "iam:DetachRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListRoles",
                "iam:DeleteRole",
                "iam:ListRolePolicies",
                "iam:GetPolicy",
                "iam:ListPolicyVersions",
                "iam:DeletePolicy"
            ],
            "Resource": "*"
        }
    ]
}

----
// Module included in the following assemblies:
//
// * rosa_cli/rosa-cli-permission-examples.adoc

[id="rosa-cli-no-permissions-required_{context}"]
= {rosa-cli} commands with no required permissions

[role="_abstract"]
These {rosa-cli-first} commands do not need IAM policies. They need an access key, a secret key, or an attached role.

.Commands
[cols="30,70", options="header"]
|===

|Command
|Input

|list cluster
|`$ rosa list cluster`

|list versions
|`$ rosa list versions`

|describe cluster
|`$ rosa describe cluster -c <cluster name>`

|create admin
|`$ rosa create admin -c <cluster name>`

|list users
|`$ rosa list users -c <cluster-name>`

|list upgrades
|`$ rosa list upgrades`

|list OIDC configuration
|`$ rosa list oidc-config`

|list identity providers
|`$ rosa list idps -c <cluster-name>`

|list ingresses
|`$ rosa list ingresses -c <cluster-name>`

|===

[role="_additional-resources"]
[id="additional-resources_min-permissions-required"]
== Additional resources

* IAM roles
* Policies and permissions in IAM
