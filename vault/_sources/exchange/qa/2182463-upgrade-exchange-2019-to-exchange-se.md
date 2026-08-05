---
title: "Upgrade Exchange 2019 to Exchange SE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2182463/upgrade-exchange-2019-to-exchange-se
question_id: 2182463
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Upgrade Exchange 2019 to Exchange SE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2182463/upgrade-exchange-2019-to-exchange-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,

Currently we have exchange 2019 CU14 hosted on windows server 2019, to in-place upgrade the new SE version do we need to upgrade the OS to Windows Server 2022? even after migrate the current cu14 to cu 15

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-02-27*

To upgrade Exchange 2019 from CU14 to CU15, you don’t need to upgrade your Windows Server 2019 to Windows Server 2022. However, for future deployments and better long-term support, it is recommended to install Exchange Server Subscription Edition (SE) on a newer operating system like Windows Server 2022 or Windows Server 2025, once it is released.     

It’s important to note that upgrading the underlying Windows OS on an existing Exchange Server is not supported. Therefore, if you plan to build a new server or migrate to Exchange SE, it's best to install the latest Windows OS before deploying Exchange Server to ensure the setup remains supported for a longer period. You can do in-place upgrade from current version to Exchange Server SE.  

You can refer this link.  

*Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.  

*  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-26*

Hi @Ahmed Essam,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, your question is about the version of Windows required to upgrade Exchange 2019 to Exchange SE.

Since the lifecycle of Windows Server 2019 ends in January 2029, it is recommended to install a new deployment of Exchange Server SE RTM on Windows Server 2022 or Windows Server 2025.

Additionally, upgrades of the underlying Windows OS on an Exchange Server are not supported and will remain unsupported.  For customers building new servers, we encourage you to install the newest Windows OS before installing Exchange Server on it (including Windows Server 2025 once Exchange 2019 CU15 is released).

You can refer to this link for details: https://techcommunity.microsoft.com/blog/exchange/upgrading-your-organization-from-current-versions-to-exchange-server-se/4241305

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
