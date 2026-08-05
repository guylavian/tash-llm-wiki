---
title: "FSMO Owner"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/112515/fsmo-owner
question_id: 112515
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# FSMO Owner

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/112515/fsmo-owner (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Fsmo roles transfared from dc1 2008r2 to DC2 2016  

when i run netdom query fsmo it shows all 5 roles in dc2.  

but when i run  

"dsquery * CN=Infrastructure,DC=DomainDnsZones,DC=mycompany,DC=com -attr fSMORoleOwner "  

the result is  

" fSMORoleOwner  

  CN=NTDS Settings,CN=DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=mycompany,DC=com"  

and when i ask for w32tm query source it answer the DC1 is the source where DC2 should be the pdc emulator holder.  

please help me to fix this.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-01*

Might also check the results below  

`dcdiag /v`

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

@Bourbita  

thanks for your response  

the steps mentioned by Patrick was helpful.  

and the replication completed with no error.  

but the first part still confuses me.  

i will appreciate any help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Patrick  

thanks for your response  

i followed the steps you provided, and the time source now is DC2.  

but the first part confused me, why fsmoRole Owner attribute in infrastructure properties still indicate to dc1 where it should be dc2.  

CN=NTDS Settings,CN=DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=mycompany,DC=com

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-30*

Hi,  

Check the replication health between your domain controllers and the status of windows time service in each domain controller  

As mentioned by Patrick , each domain controller will synchronize with the PDC in same domain. In case where you have a forest with multi child domain , the PDC of each child domain will synchronize with a domain controller in root domain.  

Please don't forget to mark this reply as answer if it help you to fix your issue
