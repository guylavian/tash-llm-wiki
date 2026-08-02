---
title: "On premis Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361007/on-premis-exchange-2016
question_id: 361007
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# On premis Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361007/on-premis-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are using on premise Exchange 2016. We have an apps running in server A sending smtp email out to external email address such as gmail, hotmail, etc and Bcc to an outlook mail box.  

The user of the apps had sent email (around 400+) out but found that not all the emails are recv in the Bcc outlook mail box.  

How to find out what is the problem that causing those emails that not recv in Bcc mail box. Note that the mails were sent on 2 Apr, note sure the log still available to trace?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-17*

Hi @Leong Yew Cheong   ,    

You can use message tracking logs to track the emails. default retention for message tracking logs is 30 days.    

Also, if the emails are not received only the mailbox (BCC'ed) check for any outlook rules (mailbox rules) as well.    

https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/search-message-tracking-logs?view=exchserver-2016    

https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/configure-message-tracking?view=exchserver-2016    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
