---
title: "Balance FSMO roles on domain."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/644290/balance-fsmo-roles-on-domain
question_id: 644290
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Balance FSMO roles on domain.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/644290/balance-fsmo-roles-on-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!  

  Nowadays (W2K19 servers), what is the best practice for configuring FSMO roles on domain? How should I balance those rules?  

C:\Users\Administrator>netdom query fsmo  

Schema master               ???  

Domain naming master        ???  

PDC                         ???  

RID pool manager            ???  

Infrastructure master       ???  

The command completed successfully.  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-01*

Hi there,  

According to Microsoft's recommendation, the Best Practice is to split the FSMO roles between the different domain controllers. The forest-wide FSMO roles should be placed on one DC, and the domain-wide roles on another. If you have only one domain controller, it is recommended you deploy an additional DC.  

-In multi-domain environments, place both forest-wide roles on the root controller, which is also a Global Catalog server.  

-Place all domain-wide roles on one server with sufficient performance  

-If you are using virtualized domain controllers, disable time synchronization of virtual machines with FSMO roles with the host;  

-Do not place any other tasks on the domain controllers  

Hope carrying out the above steps will help you out.  

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-30*

Thanks all!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-29*

Hello,  

As DSPatrick mention not need nowadays to split them unless you have performance issue, the other rule will be to ensure that you have at least another domain controller in the same site (AD Site) as the DC holding the FSMO roles  

Regards,
