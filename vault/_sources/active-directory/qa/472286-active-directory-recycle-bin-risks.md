---
title: "Active Directory recycle bin risks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/472286/active-directory-recycle-bin-risks
question_id: 472286
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory recycle bin risks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/472286/active-directory-recycle-bin-risks (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We activated AD recycle bin in my organization and we didn't really like it.  

We wanted to change it to be "disabled" but I read in a few article that the action is irreversible, so we later on figured we could just set the tombstone lifetime to 1, so we can get rid of the objects fast.  

I wanted to ask a few questions about it before we take any action:

-   We changed the lifestyle tombstone to 1, wait are the risks regardless of this action, I heard that we might have some issue incase 1 of our DC's will go down for more then the tombstone lifetime.

-   When does it start the count down? (after setting it to 1 it didn't delete items that been there for weeks).

-   What else do I need to know about AD recycle bin? I got no experience with that at all.    Thanks in advance, Raz.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-12*

Hi.  

the tombstoneLifetime value does not govern what happens to the objects in the Recycle Bin, msDs-deletedObjectsLifetime does. Once that number of days has expired, the objects are tombstoned for tombstoneLifetime days and then purged physically by garbage collection.  

So go ahead and set tombstoneLifetime to a higher value to prevent the USN rollback type problems from occurring but lower msDs-deletedObjectsLifetime to 1 to have deleted objects disappear from the Recycle Bin more quickly.  

Out of curiosity: What is it that you 'didn' like' about the Recycle Bin?
