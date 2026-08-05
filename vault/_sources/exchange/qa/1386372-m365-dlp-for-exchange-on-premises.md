---
title: "M365 DLP for Exchange On-Premises"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1386372/m365-dlp-for-exchange-on-premises
question_id: 1386372
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# M365 DLP for Exchange On-Premises

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1386372/m365-dlp-for-exchange-on-premises (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi..

We are using Exchange 2016, with no hybrid deployment. However, we have E5 licenses and wish to fully use all E5 security features. My questions are listed below, and it would be wonderful if someone could answer them.

-  We want to integrate Intune with Exchange 2016, for this i need to activate HMA.  Is a hybrid setup required to enable HMA?

-  Given that our user base is currently hosted on an On-Premise exchange and Is it feasible to route all internet emails via M365 to utilize M365 DLP for emails?  without HCW and assuming users are synced to Azure AD.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-10*

Hi @Chandra Sekhar,

We want to integrate Intune with Exchange 2016, for this i need to activate HMA. Is a hybrid setup required to enable HMA?

Yes Exchange hybrid deployment is required.

Please refer to this Exchange blog:

Announcing Hybrid Modern Authentication for Exchange On-Premises

That’s why we put the H in HMA, you need to be configured Hybrid with Exchange Online for this feature.

Given that our user base is currently hosted on an On-Premise exchange and Is it feasible to route all internet emails via M365 to utilize M365 DLP for emails? without HCW and assuming users are synced to Azure AD.

Exchange hybrid deployment is not necessary in this scenario.

For more details please refer to these documentations: 

Standalone Exchange Online Protection

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
