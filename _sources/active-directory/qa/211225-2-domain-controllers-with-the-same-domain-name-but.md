---
title: "2 Domain controllers with the same domain name but different subnets"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/211225/2-domain-controllers-with-the-same-domain-name-but
question_id: 211225
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# 2 Domain controllers with the same domain name but different subnets

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/211225/2-domain-controllers-with-the-same-domain-name-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I was faced with this scenario: an enterprise company using 2 domain controllers with the same domain name xyz.com but on different subnets.  

They need to merge these two without stopping any services or losing data on any one of them.   

Is this possible?  

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Thank you for posting in our forum  

You can just install the new server and promote the new server to a DC using the current domain and it will the 2nd DC in the domain.  

But you may also want to transfer the FMSO roles to the more robust server yet making both DC hanging the Global Catalog.  

Users will not be able to see the name of the domain controller but the domain name  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-27*

Hi,  

We need more clarification about the current situation. We can have many domain controllers in same domain.  

 Do you have two domain controllers on same domaine xyz.com or two domain using the same name?  

-  If you have two domain controllers in same domain, you don't need to migrate objects , because all domain controllers in same domain share the same objects. If you need demote one of domain controllers , you should check if there is any FSMO roles hosted on it before demote it.  

-  If you have two domain with same name , you have to rename one of them to be able to migrate it to target domain using ADMt tools because two domain using the same name can create a DNS conflict.   

Please Don't forget to mark this reply as answer if it help you fix your issue

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-27*

@ArwaSh       

Yes merging 2 domain controllers is possible.    

Please go thru below points.    

-  First configure  2-way trust in the new domains is a requirement for domain migration    

-  Migrate resources with Active Directory Migration Tool (ADMT)    

https://www.microsoft.com/en-us/download/details.aspx?id=56570    

-  Migrating Users    

-  Migrating Group policy objects    

-  Migrate files and set permissions    

-  Migrate computer accounts and local user profile    

-  decommission old domain controller    

refer-     

https://thommck.wordpress.com/2010/03/03/how-to-merge-two-small-active-directory-domains-quickly-and-easily/    

https://www.itprotoday.com/windows-78/plan-and-execute-active-directory-merger-part-1    

----------    

Please don’t forget to "Accept the answer" and “up-vote” wherever the information provided helps you, this can be beneficial to other community members.
