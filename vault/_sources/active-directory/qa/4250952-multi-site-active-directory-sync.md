---
title: "Multi-Site Active Directory Sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4250952/multi-site-active-directory-sync
question_id: 4250952
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Multi-Site Active Directory Sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4250952/multi-site-active-directory-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

I have created 4 Active Directory Domain Controllers both in different locations. One is in Delhi and Another one in Mumbai.

Delhi has 2 domain controllers Primary(DDC01) and Secondary(DDC02).

Mumbai has 2 domain controllers Primary(MDC01) and Secondary(MDC02).

Both have different networks and I can take the RDP of both Domain controllers from different locations.

Now I want to connect all 4 Domain Controllers so they can replicate the data and policies.

I saw this can be done through Active Directory Site and Services.

I Added Subnet's of Both Sites in Mumbai DC i.e. MDC01

I created Sites such as Mumbai-HO and Delhi-BO in MDC01 it got replicated to MDC02.

I could see MDC01 and MDC02 but I cannot see any of the DDC01 or DDC02 showing there.

I am checked all the Active Directory ports are opened between both Sites.

Please find the list of ports below: -

UDP Port 88 for Kerberos authentication UDP and TCP Port 135 for domain controllers-to-domain controller and client to domain controller operations. TCP port 139 and UDP 138 for File Replication Service between domain controllers. UDP Port 389 for LDAP to handle normal queries from client computers to the domain controllers. TCP and UDP Port 445 for File Replication Service TCP and UDP Port 464 for Kerberos Password Change TCP ports 3268 and 3269 for Global Catalog from client to domain controller. TCP and UDP Port 53 for DNS from client to domain controller and domain controller to the domain controller.

Am I missing something?

Just FYI... DDC01 and DDC02 are having different gateways due to some reason.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2021-10-29*

Hi Prateek,

I am Dave, I will help you with this.

I apologize, Community is just a consumer forum, due to the scope of your question (Active Directory) can you please post this question to our sister forum on Microsoft Q&A (The IT Pro Forum)

Over there you will have access to a host of Active Directory and IT Pro experts and will get a knowledgeable and quick answer to this question.

https://docs.microsoft.com/en-us/answers/index....
