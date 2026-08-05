---
title: "Track a message location in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/241757/track-a-message-location-in-exchange-online
question_id: 241757
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Track a message location in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/241757/track-a-message-location-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,  

I'm looking for a method to track an email (based on its message ID for example) to the folder it is currently residing in a users mailbox. I am aware I can use the compliance centre to do this and download the PST results to see the folder structure but I'm looking for a way where I wouldn't be exposed to the content of the message.  

I came across the following PowerShell command but this looks to be depreciated:  

Search-Mailbox -identity "User alias" -SearchQuery "Search criteria" -TargetMailbox "Admin Email" - TargetFolder "Inbox" -LogOnly -LogLevelFull  

Is there an equivalent for the replacement command New-ComplianceSearch?  

Thanks,

## Answers

_No answers on this thread._
