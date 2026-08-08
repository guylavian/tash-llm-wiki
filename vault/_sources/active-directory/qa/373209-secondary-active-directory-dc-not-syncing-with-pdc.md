---
title: "Secondary Active directory DC not syncing with PDC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373209/secondary-active-directory-dc-not-syncing-with-pdc
question_id: 373209
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Secondary Active directory DC not syncing with PDC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373209/secondary-active-directory-dc-not-syncing-with-pdc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

All of a sudden our Secondary Secondary DC stopped syncing with Primary DC for a long time.  

When I checked the network information by "Network & Sharing Center", I could not see our domain name (ourcomany.com). It was showing me 'Network' in place of domain name.  

The time of Secondary DC was different from PDC.  

I could ping both of them.  

After updating the Windows Server 2012 (Secomdary DC), it now shows our domain name (ourcompany.com). The time also syncs with the PDC and now the time is OK.  

But still the Secondary DC cannot sync with the PDC.  

I am sharing the warning below:  

```
The DFS Replication service stopped replication on volume C:. This occurs when a DFSR JET database is not shut down cleanly and Auto Recovery is disabled. To resolve this issue, back up the files in the affected replicated folders, and then use the ResumeReplication WMI method to resume replication.

Additional Information:

Volume: C:
GUID: 8786F330-B944-11E5-93E7-806E6F6E6963

Recovery Steps

1. Back up the files in all replicated folders on the volume. Failure to do so may result in data loss due to unexpected conflict resolution during the recovery of the replicated folders..

2. To resume the replication for this volume, use the WMI method ResumeReplication of the DfsrVolumeConfig class. For example, from an elevated command prompt, type the following command:
wmic /namespace:\\root\microsoftdfs path dfsrVolumeConfig where volumeGuid="8786F330-B944-11E5-93E7-806E6F6E6963" call ResumeReplication

For more information, see http://support.microsoft.com/kb/2663685.
```

Will I follow the above steps to resolve the issue or you have any other solution?  

Please assist.  

Thanks & regards

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-30*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-27*

I'd start by checking role holders  

`netdom /query fsmo`  

to see if the problematic one holds any roles.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-27*

The simplest solution may be to move roles off, demote, reboot, promo the problematic one again.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-04-27*

for a long time  

How much time? has it tombstoned? You could try the mentioned steps. https://support.microsoft.com/en-us/topic/changes-that-are-not-replicated-to-a-downstream-server-are-lost-on-the-upstream-server-after-an-automatic-recovery-process-occurs-in-a-dfs-replication-environment-in-windows-server-2008-r2-beb3536b-41db-8ae2-d360-b23194de32bc  

or in case it has exceeded tombstone time you could move roles off, demote, reboot, promo it again.  

--please don't forget to Accept as answer if the reply is helpful--
