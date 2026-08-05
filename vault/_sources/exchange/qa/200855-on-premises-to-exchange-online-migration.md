---
title: "On-premises to Exchange online migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200855/on-premises-to-exchange-online-migration
question_id: 200855
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# On-premises to Exchange online migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200855/on-premises-to-exchange-online-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello there, I wanted to know what happens when we start to migrate a mailbox from on-premises to exchange online; like what is the chronology of the movement?  

I've gone through a few Microsoft articles, but it has information about how to do migration, however I could not find the info which mentions the process like when we start to migrate a mailbox what are the steps/stages a mailbox goes through. Like if endpoints are created, what service/functionality/protocol it uses to create the connections and how data flows, etc.  

If someone has a reference to any useful links, please guide me to them as well.  

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

Hi @Nasir Syed      

According to your information above, you want to know what happens to the mailbox when migrating to o365, including what services or protocols are used in this process.    

Generally official document lists the steps to tell us how to perform the migration, not telling much about the backend process for the mailbox during migration.    

What migration method are you going to use? Do you have a hybrid environment? We can refer to this official document to determine which way to use: Ways to migrate multiple email accounts to Microsoft 365 or Office 365    

I found an article below introduces about the MIGRATION ENDPOINTS and some related services for your reference as well:    

UNDERSTANDING OFFICE 365 EXCHANGE ONLINE MIGRATION ENDPOINTS    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
