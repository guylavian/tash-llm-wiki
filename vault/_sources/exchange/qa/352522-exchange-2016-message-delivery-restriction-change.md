---
title: "Exchange 2016 - message delivery restriction, Change settings on bulk mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352522/exchange-2016-message-delivery-restriction-change
question_id: 352522
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 - message delivery restriction, Change settings on bulk mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352522/exchange-2016-message-delivery-restriction-change (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 environment all over 1000 mailboxes have enabled "Require that all senders are authenticated" under   

message delivery restrictions. So the users can't receive messages from other domains.  

What could be the ways to uncheck "Require that all senders are authenticated" from all users?  

I can do it one by one but it's hectic to do for 1000+ users.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-04-12*

Hi @IT-Empire  ,    

What could be the ways to uncheck "Require that all senders are authenticated" from all users?    

Agree with Manu that you can use the command he shared to bulk change the "Require that all senders are authenticated" setting for all mailboxes. It'ssuggested to add "-ResultSize unlimited" as you have more than 1000 users:    

```
Get-Mailbox -ResultSize unlimited | Set-Mailbox -RequireSenderAuthenticationEnabled $false
```

Or you can slightly modify the command to change the setting for all "user mailboxes":    

```
Get-Mailbox -ResultSize unlimited | ?{$_.RecipientTypeDetails -eq "UserMailbox"} | Set-Mailbox -RequireSenderAuthenticationEnabled $false
```

In addtion, if you would like to uncheck the setting for all mailboxes which currently have enabled "Require that all senders are authenticated", you can choose the command as follows:    

```
Get-Mailbox -ResultSize unlimited | ?{$_.RequireSenderAuthenticationEnabled -eq "$true"} | Set-Mailbox -RequireSenderAuthenticationEnabled $false
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
