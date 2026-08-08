---
title: "Unable to remove Exchange database, checked for arbitration & Audit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/291769/unable-to-remove-exchange-database-checked-for-arb
question_id: 291769
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to remove Exchange database, checked for arbitration & Audit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/291769/unable-to-remove-exchange-database-checked-for-arb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I Cannot remove an On-Premise Exchange 2016 CU18 database, no mailboxes (including SoftDelete and Disabled), Arbitration, Archive, AuditLog, Monitoring, PublicFolders and all the others they ask you to check for. The only "mailbox" on this database is the SystemMailbox for this database.   

What have I missed or is there a way to force its removal?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-01*

Hi,    

Have you checked that any failed move request or migration batch exists?    

If nothing left, you should use ADSI edit.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-27*

Unfortunately yes, I have removed dozens of databases in the past and have always been able to remove once I had moved all mailboxes.  

Ideally I would like to remove without the ADSIEdit method, but thank you for the references.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-27*

If you absolutely positive there are NO needed mailboxes on that database, you can delete via adsiedit, though its unsupported and you would need to be careful.   

https://www.petenetlive.com/kb/article/0001414  

https://lonesomehacks.com/2017/05/14/how-to-force-removal-of-exchange-server-mailbox-database/  

Make sure you have accounted for ALL the arbitration mailboxes and they moved to another DB:  

https://blog.rmilne.ca/2018/03/19/arbitration-mailboxes-lay-of-the-land/
