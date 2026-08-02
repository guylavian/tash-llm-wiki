---
title: "Domain Controller has multiple DNS entries (uppercase & lowercase) -- Update did not fix"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/744885/domain-controller-has-multiple-dns-entries-upperca
question_id: 744885
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller has multiple DNS entries (uppercase & lowercase) -- Update did not fix

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/744885/domain-controller-has-multiple-dns-entries-upperca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Mixed 2012 R2 & 2016 environment. The PDC name has upper & lower-case letters (dangit!). Once we added a 2016 domain controller, multiple records were generated for the PDC. I know this is a known issue, but the update did not fix the problem. Unfortunately, the presence of multiple LDAP records seem to confuse AD. On 2016 DCs, I changed the registry entry to use lower-case. The upper-case records remain. I deleted the upper-case records, but they keep coming back. Is there anyway to permanently delete these stale records? I would prefer to not demote my PDC, rename it then promote it.  

Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-24*

Once we added a 2016 domain controller, multiple records were generated     

Actually this was fixed sometime back.    

March 17, 2020—KB4541329 (OS Build 14393.3595)    

Addresses an issue that might cause domain controllers (DC) to register a lowercase and a mixed or all uppercase Domain Name System (DNS) service (SRV) record in the _MSDCS.<forest root domain> DNS zone. This occurs when DC computer names contain one or more uppercase characters.    

so I'd check that the new ones have been patched fully.    

also    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-registers-duplicate-srv-records-for-dc#resolution    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-21*

Maybe the work-around #1 mentioned here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-registers-duplicate-srv-records-for-dc#workaround-1-prevent-duplicate-srv-records    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
