---
title: "Domain Controller replication errors and rogue connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189070/domain-controller-replication-errors-and-rogue-con
question_id: 1189070
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller replication errors and rogue connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189070/domain-controller-replication-errors-and-rogue-con (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We have recently recovered a domain from a major diaster, and I'm performing some troubleshooting on the domain controllers. I've encountered some errors I'm not certain how to deal with.

Different tests (repadmin, dcdiag) show some errors. What is at this moment the most intriguing, is are the NTDS settings in the AD Sites and Services. We have a site, let's call it SiteZ, with one DC inside it. SiteZ is included in only one IP Site Link. The second site in that link is what we can call SiteAzure. When I look at the NTDS settings of the DC in SiteZ, I see connections not only to SiteAzure, but also <automatically generated> connections to 5 other sites. Sites that SiteZ is not linked to. And there are some mysteries:

-  why are those connections <automatically generated> when there is no site link in place?

-  can those link be safely deleted?

- 

I also noticed that some connections appear to be "missing". For example, if I have SiteA with one DC, which is linked to SiteAzure which has 2 DCs, I would assume that there would be two connections - one for each server in SiteAzure. Instead, I have one connection to a DC in SiteAzure, and one connection to a DC in another site, not linked to SiteA. Some pretty weird stuff is going on and I'm trying to figure out how to clean this up...

I tried running repadmin /kcc but it did not make any changes.

Any help is greatly appreciated.

Kind regards,

Wojciech

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-13*

Ok, well it still is unclear what was done, but this one could help.  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/orphaned-child-domain-isnt-replicated  

if it was a single domain controller in a domain that was restored then this is not a recommended method. Better option is to seize roles to a healthy one (if necessary)   

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds  

then perform cleanup to remove remnants  

Clean up Active Directory Domain Controller server metadata  

Step-By-Step: Manually Removing A Domain Controller Server  

then stand up a new one for replacement.  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-13*

We have recently recovered a domain from a major diaster  

Any details here?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-13*

And another question.

I see frequent 1865 events:

The Knowledge Consistency Checker (KCC) was unable to form a complete spanning tree network topology. As a result, the following list of sites cannot be reached from the local site. 

Sites: 

CN=SiteX,CN=Sites,CN=Configuration,DC=xxx,DC=xxx,DC=com 

The thing is, the DC where those events appear is not in link with that site. The topology is:

SiteAzure <----link----> SiteB

SiteB <----link----> SiteX

Interestingly enough, when I run repadmin /showrepl on a DC in SiteAzure, all looks ok and I do not see any reference to SiteX. But if on the same DC I perform a repadmin /replsummary I get this error:

Experienced the following operational errors trying to retrieve replication information:

58 - DC.from.siteX

Is this normal?

Best regards,

Wojciech

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-03-13*

All DC's do not necessarily create kcc links to all other DC's in other sites.   

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755994(v=ws.10)?redirectedfrom=MSDN  

-  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
