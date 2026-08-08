---
title: "Exchange 2016 SPAM Filter 403 Error, even as Organization Management"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1414465/exchange-2016-spam-filter-403-error-even-as-organi
question_id: 1414465
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 SPAM Filter 403 Error, even as Organization Management

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1414465/exchange-2016-spam-filter-403-error-even-as-organi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 Exchange servers setup in DAG. This has been working perfectly for years, but recently I am unable to get into the SPAM Filter, I get a 403 Sorry! Access Denied :(

How can I fix this?

```
Version: Exchange 2016 CU23 Oct23SU
        Build Number: 15.01.2507.034
        Exchange IU or Security Hotfix Detected:
                Security Update for Exchange Server 2016 Cumulative Update 23 (KB5024296)
                Security Update for Exchange Server 2016 Cumulative Update 23 (KB5025903)
                Security Update for Exchange Server 2016 Cumulative Update 23 (KB5029388)
                Security Update for Exchange Server 2016 Cumulative Update 23 (KB5030524)
                Security Update for Exchange Server 2016 Cumulative Update 23 (KB5030877)
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-06*

Hi @Kevin Merritt,

Do you mean the "malware filter" page in Exchange Admin Center by "SPAM Filter"?

If yes, have you tried another administrator account which has organization management role assigned?

If it doesn't work for you either, please create a new role group, add "Security Admin" or "Transport Hygiene" role and add another user to this group, then check if this user can access this page.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
