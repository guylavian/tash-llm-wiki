---
title: "[Migrated from MSDN Exchange Dev] Cannot send email attachments more than 1MB outside"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130605/migrated-from-msdn-exchange-dev-cannot-send-email
question_id: 130605
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Cannot send email attachments more than 1MB outside

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130605/migrated-from-msdn-exchange-dev-cannot-send-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a problem, my system is sending lots of emails with ~ 300kb files attached to the network from a mailbox address. From a good mailbox when I send an email with a file attachment larger than 1MB, the system does not queue that email, I check in the delivery report in Mail flow that the mail status is pending.  

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/6f69fd61-8a3b-4755-bf70-bf12e2792383/cannot-send-email-attachments-more-than-1mb-outside?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

Please run the following command to check the existing Message size limit:

```
Get-TransportConfig | Format-List MaxReceiveSize,MaxSendSize,MaxRecipientEnvelopeLimit  
Get-TransportRule | where {($_.MessageSizeOver -ne $null) -or ($_.AttachmentSizeOver -ne $null)} | Format-Table Name,MessageSizeOver,AttachmentSizeOver  
Get-ReceiveConnector | Format-Table Name,Max*Size,MaxRecipientsPerMessage
```

The following command is for mailbox-specific limits：

```
Get-Mailbox  | Format-List MaxReceiveSize,MaxSendSize,RecipientLimits
```

Besides, which version of Exchange/Outlook are you using? Could you post the whole message tracking log with personal information covered?

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
