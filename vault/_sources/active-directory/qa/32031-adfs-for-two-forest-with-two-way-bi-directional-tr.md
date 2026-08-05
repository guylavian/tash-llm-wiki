---
title: "ADFS for two forest with two way bi-directional trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/32031/adfs-for-two-forest-with-two-way-bi-directional-tr
question_id: 32031
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS for two forest with two way bi-directional trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/32031/adfs-for-two-forest-with-two-way-bi-directional-tr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,  

I have a scenario, in which we have two seperate forests A and forest B. There is a two way bi-directional trust between them.  

I have ADFS in forest A and there are many relying party applications ( SAML based ) in forest A.  

I want my users in forest B, to access applications in forest A.  

Question:  

-  Will it require to have ADFS in forest B or forest trust will do the job?  

-  Does it make sense to have Forest trust and also create ADFS trust between the two ADFS A and B for such a scenario ?  

Thank You

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-06-04*

-  The forest trust is enough. You'll have single sign-on without adding an ADFS in forest B.  

-  If your goal is to provide SSO, then it is required. But you might have other requirements such as delegation, or internal policies that would make the use of a "central" ADFS farm difficult. Note that when an ADFS farm trusts another one, the users will be asked to pick which farm they are from. It is called Home Realm Discovery, it can be tuned to some extend but ultimately it might change the way the authentication work for users in both sides.
