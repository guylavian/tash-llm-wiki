---
title: "New DC Stuck Initial Sync Sysvol folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/479246/new-dc-stuck-initial-sync-sysvol-folder
question_id: 479246
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# New DC Stuck Initial Sync Sysvol folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/479246/new-dc-stuck-initial-sync-sysvol-folder (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We recently add a new DC in a new site, and we have a problem because all replication diags suceed, but we noticied errors in event viewer with GPO unnacessible.     

I have checked the Sysvol folder and the Policies Group is missing ...     

For /f %i IN ('dsquery server -o rdn') do @Echo   %i && @wmic /node:"%i" /namespace:\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state    

Return the DC as "Initial State"     

I have tried to follow this procedure : change msDFSR Enabled=FALSE  replications and DFSRDIAG POLLAD but still stuck at initial Sync.    

All controller are on 2019 Server Standard, and no issue with replications except this folder policies..     

Is there a way to proper recreate the SYSVOL folder with scripts & policies ?    

Thanks !    

Steph

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-21*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-19*

Hi,  

Based on my understanding, only the new DC can't get the Sysvol synced from other DCs, right?  

Did you check the status of the new DC by running: Dcdiag /v >c:\dcdiag1.log?  

If only the issue for the SYSVOL replicaiton, as DSPatric mentioned above, we can consider the method: non-authoritative synchronization for DFSR-replicated sysvol replication on the new DC.   

If there are any progresses, welcome to share here!  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-16*

A couple of options are a non authoritative synchronization  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

or also try moving roles off, demote, reboot, promo the problematic one.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
