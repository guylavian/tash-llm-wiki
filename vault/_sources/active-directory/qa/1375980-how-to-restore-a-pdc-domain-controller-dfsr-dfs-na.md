---
title: "How to restore a PDC domain controller (DFSR + DFS namespace)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1375980/how-to-restore-a-pdc-domain-controller-dfsr-dfs-na
question_id: 1375980
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How to restore a PDC domain controller (DFSR + DFS namespace)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1375980/how-to-restore-a-pdc-domain-controller-dfsr-dfs-na (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

For days I've had a doubt that I can't "solve", so I decided to explain everything here. 

This is the context of the infrastructure (these are virtual servers): 

Site A: dcA + fileserverA

Site B: dcB + fileserverB 

dcA is the "PDC" in replication with dcB, both are DFS servers for the "\\intranet.domain.com\File Server" namespace which points to fileserverA shares. Furthermore, full mesh replication is active between fileserverA --> fileserverB. 

My question is: if dcA fails and I restore the previous night's backup, once it comes back online, would dcB realign with dcA or, since dcB is a secondary dc, would the replication (of both fileservers and SYSVOL) "breaks" and is not accepted by dcA? I have this doubt because dcB is not a read-only dc and it is not the holder of the FSMO roles... 

Thank you in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-29*

Hi, sorry, there was a misunderstanding. I said "when dcA disappears from LAN, becomes automatically primary domain controller" because of that:

If dcA fails and you restore dcA from backup (system status or full backup) to the domain, dcA will replicate with dcB in the same domain. For AD replication, now dcA is non-authoritative, but dcB is authoritative, dcA will find an authoritative DC (dcB) to replicate.

Anyway, if dcA is offline I must move the FSMO roles to dcB as first and then I can restore dcA. Correct?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-29*

Hi, MA-0049

This is Chaboon.

Hi, thank you both. Just to clarify, so dcB, when dcA disappears from LAN, becomes automatically primary domain controller?

No. If You said "primary domain controller" means FSMO Domain Controller, it does not change to primary domain controller automatically. But, dcB and dcA can perform kerberos authentication in the same way. This is done automatically.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-27*

Hi, thank you both. Just to clarify, so dcB, when dcA disappears from LAN, becomes automatically primary domain controller?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-26*

Hi, MA-0049

This is Chaboon.

I seems, If you restoreed the dcA , do sync the AD replication between to dcB automatically, but do not sync the DFS Replication automatically. There is no relationship between DFSR replication and AD replication.

If you restored dcA, you need to compare the files in SYSVOL Between dcA and dcB. 

You set the newer of the files dcA SYSVOL and dcB SYSVOL as the primary member of DFSR. The primary member is defined as having the most up-to-date data, so it is synchronized before other members.

see below the article:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-26*

Hello MA-0049,  

Thank you for posting in Q&A forum.

If there is issue/error on the FSMO roles holder, usually we will transfer/seize from problematic DC to working DC.  

If dcA fails and I restore the previous night's backup, once it comes back online, would dcB realign with dcA or, since dcB is a secondary dc?

A1: If dcA fails and you restore dcA from backup (system status or full backup) to the domain, dcA will replicate with dcB in the same domain. For AD replication, now dcA is non-authoritative, but dcB is authoritative, dcA will find an authoritative DC (dcB) to replicate.  

After AD replication is complete, you can try to check the AD replication status.  

And you can transfer back FSMO roles to dcA if needed.  

would the replication (of both fileservers and SYSVOL) "breaks" and is not accepted by dcA?

A2: The backup method and restore method about DC, SYSVOL DFSR, DFS namespace are different. If you also restore DFSR and DFS namespace from backup on dcA, you will need to check the DFSN health status and DFSR replication status.  

If there is any problem, you need to try to troubleshoot/fix it.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

==========================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
