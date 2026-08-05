---
title: "Exchange 2016 free/busy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/269734/exchange-2016-free-busy
question_id: 269734
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 free/busy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/269734/exchange-2016-free-busy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 DAG with 2 mail servers, and 3 mailbox databases. We started with 2 databases and decided to create a 3rd. All users in the newly created database cannot get free/busy information for the users in the other 2 databases. They can however, see free/busy for the other users who have mailboxes in their database. Users in the other 2 databases can see free/busy for the users in both of their databases, but not the users in the newly created database. All policies are being applied correctly, and Outlook is configured correctly. All users can send and receive mail to each other no matter what database they are in.  Thanks in advance for any help with this.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-12*

Hi @Steve Payne  ,    

Is there any error message when users fail to check the free/busy information in the other databases?    

Any relevant logs in the Event Viewer?    

How about moving one of the users' mailbox from the newly created database to any one of the old databases?    

Besides, it's suggested to try moving the newly created database to the other mailbox server and see how it goes:    

```
Move-ActiveMailboxDatabase  -ActivateOnServer 
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
