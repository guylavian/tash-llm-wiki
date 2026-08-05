---
title: "[Migrated from MSDN Exchange Dev]Exchange Server: A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is 80."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167880/migrated-from-msdn-exchange-dev-exchange-server-a
question_id: 167880
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange Server: A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is 80.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167880/migrated-from-msdn-exchange-dev-exchange-server-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

I have a Server 2012 R2 with Exchange Server Standard installed. Its been working for 3 years without mayor issues, but a couple of months now I been experience a torrent of errors in the system logs file:   

A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is 80.  

I need some guidance to troubleshoot this. There is nothing in Google, Microsoft Forums that actually fix of help find the source of this issue.  

Most of the odd responses are: "Turn the alert off and the problem go away" scenario.  

But when I clear the log, it takes 10 seconds to register at least 50 entries.  

There is nothing there to help me even start looking for a solution.  

Anyone that successfully have a procedure to troubleshoot this?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

Hi ,    

Is there any problem during the use of Exchange?    

Did you change any setting for Exchange befor this error code occurred?    

According to my research, this is an error about Schannel. Schannel is a Security Support Provider (SSP) that implements the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) Internet standard authentication protocols. You can check whether TLS verification is enabled for the Exchange organization by verifying the headers of sent and received emails. I suggest you contact the network team to check whether the TLS settings are correct and whether the function of using the authentication protocol is affected    

Through the study of some similar cases, if the normal use of your Exchange is not affected, and all organizations that require TLS encryption, including Exchange, are operating normally. Then I think you can safely ignore these logs.    

In addition, is there have any more related event log in the Event Viewer? If so, please share it with us. Please note that please cover your personal information.    

There is a similar case you could refer to: A fatal alert was received from the remote endpoint. The TLS protocol defined fatal alert code is 80    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
