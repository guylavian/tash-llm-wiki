---
title: "exchange hybrid migration - when to change mx records"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/293749/exchange-hybrid-migration-when-to-change-mx-record
question_id: 293749
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange hybrid migration - when to change mx records

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/293749/exchange-hybrid-migration-when-to-change-mx-record (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have started migrating the mailboxes but i have not completed the batches yet . so they mail is in sync (up to 95%) when is the ideal time fore the MX record to be updated Should i complete the batches and wait a few days or can i complete the batches and update MX records all in one shot?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 3 · updated: 2021-03-01*

In a hybrid environment, you can change the MX anytime to point to 365. In fact, I would change before moving mailboxes. then send a test message and verify the on-prem mailbox got it, then move the mailboxes.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-02*

looks like all the users for a particular domain had outlook as being disconnected after the mailbox was moved .  

on-premise exchange is version 2013.   

Any idea why this happened.?  

From what i understand outlook should have reconnected automatically and found the new mailbox on it's own .

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-02*

one of the migrated mailboxes is showing disconnected in outlook client . The Outlook client has been restarted several times.   

How do  we fix it? Do we need to create a  new profile?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-02*

Hi @dirkdigs      

Do suggestions above from Andy help? Yes, we need point autodiscover record to on-premise Exchange server during hybrid environment.    

For On-premise mailbox, it remain use previous autodiscover lookup behavior to find endpoint and access to Exchange.    

For migrated mailbox, autodiscover service will redirect On-premise autodiscover record to Office 365 (autodiscover-s.outlook.com), and access to Office 365.    

If you have migrated all the mailboxes to cloud, you could follow the steps above to change the autodiscover record point.    

In addition, some more links below introduce about the MX record in hybrid for your reference as well:    

MX Records for Exchange Hybrid Deployments .     

Official document here: Transport routing in Exchange hybrid deployments    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-01*

Same thing with autodiscover?
