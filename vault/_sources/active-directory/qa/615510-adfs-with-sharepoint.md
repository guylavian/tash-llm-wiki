---
title: "Adfs with Sharepoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/615510/adfs-with-sharepoint
question_id: 615510
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-development-routing", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adfs with Sharepoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/615510/adfs-with-sharepoint (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys!  

I have a question for you....  

In my test environment I have two domains:  

DOMAIN A and DOMAIN B  

In domain A I have Sharepoint Portal which uses ADFS to authenticate users.  

Now I have to federate the two domains and allow Domain B users to login to the Portal.  

You can help me out because it doesn't work at the moment.  

Thanks a lot to everyone

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-04*

Is there an Active Directory bidirectional trust between domain A and domain B? If so, there's nothing to do in ADFS really (unless you have specials rules that scope groups or for claims or access).
