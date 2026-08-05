---
title: "Configuring a shared VPC for {product-title} clusters"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-shared-vpc-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-shared-vpc-config
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# Configuring a shared VPC for {product-title} clusters

[id="rosa-hcp-shared-vpc-config"]
= Configuring a shared VPC for OpenShift Container Platform clusters

[role="_abstract"]
You can use a shared virtual private cloud (VPC) to centralize network management in a single AWS account while allowing separate AWS accounts to create OpenShift Container Platform clusters in that VPC.

[NOTE]
====
* This process requires *two separate* AWS accounts that belong to the same AWS organization. One account functions as the VPC-owning AWS account (*VPC Owner*), while the other account creates the cluster in the cluster-creating AWS account (*Cluster Creator*).

* Installing a cluster in a shared VPC is supported only for {ocp-short} 4.17.9 and later.
====

image::522-shared-vpc-overview.png[Overview of the shared VPC configuration workflow between VPC Owner and Cluster Creator accounts.]

*{sp}The hosted zones can be created in either the centrally-managed VPC account or in the workload account in which the cluster is deployed.

[NOTE]
====
Only certain cluster-to-VPC relationships are supported. Multiple OpenShift Container Platform clusters in a single VPC are not supported.
====

== Prerequisites for the *VPC Owner*
* You have an AWS account with the proper permissions to create roles and share resources.
* You enabled resource sharing from the management account for your organization.
* You have access to an AWS entrypoint such as the AWS console or the AWS command-line interface (CLI).

== Prerequisites for the *Cluster Creator*
* You installed the {rosa-cli-first} 1.2.49 or later.
* You created all of the required account roles for creating a cluster.
* You created the `ocm-role` resource.
* The *Cluster Creator's* AWS account is separate from the *VPC Owner's* AWS account.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-shared-vpc-config.adoc

[id="rosa-hcp-sharing-vpc-creation-and-sharing_{context}"]
= Step One - VPC Owner: Configuring a VPC to share within your AWS organization

[role="_abstract"]
You can share subnets within a VPC with another AWS account in your AWS organization.

image::522-shared-vpc-step-1.png[Step one of the shared VPC workflow showing VPC creation and sharing.]

.Procedure

. Create or modify a VPC to your specifications in the VPC section of the AWS console. Ensure you have selected the correct region.
. Create the `Route 53 role`.
+
[NOTE]
====
You must create the `Route 53 role` in the same account where you plan to create the Amazon Route 53 hosted zones (which are created in Step 3). For example, if you want to create the hosted zones in the centrally-managed VPC account, you must create the `Route 53 role` in the *VPC Owner* account. If you want to create the hosted zones in the workload account, you must create the `Route 53 role` in the *Cluster Creator* account.
====
+
.. Create a custom trust policy file that grants permission to assume roles:
+
[source,terminal]
----
$ cat <<EOF > /tmp/route53-role.json
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
The trust policy principals (`Principal.AWS`) may be scoped down to the ingress Operator role and installer account role rather than `root`.
+
.. Create the IAM role for the AWS managed policy `ROSASharedVPCRoute53Policy`.
+
[source,terminal]
----
$ aws iam create-role --role-name <role_name> \
    --assume-role-policy-document file:///tmp/route53-role.json
----
+
.. Attach the AWS managed policy `ROSASharedVPCRoute53Policy` to allow for necessary shared VPC permissions.
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name <role_name> \
--policy-arn arn:aws:iam::aws:policy/ROSASharedVPCRoute53Policy
----
+
. Create the `VPC endpoint role`.
.. Create a custom trust policy file that grants permission to assume roles:
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
The trust policy principals (`Principal.AWS`) may be scoped down to the ingress Operator role and installer account role rather than `root`.
+
.. Create the IAM role for the AWS managed policy `ROSASharedVPCEndpointPolicy`:
+
[source,terminal]
----
$ aws iam create-role --role-name <role_name> \
    --assume-role-policy-document file:///tmp/vpce-role.json
----
+
.. Attach the AWS managed policy `ROSASharedVPCEndpointPolicy` to allow for necessary shared VPC permissions.
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name <role_name> \
--policy-arn arn:aws:iam::aws:policy/ROSASharedVPCEndpointPolicy
----
+
. Provide the `Route 53 role` ARN and the `VPC endpoint role` ARN to the *Cluster Creator* to continue configuration.

[role="_additional-resources"]
.Additional resources
* Sharing your AWS resources (AWS documentation)

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-shared-vpc-config.adoc
[id="rosa-hcp-sharing-vpc-dns-and-roles_{context}"]
= Step Two - Cluster Creator: Reserving your DNS entries and creating cluster Operator roles

[role="_abstract"]
After the *VPC Owner* creates a VPC, subnets, and an IAM role, reserve an `openshiftapps.com` DNS domain and create Operator roles.

[NOTE]
====
For shared VPC clusters, you can choose to create the Operator roles after the cluster creation steps. The cluster is in a `waiting` state until the Ingress Operator role ARN is added to the shared VPC role trusted relationships.
====

image::522-shared-vpc-step-2.png[Step two of the shared VPC workflow showing DNS reservation and Operator role creation.]
.Prerequisites

* You have the `Route 53 role` ARN for the IAM role from the *VPC Owner*.
* You have the `VPC endpoint role` ARN for the IAM role from the *VPC Owner*.

.Procedure

. Reserve an `openshiftapps.com` DNS domain with the following command:
+
[source,terminal]
----
$ rosa create dns-domain --hosted-cp
----
+
The command creates a reserved `openshiftapps.com` DNS domain.
+
[source,terminal]
----
I: DNS domain '14eo.p3.openshiftapps.com' has been created.
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

. Create the account roles by entering the following command:
+
[source,terminal]
----
$ rosa create account-roles \
    --route53-role-arn <Created_Route_53_Role_Arn> \
    --vpc-endpoint-role-arn <Created_VPC_Endpoint_Role_Arn> \
    --prefix <user_defined_account_role_prefix> \
    --hosted-cp
----
+
--
where:

`<Created_Route_53_Role_Arn>`:: Provide the ARN for the Route 53 role that the *VPC Owner* created.
`<Created_VPC_Endpoint_Role_Arn>`:: Provide the ARN for the VPC endpoint role that the *VPC Owner* created.
`<user_defined_account_role_prefix>`:: Provide a prefix for the Operator roles.
--

. Create the Operator roles by entering the following command:
+
[source,terminal]
----
$ rosa create operator-roles --oidc-config-id <oidc-config-ID> \
    --installer-role-arn <Installer_Role> \
    --route53-role-arn <Created_Route_53_Role_Arn> \
    --vpc-endpoint-role-arn <Created_VPC_Endpoint_Role_Arn> \
    --prefix <operator-prefix> \
    --hosted-cp
----
+
--
where:

`<oidc-config-ID>`:: Provide the OIDC configuration ID that you created in the previous step.
`<Installer_Role>`:: Provide your installer ARN that was created as part of the `rosa create account-roles` process.
`<Created_Route_53_Role_Arn>`:: Provide the ARN for the Route 53 role that the *VPC Owner* created.
`<Created_VPC_Endpoint_Role_Arn>`:: Provide the ARN for the VPC endpoint role that the *VPC Owner* created.
`<operator-prefix>`:: Provide a prefix for the Operator roles.
--
+
[NOTE]
====
The Installer account role and the shared VPC roles must have a one-to-one relationship. If you want to create multiple shared VPC roles, you should create one set of account roles per shared VPC role.
====

. After creating the Operator roles, share the _Ingress Operator Cloud Credentials_, _Installer_, and _Control plane Operator Cloud Credentials_ role ARNs with the *VPC Owner*.
+
The shared information resembles these examples:
+
* ``my-rosa-cluster.14eo.p1.openshiftapps.com``
* ``arn:aws:iam::111122223333:role/ManagedOpenShift-Installer-Role``
* ``arn:aws:iam::111122223333:role/my-rosa-cluster-openshift-ingress-operator-cloud-credentials``
* ``arn:aws:iam::111122223333:role/my-rosa-cluster-control-plane-operator``
// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-shared-vpc-config.adoc
[id="rosa-hcp-sharing-vpc-hosted-zones_{context}"]
= Step Three - VPC Owner: Updating the shared VPC role and creating hosted zones

[role="_abstract"]
After the *Cluster Creator* provides the DNS domain and IAM roles, create two hosted zones and update the trust policy on the shared VPC IAM roles.

[NOTE]
====
The hosted zones can be created in either the centrally-managed VPC account or in the workload account.
====

image::522-shared-vpc-step-3.png[Step three of the shared VPC workflow showing hosted zone creation and role updates.]

*{sp}The hosted zones can be created in either the centrally-managed VPC account or in the workload account in which the cluster is deployed.

.Prerequisites

* You have the full domain name from the *Cluster Creator*.
* You have the _Ingress Operator Cloud Credentials_ role's ARN from the *Cluster Creator*.
* You have the _Installer_ role's ARN from the *Cluster Creator*.
* You have the _Control plane Operator Cloud Credentials_ role's ARN from the *Cluster Creator*.

.Procedure

. In the Resource Access Manager of the AWS console, create a resource share that shares the previously created VPC's public and private subnets with the *Cluster Creator's* AWS account ID.

. Update the `Route 53 role` and add the _Installer_ and _Ingress Operator Cloud Credentials_ roles to the principal section of the trust policy.
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
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-hcp-Installer-Role",
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-control-plane-operator"
        ]
	  },
	  "Action": "sts:AssumeRole"
	}
  ]
}
----

. Update the `VPC endpoint role` and add the _Installer_ and _Ingress Operator Cloud Credentials_ roles to the principal section of the trust policy.
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
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-hcp-Installer-Role",
          "arn:aws:iam::<Cluster-Creator's-AWS-Account-ID>:role/<prefix>-control-plane-operator"
        ]
	  },
	  "Action": "sts:AssumeRole"
	}
  ]
}
----

. Create a private hosted zone in the Route 53 section of the AWS console. In the hosted zone configuration, the domain name is `rosa.<cluster-name>.<base-domain>`. The private hosted zone must be associated with the network owner's VPC.
. Create a local hosted zone in the Route 53 section of the AWS console. In the hosted zone configuration, the domain name is `<cluster-name>.hypershift.local`. The local hosted zone must be associated with the network owner's VPC.
. After the hosted zones are created and associated with the network owner's VPC, provide the following to the *Cluster Creator* to continue configuration:
* Hosted zone IDs
* AWS region
* Subnet IDs
// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-shared-vpc-config.adoc
[id="rosa-hcp-sharing-vpc-cluster-creation_{context}"]
= Step Four - Cluster Creator: Creating your cluster in a shared VPC

[role="_abstract"]
You can create a OpenShift Container Platform cluster in a shared VPC by using the {rosa-cli-first}.

[NOTE]
====
Installing a cluster in a shared VPC is supported only for OpenShift 4.17.9 and later.
====

image::372_OpenShift_on_AWS_persona_worflows_0923_4.png[Step four of the shared VPC persona workflow showing Cluster Creator actions.]
.Prerequisites

* You have the hosted zone IDs from the *VPC Owner*.
* You have the AWS region from the *VPC Owner*.
* You have the subnet IDs from the *VPC Owner*.
* You have the `Route 53 role` ARN from the *VPC Owner*.
* You have the `VPC endpoint role` ARN from the *VPC Owner*.

.Procedure
* In a terminal, enter the following command to create the shared VPC:
+
[source,terminal]
----
$ rosa create cluster --cluster-name <cluster_name> --sts --operator-roles-prefix <prefix> --oidc-config-id <oidc_config_id> --region us-east-1 --subnet-ids <subnet_ids> --hcp-internal-communication-hosted-zone-id <local_hosted_zone_ID> --ingress-private-hosted-zone-id <private_hosted_zone_ID> --route53-role-arn <route_53_role_arn> vpc-endpoint-role-arn <vpc_endpoint_role_arn> --base-domain <dns-domain> --additional-allowed-principals <route53-role-arn>,<vpc-endpoint-role-arn> --hosted-cp
----

[role="_additional-resources"]
[id="additional-resources_rosa-hcp-shared-vpc-config"]
== Additional resources

* Multiple OpenShift Container Platform clusters in a single VPC
* Enable resource sharing within AWS Organizations (AWS documentation)
* {rosa-cli} download page
* Creating the account-wide STS roles and policies
