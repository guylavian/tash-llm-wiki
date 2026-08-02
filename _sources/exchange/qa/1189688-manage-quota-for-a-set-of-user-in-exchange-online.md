---
title: "Manage quota for a set of user in exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189688/manage-quota-for-a-set-of-user-in-exchange-online
question_id: 1189688
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Manage quota for a set of user in exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189688/manage-quota-for-a-set-of-user-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello , 

I was wondering if someone could answer me this question .  With exchange online is there a way to manage quota for a set of users .   

We have set the default quota size for our exchange plan 2 to something smaller then what Microsoft provide use .  which work great but we expect some users / department  that will require more soon .   We wish to group these user quota groups .   So we don’t have to manually manage every users individually and keep the setting consistent base on the groups needs .  Basically tiered mail quotas for a better lack of a term 

 On-prem we would setup special mailstore with default quota setting and place all these user on that mail store. Can anyone suggest how we can have tiered mail quota in exchange online ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-15*

Unfortunately, no. The only set of controls you have are on the plan level, and will apply to any newly provisioned mailbox using said plan. You will have to manually adjust it on a per user-basis. If you want to leverage a group, you can add all required users/mailboxes as members and expand the membership:

`Get-DistributionGroupMember groupname | Set-Mailbox -IssueWarningQuota 9GB -ProhibitSendQuota 10GB -ProhibitSendReceiveQuota 11GB` 

You will still need to run this periodically as users are added/removed from the group.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-15*

Did you check this article - https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/increase-or-customize-mailbox-size?source=recommendations
