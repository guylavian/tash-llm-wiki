---
title: "My exchange server send email in every gmail as spam"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1044579/my-exchange-server-send-email-in-every-gmail-as-sp
question_id: 1044579
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# My exchange server send email in every gmail as spam

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1044579/my-exchange-server-send-email-in-every-gmail-as-sp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a problem with my exchange server 2019. Every send email to gmail is mark as spam. Your help means a lot, Thank you.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-13*

Hi! @Anonymous      

Since this issue doesn’t occur on other recipients except Gmail, to me the cause of this issue may possibly be due to anti-spam settings on Gmail side.    

I would recommend contacting Gmail support for further investigation.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-10-13*

You could check the SCL in the message header for those 'spam emails'.    

In Exchange server, when a message is assigned a spam confidence level (SCL) value by Exchange, and the SCL value is greater than the SCL Junk Email folder threshold value that's configured for the Exchange organization (the default value is 4) or directly on the mailbox (the default value is not configured), the junk email filter rule moves the message to the Junk Email folder.    

We could manually add the domain to the safe sender domain using powershell.     

```
$All = Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited; $All | foreach {Set-MailboxJunkEmailConfiguration $_.Name -TrustedSendersAndDomains  
@{Add="gmail.com"} -Enabled $true}
```

Details: Configure Exchange antispam settings on mailboxes

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-12*

Hi,     

Noted, Check with messager receivers, anyone might marked your email id as a spam, try to restore that email id or use another one new email id for this procedure.
