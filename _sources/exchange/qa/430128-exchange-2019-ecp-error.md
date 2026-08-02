---
title: "Exchange 2019 ECP error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430128/exchange-2019-ecp-error
question_id: 430128
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 ECP error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430128/exchange-2019-ecp-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I've been running Exchange 2019 for 6 months with no issues, but since the beginning of the week I have noticed that when I access ECP via my browser I receive the following error:    

"error - Your request couldn't be completed. Please try again in a few moments"    

The ECP opens up on the recipients/mailboxes area by default and the mailbox highlighted generates the error. Clicking OK only just generates the error again.    

Upon further investigation, I have found that this effects the following browsers - Edge (my default), Chrome and Firefox.    

The ECP is only useable via Internet Explorer    

The URL I use to access ECP is:    

https://mail.company.com/ecp/?ExchClientVer=15.2    

There have been no updates installed on any of the Exchange servers since the last CU ( Exchange CU9) and round of server 2019 updates were installed a couple of months ago.    

All Exchange servers have been restarted and the issue persists.    

The below error is generated on any of the servers when accessing ECP:    

    

Anyone experiencing the same behaviour or have seen this before?    

Thanks in advance

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-06-21*

Hi, Apologies for the late reply.  

I discovered last week after further testing that this issue is related to an extension that I use across all browsers.  

I have reported the issue to the developers of the application.  

Thanks
