---
title: "Active directory upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/95851/active-directory-upgrade
question_id: 95851
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active directory upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/95851/active-directory-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are working on Active directory upgrade from 2012 R2 to 2019. There is a trust relationship that exist between the primary domain and other domains (around 15). With some of them the trust is bidirectional and with some inbound/outbound. The concern is when we promote new 2019 domain controllers or demote old 2012 r2 domain controllers will it effect the trust relationship between domains ?  

Please, Suggest.  

Thanks,  

Pranay.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-15*

Here's a couple of discussions on this topic.  

https://social.technet.microsoft.com/Forums/lync/en-US/00cc2cc9-b4b5-42d8-9484-b475a8354b36/twoway-trust-in-two-forests-with-difference-functional-level-after-transfer-fsmo-roles?forum=winserverDS#:~:text=No%2Cit%20won%27t%20effect,be%20remain%20on%20the%20domain.  

https://social.technet.microsoft.com/Forums/en-US/a4f01cac-5174-49bd-a938-e67ffd76af68/forest-trust-relationship-and-raising-forest-domain-funtional-levels?forum=winserverDS  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-15*

Hi Patrick,  

Thanks for the reply, can you also suggest the reason behind this or any good article which discusses this.  

Thanks,  

Pranay.
