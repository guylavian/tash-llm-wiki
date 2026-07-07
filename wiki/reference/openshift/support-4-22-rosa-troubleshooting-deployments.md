---
title: "Troubleshooting {product-title} cluster deployments"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-deployments
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-deployments
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting {product-title} cluster deployments

[id="rosa-troubleshooting-cluster-deployments"]
= Troubleshooting OpenShift Container Platform cluster deployments

[role="_abstract"]
Troubleshoot cluster deployment errors by completing the following instructions.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-general-deployment-failure_{context}"]
= Obtaining information about a failed cluster

[role="_abstract"]
If a cluster deployment fails, the cluster is put into an "error" state.

.Procedure

* Run the following command to get more information:
+
[source,terminal]
----
$ rosa describe cluster -c <my_cluster_name> --debug
----
// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-deployment-failure-osdccsadmin_{context}"]
= Troubleshooting cluster creation with an osdCcsAdmin error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message.

The following example shows the output:

[source,terminal]
----
Failed to create cluster: Unable to create cluster spec: Failed to get access keys for user 'osdCcsAdmin': NoSuchEntity: The user with name osdCcsAdmin cannot be found.
----

.Procedure

. Delete the stack:
+
[source,terminal]
----
$ rosa init --delete
----
+
. Reinitialize your account:
+
[source,terminal]
----
$ rosa init
----

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsnatgatewaylimitexceeded-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSNATGatewayLimitExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
Failed to create cluster: Error creating NAT Gateway: NatGatewayLimitExceeded: Performing this operation would exceed the limit of 5 NAT gateways.
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3019
Provisioning Error Message: NAT gateway limit exceeded. Clean unused NAT gateways or increase quota and try again.
----

This error indicates that you have reached the quota for the number of NAT gateways for that availability zone.

.Procedure

* To fix this issue, try one of the following methods:
** Request an increase in the **NAT gateways per Availability Zone quota** page by using the **Service Quotas** console (AWS).
** Check the status of your NAT gateway. A status of `Pending`, `Available`, or `Deleting` counts against your quota. If you have recently deleted a NAT gateway, wait a few minutes for the status to go from `Deleting` to `Deleted`. Then try creating a new NAT gateway.
** If you do not need your NAT gateway in a specific availability zone, try creating a NAT gateway in an availability zone where you have not reached your quota.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsapiratelimitexceeded-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSAPIRateLimitExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
level=error\nlevel=error msg=Error: error waiting for Route53 Hosted Zone .* creation: timeout while waiting for state to become 'INSYNC' (last state: 'PENDING', timeout: 15m0s)
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3008
Provisioning Error Message: AWS API rate limit exceeded. Please try again.
----

This error indicates that the AWS API rate limit has been exceeded while waiting for the Route 53 hosted zone.

.Procedure

* Reattempt the installation.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-s3bucketslimitexceeded_{context}"]
= Troubleshooting cluster creation with an S3BucketsLimitExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
level=error msg="Error: Error creating S3 bucket: TooManyBuckets: You have attempted to create more buckets than allowed"
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3014
Provisioning Error Message: S3 buckets limit exceeded. Clean unused S3 buckets or increase quota and try again.
----

This type of error indicates that you have reached the quota for the number of S3 buckets.

.Procedure

* To fix this issue, try one of the following methods:
+
** Request a quota increase from AWS:
.. Sign in to the AWS Management Console.
.. Click your user name and select **Service Quotas**.
.. Under **Manage quotas**, select an AWS service to view available quotas.
.. If the quota is adjustable, you can choose the button or the name, and then choose **Request quota increase**.
+
** Clean unused S3 buckets. You can only delete buckets that do not have any objects in them. Make sure the bucket is empty:
.. Sign in to the AWS Management Console.
.. Open the **Amazon S3** console.
.. In the **Buckets** list, select the option next to the name of the bucket that you want to delete, and then choose **Delete** at the top of the page.
.. On the **Delete bucket** page, confirm that you want to delete the bucket by entering the bucket name into the text field, and then choose **Delete bucket**.
+
[NOTE]
====
If you empty a bucket, this action cannot be undone.
====

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsvpclimit-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSVPCLimitExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message.

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3013
Provisioning Error Message: VPC limit exceeded. Clean unused VPCs or increase quota and try again.
----

This error indicates that you have reached the quota for the number of VPCs.

.Procedure

* To fix this issue, try one of the following methods:
+
* Request a quota increase from AWS:
.. Sign in to the AWS Management Console.
.. Click your user name and select **Service Quotas**.
.. Under **Manage quotas**, select a service to view available quotas.
.. If the quota is adjustable, you can choose the button or the name, and then choose **Request increase**.
.. For **Increase quota value**, enter the new value. The new value must be greater than the current value.
.. Choose **Request**.
+
* Clean unused VPCs. Before you can delete a VPC, you must first stop or delete any resources that created a requester-managed network interface in the VPC. For example, you must stop your EC2 instances and delete your load balancers, NAT gateways, transit gateways, and interface VPC endpoints before deleting a VPC:
.. Sign in to the AWS EC2 console.
.. Stop all instances in the VPC. For more information, see Stop Amazon EC2 instances.
.. Open the Amazon VPC console.
.. In the navigation pane, choose **Your VPCs**.
.. Select the VPC to delete and choose **Actions, Delete VPC**.
.. If you have a Site-to-Site VPN connection, select the option to delete it; otherwise, leave it unselected. Choose **Delete VPC**.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsinsufficientcapacity-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSInsufficientCapacity error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message:

[source,terminal]
----
Provisioning Error Code:    OCM3052
Provisioning Error Message: AWSInsufficientCapacity.
----

This error indicates that AWS has run out of capacity for a particular availability zone that you have requested.

.Procedure

* Try reinstalling or select a different AWS region or different availability zones.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-toomanyroute53zones-failure-deployment_{context}"]
= Troubleshooting cluster creation with a TooManyRoute53Zones error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
error msg=Error: error creating Route53 Hosted Zone: TooManyHostedZones: Limits Exceeded: MAX_HOSTED_ZONES_BY_OWNER - Cannot create more hosted zones.\\nlevel=error msg=\\tstatus code: 400
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3006
Provisioning Error Message: Zone limit exceeded
----

This error indicates the cluster installation was blocked as the installation program was unable to create a Route 53 hosted zone. A hosted zone is a container for records, and records contain information about how you want to route traffic for a specific domain, such as example.com, and its subdomains (acme.example.com, zenith.example.com).

The error suggests that the hosted zone quota is at capacity. By default, each Amazon Route 53 account is limited to a maximum of 500 hosted zones and 10,000 resource record sets per hosted zone.

.Procedure

* To fix this issue, try one of the following methods:
+
** Request a quota increase from AWS:
.. Sign in to the AWS Management Console.
.. Click your user name and select **Service Quotas**.
.. Under **Manage quotas**, select a service to view available quotas.
.. If the quota is adjustable, you can choose the button or the name, and then choose **Request increase**.
.. For **Increase quota value**, enter the new value. The new value must be greater than the current value.
.. Choose **Request**.
+
** Delete unused VPCs. Before you can delete a VPC, you must first stop or delete any resources that created a requester-managed network interface in the VPC. For example, you must stop your EC2 instances and delete your load balancers, NAT gateways, transit gateways, and interface VPC endpoints:
.. Sign in to the AWS EC2 console.
.. Stop all instances in the VPC. For more information, see Stop Amazon EC2 instances.
.. Open the Amazon VPC console.
.. In the navigation pane, choose **Your VPCs**.
.. Select the VPC to delete and choose **Actions, Delete VPC**.
.. If you have a Site-to-Site VPN connection, select the option to delete it; otherwise, leave it unselected. Choose **Delete VPC**.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awssubnetnotexist-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSSubnetDoesNotExist error

[role="_abstract"]
If a cluster creation action fails, you can receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
The subnet ID 'subnet-<somesubnetID>' does not exist.
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3032
Provisioning Error Message: You have specified an invalid subnet. Verify your subnet configuration is correct and try again.
----

This error indicates that the cluster installation is blocked by an invalid subnet selection error.

.Procedure

* Check your subnets provided in the `platform.aws.subnets` parameter during installation. The subnets must be a part of the same machine Network CIDR ranges that you specify.
** For a standard cluster, specify a public and a private subnet for each availability zone.
** For a private cluster, specify a private subnet for each availability zone.
+
For more information about AWS VPC and subnet requirements and optional parameters, see the _VPC_ section in the _AWS prerequisites for ROSA_ guide.

[role="_additional-resources"]
== Additional resources
* AWS prerequisites for OpenShift Container Platform

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-invalidkmskey-failure-deployment_{context}"]
= Troubleshooting cluster creation with an invalidKMSKey error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
Client.InvalidKMSKey.InvalidState: The KMS key provided is in an incorrect state
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3055
Provisioning Error Message: Invalid key.
----

This error indicates that the KMS key is invalid or the key is in an invalid state.

.Procedure

. Start by checking if EBS encryption is enabled in the EC2 settings. You can check the status by following the steps in AWS Check EBS Encryption.

. Check to see if the AWS specified key is enabled in there and not an `invalidKMSKey` that does not exist. This could happen when an old key was specified and deleted but EBS did not fall back to another key.

. If the previous two steps failed to fix the issue, disable EBS encryption entirely. If this is still a requirement you cannot disable, you can specify a customer-managed-key during ROSA install following the steps in Creating a ROSA cluster in STS mode with custom KMS key.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-multipleroute53zonesfound-failure-deployment_{context}"]
= Troubleshooting cluster creation with a MultipleRoute53ZonesFound error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message:

[source,terminal]
----
Provisioning Error Code:    OCM3049
Provisioning Error Message: DNS zone conflicts encountered.
----

The problem occurs because a previous cluster did not have had its Route 53 hosted zone removed during uninstallation. As a result, the existing Route 53 entries are conflicting with the cluster's DNS.

The cluster's installation is blocked because a duplicate Route 53 hosted zone already exists in your account.

.Procedure

. Verify the Route 53 configuration. If the hosted zone is no longer required, remove it.
. Attempt cluster installation again.
// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-invalidinstallconfigsubnet-failure-deployment_{context}"]
= Troubleshooting cluster creation with an InvalidInstallConfigSubnet error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error messages.

The following example shows the install logs output:

[source,terminal]
----
platform.aws.subnets[1]: Invalid value: "subnet-0babad72exxxxxxxx": subnet CIDR range start 10.69.1x.3x is outside of the specified machine networks
----

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3020
Provisioning Error Message: Subnet CIDR ranges are outside of specified machine CIDR.
----

These errors indicate that a subnet CIDR range start is outside of the specified machine networks.

.Procedure

. Check your subnet configuration.
. Edit your machine CIDR range to include all subnet CIDR ranges. Generally, your machine CIDR should match your VPC CIDR.
+
For more information about CIDR ranges, see _CIDR range definitions_ in the _Additional resources_ section .

[role="_additional-resources"]
== Additional resources
* CIDR range definitions

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsinsufficientpermission-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSInsufficientPermissions error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message.

The following example shows the {cluster-manager} output:

[source,terminal]
----
Provisioning Error Code:    OCM3033
Provisioning Error Message: Current credentials insufficient for performing cluster installation.
----

This error indicates that the cluster installation is blocked due to missing or insufficient privileges on the AWS account used to provision the cluster.

.Procedure

. Ensure that the prerequisites are met by reviewing _Detailed requirements for deploying ROSA (classic architecture) using STS_ or _Deploying ROSA without AWS STS_ in _Additional resources_ depending on your choice of credential mode for installing clusters.
+
[TIP]
====
[role="_abstract"]
AWS Security Token Service (STS) is the recommended credential mode for installing and interacting with clusters on OpenShift Container Platform because it provides enhanced security.
====
+
. If needed, you can re-create the permissions and policies by using the `-f` flag:
+
[source,terminal]
----
$ rosa create ocm-role -f
----
+
[source,terminal]
----
$ rosa create user-role -f
----
+
[source,terminal]
----
$ rosa create account-roles -f
----
+
[source,terminal]
----
$ rosa create operator-roles -c ${CLUSTER} -f
----

. Validate all the prerequisites and attempt cluster re-installation.

[role="_additional-resources"]
== Additional resources
* Detailed requirements for deploying OpenShift Container Platform using STS

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-deleteiamrole-deployment_{context}"]
= Troubleshooting cluster creation with a DeletingIAMRole error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message:

[source,terminal]
----
OCM3031: Error deleting IAM Role (role-name): DeleteConflict: Cannot delete entity, must detach all policies first.\nlevel=error msg=\tstatus code: 409
----

The cluster's installation was blocked as the cluster installer was not able to delete the roles it used during the installation.

.Procedure

* To unblock the cluster installation, ensure that no policies are added to new roles by default by running the following command to list all managed policies that are attached to the specified role:
+
[source,terminal]
----
$ aws iam list-attached-role-policies --role-name <role-name>
----
+
This command returns output similar to the following:
+
[source,terminal]
----
{
  "AttachedPolicies": [
    {
      "PolicyName": "SecurityAudit",
      "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit"
    }
  ],
  "IsTruncated": false
}
----
+
If there are no policies attached to the specified role (or none that match the specified path prefix), the command returns an empty list.
+
For more information about the list-attached-role-policies command, see list-attached-role-policies in the official AWS documentation.
// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-awsec2quotaexceeded-failure-deployment_{context}"]
= Troubleshooting cluster creation with an AWSEC2QuotaExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message.

The following example shows the output:

[source,terminal]
----
Provisioning Error Code:    OCM3042
Provisioning Error Message: AWS E2C quota limit exceeded. Clean unused load balancers or increase quota and try again.
----

This error indicates that you have reached the EC2 quota limit for the region mentioned in the error log.

.Procedure

* To fix this issue, try one of the following methods:
+
** Request a quota increase from AWS:
.. Sign in to the AWS Management Console.
.. Click your user name and select **Service Quotas**.
.. Under **Manage quotas**, select an AWS service to view available quotas.
.. If the quota is adjustable, you can choose the button or the name, and then choose **Request quota increase**.
+
** Delete unused EC2 instances using the console:
.. Before you delete an EC2 instance, verify your data by checking that your Amazon EBS volumes will still exist after you delete the unused EC2 instances.
.. Ensure you have copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.
.. If you have a CNAME record for your domain that points to your load balancer, point it to a new location and wait for the DNS change to take effect before deleting your load balancer.
.. Open the Amazon EC2 console.
.. On the navigation pane, choose **Instances**.
.. Select the instance, and choose **Stop instance**.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-pendingverification-failure-deployment_{context}"]
= Troubleshooting cluster creation with a PendingVerification error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message.

The following example shows the output:

[source,terminal]
----
Provisioning Error Code:    OCM3021
Provisioning Error Message: Account pending verification for region. Verify the account and try again.
----

When creating a cluster, the OpenShift Container Platform service creates small instances in all supported regions. This check ensures the AWS account being used can deploy to each supported region.

For AWS accounts that are not using all supported regions, AWS might send one or more emails confirming that "Your Request For Accessing AWS Resources Has Been Validated". Typically the sender of this email is aws-verification@amazon.com. This is expected behavior as the OpenShift Container Platform service is validating your AWS account configuration.

Normally, this validation gets completed within 15 minutes, but in some cases it can take up to 4 hours for AWS to validate. To attempt successful provisioning, Red{nbsp}Hat has configured our installer to reattempt installation if this issue occurs, but the installation can still fail if the validation continues to time out or if the validation itself fails.

.Procedure
* Reinstall the cluster or select a different AWS region or different availability zone(s).

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-lblimitexceeded-failure-deployment_{context}"]
= Troubleshooting cluster creation with an ALoadBalancerLimitExceeded error

[role="_abstract"]
If a cluster creation action fails, you might receive the following error message:

[source,terminal]
----
Provisioning Error Code:    OCM3036
Provisioning Error Message: AWS Load Balancer quota limit exceeded. Clean unused load balancers or increase quota and try again.
----

This error indicates that you have reached the quota for the number of load balancers.

.Procedure

* To fix this issue, try one of the following methods:
+
** Request a quota increase from AWS:
.. Sign in to the AWS Management Console.
.. Click your user name and select **Service Quotas**.
.. Under **Manage quotas**, select a service to view available quotas.
.. If the quota is adjustable, you can choose the button or the name, and then choose Request quota increase.
.. For **Change quota value**, enter the new value. The new value must be greater than the current value.
.. Choose **Request**.
+
** Delete a load balancer using the console:
.. If you have a CNAME record for your domain that points to your load balancer, point it to a new location and wait for the DNS change to take effect before deleting your load balancer.
.. Open the Amazon EC2 console.
.. On the navigation pane, under **LOAD BALANCING**, choose **Load Balancers**.
.. Select the load balancer, and then choose **Actions, Delete**.
.. When prompted for confirmation, choose **Yes, Delete**.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-elb-service-role_{context}"]
= Creating the Elastic Load Balancing (ELB) service-linked role

[role="_abstract"]
If you have not created a load balancer in your AWS account, it is possible that the service-linked role for Elastic Load Balancing (ELB) might not exist yet. You might receive the following error:

[source,terminal]
----
Error: Error creating network Load Balancer: AccessDenied: User: arn:aws:sts::xxxxxxxxxxxx:assumed-role/ManagedOpenShift-Installer-Role/xxxxxxxxxxxxxxxxxxx is not authorized to perform: iam:CreateServiceLinkedRole on resource: arn:aws:iam::xxxxxxxxxxxx:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"
----

.Procedure

* To resolve this issue, ensure that the role exists on your AWS account. If not, create this role with the following command:
+
[source,terminal]
----
aws iam get-role --role-name "AWSServiceRoleForElasticLoadBalancing" || aws iam create-service-linked-role --aws-service-name "elasticloadbalancing.amazonaws.com"
----
+
[NOTE]
====
This command only needs to be executed once per account.
====
// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-cluster-deletion_{context}"]
= Repairing a cluster that cannot be deleted

[role="_abstract"]
In specific cases, the following error is displayed in {cluster-manager-url} if you attempt to delete your cluster:

[source,terminal]
----
Error deleting cluster
CLUSTERS-MGMT-400: Failed to delete cluster <hash>: sts_user_role is not linked to your account. sts_ocm_role is linked to your organization <org number> which requires sts_user_role to be linked to your Red Hat account <account ID>.Please create a user role and link it to the account: User Account <account ID> is not authorized to perform STS cluster operations

Operation ID: b0572d6e-fe54-499b-8c97-46bf6890011c
----

If you try to delete your cluster from the CLI, the following error is displayed:

[source,terminal]
----
E: Failed to delete cluster <hash>: sts_user_role is not linked to your account. sts_ocm_role is linked to your organization <org_number> which requires sts_user_role to be linked to your Red Hat account <account_id>.Please create a user role and link it to the account: User Account <account ID> is not authorized to perform STS cluster operations
----

This error occurs when the `user-role` is unlinked or deleted.

.Procedure

. Run the following command to create the `user-role` IAM resource:
+
[source,terminal]
----
$ rosa create user-role
----
+
. After you see that the role has been created, you can delete the cluster. The following confirms that the role was created and linked:
+
[source,terminal]
----
I: Successfully linked role ARN <user role ARN> with account <account ID>
----
