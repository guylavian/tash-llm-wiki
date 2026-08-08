---
title: "Exchange 2019 Admin Role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/364247/exchange-2019-admin-role
question_id: 364247
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 Admin Role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/364247/exchange-2019-admin-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I need to create an admin user in Exchange Server 2019, but that admin will have no permission to do delivery reports view/track, I've removed the message tracking role from the assigned role in admin roles, but the new admin still able to view mail flow>delivery reports in Exchange Admin Center, now the question is how to properly to limit an admin to not to be able to do delivery reports view? Thanks in advance

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-20*

```
Remove-ManagementRoleEntry "CustomAdminRole\Search-MessageTrackingReport"
```

In EAC, you probably can't remove that ability to view however. The question is can they still run it? If you removed MessageTracking role, then they should not be able to
