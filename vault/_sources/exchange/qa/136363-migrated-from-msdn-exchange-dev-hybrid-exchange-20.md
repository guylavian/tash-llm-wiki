---
title: "[Migrated from MSDN Exchange Dev]Hybrid Exchange 2010 upgrade 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/136363/migrated-from-msdn-exchange-dev-hybrid-exchange-20
question_id: 136363
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev]Hybrid Exchange 2010 upgrade 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/136363/migrated-from-msdn-exchange-dev-hybrid-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi here is a question I am unable get done properly.

Our current exchange environment consist of a pair of each exchange 2010 role.Total 10 server. Mbx is dag mode. Hybrid configuration wizard is ran earlier in one of hub tansport.

We have office 365 with around 5000 mbxs, onprem have almost 2000 mbx.Now management need to install 2 band new exchange 2016/ 2019 servers and move all on-prem mailboxes to that. & decommition all 2010 servers

Is ther a best practice / step by step guide for the process ?

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/a8b1dac3-9c81-41f7-85ba-e7cdc76353ee/hybrid-exchange-2010-upgrade-2016?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-23*

Exchange 2019 cannot coexist with Exchange 2010. So, you should migrate to Exchange 2016 first:    

-  Update Exchange 2010 at least to SP3 RU 11.    

-  Install Exchange 2016 coexist Exchange 2010.    

-  Configure 2016 service URLs, such as ECP, OWA, etc.    

-  Switch public DNS records point to Exchange 2016 then rerun HCW on Exchange 2016.    

-  Migrate mailboxes from Exchange 2010 to Exchange 2016.    

-  Remove Exchange 2010 DAG and uninstall Exchange 2010.    

The steps for migrating from Exchange 2016 to 2019 are similar with steps from Exchange 2010 to Exchange 2016.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
