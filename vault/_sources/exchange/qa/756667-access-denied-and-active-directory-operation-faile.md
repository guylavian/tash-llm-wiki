---
title: "Access denied and Active Directory operation failed when I try to create a \"user mailbox\" or give user \"send-as\" or \"receive as\" permission for a Distribution Group in Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/756667/access-denied-and-active-directory-operation-faile
question_id: 756667
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Access denied and Active Directory operation failed when I try to create a "user mailbox" or give user "send-as" or "receive as" permission for a Distribution Group in Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/756667/access-denied-and-active-directory-operation-faile (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Active Directory operation failed on… This error is not retriable. Additional information: Access is denied. Active directory response: 00000005: SecErr: DSID-03152DCD, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0    

    

I am getting the above message whenever I am trying to create a "User Mailbox" or give an existed user "send-as" or "receive as" permission for a Distribution Group in Exchange Server. Due to this message, I am not even sure how many service-access might be denied. Help me find a solution, please!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 3 · updated: 2022-03-02*

Known Issue:    

https://support.microsoft.com/en-us/topic/access-denied-when-you-try-to-give-user-send-as-or-receive-as-permission-for-a-distribution-group-in-exchange-server-505822f4-8dca-7b97-d378-c8416553f6d2
