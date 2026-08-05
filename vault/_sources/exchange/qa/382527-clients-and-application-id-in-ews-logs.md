---
title: "clients and application ID in EWS logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/382527/clients-and-application-id-in-ews-logs
question_id: 382527
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# clients and application ID in EWS logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/382527/clients-and-application-id-in-ews-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I need to get a list of clients and application IDs that are using EWS on an on premise Exchange server?  

What should be looked at in the EWS logs?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-04*

I would use Ingo's blog:    

https://ingogegenwarth.wordpress.com/2017/01/12/troubleshooting-exchange-with-logparser-ews-logs/    

You can also look in the IIS logs and see which clients are accessing the EWS virtual directory    

https://learn.microsoft.com/en-us/exchange/iis-logs-and-log-parser-studio-reports-exchange-2013-help
