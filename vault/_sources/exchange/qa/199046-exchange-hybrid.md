---
title: "Exchange Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199046/exchange-hybrid
question_id: 199046
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199046/exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

Can advise possible to co-exist both Exchange Hybrid 2003 & 2016 with O365?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Hi @Russell Ang      

Do you mean Exchange 2003 or Exchange 2013?    

According to the official document list below: Exchange 2003 is not supported co-exist with Exchange 2016    

    

And if you want to deploy the Exchange 2003 hybrid, you will need to upgrde it to Exchange 2010 first, like this article introduces: Setting up Hybrid Migration from Exchange 2003 to Office 365    

If Exchange 2013, it is supported for Exchange 2013 - 2016 coexistence hybrid.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-15*

If you mean can both versions can exist in a hybrid config in the same org , yes.    

https://learn.microsoft.com/en-us/exchange/hybrid-deployment-prerequisites#prerequisites-for-hybrid-deployment
