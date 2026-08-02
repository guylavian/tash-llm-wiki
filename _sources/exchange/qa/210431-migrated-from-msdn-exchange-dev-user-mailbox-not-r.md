---
title: "[Migrated from MSDN Exchange Dev]User mailbox not receiving mails from external"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/210431/migrated-from-msdn-exchange-dev-user-mailbox-not-r
question_id: 210431
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]User mailbox not receiving mails from external

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/210431/migrated-from-msdn-exchange-dev-user-mailbox-not-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This  thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

We have a hybrid module. Accounts are created in AD and synced to cloud using AAD connect. Mailbox exists in cloud.  

We having been noticing few user accounts which was disabled and activated back in AD. After this, the mailbox will only receive mails from internal but not external.   

I have to update the Proxy address every time - switch the primary address to different smtp, sync to cloud and again switch to original smtp then works fine. Unless user reports we don't get to know. I don't know what the issue is, can anyone help?  

I have reviewed the mailbox settings, properties both on AD cloud. They look good  

The external sender will receive error :   

Your message was rejected by the recipient's domain because the recipient's email address isn't listed in the domain's directory. It might be misspelled or it might not exist.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-25*

Hi，    

If you do not change the primary smtp address and synchronize again, can you receive mail normally?    

After the user account is disabled and activated in AD, is it normal to check the smtp address of the mailbox in the EAC of Exchange online?    

Based on the information you provided, I think the issue may be caused by synchronization. Please run the following command to check settings of Azure AD connect.    

```
Get-ADSyncScheduler
```

For more information: Azure AD Connect sync: Scheduler    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
