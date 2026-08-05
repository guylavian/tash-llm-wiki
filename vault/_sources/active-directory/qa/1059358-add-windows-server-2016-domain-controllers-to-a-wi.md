---
title: "Add Windows Server 2016 Domain Controllers to a Windows Server 2008 R2 Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1059358/add-windows-server-2016-domain-controllers-to-a-wi
question_id: 1059358
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Add Windows Server 2016 Domain Controllers to a Windows Server 2008 R2 Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1059358/add-windows-server-2016-domain-controllers-to-a-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

I have a domain with two Windows Server 2008 R2 domain controllers.    

Windows Server 2008 R2 forest and domain level. There is only one domain in the forest.    

I want to add two new Windows Server 2016 DCs to the domain, transfer the FSMO roles to them, and then uninstall the old Windows Server 2008 R2 DCs.    

Do I have to manually run the "adprep /forestprep" and "adprep /domainprep" commands, or will the graphical installation wizard do it all by itself?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-10-23*

Hi,

No need to launch `adprep /domainprep manually. It wil be lauched automatically when you promote the first domain controller under windows 2016.   Regarding the command`adprep/forestprep` , it can be launched automatically if you will use a account members of enterprise admins and schema admins to promote the first domain controller under Windows 2016 . if it's not the case you have to launched it manually .

*Please don't forget to mark helpful reply answer *
