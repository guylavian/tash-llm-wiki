---
title: "Sync problem: Outlook fo IOS and Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1042147/sync-problem-outlook-fo-ios-and-exchange-online
question_id: 1042147
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Sync problem: Outlook fo IOS and Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1042147/sync-problem-outlook-fo-ios-and-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all.    

I have a curious problem with Outlook for IOS and an Exchange Online mailbox.    

The situation is the following: a user of mine has 2 mailboxes configured on the IPhone: both Exchange Online, same tenant, same domain.    

One of the two mailboxes stops synchronizing after 1 or 2 days. The only way to fix the problem is remove Outlook for IOS and reinstall it. But after a couple of days the problem returns. No problem on the other mailbox.    

Another detail: if I try to remove the account and reconfigure it (without remove Oulook) I get the following error:     

AADSTS90002: Tenant 'LONG_STRING' not found. Check to make sure you have the correct tenant ID and are signing into the correct cloud.    

Can someone help me please ?    

Thank's :D

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-14*

@Giuseppe Lucente      

We cannot test Autodiscover on mobile.     

A quick way to troubleshoot is trying to configure this mailbox on another device, then check whether the same phenomenon occurs. If this phenomenon doesn't occur, it means this issue is related with the IOS device.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-12*

Hi Kyle, thanks for your reply.    

I have news related to the problem: the emails are not synchronized but the iphone receives the notification of the arrival of the emails :D     

Anyway...both mailboxes have the same (valid) license.  There are 4 clients that access the mailbox with Outlook for Windows (without problems). POP and IMAP protocol are disabled.    

Basic authentication is disabled for the following legacy protocols:    

```
Exchange ActiveSync (EAS, used by mobile devices)  
Exchange Web Services (EWS, used by Outlook for Windows & Mac)  
Post Office Protocol (POP3, used by email clients)  
Internet Message Access Protocol (IMAP, used by email clients)  
Exchange Online Remote PowerShell (used for executing scripts)  
MAPI (used by all versions of Outlook for Windows)  
Offline Address Book (OAB, used by Outlook for Windows)  
RPC (used by older versions of Outlook for Windows)
```

How can I check and/or test the Autodiscover on the smartphone ?    

I suspect that the problem is the Outlook on the IPhone and not EXO.  But what can be done?    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-11*

@Giuseppe Lucente      

Make sure this mailbox is configured with Autodiscover, due to the basic authentication disabled in Office 365, there will exist issue when you try to configure mailbox in POP/IMAP.    

Check whether those two mailboxes assigned with the same licenses from Microsoft admin center first. Mark sure all licenses are valid.    

Then if this phenomenon occurs again, try to configure this mailbox in Outlook for PC client, check whether there exists with this mailbox.    

You can also have a check about the service health, check whether there exists issue in your tenant.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
