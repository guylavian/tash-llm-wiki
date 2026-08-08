---
title: "how to set password lifetime to exchange users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159868/how-to-set-password-lifetime-to-exchange-users
question_id: 1159868
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# how to set password lifetime to exchange users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159868/how-to-set-password-lifetime-to-exchange-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

How to set password lifetime for exchange server 2016 users?

Brgds

Liu Wei

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-12*

Hi @liuwei@cesm  

Since Exchange integrates with Active Directory (to login Exchange mailboxes users are using the credentials in AD), this setting is controlled by AD.

You can configure the password expiration time for users in AD, which may also work for Exchange.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-11*

This is done through the Microsoft 365 admin center, Settings > Org settings > Security & privacy > Password expiration policy.  You will require either the Global Administrator or Security Administrator role to see/access this setting.

Please accept as an answer if this was helpful.
