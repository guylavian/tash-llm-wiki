---
title: "Microsoft Exchange on Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/242667/microsoft-exchange-on-azure
question_id: 242667
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Microsoft Exchange on Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/242667/microsoft-exchange-on-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Microsoft Exchange plan in Azure and it is sending some items to the Junk folder. Is there a way in Azure to turn this off and put all new mail automatically in the in-box.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Hi @jeff_hoffelner      

How many users in your organization encountered the issue regular messages moved to junk folder? Did you configure any 3rd party spam filter for your organization?    

In Exchange side, we could check if there is any related information recorded in the message trace log why the mails are moved to junk folder.    

Also, we could disable the junk email rule on all users with below command, introduced in the official document: Configure junk email settings on Exchange Online mailboxes    

```
$All = Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited; $All | foreach {Set-MailboxJunkEmailConfiguration $_.Name -Enabled $false}
```

In addition, if you configured any 3rd party spam filters, which will also lead to the mails go to junk folder like the scenario 1 list here: Manage mail flow using a third-party cloud service with Exchange Online    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
