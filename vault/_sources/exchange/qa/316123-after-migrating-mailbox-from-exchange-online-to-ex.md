---
title: "After migrating mailbox from Exchange Online to Exchange 2013, users are facing webmail login issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/316123/after-migrating-mailbox-from-exchange-online-to-ex
question_id: 316123
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# After migrating mailbox from Exchange Online to Exchange 2013, users are facing webmail login issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/316123/after-migrating-mailbox-from-exchange-online-to-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hybrid Exchange | After migrating mailbox Exchange Online to Exchange 2013, users are facing webmail login issue   

Below is the error,  

An unexpected error occurred and your request couldn't be handled.  

X-ClientId: MCLC - NA9G - EKFB - KYNGG  

X-OWA-Error: SDServerErr;System.ArgumentException  

X-OWA-Version: 15.0.1497.12  

X-FEServer: EXCH02  

X-BEServer: bbl-exch01.bd.example.com  

Date: 3/14/2021 12:12:05 PM

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-20*

Ok, I have seen this before when you offboard mailboxes back to on-prem, why the need to do that?  

There is most likely some metadata in the mailbox properties that still point to 365. The tough part is determining what that is and how to fix it.   

If its just one user, can you export everything to a pst via Outlook and create a new mailbox for the user and import back in?  

You might get lucky and this will work:  

```
Set-Mailbox username -ApplyMandatoryProperties
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

@Al Amran      

I would suggest you create a new mailbox on Exchange on-premises, then check whether is this issue only occurs on migrated mailbox.    

If this issue also occur on the new created mailbox, I think this issue is related with OWA configuration, we need to troubleshoot from OWA side. Such as recreate OWA virtual directory.    

If this issue only occur on migrated mailbox, try to migrate mailbox to another database as AndyDavid said, the migrate could repair some issue on mailbox.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
