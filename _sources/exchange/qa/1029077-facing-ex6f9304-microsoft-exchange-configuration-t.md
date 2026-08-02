---
title: "Facing :  Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|The operation couldn't be performed because object '******@jitter.com' couldn't be found on 'CY4PR15A005DC12.NAMPR15A005.PROD.OUTLOOK.COM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1029077/facing-ex6f9304-microsoft-exchange-configuration-t
question_id: 1029077
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Facing :  Ex6F9304|Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException|The operation couldn't be performed because object '******@jitter.com' couldn't be found on 'CY4PR15A005DC12.NAMPR15A005.PROD.OUTLOOK.COM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1029077/facing-ex6f9304-microsoft-exchange-configuration-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

I tried following the document: https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth but unable to get through this step: https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#register-service-principals-in-exchange.    

When following : Register service principals in Exchange    

I trying to execute below command :    

```
Add-MailboxPermission -Identity "******@contoso.com" -User
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-07*

Anyone know how to supress these errors in Azure Automation runbook ?

It looks like they are being written to Output window, even if you catch them, out-null them, save them in your own ErrorVariable ... they just keep showing nevertheless as Output stream.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

@Vinay Sharma      

Two thing you need to pay attentions to:    

    

You need to connect to Exchange online module with tenant admin account with have permission to find this mailbox and add permission it:    

Use command below to check whether could find this mailbox first as michev said:    

```
Get-Mailbox ******@jitter.com
```

Then check whether this account has permission to run Add-MailboxPermission command (Tested with another user mailbox first):    

```
Add-MailboxPermission -Identity "******@jitter.com" -User "anotherUserMailbox" -AccessRights FullAccess
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-29*

Is "john.smith@Company portal   .com" a valid mailbox within your Office 365 tenant? What does Get-Recipient "john.smith@Company portal   .com" show?
