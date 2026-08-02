---
title: "Exchange 2019 remove recovery database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2029414/exchange-2019-remove-recovery-database
question_id: 2029414
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 remove recovery database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2029414/exchange-2019-remove-recovery-database (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2019

Due to reasons, I created a recovery database and ended up not needing it. 

I got to the point creating the recovery database and doing a soft recovery.

Is there anything I need to do to stop this recovery process before deleting the database to stop Exchange from trying to continue the recovery process? I don't want event viewer filled with errors of it still trying to do the recovery process and wonder where the database is. 

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-02*

Hi,

Welcome to the Microsoft Q&A platform!

To delete the recovery database and stop any associated processes, follow these steps:

Open the Exchange Management Shell and run the following command to dismount the recovery database:

```
Dismount-Database -Identity 
```

After dismounting, you can delete the recovery database using the following command: 

```
Remove-MailboxDatabase -Identity 
```

Make sure there are no active recovery processes running. You can check the event logs for any ongoing recovery operations. If the recovery database is dismounted and removed correctly, you should not see any related errors in the Event Viewer.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer!
