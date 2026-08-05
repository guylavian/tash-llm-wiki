---
title: "Promote Domain Controller into current Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/459596/promote-domain-controller-into-current-domain
question_id: 459596
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Promote Domain Controller into current Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/459596/promote-domain-controller-into-current-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have just built a server and need to join it to our existing Domain. The server is W2016.  

I have promoted servers in the past. I am stuck at the point where it asks for the site name. I am not 100% sure but on my previous builds I think I chose the option Default-first-site-name, however, I am not sure what will happens during this process. Does it populate anything in sites and services.  

Please could someone offer any advice as to what I need to chose at this point during the promotion.  

Any information would help greatly.  

Regards.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-01*

The prerequisite before introducing the first 2016 domain controller: domain functional level needs to be 2003 or higher    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-09*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-01*

Hi，  

From my side, i will check how many sites are there and the subnet configuration in my domain, you can check that through AD Site and Service:  

If there is only the Default-first-site, you can select the option.  

If there are also other sites you created before, you have to decide which site you want to put the dc into.  

Or you can just select the Default-first-site-name, and then change the site for the new DC after the promotion.  

Then the new DC will provide authentication and DNS resolution for clients in the same site with it.  

Following link for your reference:  

Setting Up Active Directory Sites, Subnets – Site-Links  

https://easycentercorp-practicemanager.com/setting-up-active-directory-sites-subnets-site-links/  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,
