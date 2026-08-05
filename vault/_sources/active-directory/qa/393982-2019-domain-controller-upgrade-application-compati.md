---
title: "2019 Domain Controller upgrade, application compatibilty"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/393982/2019-domain-controller-upgrade-application-compati
question_id: 393982
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# 2019 Domain Controller upgrade, application compatibilty

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/393982/2019-domain-controller-upgrade-application-compati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Plan is to upgrade 2008 DC’s to 2019 DC’s in our environment.   

We also have Win2003 member servers in out environment, I understand it as a risk but upgrading them as of now is not an option.   

So we’ll be enabling Smbv1 on 2019 DC’s.   

But my main question is how can we verify application compatibility in our environment with 2019 DC’s?   

Can we identify what applications may break on upgrading DC to 2019?   

Is there any authentication protocol version change in 2019 DC, compatibility to which should be pre-checked?   

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hi，  

How are things going? Could you please send me an update so that we can continue to work on this problem and resolve it? Thanks for your help.  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-14*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-14*

Hi,  

Thank you for posting in our forum  

In order to better help you solve the problem, I want to confirm some information with you first  

-  Which is the specific application?  

-  Is this program a tripartite program?  

According to these questions, analysis can be carried out  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-13*

The highest domain functional level even with 2019 domain controllers is 2016. As to application compatibility the developer will be your best resource for this information.     

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--
