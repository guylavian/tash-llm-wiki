---
title: "[Migrated from MSDN Exchange Dev]  FortiMail Received Mail.But Users are not able to receive in Outlook."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150546/migrated-from-msdn-exchange-dev-fortimail-received
question_id: 150546
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]  FortiMail Received Mail.But Users are not able to receive in Outlook.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150546/migrated-from-msdn-exchange-dev-fortimail-received (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/6ef4cd00-bbd8-48f4-8b83-8477082568cf/fortimail-received-mailbut-users-are-not-able-to-receive-in-outlook-exchange2016?forum=exchangesvrdevelopment    

Hello Support,    

Exchange Server 2016 (CU18) Single Server    

User are complaining mails are not getting from clients.    

When we checked in Fortimail Antispam device.    

Mail flow successfully released.    

i.e:-    

    

Fortimail Spam Controller mail is not blocked.    

Mails are not receiving in Outlook.     

How to check, in Exchange side. mails were stuck or something.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hello EricYin,    

Thanks for your reply.    

External user Outside of domain mails Only specific user mails were not getting.    

i run this command as below    

i am getting this logs below    

    

How i can ensure with this log, mails are received in user's Outlook

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Open Exchange Management Shell and run the following command:

```
Get-MessageTrackingLog -ResultSize Unlimited -Start "11/01/2020" -End "11/04/2020" -Sender "******@contoso.com"| fl Timestamp ,EventID, Source, MessageInfo, RecipientStatus, MessageSubject
```

If the messages were stuck or failed in Exchange, it should be logged in this message tracking log and you could know what happened through these properties. For detailed information, see Message tracking. Be free to post the log here if you need further assistance.  

Besides, what's in common among these messages? It only happens when specific sender sending mails to a specific user?

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
