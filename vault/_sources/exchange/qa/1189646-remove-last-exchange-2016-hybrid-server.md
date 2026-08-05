---
title: "Remove last Exchange 2016 hybrid server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189646/remove-last-exchange-2016-hybrid-server
question_id: 1189646
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Remove last Exchange 2016 hybrid server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189646/remove-last-exchange-2016-hybrid-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

We are running 1 Exchange hybrid with an Exchange Server 2016. All mailboxes are moved to EXO. Since it's now possible to remove the last Exchange Server, we would like to go this last step.

My problem is, that our forest functional level is still 2008 because of some Windows-XP workstations with controls for production lines. They can't be upgraded at the moment. I have read that one step to remove the last Exchange is to install Exchange Server 2019 April 2022 CU Setup to install the Exchange Management Tools, but that needs at least forest functional level 2012.

Is there a way to remove the last Exchange Server 2016 anyway?

Regards, Peter

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-14*

You can, but you wont be supported if you are still using AADConnect to sync from on-prem to Azure.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-15*

Hi @Peter B,

Is there a way to remove the last Exchange Server 2016 anyway?

If you don't need to manage users from on-premises and no longer have a need for directory synchronization or password synchronization, you can go ahead decommissioning the last Exchange server 2016. Detailed instructions can be found in Scenario One of the following document:

How and when to decommission your on-premises Exchange servers in a hybrid deployment

If you still need to keep directory synchronization or need to use Exchange for other purposes, it's not supported to remove the last Exchange server. You can learn more from the other two scenarios mentioned in the linked article above.

When it comes to your concern about "install Exchange Server 2019 April 2022 CU Setup to install the Exchange Management Tools", this can only allow you to shut down (not remove) the last Exchange server and manage recipients using Windows PowerShell. More details, see Manage recipients in Exchange Hybrid environments using Management tools.

If the answer is helpful, please click "`Accept Answer`" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
