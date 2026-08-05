---
title: "decommissioning exchange 2007 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405624/decommissioning-exchange-2007-error
question_id: 405624
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# decommissioning exchange 2007 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405624/decommissioning-exchange-2007-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone, a couple of months ago I migrated an exchange 2007 to 2013. The 2007 server has been off for at least 1 month and the users are not experiencing any problems, it's time to decommission it.  

The problem is that I can't remove the public folders, it always gives me the error "Public Folder \ Public Folder database" contains folder replicas .. etc .. "  

it is a very common problem but I have followed the various guides without finding a solution, I want to clarify that I did not want to migrate the public folders because they have never been used.  

From adsiedit in (CN=Services -> CN=Microsoft Exchange -> CN=(your organization name) -> CN=Administrative Groups -> CN=Exchange Administrative Group (FYDIBOHF23SPDLT) -> CN=Databases) i have no database related to the old server.  

I was thinking of trying to delete all the public folder key using adsiedit, do you think it could be a solution? do I create problems?  

(CN=Services -> CN=Microsoft Exchange -> CN=(your organization name) -> CN=Administrative Groups -> CN=Exchange Administrative Group (FYDIBOHF23SPDLT) -> CN=Servers -> OLDSERVER -> CN=Public folder -> CN=Public folder database)  

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-23*

by deleting ( ...CN=Public folder database) as I said I was able to remove the public folders from the old server.  

Now I want to wait for tomorrow so that I can verify the correct functioning, after which I will uninstall exchange 2007.  

I'll let you know  

thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-24*

All OK.  

Server decommissioned.  

Thank you
