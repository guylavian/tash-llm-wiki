---
title: "Moving Domain Controllers to isolated sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/117937/moving-domain-controllers-to-isolated-sites
question_id: 117937
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Moving Domain Controllers to isolated sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/117937/moving-domain-controllers-to-isolated-sites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,  

We are in the process of Active directory modernization where we are upgrading our active directory from 2012 R2 to 2019...part of this exercise is to also find the static IP address that are reaching to the legacy domain controllers before demoting them. The logic behind this is to find the servers which are only reaching out to a single domain controller and update there DNS settings to point to the new 2019 domain controllers...Before doing the demotion we wanted to suppress the DC and check if there are application or services in the environment which are getting effected by it...One way of doing this is to suppress the srv record of the domain controllers but we don't want to do this as we have faced issue with this practice before....The other option that we got to know was about moving the domain controller to an isolated site which will do the replication but will stop the client/server traffic to the domain controller....What we wanted to know was how can we isolate a site and make this happen without firewall or vlan or re-IPing the domain controllers...Please, suggest.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-08*

Hi,    

Thank you for posting in our forum, I see that you have posted the same question in this link, we have provided you with ideas, you can check    

https://learn.microsoft.com/en-us/answers/questions/118165/move-domain-controllers-to-an-isolated-site.html    

Best wishes    

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-06*

How long is your testing going to last? The much simpler method is to just power off the domain controller to check the effect. These tools may also be useful.    

https://learn.microsoft.com/en-us/sysinternals/downloads/adinsight    

https://learn.microsoft.com/en-us/sysinternals/downloads/tcpview    

--please don't forget to Accept as answer if the reply is helpful--
