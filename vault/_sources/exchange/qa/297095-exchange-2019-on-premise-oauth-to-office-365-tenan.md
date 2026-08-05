---
title: "Exchange 2019 on premise - OAuth to Office 365 tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297095/exchange-2019-on-premise-oauth-to-office-365-tenan
question_id: 297095
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-teams-teams-business-other-l1"]
---
# Exchange 2019 on premise - OAuth to Office 365 tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297095/exchange-2019-on-premise-oauth-to-office-365-tenan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in middle of upgrading our exchange 2013 environment to 2019.  Once this is completed the intent is to perform the OAuth cmdlet to our office 365 tenant to allow for more of the Teams integrations to work.(ie teams calendar, teams live meeting, adding meetings in Office 365 writing back to on premise exchange calendar).    

The second scenario we have is a second tenant that is reading the same AD(multi-forest) infrastructure.  When we perform the OAuth to the first tenant will this have any impacts on the Office 365 tenant functionalities of the second one?  ie. teams calendar, any account functionalities within Office 365?   

We are using two Azure AD connect instances to synchronize accounts to the cloud.  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Hi @Brad De Sousa      

Could you please provide more information about your environment? How many forests and tenants do you have, did you deploy a hybrid for your on-premise Exchange server and o365 or you are going to configure it?     

The official document below introduces about     

How to configure Exchange Server on-premises to use Hybrid Modern Authentication    

And if you didn't depoly hybrid previously: Use OAuth on Exchange on-premises without Hybrid Modern Authentication    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
