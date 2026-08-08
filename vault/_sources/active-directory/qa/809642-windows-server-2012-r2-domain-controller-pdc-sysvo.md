---
title: "Windows Server 2012 R2 Domain Controller PDC Sysvol Journal Wrap Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/809642/windows-server-2012-r2-domain-controller-pdc-sysvo
question_id: 809642
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server 2012 R2 Domain Controller PDC Sysvol Journal Wrap Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/809642/windows-server-2012-r2-domain-controller-pdc-sysvo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have few domain controllers in my environment which consists of Windows Server 2012 R2 and Windows Server 2003. PDC is Windows Server 2012 R2. I've recently just take over this infrastructure and by checking at it I've no idea who stopped the FRS service for more than 1 year.     

In this case I can see all the SYSVOL is not replicating among members and only the latest set is in the PDC. When I started the service it shows Journal Wrap error on the PDC. I've backed up the entire SYSVOL folder and performed registry to enable automatic restore but it moved all my existing SYSVOL folder to Preexisting.     

Seems like this is not working so I am thinking to perform a authoritative restore on the PDC and nonauthoritative restore on other domain controllers.    

Can I just follow this URL to perform this restore or any other steps required?    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-17*

Issue has been resolved by performing the SYSVOL restore using registry for D4 and D2. Thank you.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-12*

I've no idea who stopped the FRS service for more than 1 year    

You can try but it sounds like a tombstoned situation in which that one will need to be rebuilt from scratch. Seize roles (if necessary)     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then do cleanup prior to rebuild.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
