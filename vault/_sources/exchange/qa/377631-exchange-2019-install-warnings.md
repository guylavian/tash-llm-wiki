---
title: "Exchange 2019 install warnings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/377631/exchange-2019-install-warnings
question_id: 377631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 install warnings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/377631/exchange-2019-install-warnings (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

We have encountered 2 warnings in the process of installing Exchange server 2019.  

-  Setup will prepare the org for Exchange Server 2019 by using ( command). No Exchange server 2016 roles have been detected. After this operation no exchange 2016 roles will be able to be installed. We currently have exchange 2013, and after the install I just want to migrate the mailboxes to the new 2019 exchange server. I'm planning to just skip over 2016 altogether. Will this warning cause me issues when trying to move the mailboxes?

2) MAPI over HTTP, the preferred outlook desktop client connectivity with exchange, is currently not enabled. Consider enabling it using: (command)  

Where do I enable this and can I do it after the install?

Thanks for the helps.  

B

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-29*

1) No, that just is telling you that since you have no 2016 servers, you cant install any later. Your existing 2013 servers will be fine!  

2) Yes, you can: https://learn.microsoft.com/en-us/exchange/clients/mapi-over-http/configure-mapi-over-http?view=exchserver-2019
