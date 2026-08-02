---
title: "Domain Controller ports"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/908574/domain-controller-ports
question_id: 908574
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller ports

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/908574/domain-controller-ports (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All    

i have two Writable  Domain Controllers and i have setup new RODC in DMZ network.  now all the ports are blocked from the network side. I want to Allow communication between writeable domain controllers and RODC.  Do all the ports in the below MS article needs to be allowed. Should these ports be bidirectional i.e from RODC to Writeable DCs or from Writeable DCs to RODC. Currently there is no replication happening between the Writeable DCs and RODC. During the initial setup only all the ports were allowed.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-30*

is the below article applicable to windows server 2019    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd728028(v=ws.10)?redirectedfrom=MSDN

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-30*

unidirectional or bidirectional

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-29*

Yes, you should allow the ports listed in the document.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
