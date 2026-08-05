---
title: "Any reason to keep Exchange Server 2019 running on premise after all user mailboxes are migrated successfully to ExO?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1571964/any-reason-to-keep-exchange-server-2019-running-on
question_id: 1571964
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Any reason to keep Exchange Server 2019 running on premise after all user mailboxes are migrated successfully to ExO?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1571964/any-reason-to-keep-exchange-server-2019-running-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need some clarification on retaining the most recent Exchange Server installation in my on-premise data centre.   

All of my users have been migrated to Exchange Online, and the old AD DS has been synced to Azure AD (Entra ID).   

There are several Exchange Server 2016 installations on my single forest AD Domain. 

Does this mean I'll need to perform the inline upgrade to Exchange Server 2019 (the most recent Cumulative Update) and only maintain that one server running with just the Management Console?
Any help would be greatly appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-23*

Hi @EnterpriseArchitect  ,  

Supposing your organization has been running in a hybrid configuration, if you don't need to manage your users synced from on-premises, you can remove the Exchange server on-premise. Otherwise, you do need to remain at least one Exchange server on-premise. For more details, hopefully you can find the scenarios in the article below helpful:  

How and when to decommission your on-premises Exchange servers in a hybrid deployment  

(Note: if you just want to keep an on-prem Exchange for recipient management, you can be able to shut down the last Exchange server and manage recipients using Windows PowerShell, see Manage recipients in Exchange Hybrid environments using Management tools.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
