---
title: "[Migrated from MSDN Exchange Dev] Microsoft Exchange 2016 - Cutover migration move or copy?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153825/migrated-from-msdn-exchange-dev-microsoft-exchange
question_id: 153825
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Microsoft Exchange 2016 - Cutover migration move or copy?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153825/migrated-from-msdn-exchange-dev-microsoft-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/c206360b-3f5f-44db-91b8-823087bda4e6/microsoft-exchange-2016-cutover-migration-move-or-copy?forum=exchangesvrdevelopment   

Hi there,  

I have a quick question, our organization is planning to migrate from on-prem Exchange 2016 to Office365. My question here is that If we do a cutover migration, does that move or copy our data to Office365? In other people tutorials, I see that the mailboxes are copied to the destination. If that's the case, will I be able to route MX record to old server if anything goes wrong? as a part of Disaster Recovery?  

Many thanks!!!

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-11-06*

For cutover migration, yes, data will be copied to O365. In general, after changing the MX record and Autodiscover configuration, you can use the on-premises mailboxes. However, new data generated after the migration won't be available, we have to use pst files to export and import those items.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
