---
title: "Exchange 2013 Logical corruption"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/243461/exchange-2013-logical-corruption
question_id: 243461
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 Logical corruption

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/243461/exchange-2013-logical-corruption (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have Exchange 2013 with 2 DB servers. we got logical corruption in DBs and almost 50 mailboxes are affected. so my question is how to recover from logical corruption as both server's DBs are have logical corruption.  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-26*

Hi @Sajid Ali Shah   ,    

I agree with above.    

In order to better solve this issue. If possiable, please share the issue phenomenon and error information with us. But pay attention to covering the personal information.    

Please try to create a new DB, then migrate user mailbox to the new DB and see if the issue has been resolved.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Agree with AndyDavid, i.e. how do you know you have logical corruption. More importantly have you tracked down cause?  If not you may end up repeating the corruption of new DB's  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-25*

How do you know have logical corruption? Whats the symptoms and errors you are seeing?  

Bring up new databases and move mailboxes to them. Thats the best thing to do if you have issues.
