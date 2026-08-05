---
title: "Active Directory virtualization safeguard  support"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/854525/active-directory-virtualization-safeguard-support
question_id: 854525
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory virtualization safeguard  support

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/854525/active-directory-virtualization-safeguard-support (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello     

I am studying about DC backup and restore. Please correct me if I am missing something or wrong.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/introduction-to-active-directory-domain-services-ad-ds-virtualization-level-100    

"Beginning with Windows Server 2012, AD DS provides greater support for virtualizing domain controllers by introducing virtualization-safe capabilities. "    

From above link, I can not confirm Virtualization based safeguards support requirement is Win server 2012 only or domain level win 2012 instead.    

Why I ask this, because I can find generationid in AD attribute on win2012. I mean I know the way. But I can not found it on  Win server 2016 with domain level win2008.    

Group all information I found, I can have below way to restore AD, please correct me if I am wrong.    

-  use windows backup to backup system state, the use wbadmin to restore.    

-  if no system state but restore vm without generationID support, boot to DSRM and follow "To restore a previous version of a virtual domain controller VHD without system state data backup"to restore.    

-  as my question, Win2012 support virtualization safeguard     

-  Veeam can perform non-authority completely automatic.    

Thanks for your reply.    

Regards.    

Scott    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd363553(v=ws.10)?redirectedfrom=MSDN

## Answers

_No answers on this thread._
