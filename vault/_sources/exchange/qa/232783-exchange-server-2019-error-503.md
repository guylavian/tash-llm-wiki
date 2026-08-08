---
title: "Exchange Server 2019 Error 503"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/232783/exchange-server-2019-error-503
question_id: 232783
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2019 Error 503

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/232783/exchange-server-2019-error-503 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had an Exchange Server 2019 that stopped working (no secondary servers - this one was stand-alone) and ended up re-installing the OS and ES but could never get the ES setup to complete. Renamed the server and started over. ES installed but would not complete the AD portion and when we try to access ecp or owa we get HTTP Error 503. The service is unavailable. Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

-  Have you health checked AD?  If not that's where I would start  

-  If AD is healthy, have you checked the system and application event logs on the Exchange server for critical and error events?  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Hi,    

Please check:    

-  the clock on Exchange server is correct.    

-  negative to IIS manager-Exchange Backend website -bindings, check if correct certificate is selected:    

     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
