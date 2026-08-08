---
title: "New-MailboxRestoreRequest for exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1104512/new-mailboxrestorerequest-for-exchange-online
question_id: 1104512
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# New-MailboxRestoreRequest for exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1104512/new-mailboxrestorerequest-for-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We accidentally shorten the retention period to move the email to online archive. We want to move back to inbox from online archive, I have do some research that powershell New-MailboxRestoreRequest can do. However, I can't find the parameter that can pick the date range for email to restore. any idea?     

Moreover, If we want to restore to same the folder structure to the inbox not new folder ,is it use -TargetRootFolder "[Email full address]"?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-28*

Hi @Stephen Mok      

I'm afraid there is no available parameters for the New-MailboxRestoreRequest to filter the emails by date.    

Or you could consider exporting and importing Outlook pst to meet your requirements as well. And you will be able to filter the emails according to the time.    

Logon user’s Outlook, export the archive mails to pst. Then import it to primary mailbox.     

    

Some related discussion:    

Move Office 365 online archives back into mailbox    

How to Move Archived Emails Back to Inbox in Office 365? Complete Guide to Follow    

Please Note: Since the web sites are not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
