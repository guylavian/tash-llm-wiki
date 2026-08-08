---
title: "exchange public folder 2010 decomissioning and exchange 2010 decomissioning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/219007/exchange-public-folder-2010-decomissioning-and-exc
question_id: 219007
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange public folder 2010 decomissioning and exchange 2010 decomissioning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/219007/exchange-public-folder-2010-decomissioning-and-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,

i have 4 exchange 2010 servers : 2 in main, 2 in DR.  

mailflow and mailboxes are migrated to 2016. we need to decomission exchange 2010 servers.

below the components: in each site, we have two mailbox server and one two hub transport servers.  

public folder db is replicated within all the nodes.

1) please advise on how to decomission the public folders dbs in order to decomission all exchange servers  

2) do we need to create the transport rules created on 2010 on 2016 before demcomissioning?

thank you in advance  

appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

You need to check the Public Folder Replica's first before removing the Public Folder,   

http://exchangeserverpro.com/exchange-2010-remove-public-folder-database  

or you can delete from ADSI Edit.  

You can check this article for decommissioning exchange server:   

https://community.spiceworks.com/how_to/165831-how-to-decommission-exchange-server-after-migration

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-05*

thanks for replying  

first of all i am not using anymore the public folders thus i dont have to migrate any.  

" then you can use MoveAllReplicas.ps1 script to move all replicas to one PF database": regarding this, if i have already one pf db that has 2 replicas then each replica has pf db right or this is wrong? we dont have pf dbs on the target servers just a replica?  

let's start by this  

thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-05*

Hi @eg1995   ,

Please find the below suggestions,

1.You can migrate public folders to 2016 - https://learn.microsoft.com/en-us/exchange/collaboration/public-folders/batch-migration-from-previous-versions?view=exchserver-2016  

Incase if you don't want to migrate to Exchange 2016 and remove it before the decommission, then you can use MoveAllReplicas.ps1 script to move all replicas to one PF database. Use Remove-PublicFolder to remove it from that last server and finally the PF database  

https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2010/dd876883(v=exchg.141)?redirectedfrom=MSDN  

2.You can export/import Transport rule if it is not already created by the setup

https://techcommunity.microsoft.com/t5/exchange-team-blog/best-practices-when-decommissioning-exchange-2010/ba-p/1247559  

https://learn.microsoft.com/en-us/exchange/policy-and-compliance/mail-flow-rules/mail-flow-rules?view=exchserver-2019#how-mail-flow-rules-are-applied

If the above suggestion helps, please click on "Accept Answer" and upvote it
