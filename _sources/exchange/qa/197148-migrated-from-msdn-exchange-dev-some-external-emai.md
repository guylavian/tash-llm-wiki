---
title: "[Migrated from MSDN Exchange Dev] Some external emails blocked after migration from Exchange 2007 to 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197148/migrated-from-msdn-exchange-dev-some-external-emai
question_id: 197148
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Some external emails blocked after migration from Exchange 2007 to 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197148/migrated-from-msdn-exchange-dev-some-external-emai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link] Some external emails blocked after migration from Exchange 2007 to 2013  

We recently migrated from Exchange 2007 to Exchange 2013. Some of our users are now complaining that emails to clients (some of whom they used to send emails to successfully on Exchange 2007) are now being blocked with the following message  

Delivery has failed to these recipients or groups:  

name at cntoso.com  

Your message wasn't delivered because the recipients email provider rejected it.  

The following organization rehjected your message: xxxxxxx.mail.protection.outlook.com  

Currently we are advising our users to phone their clients and ask their IT departments to whitelist their email addresses. I just wanted to know if there is anything we can do on our own side/Exchange 2013 that can help somehow? Many thanks everyone

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

Hi,    

Could you please share the complete NDR information here (note to remove personal information)     

Please also try using the Mxtoolbox to check if you have configured all the DNS record correctly and if you are blacklisted    

Compare the message header for the new and previous email to check what changed.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
