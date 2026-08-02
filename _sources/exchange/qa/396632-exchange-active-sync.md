---
title: "Exchange Active Sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/396632/exchange-active-sync
question_id: 396632
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Active Sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/396632/exchange-active-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've configured any URLs which Exchange needed.    

I don't have any problem with Certificate and DNS Resolving.    

I can access my emails through of outlook and owa.    

but i can't access my email account with any mobile devices.    

I set rules for all outlook and mobile devices and set allow all of them. actually  I check ActiveSync Health and there is no special thing to say.it was healthy.I check specific user   CASMailbox and it was true.    

is there anyone who can guide me?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hi,    

You can Use Test-ActiveSyncConnectivity to Verify Exchange ActiveSync or Use EXRCA to simulate an Exchange ActiveSync connection from a mobile device to a mailbox, if it works, you could read below articles.     

For Android devices, follow the guidance here.    

For IOS devices, see here.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
