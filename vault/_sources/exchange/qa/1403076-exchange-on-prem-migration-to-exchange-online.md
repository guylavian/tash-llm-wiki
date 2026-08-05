---
title: "Exchange on-prem migration to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1403076/exchange-on-prem-migration-to-exchange-online
question_id: 1403076
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange on-prem migration to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1403076/exchange-on-prem-migration-to-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm trying to migrate my on-prem mailboxes in Exchange 2016 to Exchange online using cutover migration.

The exchange activesync test is working.

When i try to create the migration endpoint it gives me this error:

I've enabled MRS Proxy in EWS virtual directory.

What am i missing to setup or where could be the problem?  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-25*

Did you checked this thread - https://answers.microsoft.com/en-us/msoffice/forum/all/i-have-the-error-response-content-is-null-when-i/728ab075-6f33-47c1-aeeb-8d06152aff45

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-25*

Hi @André Barradas  ,  

Have you tried the options listed in the error message like changing the mailbox provided and see how it goes? 

If it doesn't work, it's suggested to try updating the password of the administrator account you entered when creating the migration endpoint and try it again.

Furthermore, you can also take a look at the following article and see if you have missed any preparation tasks:   

Prepare for a cutover migration  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
