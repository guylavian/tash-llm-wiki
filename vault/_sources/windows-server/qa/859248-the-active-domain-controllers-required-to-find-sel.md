---
title: "the active domain controllers required to find selected objects in the following domain are not available"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/859248/the-active-domain-controllers-required-to-find-sel
question_id: 859248
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# the active domain controllers required to find selected objects in the following domain are not available

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/859248/the-active-domain-controllers-required-to-find-sel (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My setup is    

pizza.local (old domain Windows 2008 R2 functional level)     

eu.pizza.local    

uk.pizza.local    

us.pizza.local    

ad.pizza.com (new domain Windows 2016 functional level)    

Active Directory Two-way, transitive forest trust between two Active Directory forests.    

I want to share a folder in a server from pizza.local to the users from ad.pizza.com but I receive the same error like:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/rpc-endpoint-mapper-prevents-users-added-to-trust-forest    

I can ping and resolve DNS without issues and If I try to share a folder from ad.pizza.com with pizza.local users it works.     

Any suggestions?    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-23*

Hi  

Yes, I created conditional forwarders on both Domain controllers and replicated them to all servers.  

The Name Suffix Routing  

For pizza.local  

pizza.com	disabled	conflicting  

pizza.de	enabled  

pizza.local	enabled  

pizza.net	enabled  

For ad.pizza.com  

pizza.com	disabled	conflicting  

pepperoni.com	disabled  

I just moved some users from pizza.local to ad.pizza.com.  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-22*

Some ideas here.  

https://social.technet.microsoft.com/forums/windowsserver/en-US/13407b54-cfcd-4f8a-b6d1-f4a1eef0cd30/quotthe-active-domain-controllers-required-to-find-selected-objects-in-the-following-domain-are?forum=winserverMigration  

https://social.technet.microsoft.com/Forums/en-US/fc14ed76-3f43-4fa7-be73-b5237fe61638/trust-error-when-adding-groups?forum=winservergen  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
