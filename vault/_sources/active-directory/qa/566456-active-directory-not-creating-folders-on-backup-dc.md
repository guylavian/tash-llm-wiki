---
title: "Active directory not creating folders on backup DC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/566456/active-directory-not-creating-folders-on-backup-dc
question_id: 566456
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Active directory not creating folders on backup DC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/566456/active-directory-not-creating-folders-on-backup-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am having the issue that when I created a new GPO on the primary 2012 DC the GPO gets created on both primary and backup DC but the GPO folder  on the backup DC does not get created. When I try to edit the GPO on the backup DC it says folder missing.  

I have checked permissions and all look OK on folders.  

There are no errors I can see and dcdiag returns ok.  

Thanks for any help

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-28*

Hello JulianHaines,    

Domain controllers will not service authentication requests during the procedure. Only when the SYSVOL and NETLOGON folders are shared again will the domain controller authenticate requests. This procedure should not be performed during peak hours.    

We strongly recommend that you monitor FRS performance and health by using monitoring tools. By using monitoring tools, you may prevent the need for replica set authoritative and non-authoritative restores. Also, by using monitoring tools, you may provide insight into the root cause of FRS failures.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/rebuild-sysvol-tree-and-content-in-a-domain    

----------------------------------------------------------------------------------------------------------------------------    

Hope this answers all your queries, if not please do repost back.     

If an Answer is helpful, please click "Accept Answer" and upvote it : )

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-26*

Might check the DFS Replication event log for errors.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
