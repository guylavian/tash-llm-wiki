---
title: "exchange service administrator and company adminstrator in ExO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1499381/exchange-service-administrator-and-company-adminst
question_id: 1499381
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange service administrator and company adminstrator in ExO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1499381/exchange-service-administrator-and-company-adminst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are doing a review of admin role and assignments in AAD/Entra and the major 365 apps such as Exchange Online (ExO). Under the 'organization management' role in ExO – there are x2 groups listed: 'exchange service administrator' and 'company administrator'. However, we are struggling to find where these groups are actually established to determine membership, as there are no obvious groups in either AAD/Entra or ExO that match the names. So I am wondering if they are some sort of security principle in Entra/ExO/365 whereby other roles and members naturally become members of these ‘groups’ in ExO and therefore get Organization Management in ExO, or if this is some sort of default configuration when a new tenant is created/ExO is initially setup? I basically need to know who is a ‘member’ of these groups and where this could be viewed & evidenced?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-01-18*

Yes, Company Admin = Global Admin:
https://office365itpros.com/2019/07/08/new-roles-page-office-365-admin-center/

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-18*

Thanks Andy, I understand the 2nd section around who gets organisation management permissions via exchange service admins/exchange admin.
Re company administrator role & membership- there isn't actually a visible admin role in Entra called company administrator, so presumably all we need to check is global admins for that side of the equation.
