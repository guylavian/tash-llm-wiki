---
title: "Exchange error | X-MS-ASError: Message = Element 'Calendar::Categories'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/247541/exchange-error-x-ms-aserror-message-element-calend
question_id: 247541
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange error | X-MS-ASError: Message = Element 'Calendar::Categories'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/247541/exchange-error-x-ms-aserror-message-element-calend (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear readers, what does the following error mean? I am trying to sync calendar items with an android phone with the Samsung mail client but that fails.   

We are running Exchange 2016 Cu11 (yes and old one)   

http://interoperability.blob.core.windows.net/files/MS-ASCAL/%5BMS-ASCAL%5D.pdf  

In here, page 24 section 2.2.2.11 it describes what it is but not how to solve it.   

ResponseHeader :   

HTTP/1.1 200 OK  

MS-Server-ActiveSync: 15.1  

X-MS-ASError: Message = Element 'Calendar::Categories' cannot appear more than once if content model type is "all".; Severity = Error  

ResponseBody :   

<?xml version="1.0" encoding="utf-8" ?>  

<Sync xmlns="AirSync:">  

<Status>4</Status>  

</Sync>  

ResponseTime :   

01/27/2021 11:45:08

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-18*

Well, after lots and lots of research we found the solution. It turned out that the firewall was set a bit strict, after loosening it up everything went much smoother.     

@Anonymous   your answer helped us a lot!
