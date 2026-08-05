---
title: "Error Demoting Server 2008R2 Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/465533/error-demoting-server-2008r2-domain-controller
question_id: 465533
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Error Demoting Server 2008R2 Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/465533/error-demoting-server-2008r2-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our domain has a working 2019 Standard domain controller.  When I ran DCPROMO to remove a 2008 R2 domain controller, I received this error:      

Active Directory Domain Services could not transfer the remaining data in directory partition DC=ForestDNSZones,DC=ourdomain,DC=com to \OUR2019SRVR.ourdomain.com    

A dsquery I ran references a server no longer part of the domain:      

CN=NTDS Settings\0ADEL:764e2527-7deb-4368-aeaa-a522d42264b5,CN=OLDSERVER\0ADEL: 99118ba6-6bfa-4ae4-a825-a569473329d4,CN=Servers,CN=Default-First-Site-Name,CN=Si tes,CN=Configuration,DC=ourdomain,DC=com    

I wasn't sure if I should run the fixfsmo.vbs script I found at:    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/identity/error-run-adprep-rodcprep-command    

I'm not well versed in scripts and wasn't 100% certain if this would replace the reference to the old server with our current DC that holds all FSMO roles, and allow DCPROMO to work.  Any ideas or suggestions greatly appreciated.    

Thanks,    

Mike

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-11*

should just remove any of the 2008 server references in DNS  

Yes, remove the records.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-07-07*

Hello @Mike N  ,    

Thank you for posting here.    

To better understand your question, please confirm the following information at your convenience.    

-  Is your AD forest single forest with single domain or multiple domains?    

-  If your forest is single forest with multiple domains, how many domains are there?    

-  What is forest functional level and domain functional level?    

-  How many DCs are there in the same domain as this 2008R2 Domain Controller? Please run command nltest /dclist:domain.com to check.    

-  Which DC holds the FSMO roles? Please run command netdom query FSMO to check.    

Meanwhile, here is a document that similar to your issue. You can try the resolution within the link.    

DCPROMO demotion fails if it's unable to contact the DNS infrastructure master    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcpromo-demotion-fails    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-07*

This one may help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/dcpromo-demotion-fails    

Worst case you should be able to seize roles to another healthy domain controller.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove the remnants.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-07*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
