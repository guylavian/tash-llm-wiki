---
title: "Creating a default {product-title} cluster using Terraform"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-classic-creating-a-cluster-quickly-terraform
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-classic-creating-a-cluster-quickly-terraform
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Creating a default {product-title} cluster using Terraform

[id="rosa-classic-creating-a-cluster-quickly-terraform"]
= Creating a default OpenShift Container Platform cluster using Terraform

[role="_abstract"]
Create a OpenShift Container Platform cluster quickly by using a Terraform cluster template that is configured with the default cluster options.

The cluster creation process described below uses a Terraform configuration that prepares a OpenShift Container Platform AWS Security Token Service (STS) cluster with the following resources:

* An OIDC provider with a managed `oidc-config` configuration
* Prerequisite IAM Operator roles with associated AWS Managed  Policies
* IAM account roles with associated AWS Managed ROSA Policies
* All other AWS resources required to create a OpenShift Container Platform with STS cluster

// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-terraform-overview_{context}"]
= Overview of Terraform

[role="_abstract"]
Terraform is an infrastructure-as-code tool that provides a way to configure your resources once and replicate those resources as desired. Terraform accomplishes the creation tasks by using declarative language. You declare what you want the final state of the infrastructure resource to be, and Terraform creates these resources to your specifications.
// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-sts-terraform-prerequisites_{context}"]
= Prerequisites

[role="_abstract"]
To use the Red{nbsp}Hat Cloud Services provider inside your Terraform configuration, you must meet the following prerequisites:

* You have installed the {rosa-cli} tool.
* You have your offline {cluster-manager-first} token.
* You have installed Terraform version 1.4.6 or newer.
* You have created the ocm-role IAM role.
* You have created the ocm-role IAM role.
* You have created your AWS account-wide IAM roles.
+
The specific account-wide IAM roles and policies provide the STS permissions required for OpenShift Container Platform support, installation, control plane, and compute functionality. This includes account-wide Operator policies. See the Additional resources for more information on the AWS account roles.
* You have an AWS account and associated credentials that allow you to create resources. The credentials are configured for the AWS provider. See the Authentication and Configuration section in AWS Terraform provider documentation.
* You have, at minimum, the following permissions in your AWS IAM role policy that is operating Terraform. Check for these permissions in the AWS console.
+
[source,json]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "iam:GetPolicyVersion",
        "iam:DeletePolicyVersion",
        "iam:CreatePolicyVersion",
        "iam:UpdateAssumeRolePolicy",
        "secretsmanager:DescribeSecret",
        "iam:ListRoleTags",
        "secretsmanager:PutSecretValue",
        "secretsmanager:CreateSecret",
        "iam:TagRole",
        "secretsmanager:DeleteSecret",
        "iam:UpdateOpenIDConnectProviderThumbprint",
        "iam:DeletePolicy",
        "iam:CreateRole",
        "iam:AttachRolePolicy",
        "iam:ListInstanceProfilesForRole",
        "secretsmanager:GetSecretValue",
        "iam:DetachRolePolicy",
        "iam:ListAttachedRolePolicies",
        "iam:ListPolicyTags",
        "iam:ListRolePolicies",
        "iam:DeleteOpenIDConnectProvider",
        "iam:DeleteInstanceProfile",
        "iam:GetRole",
        "iam:GetPolicy",
        "iam:ListEntitiesForPolicy",
        "iam:DeleteRole",
        "iam:TagPolicy",
        "iam:CreateOpenIDConnectProvider",
        "iam:CreatePolicy",
        "secretsmanager:GetResourcePolicy",
        "iam:ListPolicyVersions",
        "iam:UpdateRole",
        "iam:GetOpenIDConnectProvider",
        "iam:TagOpenIDConnectProvider",
        "secretsmanager:TagResource",
        "sts:AssumeRoleWithWebIdentity",
        "iam:ListRoles"
      ],
      "Resource": [
        "arn:aws:secretsmanager:*:<ACCOUNT_ID>:secret:*",
        "arn:aws:iam::<ACCOUNT_ID>:instance-profile/*",
        "arn:aws:iam::<ACCOUNT_ID>:role/*",
        "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/*",
        "arn:aws:iam::<ACCOUNT_ID>:policy/*"
      ]
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": [
        "s3:*"
        ],
      "Resource": "*"
    }
  ]
}
----
// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-sts-terraform-considerations_{context}"]
= Considerations when using Terraform

[role="_abstract"]
In general, using Terraform to manage cloud resources should be done with the expectation that any changes should be done using the Terraform methodology. Use caution when using tools outside of Terraform, such as the AWS console or Red{nbsp}Hat console, to modify cloud resources created by Terraform. Using tools outside Terraform to manage cloud resources that are already managed by Terraform introduces configuration drift from your declared Terraform configuration.

For example, if you upgrade your Terraform-created cluster by using the {hybrid-console-url}, you need to reconcile your Terraform state before applying any forthcoming configuration changes.
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc

[id="rosa-sts-overview-of-the-default-cluster-specifications_{context}"]
= Overview of the default cluster specifications

[role="_abstract"]
You can quickly create a OpenShift Container Platform cluster by using the default installation options.

.Default OpenShift Container Platform cluster specifications

[cols=".^1,.^3a",options="header"]
|===

|Component
|Default specifications

|Accounts and roles
|
* Default IAM role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default IAM role prefix: `ManagedOpenShift`
* Default IAM role prefix: `HCP-ROSA`
* No cluster admin role created

|Cluster settings
|
* Default cluster version: `4.14`
* Cluster name: `rosa-<6-digit-alphanumeric-string>`
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-2 (US East, Ohio)
* Availability: Multi zone for the data plane
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Default cluster version: Latest
* Default AWS region for installations using the {cluster-manager-first} {hybrid-console-second}: us-east-1 (US East, North Virginia)
* Default AWS region for installations using the {rosa-cli} (`rosa`): Defined by your `aws` CLI configuration
* Default EC2 IMDS endpoints (both v1 and v2) are enabled
* EC2 Instance Metadata Service (IMDS) is enabled and allows the use of IMDSv1 or IMDSv2 (token optional)
* Availability: Single zone for the data plane
* Monitoring for user-defined projects: Enabled
* No cluster admin role created
|Encryption
|* Cloud storage is encrypted at rest
* Additional etcd encryption is not enabled
* The default AWS Key Management Service (KMS) key is used as the encryption key for persistent data

|Control plane node configuration
|* Control plane node instance type: m5.2xlarge (8 vCPU, 32 GiB RAM)
* Control plane node count: 3
|Infrastructure node configuration
|* Infrastructure node instance type: r5.xlarge (4 vCPU, 32 GiB RAM)
* Infrastructure node count: 2

|Compute node machine pool
|* Compute node instance type: m5.xlarge (4 vCPU 16, GiB RAM)
* Compute node count: 2
* Compute node count: 3
* Autoscaling: Not enabled
* No additional node labels

|Networking configuration
|
* Cluster privacy: Public
* Cluster privacy: public or private
* You can choose to create a new VPC during the Terraform cluster creation process.
* You must have configured your own Virtual Private Cloud (VPC)
* No cluster-wide proxy is configured

|Classless Inter-Domain Routing (CIDR) ranges
|
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Machine CIDR: 10.0.0.0/16
* Service CIDR: 172.30.0.0/16
* Pod CIDR: 10.128.0.0/14
* Host prefix: /23
+
[NOTE]
====
The static IP address `172.20.0.1` is reserved for the internal Kubernetes API address. The machine, pod, and service CIDRs ranges must not conflict with this IP address.
====

|Cluster roles and policies
|* Mode used to create the Operator roles and the OpenID Connect (OIDC) provider: `auto`
* A configured `ocm-role`, which is required for all OpenShift Container Platform clusters.
+
[NOTE]
====
For installations that use {cluster-manager} on the {hybrid-console-second}, the `auto` mode requires an admin-privileged {cluster-manager} role (ocm-role).
====
* Default Operator role prefix: `rosa-<6-digit-alphanumeric-string>`
* Default Operator role prefix: `<cluster_name>-<4_digit_random_string>`

|Storage
|* Node volumes:
** Type: AWS EBS GP3
** Default size: 300GiB (adjustable at creation time)
* Workload persistent volumes:
** Default StorageClass: gp3-csi
** Provisioner: ebs.csi.aws.com
** Dynamic persistent volume provisioning

|Cluster update strategy
|* Individual updates
* 1 hour grace period for node draining

|===

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-classic-cluster-terraform-creation-intro_{context}"]
= Creating a default OpenShift Container Platform cluster using Terraform

[role="_abstract"]
Terraform provisions account-wide IAM roles and a OpenShift Container Platform cluster with a managed OIDC configuration.
// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc
//

[id="rosa-sts-cluster-terraform-setup_{context}"]
= Preparing your environment for Terraform

[role="_abstract"]
Before you can create your OpenShift Container Platform cluster by using Terraform, you need to export your offline {cluster-manager-first} token.

.Procedure
. *Optional*: Because the Terraform files get created in your current directory during this procedure, you can create a new directory to store these files and navigate into it by running the following command:
+
[source,terminal]
----
$ mkdir terraform-cluster && cd terraform-cluster
----

. Grant permissions to your account by using an offline {cluster-manager-first} token.

. Copy your offline token, and set the token as an environmental variable by running the following command:
+
[source,terminal]
----
$ export RHCS_TOKEN=<your_offline_token>
----
+
[NOTE]
====
This environmental variable resets at the end of each session, such as restarting your machine or closing the terminal.
====

.Verification

* After you export your token, verify the value by running the following command:
+
[source,terminal]
----
$ echo $RHCS_TOKEN
----

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-classic-cluster-terraform-file-creation_{context}"]
= Creating your Terraform files locally

[role="_abstract"]
After you set up your offline {cluster-manager-first} token, you need to create the Terraform files locally to build your cluster. You can create these files by using the following code templates.

.Procedure

. Create the `main.tf` file by running the following command:
+
[source,terminal]
----
$ cat<<-EOF>main.tf
#
# Copyright (c) 2023 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.22.0"
    }
    rhcs = {
      version = ">= 1.6.2"
      source  = "terraform-redhat/rhcs"
    }
  }
}

# Export token using the RHCS_TOKEN environment variable
provider "rhcs" {}

provider "aws" {
  region = var.aws_region
  ignore_tags {
    key_prefixes = ["kubernetes.io/"]
  }
  default_tags {
    tags = var.default_aws_tags
  }
}

data "aws_availability_zones" "available" {}

locals {
  # The default setting creates 3 availability zones. Set to "false" to create a single availability zones.
  region_azs = var.multi_az ? slice([for zone in data.aws_availability_zones.available.names : format("%s", zone)], 0, 3) : slice([for zone in data.aws_availability_zones.available.names : format("%s", zone)], 0, 1)
}

resource "random_string" "random_name" {
  length  = 6
  special = false
  upper   = false
}

locals {
  path                 = coalesce(var.path, "/")
  worker_node_replicas = try(var.worker_node_replicas, var.multi_az ? 3 : 2)
  # If cluster_name is not null, use that, otherwise generate a random cluster name
  cluster_name = coalesce(var.cluster_name, "rosa-\${random_string.random_name.result}")
}

# The network validator requires an additional 60 seconds to validate Terraform clusters.
resource "time_sleep" "wait_60_seconds" {
  count = var.create_vpc ? 1 : 0
  depends_on = [module.vpc]
  create_duration = "60s"
}

module "rosa-classic" {
  source                 = "terraform-redhat/rosa-classic/rhcs"
  version                = "1.5.0"
  cluster_name           = local.cluster_name
  openshift_version      = var.openshift_version
  account_role_prefix    = local.cluster_name
  operator_role_prefix   = local.cluster_name
  replicas               = local.worker_node_replicas
  aws_availability_zones = local.region_azs
  create_oidc            = true
  private                = var.private_cluster
  aws_private_link       = var.private_cluster
  aws_subnet_ids         = var.create_vpc ? var.private_cluster ? module.vpc[0].private_subnets : concat(module.vpc[0].public_subnets, module.vpc[0].private_subnets) : var.aws_subnet_ids
  multi_az               = var.multi_az
  create_account_roles   = true
  create_operator_roles  = true
# Optional: Configure a cluster administrator user \
#
# Option 1: Default cluster-admin user
# Create an administrator user (cluster-admin) and automatically
# generate a password by uncommenting the following parameter:
#  create_admin_user = true
# Generated administrator credentials are displayed in terminal output.
#
# Option 2: Specify administrator username and password
# Create an administrator user and define your own password
# by uncommenting and editing the values of the following parameters:
#  admin_credentials_username = <username>
#  admin_credentials_password = <password>

  depends_on = [time_sleep.wait_60_seconds]
}
EOF
----
+
[NOTE]
====
You can optionally create an administrator user during cluster creation by uncommenting the appropriate parameters in the `main.tf` file and editing their values.
====

. Create the `variables.tf` file by running the following command:
+
[NOTE]
====
Copy and edit this file _before_ running the command to build your cluster.
====
+
[source,terminal]
----
$ cat<<-EOF>variables.tf
#
# Copyright (c) 2023 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
variable "openshift_version" {
  type        = string
  default     = "4.14.20"
  description = "Desired version of OpenShift for the cluster, for example '4.14.20'. If version is greater than the currently running version, an upgrade will be scheduled."
}

variable "create_vpc" {
  type        = bool
  description = "If you would like to create a new VPC, set this value to 'true'. If you do not want to create a new VPC, set this value to 'false'."
}

# ROSA Cluster info
variable "cluster_name" {
  default     = null
  type        = string
  description = "The name of the ROSA cluster to create"
}

variable "additional_tags" {
  default = {
    Terraform   = "true"
    Environment = "dev"
  }
  description = "Additional AWS resource tags"
  type        = map(string)
}

variable "path" {
  description = "(Optional) The arn path for the account/operator roles as well as their policies."
  type        = string
  default     = null
}

variable "multi_az" {
  type        = bool
  description = "Multi AZ Cluster for High Availability"
  default     = true
}

variable "worker_node_replicas" {
  default     = 3
  description = "Number of worker nodes to provision. Single zone clusters need at least 2 nodes, multizone clusters need at least 3 nodes"
  type        = number
}

variable "aws_subnet_ids" {
  type        = list(any)
  description = "A list of either the public or public + private subnet IDs to use for the cluster blocks to use for the cluster"
  default     = ["subnet-01234567890abcdef", "subnet-01234567890abcdef", "subnet-01234567890abcdef"]
}

variable "private_cluster" {
  type        = bool
  description = "If you want to create a private cluster, set this value to 'true'. If you want a publicly available cluster, set this value to 'false'."
}

#VPC Info
variable "vpc_name" {
  type        = string
  description = "VPC Name"
  default     = "tf-qs-vpc"
}

variable "vpc_cidr_block" {
  type        = string
  description = "value of the CIDR block to use for the VPC"
  default     = "10.0.0.0/16"
}

variable "private_subnet_cidrs" {
  type        = list(any)
  description = "The CIDR blocks to use for the private subnets"
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "public_subnet_cidrs" {
  type        = list(any)
  description = "The CIDR blocks to use for the public subnets"
  default     = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}

variable "single_nat_gateway" {
  type        = bool
  description = "Single NAT or per NAT for subnet"
  default     = false
}

#AWS Info
variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "default_aws_tags" {
  type        = map(string)
  description = "Default tags for AWS"
  default     = {}
}
EOF
----

. Create the `vpc.tf` file by running the following command:
+
[source,terminal]
----
$ cat<<-EOF>vpc.tf
#
# Copyright (c) 2023 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.2"

  count = var.create_vpc ? 1 : 0
  name  = var.vpc_name
  cidr  = var.vpc_cidr_block

  azs             = local.region_azs
  private_subnets = var.private_subnet_cidrs
  public_subnets  = var.public_subnet_cidrs

  enable_nat_gateway   = true
  single_nat_gateway   = var.single_nat_gateway
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = var.additional_tags
}
EOF
----
+
You are ready to initiate Terraform.
// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="rosa-sts-cluster-terraform-execute_{context}"]
= Using Terraform to create your OpenShift Container Platform cluster

[role="_abstract"]
After you create the Terraform files, you must initiate Terraform to provide all of the required dependencies. Then apply the Terraform plan.

.Procedure

. Configure Terraform to create your resources based on your Terraform files, run the following command:
+
[source,terminal]
----
$ terraform init
----

. *Optional*: Verify that the Terraform you copied is correct by running the following command:
+
[source,terminal]
----
$ terraform validate
----
+
.Example output
[source,terminal]
----
Success! The configuration is valid.
----

. Create your cluster with Terraform by running the following command:
+
[source,terminal]
----
$ terraform apply
----
+
The Terraform interface asks two questions to create your cluster, similar to the following:
+
[source,terminal]
----
var.create_vpc
  If you would like to create a new VPC, set this value to 'true'. If you do not want to create a new VPC, set this value to 'false'.

  Enter a value:

var.private_cluster
  If you want to create a private cluster, set this value to 'true'. If you want a publicly available cluster, set this value to 'false'.

  Enter a value:
----

. Enter `yes` to proceed or `no` to cancel when the Terraform interface lists the resources to be created or changed and prompts for confirmation:
+
[source,terminal]
----
Plan: 63 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
----
.Example output
[source,terminal]
----
Plan: 74 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
----
+
If you enter `yes`, your Terraform plan starts, creating your AWS account roles, Operator roles, and your OpenShift Container Platform cluster.

.Verification
. Verify that your cluster was created by running the following command:
+
[source,terminal]
----
$ rosa list clusters
----
+
This example shows a cluster in the `ready` state:
+
[source,terminal]
----
ID                                NAME          STATE  TOPOLOGY
27c3snjsupa9obua74ba8se5kcj11269  rosa-tf-demo  ready  Hosted CP
----
[source,terminal]
----
ID                                NAME          STATE  TOPOLOGY
27c3snjsupa9obua74ba8se5kcj11269  rosa-tf-demo  ready  Classic (STS)
----

. Verify that your account roles were created by running the following command:
+
[source,terminal]
----
$ rosa list account-roles
----
+
This example shows the account roles that were created:
+
[source,terminal]
----
I: Fetching account roles
ROLE NAME                                   ROLE TYPE      ROLE ARN                                                           OPENSHIFT VERSION  AWS Managed
ROSA-demo-ControlPlane-Role                 Control plane  arn:aws:iam::<ID>:role/ROSA-demo-ControlPlane-Role                 4.14               No
ROSA-demo-Installer-Role                    Installer      arn:aws:iam::<ID>:role/ROSA-demo-Installer-Role                    4.14               No
ROSA-demo-Support-Role                      Support        arn:aws:iam::<ID>:role/ROSA-demo-Support-Role                      4.14               No
ROSA-demo-Worker-Role                       Worker         arn:aws:iam::<ID>:role/ROSA-demo-Worker-Role                       4.14               No
----

. Verify that your Operator roles were created by running the following command:
+
[source,terminal]
----
$ rosa list operator-roles
----
+
This example shows the Terraform-created Operator roles:
+
[source,terminal]
----
I: Fetching operator roles
ROLE PREFIX    AMOUNT IN BUNDLE
rosa-demo      6
rosa-demo      8
----

// Module included in the following assemblies:
//
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc
// * rosa_install_access_delete_clusters/terraform/rosa-classic-creating-a-cluster-quickly-terraform.adoc

[id="sd-terraform-cluster-destroy_{context}"]
= Deleting your OpenShift Container Platform cluster with Terraform

[role="_abstract"]
Use the `terraform destroy` command to remove all resources you create with the `terraform apply` command.

[NOTE]
====
Keep your Terraform .tf files unchanged before destroying your resources. These variables are matched to resources to delete.
====

.Procedure
. In the directory where you ran the `terraform apply` command to create your cluster, run the following command to delete the cluster:
+
[source,terminal]
----
$ terraform destroy
----
+
The Terraform interface prompts you for two variables. These should match the answers you provided when creating a cluster:
+
[source,terminal]
----
var.create_vpc
  If you would like to create a new VPC, set this value to 'true.' If you do not want to create a new VPC, set this value to 'false.'

  Enter a value:

var.private_cluster
  If you want to create a private cluster, set this value to 'true.' If you want a publicly available cluster, set this value to 'false.'

  Enter a value:
----

. Enter `yes` to start the role and cluster deletion:
+
.Example output
[source,terminal]
----
Plan: 0 to add, 0 to change, 63 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes
----
+
.Example output
[source,terminal]
----
Plan: 0 to add, 0 to change, 74 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes
----

.Verification
. Verify that your cluster was destroyed by running the following command:
+
[source,terminal]
----
$ rosa list clusters
----
+
.Example output showing no cluster
[source,terminal]
----
I: No clusters available
----

. Verify that the account roles were destroyed by running the following command:
+
[source,terminal]
----
$ rosa list account-roles
----
+
.Example output showing no Terraform-created account roles
[source,terminal]
----
I: Fetching account roles
I: No account roles available
----

. Verify that the Operator roles were destroyed by running the following command:
+
[source,terminal]
----
$ rosa list operator-roles
----
+
.Example output showing no Terraform-created Operator roles
[source,terminal]
----
I: Fetching operator roles
I: No operator roles available
----

[role="_additional-resources"]
[id="additional-resources_rosa-classic-creating-a-cluster-quickly-terraform"]
== Additional resources
* Account-wide IAM role and policy reference
