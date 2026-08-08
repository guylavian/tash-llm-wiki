---
title: "exchange mail contacts and shared smtp"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/330356/exchange-mail-contacts-and-shared-smtp
question_id: 330356
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# exchange mail contacts and shared smtp

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/330356/exchange-mail-contacts-and-shared-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to have multi mail contacts all forwarding out to a separate domain (smtp address).   

error:  

The proxy address "SMTP:******@do.com" is already being used by the proxy addresses or LegacyExchangeDN of "do.com/users - Contacts/test1". Please choose another proxy address.( The "MailContact" with display name "test1" is already setup and using the same address.)  

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi @Efff dd      

According to the error information above, we will need to find which mailbox/recipient is using the proxy address, then remove the proxy address from other mailbox/recipient.    

Get-Recipient | where {$_.EmailAddresses -match "******@do.com"}    

Or     

Get-Mailbox ******@do.com | fl UserPrincipalName,EmailAddresses    

Below are the links which discussed about this similar issue:     

How to fix conflicting proxy addresses in O365 when creating a mailbox    

The proxy address is already being used by the proxy address of another mailbox    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
