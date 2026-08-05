---
title: "ADFS 2019 Access control Policy - Permit from specific domain name"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195271/adfs-2019-access-control-policy-permit-from-specif
question_id: 1195271
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 2019 Access control Policy - Permit from specific domain name

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195271/adfs-2019-access-control-policy-permit-from-specif (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

User login to ADF using DomainA\UserID. I want to only allow users from DomainA login and get a claim using Access Control Policy. 

What will be correct REgEx to match user login with DomainA and deny other domains? I Can do with UPN with UPN contain @domaina.com

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2023-04-01*

To create a rule to permit users from “DomainA” but deny all other domains in ADFS 2019 Access control Policy, you can use regular expressions as follows:

-  Open AD FS Management, click Access Control Policies > Action > Add Access Control Policy.

-  In the name box, enter a name for your policy, a description and click Add.

-  Under Permit access if any of the following rules are met, click Add.

-  In the Claim rule template drop-down list, select Send Claims Using a Custom Rule. See Figure 1.

Figure 1. What the interface looks like up too this point.

-  In the Custom rule box, enter the following regular expression:

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Value =~ "(?i)^DomainA\\.*"]
```

-  Under Deny access if any of the following rules are met, click Add.

-  In the Claim rule template drop-down list, select Send Claims Using a Custom Rule.

-  In the Custom rule box, enter the following regular expression:

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Value =~ "(?i)^(?!DomainA\\).*"]
```

-  Click OK to save your policy

Please let us know if it works!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-01*

Actually, I dont option to select custom rule template. can you send screenshot?

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-01*

Perfect!

Thanks
