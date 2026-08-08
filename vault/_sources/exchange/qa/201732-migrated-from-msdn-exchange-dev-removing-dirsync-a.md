---
title: "[Migrated from MSDN Exchange Dev] Removing Dirsync and Last On-Premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/201732/migrated-from-msdn-exchange-dev-removing-dirsync-a
question_id: 201732
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# [Migrated from MSDN Exchange Dev] Removing Dirsync and Last On-Premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/201732/migrated-from-msdn-exchange-dev-removing-dirsync-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to get an answer to my theory in my head how to remove last exchange in a hybrid setup.  

Currently in hybrid with dirsync & Exchange 2010  

I know you can't remove remove last exchange and keep dirsync.  

My question is, Can i remove the dirsync then remove last exchange and about a month later enable the dirsync without needing the exchange?  

Does it still cause the need for ADSIEdit ?  

I can't find any information on this way  

Source Link: https://social.msdn.microsoft.com/Forums/office/en-US/19390c05-c38c-4edc-b578-2a823f2a8b74/removing-dirsync-and-last-onpremise?forum=exchangesvrdevelopment

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-17*

Answered already in:    

https://learn.microsoft.com/en-us/answers/questions/200772/removing-dirsync-and-last-exchange.html

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

The Scenario one is suitable one for you, you could disable the directory synchronization(Step 7) after checking on your Exchange server.     

Then you could uninstall AAD connect and Exchange on-premises.
