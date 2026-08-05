---
title: "Exchange Hybrid Cross Forest Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1291367/exchange-hybrid-cross-forest-migration
question_id: 1291367
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid Cross Forest Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1291367/exchange-hybrid-cross-forest-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently we have single forest with exchange hybrid environment. Recently, the company has done the rebranding. and would like to migrate all users from Forest A to Forest B.

I know I can use the ADMT tool to migrate the user account and computer account. but I have some confusion.

how we can configure the exchange hybrid with new tenant. if it is already configured with Forest A.

how we can maintain the domanA.com & domainB.com email address in both forest.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-26*

Hello @Mohammed Gayasuddin !

For the Outlook Part users have to create new Profiles

 I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-26*

Hi @Mohammed Gayasuddin,

how we can configure the exchange hybrid with new tenant. if it is already configured with Forest A.

Hybrid deployments with multiple forests is supported.

Please refer to this link for more information: Hybrid deployments with multiple forests

how we can maintain the domanA.com & domainB.com email address in both forest.

You can add another domain as an accept domain (internal relay domain) on your Exchange server.

Then create email address policies and assign the policy to the mailboxes which need to use another domain as their email address domain suffix.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
