---
title: "Exchange 2013 / OAB not working anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/395720/exchange-2013-oab-not-working-anymore
question_id: 395720
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 / OAB not working anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/395720/exchange-2013-oab-not-working-anymore (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

We have (5) vm's running Exchange 2013 cu21. Two of them are used for CAS role (One to the production site one to the DR) and the other remaining three are mailbox servers. Two of them are located to PR site and one of them to the DR. What is the problem... OAB stopped working from all Outlook clients (Outlook 2016/2019).  The outlook error is Task' ******@companydomain.com' reported error 0x80072F06: 'Unknown error 0x80072F06'  

Could you please let me know what i have to check first?  

Thank you  

George

## Answer (community) — community member

*upvotes: 1 · updated: 2021-07-14*

I had the same, creating a new offline address book solved the problem.  

thanks to ZhengqiLou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-21*

Sorry for the delay of my response  

I tried before posting the question the steps 1,2 and 3 nothing much happened.  

Then i tried step 4 and it worked. I created a new OAB and attached it to the database. After a few minutes i went to an outlook client and i run test autoconfiguration. The url of OAB was pointing to the correct (new) offline address book. I went to send/receive and manually i tried to download the address book. It worked  

Thank you
