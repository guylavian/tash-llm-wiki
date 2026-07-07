---
title: "Adding additional constraints for IP-based AWS role assumption"
type: reference
domain: openshift
slug: security-4-22-rosa-adding-additional-constraints-for-ip-based-aws-role-assumption
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/rosa-adding-additional-constraints-for-ip-based-aws-role-assumption
version: 4.22
family: security
documentKind: "Documentation"
---

# Adding additional constraints for IP-based AWS role assumption

[id="rosa-adding-additional-constraints-for-ip-based-aws-role-assumption"]
= Adding additional constraints for IP-based AWS role assumption

[role="_abstract"]
Create an identity-based policy that denies requests from non-allowlisted IP addresses. Restricting role access can improve your AWS account security.

// Module included in the following assemblies:
//
// * rosa-adding-additional-constraints-for-ip-based-aws-role-assumption/rosa-create-an-identity-based-policy.adoc
[id="rosa-create-an-identity-based-policy_{context}"]
= Creating an identity-based IAM policy

[role="_abstract"]
Create an Identity and Access Management (IAM) policy that denies access to all AWS actions if the request is made from an IP address not provided by Red{nbsp}Hat.

.Prerequisites

* You have access to the AWS Management Console with the permissions required to create and modify IAM policies.

.Procedure

. Sign in to the AWS Management Console using your AWS account credentials.
. Navigate to the IAM service.
. In the IAM console, select *Policies* from the left navigation menu.
. Click *Create policy*.
. Select the *JSON* tab to define the policy using JSON format.
. To get the IP addresses required for the JSON policy document, run the following command:
+
[source,terminal]
----
$ ocm get /api/clusters_mgmt/v1/trusted_ip_addresses
----
+
[NOTE]
====
These IP addresses are not permanent and can change. Regularly review the API output and update the JSON policy document.
====
+
. Copy and paste the following `policy_document.json` file into the editor:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": []
                },
                "Bool": {
                    "aws:ViaAWSService": "false"
                }
            }
        }
    ]
}
----
+
. Copy and paste all of the IP addresses, which you got in Step 6, into the `"aws:SourceIp": []` array in your `policy_document.json` file.
. Click *Review and create*.
. Provide a name and description for the policy, and review the details for accuracy.
. Click *Create policy* to save the policy.
+
[NOTE]
====
Set the `aws:ViaAWSService` condition key to false to ensure that subsequent calls succeed after your initial call. For example, if you do not set `aws:ViaAWSService` to false and run `aws ec2 describe-instances`, some follow-up calls can fail. It applies to subsequent calls that you make within the AWS API server to retrieve information about the Elastic Block Store (EBS) volumes attached to the EC2 instance. The subsequent calls fail because they originate from AWS IP addresses that are not included in the AllowList.
====

// Module included in the following assemblies:
//
// * rosa-adding-additional-constraints-for-ip-based-aws-role-assumption/rosa-attaching-the-policy.adoc
[id="rosa-attaching-the-policy_{context}"]
= Attaching the identity-based IAM policy

[role="_abstract"]
After you create an Identity and Access Management (IAM) policy, attach it to the relevant IAM users, groups, or roles in your AWS account. The policy prevents IP-based role assumption for these entities.

.Procedure

. Navigate to the IAM console in the AWS Management Console.
. Select the default IAM `ManagedOpenShift-Support-Role` role to attach the policy.
+
[NOTE]
====
You can change the default IAM `ManagedOpenShift-Support-Role` role. For more information about roles, see Red{nbsp}Hat support access.
====
+
. In the *Permissions* tab, select *Add Permissions* or *Create inline policy* from the *Add Permissions* drop-down list.
. Search for the policy you created earlier by:
.. Entering the policy name.
.. Filtering by the appropriate category.
. Select the policy and click *Attach policy*.
+
[IMPORTANT]
====
To prevent IP-based role assumption, keep the allowlisted IPs up-to-date. Outdated IPs can block Red{nbsp}Hat site reliability engineering (SRE) from accessing your account and affect your Service Level Agreement (SLA).
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* AWS: Denies access to AWS based on the source IP
