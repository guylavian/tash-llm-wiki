---
title: "Rebuilding crashed Domain Controller - is it worth it?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/170873/rebuilding-crashed-domain-controller-is-it-worth-i
question_id: 170873
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Rebuilding crashed Domain Controller - is it worth it?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/170873/rebuilding-crashed-domain-controller-is-it-worth-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, we recently had a 6-hour long power outage at one of our sites due to inclement weather and the domain controller got corrupted. When it came back on-line the DNS got corrupted, some of the OUs were also missing. It happened at a site that only has a single DC and some security appliances and no backups. As a quick workaround we configured DHCP to use DNS from another site.   

Do you think it would be worth trying demoting the DC during maintenance window, removing from domain, joining to domain, promoting as DC, importing DHCP and forcing replication or just building a new DC from scratch? What would be recommended steps for rebuilding a corrupted DC?   

Thank you!

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-11-21*

I probably would not spend much time with it.    

If necessary you can perform cleanup.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

Then rebuild it. I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health.    

--please don't forget to Accept as answer if the reply is helpful--
