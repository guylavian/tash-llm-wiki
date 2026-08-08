---
title: "Reverting Migration Exchange 2010 mailbox from backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1077069/reverting-migration-exchange-2010-mailbox-from-bac
question_id: 1077069
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Reverting Migration Exchange 2010 mailbox from backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1077069/reverting-migration-exchange-2010-mailbox-from-bac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone    

I am in the middle of migrating users from Exchange 2010 to Exchange 2019.  The process went well for most of my users, 43 out of 65 then the Exchange    

2019 database dismounted. It would not let me manually mount it. Before running any tools to see if the database was corrupted or not, I rebooted the Exchange 2019 server.  That is when I discovered it was not software, but a hardware issue.  Two of the six hard drives on the raid-5 failed.     

I am in the middle of rebuilding the Raid drive.  I am hopeful that will work, but in the event it does not, I have a question. I have a backup of the exchange    

2010 database just prior to the migration and a full metal backup of the exchange 2016 the day before the migration.  If it is not possible to recover the exchange 2016 hardware, what steps do I need to perform to allow the users mailboxes of the exchange 2010 server back to the state they were in before the migration?    

Thank you for your time.    

Wendell Jones

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-10*

Hi @Wendell Jones   ,    

Thanks for your feedback above which shared more information and glad to know that your issue is resolved now! Since our forum has the policy that The question author cannot accept their own answer. They can only accept answers by others, and according to the scenario introduced here: Answering your own questions on Microsoft Q&A    

I would make a brief summary of this post so that other forum members could easily find useful information here:    

[Reverting Migration Exchange 2010 mailbox from backup - Summary]    

Issue Symptom:    

Problems with mailbox migration, hard drive failure    

Solution:    

Migrate mailboxes to the cloud    

You could "Accept Answer" for this summary to close this thread, and your action would be helpful to other users who encounter the same issue and read this thread. Thanks for your understanding!    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-09*

The raid drive was unsalvageable.  So we improvised.  Used Azure AD Connect to push out the mailbox guid information to the cloud, Had all of the users make a duplicate of their outlook client data, imported those into the cloud.  They are up and running.  All the users on the 2010 machine, we used Bittitan and are moving them to the cloud.  Made some changes to the cloud exchange service and we are moving.  These are just broad strokes, I did not do the work.
