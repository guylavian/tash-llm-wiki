---
title: "SYSVOL DFSR not replicating, not listed in wmic dfsrvolumeconfig"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/817947/sysvol-dfsr-not-replicating-not-listed-in-wmic-dfs
question_id: 817947
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-devices-other", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL DFSR not replicating, not listed in wmic dfsrvolumeconfig

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/817947/sysvol-dfsr-not-replicating-not-listed-in-wmic-dfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is an addendum to the only post on the internet with the same symptoms as what I'm seeing. https://social.technet.microsoft.com/Forums/en-US/a90e17ff-2803-4983-8389-a6b3a8abcd96/dfsr-sysvol-folder-not-replicating?forum=winserverDS#24904895-6af0-4db8-8a4d-ec4b00de508a   

Backstory: coming on as addtl SysAdmin for existing domain, with an unstable baremetal W2019 running every service. Adding a 2nd DC as VM on a new rack revealed the sysvol replication failure exactly as described in the link above. Performing a D4-like authoritative restore doesnt do anything. wmic repeatedly reported "No available instances" for any relevant queries of the original DC.   

Digging in to the debug log, found  

-  Multiple volumes share the same volume serial number which prevents DFSR from finding the right volume  

-  ReadConfigFilePath Location of valueName:Volume Configuration File is location:\.\C:\System Volume Information\DFSR\Config\Volume_DFC14B54-9DC0-4AEC-9E44-BB688F6A2BCC.XML  

Digging further, found that current system (C) was cloned from a partition on the big raid drive (now F). They shared the same serial number, but different volumeGUIDs. The XML above has the GUID from the now F drive in its name.   

Moral of the story - cloning a system drive on a DC can have consequences later. Problem wasnt revealed until we tried to add a 2nd DC for sanity.   

Question: does anyone believe this is recoverable? Could I start poking around in C:\System Volume Information\DFSR and copy/ren/edit the .XML (and quite possibly the registry, AD too), and get all values pointing to legitimate ones?    

This is mostly academic as the lean from all parties is towards massaging the new DC into place with manual copying of sysvol, doing D4 to it not the old server, and demoting the old server once things are confirmed stable.   

Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-05-03*

Doesn't sound good. I'd look for a known good backup, otherwise something here could help.  

https://gist.github.com/awnish25/eab6d4e2eed787a8bbafc317dfbde048  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-19*

No dice - I tried that - problem is there is no GUID for the SYSVOL in wmic. So there's no GUID to call ResumeReplication on. StopReplicationOnAutoRecovery was already 0 on both DCs.   

The issue is that DFSR cant discern the proper volume to reference, so it just bails out.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-19*

In Powershell try: wmic /namespace:\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="<GUID>" call ResumeReplication    

Replication is not resumed automatically in order to give system administrator you opportunity to backup replicated folders before starting recovery.    

If you prefer for replication to resume automatically you need make following registry change:    

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DFSR\Parameters    

StopReplicationOnAutoRecovery = 0    

then in PowerShell: repadmin /syncall    

Take a look at this article: https://learn.microsoft.com/en-US/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization
