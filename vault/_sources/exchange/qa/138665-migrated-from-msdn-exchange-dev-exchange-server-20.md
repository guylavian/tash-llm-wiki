---
title: "[Migrated from MSDN Exchange Dev]exchange server 2016 do not send email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138665/migrated-from-msdn-exchange-dev-exchange-server-20
question_id: 138665
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]exchange server 2016 do not send email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138665/migrated-from-msdn-exchange-dev-exchange-server-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi   

Until yesterday, the email server used to send emails everywhere, but now it does not send emails anywhere except to itself. I checked everything that was on the Internet, including the sending connector and security system items, but it seems like everything OK, however, no email will be sent, please help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi,  

In order to better solve the issue, I need to collect more information  

Could you received mail normally?  

Have you recently made any changes to the settings in Exchange?  

-  Is there a specific error or NDR when sending an email fails?  

-  Please try to restart the Exchange server and run the following command to check whether required services are running.    Test-ServiceHealth  

3.Please try to create a new receive connector according to the previous settings.  

4.Please check the queue in the queue viewer in Exchange toolbox, especially the "last error" attribute, which expresses the cause of the mail stuck in the queue.  

5.Please run the following command line to enable the protocol logging, the Protocol logging records the SMTP conversations that occur between messaging servers and between Exchange services in the transport pipeline as part of message delivery. Please send a test email and then check whether relevant information is recorded in the protocol log.

```
  -ProtocolLoggingLevel Verbose
```

For more information:Configure protocol logging

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
