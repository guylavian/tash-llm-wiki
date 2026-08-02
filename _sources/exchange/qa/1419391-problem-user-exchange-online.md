---
title: "Problem User Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1419391/problem-user-exchange-online
question_id: 1419391
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Problem User Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1419391/problem-user-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,

We have a problem:

Current obstacles:

User status on Server On Premise = Already Migrated O365 .  

But after Exchange Online licensing is activated. There is a statement :   

This user's local mailbox has not been migrated to ‎Exchange Online‎. The ‎Exchange Online‎ mailbox will be available after the migration is complete  

I found it in the active user = menu then the mail column

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-08*

Hi @Ramos simtnt  ，

Does this issue only affect this particular user?  

Are you able to see the mailbox from the Exchange Online EAC > Recipients > Mailboxes? If not, is it available under Recipients > Contacts?  

For current situation, you can have a try by performing a hard match by using GUID and see if it can help. For more details about the steps, you could refer to:  Soft (SMTP) vs. Hard (immutableID) matching with Azure AD Connect.  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
