---
title: "Exchange 2016 (database count/drive space)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238319/exchange-2016-database-count-drive-space
question_id: 238319
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 (database count/drive space)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238319/exchange-2016-database-count-drive-space (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,  

Recently I have noticed that drive space on one of the Exchange databases is slowly dropping.  The Exchange Full backups are running as expected and circular logging is off.  The mailbox counts on this database is close to what the others have so it appears to be a pretty even spread, but for this particular database it has far less space available while all the other databases have very high percentages giving us a lot of wiggle room.  

I know that moving mailboxes from the database with low space does not just free up drive space on the servers impacted, so what is the appropriate fix to increasing the drive space availability on this database/server and creating a more balanced environment?  

Thank you for any input you you may have,  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Thanks Andy.  

Much appreciated sir.  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Morning Andy,  

Unfortunately we do not have space at this point on the DB/Server we are low on to create a new database.  Do you think moving any arbitration mailboxes we have on the problematic DB/Server would free up space?  Can moving mailboxes from this server to other ones help free up space on this one?  

Thanks for the reply (wish this was an option).  Crazy thing is that the counts are very balanced across them all, but ofcourse sizes of each mailbox are clearly not :o)  

CWT
