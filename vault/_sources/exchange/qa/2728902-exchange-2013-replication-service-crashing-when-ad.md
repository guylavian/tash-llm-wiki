---
title: "Exchange 2013 Replication service crashing when adding DB copy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2728902/exchange-2013-replication-service-crashing-when-ad
question_id: 2728902
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange 2013 Replication service crashing when adding DB copy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2728902/exchange-2013-replication-service-crashing-when-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

I have installed new 4 Exchange 2013 CU15 servers on windows 2012 R2 with and all servers joined one DAG

I created 6 DB on each server and when I try to create copy databases from server to another copy is done for one server only and the other two servers Microsoft Exchange Replication service crash on target server and keep restarting with
Event ID 7031 appears in event log "The Microsoft Exchange Replication service terminated unexpectedly. It has done this 1 time(s). The following corrective action will be taken in 5000 milliseconds: Restart the service."

when I remove the DB copy the service is running normally.

I tried to restart all Exchange services and reboot the server and still same error

I also tried to clear the event log in the following location:  Applications and Services Logs / Microsoft / Exchange / MailboxDatabaseFailureItems / Operational

Wevtutil.exe cl “Microsoft-Exchange-MailboxDatabaseFailureItems/Operational”    But still same error

Also removed Exchange from one server and reinstall but same error

Print Screens attached

## Answer (community) — community member

*upvotes: 0 · updated: 2017-02-10*

Hi,

Your question is outside the scope of this Community.

I suggest that you repost your Question in the TechNet Exchange Forums.

https://social.technet.microsoft.com/Forums/exchange/en-us/home?category=exchangeserver

And/or here:

https://social.technet.microsoft.com/Forums/exchange/en-US/home?forum=exchangesvrgeneral

TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

Or MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
