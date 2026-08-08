---
title: "Exchange 2016 TransportAgent; message deleted by transport agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/389033/exchange-2016-transportagent-message-deleted-by-tr
question_id: 389033
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 TransportAgent; message deleted by transport agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/389033/exchange-2016-transportagent-message-deleted-by-tr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have exchange 2016 CU20.  

There are some mails with:  

Source                  : AGENT  

EventId                 : DROP  

RecipientStatus         : {[{LED=550 4.3.2 QUEUE.TransportAgent; message deleted by transport agent};{MSG=};{FQDN=};{IP=};{LRT=}]}  

How do I trace, what agent and what is the reason of eventid DROP.  (Exch 2016 doesn't have message trace in EOP)   

Thank you in advance

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-12*

Get-MessageTrackingLog -EventID Drop -MessageSubject "Subject" -Sender sender@keyman  .com -recipients Recipient@keyman  .com | FL    

SourceContext           : ScanMail Routing Agent   <-----  I really don't know how I missed it.  It is antivirus software.     

ConnectorId             :    

Source                  : AGENT    

EventId                 : DROP    

Thank you for response.
