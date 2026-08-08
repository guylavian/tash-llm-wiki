---
title: "Upgrade AD onto new server and migrate Exchange 2016 to 2029"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1251138/upgrade-ad-onto-new-server-and-migrate-exchange-20
question_id: 1251138
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Upgrade AD onto new server and migrate Exchange 2016 to 2029

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1251138/upgrade-ad-onto-new-server-and-migrate-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one forest and on domain, two DC on this and Exchange Server 2016 in an hybrid configuration.
We are preparing to migrate AD roles to new DC servers with Windows Server 2022 (the current DCs have Windows Server 2012R2 and NFL 2088R2), and then, migrate Exchange Server 2016 to 2019 (on-premise). It is correct do this in that sequence?, first AD and final Exchange. Or must be do this migrating Exchange first and then AD. We need some advise from someone that has done this already.
I hope you guys can give us some advise
Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-24*

Hi @ Scorpion，

Can I understand that you need to migrate across forests?

Then yes, it is generally recommended to perform an Active Directory (AD) migration prior to an Exchange migration. This is because Exchange relies heavily on AD for operations.

Here's a related post detailing two ways to migrate across forests, both migrating Aand D users first and then migrating Exchange mailboxes:

Cross-forest mailbox migration with ADMT - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-21*

Hello there,
You cannot update Exchange 2016 to Exchange 2019 directly. You need to create Exchange 2019 coexist with Exchange 2016 first, then migrate mailboxes to Exchange 2019, then uninstall Exchange 2016.
This article describes when and how to transfer or seize Operation Master roles, formerly known as Flexible Single Master Operations (FSMO) roles.
https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-operation-master-roles-in-ad-ds
Similar discussion here https://learn.microsoft.com/en-us/answers/questions/132513/migration-from-exchange-2016-cu3-to-exchange-2019
Hope this resolves your Query !!
--If the reply is helpful, please Upvote and Accept it as an answer--
