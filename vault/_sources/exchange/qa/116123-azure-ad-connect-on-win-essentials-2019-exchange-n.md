---
title: "Azure AD Connect on Win Essentials 2019, Exchange needed?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116123/azure-ad-connect-on-win-essentials-2019-exchange-n
question_id: 116123
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# Azure AD Connect on Win Essentials 2019, Exchange needed?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116123/azure-ad-connect-on-win-essentials-2019-exchange-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have a customer that is going to install Windows Server 2019 Essentials. I know that is the only version of Essential editions that AD Connect is supported. But in order to update Exchange attributes is also needed to have Exchange on-premise installed too?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-09*

You should not need to install Exchange as Azure AD connect syncs the active directory attributes. I have a few customers running Azure AD connect with no Exchange on-premise.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-05*

Hi anonymous user , what's the detailed information about your environment?     

Are you using Exchange hybrid or O365 only?     

If you are using Exchange hybrid, you could refer to the official document which introduces different scenarios whether we need to keep the on-premise Exchange server in your environment.    

How and when to decommission your on-premises Exchange servers in a hybrid deployment    

If your environment never has on-premise Exchange servers deployed, it should work fine without them. However, microsoft recommend to install Exchange server in your organization because you have directory sync and your objects are being synced from on-premises to Office 365. Here is a retaled thread discussed about this question for your reference: Is an on-premises Exchange server still required with Azure AD Connect?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
