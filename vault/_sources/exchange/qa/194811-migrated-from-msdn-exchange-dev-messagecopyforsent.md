---
title: "[Migrated from MSDN Exchange Dev] MessageCopyForSentAsEnabled not applying"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/194811/migrated-from-msdn-exchange-dev-messagecopyforsent
question_id: 194811
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] MessageCopyForSentAsEnabled not applying

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/194811/migrated-from-msdn-exchange-dev-messagecopyforsent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 CU12 - messages sent as shared mailbox or user mailbox are not copied to the shared mailbox / sender mailbox sent items, with MessageCopyForSentAsEnabled $True  

I've gone trough all google hits, none of them working. Any suggestions?  

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/d54e338a-0651-4337-90d1-da7e2c099c2c/messagecopyforsentasenabled-not-applying?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-11*

Do you try to send emails from the OWA?    

When you send as a shared mailbox, this email will show in your mailbox Sent Items by default. If you want this email could also show in shared mailbox, you need to enable the "MessageCopyForSentAsEnabled" on shared mailbox rather than your mailbox. I would suggest you check the configuration again.    

```
Get-Mailbox YourShared | fl MessageCopyForSentAsEnabled
```

When you send email from Outlook client, if there exist multiple mailboxes in this profile, you need to choose the email address that between the horizontal line, those email addresses are the send as email address(Will appear after the first use):    

    

If you select the address above the horizontal line, the email will be sent directly from the this mailbox rather than sent in the way of "send as".    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
