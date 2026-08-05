---
title: "[Migrated from MSDN Exchange Dev] Node offline - Disaster Recovery Site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138704/migrated-from-msdn-exchange-dev-node-offline-disas
question_id: 138704
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Node offline - Disaster Recovery Site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138704/migrated-from-msdn-exchange-dev-node-offline-disas (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/7b204225-1523-4988-bf8a-f00219633142/node-offline-disaster-recovery-site?forum=exchangesvrdevelopment   

Hi All,  

i try rebuild new Exchange 2013 DR site after server is blow-up, and i make some mistake install new exchange DR and not use Recover Server and now im facing this error after join DR server in DAG server.  

The operation couldn't be performed because object '*\1NSGOV-DR-EX' couldn't be found on '1NSGOV-AD01.1ns.net'.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-26*

How many DAG members do you have?     

Did you remove the old and broken server from DAG and your organization?    

Do you mean you install a totally new Exchange server in the DR site? Is the server name in the error information used for your new Exchange server, or it's the name of the broken one?    

Please provide more information about your organization, so that we can provide more appropriate suggestions.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
