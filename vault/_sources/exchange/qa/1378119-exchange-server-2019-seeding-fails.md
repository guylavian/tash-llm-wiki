---
title: "Exchange Server 2019: Seeding fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1378119/exchange-server-2019-seeding-fails
question_id: 1378119
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange Server 2019: Seeding fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1378119/exchange-server-2019-seeding-fails (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

Two-node DAG, adding the first database copy to EXCH2:

Would you please tell me why this "...connected party did not properly respond..." if this is the newly-installed Win2022/Exch2019 that's not expiriencing any (at least tangible) issues???

I don't see any errors in the logs that could relate to the problem...

Thank you in advance,  

Michael

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-06*

Sorry for the delay - didn't noticed the comment :(

"Does this issue also occur on DB01S if you try to add a copy on EXCH2?" - Yes, it does, but the cause of the issue was rather simple: there was the second ip-address (from another subnet) applied to the EXCH2's network adapter -I had been using that ip during initial setup of the server - and that ip was preventing EXCH2 from connecting to EXCH1 (seems EXCH2 tried to connect to EXCH1 using that another subnet), so please excuse me for the question!

Kael Yao-MSFT, thank you for your help!

Regards,  

Michael Firsov

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-02*

Here it is (when NO database copies are configured, prior to starting the seeding):

DB01S is the default database on EXCH2 that does not need to be replicated to Exch1. 

Should I add a new database copy for EXCH1\DB01 - the new error will be added:

The error is the same as when starting the seeding process.

This lookes strange to me as I've created many configurations like this (2-node DAGs) and have never bumped into the issue like this :(

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-02*

Hi Kael Yao-MSFT ,

Yes, both servers are connected to the same switch, the firewall on EXCH2 is off...
