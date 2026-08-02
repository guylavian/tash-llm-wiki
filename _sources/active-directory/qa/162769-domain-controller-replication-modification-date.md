---
title: "Domain Controller Replication - Modification Date"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162769/domain-controller-replication-modification-date
question_id: 162769
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Replication - Modification Date

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162769/domain-controller-replication-modification-date (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I recently upgraded our domain from 2008 to 2016 however I had some issues with replication on the Sysvol. Initially it was ACL which I found out where related to a duplicated "Domain Admins" created when upgraded. I have resolved that but now on the PDC (holding the PDC, RID and Infrastructure master roles) it is showing the "modification date" is different from the "Basline" which is showing a date from two years ago. However another of the DC's is showing the replication is fine between them.    

DCDiag Error:     

A warning event occurred.  EventID: 0x00000087    

Repladmin:    

No Errors - Successfully in Sync    

Dfsdiag /testdcs:    

No Errors

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-18*

it is now showing as inaccessible    

Did you mean sysvol / netlogon missing?    

FRS    

https://support.microsoft.com/en-us/help/257338/troubleshooting-missing-sysvol-and-netlogon-shares-on-windows-domain-c    

DFS    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-18*

Hi,  

Just checking in to see if the information provided was helpful.  

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-14*

That may be the safer / simpler solution. Stand up a new one for replacement.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-14*

Thanks.  

I did try both a non-authoritative restore and an authoritative restore. I now get an issue on the "ACL" which has reverted back to all the permissions being wrong in the SYSVOL on this DC only. Strange as the other one is fine and the PDC is fine.   

I am debating to decommission this DC and recreate a new 2019 DC this one is a 2016 DC.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-14*

Not clear of the issues. The event logs may provide more details, then this one may also help.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization    

--please don't forget to Accept as answer if the reply is helpful--
