---
title: "Configure User provisioning from Active Directory to SAP Identity Services and S4hana"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1442024/configure-user-provisioning-from-active-directory
question_id: 1442024
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Configure User provisioning from Active Directory to SAP Identity Services and S4hana

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1442024/configure-user-provisioning-from-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,

I'm trying to configure user provisioning in SAP IPS having source as MS Active Directory and Target as IAS and S4hana. The main objective of my project is to provision only specific members/users  of  different groups required for S4hana business, like HR group/PO Approvers etc.

The main problem I'm facing that while running the IPS job all users from entire Active directly is getting synced and not the specific members of the desired groups.

Could you please help me find the correct properties/attributes that I should be using in SAP IPS source system for Active Directory to filter only the users of specific groups and not all users. Currently I've used several properties to fetch users from groups for example like "ldap.group.filter", "ldap.attribute.dn", "ldap.user.filter" etc but none working as desired.

I have raised concern with SAP as well, but they  are saying that have no knowledge of the exact attributes to use from AD to SAP IPS to provision the specific members of any groups.

Appreciate your response on this issue.

Thanks & Regards,

Anwar

## Answers

_No answers on this thread._
