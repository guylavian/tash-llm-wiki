---
title: "Configuring a shared VPC for ROSA clusters"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-shared-vpc-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-shared-vpc-config
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Configuring a shared VPC for ROSA clusters

[id="rosa-shared-vpc-config"]
= Configuring a shared VPC for ROSA clusters

[role="_abstract"]
You can create OpenShift Container Platform clusters in shared, centrally-managed AWS virtual private clouds (VPCs).

[NOTE]
====
This process requires *two separate* AWS accounts that belong to the same AWS organization. One account functions as the VPC-owning AWS account (*VPC Owner*), while the other account creates the cluster in the cluster-creating AWS account (*Cluster Creator*).
====

image::372_OpenShift_on_AWS_persona_worflows_0923_all.png[]

== Prerequisites for the VPC Owner

* You have an AWS account with the proper permissions to create roles and share resources.
* The *Cluster Creator's* AWS account is separate from the *VPC Owner's* AWS account.
* Both AWS accounts belong to the same AWS organization.
* You enabled resource sharing from the management account for your organization.
* You have access to the AWS console.

== Prerequisites for the Cluster Creator

* You installed the ROSA CLI (`rosa`) 1.2.26 or later.
* You created all of the required
account-wide roles and policies
* account-wide roles and policies
for creating a cluster.
* You have created your `ocm-role` resource.
* The *Cluster Creator's* AWS account is separate from the *VPC Owner's* AWS account.
* Both AWS accounts belong to the same AWS organization.

[NOTE]
====
Installing a cluster in a shared VPC is supported only for OpenShift 4.12.34 and later, 4.13.10 and later, and all future 4.y-streams.
====

// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc

[id="rosa-sharing-vpc-creation-and-sharing_{context}"]
= Step One - VPC Owner: Configuring a VPC to share within your AWS organization

[role="_abstract"]
You can share subnets within a configured VPC with another AWS user account if that account is within your current AWS organization.

image::372_OpenShift_on_AWS_persona_worflows_0923_1.png[]
.Procedure

. Create or modify a VPC to your specifications in the VPC section of the AWS console.
+
. Create a custom policy file to allow for necessary shared VPC permissions that uses the name `SharedVPCPolicy`:
+
[source,terminal]
----
$ cat <<EOF > /tmp/shared-vpc-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets",
                "route53:ListHostedZones",
                "route53:ListHostedZonesByName",
                "route53:ListResourceRecordSets",
                "route53:ChangeTagsForResource",
                "route53:GetAccountLimit",
                "route53:GetChange",
                "route53:GetHostedZone",
                "route53:ListTagsForResource",
                "route53:UpdateHostedZoneComment",
                "tag:GetResources",
                "tag:UntagResources"
            ],
            "Resource": "*"
        }
    ]
}
EOF
----
+
. Create the policy in AWS:
+
[source,terminal]
----
$ aws iam create-policy \
    --policy-name SharedVPCPolicy \
    --policy-document file:///tmp/shared-vpc-policy.json
----
+
You will attach this policy to a role necessary for the shared VPC permissions.
+
. Create a custom trust policy file that grants permission to assume roles. Replace `<Account-ID>` with the *Cluster Creator's* AWS account ID. The principal will be scoped down after the *Cluster Creator* creates the necessary cluster roles. On creation, you must create a root user placeholder by using the *Cluster Creator's* AWS account ID as `arn:aws:iam::{Account}:root`.
+
[source,terminal]
----
$ cat <<EOF > /tmp/shared-vpc-role.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<Account-ID>:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
----
+
. Create the IAM role. Replace `<role_name>` with the name of the role you want to create.
+
[source,terminal]
----
$ aws iam create-role --role-name <role_name> \
    --assume-role-policy-document file:///tmp/shared-vpc-role.json
----
+
. Attach the custom `SharedVPCPolicy` permissions policy.
+
[source, terminal]
----
$ aws iam attach-role-policy --role-name <role_name> --policy-arn \
    arn:aws:iam::<AWS_account_ID>:policy/SharedVPCPolicy
----
+
--
where:

`<role_name>`:: Replace with the name of the role you created.
`<AWS_account_ID>`:: Replace with the *VPC Owner's* AWS account ID.
--

. Provide the `SharedVPCRole` ARN to the *Cluster Creator* to continue configuration.

[role="_additional-resources"]
[id="additional-resources_shared-vpc_vpc-creation"]
== Additional resources
* AWS documentation on sharing your AWS resources

// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc
[id="rosa-sharing-vpc-dns-and-roles_{context}"]
= Step Two - Cluster Creator: Reserving your DNS and creating cluster operator roles

[role="_abstract"]
After the *VPC Owner* creates a virtual private cloud, subnets, and an IAM role for sharing the VPC resources, reserve an `openshiftapps.com` DNS domain and create Operator roles to communicate back to the *VPC Owner*.

[NOTE]
====
For shared VPC clusters, you can choose to create the Operator roles after the cluster creation steps. The cluster will be in a `waiting` state until the Ingress Operator role ARN is added to the shared VPC role trusted relationships.
====

image::372_OpenShift_on_AWS_persona_worflows_0923_2.png[]
.Prerequisites

* You have the `SharedVPCRole` ARN for the IAM role from the *VPC Owner*.

.Procedure

. Reserve an `openshiftapps.com` DNS domain with the following command:
+
[source,terminal]
----
$ rosa create dns-domain
----
+
The command creates a reserved `openshiftapps.com` DNS domain.
+
[source,terminal]
----
I: DNS domain '14eo.p1.openshiftapps.com' has been created.
I: To view all DNS domains, run 'rosa list dns-domains'
----
. Create an OIDC configuration.
+
Review this article for more information on the OIDC configuration process. The following command produces the OIDC configuration ID that you need:
+
[source,terminal]
----
$ rosa create oidc-config
----
+
You receive confirmation that the command created an OIDC configuration:
+
[source,terminal]
----
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 25tu67hq45rto1am3slpf5lq6jargg
----

. Create the Operator roles by entering the following command. Provide the OIDC configuration ID from the previous step, your installer ARN that was created as part of the `rosa create account-roles` process, the ARN for the role that the *VPC Owner* created, and a prefix for the Operator roles.
+
[source,terminal]
----
$ rosa create operator-roles --oidc-config-id <oidc-config-ID> \
    --installer-role-arn <Installer_Role> \
    --shared-vpc-role-arn <Created_VPC_Role_Arn> \
    --prefix <operator-prefix>
----
+
[NOTE]
====
The Installer account role and the shared VPC role must have a one-to-one relationship. If you want to create multiple shared VPC roles, you should create one set of account roles per shared VPC role.
====

 . After creating the Operator roles, share the following information with the *VPC Owner* to proceed with the configuration:
+
--
** The full domain name, `<intended_cluster_domain_prefix>.<reserved_dns_domain>` (for example, `my-rosa-cluster.14eo.p1.openshiftapps.com`)
** The ARN for your Installer role (for example, `arn:aws:iam::111122223333:role/ManagedOpenShift-Installer-Role`)
** The ARN for your Ingress Operator Cloud Credentials role (for example, `arn:aws:iam::111122223333:role/my-rosa-cluster-openshift-ingress-operator-cloud-credentials`)
--
// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc
[id="rosa-sharing-vpc-hosted-zones_{context}"]
= Step Three - VPC Owner: Updating the shared VPC role and creating hosted zones

[role="_abstract"]
After the *Cluster Creator* provides the DNS domain and the IAM roles, create a private hosted zone and update the trust policy on the IAM role that was created for sharing the VPC.

image::372_OpenShift_on_AWS_persona_worflows_0923_3.png[]
.Prerequisites

* You have the full domain name from the *Cluster Creator*.
* You have the _Ingress Operator Cloud Credentials_ role's ARN from the *Cluster Creator*.
* You have the _Installer_ role's ARN from the *Cluster Creator*.

.Procedure

. In the Resource Access Manager of the AWS console, create a resource share that shares the previously created public and private subnets with the *Cluster Creator's* AWS account ID.

. Update the VPC sharing IAM role and add the _Installer_ and _Ingress Operator Cloud Credentials_ roles to the principal section of the trust policy.
+
[source,terminal]
----
{
  "Version": "2012-10-17",
  "Statement": [
    {
	  "Sid": "Statement1",
	  "Effect": "Allow",
	  "Principal": {
	  	"AWS": [
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-ingress-operator-cloud-credentials",
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-Installer-Role"
        ]
	  },
	  "Action": "sts:AssumeRole"
	}
  ]
}
----
. Create a private hosted zone in the Route 53 section of the AWS console. In the hosted zone configuration, the domain name is `<cluster_domain_prefix>.<reserved_dns_domain>`. The private hosted zone must be associated with the created VPC.
. After the hosted zone is created and associated with the VPC, provide the following to the *Cluster Creator* to continue configuration:
* Hosted zone ID
* AWS region
* Subnet IDs
// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc
[id="rosa-sharing-vpc-cluster-creation_{context}"]
= Step Four - Cluster Creator: Creating your cluster in a shared VPC

[role="_abstract"]
To create a cluster in a shared VPC, complete the following steps.

[NOTE]
====
Installing a cluster in a shared VPC is supported only for OpenShift 4.12.34 and later, 4.13.10 and later, and all future 4.y-streams.
====

image::372_OpenShift_on_AWS_persona_worflows_0923_4.png[]
.Prerequisites

* You have the hosted zone ID from the *VPC Owner*.
* You have the AWS region from the *VPC Owner*.
* You have the subnet IDs from the *VPC Owner*.
* You have the `SharedVPCRole` ARN from the *VPC Owner*.

.Procedure
* In a terminal, enter the following command to create the shared VPC:
+
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> --sts \
  --operator-roles-prefix <prefix> \
  --oidc-config-id <oidc_config_id> \
  --region us-east-1 \
  --subnet-ids <subnet_ids> \
  --private-hosted-zone-id <hosted_zone_ID> \
  --shared-vpc-role-arn <vpc-role-arn> \
  --base-domain <dns-domain>
----
+
