---
title: "Creating a private cluster on {product-title}"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-aws-private-creating-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-aws-private-creating-cluster
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# Creating a private cluster on {product-title}

[id="rosa-hcp-aws-private-creating-cluster"]
= Creating a private cluster on OpenShift Container Platform

[role="_abstract"]
For OpenShift Container Platform workloads that do not require public internet access, you can create a private cluster.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-fips-encryption.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster,  you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Configure a virtual private cloud (VPC)
* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

// Module included in the following assemblies:
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * support/troubleshooting/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-ocm-roles-and-permissions-iam-basic-role_{context}"]
= Creating an ocm-role IAM role

[role="_abstract"]
You create your `ocm-role` IAM roles by using the {rosa-cli-first}. If you want to create and manage clusters by using only the {rosa-cli-first} and the OpenShift CLI (`oc`), you can use the `--no-console` profile for the `ocm-role` IAM resource. For more information about the `ocm-role` IAM resource permissions profile, see the _Additional resources_.

[IMPORTANT]
====
You must create the `ocm-role` IAM role before you can create your OpenShift Container Platform cluster.
====

.Prerequisites

* You have an AWS account.
* You have Red{nbsp}Hat Organization Administrator privileges in the {cluster-manager} organization.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest {rosa-cli}, `rosa`, on your installation host.

.Procedure
* Run one of the following commands to create the required `ocm-role` IAM resource:
+
[IMPORTANT]
====
The process to change your `ocm-role` IAM resource profile requires you to unlink and delete the current `ocm-role` IAM resource and create a new one with the required profile.
====

** To create an `ocm-role` IAM role with standard privileges, run the following command:
+
[source,terminal]
----
$ rosa create ocm-role
----
+
** To create an `ocm-role` IAM role with admin privileges, run the following command:
+
[IMPORTANT]
====
The admin profile supports "auto" mode configuration for OpenShift Container Platform clusters which provisions OIDC Configuration and Operator roles automatically. To achieve this automatic flow, the profile has a wider set of permissions than the standard profile.
====
+
[source,terminal]
----
$ rosa create ocm-role --admin
----
+
This command allows you to create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the {rosa-cli} (`rosa`) create your Operator roles and policies.
See "Methods of account-wide role creation" for more information. The following example shows what your creation flow might look like.
+
[source,terminal]
----
I: Creating ocm role
? Role prefix: ManagedOpenShift
? Enable admin capabilities for the OCM role (optional): No
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::<ARN>:user/<UserName>'
? Create the 'ManagedOpenShift-OCM-Role-182' role? Yes
I: Created role 'ManagedOpenShift-OCM-Role-182' with ARN  'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'? Yes
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' with organization account '<AWS ARN>'
----
+
where:
+
--
`Role prefix`:: A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
`Enable admin capabilities for the OCM role (optional)`:: Choose if you want this role to have the additional admin permissions.
+
[NOTE]
====
You do not see this prompt if you used the `--admin` option.
====
+
`Permissions boundary ARN (optional)`:: The Amazon Resource Name (ARN) of the policy to set permission boundaries.
`Role Path (optional)`:: Specify an IAM path for the user name.
`Role creation mode`:: Choose the method to create your AWS roles. By using `auto`, the {rosa-cli} generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
`Create the 'ManagedOpenShift-OCM-Role-182' role?`:: The `auto` method asks if you want to create a specific `ocm-role` by using your prefix.
`OCM Role ARN`:: Confirm that you want to associate your IAM role with your {cluster-manager}.
`Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'?`:: Links the created role with your AWS organization.
--

** To create an `ocm-role` IAM role with the minimum required privileges, run the following command:
+
[NOTE]
====
While the `no-console` profile offers the minimum permissions policy that can still create OpenShift Container Platform clusters, the permissions are insufficient if you want to use {cluster-manager-url} for cluster creation.
====
+
[source,terminal]
----
$ rosa create ocm-role --no-console
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
[id="rosa-hcp-aws-private-create-cluster_{context}"]
= Creating a private OpenShift Container Platform cluster using the ROSA CLI

[role="_abstract"]
You can create a private cluster with multiple availability zones (Multi-AZ) on OpenShift Container Platform using the ROSA command-line interface (CLI), `rosa`.

Creating a cluster with {hcp} can take around 10 minutes.

.Prerequisites

* You have available AWS service quotas.
* You have enabled the OpenShift Container Platform in the AWS Console.
* You have installed and configured the latest version of the ROSA CLI on your installation host.

.Procedure

. Create a VPC with at least one private subnet. Ensure that your machine's classless inter-domain routing (CIDR) matches your virtual private cloud's CIDR. For more information, see Requirements for using your VPC and VPC validation.
+
[IMPORTANT]
====
If you use a firewall, you must configure it so that ROSA can access the sites that required to function.

For more information, see the "AWS PrivateLink firewall prerequisites" section.
====

. Create the account-wide IAM roles by running the following command:
+
[source,terminal]
----
$ rosa create account-roles --hosted-cp
----

. Create the OIDC configuration by running the following command:
+
[source,terminal]
----
$ rosa create oidc-config --mode=auto --yes
----
+
Save the OIDC configuration ID because you need it to create the Operator roles.
+
.Example output
[source,terminal]
----
I: Setting up managed OIDC configuration
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 28s4avcdt2l318r1jbk3ifmimkurk384
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: Creating OIDC provider using 'arn:aws:iam::46545644412:user/user'
I: Created OIDC provider with ARN 'arn:aws:iam::46545644412:oidc-provider/oidc.op1.openshiftapps.com/28s4avcdt2l318r1jbk3ifmimkurk384'
----

. Create the Operator roles by running the following command:
+
[source,terminal]
----
$ rosa create operator-roles --hosted-cp --prefix <operator_roles_prefix> --oidc-config-id <oidc_config_id> --installer-role-arn arn:aws:iam::$<account_roles_prefix>:role/$<account_roles_prefix>-HCP-ROSA-Installer-Role
----

. Create a private OpenShift Container Platform cluster by running the following command:
+
[source,terminal]
----
$ rosa create cluster --private --cluster-name=<cluster-name> --sts --mode=auto --hosted-cp --operator-roles-prefix <operator_role_prefix> --oidc-config-id <oidc_config_id> [--machine-cidr=<VPC CIDR>/16] --subnet-ids=<private-subnet-id1>[,<private-subnet-id2>,<private-subnet-id3>]
----

. Enter the following command to check the status of your cluster. During cluster creation, the `State` field transitions from `pending` to `installing`, and finally, to `ready`.
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
[NOTE]
====
If installation fails or the `State` field does not change to `ready` after 10 minutes, see the "Troubleshooting Red{nbsp}Hat OpenShift Service on AWS installations" documentation in the Additional resources section.
====

. Enter the following command to follow the OpenShift installer logs to track the progress of your cluster:
+
[source,terminal]
----
$ rosa logs install --cluster=<cluster_name> --watch
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc

[id="rosa-hcp-aws-private-security-groups_{context}"]
= Adding additional AWS security groups to the AWS PrivateLink endpoint

[role="_abstract"]
The AWS PrivateLink endpoint in the host VPC has a default security group that restricts access to the cluster's Machine CIDR range. To grant API access from outside the VPC, you must create and attach an additional security group to the PrivateLink endpoint.

[IMPORTANT]
====
Adding additional AWS security groups to the AWS PrivateLink endpoint is only supported on OpenShift Container Platform version 4.17.2 and later.
====

.Prerequisites

* Your corporate network or other VPC has connectivity.
* You have permission to create and attach security groups within the VPC.

.Procedure

. Set your cluster name as an environmental variable by running the following command:
+
[source,terminal]
----
$ export CLUSTER_NAME=<cluster_name>
----
+
Verify that the variable exists by running the following command:
+
[source,terminal]
----
$ echo $CLUSTER_NAME
----
+
.Example output
[source,terminal]
----
hcp-private
----

. Find the VPC endpoint (VPCE) ID and VPC ID by running the following command:
+
[source,terminal]
----
$ read -r VPCE_ID VPC_ID <<< $(aws ec2 describe-vpc-endpoints --filters "Name=tag:api.openshift.com/id,Values=$(rosa describe cluster -c ${CLUSTER_NAME} -o yaml | grep '^id: ' | cut -d' ' -f2)" --query 'VpcEndpoints[].[VpcEndpointId,VpcId]' --output text)
----
+
[WARNING]
====
Modifying or removing the default AWS PrivateLink endpoint security group is not supported and might result in unexpected behavior.
====
+
. Create an additional security group by running the following command:
+
[source,terminal]
----
$ export SG_ID=$(aws ec2 create-security-group --description "Granting API access to ${CLUSTER_NAME} from outside of VPC" --group-name "${CLUSTER_NAME}-api-sg" --vpc-id $VPC_ID --output text)
----

. Add an inbound (ingress) rule to the security group by running the following command:
+
[source,terminal]
----
$ aws ec2 authorize-security-group-ingress --group-id $SG_ID --ip-permissions FromPort=443,ToPort=443,IpProtocol=tcp,IpRanges=[{CidrIp=<cidr-to-allow>}]
----

. Add the new security group to the VPCE by running the following command:
+
[source,terminal]
----
$ aws ec2 modify-vpc-endpoint --vpc-endpoint-id $VPCE_ID --add-security-group-ids $SG_ID
----
+
You can now access the API of your OpenShift Container Platform private cluster from the specified CIDR block.

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc

[id="rosa-additional-principals-overview_{context}"]
= Additional principals on your OpenShift Container Platform cluster

[role="_abstract"]
You can allow AWS Identity and Access Management (IAM) roles as additional principals to connect to your cluster's private API server endpoint.

You can access your OpenShift Container Platform cluster's API server endpoint from the public internet or the VPC private subnet interface endpoint. By default, you can privately access your OpenShift Container Platform API Server by using the `-kube-system-kube-controller-manager` Operator role. To access the OpenShift Container Platform API server from another account without using the primary account, include cross-account IAM roles as additional principals. This feature simplifies your network architecture and reduces data transfer costs. You can avoid peering or attaching cross-account VPCs to the cluster's VPC.

image::AWS_cross_account_access.png[Overview of AWS cross account access]

In this diagram, the cluster creating account is designated as Account A. This account designates that another account, Account B, should have access to the API server.

[NOTE]
====
After configuring additional allowed principals, create an interface VPC endpoint in the VPC that accesses the cross-account OpenShift Container Platform API server. Then, create a private hosted zone in Route53. Configure the hosted zone to route calls to the cross-account OpenShift Container Platform API server through the VPC endpoint.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc

[id="rosa-additional-principals-create_{context}"]
= Adding additional principals while creating your OpenShift Container Platform cluster

[role="_abstract"]
By default, only the IAM role that created the cluster can access the cluster's API. If other IAM roles in your AWS account need access to the cluster API, you can grant them access by specifying additional allowed principals during cluster creation.

.Procedure

. Add the `--additional-allowed-principals` argument to the `rosa create cluster` command, similar to the following:
+
[source,terminal]
----
$ rosa create cluster [...] --additional-allowed-principals <arn_string>
----
+
You can use `arn:aws:iam::account_id:role/role_name` to approve a specific role.

. When the cluster creation command runs, you receive a summary of your cluster with the `--additional-allowed-principals` specified:
+
.Example output
[source,terminal]
----
Name:                       mycluster
Domain Prefix:              mycluster
Display Name:               mycluster
ID:                         <cluster-id>
External ID:                <cluster-id>
Control Plane:              ROSA Service Hosted
OpenShift Version:          4.15.17
Channel Group:              stable
DNS:                        Not ready
AWS Account:                <aws_id>
AWS Billing Account:        <aws_id>
API URL:
Console URL:
Region:                     us-east-2
Availability:
 - Control Plane:           MultiAZ
 - Data Plane:              SingleAZ

Nodes:
 - Compute (desired):       2
 - Compute (current):       0
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            172.30.0.0/16
 - Machine CIDR:            10.0.0.0/16
 - Pod CIDR:                10.128.0.0/14
 - Host Prefix:             /23
 - Subnets:                 subnet-453e99d40, subnet-666847ce827
EC2 Metadata Http Tokens:   optional
Role (STS) ARN:             arn:aws:iam::<aws_id>:role/mycluster-HCP-ROSA-Installer-Role
Support Role ARN:           arn:aws:iam::<aws_id>:role/mycluster-HCP-ROSA-Support-Role
Instance IAM Roles:
 - Worker:                  arn:aws:iam::<aws_id>:role/mycluster-HCP-ROSA-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<aws_id>:role/mycluster-kube-system-control-plane-operator
 - arn:aws:iam::<aws_id>:role/mycluster-openshift-cloud-network-config-controller-cloud-creden
 - arn:aws:iam::<aws_id>:role/mycluster-openshift-image-registry-installer-cloud-credentials
 - arn:aws:iam::<aws_id>:role/mycluster-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<aws_id>:role/mycluster-openshift-cluster-csi-drivers-ebs-cloud-credentials
 - arn:aws:iam::<aws_id>:role/mycluster-kube-system-kms-provider
 - arn:aws:iam::<aws_id>:role/mycluster-kube-system-kube-controller-manager
 - arn:aws:iam::<aws_id>:role/mycluster-kube-system-capa-controller-manager
Managed Policies:           Yes
State:                      waiting (Waiting for user action)
Private:                    No
Delete Protection:          Disabled
Created:                    Jun 25 2024 13:36:37 UTC
User Workload Monitoring:   Enabled
Details Page:               https://console.redhat.com/openshift/details/s/Bvbok4O79q1Vg8
OIDC Endpoint URL:          https://oidc.op1.openshiftapps.com/vhufi5lap6vbl3jlq20e (Managed)
Audit Log Forwarding:       Disabled
External Authentication:    Disabled
Additional Principals:      arn:aws:iam::<aws_id>:role/additional-user-role
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc

[id="rosa-additional-principals-edit_{context}"]
= Adding additional principals to your existing OpenShift Container Platform cluster

[role="_abstract"]
If you did not specify additional allowed principals when you created your cluster, or if your access requirements have changed, you can add additional principals to an existing cluster by using the {rosa-cli-first}.

.Procedure

* Run the following command to edit your cluster and add an additional principal who can access this cluster's endpoint:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name> --additional-allowed-principals <arn_string>
----
+
You can use `arn:aws:iam::account_id:role/role_name` to approve a specific role.

.Next steps

* Configure an identity provider.

[role="_additional-resources"]
[id="additional-resources_rosa-hcp-aws-privatelink-creating-cluster"]
== Additional resources

* Configuring identity providers
* AWS PrivateLink firewall prerequisites
* Deleting a OpenShift Container Platform cluster
* OpenShift Container Platform architecture models
* Troubleshooting OpenShift Container Platform cluster installations
