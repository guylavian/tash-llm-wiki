---
title: "Upgrade domain controllers to a newer version of Windows Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/904162/upgrade-domain-controllers-to-a-newer-version-of-w
question_id: 904162
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Upgrade domain controllers to a newer version of Windows Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/904162/upgrade-domain-controllers-to-a-newer-version-of-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers    

Step 5: On the Deployment Configuration screen, select Add a new domain to an existing forest and select Next.    

It should be the first choice:  Add a domain controller to an existing domain    

Right?    

Thanks.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-28*

Hello EmmaYoyo,    

In this case, the information is correct to Add a New Domain controller upgrading your environment, as if you are adding the Domain controller to your Forest Root domain (for example "Contoso .com") and the operation needs to upgrade the Forest Functional Level, not only the Domain Functional Level.     

-----------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
