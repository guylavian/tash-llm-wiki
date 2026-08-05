---
title: "Exchange Server DAG, DB GUID info missing from registry on one of my three servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1275303/exchange-server-dag-db-guid-info-missing-from-regi
question_id: 1275303
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server DAG, DB GUID info missing from registry on one of my three servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1275303/exchange-server-dag-db-guid-info-missing-from-regi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have inherited a three server Exchange 2016 DAG running on 2012 R2.

We have two DBs(old) on one drive and we created two new DB's on different drives to move to.  

So one of the changes was to increase the DB size threshold in reg.

I went in to the registry on my Primary srv1 to make the reg change to increase the DBs size threshold. 

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MSExchangeIS\ServerName\Private-GUID\  

Restarted services and it was populated to one of my secondary's srv2 but not the other srv3. 

I open the key up I on srv3 and I only see two entries, the two missing are the new DB's created about 3 months ago.

If we never actually failed over to srv3 would it not have the reg keys for the DBs?

Do we need to make it Primary to get the GUID entries?

I have never seen an issue like this and before I start testing things I wanted to get some opinions.  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-03*

Hi @ Larry Desmond ,

Typically, when you change this registry, the change is propagated to all servers that host copies of this database.

I recommend that you could recreate these two new database copies in Srv3 to see if the issue persists.

If it is still not synchronized, it is recommended that you run Test-ReplicationHealth and check the event log for any messages indicating a problem that might prevent the GUID update for the new database.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
