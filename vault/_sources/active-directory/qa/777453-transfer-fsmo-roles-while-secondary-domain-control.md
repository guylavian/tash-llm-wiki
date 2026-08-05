---
title: "Transfer FSMO roles while secondary domain controller is offline"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/777453/transfer-fsmo-roles-while-secondary-domain-control
question_id: 777453
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Transfer FSMO roles while secondary domain controller is offline

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/777453/transfer-fsmo-roles-while-secondary-domain-control (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 domain controllers as below and I planned to transfer the FSMO role while one of the secondary domain controller is off.  

DC1 - FSMO roles holder (ONLINE)  

DC2 - Writable DC (ONLINE) <Going to move role to this domain controller>  

DC3 - Writable DC (OFFLINE) <Not replicating for 3 days and will be online in 2 days after moving this physical server to a new site)  

While DC3 is down, if I transfer the role from DC1 to DC2. What would be the impact and if after 2 days and I power on DC3, it will replicate the changes without any issue? I'm thinking to just reimage it and promote again as a domain controller but to save my time I would like to know if I can just safely power it back on and let it replicate?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-18*

While DC3 is down, if I transfer the role from DC1 to DC2. What would be the impact and if after 2 days and I power on DC3, it will replicate the changes ****without any issue? I'm thinking to just reimage it and promote again as a domain controller but to save my time I would like to know if I can just safely power it back on and let it replicate?

If the DC with FSMO is online , you can transfer FSMO to another online DC without any issue.

The DC3 , will replicate once you start DC3 after 2 days. 2 days is ok because you don't exceed the TombstoneLifeTime.

Please don't forget to mark helpful reply as answer

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-18*

No problem in that case.  As long as the DC is not offline for a very long period.  But 3 days is not so bad.  

When the DC3 will be online, it will replicate changes even if the FSMO roles has moved to another DC.  

You will probably have several warning messages on the other DC's that has replication connector with DC3 but it should be fine.  

Be sure that after DC3 is back online, you validate that everything is working well.  

On DC3, after the 3 days, validate event logs for any error messages and validate the replication on all DC's  

dcdiag.exe /V /C /D /s:%computername% > c:\temp\dcdiag_%computername%.log  

repadmin.exe /showrepl %computername% /verbose /all /intersite > c:\temp\repl_%computername%.txt  

repadmin.exe /replsummary > c:\temp\repl_summary_%computername%.txt  

Also be sure that no computer try to contact DC3 while it's offline.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-18*

If you try to transfer a FSMO role while the FSMO role owner is offline, it will not work.  

The FSMO role owner must be online to transfer a role.
