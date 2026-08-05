---
title: "Exchange Server 2010 mail deliver issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/231334/exchange-server-2010-mail-deliver-issue
question_id: 231334
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2010 mail deliver issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/231334/exchange-server-2010-mail-deliver-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, All  

We regularly send emails with the same title and the same content. This mail contains a schedule. However, at some point, there has been a phenomenon in which a large number of recipients do not receive emails.  

In CAS, 61 recipients are identified, and the actual number of people who received is only 14. Therefore, sending and receiving the same mail directly to one person who did not receive the mail is normal.  

Plus, one of person claims that he accepted schedule but schedule is not registered into his outlook.  

What should we check?  

Thanx

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Hi @Anonymous      

What's the UR version of your Exchange 2010?  What changes have been made recently on your server?    

Have you checked the message tracking log for the message? Is this an internal message or a relay message which occurs the issue?    

Did you receive any NDR message when failing sending it?    

In addition, Exchange 2010 has ended support, it's better to migrate to Exchange 2016/2019 or O365 to get better support. Detailed information here: Exchange 2010 end of support roadmap    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
