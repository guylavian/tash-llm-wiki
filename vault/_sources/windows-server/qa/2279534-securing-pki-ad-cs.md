---
title: "Securing PKI (AD CS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2279534/securing-pki-ad-cs
question_id: 2279534
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# Securing PKI (AD CS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2279534/securing-pki-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I was reading an old document about Securing PKI

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786443(v=ws.11)

as well as the built-in security group Cert Publishers

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#cert-publishers

But I do not find details on the actual RBAC model and who can do what or how to delegate specific things.

For example, a certificate template is marked as "Issuance Requirements / CA certificate manager approval":

-  What is the actual role, or least privilege role, needed for that?

-  Can it be delegated?

Thank you!

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-29*

Hello TheNewGuy-0614,

   Thank you for posting question on Microsoft Windows forum!

   Based on your query of proper RBAC model for ADCS, The followings are some key aspects of RBAC model for your reference.

-  Define Roles and Permissions:

-  Identify the various roles involved in PKI management, such as Certificate Authority administrators, enrollment agents, and certificate users. Like below examples.

-  Certificate Authority Administrator -> Permissions to manage CA settings, issue certificates, revoke certificates, and manage templates. 

-  Enrollment Agent -> Permissions to register users and computers for certificate enrollment. 

-  Certificate User -> Permissions to enroll for and use certificates.

2.Assign Roles to Groups:

-  Assign roles to groups, not individual users, to streamline administration and ensure consistent permissions across multiple users. 

-  Create an "Enrollment Agents" group and grant them the necessary permissions to enroll users for certificates.

3.Implement Least Privilege:

-  Ensure that each role has only the minimum necessary permissions to perform their tasks. 

-  Avoid granting "Domain Admin" access to users who only need to manage certificates. 

4.Regularly Review and Update:

-  Periodically review and update the RBAC model to ensure it aligns with the organization's evolving security needs and regulatory requirements. 

-  Regularly audit user access and remove unnecessary permissions.

You can refer to the following useful articles for the best practice of RBAC as well as Delegating Active Directory PKI Permissions.

-  https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn786430(v=ws.11)

-  https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices

-  https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-least-privilege-administrative-models

Hope the above information is helpful!
