---
title: "Exchange 2016 keep hung up"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/180503/exchange-2016-keep-hung-up
question_id: 180503
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 keep hung up

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/180503/exchange-2016-keep-hung-up (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have an Exchange 2016 server on premise (on Hyper-V) that keep hung up once a week or so.  Users can't send or receive emails when that happened; we can still ping the server ip address, but we can't connect via the Hyper-V Manager, RDS, or Teamviewer although it's shown running on the Hyper-V Manager.   We have to restart the Exchange server from Hyper-V in order for users to be able to send and receive mails again.  

Is there anywhere in a log or event log that we can take a look to see what the problem would be?  

Your comments or advices will be greatly appreciated.  

Tee

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-03*

Hi all,  

There are so many errors and warnings in the event log, and most of those I don't know what that were.  I will need to do some more error lookups.  

Anyway,  I have seen the CPU and Memory usages were high in the upper 90's and sometime reached 100.   I have increased more memory and CPU to the Exchange server and it seems to be stable since.  I checked the event log afterward and didn't see any more warning or error.  

Thanks everyone again for all  your help.  

Tee

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

Thank you guys,  I will try your suggestions.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-01*

Hi @Tee356       

I agree with the suggestions above, we could check the application log for both VM and your Exchange server. In addition, the official document introduces about Exchange Server virtualization, we can mainly refer to the part Exchange memory requirements and recommendations:    

Exchange (like many server applications with optimizations for performance that involve caching of data in memory) is susceptible to poor system performance and an unacceptable client experience if it doesn't have full control over the memory allocated to the physical or virtual machine on which it's running. As a result, using dynamic memory or memory overcommit features for Exchange isn't supported.    

Keep us updated if any news comes up.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
