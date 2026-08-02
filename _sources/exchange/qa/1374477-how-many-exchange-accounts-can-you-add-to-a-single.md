---
title: "How many Exchange accounts can you add to a single mail profile in Outlook?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374477/how-many-exchange-accounts-can-you-add-to-a-single
question_id: 1374477
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator"]
---
# How many Exchange accounts can you add to a single mail profile in Outlook?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374477/how-many-exchange-accounts-can-you-add-to-a-single (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How many Exchange accounts can you add to a single mail profile in Outlook?

## Answer (community) — Microsoft Moderator

*upvotes: 3 · updated: 2023-09-25*

Hi @FEMY FRANCISCO  ,

How many Exchange accounts can you add to a single mail profile in Outlook?

Beginning with Outlook 2013，by default up to 10 Exchange accounts can be added to a single mail profile.  

But it you need to add more than 10 Exchange accounts in one profile for some reason, you can extend this limit up to 9999 using registry below:

Important: Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, back up the registry for restoration in case problems occur.

Key: `HKEY_CURRENT_USER\Software\Microsoft\Exchange`  

Value name: `maxnumexchange`  

Value type: `REG_DWORD`

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
