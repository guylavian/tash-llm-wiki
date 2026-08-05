---
title: "Exchange Online Mailboxes still receiving mail without a license."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1057879/exchange-online-mailboxes-still-receiving-mail-wit
question_id: 1057879
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Mailboxes still receiving mail without a license.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1057879/exchange-online-mailboxes-still-receiving-mail-wit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently running a hybrid MS 365 environment using AD connect to sync.    

Scenario;    

UserA    

User mailbox was migrated from on-prem Exchange server to Exchange Online    

I remove the license and lock the account via AD    

I send email to user A and it still delivers.    

UserB    

User was created in AD and after the AD Sync I created the mailbox on M365.    

I remove the license and lock the account.    

I send email to user A I get an NDR.9 Which is the desired result .    

Why are my migrated accounts still accepting mail?    

We don't delete accounts, we disable them for audit and record keeping    

Sincere thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-24*

Hi @Sam Brink      

Is there any update here about your question?     

I agree with the method shared above using a mailflow rule to reject the message sent to that account. And according to my research, I found this thread discussed the similar question: E3 license removed but mailbox still receives mail.    

It shared a solution: Remove the proxy addresses from on-premise AD account.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-21*

If you want to prevent message delivery, use a mail flow rule. As long as the mailbox still exists, it will keep receiving messages regardless of whether it has license or not.    

There are many scenarios is which a mailbox will exist even when you remove the Exchange license, such as when it was put on hold, shared/resource mailboxes, migrated mailboxes in the grace period, etc.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-21*

When you remove the license for a regular user mailbox, the mailbox doesnt necessarily go away immediately ( I Assume that is what you want).    

It may take some time and is actually recoverable for 30 days:    

https://learn.microsoft.com/en-us/microsoft-365/admin/manage/remove-licenses-from-users?view=o365-worldwide
